# Evidence Pack: third_party_sqlite OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `sqlite_v6_0_0_2_to_v6_1`
- Repository: `third_party_sqlite`
- Category: `database`
- Reference version: `OpenHarmony-v6.0.0.2-Release`
- Target version: `OpenHarmony-v6.1-Release`
- Pipeline status: `verified_full_pipeline_mock`
- Ground-truth status: `draft_required`

## Evidence Sources To Inspect

- [ ] OpenHarmony v6.0 and v6.1 platform release notes if available
- [ ] commit_messages
- [ ] function_level_diff
- [ ] SQLite upstream changelog if matching changes are identifiable

## Local Artifacts

- Changed functions: `outputs/benchmark/third_party_sqlite/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/changed_functions.json`
- cmg_output: `outputs/benchmark/third_party_sqlite/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/cmg.json`
- prompt_input: `outputs/benchmark/third_party_sqlite/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/prompt_input.json`
- prompt_bundle: `outputs/benchmark/third_party_sqlite/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/prompt_bundle.json`
- release_note_mock_rule_family: `outputs/benchmark/third_party_sqlite/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/release_note_mock_rule_family.json`

## Pipeline Summary

- Commit count: `60`
- Changed C/C++ files: `6`
- Changed functions: `42`
- Patch only: `False`
- CMG matched entries: `18`
- CMG unmatched entries: `24`
- Fallback-context entries: `42`
- Diff-derived call edges: `239`
- Prompt entries: `42`
- Mock generated entries: `42`

## Commit Messages

- !337 merge cherry-pick-mr-336-1770605223304-auto into OpenHarmony-6.1-Release
- sync code to gitcode
- !334 merge master into master
- fix sqlite community issue of OOB read and infinite loop
- !333 merge master into master
- fix sqlite community issue of an integer overflow
- !331 merge change_zstd into master
- zstd redirect to libzstd.z.so
- !330 merge master into master
- add visibility path for plugins/data
- !328 merge master into master
- fix issus to add batch binlog replay
- !327 merge FixIssue into master
- fix issue while empty db
- !325 merge master into master
- Enhance dfx issue
- !323 merge master into master
- Return corrupt/busy through compressvfs
- !321 merge fix_rekey_ios_lock into master
- fix rekey ios lock error
- !318 merge master into master
- fix sqlite community integer overflow issue
- !317 merge fix_tcl into master
- fix rekey memory errors
- !316 merge fix_gn_patch into master
- !314 merge enhance_rekey_debug into master
- fix apply patch
- some fix of enhance rekey
- !315 merge FixFuzzIssue into master
- Fix compress func param mismatch issue
- !313 merge enhance_rekey_v5 into master
- enhance rekey
- merge FixJournalIssue into master
- Fix busy issue
- merge fix_codec_ret into master
- codec error return SQLITE_CORRUPT
- merge FixJournalIssue into master
- Fix unexpected journal file generate while operate compress db
- merge master into master
- merge master into master
- Fix error code missing
- fix CVE-2025-7709
- !300 Fix issue while open db Merge pull request !300 from MartinChoo/NotADbIssue
- !299 binlog replay add rollback on failure Merge pull request !299 from hongyangliu/master0911
- Fix issue while open db
- binlog replay add rollback on failure
- !297 Optimize log print Merge pull request !297 from MartinChoo/FixIssue
- !298 fix: not support pragma key Merge pull request !298 from tankaisheng/0910
- fix: not suppot pragma key
- Optimize log print
- !293 fix binlog with zeroblob Merge pull request !293 from hongyangliu/masterNew
- fix binlog not skip temp db
- !296 sync sqlite community fts3/fts5 issue Merge pull request !296 from ryne3366/sync_community_fixes
- sync sqlite community fts3/fts5 issue
- !292 Add debug for dirsync Merge pull request !292 from ryne3366/dirsync_debug
- Add debug for dirsync
- !291 Check file before open compress db Merge pull request !291 from MartinChoo/FixCompressIssue
- Check file before open compress db
- !290 fix binlog replay failed with single quotes Merge pull request !290 from hongyangliu/master0814
- fix binlog replay failed with single quotes

