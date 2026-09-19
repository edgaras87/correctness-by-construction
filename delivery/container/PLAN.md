# Plan: <project name>

<!-- The stub ships the pure shape: the steps below are placeholders
     showing the form — a goal, a gate of verifiable facts, the records
     expected. At birth the install manual replaces the region between
     the STEPS markers with a playbook's full sequence — the handbook's
     or a concept's; the playbook itself stays where it came from. Born
     without one, fill the placeholders in place. Either way the two
     STEPS markers stay: they are what makes the swap re-runnable. -->

<!-- Steps from: <playbook> v<N> at <handbook or concept commit>,
     copied at birth. Filled in place at birth; this comment stays —
     the retrospective folds lessons back to what it names. -->

## Legend

`[ ]` planned  ·  `[~]` in progress  ·  `[x]` done (+date)  ·  `[!]` blocked (+what unblocks)  ·  `[-]` skipped (+why)

**Gate** = exit criteria: verifiable facts, not intentions. A step is done only when every gate item is true.
Detail only the next 1–2 steps finely; keep later steps coarse (rolling wave).

---

<!-- STEPS-BEGIN — steps between the markers; the markers stay -->

## Step 0: <first step, e.g. "Bootstrap">

Goal: <one sentence>.
Gate:
- [ ] <verifiable fact, not an intention>
- [ ] <verifiable fact>
Records: <records this step is expected to produce: ADRs, README
sections, …>.
Notes:

## Step: <next step>

Goal: <one sentence>.
Gate:
- [ ] <criterion>
- [ ] <criterion>
Records: <ADRs expected here, if any>.
Notes:

## Step: <coarse placeholder — detail when a project reaches it>

Goal: <one line>.
Gate: TBD — depends on <decision that unlocks it>.

## Step N: <last step, e.g. "Release">

Gate:
- [ ] <the facts that make this project done or shipped>
Notes:

<!-- STEPS-END -->

---

## Discovered along the way

<!-- Non-blocking findings. Triage each into TODO.md: assign to a step,
     park in Later, or drop. Then delete the line here. -->
- <YYYY-MM-DD> <finding> → <where it went>

## Decision index

- ADR-0001: Record architecture decisions (birth)

---

## Retrospective  (fill at project end)

Ran: <start> → <end>

1. Estimate vs reality — which steps took much longer/shorter, why?
2. Wrong order — what needed to happen earlier?
3. Dead ends — approaches tried and abandoned (→ playbook warnings).
4. Missing steps — work that had no home in the plan.
5. Useless gates — ceremony that caught nothing.
6. The entry file — read CLAUDE.md top to bottom; every line still
   passes its three tests, or leaves (agent-arrangement §2).

Then fold lessons into the playbook the steps came from — the
"Steps from" line at the top names it — in the repo that owns it,
and bump its version there.
