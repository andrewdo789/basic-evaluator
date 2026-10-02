"""Drill 01: fill the TODOs. Do not change signatures. Run `python check.py`."""
import torch


def greedy_generate(model, tokenizer, prompt: str, max_new_tokens: int) -> list[int]:
    """Return prompt ids + generated ids, greedy, without model.generate."""
    # TODO
    raise NotImplementedError


def apply_temperature(logits: torch.Tensor, temperature: float) -> torch.Tensor:
    # TODO
    raise NotImplementedError


def top_p_filter(logits: torch.Tensor, p: float) -> torch.Tensor:
    """logits [batch, vocab] -> same shape, tokens outside the nucleus set to -inf."""
    # TODO
    raise NotImplementedError


def sample_batch(model, tokenizer, prompts: list[str], max_new_tokens: int, temperature: float, top_p: float,
                 seed: int = 0) -> list[dict]:
    """Left-padded batched sampling; returns [{"prompt", "completion", "n_tokens"}, ...] in prompt order."""
    # TODO
    raise NotImplementedError
