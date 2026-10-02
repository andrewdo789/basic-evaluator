# Rubric: safety toolcraft, ARENA 1.2

Grader only.

Ask the person to run every test cell in `1.2_Intro_to_Mech_Interp_exercises.ipynb` and paste the outputs, and to
confirm the solutions files were not opened.

| Result | Level |
| --- | --- |
| Every exercise test passes, solutions never opened | 7 |
| The TransformerLens and induction-head sections pass; later sections (hooks, ablation, reverse-engineering) incomplete | 6, provisional |
| Only the first section passes | 5, provisional |
| Solutions opened for any exercise | that exercise does not count |

Then ask three questions aloud (record pass or fail): what an induction head attends to and why it needs a previous-token
head; what `run_with_cache` returns; what zero-ablating a head can mislead you about. Two of three must be right for
level 7 to stand.
