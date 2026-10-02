# Level 2: scanning

Add two read methods. Level 1 behaviour must keep working.

- `scan(key) -> list[str]`
  Return every field of the record as strings `"<field>(<value>)"`, sorted by field name (plain string order). Return `[]` if the record doesn't exist.
- `scan_by_prefix(key, prefix) -> list[str]`
  Same format and order, but only fields whose name starts with `prefix`. Return `[]` if none match or the record doesn't exist.

Example: after `set("A", "b", "2")` and `set("A", "a", "1")`, `scan("A")` returns `["a(1)", "b(2)"]`.

Run: `python -m unittest tests.test_level2 -v`
