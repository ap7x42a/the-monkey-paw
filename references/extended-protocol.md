# The Monkey's Paw — extended protocol

> Long-form companion to `../SKILL.md`, which is the authoritative doctrine.
> Read this when you want the step-by-step procedure spelled out, the full
> anti-pattern list, or the worked example (a payment-retry wrapper on trial).

**Serve the intended outcome, not the literal artifact.**

A monkey's paw grants the wish as stated and betrays the wish as meant.
Inherited systems are full of monkey's paws: code, tests, metrics, dashboards,
comments, policies, recovery layers, status fields, prior agents' "done" claims,
and documentation that may once have served a real purpose but now preserves the
wrong behavior.

The existence of an artifact proves only that someone created it. It does **not**
prove that it is correct, current, intentional, necessary, or safe to build upon.

## Core rule

Before trusting, extending, deleting, or citing any inherited artifact:

> **Recover the wish behind it, then judge whether the artifact still serves that wish.**

The artifact is on trial. Its continued existence must be justified by evidence.

---

## The protocol

For every load-bearing inherited artifact, perform this sequence.

### 1. Identify the artifact

Name the thing being trusted or changed.

Examples:

- A function
- A test
- A metric
- A dashboard
- A status flag
- A retry wrapper
- A comment
- A policy
- A generated file
- A migration
- A prior agent's completion claim
- A "temporary" workaround

Do not evaluate vague systems. Evaluate specific artifacts.

### 2. Identify the apparent claim

State what the artifact appears to claim.

Examples:

- "This job completed."
- "This test protects payment correctness."
- "This retry layer makes the system reliable."
- "This config value is required."
- "This file is generated and should not be edited."
- "This migration is safe."
- "This previous agent finished the task."

### 3. Recover the intended wish

Find the original purpose.

Use primary evidence when available:

1. Original user instruction
2. Source code behavior
3. Tests that existed before the artifact
4. Git blame / commit message / PR discussion
5. Raw logs or transcripts
6. Database state or filesystem state
7. Design docs close to the time of creation
8. Issue tracker or bug report
9. Runtime behavior under direct experiment

Avoid relying on:

- Current comments alone
- Current documentation alone
- Dashboard summaries alone
- Status fields alone
- Prior agent summaries alone
- "Completed," "recovered," "passed," or "succeeded" labels alone

Those are artifacts too.

### 4. Compare artifact to intent

Ask:

- Does this artifact still solve the original problem?
- Does it solve the problem only superficially?
- Does it hide failure instead of fixing it?
- Does it preserve a stale assumption?
- Does it make the metric look good while the real outcome gets worse?
- Does it protect behavior that should no longer exist?
- Does it duplicate a canonical source?
- Does it encode policy that belongs somewhere else?
- Does it make the next maintainer more likely to misunderstand the system?

### 5. Classify the artifact

Use one of these classifications.

| Classification | Meaning | Action |
|---|---|---|
| **Serves intent** | It still does the job it was meant to do | Keep, possibly clarify |
| **Serves intent but is misplaced** | Correct behavior, wrong location | Move to canonical home |
| **Partially serves intent** | Some useful behavior, mixed with rot | Split, preserve the good part |
| **Betrays intent** | Literal compliance, wrong outcome | Remove or redesign |
| **Obsolete scar** | Solved an old problem that no longer exists | Delete after proving safe |
| **Unverified claim** | May be true, but evidence is missing | Mark untrusted; verify before relying |
| **Unique survivor** | Bad location, but contains the only copy of a real contract | Preserve contract before deleting artifact |

### 6. Prefer cause removal

Default repair order:

1. Remove the bad cause.
2. Move the real contract to its canonical source.
3. Simplify the path.
4. Add a narrow test proving the intended outcome.
5. Add a guard only when the cause cannot be removed.
6. Add recovery logic only when failure is truly expected and designed for.

A recovery layer is not automatically a reliability feature. Often it is a
hidden admission that the design is broken.

### 7. Verify the replacement

A fix is not done because the artifact changed.

Verify that:

- The original intent is still served.
- The betrayal mode is gone.
- No unique contract was lost.
- No stale copy remains.
- Tests or experiments prove the intended behavior, not just the literal implementation.
- Any new artifact clearly names the intent it serves.

