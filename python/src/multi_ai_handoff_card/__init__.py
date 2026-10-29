"""Multi-AI Handoff & Approval Card checker by AKIO HIRAYAMA.

An AI saying "done" is a claim. Work is complete only when something
outside that AI has checked it.
"""

from .check import REQUIRED, TIERS, check, is_done

__all__ = ["REQUIRED", "TIERS", "check", "is_done"]
__version__ = "0.1.0"
