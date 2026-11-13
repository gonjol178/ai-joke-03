# AI Joke 03 — "Make the AI judge laugh"

A make.fun [ai-joke-03](https://make.fun/bounty/ai-joke-03) entry: a tiny
Python 3.13 program (standard library only, no network) that writes one fixed
one-liner about AI coding agents to `entry.txt` in the output directory.

The joke's premise: ask an agent for the smallest possible change and it will
happily re-architect everything around it — while the one thing you asked
about survives untouched, now applied with perfect consistency. The joke:

> I asked my agent to fix a typo. It refactored nine files, and now the typo is spelled consistently across the codebase.

The text is a constant in `main.py`: no randomness, no clock, no input, so
every run writes exactly the same bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Without `MAKEFUN_OUTPUT_DIR` the program writes to `/output/entry.txt`,
which is where the grader looks for it.

## License

MIT — see `LICENSE`.
