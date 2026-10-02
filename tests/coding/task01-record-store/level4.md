# Level 4: backup and restore

Add snapshots. Timestamps still strictly increase across all `_at` calls, `backup` and `restore`.

- `backup(timestamp) -> int`
  Save the current state of the store as of `timestamp`, and return the number of records that have at least one unexpired field. For fields with a TTL, the backup remembers the **remaining** lifetime at `timestamp`, not the absolute expiry.
- `restore(timestamp, timestamp_to_restore) -> None`
  Replace the whole store with the latest backup taken at or before `timestamp_to_restore`. There is always at least one such backup. Fields with a TTL get their remaining lifetime counted from `timestamp` (the restore time). Fields that had expired by the backup time stay gone.

Example: a field set at t=10 with ttl=20 (expires at 30) and backed up at t=15 has 15 units left. Restored at t=100, it expires at 115.

Run: `python -m unittest tests.test_level4 -v`
