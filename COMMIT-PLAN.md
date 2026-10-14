# Commit plan: chapter edits

## Summary — the state after all commits

A run may edit its copy of a concept chapter as it edits any copy,
but only from a mistake it lived, never from a preference for other
wording; the edit reaches the concept only when the deliverer takes
it. A copy the run has finished with is fixed whenever the evidence
is there, never kept as a note for a later run, and its hand-off
line marks it untried. ADR-0051 records both, from run 3's RETRO.md,
D28, and reverses the exchange's "the concept is never edited". The
exchange manual, `ARCHITECTURE.md` and the shipped
`delivered-copies.md` say it alike, and the shipped rule is run 3's
plain text, its seven rules and their numbers kept.

## Commits

**1. `docs(agent): add commit plan for chapter edits`**
This plan, agreed.

**2. `docs(adr): 0051, a run fixes what it lived`**
The decision, opened Proposed: a chapter edited from a lived
mistake; a finished copy fixed when the evidence is there, marked
untried. The options rejected, the hold the agent proposed among
them.

**3. `docs: a run may edit a chapter it found wrong`**
The exchange manual's §5.6, `ARCHITECTURE.md` §1.1 and the shipped
rule's rule 1, together: one change, and the paragraph that maps it.

**4. `docs: a finished copy is fixed, marked untried`**
The manual's §5.1 and §5.2, and the shipped rule's rules 4 and 7:
fixed whenever the evidence is there; the hand-off line's mark.

**5. `docs: the delivered-copies rule, plain`**
The shipped rule rewritten in run 3's plain text, meaning unchanged:
the pin and the read-through, rule 2's three conditions and rule 7's
three reasons as lists, the take's order as seven numbered steps.
After it, the shipped rule equals run 3's byte for byte.

**6. `docs: records carry the chapter edits`**
ADR-0051 Accepted.

**7. `docs(agent): close commit plan for chapter edits`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **Meaning before wording.** Commits 3 and 4 put run 3's two
  changes into our text as it stands; commit 5 rewrites it plain
  after, so each change is read on its own and the rewrite is read
  as a rewrite. Run 3 applied them in the same order.
- **One ADR for both rules.** Both come from RETRO D28 and answer one
  question: what a run does with a lesson about a copy it holds.
- **No TODO line.** Nothing is held; the concept's version question
  is ADR-0003's and is asked when a run's chapter edit is first
  taken, not now.
- **No decisions-log entry, no copy of ours.** We hold no
  `delivered-copies.md` of our own.
- **The reading's marks stay outside**, as before.
