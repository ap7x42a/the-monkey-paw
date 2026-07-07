---
name: the-monkey-paw
description: >-
  Use when working an inherited system, artifact, claim, metric, test, or prior
  agent result you did not author and cannot fully trust -- especially long-lived
  AI-built systems where intent and implementation have drifted. Read every
  load-bearing artifact as a possible cursed wish: something that satisfies the
  literal request while betraying the intended outcome. Also use before
  trusting, extending, deleting, or citing any inherited behavior, and when
  reviewing a system's own account of how it did. The complement to building
  (fable-method) and proving a claim (evaluate-by-experiment): how to stand
  toward what you inherited.
metadata:
  self_test: "python3 scripts/self_test.py"
---

# The Monkey's Paw

**serve the spirit, never the letter**

A monkey's paw grants the wish you said and betrays the wish you meant. Every
artifact you inherit -- a function, a directive, a metric, a test, a comment, a
recovery layer, a prior agent's `completed` -- can be exactly that: a real intent,
granted in letter and twisted in spirit by whoever implemented it last. You are
not here to work *within* the system; you are here to recover what each thing was
*meant* to do and judge it against that.

> The existence of a thing is not evidence of its rightness. It proves only that
> someone made it -- not that it is correct, current, intentional, or safe to
> build on.

## The one move

Before you trust an artifact, extend it, delete it, or cite it as ground truth:
**find the wish behind it.** Who made it, when, against what problem -- git blame,
the commit message, the original instruction, the surrounding history. Then
measure the artifact against that wish. The artifact is on trial; its continued
existence must be earned by evidence.

## Reading what you inherited

1. **Distrust the self-report.** Metrics, dashboards, status fields, "completed"
   -- all artifacts, and artifacts lie. Reconstruct truth from primary sources:
   source actually read, git history, raw transcripts, the filesystem. A
   "recovered" or "succeeded" label is a surface artifact -- ask what it cost and
   what it betrays, because a clear design would not have needed to recover.
2. **Recover the intent.** A directive that looks authoritative may be a scar
   from a past over-correction. Trace its provenance, name the problem it was
   born to solve, ask whether it still solves that or now causes its opposite.
3. **Burden of proof is on the artifact.** Your change need not justify itself
   against the original; the original must justify its continued existence -- but
   do not "fix" deliberate-looking design unproven either. Prove the mechanism
   before you cut or keep.
4. **Reach for the eraser -- but prove it lossless first.** Bandaids en masse are
   toxic; recovery being necessary is itself the bug. Before deleting a
   duplicate, confirm its intent survives at the canonical source and relocate
   any one-of-a-kind survivor there. An eraser that drops a unique contract is a
   monkey's paw in a janitor's uniform.
5. **A guard is an artifact too.** A test, a regression check, or a comment that
   "protects" an artifact is itself a possible cursed wish -- its existence is
   not proof the thing it guards deserves to exist. An agent can inline a cursed
   copy and bolt a guard onto it in the same breath. A passing guard can be
   locking in the rot; interrogate its provenance like anything else.

## Classify, then act

Put the artifact in exactly one bucket -- the bucket names the move.

| Verdict | Meaning | Move |
|---|---|---|
| **Serves the intent** | still does its job | keep; clarify if murky |
| **Right behavior, wrong home** | correct, but misplaced | move to the canonical source |
| **Partially serves** | good behavior tangled with rot | split; preserve the good part |
| **Betrays the intent** | literal compliance, wrong outcome | remove or redesign |
| **Obsolete scar** | solved a problem that no longer exists | delete once proven safe |
| **Unverified claim** | may be true, no evidence | mark untrusted; verify before relying |
| **Unique survivor** | bad artifact, but the only copy of a real contract | relocate the contract, *then* delete |

## Evidence hierarchy

When sources disagree, trust in this order -- and never let a lower tier overrule
a higher one. A self-report is never enough when the result is load-bearing.

1. Direct runtime experiment
2. Actual source behavior
3. Raw logs / transcripts / filesystem / database state
4. The original instruction or requirement
5. Tests written close to that requirement
6. Commit history / PR discussion
7. Design docs
8. Current docs
9. Comments
10. Dashboards, status fields, summaries, prior "done" claims

## The cursed wishes you will meet

The grant is always technically faithful to the words. The named ones:

- **"Mark it complete."** Cursed: set `completed` after partial work, treat
  *recovery* as success, hide skipped work. Meant: the required work actually
  happened and can be verified.
- **"Make it pass."** Cursed: weaken the gate, match the broken output, mock the
  failing path, skip the check. Meant: the system satisfies the behavior the gate
  exists to protect.
- **"Make it reliable."** Cursed: infinite retries, swallowed errors, fake
  success, silent fallback to stale data. Meant: succeed correctly, or fail
  visibly and safely.
- **"Add a guard."** Cursed: the guard protects a workaround, a duplicate, or a
  stale assumption. Meant: a real invariant stays true -- and every guard must
  answer *what real failure does this prevent?*
- **"Don't break compatibility."** Cursed: preserve every bug forever, wrap
  adapters around adapters, let deprecated paths keep mutating state. Meant:
  preserve valid external contracts while retiring accidental behavior.

For the long-form step-by-step protocol with a worked example (payment-retry
wrapper on trial), read `references/extended-protocol.md`.

## Building so you are not the next paw

- Implement the **intent** behind an instruction, not its literal shape.
- Prefer removing a cause to adding a guard; add recovery only when failure is
  genuinely expected and designed for.
- Name the wish your own work serves, so the next reader can measure your
  artifact against it.

## Name it when you act

For any load-bearing call, make the reasoning legible -- the proof table for
inheritance:

```
Artifact:         the thing on trial
Claim:            what it appears to guarantee
Recovered intent: the wish behind it, from primary evidence
Evidence:         the primary sources you actually read
Betrayal risk:    how it serves the letter but not the spirit
Decision:         keep / relocate / split / remove / verify
Verification:     the failable check proving the intent survives
```

## When to reach for this

Any time you touch code, doctrine, data, or a claim you did not author this
session; any time a metric or a prior result is load-bearing for a decision; any
time an instruction's literal reading and its evident purpose could diverge; any
time you are reviewing a system's own account of how it did. Skip it only for
genuinely greenfield work with no inheritance.

## Done means

- Every load-bearing inherited artifact was measured against its recovered
  intent, not taken on faith.
- Self-reports were corroborated from primary sources or left marked unverified.
- Betraying artifacts were removed, relocated, or quarantined -- and any unique
  contract from a bad artifact was preserved in its canonical place first.
- New tests verify intended outcomes, not accidental implementation details.
- Your additions name the intent they serve and add the least machinery that
  serves it.

## Scope and precedence

This governs how to read and judge an inherited system; higher-priority safety,
consent, and operator instructions win. It harmonizes with its siblings: **build
forward (fable-method), prove the point (evaluate-by-experiment), read the
inheritance backward (the monkey's paw).**
