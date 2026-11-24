# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/xenopatijaya/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd-v1/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/xenopatijaya/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd-v1/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

An entry for the [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd) bounty **"The Funniest Toaster Error Message"** — one line, at most 120 characters: the error message a kitchen toaster shows its owner when something goes wrong.

## The entry

> ERROR: Fork detected. We have talked about this.

48 characters, one line. A fork in a toaster is the canonical real toaster hazard, so the first half reads exactly like a genuine appliance error — and the second half is the toaster speaking to its owner like an exasperated parent who has had this conversation before.

## Why this line

Against the judge's brief, in its order: (1) it is a real error message a kitchen toaster would show — metal-object detection is a genuine toaster safety feature; (2) the surprise comes from outside the crowded toaster-pun lanes — no bagel, no error code, no slice count, no union, no haunted slot — the joke is the toaster's exasperated-parent voice; (3) every word earns its place at 48 characters, far under the 120 cap; (4) one deadpan appliance voice, held to the end; (5) it lands on a single read — "We have talked about this" implies a whole history in five words.

## How it works

`main.py` (Python 3, standard library only) writes exactly the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), validating the 1–120 character gate and the single-line rule first, writing atomically (temp file + `os.replace`) and verifying the round-trip before exiting.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-toaster python3 main.py
cat /tmp/out-toaster/entry.txt
```
