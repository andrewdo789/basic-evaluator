# Key: quantitative rigor, quiz 01

Grader only. Each question is pass or fail: the number (where asked) within the tolerance, and reasoning that names the
key idea. Wording need not match. **Pass: 10 of 12.** Below 10, partial credit (README) can set level 5-6 only if the
misses are slips rather than missing concepts; otherwise the skill stays 0.

| # | Key answer | Pass if |
| --- | --- | --- |
| 1 | SE = sqrt(0.62 x 0.38 / 400) = 0.0243, about 2.4 points. 95% CI = 62% +/- 1.96 x 2.43 = about 57.2% to 66.8% | SE 2.3-2.5 points and a CI within 0.5 points of that |
| 2 | The 5 questions per passage are correlated (share a passage), so there are fewer than 400 independent pieces of information; the plain SE is too small. Report a clustered standard error (cluster by passage, 80 clusters), or bootstrap by passage | Names the dependence within passages and a cluster-level fix |
| 3 | A paired test on the per-item differences (paired t-test on the 400 differences, or McNemar's test for right/wrong). Both models answered the same items, and their per-item scores are correlated; pairing removes the shared item difficulty and gives a smaller SE. Checking two CIs for overlap ignores that correlation and is the wrong test (overlap does not imply no significant difference) | Names a paired test and the shared-items reason |
| 4 | n per condition = (z_0.975 + z_0.8)^2 x [p1(1-p1) + p2(1-p2)] / delta^2 = (1.96 + 0.84)^2 x (0.24 + 0.2275) / 0.05^2, about 1,470 per condition | Correct formula shown and an answer of 1,300-1,600 |
| 5 | 1 - 0.95^10 = 0.40 (40%). Bonferroni: test each at 0.05/10 = 0.005, which holds the chance of any false positive at 5% or below (Holm is uniformly better; Benjamini-Hochberg controls the false discovery rate instead) | About 40% and one named correction with what it controls |
| 6 | The unit is the training run (seed); n = 3 per condition, not the number of eval items. With 3 runs, seed-to-seed variation may easily cover 2 points | Unit = run or seed and n = 3 |
| 7 | Blocking: group units into homogeneous blocks and compare treatments within each block, so block-to-block variation leaves the error term. Factor: the model (run both probes on each of the 6 models and compare within model); layer or dataset are acceptable | A correct definition and a sensible factor |
| 8 | Randomization protects against unknown or unmeasured confounders and systematic assignment bias, and justifies the inference; blocking only removes known nuisance factors | Names unknown confounders |
| 9 | If the null hypothesis (and the test's assumptions) were true, data at least this extreme would occur 3% of the time. It is not the probability the null is true, not the effect size or its importance, and not a 97% chance of replication | Correct meaning and one correct "does not mean" |
| 10 | Intra-rater reliability (test-retest consistency, repeatability). Not enough: consistency is not accuracy; a judge can be consistently wrong or biased (length, position, style). Needs agreement with human or ground-truth labels, ideally chance-corrected (Cohen's kappa), since raw agreement can be high when labels are imbalanced | Names self-consistency or reliability and that it does not establish validity |
| 11 | Any two of: a confounder driving both (prompt topic, harmfulness, length); reverse direction (the model's refusal state drives the probe reading, so the probe reads refusal rather than causing it); 30 prompts selected or a few outliers driving the correlation; many probes or layers tried (selection). The causal test is an intervention: steer or ablate along the probe direction and measure refusal | Two distinct alternatives |
| 12 | Exploratory: generates hypotheses; findings are tentative and need confirmation. Confirmatory: tests a hypothesis stated in advance, so error rates mean what they say. Pre-registration fixes the hypotheses, primary metric, sample size or stopping rule, exclusions, and the analysis before seeing the data | Both claims distinguished and at least three pre-registered items |

Sources for graders who want depth: Miller, "Adding Error Bars to Evals" (arXiv 2411.00640) for 1-3 and 5; Cohen,
*Statistical Power Analysis* for 4; Box, Hunter and Hunter, *Statistics for Experimenters*, for 6-8; Shadish, Cook and
Campbell, *Experimental and Quasi-Experimental Designs*, for 11-12.
