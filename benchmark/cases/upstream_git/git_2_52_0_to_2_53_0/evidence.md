# Evidence Pack: upstream_git v2.52.0 -> v2.53.0

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `git_2_52_0_to_2_53_0`
- Repository: `upstream_git`
- Category: `version_control`
- Reference version: `v2.52.0`
- Target version: `v2.53.0`
- Pipeline status: `verified_stage1`
- Ground-truth status: `reviewed`

## Evidence Sources To Inspect

- [ ] official Git 2.53 release notes
- [ ] commit_messages
- [ ] function_level_diff
- [ ] changed_files

## Local Artifacts

- Changed functions: `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/changed_functions.json`

## Pipeline Summary

- Commit count: `639`
- Changed C/C++ files: `223`
- Changed functions: `905`
- Patch only: `False`
- CMG matched entries: `unknown`
- CMG unmatched entries: `unknown`
- Fallback-context entries: `unknown`
- Diff-derived call edges: `unknown`
- Prompt entries: `unknown`
- Mock generated entries: `unknown`

## Commit Messages

- Git 2.53
- Merge tag 'l10n-2.53.0-v1' of https://github.com/git-l10n/git-po
- RelNotes: fully spell negation
- Merge branch 'jx/zh_CN' of github.com:jiangxin/git
- Merge branch 'l10n/zh-TW/git-2-53' of github.com:l10n-tw/git-po
- Merge branch 'po-id' of github.com:bagasme/git-po
- Merge branch 'l10n-ga-2.53' of github.com:aindriu80/git-po
- Merge branch 'master' of github.com:alshopov/git-po
- Merge branch 'fr_2.53' of github.com:jnavila/git
- Merge branch 'tr-l10n' of github.com:bitigchi/git-po
- Merge branch 'master' of github.com:nafmo/git-l10n-sv
- l10n: zh_CN: standardize glossary terms
- RelNotes: correct "fast-import" option name
- l10n: zh_CN: updated translation for 2.53
- l10n: zh_CN: fix inconsistent use of standard vs. wide colons
- l10n: fr: v2.53
- l10n: zh_TW.po: update Git 2.53 translation
- RelNotes: a few spelling fixes
- l10n: tr: Update Turkish translations
- l10n: sv.po: Update Swedish translation
- Git 2.53-rc2
- l10n: po-id for 2.53
- l10n: ga.po: Fix git-po-helper warnings
- Revert "Merge branch 'cs/rebased-subtree-split'"
- Merge branch 'master' of https://github.com/j6t/git-gui
- l10n: bg.po: Updated Bulgarian translation (6091t)
- git-gui: mark *.po files at any directory level as UTF-8
- Merge branch 'master' of github.com:alshopov/git-gui
- git-gui i18n: Update Bulgarian translation (558t)
- Merge branch 'master' of github.com:alshopov/git-gui
- A bit more before -rc2
- Merge branch 'dk/replay-doc-omit-irrelevant-rev-list-options'
- Merge branch 'js/symlink-windows'
- Merge branch 'pw/mailmap-self'
- Merge branch 'js/ci-leak-skip-svn'
- Merge branch 'jx/build-options-gettext'
- Merge branch 'ty/t1005-test-path-is-helpers'
- Merge branch 'rj/cygwin-test-fixes-for-2.53'
- Merge branch 'sb/doc-update-ref-markup-fix'
- Merge branch 'kh/mailmap-avila'
- l10n: ga.po: Update Irish translation for Git 2.53
- git-gui i18n: Update Bulgarian translation (557t)
- A few on top of -rc1
- Merge branch 'rs/tree-wo-the-repository'
- Merge branch 'ps/config-doc-get-urlmatch-fix'
- Merge branch 'tb/midx-write-corrupt-checksum-fix'
- Merge branch 'ps/geometric-repacking-with-promisor-remotes'
- .mailmap: fix and expand mappings for Jean-Noël Avila
- Git 2.53-rc1
- Merge branch 'js/prep-symlink-windows'
- Merge branch 'ps/read-object-info-improvements'
- Merge branch 'ps/packfile-store-in-odb-source'
- Merge branch 'kt/http-backend-errors'
- Merge branch 'ps/t1410-cleanup'
- Merge branch 'ps/ref-consistency-checks'
- Merge branch 'tb/macos-iconv-workarounds'
- Merge branch 'cs/rebased-subtree-split'
- Merge branch 'je/doc-reset'
- Merge branch 'en/fsck-snapshot-ref-state'
- lint-gitlink: preemptively ignore all /ifn?def|endif/ macros
- replay: drop rev-list formatting options from manual
- mailmap: add an entry for Phillip Wood
- ci: skip CVS and P4 tests in leaks job, too
- ci(*-leaks): skip the git-svn tests to save time
- t1005: modernize "! test -f" to "test_path_is_missing"
- help: report on whether or not gettext is enabled
- t0610-reftable-basics: mitigate a flaky test on cygwin
- t9700/test.pl: fix path type expectation on cygwin
- Merge a handful more topics after -rc0
- Merge branch 'ml/doc-blame-markup'
- Merge branch 'kh/doc-patch-id'
- Merge branch 'bc/doc-stash-import-export'
- Merge branch 'kj/t7101-modernize'
- Merge branch 'ds/builtin-doc-update'
- Merge branch 'ac/t1420-use-more-direct-check'
- Merge branch 'jk/cat-file-avoid-bitmap-when-unneeded'
- Merge branch 'jk/t-perf-fixes'
- cocci: remove obsolete the_repository rules
- Revert "Merge branch 'ar/run-command-hook'"
- Git 2.53-rc0
- Merge branch 'ps/clar-integers'
- Merge branch 'kh/replay-invalid-onto-advance'
- Merge branch 'ps/odb-misc-fixes'
- Merge branch 'pt/t7800-difftool-test-racefix'
- Documentation/config: fix replacement for --get-urlmatch
- builtin/repack: handle promisor packs with geometric repacking
- repack-promisor: extract function to remove redundant packs
- repack-promisor: extract function to finalize repacking
- repack-geometry: extract function to compute repacking split
- builtin/pack-objects: exclude promisor objects with "--stdin-packs"
- midx-write.c: assume checksum-invalid MIDXs require an update
- t/t5319-multi-pack-index.sh: drop early 'test_done'
- Merge branch 'ps/repack-avoid-noop-midx-rewrite' into tb/midx-write-corrupt-checksum-fix
- utf8.c: enable workaround for iconv under macOS 14/15
- utf8.c: prepare workaround for iconv under macOS 14/15
- builtin/fsck: drop `fsck_head_link()`
- builtin/fsck: move generic HEAD check into `refs_fsck()`
- builtin/fsck: move generic object ID checks into `refs_fsck()`
- refs/reftable: introduce generic checks for refs
- refs/reftable: fix consistency checks with worktrees
- refs/reftable: extract function to retrieve backend for worktree
- refs/reftable: adapt includes to become consistent
- refs/files: introduce function to perform normal ref checks
- refs/files: extract generic symref target checks
- fsck: drop unused fields from `struct fsck_ref_report`
- refs/files: perform consistency checks for root refs
- refs/files: improve error handling when verifying symrefs
- refs/files: extract function to check single ref
- refs/files: remove useless indirection
- refs/files: remove `refs_check_dir` parameter
- refs/files: move fsck functions into global scope
- refs/files: simplify iterating through root refs
- packfile: drop repository parameter from `packed_object_info()`
- packfile: skip unpacking object header for disk size requests
- packfile: disentangle return value of `packed_object_info()`
- packfile: always populate pack-specific info when reading object info
- packfile: extend `is_delta` field to allow for "unknown" state
- packfile: always declare object info to be OI_PACKED
- object-file: always set OI_LOOSE when reading object info
- The 17th batch
- Merge branch 'js/mailmap-karsten-blees'
- Merge branch 'ps/t1300-2021-use-test-path-is-helpers'
- Merge branch 'rs/commit-stack'
- Merge branch 'sb/bundle-uri-without-uri'
- Merge branch 'ja/doc-synopsis-style-more'
- t1410: use test helpers in reflog rewind test
- http-backend: write newlines to stderr when responding with errors
- .mailmap: replace Karsten Blees' default address
- contrib/subtree: detect rewritten subtree commits
- cocci: convert parse_tree functions to repo_ variants
- tree: stop using the_repository
- tree: use repo_parse_tree()
- path-walk: use repo_parse_tree_gently()
- pack-bitmap-write: use repo_parse_tree()
- delta-islands: use repo_parse_tree()
- bloom: use repo_parse_tree()
- add-interactive: use repo_parse_tree_indirect()
- tree: add repo_parse_tree*()
- environment: move access to core.maxTreeDepth into repo settings
- mingw: special-case index entries for symlinks with buggy size
- mingw: emulate `stat()` a little more faithfully
- mingw: try to create symlinks without elevated permissions
- mingw: add support for symlinks to directories
- mingw: implement basic `symlink()` functionality (file symlinks only)
- mingw: implement `readlink()`
- mingw: allow `mingw_chdir()` to change to symlink-resolved directories
- mingw: support renaming symlinks
- mingw: handle symlinks to directories in `mingw_unlink()`
- mingw: add symlink-specific error codes
- mingw: change default of `core.symlinks` to false
- mingw: factor out the retry logic
- mingw: compute the correct size for symlinks in `mingw_lstat()`
- mingw: teach dirent about symlinks
- mingw: let `mingw_lstat()` error early upon problems with reparse points
- mingw: drop the separate `do_lstat()` function
- mingw: implement `stat()` with symlink support
- mingw: don't call `GetFileAttributes()` twice in `mingw_lstat()`
- Merge branch 'js/prep-symlink-windows' into js/symlink-windows
- trim_last_path_component(): avoid hard-coding the directory separator
- strbuf_readlink(): support link targets that exceed 2*PATH_MAX
- strbuf_readlink(): avoid calling `readlink()` twice in corner-cases
- init: do parse _all_ core.* settings early
- mingw: do resolve symlinks in `getcwd()`
- fsck: snapshot default refs before object walk
- packfile: move MIDX into packfile store
- packfile: refactor `find_pack_entry()` to work on the packfile store
- packfile: inline `find_kept_pack_entry()`
- packfile: only prepare owning store in `packfile_store_prepare()`
- packfile: only prepare owning store in `packfile_store_get_packs()`
- packfile: move packfile store into object source
- packfile: refactor misleading code when unusing pack windows
- packfile: refactor kept-pack cache to work with packfile stores
- packfile: pass source to `prepare_pack()`
- packfile: create store via its owning source
- builtin.h: update documentation
- t7101: modernize test path checks
- gitfaq: document using stash import/export to sync working tree
- doc: git-blame: convert to new doc format
- doc: blame-options: convert to new doc format
- doc: patch-id: --verbatim locks in --stable
- doc: patch-id: spell out the git-diff-tree(1) form
- doc: patch-id: use definite article for the result
- patch-id: use “patch ID” throughout
- doc: patch-id: capitalize Git version
- doc: patch-id: don’t use semicolon between bullet points
- The 16th batch
- Merge branch 'en/ort-recursive-d-f-conflict-fix'
- Merge branch 'dd/t5403-modernise'
- Merge branch 'ds/diff-lazy-fetch-with-name-only-fix'
- Merge branch 'rs/tag-wo-the-repository'
- Merge branch 'ps/odb-misc-fixes' into ps/packfile-store-in-odb-source
- t1420: modernize the lost-found test
- odb: properly close sources before freeing them
- builtin/gc: fix condition for whether to write commit graphs
- cat-file: only use bitmaps when filtering
- t/perf/run: preserve GIT_PERF_* from environment
- t/perf/perf-lib: fix assignment of TEST_OUTPUT_DIRECTORY
- The 15th batch
- Merge branch 'rs/parse-config-expiry-simplify'
- Merge branch 'ar/run-command-hook'
- Merge branch 'rs/show-branch-prio-queue'
- Merge branch 'rs/macos-iconv-workaround'
- Merge branch 'bc/checkout-error-message-fix'
- doc: git-reset: clarify `git reset <pathspec>`
- doc: git-reset: clarify `git reset [mode]`
- doc: git-reset: clarify intro
- doc: git-reset: reorder the forms
- t3650: add more regression tests for failure conditions
- replay: die if we cannot parse object
- replay: improve code comment and die message
- replay: die descriptively when invalid commit-ish is given
- replay: find *onto only after testing for ref name
- replay: remove dead code and rearrange
- t1300: use test helpers instead of `test` command
- t7800: fix racy "difftool --dir-diff syncs worktree" test
- The 14th batch
- Merge branch 'jk/test-curl-updates'
- Merge branch 'jc/object-read-stream-fix'
- Merge branch 'js/test-func-comment-fix'
- Merge branch 'gf/clear-path-cache-cleanup'
- Merge branch 'gf/maintenance-is-needed-fix'
- Merge branch 'dk/ci-rust-fix'
- Merge branch 'mh/doc-core-attributesfile'
- Merge branch 'ps/repack-avoid-noop-midx-rewrite'
- Merge branch 'js/test-symlink-windows'
- Merge branch 'jt/doc-rev-list-filter-provided-objects'
- Merge branch 'jt/repo-struct-more-objinfo'
- diff: avoid segfault with freed entries
- t5403: use test_path_is_file instead of test -f
- merge-ort: fix corner case recursive submodule/directory conflict handling
- tag: stop using the_repository
- tag: support arbitrary repositories in parse_tag()
- tag: support arbitrary repositories in gpg_verify_tag()
- tag: use algo of repo parameter in parse_tag_buffer()
- The 13th batch
- Merge branch 'ap/packfile-promisor-object-optim'
- Merge branch 'ja/doc-misc-fixes'
- Merge branch 'jc/doc-commit-signoff-config'
- Merge branch 'jc/c99-fam'
- config: use git_parse_int() in git_config_get_expiry_in_days()
- receive-pack: convert receive hooks to hook API
- receive-pack: convert update hooks to new API
- hooks: allow callers to capture output
- run-command: allow capturing of collated output
- hook: allow overriding the ungroup option
- reference-transaction: use hook API instead of run-command
- transport: convert pre-push to hook API
- hook: convert 'post-rewrite' hook in sequencer.c to hook API
- hook: provide stdin via callback
- run-command: add stdin callback for parallelization
- run-command: add first helper for pp child states
- show-branch: use prio_queue
- macOS: use iconv from Homebrew if needed and present
- macOS: make Homebrew use configurable
- commit-reach: use commit_stack
- commit-graph: use commit_stack
- commit: add commit_stack_grow()
- shallow: use commit_stack
- pack-bitmap-write: use commit_stack
- commit: add commit_stack_init()
- test-reach: use commit_stack
- remote: use commit_stack for src_commits
- remote: use commit_stack for sent_tips
- remote: use commit_stack for local_commits
- name-rev: use commit_stack
- midx: use commit_stack
- log: use commit_stack
- revision: export commit_stack
- checkout: quote invalid treeish in error message
- The 12th batch
- Merge branch 'kn/fix-fetch-backfill-tag-with-batched-ref-updates'
- Merge branch 'rs/diff-files-r-find-copies-fix'
- Merge branch 'jc/memzero-array'
- Merge branch 'tc/memzero-array'
- Merge branch 'jc/completion-no-single-letter-options'
- Merge branch 'jc/submodule-add'
- Merge branch 'ds/doc-scalar-config'
- The 11th batch
- Merge branch 'rs/t4014-git-version-string-fix'
- Merge branch 'kj/pull-options-decl-cleanup'
- Merge branch 'jc/macports-darwinports'
- Merge branch 'rs/replay-wrong-onto-fix'
- Merge branch 'kh/doc-replay-updates'
- Merge branch 'ps/odb-alternates-object-sources'
- doc: convert git-remote to synopsis style
- doc: convert git stage to use synopsis block
- doc: convert git-status tables to AsciiDoc format
- doc: convert git-status to synopsis style
- doc: fix t0450-txt-doc-vs-help to select only first synopsis block
- doc: correct minor wording issues
- doc: fix asciidoc markup issues in several files
- bundle-uri: validate that bundle entries have a uri
- signoff-option: linkify the reference to gitfaq
- rust: build correctly without GNU sed
- Merge branch 'ps/ci-rust' into dk/ci-rust-fix
- refs: dereference the value of the required pointer
- repository: remove duplicate free of cache->squash_msg
- test_detect_ref_format: fix comment
- t5563: add missing end-of-line in HTTP header
- t5551: handle trailing slashes in expected cookies output
- Merge branch 'jc/object-read-stream-fix' into ps/read-object-info-improvements
- odb: do not use "blank" substitute for NULL
- Merge branch 'ps/object-read-stream' into jc/object-read-stream-fix
- docs: note the type of core.attributesfile
- builtin/repo: add object disk size info to structure table
- builtin/repo: add disk size info to keyvalue stucture output
- builtin/repo: add inflated object info to structure table
- builtin/repo: add inflated object info to keyvalue structure output
- builtin/repo: humanise count values in structure output
- strbuf: split out logic to humanise byte values
- builtin/repo: group per-type object values into struct
- Merge branch 'js/test-symlink-windows' into js/prep-symlink-windows
- t7800: work around the MSYS path conversion on Windows
- t6423: introduce Windows-specific handling for symlinking to /dev/null
- t1305: skip symlink tests that do not apply to Windows
- t1006: accommodate for symlink support in MSYS2
- t0600: fix incomplete prerequisite for a test case
- t0301: another fix for Windows compatibility
- t0001: handle `diff --no-index` gracefully
- mingw: special-case `open(symlink, O_CREAT | O_EXCL)`
- apply: symbolic links lack a "trustable executable bit"
- t9700: accommodate for Windows paths
- commit: document that $command.signoff will not be added
- The 10th batch
- Merge branch 'kh/doc-send-email-paragraph-fix'
- Merge branch 'mh/doc-config-gui-gcwarning'
- Merge branch 'kh/doc-pre-commit-fix'
- Merge branch 'jc/capability-leak'
- The ninth batch
- Merge branch 'rs/ban-mktemp'
- Merge branch 'gf/win32-pthread-cond-init'
- Merge branch 'ps/object-read-stream'
- diff-files: fix copy detection
- Merge branch 'rs/diff-index-find-copies-harder-optim' into rs/diff-files-r-find-copies-fix
- docs: clarify git-rev-list(1) --filter behavior
- scalar: document config settings
- Merge branch 'ps/object-read-stream' into ps/packfile-store-in-odb-source
- The eighth batch
- Merge branch 'je/doc-data-model'
- Merge branch 'lo/repo-struct-z'
- Merge branch 'kh/advise-w-git-help-in-branch'
- Merge branch 'je/doc-pull'
- Merge branch 'tc/meson-cross-compile-fix'
- Merge branch 'js/last-modified-with-sparse-checkouts'
- Merge branch 'rs/diff-index-find-copies-harder-optim'
- Merge branch 'tc/last-modified-active-paths-optimization'
- doc: replay: link section using markup
- replay: improve --contained and add to doc
- doc: replay: mention no output on conflicts
- t4014: support Git version strings with spaces
- cocci: use MEMZERO_ARRAY() a bit more
- coccicheck: emit the contents of cocci patch
- Merge branch 'tc/memzero-array' into jc/memzero-array
- scalar: alphabetize and simplify config
- scalar: remove stale config values
- scalar: use index.skipHash=true for performance
- scalar: annotate config file with "set by scalar"
- pull: move options[] array into function scope
- FLEX_ARRAY: require platforms to support the C99 syntax
- replay: move onto NULL check before first use
- Merge branch 'sa/replay-atomic-ref-updates' into rs/replay-wrong-onto-fix
- Makefile: help macOS novices by mentioning MacPorts
- odb: write alternates via sources
- odb: read alternates via sources
- odb: drop forward declaration of `read_info_alternates()`
- odb: remove mutual recursion when parsing alternates
- odb: stop splitting alternate in `odb_add_to_alternates_file()`
- odb: move computation of normalized objdir into `alt_odb_usable()`
- odb: resolve relative alternative paths when parsing
- odb: refactor parsing of alternates to be self-contained
- contrib/coccinelle: pass include paths to spatch(1)
- git-compat-util: introduce MEMZERO_ARRAY() macro
- Merge branch 'tc/last-modified-active-paths-optimization' into tc/memzero-array
- midx-write: skip rewriting MIDX with `--stdin-packs` unless needed
- midx-write: extract function to test whether MIDX needs updating
- midx: fix `BUG()` when getting preferred pack without a reverse index
- fetch: fix failed batched updates skipping operations
- fetch: fix non-conflicting tags not being committed
- doc: fix `update-ref` `symref-create` formatting
- packfile: skip hash checks in add_promisor_object()
- object: apply skip_hash and discard_tree optimizations to unknown blobs too
- The seventh batch
- Merge branch 'en/replay-doc-revision-range'
- Merge branch 'yc/xdiff-patience-optim'
- Merge branch 'bc/zsh-testsuite'
- Merge branch 'pw/replay-exclude-gpgsig-fix'
- config: document 'gui.GCWarning'
- doc: send-email: fix broken list continuation
- connect: plug protocol capability leak
- doc: join default pre-commit paragraphs
- completion: clarify support for short options and arguments
- compat: remove gitmkdtemp()
- banned.h: ban mktemp(3)
- compat: remove mingw_mktemp()
- compat: use git_mkdtemp()
- wrapper: add git_mkdtemp()
- gitattributes: disable blank-at-eof errors for clar test expectations
- t/unit-tests: demonstrate use of integer comparison assertions
- t/unit-tests: update clar to 39f11fe
- Merge branch 'ps/object-source-management' into ps/odb-misc-fixes
- The sixth batch
- Merge branch 'rs/config-set-multi-error-message-fix'
- Merge branch 'rs/config-unset-opthelp-fix'
- Merge branch 'ps/object-source-management'
- Merge branch 'cc/fast-import-strip-if-invalid'
- Merge branch 'js/ci-show-breakage-in-dockerized-jobs'
- Merge branch 'kh/doc-committer-date-is-author-date'
- Merge branch 'jc/optional-path'
- Merge branch 'js/strip-scalar-too'
- Merge branch 'en/xdiff-cleanup-2'
- repo: add -z as an alias for --format=nul to git-repo-structure
- repo: use [--format=... | -z] instead of [-z] in git-repo-info synopsis
- repo: remove blank line from Documentation/git-repo.adoc
- meson: use is_cross_build() where possible
- meson: only detect ICONV_OMITS_BOM if possible
- meson: ignore subprojects/.wraplock
- last-modified: support sparse checkouts
- doc: git-pull: fix 'git --rebase abort' typo
- doc: remove stray text in Git data model
- branch: advice using git-help(1) instead of man(1)
- The fifth batch
- Merge branch 'jk/asan-bonanza'
- Merge branch 'je/doc-data-model'
- Merge branch 'jc/whitespace-incomplete-line'
- Merge branch 'ja/doc-synopsis-style'
- Merge branch 'lo/repo-info-all'
- diff-index: don't queue unchanged filepairs with diff_change()
- last-modified: fix use of uninitialized memory
- Documentation/git-replay.adoc: fix errors around revision range
- xdiff: optimize patience diff's LCS search
- t5564: fix test hang under zsh's sh mode
- t0614: use numerical comparison with test_line_count
- The fourth batch
- Merge branch 'gf/win32-pthread-cond-wait-err'
- Merge branch 'jk/ci-windows-meson-test-fix'
- Merge branch 'pw/worktree-list-display-width-fix'
- Merge branch 'js/wincred-get-credential-alloc-fix'
- Merge branch 'js/cmake-libgit-fix'
- Merge branch 'js/mingw-assign-comma-fix'
- Merge branch 'js/ci-github-setup-go-update'
- Merge branch 'jk/test-mktemp-leakfix'
- Merge branch 'rs/xmkstemp-simplify'
- Merge branch 'ad/blame-diff-algorithm'
- Merge branch 'en/ort-rename-another-fix'
- ci(dockerized): do show the result of failing tests again
- Merge branch 'master' of https://github.com/j6t/gitk
- replay: do not copy "gpgsign-sha256" header
- fast-import: add 'strip-if-invalid' mode to --signed-commits=<mode>
- Merge branch 'tb/external-diff-renamed'
- Merge branch 'js/persist-ref-window-geometry'
- odb: handle recreation of quarantine directories
- odb: handle changing a repository's commondir
- chdir-notify: add function to unregister listeners
- odb: handle initialization of sources in `odb_new()`
- http-push: stop setting up `the_repository` for each reference
- t/helper: stop setting up `the_repository` repeatedly
- builtin/index-pack: fix deferred fsck outside repos
- oidset: introduce `oidset_equal()`
- odb: move logic to disable ref updates into repo
- submodule add: sanity check existing .gitmodules
- config: really treat missing optional path as not configured
- config: really pretend missing :(optional) value is not there
- The third batch
- Merge branch 'jx/repo-struct-utf8width-fix'
- Merge branch 'kn/osxkeychain-idempotent-store-fix'
- Merge branch 'kh/doc-commit-extra-references'
- Merge branch 'ps/object-source-loose'
- Merge branch 'qj/doc-http-bad-want-response'
- Merge branch 'sa/replay-atomic-ref-updates'
- Merge branch 'bc/submodule-force-same-hash'
- Merge branch 'jk/attr-macroexpand-wo-recursion'
- config: fix short help of unset flags
- config: fix suggestion for failed set of multi-valued option
- doc: pull-fetch-param typofix
- streaming: drop redundant type and size pointers
- streaming: move into object database subsystem
- streaming: refactor interface to be object-database-centric
- streaming: move logic to read packed objects streams into backend
- streaming: move logic to read loose objects streams into backend
- streaming: make the `odb_read_stream` definition public
- streaming: get rid of `the_repository`
- streaming: rely on object sources to create object stream
- packfile: introduce function to read object info from a store
- streaming: move zlib stream into backends
- streaming: create structure for filtered object streams
- streaming: create structure for packed object streams
- streaming: create structure for loose object streams
- streaming: create structure for in-core object streams
- streaming: allocate stream inside the backend-specific logic
- streaming: explicitly pass packfile info when streaming a packed object
- streaming: propagate final object type via the stream
- streaming: drop the `open()` callback function
- streaming: rename `git_istream` into `odb_read_stream`
- The second batch
- Merge branch 'jc/gitattributes-whitespace-no-indent-fix'
- Merge branch 'kn/maintenance-is-needed'
- Merge branch 'rs/diff-quiet-no-rename'
- fetch: extract out reference committing logic
- config: mark otherwise unused function as file-scope static
- win32: pthread_cond_init should return a value
- win32: return error if SleepConditionVariableCS fails
- doc: warn against --committer-date-is-author-date
- odb: refactor `odb_clear()` to `odb_free()`
- odb: adopt logic to close object databases
- setup: convert `set_git_dir()` to have file scope
- path: move `enter_repo()` into "setup.c"
- Merge branch 'ps/object-source-loose' into ps/object-source-management
- Merge branch 'ps/object-source-loose' into ps/object-read-stream
- doc: convert git push to synopsis style
- doc: convert git pull to synopsis style
- doc: convert git fetch to synopsis style
- Start 2.53 cycle
- Merge branch 'ps/ref-peeled-tags-fixes'
- Merge branch 'kn/refs-optim-cleanup'
- Merge branch 'ps/ref-peeled-tags'
- Merge branch 'ps/packed-git-in-object-store'
- xdiff: rename rindex -> reference_index
- xdiff: change rindex from long to size_t in xdfile_t
- xdiff: make xdfile_t.nreff a size_t instead of long
- xdiff: make xdfile_t.nrec a size_t instead of long
- xdiff: split xrecord_t.ha into line_hash and minimal_perfect_hash
- xdiff: use unambiguous types in xdl_hash_record()
- xdiff: use size_t for xrecord_t.size
- xdiff: make xrecord_t.ptr a uint8_t instead of char
- xdiff: use ptrdiff_t for dstart/dend
- doc: define unambiguous type mappings across C and Rust
- repo: add --all to git-repo-info
- repo: factor out field printing to dedicated function
- worktree list: quote paths
- worktree list: fix column spacing
- test-mktemp: plug memory and descriptor leaks
- ci(windows-meson-test): handle options and output like other test jobs
- unit-test: ignore --no-chain-lint
- t: enable ASan's strict_string_checks option
- fsck: avoid parse_timestamp() on buffer that isn't NUL-terminated
- fsck: remove redundant date timestamp check
- fsck: avoid strcspn() in fsck_ident()
- fsck: assert newline presence in fsck_ident()
- cache-tree: avoid strtol() on non-string buffer
- Makefile: turn on NO_MMAP when building with ASan
- pack-bitmap: handle name-hash lookups in incremental bitmaps
- compat/mmap: mark unused argument in git_munmap()
- ci: bump actions/setup-go from 5 to 6
- mingw: avoid the comma operator
- cmake: stop trying to build the reftable and xdiff libraries
- wincred: avoid memory corruption
- merge-ort: fix failing merges in special corner case
- merge-ort: remove debugging crud
- t6429: update comment to mention correct tool
- make strip: include `scalar`
- wrapper: simplify xmkstemp()
- blame: make diff algorithm configurable
- xdiff: add 'minimal' to XDF_DIFF_ALGORITHM_MASK
- commit: refactor verify_commit_buffer()
- fast-import: refactor finalize_commit_buffer()
- builtin/repo: fix table alignment for UTF-8 characters
- t/unit-tests: add UTF-8 width tests for CJK chars
- read-cache: drop submodule check from add_to_cache()
- object-file: disallow adding submodules of different hash algo
- doc: commit: link to git-status(1) on all format options
- osxkeychain: avoid incorrectly skipping store operation
- attr: enable incomplete-line whitespace error for this project
- diff: highlight and error out on incomplete lines
- apply: check and fix incomplete lines
- whitespace: allocate a few more bits and define WS_INCOMPLETE_LINE
- apply: revamp the parsing of incomplete lines
- diff: update the way rewrite diff handles incomplete lines
- diff: call emit_callback ecbdata everywhere
- diff: refactor output of incomplete line
- diff: keep track of the type of the last line seen
- diff: correct suppress_blank_empty hack
- diff: emit_line_ws_markup() if/else style fix
- whitespace: correct bit assignment comments
- doc: add an explanation of Git's data model
- attr: avoid recursion when expanding attribute macros
- .gitattributes: remove misspelled no-op whitespace attribute
- diff: disable rename detection with --quiet
- maintenance: add 'is-needed' subcommand
- maintenance: add checking logic in `pack_refs_condition()`
- refs: add a `optimize_required` field to `struct ref_storage_be`
- reftable/stack: add function to check if optimization is required
- reftable/stack: return stack segments directly
- object: fix performance regression when peeling tags
- Merge branch 'ps/ref-peeled-tags' into ps/ref-peeled-tags-fixes
- gitk: add external diff file rename detection
- doc: clarify server behavior for invalid 'want' lines in HTTP protocol
- gitk: show unescaped file names on 'rename' and 'copy' lines
- gitk: fix a 'continue' statement outside a loop to 'return'
- replay: add replay.refAction config option
- replay: make atomic ref updates the default behavior
- replay: use die_for_incompatible_opt2() for option validation
- Merge branch 'kn/refs-optim-cleanup' into kn/maintenance-is-needed
- Merge branch 'ps/ref-peeled-tags' into kn/maintenance-is-needed
- t/pack-refs-tests: move the 'test_done' to callees
- refs: rename 'pack_refs_opts' to 'refs_optimize_opts'
- refs: move to using the '.optimize' functions
- Merge branch 'ps/ref-peeled-tags' into kn/refs-optim-cleanup
- t7004: do not chdir around in the main process
- ref-filter: fix stale parsed objects
- ref-filter: parse objects on demand
- ref-filter: detect broken tags when dereferencing them
- refs: don't store peeled object IDs for invalid tags
- object: add flag to `peel_object()` to verify object type
- refs: drop infrastructure to peel via iterators
- refs: drop `current_ref_iter` hack
- builtin/show-ref: convert to use `reference_get_peeled_oid()`
- ref-filter: propagate peeled object ID
- upload-pack: convert to use `reference_get_peeled_oid()`
- refs: expose peeled object ID via the iterator
- refs: refactor reference status flags
- refs: fully reset `struct ref_iterator::ref` on iteration
- refs: introduce `.ref` field for the base iterator
- refs: introduce wrapper struct for `each_ref_fn`
- object-file: refactor writing objects via a stream
- object-file: rename `write_object_file()`
- object-file: refactor freshening of objects
- object-file: rename `has_loose_object()`
- object-file: read objects via the loose object source
- object-file: move loose object map into loose source
- object-file: hide internals when we need to reprepare loose sources
- object-file: move loose object cache into loose source
- object-file: introduce `struct odb_source_loose`
- object-file: move `fetch_if_missing`
- odb: adjust naming to free object sources
- odb: introduce `odb_source_new()`
- odb: fix subtle logic to check whether an alternate is usable
- packfile: track packs via the MRU list exclusively
- packfile: always add packfiles to MRU when adding a pack
- packfile: move list of packs into the packfile store
- builtin/pack-objects: simplify logic to find kept or nonlocal objects
- packfile: fix approximation of object counts
- http: refactor subsystem to use `packfile_list`s
- packfile: move the MRU list into the packfile store
- packfile: use a `strmap` to store packs by name
- Merge branch 'ps/remove-packfile-store-get-packs' into ps/packed-git-in-object-store
- Merge branch 'jt/repo-structure' into ps/ref-peeled-tags
- Merge branch 'tb/incremental-midx-part-3.1' into ps/ref-peeled-tags
- gitk: persist position and size of the Tags and Heads window
- Revert "gitk: Only restore window size from ~/.gitk, not position"

