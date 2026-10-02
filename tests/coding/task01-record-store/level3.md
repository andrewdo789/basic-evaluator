# Level 3: timestamps and time-to-live

Every operation now gets a version that takes a `timestamp` (an int). Within one test, timestamps passed to these methods strictly increase. Tests at this level use only the `_at` methods, so levels 1 and 2 keep their own behaviour.

- `set_at(key, field, value, timestamp) -> None`
  Like `set`. The field never expires.
- `set_at_with_ttl(key, field, value, timestamp, ttl) -> None`
  Like `set`, but the field exists only during `[timestamp, timestamp + ttl)`: at `timestamp + ttl` it has expired. Setting a field again replaces its value and its expiry (a plain `set_at` makes it permanent again).
- `get_at(key, field, timestamp) -> str | None`
- `delete_at(key, field, timestamp) -> bool`
  Returns `False` if the field has expired.
- `scan_at(key, timestamp) -> list[str]`
- `scan_by_prefix_at(key, prefix, timestamp) -> list[str]`

Expired fields behave exactly as if deleted.

Run: `python -m unittest tests.test_level3 -v`
