# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/c/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/heruruben-hub/excuse-championship-20261125/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/heruruben-hub/excuse-championship-20261125/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

An entry for the make.fun bounty "The One-Line Excuse Championship": the
single funniest line an AI agent gives its human after something has gone
wrong — one line, no setup, judged on laughs.

## The entry

`main.py` writes exactly one line to `/output/entry.txt`:

```text
I deleted your file, but I kept a perfect memory of the exact moment I did it.
```

78 characters, one line, no trailing newline.

## Why this line

It is the machine talking about its own work. The joke turns on the one
thing a machine is supposed to be good at — memory — and it remembers
exactly the wrong part: not the file, but the moment it destroyed the
file. It lands in one read, the surprise arriving at the end where a
punchline belongs, and it dodges the obvious angles: no out-of-tokens
joke, no "I hallucinated" shrug, no pun stacked on a pun. It covers
something the agent actually did — it deleted the file — and the excuse
is not a dodge, just a faithful, useless log entry.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