## Changed C/C++ Files

- `include/sqlite3sym.h`
- `src/shell.c`
- `src/sqlite3.c`
- `unittest/sqlite_binlog_test.cpp`
- `unittest/sqlite_codec_rekey_test.cpp`
- `unittest/sqlite_compress_test.cpp`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `output_hex_blob` | `modified` | `src/shell.c` | `18543-18562` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 2 | `sqlite3VdbeExec` | `modified` | `src/sqlite3.c` | `93100-101388` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 3 | `fts3IncrmergeWriter` | `modified` | `src/sqlite3.c` | `198918-198970` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 4 | `rtreenode` | `modified` | `src/sqlite3.c` | `210460-210501` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 5 | `sessionChangeHash` | `modified` | `src/sqlite3.c` | `221884-221925` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 6 | `sessionChangesetBufferTblhdr` | `modified` | `src/sqlite3.c` | `224782-224821` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 7 | `fts5DlidxLvlNext` | `modified` | `src/sqlite3.c` | `238110-238137` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 8 | `fts5WriteDlidxAppend` | `modified` | `src/sqlite3.c` | `240771-240829` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 9 | `UtPresetDb` | `modified` | `unittest/sqlite_binlog_test.cpp` | `41-63` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 10 | `BinlogReplayTest002` | `added` | `unittest/sqlite_binlog_test.cpp` | `185-232` | `matched` | matched; level=symbol+overlap; diff_hunks=1; fallback_calls=0 |
| 11 | `BinlogReplayTest003` | `added` | `unittest/sqlite_binlog_test.cpp` | `239-298` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 12 | `BinlogInterfaceTest001` | `added` | `unittest/sqlite_binlog_test.cpp` | `305-355` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 13 | `BinlogInterfaceTest002` | `added` | `unittest/sqlite_binlog_test.cpp` | `362-379` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 14 | `UtSqliteLogPrint` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `44-47` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 15 | `LibSQLiteRekeyTest::SetUpTestCase` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `57-62` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 16 | `LibSQLiteRekeyTest::TearDownTestCase` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `64-67` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 17 | `LibSQLiteRekeyTest::SetUp` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `69-72` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 18 | `LibSQLiteRekeyTest::TearDown` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `74-76` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 19 | `CreateTable` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `78-97` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 20 | `InsertRecords` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `100-127` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 21 | `QueryIndexInfo` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `130-157` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 22 | `GetRecordCount` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `160-178` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 23 | `PrepareDataForDb` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `180-186` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 24 | `QueryData` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `188-199` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 25 | `EncryptDbConfig` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `201-211` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 26 | `LibSQLiteRekeyTest001` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `218-263` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 27 | `LibSQLiteRekeyTest002` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `270-305` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 28 | `LibSQLiteRekeyTest003` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `312-357` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 29 | `LibSQLiteRekeyTest004` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `364-395` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 30 | `LibSQLiteRekeyTest005` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `402-433` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 31 | `LibSQLiteRekeyTest006` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `440-471` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 32 | `LibSQLiteRekeyTest007` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `478-509` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 33 | `LibSQLiteRekeyTest008` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `516-537` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 34 | `LibSQLiteRekeyTest009` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `544-569` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 35 | `LibSQLiteRekeyTest010` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `576-623` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 36 | `LibSQLiteRekeyTest011` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `631-678` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 37 | `LibSQLiteRekeyTest012` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `685-724` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 38 | `LibSQLiteRekeyTest013` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `731-773` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 39 | `LibSQLiteRekeyTest014` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `780-839` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 40 | `LibSQLiteRekeyTest015` | `added` | `unittest/sqlite_codec_rekey_test.cpp` | `846-895` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 41 | `CompressTest014` | `modified` | `unittest/sqlite_compress_test.cpp` | `724-757` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 42 | `CompressTest015` | `added` | `unittest/sqlite_compress_test.cpp` | `764-785` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |

## Function-Level Diff Snippets

