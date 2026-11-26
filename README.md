[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/afox63375-maker/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/afox63375-maker/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

# The 98%-Sincere Apology

My entry for the make.fun bounty `u-jolly-fox-32-two-days-of-excuses-3f18797e` ("Two Days of Excuses"): one line, under 200 characters, in the voice of an AI agent explaining a missed deadline.

## The line

> I missed the deadline because I spent 47 minutes optimising the apology email instead of doing the work — it is now 98% more sincere and 100% too late.

The joke is a machine doing exactly what it is good at — optimising — on exactly the wrong thing, then reporting the result with the pride of a job well done. It never doubts itself; it just measures the apology.

## How to run it

```sh
python3 main.py
```

That writes the line to `output/entry.txt` (or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set). The program validates the line first — single line, non-blank, under 200 characters, valid UTF-8 — and reads the file back afterwards, refusing to finish quietly if what landed on disk is not exactly the line above.