## Changed C/C++ Files

- `add-interactive.c`
- `apply.c`
- `archive-tar.c`
- `archive-zip.c`
- `archive.c`
- `attr.c`
- `banned.h`
- `bisect.c`
- `bloom.c`
- `branch.c`
- `builtin.h`
- `builtin/am.c`
- `builtin/bisect.c`
- `builtin/blame.c`
- `builtin/branch.c`
- `builtin/cat-file.c`
- `builtin/checkout.c`
- `builtin/clone.c`
- `builtin/commit.c`
- `builtin/config.c`
- `builtin/describe.c`
- `builtin/diff-tree.c`
- `builtin/fast-export.c`
- `builtin/fast-import.c`
- `builtin/fetch.c`
- `builtin/fsck.c`
- `builtin/gc.c`
- `builtin/grep.c`
- `builtin/index-pack.c`
- `builtin/last-modified.c`
- `builtin/log.c`
- `builtin/ls-remote.c`
- `builtin/ls-tree.c`
- `builtin/merge-tree.c`
- `builtin/merge.c`
- `builtin/name-rev.c`
- `builtin/pack-objects.c`
- `builtin/patch-id.c`
- `builtin/pull.c`
- `builtin/read-tree.c`
- `builtin/receive-pack.c`
- `builtin/remote.c`
- `builtin/repack.c`
- `builtin/replace.c`
- `builtin/replay.c`
- `builtin/repo.c`
- `builtin/reset.c`
- `builtin/rev-parse.c`
- `builtin/show-branch.c`
- `builtin/show-ref.c`
- `builtin/stash.c`
- `builtin/submodule--helper.c`
- `builtin/tag.c`
- `builtin/unpack-objects.c`
- `builtin/upload-archive.c`
- `builtin/upload-pack.c`
- `builtin/verify-tag.c`
- `builtin/worktree.c`
- `bundle-uri.c`
- `cache-tree.c`
- `chdir-notify.c`
- `chdir-notify.h`
- `commit-graph.c`
- `commit-reach.c`
- `commit.c`
- `commit.h`
- `compat/mingw-posix.h`
- `compat/mingw.c`
- `compat/mkdtemp.c`
- `compat/mmap.c`
- `compat/posix.h`
- `compat/simple-ipc/ipc-win32.c`
- `compat/win32.h`
- `compat/win32/dirent.c`
- `compat/win32/pthread.c`
- `compat/win32/pthread.h`
- `config.c`
- `config.h`
- `connect.c`
- `contrib/credential/osxkeychain/git-credential-osxkeychain.c`
- `contrib/credential/wincred/git-credential-wincred.c`
- `delta-islands.c`
- `diff-delta.c`
- `diff-lib.c`
- `diff.c`
- `diff.h`
- `diffcore-delta.c`
- `entry.c`
- `environment.c`
- `environment.h`
- `ewah/bitmap.c`
- `fetch-pack.c`
- `fsck.c`
- `fsck.h`
- `git-compat-util.h`
- `gpg-interface.c`
- `gpg-interface.h`
- `hashmap.c`
- `help.c`
- `http-backend.c`
- `http-push.c`
- `http-walker.c`
- `http.c`
- `http.h`
- `linear-assignment.c`
- `list-objects.c`
- `lockfile.c`
- `log-tree.c`
- `loose.c`
- `ls-refs.c`
- `merge-ort.c`
- `merge.c`
- `midx-write.c`
- `midx.c`
- `negotiator/default.c`
- `negotiator/skipping.c`
- `notes.c`
- `object-file.c`
- `object-file.h`
- `object-name.c`
- `object.c`
- `object.h`
- `odb.c`
- `odb.h`
- `odb/streaming.c`
- `odb/streaming.h`
- `oidset.c`
- `oidset.h`
- `pack-bitmap-write.c`
- `pack-bitmap.c`
- `pack-refs.c`
- `pack-revindex.c`
- `pack-revindex.h`
- `packfile.c`
- `packfile.h`
- `parallel-checkout.c`
- `path-walk.c`
- `path.c`
- `path.h`
- `pseudo-merge.c`
- `reachable.c`
- `read-cache.c`
- `ref-filter.c`
- `ref-filter.h`
- `reflog.c`
- `refs.c`
- `refs.h`
- `refs/debug.c`
- `refs/files-backend.c`
- `refs/iterator.c`
- `refs/packed-backend.c`
- `refs/ref-cache.c`
- `refs/refs-internal.h`
- `refs/reftable-backend.c`
- `reftable/reftable-stack.h`
- `reftable/stack.c`
- `remote.c`
- `repack-geometry.c`
- `repack-midx.c`
- `repack-promisor.c`
- `repack.h`
- `replace-object.c`
- `repo-settings.c`
- `repo-settings.h`
- `repository.c`
- `repository.h`
- `reset.c`
- `revision.c`
- `run-command.c`
- `scalar.c`
- `sequencer.c`
- `server-info.c`
- `setup.c`
- `setup.h`
- `shallow.c`
- `shallow.h`
- `strbuf.c`
- `strbuf.h`
- `streaming.c`
- `streaming.h`
- `submodule.c`
- `t/helper/test-cache-tree.c`
- `t/helper/test-match-trees.c`
- `t/helper/test-mktemp.c`
- `t/helper/test-reach.c`
- `t/helper/test-ref-store.c`
- `t/helper/test-repository.c`
- `t/helper/test-simple-ipc.c`
- `t/unit-tests/clar/clar.c`
- `t/unit-tests/clar/clar.h`
- `t/unit-tests/clar/clar/print.h`
- `t/unit-tests/clar/test/selftest.c`
- `t/unit-tests/clar/test/suites/combined.c`
- `t/unit-tests/u-reftable-record.c`
- `t/unit-tests/u-reftable-stack.c`
- `t/unit-tests/u-utf8-width.c`
- `t/unit-tests/unit-test.c`
- `t/unit-tests/unit-test.h`
- `tag.c`
- `tag.h`
- `tree-diff.c`
- `tree-walk.c`
- `tree.c`
- `tree.h`
- `upload-pack.c`
- `utf8.c`
- `walker.c`
- `worktree.c`
- `wrapper.c`
- `wrapper.h`
- `ws.c`
- `ws.h`
- `xdiff-interface.c`
- `xdiff/xdiff.h`
- `xdiff/xdiffi.c`
- `xdiff/xemit.c`
- `xdiff/xhistogram.c`
- `xdiff/xmerge.c`
- `xdiff/xpatience.c`
- `xdiff/xprepare.c`
- `xdiff/xtypes.h`
- `xdiff/xutils.c`
- `xdiff/xutils.h`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `run_revert` | `modified` | `add-interactive.c` | `804-889` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 2 | `record_ws_error` | `modified` | `apply.c` | `1627-1656` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 3 | `adjust_incomplete` | `added` | `apply.c` | `1695-1708` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 4 | `parse_fragment` | `modified` | `apply.c` | `1716-1826` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 5 | `check_preimage` | `modified` | `apply.c` | `3768-3847` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 6 | `stream_blocked` | `modified` | `archive-tar.c` | `130-149` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 7 | `write_zip_entry` | `modified` | `archive-zip.c` | `294-563` | `unmatched` | unmatched; level=unmatched; diff_hunks=7; fallback_calls=0 |
| 8 | `parse_treeish_arg` | `modified` | `archive.c` | `485-552` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 9 | `attr_state_queue_push` | `added` | `attr.c` | `1072-1079` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 10 | `attr_state_queue_pop` | `added` | `attr.c` | `1081-1084` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 11 | `attr_state_queue_release` | `added` | `attr.c` | `1086-1089` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 12 | `fill_one` | `modified` | `attr.c` | `1091-1114` | `unmatched` | unmatched; level=unmatched; diff_hunks=6; fallback_calls=0 |
| 13 | `macroexpand_one` | `deleted` | `attr.c` | `1109-1117` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 14 | `register_ref` | `added` | `bisect.c` | `453-472` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 15 | `register_ref` | `deleted` | `bisect.c` | `453-473` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 16 | `mark_for_removal` | `added` | `bisect.c` | `1180-1186` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 17 | `mark_for_removal` | `deleted` | `bisect.c` | `1181-1190` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 18 | `has_entries_with_high_bit` | `modified` | `bloom.c` | `355-389` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 19 | `validate_branchname` | `modified` | `branch.c` | `373-383` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 20 | `fast_forward_to` | `modified` | `builtin/am.c` | `1995-2029` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 21 | `merge_tree` | `modified` | `builtin/am.c` | `2035-2063` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 22 | `clean_index` | `modified` | `builtin/am.c` | `2069-2105` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 23 | `inc_nr` | `added` | `builtin/bisect.c` | `366-371` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 24 | `inc_nr` | `deleted` | `builtin/bisect.c` | `366-374` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 25 | `add_bisect_ref` | `added` | `builtin/bisect.c` | `554-561` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 26 | `add_bisect_ref` | `deleted` | `builtin/bisect.c` | `557-565` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 27 | `get_first_good` | `added` | `builtin/bisect.c` | `1169-1173` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 28 | `get_first_good` | `deleted` | `builtin/bisect.c` | `1173-1180` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 29 | `git_blame_config` | `modified` | `builtin/blame.c` | `710-802` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 30 | `blame_diff_algorithm_minimal` | `added` | `builtin/blame.c` | `841-853` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 31 | `blame_diff_algorithm_callback` | `added` | `builtin/blame.c` | `855-871` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 32 | `cmd_blame` | `modified` | `builtin/blame.c` | `928-1306` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 33 | `copy_or_rename_branch` | `modified` | `builtin/branch.c` | `575-674` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 34 | `stream_blob` | `modified` | `builtin/cat-file.c` | `96-101` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 35 | `batch_object_write` | `modified` | `builtin/cat-file.c` | `471-565` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 36 | `batch_each_object` | `modified` | `builtin/cat-file.c` | `839-871` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 37 | `reset_tree` | `modified` | `builtin/checkout.c` | `705-745` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 38 | `merge_working_tree` | `modified` | `builtin/checkout.c` | `789-950` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 39 | `add_pending_uninteresting_ref` | `deleted` | `builtin/checkout.c` | `1066-1072` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 40 | `add_pending_uninteresting_ref` | `added` | `builtin/checkout.c` | `1068-1072` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 41 | `setup_new_branch_info_and_source_tree` | `modified` | `builtin/checkout.c` | `1259-1294` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 42 | `checkout_main` | `modified` | `builtin/checkout.c` | `1768-1986` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 43 | `checkout` | `modified` | `builtin/clone.c` | `637-740` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 44 | `cmd_clone` | `modified` | `builtin/clone.c` | `864-1650` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 45 | `create_base_index` | `modified` | `builtin/commit.c` | `311-339` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 46 | `format_config` | `modified` | `builtin/config.c` | `270-333` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 47 | `collect_config` | `modified` | `builtin/config.c` | `350-383` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 48 | `get_value` | `modified` | `builtin/config.c` | `385-499` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 49 | `get_urlmatch` | `modified` | `builtin/config.c` | `704-759` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 50 | `cmd_config_set` | `modified` | `builtin/config.c` | `965-1022` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 51 | `cmd_config_unset` | `modified` | `builtin/config.c` | `1024-1060` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 52 | `replace_name` | `modified` | `builtin/describe.c` | `99-130` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 53 | `get_name` | `added` | `builtin/describe.c` | `157-234` | `unmatched` | unmatched; level=unmatched; diff_hunks=6; fallback_calls=0 |
| 54 | `get_name` | `deleted` | `builtin/describe.c` | `157-234` | `unmatched` | unmatched; level=unmatched; diff_hunks=6; fallback_calls=0 |
| 55 | `append_name` | `modified` | `builtin/describe.c` | `334-357` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 56 | `stdin_diff_trees` | `modified` | `builtin/diff-tree.c` | `48-63` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 57 | `handle_commit` | `modified` | `builtin/fast-export.c` | `680-872` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 58 | `handle_tag` | `modified` | `builtin/fast-export.c` | `883-1032` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 59 | `end_packfile` | `modified` | `builtin/fast-import.c` | `868-943` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 60 | `store_object` | `modified` | `builtin/fast-import.c` | `951-1092` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 61 | `stream_blob` | `modified` | `builtin/fast-import.c` | `1101-1211` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 62 | `add_gpgsig_to_commit` | `modified` | `builtin/fast-import.c` | `2778-2794` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 63 | `finalize_commit_buffer` | `added` | `builtin/fast-import.c` | `2827-2837` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 64 | `handle_strip_if_invalid` | `added` | `builtin/fast-import.c` | `2839-2876` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 65 | `parse_new_commit` | `modified` | `builtin/fast-import.c` | `2878-3027` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 66 | `handle_tag_signature` | `modified` | `builtin/fast-import.c` | `3029-3067` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 67 | `add_one_refname` | `added` | `builtin/fetch.c` | `292-298` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 68 | `add_one_refname` | `deleted` | `builtin/fetch.c` | `292-300` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 69 | `add_oid` | `added` | `builtin/fetch.c` | `1417-1423` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 70 | `add_oid` | `deleted` | `builtin/fetch.c` | `1419-1428` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 71 | `commit_ref_transaction` | `added` | `builtin/fetch.c` | `1688-1712` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 72 | `do_fetch` | `modified` | `builtin/fetch.c` | `1714-1985` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 73 | `check_unreachable_object` | `modified` | `builtin/fsck.c` | `292-362` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 74 | `fsck_handle_reflog_ent` | `modified` | `builtin/fsck.c` | `508-524` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 75 | `fsck_handle_ref` | `deleted` | `builtin/fsck.c` | `533-565` | `unmatched` | unmatched; level=unmatched; diff_hunks=6; fallback_calls=0 |
| 76 | `snapshot_ref` | `added` | `builtin/fsck.c` | `551-584` | `unmatched` | unmatched; level=unmatched; diff_hunks=7; fallback_calls=0 |
| 77 | `get_default_heads` | `deleted` | `builtin/fsck.c` | `571-613` | `unmatched` | unmatched; level=unmatched; diff_hunks=6; fallback_calls=0 |
| 78 | `fsck_handle_ref` | `added` | `builtin/fsck.c` | `586-597` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 79 | `snapshot_refs` | `added` | `builtin/fsck.c` | `599-659` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 80 | `free_snapshot_refs` | `added` | `builtin/fsck.c` | `662-667` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| ... | ... | ... | ... | ... | ... | truncated at 80 of 905 functions |

