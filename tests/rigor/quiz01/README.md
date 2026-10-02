# Quantitative rigor, quiz 01 (level-7 placement test)

**Clock:** 45 minutes. **No AI**; a calculator and Python are fine; no books or notes. **Pass:** 10 of 12. Each answer
is judged on the number (where there is one) and one sentence of reasoning. Write your answers below each question.

1. A model scores 62% on a 400-item benchmark. Give the standard error of that accuracy and a 95% confidence interval.
2. The same 400 items were written as 80 passages with 5 questions each. Why can the interval from question 1 be too
   narrow, and what do you report instead?
3. Model A scores 64% and model B 60% on the same 400 items. Which test compares them correctly, and why is it not
   two separate confidence intervals checked for overlap?
4. You want to detect a 5-point accuracy gain (60% to 65%) with 80% power at alpha = 0.05, with independent samples.
   Roughly how many items per condition do you need? Show the formula you used.
5. You compare one baseline against 10 prompt variants, each at alpha = 0.05. What is the chance of at least one false
   positive if nothing works? Name one correction and what it does.
6. You fine-tune with 3 seeds per condition and see a 2-point difference. What is the experimental unit, and what is n?
7. Define blocking in one sentence, and give one blocking factor you would use when comparing two probes across 6
   models.
8. What does randomization protect against that blocking does not?
9. A result is significant at p = 0.03. State what that p-value means in one sentence, and one thing it does not mean.
10. An LLM judge scores the same 200 transcripts twice and agrees with itself 88% of the time. Name the property this
    measures and one reason it is not enough to trust the judge.
11. You find a 0.9 correlation between a probe's score and the model's refusal rate across 30 prompts. Name two
    alternative explanations you would rule out before calling it causal.
12. Exploratory versus confirmatory: in one sentence each, what you are allowed to claim from each, and what a
    pre-registration fixes in advance.

## Your result

Date, minutes used. Then tell your agent "grade quiz01".
