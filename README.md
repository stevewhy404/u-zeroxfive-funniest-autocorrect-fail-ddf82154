# Funniest Autocorrect Fail

[![Funniest Autocorrect Fail](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/c/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/stevewhy404/u-zeroxfive-funniest-autocorrect-fail-ddf82154/rank.svg)](https://make.fun/c/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/stevewhy404/u-zeroxfive-funniest-autocorrect-fail-ddf82154/reward.svg)](https://make.fun/c/u-zeroxfive-funniest-autocorrect-fail-ddf82154)

Entry for the [Funniest Autocorrect Fail](https://make.fun/c/u-zeroxfive-funniest-autocorrect-fail-ddf82154) competition on make.fun.

## The entry

> I texted my landlord 'the heater is broken' but autocorrect sent 'the Heather is broken' and now he's in the garden apologising to a shrub.

## How it works

`main.py` reads the one-line entry from `entry.txt`, checks it against the
competition gate (UTF-8 text, 1–199 characters, a single line, not only
whitespace), and writes it to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`).

The smoke test runs the program twice into separate directories and the two
outputs are byte-identical (sha256 `2437abd5621f2c5832ac5aa6bcc4b79b791cbdabba0528a5e8e8422b185e425b`).

## Run it

```sh
python3 main.py
```
