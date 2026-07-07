#!/usr/bin/env python3
"""Structural self-test for the-monkey-paw skill.

Fails (exit 1) if the doctrine file drifts from its load-bearing structure:
frontmatter shape, name/directory invariant, required sections, the ordered
evidence hierarchy, the classification verdicts, and resolvable local
references. Stdlib only; read-only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
FAILURES: list[str] = []


def check(ok: bool, label: str) -> None:
    print(("  ok:   " if ok else "  FAIL: ") + label)
    if not ok:
        FAILURES.append(label)


def main() -> int:
    skill_md = SKILL_DIR / "SKILL.md"
    check(skill_md.is_file(), "SKILL.md exists")
    if not skill_md.is_file():
        return finish()
    text = skill_md.read_text(encoding="utf-8")

    # Frontmatter shape and name/directory invariant.
    fm = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    check(fm is not None, "frontmatter block parses")
    if fm:
        check(
            re.search(r"^name:\s*the-monkey-paw\s*$", fm.group(1), re.M) is not None,
            "frontmatter name matches directory (the-monkey-paw)",
        )
        check("description:" in fm.group(1), "frontmatter has a description")
        check(
            "Recover the original intent" not in fm.group(1),
            "description carries triggers, not a workflow summary",
        )

    # Exactly one frontmatter block in the package (no shadow SKILL variants).
    shadow = [
        p
        for p in SKILL_DIR.rglob("*.md")
        if p != skill_md and p.read_text(encoding="utf-8").startswith("---\n")
    ]
    check(not shadow, f"no second frontmattered markdown in package {shadow or ''}")

    # Required sections.
    for section in (
        "## The one move",
        "## Reading what you inherited",
        "## Classify, then act",
        "## Evidence hierarchy",
        "## The cursed wishes you will meet",
        "## Name it when you act",
        "## Done means",
    ):
        check(section in text, f"section present: {section}")

    # Evidence hierarchy: all ten tiers present, in order.
    tiers = [
        "Direct runtime experiment",
        "Actual source behavior",
        "Raw logs",
        "original instruction",
        "Tests written close",
        "Commit history",
        "Design docs",
        "Current docs",
        "Comments",
        "Dashboards, status fields",
    ]
    section = re.search(r"## Evidence hierarchy\n(.*?)\n## ", text, re.DOTALL)
    hier = section.group(1) if section else ""
    pos = -1
    ordered = bool(hier)
    for tier in tiers:
        found = hier.find(tier)
        if found < 0 or found < pos:
            ordered = False
            break
        pos = found
    check(ordered, "evidence hierarchy has all 10 tiers in canonical order")

    # Classification verdicts survive.
    for verdict in (
        "Serves the intent",
        "Right behavior, wrong home",
        "Partially serves",
        "Betrays the intent",
        "Obsolete scar",
        "Unverified claim",
        "Unique survivor",
    ):
        check(verdict in text, f"classification verdict present: {verdict}")

    # Trial-record fields survive.
    for field in (
        "Artifact:",
        "Claim:",
        "Recovered intent:",
        "Evidence:",
        "Betrayal risk:",
        "Decision:",
        "Verification:",
    ):
        check(field in text, f"trial-record field present: {field}")

    # Local references named in SKILL.md resolve inside the package.
    for rel in re.findall(r"`(references/[^`]+|assets/[^`]+|scripts/[^`]+)`", text):
        check((SKILL_DIR / rel).is_file(), f"referenced path resolves: {rel}")

    return finish()


def finish() -> int:
    if FAILURES:
        print(f"SELF-TEST FAILED ({len(FAILURES)} failures)")
        return 1
    print("SELF-TEST PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
