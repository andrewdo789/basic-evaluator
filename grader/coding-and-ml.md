# Rubric: coding task 01 and ML drill 01

Grader only.

## Coding, task 01 (record store)

Run each level's tests from the task folder. Score like the real platform: each level counts when all its tests pass.

| Result | Level |
| --- | --- |
| Levels 1-3 pass inside 90 minutes | 7 |
| All 4 pass inside 90 minutes | 9 (this task is then spent; the next test is a fresh build) |
| Stopped or out of time with levels 1-2 passing on pace and level 3 close | 6, provisional |
| Only level 1, or levels 1-2 slowly | 5, provisional |
| Nothing passing | stays 0 |

Official time budgets for context: level 1 10-15 min, level 2 20-30, level 3 30-60, level 4 30-60. Note any test-file
reading or debugger use in the record.

Review in this order, one line each with an example from their code: correctness (which tests fail and the root cause,
named, not fixed); idioms (`key not in`, `setdefault`, sentinels such as `None` over magic numbers); extensibility (did
the data representation survive each new level, or was it patched).

## ML iteration, drill 01 (generation loop)

Run `python check.py` from the drill folder.

| Result | Level |
| --- | --- |
| All checks `ok` inside 60 minutes | 7 |
| Greedy loop matches and two of the other three pass, or all pass but over time | 6, provisional |
| Greedy loop only | 5, provisional |
| Nothing passing | stays 0 |

Review: the greedy loop (last-position logits, stopping rule); top-p (sorting, cumulative sum, always keeping the top
token, mapping back to vocabulary order); batching (left padding, attention mask, position ids that skip padding).