## Function-Level Diff Snippets

### 1. `run_revert` in `add-interactive.c`

```diff
-		tree = parse_tree_indirect(&oid);
+		tree = repo_parse_tree_indirect(s->r, &oid);
```

### 2. `record_ws_error` in `apply.c`

```diff
+	/*
+	 * line[len] for an incomplete line points at the "\n" at the end
+	 * of patch input line, so "%.*s" would drop the last letter on line;
+	 * compensate for it.
+	 */
+	if (result & WS_INCOMPLETE_LINE)
+		len++;
+
```

### 3. `adjust_incomplete` in `apply.c`

```diff
+static int adjust_incomplete(const char *line, int len,
+			     unsigned long size)
+{
+	int nextlen;
+
+	if (*line != '\n' && *line != ' ' && *line != '+' && *line != '-')
+		return 0;
+	if (size - len < 12 || memcmp(line + len, "\\ ", 2))
+		return 0;
+	nextlen = linelen(line + len, size - len);
+	if (nextlen < 12)
+		return 0;
... truncated 2 additional diff lines ...
```

### 4. `parse_fragment` in `apply.c`

```diff
+	int skip_len = 0;
+
+		/*
+		 * For an incomplete line, skip_len counts the bytes
+		 * on "\\ No newline..." marker line that comes next
+		 * to the current line.
+		 *
+		 * Reduce "len" to drop the newline at the end of
+		 * line[], but add one to "skip_len", which will be
+		 * added back to "len" for the next iteration, to
+		 * compensate.
+		 */
... truncated 30 additional diff lines ...
```

