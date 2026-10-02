# Level 1: basic records

Build an in-memory store of **records**. Each record has a string `key` and holds **fields**, each a string name with a string value.

Implement these methods on `RecordStore`:

- `set(key, field, value) -> None`
  Set `field` of record `key` to `value`. Create the record if it doesn't exist. Overwrite the value if the field exists.
- `get(key, field) -> str | None`
  Return the field's value, or `None` if the record or the field doesn't exist.
- `delete(key, field) -> bool`
  Remove the field. Return `True` if it existed, `False` otherwise. A record with no fields left no longer exists.

Run: `python -m unittest tests.test_level1 -v`
