"""Checks for drill 01. Each prints ok or FAIL with the reason. Needs torch and transformers."""
import math
import traceback

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

import drill


def run(name, fn):
    try:
        fn()
        print(f"ok    {name}")
        return True
    except Exception as e:  # noqa: BLE001
        print(f"FAIL  {name}: {type(e).__name__}: {e}")
        if not isinstance(e, (AssertionError, NotImplementedError)):
            traceback.print_exc(limit=2)
        return False


tok = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2").eval()


def greedy():
    for prompt in ["The capital of France is", "def fibonacci(n):"]:
        ids = tok(prompt, return_tensors="pt").input_ids
        with torch.no_grad():
            ref = model.generate(ids, max_new_tokens=12, do_sample=False, pad_token_id=tok.eos_token_id)[0].tolist()
            got = drill.greedy_generate(model, tok, prompt, 12)
        assert list(got) == ref, f"differs from model.generate at position {next((i for i, (a, b) in enumerate(zip(got, ref)) if a != b), min(len(got), len(ref)))}"


def temperature():
    x = torch.tensor([[2.0, 1.0, 0.0]])
    assert torch.allclose(drill.apply_temperature(x, 2.0), torch.tensor([[1.0, 0.5, 0.0]]))
    assert torch.allclose(drill.apply_temperature(x, 1.0), x)


def top_p():
    probs = torch.tensor([[0.5, 0.3, 0.15, 0.05], [0.9, 0.05, 0.03, 0.02]])
    out = drill.top_p_filter(probs.log(), 0.75)
    assert out.shape == probs.shape
    kept = torch.isfinite(out)
    assert kept.tolist() == [[True, True, False, False], [True, False, False, False]], f"kept {kept.tolist()}"
    assert torch.allclose(out[kept], probs.log()[kept]), "kept logits must be unchanged"
    shuffled = probs[:, [2, 0, 3, 1]]
    kept2 = torch.isfinite(drill.top_p_filter(shuffled.log(), 0.75)).tolist()
    assert kept2 == [[False, True, False, True], [False, True, False, False]], f"order-dependent: {kept2}"


def batch():
    prompts = ["Once upon a time", "The weather today", "In machine learning, a probe"]
    rows = drill.sample_batch(model, tok, prompts, max_new_tokens=8, temperature=0.8, top_p=0.9, seed=0)
    assert isinstance(rows, list) and len(rows) == 3
    for r, p in zip(rows, prompts):
        assert set(r) >= {"prompt", "completion", "n_tokens"}, f"row keys {set(r)}"
        assert r["prompt"] == p and isinstance(r["completion"], str) and 1 <= r["n_tokens"] <= 8
        assert tok.eos_token not in r["completion"] and "<pad>" not in r["completion"], "padding leaked into the text"
    again = drill.sample_batch(model, tok, prompts, max_new_tokens=8, temperature=0.8, top_p=0.9, seed=0)
    assert [r["completion"] for r in rows] == [r["completion"] for r in again], "same seed must give the same samples"
    cold = drill.sample_batch(model, tok, prompts, max_new_tokens=8, temperature=1e-4, top_p=1.0, seed=1)
    for r, p in zip(cold, prompts):
        g = drill.greedy_generate(model, tok, p, 8)
        want = tok.decode(g[len(tok(p).input_ids):])
        assert r["completion"].startswith(want[: max(1, len(want) // 2)]), f"near-zero temperature should match greedy for {p!r}"


results = [run(n, f) for n, f in [("greedy matches model.generate", greedy), ("temperature", temperature),
                                   ("top-p nucleus", top_p), ("batched sampling table", batch)]]
print(f"\n{sum(results)}/{len(results)} checks passed")