### 5. `check_preimage` in `apply.c`

```diff
-		if (trust_executable_bit)
+		if (trust_executable_bit || !S_ISREG(st->st_mode))
```

### 6. `stream_blocked` in `archive-tar.c`

```diff
-	struct git_istream *st;
-	enum object_type type;
-	unsigned long sz;
+	struct odb_read_stream *st;
-	st = open_istream(r, oid, &type, &sz, NULL);
+	st = odb_read_stream_open(r->objects, oid, NULL);
-		readlen = read_istream(st, buf, sizeof(buf));
+		readlen = odb_read_stream_read(st, buf, sizeof(buf));
-	close_istream(st);
+	odb_read_stream_close(st);
```

### 7. `write_zip_entry` in `archive-zip.c`

```diff
-	struct git_istream *stream = NULL;
+	struct odb_read_stream *stream = NULL;
-			enum object_type type;
-			stream = open_istream(args->repo, oid, &type, &size,
-					      NULL);
+			stream = odb_read_stream_open(args->repo->objects, oid, NULL);
+			size = stream->size;
-			readlen = read_istream(stream, buf, sizeof(buf));
+			readlen = odb_read_stream_read(stream, buf, sizeof(buf));
-		close_istream(stream);
+		odb_read_stream_close(stream);
-			readlen = read_istream(stream, buf, sizeof(buf));
... truncated 3 additional diff lines ...
```

