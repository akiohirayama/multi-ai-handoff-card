"""Rules for deciding whether a handoff card shows finished work."""

REQUIRED = [
    "task", "claimed_result", "risk_tier", "risk_reason", "evidence",
    "changed", "rollback", "open_items", "approved_by",
]
TIERS = ("auto", "auto-then-verify", "human-approval")


def check(card):
    """Return a list of problems. An empty list means the work is done."""
    if not isinstance(card, dict):
        return ["card must be a JSON object"]
    problems = []
    for key in REQUIRED:
        if key not in card:
            problems.append(f"missing field: {key}")
    for key in ("task", "claimed_result", "risk_reason", "approved_by"):
        if key in card and not str(card[key]).strip():
            problems.append(f"empty field: {key}")
    if card.get("risk_tier") not in TIERS:
        problems.append("risk_tier must be auto, auto-then-verify or human-approval")
    evidence = card.get("evidence") or []
    if not isinstance(evidence, list) or not evidence:
        problems.append("no evidence: the work is reported, not done")
        evidence = []
    for item in evidence:
        item = item if isinstance(item, dict) else {}
        name = item.get("check", "?")
        if item.get("result") != "pass":
            problems.append(f"evidence not passing: {name}")
        if not str(item.get("checked_by", "")).strip():
            problems.append(f"evidence without a checker: {name}")
    rollback = card.get("rollback") or {}
    if not isinstance(rollback, dict) or not rollback.get("how") or not rollback.get("who"):
        problems.append("rollback needs both how and who")
    open_items = card.get("open_items")
    if isinstance(open_items, list) and open_items:
        problems.append(f"{len(open_items)} open item(s) still listed")
    return problems


def is_done(card):
    """True only when the card has no problems."""
    return not check(card)
