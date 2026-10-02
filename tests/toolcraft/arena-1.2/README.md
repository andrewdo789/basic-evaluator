# Safety toolcraft, ARENA 1.2 (level-7 placement test)

**What:** the exercises of ARENA chapter 1.2, *Intro to Mech Interp* (TransformerLens, attention patterns, induction
heads, hooks, ablation). **Pass:** every exercise's test passes, **with the solutions files never opened**. No time cap;
record your hours. Ask your agent about concepts when stuck, never for code.

ARENA recommends chapters 0.0 (prerequisites and einops) and 1.1 (transformer from scratch) first. 1.1 is also the
ML-iteration level-9 test, so doing it first trains two skills.

## Setup

- **Course pages:** https://learn.arena.education/ (chapter 1, part 2).
- **Exercises:** `git clone https://github.com/callummcdougall/ARENA_3.0`, then
  `chapter1_transformer_interp/exercises/part2_intro_to_mech_interp/1.2_Intro_to_Mech_Interp_exercises.ipynb`.
  The `*_solutions.ipynb` and `solutions.py` beside it stay closed.
- **Easiest:** the Colab link on the course page (no install; GPT-2 small fits a free GPU).
- **Local, tested on Windows with an RTX 5090** (uv, Python 3.12). Do not install ARENA's whole `requirements.txt`: it
  points at CUDA 11.8 builds of PyTorch (too old for recent GPUs) and pins jax for chapter 2, which conflicts with
  chapter 1's numpy. Instead, from the ARENA root:

  ```powershell
  uv venv --python 3.12 .venv-arena
  .venv-arena\Scripts\activate
  uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
  $lines = Get-Content requirements.txt
  $end = ($lines | Select-String '^# Chapter 2' | Select-Object -First 1).LineNumber - 1
  $lines[0..($end-1)] | Where-Object { $_ -notmatch '^(--extra-index-url.*|torch|torchvision|torchaudio)\s*$' } | Set-Content req-ch01.txt -Encoding utf8
  uv pip install -r req-ch01.txt
  python -c "import torch, numpy, transformer_lens; print(torch.__version__, numpy.__version__, torch.cuda.is_available())"
  ```

  Expect a `+cu128` torch, numpy below 2, and `True`. Use the matching CUDA index for your GPU (cu121 or cu124 for
  older cards). Pick `.venv-arena` as the notebook kernel. The local course pages run from the ARENA root:
  `.venv-arena\Scripts\streamlit run chapter1_transformer_interp\instructions\Home.py` (launching from inside
  `instructions` breaks the app's path check).

## Your result

Date, total hours, sections finished, any test that would not pass. Then tell your agent "grade arena-1.2" and paste
the test outputs.