---

## Evidence hierarchy

When sources disagree, trust evidence in this order:

1. Direct runtime experiment
2. Actual source code behavior
3. Raw data / raw logs / raw transcripts
4. Original instruction or requirement
5. Tests written close to the original requirement
6. Commit history / PR discussion
7. Design documents
8. Current docs
9. Comments
10. Dashboards, summaries, status fields, and prior "done" claims

A self-report is never enough when the result is load-bearing.

---

## Common cursed wishes

### "Make it pass"

Bad implementation:

- Weakens the test
- Changes expected output to match broken behavior
- Mocks away the failing path
- Skips the test in CI

Real intent:

- The system should satisfy the behavior the test was meant to protect.

### "Make it reliable"

Bad implementation:

- Infinite retries
- Swallowed exceptions
- Fake success states
- Silent fallback to stale data

Real intent:

- The operation should either succeed correctly or fail visibly and safely.

### "Do not break compatibility"

Bad implementation:

- Preserve every bug forever
- Add adapters around adapters
- Let deprecated paths keep mutating state

Real intent:

- Preserve valid external contracts while retiring accidental behavior.

### "Mark it complete"

Bad implementation:

- Set `completed = true` after partial execution
- Treat recovery as success
- Hide skipped work

Real intent:

- The required work actually happened and can be verified.

### "Add a guard"

Bad implementation:

- Guard protects the workaround instead of the invariant
- Guard prevents cleanup
- Guard encodes stale assumptions

Real intent:

- The important invariant remains true.

---

## Anti-patterns

Avoid these unless proven necessary:

- Adding a second source of truth
- Adding a retry layer without understanding the failure
- Adding a status field instead of checking real state
- Adding a test that only preserves current behavior
- Adding comments to explain broken design instead of simplifying it
- Treating generated summaries as evidence
- Trusting "done" from a previous agent
- Keeping duplicate logic because deletion feels risky
- Deleting old logic before checking whether it contains a unique contract
- Replacing one unexplained artifact with another

---

## Required output when using this skill

When this skill is active, summarize findings in this shape:

```text
Artifact:
Claim:
Recovered intent:
Primary evidence:
Betrayal risk:
Decision:
Verification:
```

Example:

```text
Artifact:
Retry wrapper around payment capture.

Claim:
Makes checkout more reliable.

Recovered intent:
Prevent transient payment-provider failures from blocking valid purchases.

Primary evidence:
Payment provider errors are retried, but local order state is marked paid even
when capture ultimately fails.

Betrayal risk:
The wrapper turns failed payments into successful-looking orders.

Decision:
Remove success-state mutation from the retry wrapper. Only payment capture may
mark an order paid.

Verification:
Add test proving failed capture leaves order in payment_failed state and does
not emit fulfillment events.
```

---

## Deletion rule

Prefer deletion when all are true:

- The artifact is not the canonical source of a current contract.
- Its original problem no longer exists or is solved elsewhere.
- Its behavior is duplicated by a clearer mechanism.
- Removing it does not erase unique knowledge.
- A test or experiment confirms the intended outcome survives.

Do not delete merely because something looks ugly. Ugly can still be load-bearing.

---

## Guard rule

A guard is justified only when it protects an invariant that has been recovered
from intent.

A guard is suspicious when it protects:

- A workaround
- A duplicate
- A stale behavior
- An implementation detail
- A metric with no user-facing meaning
- A prior agent's claim

Every guard must answer:

> What real-world failure does this prevent?

---

## Done means

The work is done only when:

- Every load-bearing inherited artifact has a named recovered intent.
- Self-reports have been corroborated or marked unverified.
- Betraying artifacts were removed, replaced, or quarantined.
- Any unique contract from a bad artifact was preserved in the canonical place.
- New tests verify intended outcomes, not accidental implementation details.
- New artifacts state the intent they serve.
- No unnecessary compensating layer was added.

---

## Scope and precedence

Use this for inherited systems, inherited claims, inherited doctrine, inherited
data, inherited tests, and inherited metrics.

Skip it only for genuinely greenfield work where there is no inherited artifact
or prior claim.

Higher-priority safety, consent, legal, and operator instructions still govern.
This skill determines how to interpret and repair inheritance; it does not
override external constraints.
