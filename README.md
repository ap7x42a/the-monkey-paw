# The Monkey's Paw

The Monkey's Paw is an agent skill for inherited systems, prior-agent artifacts,
metrics, tests, comments, docs, and status claims that might satisfy the literal
request while betraying the intended outcome.

The core stance:

```text
The artifact is on trial. Its existence proves only that someone made it.
```

Before trusting, extending, deleting, or citing an inherited artifact, recover
the intent behind it and measure the artifact against that intent.

## Use It When

- You inherit a code path, test, metric, doc, guard, or prior result you did not
  author.
- A status field, summary, dashboard, or prior agent says something is complete.
- A workaround may have become accidental architecture.
- A guard might be protecting the wrong behavior.
- You are about to delete something that might be the only surviving copy of a
  real contract.
- The literal instruction and the evident purpose could diverge.

## What The Package Includes

- `SKILL.md` - the inheritance-reading doctrine and verdict categories.
- `references/extended-protocol.md` - a longer step-by-step protocol with a
  worked inherited-artifact review.
- `scripts/self_test.py` - regression checks for required sections, verdict
  categories, evidence hierarchy, and proof-table shape.
- `agents/openai.yaml` - skill metadata for runtimes that display skill cards.
- `SHA256SUMS.txt` - drift manifest.

## Artifact Review Shape

Use this proof table for load-bearing inherited artifacts:

```text
Artifact:         the thing on trial
Claim:            what it appears to guarantee
Recovered intent: the original wish or requirement behind it
Evidence:         primary sources actually read
Betrayal risk:    how it could satisfy the letter but not the spirit
Decision:         keep / relocate / split / remove / verify
Verification:     failable check proving the intent survives
```

## Verdicts

| Verdict | Meaning | Move |
|---|---|---|
| Serves the intent | Still does its job | Keep; clarify if needed |
| Right behavior, wrong home | Correct but misplaced | Move to the canonical source |
| Partially serves | Useful behavior tangled with rot | Split and preserve the good part |
| Betrays the intent | Literal compliance, wrong outcome | Remove or redesign |
| Obsolete scar | Solves a problem that no longer exists | Delete once proven safe |
| Unverified claim | May be true, no evidence | Mark untrusted; verify before relying |
| Unique survivor | Bad artifact, only copy of a real contract | Relocate the contract, then delete |

## Install As An Agent Skill

```bash
git clone https://github.com/ap7x42a/the-monkey-paw.git
cp -a the-monkey-paw ~/.codex/skills/the-monkey-paw
```

For project-local skill surfaces, copy the directory into the location your
runtime uses, such as `.agents/skills/the-monkey-paw`.

## Verify The Package

```bash
python3 scripts/self_test.py
sha256sum -c SHA256SUMS.txt
```

## Limits

This skill is a review stance, not a license to thrash inherited systems. It
requires proof before cutting, proof before keeping, and preservation of any
unique contract before deleting the artifact that carried it.
