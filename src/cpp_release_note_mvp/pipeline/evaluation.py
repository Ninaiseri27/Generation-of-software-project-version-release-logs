from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ReleaseNoteEvaluator:
    def __init__(
        self,
        *,
        ground_truth_path: str | Path,
        release_note_path: str | Path,
        matches_path: str | Path | None = None,
    ) -> None:
        self.ground_truth_path = Path(ground_truth_path)
        self.release_note_path = Path(release_note_path)
        self.matches_path = Path(matches_path) if matches_path else None

    def build_payload(self) -> dict[str, object]:
        ground_truth_entries = self._parse_ground_truth_entries(self.ground_truth_path)
        release_note_payload = self._read_json(self.release_note_path)
        generated_entries = self._extract_generated_entries(release_note_payload)
        matches = self._read_matches(self.matches_path) if self.matches_path else []
        metrics = self._compute_metrics(
            ground_truth_entries=ground_truth_entries,
            generated_entries=generated_entries,
            matches=matches,
            match_file_supplied=self.matches_path is not None,
        )

        return {
            "source": {
                "evaluator": "release-note-evaluator-v1",
                "match_mode": "manual" if self.matches_path else "template_required",
            },
            "inputs": {
                "ground_truth_path": str(self.ground_truth_path),
                "release_note_path": str(self.release_note_path),
                "matches_path": str(self.matches_path) if self.matches_path else None,
            },
            "summary": metrics,
            "ground_truth_entries": ground_truth_entries,
            "generated_entries": generated_entries,
            "matches": matches,
            "match_template": self.build_match_template(
                ground_truth_entries=ground_truth_entries,
                generated_entries=generated_entries,
            ),
        }

    @classmethod
    def build_match_template(
        cls,
        *,
        ground_truth_entries: list[dict[str, object]],
        generated_entries: list[dict[str, object]],
    ) -> dict[str, object]:
        return {
            "instructions": [
                "Fill matches with semantic correspondences between generated_id and gt_id.",
                "Use decision=match only when the generated note is supported by the ground truth entry.",
                "Leave uncertain or unsupported generated notes unmatched, and record notes when useful.",
            ],
            "ground_truth_entries": ground_truth_entries,
            "generated_entries": generated_entries,
            "matches": [
                {
                    "generated_id": "",
                    "gt_id": "",
                    "decision": "match",
                    "notes": "",
                }
            ],
        }

    @classmethod
    def _compute_metrics(
        cls,
        *,
        ground_truth_entries: list[dict[str, object]],
        generated_entries: list[dict[str, object]],
        matches: list[dict[str, object]],
        match_file_supplied: bool,
    ) -> dict[str, object]:
        gt_ids = {str(entry.get("gt_id")) for entry in ground_truth_entries}
        generated_ids = {str(entry.get("generated_id")) for entry in generated_entries}
        valid_matches: list[dict[str, object]] = []
        invalid_matches: list[dict[str, object]] = []

        for match in matches:
            generated_id = str(match.get("generated_id", "")).strip()
            gt_id = str(match.get("gt_id", "")).strip()
            decision = str(match.get("decision", "match")).strip().lower()
            if decision != "match":
                continue
            if generated_id in generated_ids and gt_id in gt_ids:
                valid_matches.append(match)
            else:
                invalid_matches.append(match)

        matched_generated_ids = {str(match.get("generated_id")) for match in valid_matches}
        matched_gt_ids = {str(match.get("gt_id")) for match in valid_matches}
        total_generated = len(generated_entries)
        total_gt = len(ground_truth_entries)
        precision = len(matched_generated_ids) / total_generated if total_generated else 0.0
        recall = len(matched_gt_ids) / total_gt if total_gt else 0.0
        f1 = 0.0
        if precision + recall:
            f1 = 2 * precision * recall / (precision + recall)

        gt_match_counts: dict[str, int] = {}
        for match in valid_matches:
            gt_id = str(match.get("gt_id"))
            gt_match_counts[gt_id] = gt_match_counts.get(gt_id, 0) + 1
        redundancy_count = sum(max(0, count - 1) for count in gt_match_counts.values())
        redundancy_per_gt = redundancy_count / total_gt if total_gt else 0.0
        avg_matches_per_gt = len(valid_matches) / total_gt if total_gt else 0.0
        unsupported_claim_count = total_generated - len(matched_generated_ids)
        structural_valid_count = sum(
            1
            for entry in generated_entries
            if str(entry.get("section", "")).strip()
            and str(entry.get("title", "")).strip()
            and str(entry.get("summary", "")).strip()
        )

        if not match_file_supplied:
            return {
                "evaluation_status": "match_required",
                "ground_truth_count": total_gt,
                "generated_count": total_generated,
                "valid_match_count": 0,
                "invalid_match_count": 0,
                "matched_generated_count": 0,
                "matched_ground_truth_count": 0,
                "precision": None,
                "recall": None,
                "f1": None,
                "unsupported_claim_count": None,
                "unsupported_claim_rate": None,
                "redundancy_count": None,
                "redundancy_per_gt": None,
                "avg_matches_per_gt": None,
                "structural_valid_count": structural_valid_count,
                "structural_valid_rate": round(
                    structural_valid_count / total_generated,
                    4,
                )
                if total_generated
                else 0.0,
            }

        return {
            "evaluation_status": "evaluated",
            "ground_truth_count": total_gt,
            "generated_count": total_generated,
            "valid_match_count": len(valid_matches),
            "invalid_match_count": len(invalid_matches),
            "matched_generated_count": len(matched_generated_ids),
            "matched_ground_truth_count": len(matched_gt_ids),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "unsupported_claim_count": unsupported_claim_count,
            "unsupported_claim_rate": round(
                unsupported_claim_count / total_generated,
                4,
            )
            if total_generated
            else 0.0,
            "redundancy_count": redundancy_count,
            "redundancy_per_gt": round(redundancy_per_gt, 4),
            "avg_matches_per_gt": round(avg_matches_per_gt, 4),
            "structural_valid_count": structural_valid_count,
            "structural_valid_rate": round(
                structural_valid_count / total_generated,
                4,
            )
            if total_generated
            else 0.0,
        }

    @staticmethod
    def _parse_ground_truth_entries(path: Path) -> list[dict[str, object]]:
        if not path.exists():
            raise FileNotFoundError(f"Ground truth file not found: {path}")

        entries: list[dict[str, object]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped.startswith("| GT-"):
                continue
            parts = [part.strip() for part in stripped.strip("|").split("|")]
            if len(parts) < 5:
                continue
            entries.append(
                {
                    "gt_id": parts[0],
                    "section": parts[1],
                    "entry": parts[2],
                    "supporting_evidence": parts[3],
                    "notes": parts[4],
                }
            )
        return entries

    @staticmethod
    def _extract_generated_entries(payload: dict[str, object]) -> list[dict[str, object]]:
        notes = payload.get("aggregated_release_notes")
        if not isinstance(notes, list) or not notes:
            notes = payload.get("structured_release_notes")
        if not isinstance(notes, list) or not notes:
            notes = payload.get("deduplicated_release_notes")
        if not isinstance(notes, list):
            return []

        generated_entries: list[dict[str, object]] = []
        for index, note in enumerate(notes, start=1):
            generated_id = f"GEN-{index:03d}"
            if isinstance(note, dict):
                generated_entries.append(
                    {
                        "generated_id": generated_id,
                        "section": str(note.get("section", "")),
                        "title": str(note.get("title", "")),
                        "summary": str(note.get("summary", "")),
                        "source_entry_ids": ReleaseNoteEvaluator._list_text(
                            note.get("source_entry_ids") or note.get("entry_ids")
                        ),
                        "source_symbols": ReleaseNoteEvaluator._list_text(
                            note.get("source_symbols") or note.get("symbols")
                        ),
                    }
                )
            else:
                generated_entries.append(
                    {
                        "generated_id": generated_id,
                        "section": "",
                        "title": "",
                        "summary": str(note),
                        "source_entry_ids": [],
                        "source_symbols": [],
                    }
                )
        return generated_entries

    @staticmethod
    def _read_matches(path: Path | None) -> list[dict[str, object]]:
        if path is None:
            return []
        if not path.exists():
            raise FileNotFoundError(f"Match file not found: {path}")
        payload = ReleaseNoteEvaluator._read_json(path)
        raw_matches = payload.get("matches", payload if isinstance(payload, list) else [])
        if not isinstance(raw_matches, list):
            raise ValueError(f"matches must be a list in {path}")
        return [match for match in raw_matches if isinstance(match, dict)]

    @staticmethod
    def _read_json(path: Path) -> dict[str, object]:
        if not path.exists():
            raise FileNotFoundError(f"JSON file not found: {path}")
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(payload, dict):
            raise ValueError(f"JSON payload must be an object: {path}")
        return payload

    @staticmethod
    def _list_text(raw: object) -> list[str]:
        if not isinstance(raw, list):
            return []
        return [str(item) for item in raw if str(item).strip()]
