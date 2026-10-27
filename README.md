# Multi-AI Handoff & Approval Card

A free, copy-paste template by [AKIO HIRAYAMA](https://akiohirayama.com/) for deciding when AI work is actually finished, and for passing work from one AI to another without relying on trust.

> An AI saying "done" is a claim. Work is complete only when something outside that AI has checked it.

## The card

Fill this in before any AI's work counts as finished, or moves to another AI.
**If a field is empty, the work is not done. It is only reported.**

```text
TASK: what was asked, in one sentence
CLAIMED RESULT: what the AI says it did
RISK TIER: auto / auto-then-verify / human approval (why?)
EVIDENCE: what was checked, by what (not the same AI run), result
CHANGED: pages, files or systems touched
ROLLBACK: how to undo it, and who can
OPEN ITEMS: anything unverified, ambiguous or skipped
APPROVED BY: a human, or the rule that allowed auto-approval
```

A machine-readable version is in [`card.json`](card.json).

## Risk tiers

| Tier | Examples | Default |
|---|---|---|
| Reversible, local | Draft a translation, generate a design option | Run automatically, log it |
| Visible, recoverable | Change a live page, update shared text | Run, then verify before it counts as done |
| Hard to undo / outward-facing | Publish, delete, spend, touch credentials, message anyone | Stop and ask a human, with a one-screen summary |

## Principles

1. **Approve less, but approve the right things.** Approving every step trains people to click "yes" without reading.
2. **Verification comes from outside the AI that did the work.** Use a separate run with a fresh context, a deterministic script, or the real state of the system.
3. **Handoffs need receipts, not trust.** The next AI should receive a structured record, not a summary it has to believe.

## What this does not solve

- Risk tiers drift as context changes.
- Verifiers can be wrong too. A passing check is evidence, not proof.
- A different AI is not automatically an independent one.

## More

- Notes: [Multi-AI Control Notes](https://akiohirayamanotes.wordpress.com/)
- AKIO HIRAYAMA is hiring an AI Engineer (USD 30,000/month) to build this kind of control layer: [role details](https://akiohirayamaaiengineer.wordpress.com/)

License: CC BY 4.0. Free to use and adapt with attribution to AKIO HIRAYAMA.
