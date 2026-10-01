# Commit plan: working a reading is a rule

## Summary — the state after all commits

How this repo works a reading is a standing rule,
`.claude/rules/working-a-reading.md`, loading on the same reading
files as the reading's shape. It holds the steps from count to
delivery and the lessons that have held across three readings of
run 3 (2026-09-23, 2026-09-30, 2026-10-01). The shape,
`.claude/rules/exchange-reading.md`, goes back to form only: its
process lines move into the new rule, since a shape is form, never
content (`docs/conventions/shapes/` §1).

`temp/working-a-reading.md` is gone, its header's own condition met
— it lands once it has run twice. What it held that is not a rule
yet goes where it can wait: the questions it had not thought about
to TODO, its history to git. The agent-arrangement manual names
the third rule of the deliverer's own.

## Commits

**1. `docs(agent): add commit plan for working a reading`**
This plan.

**2. `chore(agent): working a reading is a rule`**
The new rule, from the draft's *How it goes* and the lessons that
held; the shape loses the four process lines it carried; a
`.claude/decisions.md` entry with the options rejected — folding
into the shape, a skill, leaving the draft. All agent-side, so one
commit.

**3. `docs(conventions): the deliverer holds three rules`**
`docs/conventions/agent-arrangement/` §*The deliverer's seat*
names `working-a-reading.md` beside the two it lists.

**4. `docs: the working draft lands`**
`temp/working-a-reading.md` deleted. TODO's item to place it
closes; its open questions take a line each in Later. The devlog
says so at the session's end, not here.

**5. `docs(agent): close commit plan for working a reading`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The rule's `foundation`.** The exchange says nothing about how
  a reading is worked (§6.3), so the rule derives from no manual.
  Proposed: `practice, under the exchange convention` — what it
  stands on is three readings, inside the exchange's frame
  (`docs/conventions/conventions/` §2: the value carries the
  relation where it is not derivation).
- **What becomes rule, and what does not.** The nine steps, and
  the lessons lived more than once or fixed by a lived failure: the
  pass after every close, decisions first, a decision as a proposed
  ADR, the count and why it undercounts, a mid-list note says what
  is open. What another manual or skill already owns is pointed at,
  not restated: overtaken readings (exchange §6.4), the run moving
  before the note (`exchange-deliver` step 0).
- **Three open questions to TODO, one dropped.** When to read, more
  than one run, and the reviewer's seat take Later lines. "Two
  readings at once" happened once, during a review now closed, and
  is not carried.
- **No ADR.** The arrangement changed, so `.claude/decisions.md`
  carries the why and the rejected options, as the entry file's
  records table puts it.
