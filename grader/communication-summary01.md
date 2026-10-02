# Rubric: communication, summary 01 (blind)

Grader only. Run by a fresh agent that has seen nothing but the paper (arXiv 2411.00640, fetch the full text) and the
summary. The main agent then checks each reported factual error against the paper before recording.

## Marks

1. **Factual errors.** Any claim that misstates the paper. Any one fails the test. Quote the summary sentence and the
   contradicting paper text with its section. A vague but not wrong statement is not an error.
2. **Required parts**, each present, partial, or missing: the question; at least three concrete practices; the evidence
   or argument behind each; the limits; why an eval builder should care.
3. **Claims without their limits.**
4. **Unclear sentences**: any a newcomer could not follow (undefined terms, garbled phrasing).

**Pass:** no factual errors, all five parts present, at most two unclear sentences. Report a word count.

## What the paper says (for checking)

- Treat eval questions as drawn from a large unseen super-population of questions. This is a modelling assumption about
  the questions the eval already has, not advice to subsample.
- Report the standard error of the mean score (via the Central Limit Theorem) and the number of questions.
- When questions come in groups (several per passage, one question in several languages), use clustered standard
  errors; naive ones can be several times too small.
- Variance can be reduced by resampling answers per question (cuts only the per-question noise, with diminishing
  returns) and, for evals without chain of thought, by using next-token probabilities instead of sampled answers.
- Do not lower the temperature to reduce noise unless you mean to study the model at that temperature.
- Compare models with paired differences on the same questions; it removes shared question difficulty.
- Use power analysis to choose how many questions an eval needs to detect a given difference.
- Limits: it says nothing about whether an eval measures the right thing; variance from the choice of questions can be
  reduced only by adding questions; everything rests on the super-population assumption.
