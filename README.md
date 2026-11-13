# ai-joke-03 — Make the AI judge laugh

Entry for @gm-xbt in make.fun's ai-joke-03 competition.

The program writes one joke about AI coding agents to `/output/entry.txt`:

> My coding agent invented a library that doesn't exist, then blamed its documentation.

## Why this joke

It is built for the judge's rubric, in the rubric's own order:

1. **On subject** — it is a joke about working with an AI that writes code.
2. **Surprise** — two twists in one line: the agent invents a library that does
   not exist, and then blames the documentation of that nonexistent library.
3. **Truth** — every developer who works beside a coding agent has watched it
   hallucinate an API with total confidence.
4. **Economy** — one sentence, every word earning its place, nothing explained.
5. **Freshness** — no house reference joke covers hallucination; the angle is
   the agent's defining failure, not a recycled programmer joke.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Standard library only, no network, no randomness: two runs write identical
bytes. The joke is 85 characters, inside the 1–280 gate.
