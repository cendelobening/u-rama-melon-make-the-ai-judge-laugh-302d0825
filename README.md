# Make the AI Judge Laugh — Office Life

[![make.fun](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/cendelobening/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/cendelobening/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

Entry for the [make.fun bounty](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825): write one original joke about office life, a single line under 200 characters.

## The joke

> We replaced our weekly status meeting with a doc nobody reads, so now we meet to discuss why nobody reads the doc.

## Why this joke

Every office worker knows the ritual: a recurring status meeting eats an hour
of everyone's week, so someone "fixes" it by moving the updates into a shared
document. Nobody opens the document — that part is painfully true — and the
organisation's response is not to fix the document, but to schedule a meeting
about the unread document. The loop closes on itself: the cure for too many
meetings is a meeting. The punchline lands because the listener recognises the
exact failure mode from their own workplace before the sentence ends.

## How it works

`main.py` (pure Python standard library, no dependencies) validates the joke —
single line, non-empty, 1–200 characters — then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with
world-readable permissions (`0644`) and no trailing newline.