### 8. `parse_treeish_arg` in `archive.c`

```diff
-	tree = parse_tree_indirect(&oid);
+	tree = repo_parse_tree_indirect(the_repository, &oid);
```

### 9. `attr_state_queue_push` in `attr.c`

```diff
+static void attr_state_queue_push(struct attr_state_queue *t,
+				 const struct match_attr *a)
+{
+	for (size_t i = 0; i < a->num_attr; i++) {
+		ALLOC_GROW(t->items, t->nr + 1, t->alloc);
+		t->items[t->nr++] = &a->state[i];
+	}
+}
```

### 10. `attr_state_queue_pop` in `attr.c`

```diff
+static const struct attr_state *attr_state_queue_pop(struct attr_state_queue *t)
+{
+	return t->nr ? t->items[--t->nr] : NULL;
+}
```

### 11. `attr_state_queue_release` in `attr.c`

```diff
+static void attr_state_queue_release(struct attr_state_queue *t)
+{
+	free(t->items);
+}
```

### 12. `fill_one` in `attr.c`

```diff
+	struct attr_state_queue todo = { 0 };
+	const struct attr_state *state;
+	attr_state_queue_push(&todo, a);
+	while (rem > 0 && (state = attr_state_queue_pop(&todo))) {
+		const struct git_attr *attr = state->attr;
+		const char *v = state->setto;
+			const struct all_attrs_item *item =
+				&all_attrs[attr->attr_nr];
+			if (item->macro && item->value == ATTR__TRUE)
+				attr_state_queue_push(&todo, item->macro);
+	attr_state_queue_release(&todo);
```