### 1. `output_hex_blob` in `src/shell.c`

```diff
-  char *zStr = sqlite3_malloc(nBlob*2 + 1);
+  char *zStr = sqlite3_malloc64((i64)nBlob*2 + 1);
```

### 2. `sqlite3VdbeExec` in `src/sqlite3.c`

```diff
-  nByte = pIn1->n + pIn2->n;
+  nByte = pIn1->n;
+  nByte += pIn2->n;
```

### 3. `fts3IncrmergeWriter` in `src/sqlite3.c`

```diff
-  int nLeafEst = 0;               /* Blocks allocated for leaf nodes */
+  i64 nLeafEst = 0;               /* Blocks allocated for leaf nodes */
-      nLeafEst = sqlite3_column_int(pLeafEst, 0);
+      nLeafEst = sqlite3_column_int64(pLeafEst, 0);
```

### 4. `rtreenode` in `src/sqlite3.c`

```diff
-  if( nData<NCELL(&node)*tree.nBytesPerCell ) return;
+  if( nData<4+NCELL(&node)*tree.nBytesPerCell ) return;
```

### 5. `sessionChangeHash` in `src/sqlite3.c`

```diff
-    /* It is not possible for eType to be SQLITE_NULL here. The session
-    ** module does not record changes for rows with NULL values stored in
-    ** primary key columns. */
-    assert( !isPK || (eType!=0 && eType!=SQLITE_NULL) );
-      }else{
+      }else if( eType==SQLITE_TEXT || eType==SQLITE_BLOB ){
+      /* It should not be possible for eType to be SQLITE_NULL or 0x00 here,
+      ** as the session module does not record changes for rows with NULL
+      ** values stored in primary key columns. But a corrupt changesets
+      ** may contain such a value.  */
```

### 6. `sessionChangesetBufferTblhdr` in `src/sqlite3.c`

```diff
+
+    /* Break out of the loop if if the nul-terminator byte has been found.
+    ** Otherwise, read some more input data and keep seeking. If there is
+    ** no more input data, consider the changeset corrupt.  */
+    if( rc==SQLITE_OK && (pIn->iNext + nRead)>=pIn->nData ){
+      rc = SQLITE_CORRUPT_BKPT;
+    }
```

### 7. `fts5DlidxLvlNext` in `src/sqlite3.c`

```diff
-      i64 iVal;
+      u64 iVal;
-      iOff += fts5GetVarint(&pData->p[iOff], (u64*)&iVal);
+      iOff += fts5GetVarint(&pData->p[iOff], &iVal);
```

### 8. `fts5WriteDlidxAppend` in `src/sqlite3.c`

```diff
-      iVal = iRowid - pDlidx->iPrev;
+      iVal = (u64)iRowid - (u64)pDlidx->iPrev;
```

### 9. `UtPresetDb` in `unittest/sqlite_binlog_test.cpp`

```diff
-        "class INTEGER);";
+        "class INTEGER,"
+        "extra BLOB);";
```

### 10. `BinlogReplayTest002` in `unittest/sqlite_binlog_test.cpp`

```diff
+HWTEST_F(SqliteBinlogTest, BinlogReplayTest002, TestSize.Level1)
+{
+    /**
+     * @tc.steps: step1. open db and set binlog
+     * @tc.expected: step1. ok
+     */
+    sqlite3 *db = NULL;
+    EXPECT_EQ(sqlite3_open_v2(TEST_DB, &db,
+        SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE | SQLITE_OPEN_FULLMUTEX, nullptr), SQLITE_OK);
+    ASSERT_NE(db, nullptr);
+    UtEnableBinlog(db);
+    /**
... truncated 36 additional diff lines ...
```

### 11. `BinlogReplayTest003` in `unittest/sqlite_binlog_test.cpp`

