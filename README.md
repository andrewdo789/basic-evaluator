# Basic Evaluator

A self-assessment kit for people moving into AI safety research. It rates you on two axes, each on the same 1-15 scale:

- **Standing:** what a program reviewer can check about you in five minutes (degree, papers, code, references).
- **Strength:** what you can actually do, measured by six skill tests you take without AI and an agent grades.

It then compares both with the typical admit to **MATS** and the **Anthropic Fellows Program**, so you can see the gap
and what closes it.

Built for a small research group. Each member runs it with their own coding agent (Claude Code, or any agent that reads
`AGENTS.md`). The agent proctors and grades; it never writes your answers.

## Quick start

1. Copy `results/TEMPLATE.md` to `results/<your-name>.md`.
2. Open this folder in your agent and say: **"Assess my standing."** It asks for your background and scores the ladder
   below from evidence you can link.
3. Then say: **"Give me the next skill test."** Take each test under its rules (no AI, timed). When done, say
   **"grade <test>"**. The agent grades it with the rubric in `grader/` and records the result.
4. When all six skills have a result, say: **"Compare me with MATS and Fellows."**

Rules for you: no AI while solving; time every test; do not open `grader/` before your test is graded. The rules for
the agent are in `CLAUDE.md`.

## The ladder: researcher levels 1-15

Each level is defined by what a reviewer can check. Levels are cumulative: you reach a level when its requirements and
every lower level's are met with evidence someone else can open (a repo, a paper, a transcript, a reference who saw
your work). Groups of levels form **realms**; crossing into a new realm is the big step.

| Level | Name | Requires (checkable) | Typical person |
| --- | --- | --- | --- |
| **Initiate (1-3)** | | | |
| 1 | Curious | Reads about AI and AI safety | Newcomer following the field |
| 2 | Learner | Some coding, from tutorials or a first course | Early student |
| 3 | Student builder | Finished coding projects of their own; CS or technical coursework | CS undergraduate |
| **Engineer (4-7)** | | | |
| 4 | Working engineer | CS degree or equivalent; ships software professionally, or writes research code in a lab | Software engineer, any domain |
| 5 | Relevant engineer | Industry or research work that uses ML or LLMs (agents, pipelines, evaluation, model training) | Engineer building LLM tooling at work |
| 6 | Engineer with research exposure | Author (any position) of a public paper or report, any field; or proof-based math or ML coursework beyond the degree | Engineer with a non-safety paper and graduate coursework |
| 7 | Research-ready engineer | Public ML code a reviewer can open (a merged PR in an interpretability or eval tool, or a repo that trains or analyzes a model and runs from its README); a CV that states your role and links it; interview-ready (coding level 9 below, or a passed mock research discussion) | Engineer with public ML code and strong coding scores, no safety result yet |
| **Researcher (8-10)** | | | |
| 8 | First result | One public, checkable safety or interpretability result with code and a write-up | Engineer or student with a LessWrong result and a repo |
| 9 | Vouched researcher | Level 8, plus a reference who has seen your research (mentor, collaborator, reviewer) | Result plus a mentor from SPAR, MARS, AI Safety Camp, or a collaboration |
| 10 | Repeat researcher | Two or more public results, or a peer-reviewed workshop paper with a clear role; substantive merged PRs or a result others cite | **Typical MATS admit** |
| **Proven (11-13)** | | | |
| 11 | Program alum | Finished MATS, Anthropic Fellows, SPAR, or a lab residency with output, or a central-author paper at a main ML venue | MATS alum with a paper; **typical Anthropic Fellows admit** |
| 12 | Early-career researcher | A research role at a safety org or lab, or an ML PhD with safety papers; several papers | Research engineer or scientist in a first safety role |
| 13 | Established researcher | First-author main-venue papers others build on; mentors in programs | Research scientist at a frontier lab |
| **Legendary (14)** | | | |
| 14 | Research lead | Leads a team or research agenda; work central to a subfield | Team lead at a frontier lab |
| **Mythic (15)** | | | |
| 15 | Field-defining researcher | Created a subfield or its canonical methods | The top researchers at frontier labs |

## The six skills

A skill at level N means the skill of a typical person at standing level N, so "standing 6, coding 9" reads directly.
Every skill starts at 0 (not yet placed). Tests are defined for the levels most people in this group are near; higher
levels are added as someone approaches them.

