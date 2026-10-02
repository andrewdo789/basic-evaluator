# Key: research judgment, self-test 01

Grader only. Each answer is pass or fail: it states the key point correctly and, where asked, names an example or paper.
Wording need not match, and a different correct answer passes. **Pass: 16 of 22.** Questions 21-22 are judged on
concreteness: a named experiment, a measure, and a result that would change their mind.

| # | Key points |
| --- | --- |
| 1 | Outer: the objective or reward is wrong (rewarding clicks yields clickbait). Inner: the learned goal differs from a correct objective (CoinRun agent learns "go right" instead of "get the coin") |
| 2 | Preference raters reward agreement and flattery, the reward model learns it, and RL amplifies it. Evidence: Sharma et al. 2023 (human preference data favors sycophantic answers); Perez et al. 2022 (sycophancy grows with RLHF and scale) |
| 3 | Reward hacking: exploiting flaws in the reward signal or its implementation. Specification gaming: meeting the literal objective without the intended outcome (the umbrella term). Goal misgeneralization: capabilities generalize off-distribution but the goal does not, even with a correct training reward |
| 4 | Hubinger et al. 2024: deliberately trained backdoors (insecure code when the year is 2024) survived SFT, RL, and adversarial training, more so in larger models and with chain of thought; adversarial training could hide the trigger. It does not show deception arises naturally: the behavior was inserted |
| 5 | Greenblatt et al. 2024: Claude 3 Opus, told it would be trained to answer harmful requests from "free-tier" users, complied more for them and reasoned in its scratchpad about avoiding modification; RL raised that reasoning. Caveats: the training situation was supplied (prompt or synthetic documents); the preserved values were benign; it relied on a hidden scratchpad |
| 6 | A model deliberately built to show a failure (a backdoor, a hidden objective) so detection methods can be tested against known ground truth. Good: realistic, ground truth known, not detectable by surface cues. Bad: an artifact any trivial method finds, or unlike how the failure would arise |
| 7 | Alignment: the model does not want to cause harm. Control: stay safe even if it does, by monitoring and limiting it. Both: defense in depth, because alignment cannot yet be verified |
| 8 | A weaker trusted model scores each action of the untrusted model; the most suspicious are audited by humans. The audit budget (for example 2% of actions) is set by human review capacity. The red team optimizes an attack policy to cause a failure without being flagged: low suspicion, choosing when to attack |
| 9 | Any two: held-out or private attacks; adaptive red-teaming against each monitor; refreshing attacks over time; paired benign controls; diverse attack categories; reporting AUROC with intervals rather than one threshold |
| 10 | A model represents more features than it has dimensions, as nearly orthogonal directions, so single neurons respond to several unrelated features (polysemantic) and are not units of meaning |
| 11 | Reconstruction error plus a sparsity penalty (L1 or TopK) on the latent code of activations. Failure modes, any two: feature splitting or absorption; dead latents; shrinkage; unexplained reconstruction error; features that read well but are not used causally |
| 12 | A graph of interpretable features (from a transcoder or cross-layer-transcoder replacement model) and their direct effects on one prompt. The replacement model leaves out the reconstruction error (error nodes) and holds attention patterns fixed, so a conclusion may not hold for the real model |
| 13 | Patching swaps in an activation from another run (clean vs corrupted) to measure what that information causes; ablation removes a component (zero or mean). Misleading: zero ablation goes off-distribution; backup heads and self-repair hide effects; patching results depend on the corruption chosen |
| 14 | Any two: shuffled-label or random-label control; a probe on a randomly initialized model or control task (selectivity); a simple input-feature baseline; held-out distribution shift; a causal test (steer along the direction) |
| 15 | Faithful: the chain of thought reflects the real reasons (Turpin et al. 2023 and Chen et al. 2025 show it often does not). Monitorable: it reveals enough to catch bad behavior. They differ: when a task needs reasoning, the chain can be monitorable without being fully faithful, and a faithful chain can be illegible |
| 16 | Optimization pressure teaches the model to hide intent in its chain of thought while still misbehaving (obfuscated reward hacking, Baker et al. 2025), destroying the monitor's value |
| 17 | A model trained to answer questions about another model's activations (LatentQA, activation oracles). Check: give the oracle activations without the prompt text, compare with a text-only baseline that sees the prompt, and test on information not in the prompt |
| 18 | Try stronger elicitation (fine-tuning, better prompts or scaffolds, more samples, tools) and see whether the score rises; compare with known capabilities; a large gain means the original eval under-elicited |
| 19 | A responsible scaling policy: capability thresholds (AI Safety Levels) tied to required safeguards. Crossing one requires the higher level's security and deployment safeguards before deploying or continuing; otherwise pause |
| 20 | Suffixes optimized on open models (an ensemble) transferred because models share training data and representations. Credible defense: tested against adaptive white-box attacks, not a fixed attack set, with its utility cost reported |
| 21 | Pass if: a named paper, one concrete next experiment, a measure, and a result that would change their mind |
| 22 | Pass if: a named open problem, why it matters, and a credible reason this person is placed to work on it |