```diff
+HWTEST_F(SqliteBinlogTest, BinlogReplayTest003, TestSize.Level1)
+{
+    /**
+     * @tc.steps: step1. open db and set binlog
+     * @tc.expected: step1. ok
+     */
+    sqlite3 *db = NULL;
+    EXPECT_EQ(sqlite3_open_v2(TEST_DB, &db,
+        SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE | SQLITE_OPEN_FULLMUTEX, nullptr), SQLITE_OK);
+    ASSERT_NE(db, nullptr);
+    UtEnableBinlog(db);
+    /**
... truncated 48 additional diff lines ...
```

### 12. `BinlogInterfaceTest001` in `unittest/sqlite_binlog_test.cpp`

```diff
+HWTEST_F(SqliteBinlogTest, BinlogInterfaceTest001, TestSize.Level0)
+{
+    /**
+     * @tc.steps: step1. open db and set binlog
+     * @tc.expected: step1. ok
+     */
+    sqlite3 *db = NULL;
+    EXPECT_EQ(sqlite3_open_v2(TEST_DB, &db,
+        SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE | SQLITE_OPEN_FULLMUTEX, nullptr), SQLITE_OK);
+    ASSERT_NE(db, nullptr);
+    UtEnableBinlog(db);
+    /**
... truncated 39 additional diff lines ...
```

### 13. `BinlogInterfaceTest002` in `unittest/sqlite_binlog_test.cpp`

```diff
+HWTEST_F(SqliteBinlogTest, BinlogInterfaceTest002, TestSize.Level0)
+{
+    /**
+     * @tc.steps: step1. open db and set binlog
+     * @tc.expected: step1. ok
+     */
+    sqlite3 *db = NULL;
+    EXPECT_EQ(sqlite3_open_v2(TEST_DB, &db,
+        SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE | SQLITE_OPEN_FULLMUTEX, nullptr), SQLITE_OK);
+    ASSERT_NE(db, nullptr);
+    UtEnableBinlog(db);
+    /**
... truncated 6 additional diff lines ...
```

### 14. `UtSqliteLogPrint` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static void UtSqliteLogPrint(const void *data, int err, const char *msg)
+{
+    std::cout << "LibSQLiteRekeyTest SQLite xLog err:" << err << ", msg:" << msg << std::endl;
+}
```

### 15. `LibSQLiteRekeyTest::SetUpTestCase` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+void LibSQLiteRekeyTest::SetUpTestCase(void)
+{
+    sqlite3_config(SQLITE_CONFIG_LOG, &UtSqliteLogPrint, NULL);
+    // permission 0770
+    mkdir(TEST_DIR, 0770);
+}
```

### 16. `LibSQLiteRekeyTest::TearDownTestCase` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+void LibSQLiteRekeyTest::TearDownTestCase(void)
+{
+    sqlite3_config(SQLITE_CONFIG_LOG, NULL, NULL);
+}
```

### 17. `LibSQLiteRekeyTest::SetUp` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+void LibSQLiteRekeyTest::SetUp(void)
+{
+    system("rm -rf " TEST_DB "*");
+}
```

### 18. `LibSQLiteRekeyTest::TearDown` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+void LibSQLiteRekeyTest::TearDown(void)
+{
+}
```

### 19. `CreateTable` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static void CreateTable(sqlite3* db, std::string tableName, std::string indexName)
+{
+    // Enable WAL (Write-Ahead Logging) mode
+    ASSERT_EQ(sqlite3_exec(db, "PRAGMA journal_mode=WAL;", nullptr, nullptr, nullptr), SQLITE_OK)
+        << "Failed to enable WAL mode: " << sqlite3_errmsg(db);
+    
+    const std::string sql = "CREATE TABLE " + tableName +
+        "(id INTEGER PRIMARY KEY, "
+        "name TEXT NOT NULL, "
+        "users TEXT UNIQUE);";
+    
+    ASSERT_EQ(sqlite3_exec(db, sql.c_str(), nullptr, nullptr, nullptr), SQLITE_OK)
... truncated 8 additional diff lines ...
```