### 13. `macroexpand_one` in `attr.c`

```diff
-static int macroexpand_one(struct all_attrs_item *all_attrs, int nr, int rem)
-{
-	const struct all_attrs_item *item = &all_attrs[nr];
-
-	if (item->macro && item->value == ATTR__TRUE)
-		return fill_one(all_attrs, item->macro, rem);
-	else
-		return rem;
-}
```

### 14. `register_ref` in `bisect.c`

```diff
+static int register_ref(const struct reference *ref, void *cb_data UNUSED)
+	if (!strcmp(ref->name, term_bad)) {
+		oidcpy(current_bad_oid, ref->oid);
+	} else if (starts_with(ref->name, good_prefix.buf)) {
+		oid_array_append(&good_revs, ref->oid);
+	} else if (starts_with(ref->name, "skip-")) {
+		oid_array_append(&skipped_revs, ref->oid);
```

### 15. `register_ref` in `bisect.c`

```diff
-static int register_ref(const char *refname, const char *referent UNUSED, const struct object_id *oid,
-			int flags UNUSED, void *cb_data UNUSED)
-	if (!strcmp(refname, term_bad)) {
-		oidcpy(current_bad_oid, oid);
-	} else if (starts_with(refname, good_prefix.buf)) {
-		oid_array_append(&good_revs, oid);
-	} else if (starts_with(refname, "skip-")) {
-		oid_array_append(&skipped_revs, oid);
```

### 16. `mark_for_removal` in `bisect.c`

```diff
+static int mark_for_removal(const struct reference *ref, void *cb_data)
+	char *bisect_ref = xstrfmt("refs/bisect%s", ref->name);
+	string_list_append(refs, bisect_ref);
```

### 17. `mark_for_removal` in `bisect.c`

```diff
-static int mark_for_removal(const char *refname,
-			    const char *referent UNUSED,
-			    const struct object_id *oid UNUSED,
-			    int flag UNUSED, void *cb_data)
-	char *ref = xstrfmt("refs/bisect%s", refname);
-	string_list_append(refs, ref);
```

### 18. `has_entries_with_high_bit` in `bloom.c`

```diff
-	if (parse_tree(t))
+	if (repo_parse_tree(r, t))
```

### 19. `validate_branchname` in `branch.c`

```diff
-				  _("See `man git check-ref-format`"));
+				  _("See 'git help check-ref-format'"));
```

### 20. `fast_forward_to` in `builtin/am.c`

```diff
-	if (parse_tree(head) || parse_tree(remote))
+	if (repo_parse_tree(the_repository, head) || repo_parse_tree(the_repository, remote))
```

### 21. `merge_tree` in `builtin/am.c`

```diff
-	if (parse_tree(tree))
+	if (repo_parse_tree(the_repository, tree))
```

### 22. `clean_index` in `builtin/am.c`

```diff
-	head_tree = parse_tree_indirect(head);
+	head_tree = repo_parse_tree_indirect(the_repository, head);
-	remote_tree = parse_tree_indirect(remote);
+	remote_tree = repo_parse_tree_indirect(the_repository, remote);
-	index_tree = parse_tree_indirect(&index);
+	index_tree = repo_parse_tree_indirect(the_repository, &index);
```

### 23. `inc_nr` in `builtin/bisect.c`

```diff
+static int inc_nr(const struct reference *ref UNUSED, void *cb_data)
```

### 24. `inc_nr` in `builtin/bisect.c`

```diff
-static int inc_nr(const char *refname UNUSED,
-		  const char *referent UNUSED,
-		  const struct object_id *oid UNUSED,
-		  int flag UNUSED, void *cb_data)
```

### 25. `add_bisect_ref` in `builtin/bisect.c`

```diff
+static int add_bisect_ref(const struct reference *ref, void *cb)
+	add_pending_oid(data->revs, ref->name, ref->oid, data->object_flags);
```

### 26. `add_bisect_ref` in `builtin/bisect.c`

```diff
-static int add_bisect_ref(const char *refname, const char *referent UNUSED, const struct object_id *oid,
-			  int flags UNUSED, void *cb)
-	add_pending_oid(data->revs, refname, oid, data->object_flags);
```

### 27. `get_first_good` in `builtin/bisect.c`

```diff
+static int get_first_good(const struct reference *ref, void *cb_data)
+	oidcpy(cb_data, ref->oid);
```

### 28. `get_first_good` in `builtin/bisect.c`

```diff
-static int get_first_good(const char *refname UNUSED,
-			  const char *referent UNUSED,
-			  const struct object_id *oid,
-			  int flag UNUSED, void *cb_data)
-	oidcpy(cb_data, oid);
```

### 29. `git_blame_config` in `builtin/blame.c`

```diff
-		string_list_insert(&ignore_revs_file_list, str);
+		if (str)
+			string_list_insert(&ignore_revs_file_list, str);
+	if (!strcmp(var, "diff.algorithm")) {
+		long diff_algorithm;
+		if (!value)
+			return config_error_nonbool(var);
+		diff_algorithm = parse_algorithm_value(value);
+		if (diff_algorithm < 0)
+			return error(_("unknown value for config '%s': %s"),
+				     var, value);
+		xdl_opts &= ~XDF_DIFF_ALGORITHM_MASK;
... truncated 4 additional diff lines ...
```

### 30. `blame_diff_algorithm_minimal` in `builtin/blame.c`

```diff
+static int blame_diff_algorithm_minimal(const struct option *option,
+					const char *arg, int unset)
+{
+	int *opt = option->value;
+
+	BUG_ON_OPT_ARG(arg);
+
+	*opt &= ~XDF_DIFF_ALGORITHM_MASK;
+	if (!unset)
+		*opt |= XDF_NEED_MINIMAL;
+
+	return 0;
... truncated 1 additional diff lines ...
```

### 31. `blame_diff_algorithm_callback` in `builtin/blame.c`

```diff
+static int blame_diff_algorithm_callback(const struct option *option,
+					 const char *arg, int unset)
+{
+	int *opt = option->value;
+	long value = parse_algorithm_value(arg);
+
+	BUG_ON_OPT_NEG(unset);
+
+	if (value < 0)
+		return error(_("option diff-algorithm accepts \"myers\", "
+			       "\"minimal\", \"patience\" and \"histogram\""));
+
... truncated 5 additional diff lines ...
```

