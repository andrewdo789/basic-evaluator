# ML iteration, drill 01: generation loop and sampling (level-7 placement test)

**Clock:** 60 minutes. **No AI**, no autocomplete that writes code; the PyTorch and Hugging Face docs are fine.
Model: GPT-2 small (`gpt2`, downloads once, runs on CPU or GPU). Fill every `# TODO` in `drill.py` without changing the
function signatures, then run `python check.py` from this folder. **Pass:** all checks print `ok` inside 60 minutes.
This is part A of the reported Colab LLM interview round in miniature. Needs `torch` and `transformers` installed.

What each function must do:
1. `greedy_generate`: your own loop (no `model.generate`): tokenize, forward pass, take the logits at the last
   position, pick the argmax, append, stop at `max_new_tokens` or the end-of-sequence token. It must match
   `model.generate(do_sample=False)` token for token.
2. `apply_temperature`: divide logits by the temperature (temperature > 0).
3. `top_p_filter`: keep the smallest set of tokens whose probability sums to at least `p` (always keep the top
   token), set the rest to `-inf`. Works on a batch of logits, shape `[batch, vocab]`.
4. `sample_batch`: generate from several prompts at once with temperature and top-p, using left padding, an
   attention mask, and position ids that skip the padding, and return a list of dicts `{"prompt", "completion", "n_tokens"}`.

## Your result

Date, minutes used, which checks passed, one line on what slowed you. Then tell your agent "grade drill01".