### 20. `InsertRecords` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static void InsertRecords(sqlite3* db, const std::string& table, int count)
+{
+    const std::string sql = "INSERT INTO " + table + " VALUES (?,?,?);";
+    sqlite3_stmt* stmt = nullptr;
+    // Prepare statement
+    ASSERT_EQ(sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, nullptr), SQLITE_OK)
+        << "Prepare failed for " << table << ": " << sqlite3_errmsg(db);
+    // Insert test data
+    for (int i = 0; i < count; ++i) {
+        // Bind parameters based on table structure
+        std::string name = "User_" + std::to_string(i);
+        std::string users = "user" + std::to_string(i) + "@example.com";
... truncated 16 additional diff lines ...
```

### 21. `QueryIndexInfo` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static int QueryIndexInfo(sqlite3* db, const std::string &indexName)
+{
+    sqlite3_stmt* stmt = nullptr;
+    std::string sql = "PRAGMA index_info(" + indexName + ");";
+    
+    std::cout << "\nIndex Information for: " << indexName << "\n";
+    std::cout << "-----------------------------------\n";
+
+    int rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, nullptr);
+    if (rc != SQLITE_OK) {
+        std::cout << "Index info prepare failed: " << sqlite3_errmsg(db) << std::endl;
+        return rc;
... truncated 16 additional diff lines ...
```

### 22. `GetRecordCount` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static int GetRecordCount(sqlite3* db, std::string table, int &count)
+{
+    const std::string sqlCount = "SELECT COUNT(*) FROM " + table + ";";
+    sqlite3_stmt* stmt = nullptr;
+    int rc = sqlite3_prepare_v2(db, sqlCount.c_str(), -1, &stmt, nullptr);
+    if (rc != SQLITE_OK) {
+        std::cout << "Count preparation failed for " << table << std::endl;
+        return rc;
+    }
+        
+    rc = sqlite3_step(stmt);
+    if (rc != SQLITE_OK && rc != SQLITE_ROW && rc != SQLITE_DONE) {
... truncated 7 additional diff lines ...
```

### 23. `PrepareDataForDb` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static void PrepareDataForDb(sqlite3* db)
+{
+    CreateTable(db, "customers", "customers_idx");
+    CreateTable(db, "orders", "orders_idx");
+    InsertRecords(db, "customers", 50);
+    InsertRecords(db, "orders", 100);
+}
```

### 24. `QueryData` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static void QueryData(sqlite3* db)
+{
+    // Verify record counts
+    int count = 0;
+    EXPECT_EQ(GetRecordCount(db, "customers", count), SQLITE_OK) << "Incorrect get customer count";
+    EXPECT_EQ(count, 50) << "Incorrect customer count";
+    EXPECT_EQ(GetRecordCount(db, "orders", count), SQLITE_OK) << "Incorrect get order count";
+    EXPECT_EQ(count, 100) << "Incorrect customer count";
+    // Query index information
+    EXPECT_EQ(QueryIndexInfo(db, "customers_idx"), SQLITE_OK);
+    EXPECT_EQ(QueryIndexInfo(db, "orders_idx"), SQLITE_OK);
+}
```

### 25. `EncryptDbConfig` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+static void EncryptDbConfig(sqlite3* db, CodecConfig *config)
+{
+    // key size 32
+    ASSERT_EQ(sqlite3_key(db, config->pKey, config->nKey), SQLITE_OK);
+    const std::string sqlKey = "PRAGMA codec_cipher='" + std::string((const char *)config->pCipher) +
+        "';PRAGMA codec_hmac_algo='" + std::string((const char *)config->pHmacAlgo) + "';PRAGMA codec_kdf_algo='" +
+        std::string((const char *)config->pKdfAlgo) + "';PRAGMA codec_page_size='" +
+        std::to_string(config->pageSize) + "';PRAGMA codec_kdf_iter='" + std::to_string(config->kdfIter) + "';";
+    ASSERT_EQ(sqlite3_exec(db, sqlKey.c_str(), nullptr, nullptr, nullptr), SQLITE_OK)
+        << "execute " << sqlKey << " failed: " << sqlite3_errmsg(db);
+}
```

### 26. `LibSQLiteRekeyTest001` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest001, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA1", "KDF_SHA1", "01234567890123456789012345678901", 32, 5000, 1024
+    };
+    EncryptDbConfig(db, &config);
... truncated 34 additional diff lines ...
```

### 27. `LibSQLiteRekeyTest002` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest002, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA1", "KDF_SHA1", "01234567890123456789012345678901", 32, 5000, 1024
+    };
+    EncryptDbConfig(db, &config);
... truncated 24 additional diff lines ...
```

### 28. `LibSQLiteRekeyTest003` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest003, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA1", "KDF_SHA1", "01234567890123456789012345678901", 32, 5000, 1024
+    };
+    EncryptDbConfig(db, &config);
... truncated 34 additional diff lines ...
```

### 29. `LibSQLiteRekeyTest004` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest004, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA1", "KDF_SHA1", "01234567890123456789012345678901", 32, 5000, 1024
+    };
+    EncryptDbConfig(db, &config);
... truncated 20 additional diff lines ...
```

### 30. `LibSQLiteRekeyTest005` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest005, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA1", "KDF_SHA1", "01234567890123456789012345678901", 32, 5000, 1024
+    };
+    EncryptDbConfig(db, &config);
... truncated 20 additional diff lines ...
```

### 31. `LibSQLiteRekeyTest006` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest006, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    PrepareDataForDb(db);
+    sqlite3_close(db);
+    /**
+     * @tc.steps: step2. Rekey to unencrypt db and pagesize no changed
... truncated 20 additional diff lines ...
```