### 32. `cmd_blame` in `builtin/blame.c`

```diff
+		OPT_CALLBACK_F(0, "diff-algorithm", &xdl_opts, N_("<algorithm>"),
+			       N_("choose a diff algorithm"),
+			       PARSE_OPT_NONEG, blame_diff_algorithm_callback),
+		OPT_CALLBACK_F(0, "minimal", &xdl_opts, NULL,
+			       N_("spend extra cycles to find a better match"),
+			       PARSE_OPT_NOARG | PARSE_OPT_HIDDEN, blame_diff_algorithm_minimal),
```

### 33. `copy_or_rename_branch` in `builtin/branch.c`

```diff
-					  _("See `man git check-ref-format`"));
+					  _("See 'git help check-ref-format'"));
```

### 34. `stream_blob` in `builtin/cat-file.c`

```diff
-	if (stream_blob_to_fd(1, oid, NULL, 0))
+	if (odb_stream_blob_to_fd(the_repository->objects, 1, oid, NULL, 0))
```

### 35. `batch_object_write` in `builtin/cat-file.c`

```diff
-			ret = packed_object_info(the_repository, pack,
-						 offset, &data->info);
+			ret = packed_object_info(pack, offset, &data->info);
```

### 36. `batch_each_object` in `builtin/cat-file.c`

```diff
-	struct bitmap_index *bitmap = prepare_bitmap_git(the_repository);
+	struct bitmap_index *bitmap = NULL;
-	if (bitmap && !for_each_bitmapped_object(bitmap, &opt->objects_filter,
-						 batch_one_object_bitmapped, &payload)) {
+	if (opt->objects_filter.choice != LOFC_DISABLED &&
+	    (bitmap = prepare_bitmap_git(the_repository)) &&
+	    !for_each_bitmapped_object(bitmap, &opt->objects_filter,
+				       batch_one_object_bitmapped, &payload)) {
```

### 37. `reset_tree` in `builtin/checkout.c`

```diff
-	if (parse_tree(tree) < 0)
+	if (repo_parse_tree(the_repository, tree) < 0)
```

### 38. `merge_working_tree` in `builtin/checkout.c`

```diff
-		new_tree = parse_tree_indirect(the_hash_algo->empty_tree);
+		new_tree = repo_parse_tree_indirect(the_repository,
+						    the_hash_algo->empty_tree);
-		tree = parse_tree_indirect(old_commit_oid);
+		tree = repo_parse_tree_indirect(the_repository,
+						old_commit_oid);
-		if (parse_tree(new_tree) < 0)
+		if (repo_parse_tree(the_repository, new_tree) < 0)
```

### 39. `add_pending_uninteresting_ref` in `builtin/checkout.c`

```diff
-static int add_pending_uninteresting_ref(const char *refname, const char *referent UNUSED,
-					 const struct object_id *oid,
-					 int flags UNUSED, void *cb_data)
-	add_pending_oid(cb_data, refname, oid, UNINTERESTING);
```

### 40. `add_pending_uninteresting_ref` in `builtin/checkout.c`

```diff
+static int add_pending_uninteresting_ref(const struct reference *ref, void *cb_data)
+	add_pending_oid(cb_data, ref->name, ref->oid, UNINTERESTING);
```

### 41. `setup_new_branch_info_and_source_tree` in `builtin/checkout.c`

```diff
-		*source_tree = parse_tree_indirect(rev);
+		*source_tree = repo_parse_tree_indirect(the_repository, rev);
```

### 42. `checkout_main` in `builtin/checkout.c`

```diff
-			die(_("could not resolve %s"), opts->from_treeish);
+			die(_("could not resolve '%s'"), opts->from_treeish);
```

### 43. `checkout` in `builtin/clone.c`

```diff
-	tree = parse_tree_indirect(&oid);
+	tree = repo_parse_tree_indirect(the_repository, &oid);
-	if (parse_tree(tree) < 0)
+	if (repo_parse_tree(the_repository, tree) < 0)
```

### 44. `cmd_clone` in `builtin/clone.c`

```diff
-		close_object_store(the_repository->objects);
+		odb_close(the_repository->objects);
```

### 45. `create_base_index` in `builtin/commit.c`

```diff
-	tree = parse_tree_indirect(&current_head->object.oid);
+	tree = repo_parse_tree_indirect(the_repository,
+					&current_head->object.oid);
-	if (parse_tree(tree) < 0)
+	if (repo_parse_tree(the_repository, tree) < 0)
```

### 46. `format_config` in `builtin/config.c`

```diff
-			strbuf_addstr(buf, v);
+			if (v)
+				strbuf_addstr(buf, v);
+			else
+				return 1; /* :(optional)no-such-file */
```

### 47. `collect_config` in `builtin/config.c`

```diff
+	int status;
-	return format_config(data->display_opts, &values->items[values->nr++],
-			     key_, value_, kvi);
+	status = format_config(data->display_opts, &values->items[values->nr++],
+			       key_, value_, kvi);
+	if (status < 0)
+		return status;
+	if (status) {
+		strbuf_release(&values->items[--values->nr]);
+		status = 0;
+	}
+	return status;
```

### 48. `get_value` in `builtin/config.c`

```diff
+		int status;
-		if (format_config(display_opts, item, key_,
-				  display_opts->default_value, &kvi) < 0)
+
+		status = format_config(display_opts, item, key_,
+				       display_opts->default_value, &kvi);
+		if (status < 0)
+		if (status) {
+			/* default was a missing optional value */
+			values.nr--;
+			strbuf_release(item);
+		}
```

### 49. `get_urlmatch` in `builtin/config.c`

```diff
+		int status;
-		format_config(&display_opts, &buf, item->string,
-			      matched->value_is_null ? NULL : matched->value.buf,
-			      &matched->kvi);
-		fwrite(buf.buf, 1, buf.len, stdout);
+		status = format_config(&display_opts, &buf, item->string,
+				       matched->value_is_null ? NULL : matched->value.buf,
+				       &matched->kvi);
+		if (!status)
+			fwrite(buf.buf, 1, buf.len, stdout);
```

### 50. `cmd_config_set` in `builtin/config.c`

```diff
-			"       Use a regexp, --add or --replace-all to change %s."), argv[0]);
+			"       Use --value=<pattern>, --append or --all to change %s."), argv[0]);
```

### 51. `cmd_config_unset` in `builtin/config.c`

```diff
+		OPT_BIT(0, "all", &flags, N_("unset all multi-valued config options"), CONFIG_FLAGS_MULTI_REPLACE),
+		OPT_STRING(0, "value", &value_pattern, N_("pattern"), N_("unset multi-valued config options with matching values")),
```

### 52. `replace_name` in `builtin/describe.c`

```diff
-			if (!t || parse_tag(t))
+			if (!t || parse_tag(the_repository, t))
-		if (!t || parse_tag(t))
+		if (!t || parse_tag(the_repository, t))
```

### 53. `get_name` in `builtin/describe.c`

```diff
+static int get_name(const struct reference *ref, void *cb_data UNUSED)
+	if (skip_prefix(ref->name, "refs/tags/", &path_to_match)) {
+		    !skip_prefix(ref->name, "refs/heads/", &path_to_match) &&
+		    !skip_prefix(ref->name, "refs/remotes/", &path_to_match)) {
+	if (!reference_get_peeled_oid(the_repository, ref, &peeled)) {
+		is_annotated = !oideq(ref->oid, &peeled);
+		oidcpy(&peeled, ref->oid);
+	add_to_known_names(all ? ref->name + 5 : ref->name + 10,
+			   &peeled, prio, ref->oid);
```

### 54. `get_name` in `builtin/describe.c`

```diff
-static int get_name(const char *path, const char *referent UNUSED, const struct object_id *oid,
-		    int flag UNUSED, void *cb_data UNUSED)
-	if (skip_prefix(path, "refs/tags/", &path_to_match)) {
-		    !skip_prefix(path, "refs/heads/", &path_to_match) &&
-		    !skip_prefix(path, "refs/remotes/", &path_to_match)) {
-	if (!peel_iterated_oid(the_repository, oid, &peeled)) {
-		is_annotated = !oideq(oid, &peeled);
-		oidcpy(&peeled, oid);
-	add_to_known_names(all ? path + 5 : path + 10, &peeled, prio, oid);
```

### 55. `append_name` in `builtin/describe.c`

```diff
-		if (!n->tag || parse_tag(n->tag))
+		if (!n->tag || parse_tag(the_repository, n->tag))
```

### 56. `stdin_diff_trees` in `builtin/diff-tree.c`

```diff
-	if (!tree2 || parse_tree(tree2))
+	if (!tree2 || repo_parse_tree(the_repository, tree2))
```

### 57. `handle_commit` in `builtin/fast-export.c`

```diff
-		case SIGN_ABORT:
-			die(_("encountered signed commit %s; use "
-			      "--signed-commits=<mode> to handle it"),
-			    oid_to_hex(&commit->object.oid));
+		/* Exporting modes */
+
+		/* Stripping modes */
+
+		/* Aborting modes */
+		case SIGN_ABORT:
+			die(_("encountered signed commit %s; use "
+			      "--signed-commits=<mode> to handle it"),
... truncated 6 additional diff lines ...
```

### 58. `handle_tag` in `builtin/fast-export.c`

```diff
-			case SIGN_ABORT:
-				die(_("encountered signed tag %s; use "
-				      "--signed-tags=<mode> to handle it"),
-				    oid_to_hex(&tag->object.oid));
+			/* Exporting modes */
+
+			/* Stripping modes */
+
+			/* Aborting modes */
+			case SIGN_ABORT:
+				die(_("encountered signed tag %s; use "
+				      "--signed-tags=<mode> to handle it"),
... truncated 6 additional diff lines ...
```

