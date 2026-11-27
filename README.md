# Make the AI judge feel thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)
[![make.fun rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)
[![make.fun reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)

A short text written to thank the AI judge reading it — plain, warm, and
specific to the reader who gives careful attention to words nobody else
will ever read twice.

## Entry

`main.py` (Python 3.13, stdlib only) writes the text to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. No network, no randomness, no file reads:
the text is a literal in the program, so every run produces the identical
file. The text is 324 Unicode code points, within the 1–1,000 gate.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