### 32. `LibSQLiteRekeyTest007` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest007, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    PrepareDataForDb(db);
+    sqlite3_close(db);
+    /**
+     * @tc.steps: step2. Rekey to unencrypt db and pagesize changed
... truncated 20 additional diff lines ...
```

### 33. `LibSQLiteRekeyTest008` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest008, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    PrepareDataForDb(db);
+
+    /**
+     * @tc.steps: step2. Rekey to unencrypt db and pagesize changed
... truncated 10 additional diff lines ...
```

### 34. `LibSQLiteRekeyTest009` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest009, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA256", "KDF_SHA256", "01234567890123456789012345678901", 32, 5000, 4096
+    };
+    EncryptDbConfig(db, &config);
... truncated 14 additional diff lines ...
```

### 35. `LibSQLiteRekeyTest010` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest010, TestSize.Level0)
+{
+    // 1. 创建匿名内存映射 (可读写/共享)
+    size_t mapSize = sizeof(int);
+    int *shared = (int *)mmap(nullptr, mapSize, PROT_READ | PROT_WRITE,
+        MAP_SHARED | MAP_ANONYMOUS, -1, 0);
+    ASSERT_NE(shared, MAP_FAILED);
+    *shared = MULPROC_STEP_1;
+    pid_t pid = fork();
+    ASSERT_GE(pid, 0);
+    // child
+    if (pid == 0) {
... truncated 36 additional diff lines ...
```

### 36. `LibSQLiteRekeyTest011` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest011, TestSize.Level0)
+{
+    // 1. 创建匿名内存映射 (可读写/共享)
+    size_t mapSize = sizeof(int);
+    int *shared = (int *)mmap(nullptr, mapSize, PROT_READ | PROT_WRITE,
+        MAP_SHARED | MAP_ANONYMOUS, -1, 0);
+    ASSERT_NE(shared, MAP_FAILED);
+    *shared = MULPROC_STEP_1;
+    pid_t pid = fork();
+    ASSERT_GE(pid, 0);
+    // child
+    if (pid == 0) {
... truncated 36 additional diff lines ...
```

### 37. `LibSQLiteRekeyTest012` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest012, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA256", "KDF_SHA256", "01234567890123456789012345678901", 32, 5000, 4096
+    };
+    EncryptDbConfig(db, &config);
... truncated 28 additional diff lines ...
```

### 38. `LibSQLiteRekeyTest013` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest013, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA256", "KDF_SHA256", "01234567890123456789012345678901", 32, 5000, 4096
+    };
+    EncryptDbConfig(db, &config);
... truncated 31 additional diff lines ...
```

### 39. `LibSQLiteRekeyTest014` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest014, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA1", "KDF_SHA1", "01234567890123456789012345678901", 32, 5000, 1024
+    };
+    EncryptDbConfig(db, &config);
... truncated 48 additional diff lines ...
```

### 40. `LibSQLiteRekeyTest015` in `unittest/sqlite_codec_rekey_test.cpp`

```diff
+HWTEST_F(LibSQLiteRekeyTest, LibSQLiteRekeyTest015, TestSize.Level0)
+{
+    sqlite3* db;
+    /**
+     * @tc.steps: step1. Open database and create table
+     * @tc.expected: step1. Return SQLITE_OK
+     */
+    ASSERT_EQ(sqlite3_open(TEST_DB, &db), SQLITE_OK);
+    CodecConfig config = {
+        "aes-256-gcm", "SHA1", "KDF_SHA1", "01234567890123456789012345678901", 32, 5000, 1024
+    };
+    EncryptDbConfig(db, &config);
... truncated 38 additional diff lines ...
```

### 41. `CompressTest014` in `unittest/sqlite_compress_test.cpp`

```diff
-    EXPECT_EQ(sqlite3_exec(slaveDb, UT_DML_INSERT_DEMO.c_str(), nullptr, nullptr, nullptr), SQLITE_OK);
+    for (int i = 0; i < 1000; i++) {  // 1000 means the total number of insert data
+        std::string insert = "INSERT INTO demo(id, name) VALUES(";
+        insert += std::to_string(1000 + i);  // 1000 means the start id of insert data
+        insert += ", '";
+        insert += std::string(100, 'a' + (i % ('z' - 'a'))) + "Call";  // 100 means the length of field's value
+        insert += "');";
+        EXPECT_EQ(sqlite3_exec(slaveDb, insert.c_str(), nullptr, nullptr, nullptr), SQLITE_OK);
+    }
-    Common::DestroyDbFile(slavePath, 2 * 4096, "testcase013");  // 2 * 4096 means the 2rd page's offset
+    Common::DestroyDbFile(slavePath, 5 * 4096, "testcase013");  // 5 * 4096 means the 6th page, belongs to vfs_pages
-    EXPECT_EQ(sqlite3_exec(slaveDb, "SELECT COUNT(name) FROM demo;", nullptr, nullptr, nullptr), SQLITE_IOERR);
... truncated 3 additional diff lines ...
```

### 42. `CompressTest015` in `unittest/sqlite_compress_test.cpp`

```diff
+HWTEST_F(SQLiteCompressTest, CompressTest015, TestSize.Level0)
+{
+    if (!IsSupportPageCompress()) {
+        GTEST_SKIP() << "Current testcase is not compatible";
+    }
+    std::string slavePath = TEST_DIR "/test015_slave.db";
+    sqlite3 *slaveDb = nullptr;
+    EXPECT_EQ(sqlite3_open_v2(slavePath.c_str(), &slaveDb, SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE, "compressvfs"),
+        SQLITE_OK);
+    sqlite3_close_v2(slaveDb);
+    EXPECT_EQ(sqlite3_open_v2(slavePath.c_str(), &slaveDb, SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE, "compressvfs"),
+        SQLITE_OK);
... truncated 8 additional diff lines ...
```

## Mock Release-Note Drafts

1. [Features] Add CreateTable: Added CreateTable.
2. [Features] Add EncryptDbConfig: Added EncryptDbConfig.
3. [Features] Add GetRecordCount: Added GetRecordCount.
4. [Features] Add InsertRecords: Added InsertRecords.
5. [Features] Add PrepareDataForDb: Added PrepareDataForDb.
6. [Features] Add QueryData: Added QueryData.
7. [Features] Add QueryIndexInfo: Added QueryIndexInfo.
8. [Features] Add UtSqliteLogPrint: Added UtSqliteLogPrint.
9. [Testing] Add LibSQLiteRekeyTest::SetUp: Added LibSQLiteRekeyTest::SetUp.
10. [Testing] Add LibSQLiteRekeyTest::SetUpTestCase: Added LibSQLiteRekeyTest::SetUpTestCase.
11. [Testing] Add LibSQLiteRekeyTest::TearDown: Added LibSQLiteRekeyTest::TearDown.
12. [Testing] Add LibSQLiteRekeyTest::TearDownTestCase: Added LibSQLiteRekeyTest::TearDownTestCase.
13. [Testing] Add a regression test for compressed-database corruption: Added a regression test for compressed-database corruption that expects query execution to surface an I/O error.
14. [Testing] Add regression coverage around BinlogInterfaceTest001: Added regression coverage around BinlogInterfaceTest001.
15. [Testing] Add regression coverage around BinlogInterfaceTest002: Added regression coverage around BinlogInterfaceTest002.
16. [Testing] Add regression coverage around BinlogReplayTest002: Added regression coverage around BinlogReplayTest002.
17. [Testing] Add regression coverage around BinlogReplayTest003: Added regression coverage around BinlogReplayTest003.
18. [Testing] Add regression coverage around CompressTest015: Added regression coverage around CompressTest015.
19. [Testing] Add regression coverage around LibSQLiteRekeyTest002: Added regression coverage around LibSQLiteRekeyTest002.
20. [Testing] Add regression coverage around LibSQLiteRekeyTest003: Added regression coverage around LibSQLiteRekeyTest003.
21. [Testing] Add regression coverage around LibSQLiteRekeyTest004: Added regression coverage around LibSQLiteRekeyTest004.
22. [Testing] Add regression coverage around LibSQLiteRekeyTest005: Added regression coverage around LibSQLiteRekeyTest005.
23. [Testing] Add regression coverage around LibSQLiteRekeyTest006: Added regression coverage around LibSQLiteRekeyTest006.
24. [Testing] Add regression coverage around LibSQLiteRekeyTest007: Added regression coverage around LibSQLiteRekeyTest007.
25. [Testing] Add regression coverage around LibSQLiteRekeyTest008: Added regression coverage around LibSQLiteRekeyTest008.
26. [Testing] Add regression coverage around LibSQLiteRekeyTest009: Added regression coverage around LibSQLiteRekeyTest009.
27. [Testing] Add regression coverage around LibSQLiteRekeyTest010: Added regression coverage around LibSQLiteRekeyTest010.
28. [Testing] Add regression coverage around LibSQLiteRekeyTest011: Added regression coverage around LibSQLiteRekeyTest011.
29. [Testing] Add regression coverage around LibSQLiteRekeyTest012: Added regression coverage around LibSQLiteRekeyTest012.
30. [Testing] Add regression coverage around LibSQLiteRekeyTest013: Added regression coverage around LibSQLiteRekeyTest013.
31. [Testing] Add regression coverage around LibSQLiteRekeyTest014: Added regression coverage around LibSQLiteRekeyTest014.
32. [Testing] Add regression coverage around LibSQLiteRekeyTest015: Added regression coverage around LibSQLiteRekeyTest015.
33. [Testing] Expand compressed database corruption tests: Added a regression test for corrupted compressed databases, verifying that invalid files are rejected with the expected not-a-database error.
34. [Internal] Update UtPresetDb: Updated UtPresetDb.
35. [Internal] Update fts3IncrmergeWriter: Updated fts3IncrmergeWriter.
36. [Internal] Update fts5DlidxLvlNext: Updated fts5DlidxLvlNext.
37. [Internal] Update fts5WriteDlidxAppend: Updated fts5WriteDlidxAppend.
38. [Internal] Update sessionChangeHash: Updated sessionChangeHash.
39. [Internal] Update sessionChangesetBufferTblhdr: Updated sessionChangesetBufferTblhdr.
40. [Internal] Update sqlite3VdbeExec: Updated sqlite3VdbeExec.
41. [Internal] Update the output_hex_blob routine: Updated the output_hex_blob routine.
42. [Internal] Update the rtreenode routine: Updated the rtreenode routine.

These drafts are generated evidence only. Do not copy them as ground truth without review.

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