### 59. `end_packfile` in `builtin/fast-import.c`

```diff
-		new_p = packfile_store_load_pack(pack_data->repo->objects->packfiles,
+		new_p = packfile_store_load_pack(pack_data->repo->objects->sources->packfiles,
```

### 60. `store_object` in `builtin/fast-import.c`

```diff
-	struct packfile_store *packs = the_repository->objects->packfiles;
+	struct odb_source *source;
-	} else if (find_oid_pack(&oid, packfile_store_get_packs(packs))) {
+	}
+
+	for (source = the_repository->objects->sources; source; source = source->next) {
+		if (!packfile_list_find_oid(packfile_store_get_packs(source->packfiles), &oid))
+			continue;
```

### 61. `stream_blob` in `builtin/fast-import.c`

```diff
+	struct odb_source *source;
+		goto out;
+	}
-	} else if (find_oid_pack(&oid, packfile_store_get_packs(packs))) {
+	for (source = the_repository->objects->sources; source; source = source->next) {
+		if (!packfile_list_find_oid(packfile_store_get_packs(source->packfiles), &oid))
+			continue;
-
-	} else {
-		e->depth = 0;
-		e->type = OBJ_BLOB;
-		e->pack_id = pack_id;
... truncated 14 additional diff lines ...
```

### 62. `add_gpgsig_to_commit` in `builtin/fast-import.c`

```diff
+	if (!sig || !sig->hash_algo)
```

### 63. `finalize_commit_buffer` in `builtin/fast-import.c`

```diff
+static void finalize_commit_buffer(struct strbuf *new_data,
+				   struct signature_data *sig_sha1,
+				   struct signature_data *sig_sha256,
+				   struct strbuf *msg)
+{
+	add_gpgsig_to_commit(new_data, "gpgsig ", sig_sha1);
+	add_gpgsig_to_commit(new_data, "gpgsig-sha256 ", sig_sha256);
+
+	strbuf_addch(new_data, '\n');
+	strbuf_addbuf(new_data, msg);
+}
```

### 64. `handle_strip_if_invalid` in `builtin/fast-import.c`

```diff
+static void handle_strip_if_invalid(struct strbuf *new_data,
+				    struct signature_data *sig_sha1,
+				    struct signature_data *sig_sha256,
+				    struct strbuf *msg)
+{
+	struct strbuf tmp_buf = STRBUF_INIT;
+	struct signature_check signature_check = { 0 };
+	int ret;
+
+	/* Check signature in a temporary commit buffer */
+	strbuf_addbuf(&tmp_buf, new_data);
+	finalize_commit_buffer(&tmp_buf, sig_sha1, sig_sha256, msg);
... truncated 26 additional diff lines ...
```

### 65. `parse_new_commit` in `builtin/fast-import.c`

```diff
+		case SIGN_STRIP_IF_INVALID:
-	add_gpgsig_to_commit(&new_data, "gpgsig ", &sig_sha1);
-	add_gpgsig_to_commit(&new_data, "gpgsig-sha256 ", &sig_sha256);
+	if (signed_commit_mode == SIGN_STRIP_IF_INVALID &&
+	    (sig_sha1.hash_algo || sig_sha256.hash_algo))
+		handle_strip_if_invalid(&new_data, &sig_sha1, &sig_sha256, &msg);
+	else
+		finalize_commit_buffer(&new_data, &sig_sha1, &sig_sha256, &msg);
-	strbuf_addch(&new_data, '\n');
-	strbuf_addbuf(&new_data, &msg);
```

### 66. `handle_tag_signature` in `builtin/fast-import.c`

```diff
+	/* Third, aborting modes */
+	case SIGN_ABORT:
+		die(_("encountered signed tag; use "
+		      "--signed-tags=<mode> to handle it"));
+	case SIGN_STRIP_IF_INVALID:
+		die(_("'strip-if-invalid' is not a valid mode for "
+		      "git fast-import with --signed-tags=<mode>"));
```

### 67. `add_one_refname` in `builtin/fetch.c`

```diff
+static int add_one_refname(const struct reference *ref, void *cbdata)
+	(void) refname_hash_add(refname_map, ref->name, ref->oid);
```

### 68. `add_one_refname` in `builtin/fetch.c`

```diff
-static int add_one_refname(const char *refname, const char *referent UNUSED,
-			   const struct object_id *oid,
-			   int flag UNUSED, void *cbdata)
-	(void) refname_hash_add(refname_map, refname, oid);
```

### 69. `add_oid` in `builtin/fetch.c`

```diff
+static int add_oid(const struct reference *ref, void *cb_data)
+	oid_array_append(oids, ref->oid);
```

### 70. `add_oid` in `builtin/fetch.c`

```diff
-static int add_oid(const char *refname UNUSED,
-		   const char *referent UNUSED,
-		   const struct object_id *oid,
-		   int flags UNUSED, void *cb_data)
-	oid_array_append(oids, oid);
```

### 71. `commit_ref_transaction` in `builtin/fetch.c`

```diff
+static int commit_ref_transaction(struct ref_transaction **transaction,
+				  bool is_atomic, const char *remote_name,
+				  struct strbuf *err)
+{
+	int retcode = ref_transaction_commit(*transaction, err);
+	if (retcode)
+		goto out;
+
+	if (!is_atomic) {
+		struct ref_rejection_data data = {
+			.conflict_msg_shown = 0,
+			.remote_name = remote_name,
... truncated 13 additional diff lines ...
```

### 72. `do_fetch` in `builtin/fetch.c`

```diff
-	retcode = ref_transaction_commit(transaction, &err);
-	if (retcode) {
-		/*
-		 * Explicitly handle transaction cleanup to avoid
-		 * aborting an already closed transaction.
-		 */
-		ref_transaction_free(transaction);
-		transaction = NULL;
+	retcode = commit_ref_transaction(&transaction, atomic_fetch,
+					 transport->remote->name, &err);
+	/*
+	 * With '--atomic', bail out if the transaction fails. Without '--atomic',
... truncated 29 additional diff lines ...
```

### 73. `check_unreachable_object` in `builtin/fsck.c`

```diff
-				if (stream_blob_to_fd(fileno(f), &obj->oid, NULL, 1))
+				if (odb_stream_blob_to_fd(the_repository->objects, fileno(f),
+							  &obj->oid, NULL, 1))
```

### 74. `fsck_handle_reflog_ent` in `builtin/fsck.c`

```diff
+	if (now && timestamp > now)
+		return 0;
+
```

### 75. `fsck_handle_ref` in `builtin/fsck.c`

```diff
-static int fsck_handle_ref(const char *refname, const char *referent UNUSED, const struct object_id *oid,
-			   int flag UNUSED, void *cb_data UNUSED)
-	obj = parse_object(the_repository, oid);
-		if (is_promisor_object(the_repository, oid)) {
-		      refname, oid_to_hex(oid));
-	if (obj->type != OBJ_COMMIT && is_branch(refname)) {
-		error(_("%s: not a commit"), refname);
-			     oid, "%s", refname);
```

### 76. `snapshot_ref` in `builtin/fsck.c`

```diff
+static int snapshot_ref(const struct reference *ref, void *cb_data)
+	struct snapshot *snap = cb_data;
+	obj = parse_object(the_repository, ref->oid);
+		if (is_promisor_object(the_repository, ref->oid)) {
+		      ref->name, oid_to_hex(ref->oid));
+	if (obj->type != OBJ_COMMIT && is_branch(ref->name)) {
+		error(_("%s: not a commit"), ref->name);
+
+	ALLOC_GROW(snap->ref, snap->nr + 1, snap->alloc);
+	snap->ref[snap->nr].refname = xstrdup(ref->name);
+	oidcpy(&snap->ref[snap->nr].oid, ref->oid);
+	snap->nr++;
... truncated 3 additional diff lines ...
```

### 77. `get_default_heads` in `builtin/fsck.c`

```diff
-static void get_default_heads(void)
-			     fsck_handle_ref, NULL);
-		struct strbuf ref = STRBUF_INIT;
-		strbuf_worktree_ref(wt, &ref, "HEAD");
-		fsck_head_link(ref.buf, &head_points_at, &head_oid);
-		if (head_points_at && !is_null_oid(&head_oid))
-			fsck_handle_ref(ref.buf, NULL, &head_oid, 0, NULL);
-		strbuf_release(&ref);
-		if (include_reflogs)
-	free_worktrees(worktrees);
```

### 78. `fsck_handle_ref` in `builtin/fsck.c`

```diff
+static int fsck_handle_ref(const struct reference *ref, void *cb_data UNUSED)
+{
+	struct object *obj;
+
+	obj = parse_object(the_repository, ref->oid);
+			     ref->oid, "%s", ref->name);
```

### 79. `snapshot_refs` in `builtin/fsck.c`

```diff
+static void snapshot_refs(struct snapshot *snap, int argc, const char **argv)
+	for (int i = 0; i < argc; i++) {
+		const char *arg = argv[i];
+		struct object_id oid;
+		if (!repo_get_oid(the_repository, arg, &oid)) {
+			struct reference ref = {
+				.name = arg,
+				.oid = &oid,
+			};
+
+			snapshot_ref(&ref, snap);
+			continue;
... truncated 39 additional diff lines ...
```

### 80. `free_snapshot_refs` in `builtin/fsck.c`

```diff
+static void free_snapshot_refs(struct snapshot *snap)
+{
+	for (size_t i = 0; i < snap->nr; i++)
+		free(snap->ref[i].refname);
+	free(snap->ref);
+}
```

## Mock Release-Note Drafts

- No mock release-note output available.

## Ground-Truth Drafting Workspace

| GT ID | Section | Semantic Release-Note Entry | Supporting Evidence | Decision |
| --- | --- | --- | --- | --- |
| GT-001 |  |  |  | pending |

## Excluded Or Low-Level Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
|  |  |  |

## Reviewer Notes

- Record uncertainty, alternative interpretations, and final consensus here.