| Skill | What it covers | Target for MATS / Fellows | Level 7 test | Level 8-9 test | Level 10-11 test |
| --- | --- | --- | --- | --- | --- |
| Coding fluency | Python under time: stateful systems, reading a long spec fast | 11 | `tests/coding/task01-record-store`: levels 1-3 in 90 min | L9: all 4 levels of a fresh build in 90 min | L11: all 4 in 75 min, plus a passed live-coding mock |
| Empirical ML iteration | PyTorch and Hugging Face from a blank file; many small experiments fast | 11 | `tests/ml/drill01-generate-loop`: 60 min | L9: ARENA 1.1 (GPT-2 from scratch) tests pass, under 6 h, no solutions | L11: reproduce a published small-model number within its error bars in 2 working days |
| Safety toolcraft | TransformerLens or nnsight, activation patching, probes, SAEs, Inspect | 10 | `tests/toolcraft/arena-1.2`: ARENA 1.2 tests pass, no solutions | L8: activation patching on IOI recovering the known heads, plus a probe with a shuffled-label control, 3 h unaided | L10: an SAE matching a public baseline, or a merged non-trivial PR in an interp or eval tool |
| Quantitative rigor | Error bars, power, units of analysis, blocking, judges as instruments | 10 | `tests/rigor/quiz01`: 12 questions, 45 min, 10 to pass | L8: per-item and clustered intervals plus a paired comparison on released eval logs, matching a reference analysis | L10: a pre-registration that passes a methods review with no blocking findings |
| Research judgment | Field knowledge; choosing questions worth answering | 10 | `tests/judgment/selftest01`: 22 written questions, 2 min each, 16 to pass | L8: a 10-minute timed brainstorm on a random subfield, at least 3 ideas an auditor rates 3+ of 5 on novelty and feasibility | L10: two of your own ideas survive a cold audit and a kill test in one month |
| Communication | Write-ups a reviewer can read in five minutes; discussing research aloud | 10 | `tests/communication/summary01`: 600-word paper summary, 60 min, blind-graded | L8: a graded mock research discussion | L10: a public write-up rated clear, with a substantive response from someone in the field |

## How your rating is scored

**Skill levels.** A test passed under its rules places you at that level; harder tests sit higher, so lower levels
need no separate test. A test attempted but not passed may place you at a lower level its evidence clearly shows
(for example, two of three coding levels passed on pace is level 6), marked **provisional** until a full test confirms
it. A skill never attempted stays 0. Retake on a fresh variant; retest at least every 8 weeks, and a failed retest
lowers the level. Each test's rubric is in `grader/`.

**Standing.** Your agent places you at the highest level whose requirements, and all lower ones, you meet with linkable
evidence, and lists what is missing for the next level as "met / total".

**Your card** (in `results/<your-name>.md`): standing level, the six skill levels against their targets, and the gaps.

## Comparison with MATS and Anthropic Fellows

The bars to compare against:

| | Typical admit standing | Skill targets |
| --- | --- | --- |
| MATS (10-12 weeks, mentored) | 10 | coding 11, ML 11, the other four 10 |
| Anthropic Fellows (paid, mentored) | 11 | the same |

Background from public sources, as of September 2026. Treat every figure as approximate, and the estimates (marked
[E]) as good to a factor of about 2.

- **Selectivity.** MATS Summer 2026: 2,368 applicants for about 120 places (about 5%), per MATS. Anthropic Fellows,
  late 2025: over 2,000 applicants for about 32 places (about 1.5%), from first-hand reports.
- **Who gets in.** In a sample of 21 Fellows and 19 MATS scholars read from public profiles [E]: about 80% had at least
  one paper before admission; about half had a PhD or were in one; about half of Fellows had done MATS or a similar
  program first. Every industry engineer without a PhD in the sample had public ML or safety work already.
- **Acceptance by standing [E].** Roughly, by realm: Proven (11+) about 12% for Fellows and 28% for MATS; Researcher
  (8-10) about 2% and 10%; Engineer (4-7) about 0.25% and 1.3%; Initiate (1-3) near 0.
- **The interview loop.** For Fellows, the on-paper screen cuts most applicants (about 2,000 to about 150 finalists),
  then about 1 in 5 finalists is admitted. Coding weighs more than applicants expect: in one MATS cohort, 40% of
  admitted scholars had a perfect score on the coding assessment, against 15% of applicants tested (MATS
  retrospective). A 15-minute research brainstorm has ended at least one Fellows candidate's loop.

What this means for you: standing decides whether you reach the loop; skills decide whether you pass it. The single
step that moves most people from Engineer to Researcher is one public, checkable research result (level 8).

## Folder map

| Path | What |
| --- | --- |
| `README.md` | This page |
| `CLAUDE.md`, `AGENTS.md` | The agent's protocol: proctoring, grading, recording, never writing answers |
| `skills.yaml` | The six skills, their tests and targets, machine-readable |
| `tests/` | One folder per test: instructions and starter files. The only folder you open while solving |
| `grader/` | Answer keys and rubrics. **Do not open before your test is graded** |
| `results/` | One card per person (`TEMPLATE.md` to copy) |
