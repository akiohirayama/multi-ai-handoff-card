# multi-ai-handoff-card

Check whether AI work is **done** or only **reported**, using the Multi-AI Handoff & Approval Card by [AKIO HIRAYAMA](https://akiohirayama.com/).

> An AI saying "done" is a claim. Work is complete only when something outside that AI has checked it.

## Install

```
pip install multi-ai-handoff-card
```

## Use

```
handoff-card card.json
```

It prints the problems it finds and `DONE` or `NOT DONE`. The exit code is 0 only when the work is done, so it can gate a pipeline step or a handoff to the next agent.

```python
from multi_ai_handoff_card import check, is_done

problems = check(card)   # [] when the work is done
```

## The card

```json
{
  "task": "what was asked, in one sentence",
  "claimed_result": "what the AI says it did",
  "risk_tier": "auto | auto-then-verify | human-approval",
  "risk_reason": "why this tier",
  "evidence": [{ "check": "what was checked", "checked_by": "script / fresh-context run / human", "result": "pass | fail | unclear" }],
  "changed": ["pages, files or systems touched"],
  "rollback": { "how": "how to undo it", "who": "who can undo it" },
  "open_items": ["anything unverified, ambiguous or skipped"],
  "approved_by": "a human, or the rule that allowed auto-approval"
}
```

## Links

- Template and field guide: https://github.com/akiohirayama/multi-ai-handoff-card , https://akiohirayama.github.io/
- Try it in the browser: https://huggingface.co/spaces/AKIOHIRAYAMA/handoff-card-checker
- Papers (DOI): https://doi.org/10.5281/zenodo.23771747 , https://doi.org/10.5281/zenodo.23771780

License: CC BY 4.0. Free to use and adapt with attribution to AKIO HIRAYAMA.
