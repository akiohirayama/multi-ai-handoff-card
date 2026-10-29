from multi_ai_handoff_card import check, is_done

GOOD = {"task": "Translate the contact page into Thai", "claimed_result": "Thai contact page drafted",
        "risk_tier": "auto-then-verify", "risk_reason": "visible but easy to revert",
        "evidence": [{"check": "page renders with lang=th", "checked_by": "script", "result": "pass"}],
        "changed": ["/th/contact/ draft"], "rollback": {"how": "restore previous revision", "who": "site owner"},
        "open_items": [], "approved_by": "rule: drafts may run automatically"}
BAD = {"task": "Publish the article", "claimed_result": "Published", "risk_tier": "human-approval",
       "risk_reason": "public", "evidence": [{"check": "links work", "checked_by": "", "result": "unclear"}],
       "changed": ["note.com"], "rollback": {"how": "unpublish"}, "open_items": ["image credits"], "approved_by": ""}


def test_good_card_is_done():
    assert check(GOOD) == [] and is_done(GOOD)


def test_bad_card_lists_every_problem():
    assert check(BAD) == [
        "empty field: approved_by",
        "evidence not passing: links work",
        "evidence without a checker: links work",
        "rollback needs both how and who",
        "1 open item(s) still listed",
    ]


def test_non_object_and_empty_card():
    assert check([]) == ["card must be a JSON object"]
    assert "no evidence: the work is reported, not done" in check({})
