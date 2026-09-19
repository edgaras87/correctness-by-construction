# 0032. The chain is a section, and it is drawn

Date: 2026-09-19
Status: Accepted

## Context

Ten conventions, ten manuals, and nothing states how they relate. A
reader learns what `commit-plan` is from its manual and what
`decide-first` is from its own, and nowhere learns that one hands
to the other, that neither requires the other, or that the sequence
*inside* a plan comes from somewhere else entirely.

Two questions were settled before the shape was compared, by
`decide-first`'s first live run (`temp/deciding-the-map.md`):

- **It does not ship.** Measured against `artifact-kinds`, the map
  is a **guide** — its force is *advise*, not *bind*, and every
  rule it points at binds on its own. Shipping a guide into
  `delivery/container/.claude/skills/` would put a second kind in a
  directory ADR-0031 had just made single-kind.
- **It lands as a section of `docs/conventions/README.md`**, not
  its own file. Recorded with its cost: the map names the domain
  skills, which are not conventions, so the index now holds a
  section about more than it indexes and grows by roughly half
  again. Decided against that argument.

## What a reader must get

Written before any candidate existed.

1. **The order things happen in**, from an idea to committed work.
2. **That each fires on its own.** Nothing requires the one before
   it: a typo fix calls `commit-messages` with no plan and no
   deciding.
3. **Which specialises which** — `visual-comparison` is
   `option-comparison` for things you look at.
4. **Where the sequence inside a plan comes from**: the domain
   skills, which are not conventions.
5. **No rule is restated.** Every rule lives in a manual or a
   skill. A shape that tempts restatement fails.
6. **It costs less to keep true than to read.**

## The candidates

**Round one — is it a picture at all?** Four built: a chained
Mermaid flowchart (A), a table (B), a numbered list (C), prose (D).

- **B fails 4 on what it cannot hold.** The domain skills are not a
  trigger and have no "fires when"; a row for them would be a lie
  in a column. A finding about tables, not about this table.
- **C and D both carry all six and fail differently on 1.** A list
  is scannable and shows no flow; prose says 2 and 4 in words a
  list needs a footnote for.
- **A carries 1, 3 and 4 and fails 2.** Its arrows are the order,
  and the order is the lie: drawn plainly it says a typo fix begins
  at `decide-first`.

**Round two — if it is a picture, which dialect?** Three more, after
the reviewer chose a picture: `classDiagram` (E), `mindmap` (F), and
a flowchart grouped by moment rather than chained (G).

- **E draws requirement 3 natively** — the inheritance arrow is the
  best statement of specialisation available here — and loses 1 and
  4, with a `..>` that means *depends on*, which `decide-first`
  does not. Third instance of this skill's first §4 entry: the
  dialect built for the job can be the one that fails.
- **F solves 2 structurally**, having no arrows at all, and breaks
  3, because nesting reads as *contains*. A shape with no way to be
  wrong about direction is also a shape with no way to be right
  about relation. It is also the most expensive to keep true —
  Mermaid's mindmap is whitespace-sensitive, so a reorder is a
  silent re-parse, which requirement 6 caught and no reading would.
- **G holds 1 and 2 at once**, alone among the seven. Two subgraphs
  with nothing crossing between them say *these happen around here*
  without saying *you go this way*.

## Decision

1. **The section is drawn as A, the chained flowchart**, at the
   reviewer's call. The reading recommended G and is preserved
   above rather than rewritten to agree: A was the reviewer's
   choice before round two and remained it after, which is a
   decision the comparison informs and does not make.

2. **Requirement 2 is carried by one sentence under the picture**,
   and by nothing else: *each fires at its own moment; the arrows
   say what hands to what, not what you must pass through*. This is
   ADR-0028 decision 1's shape — the picture is additive and the
   prose carries what a picture cannot — with the difference that
   here the prose is carrying a requirement the picture actively
   contradicts, rather than one it merely omits. **Stated plainly
   because it is the weak point:** a reader who takes the picture
   and not the line gets the wrong answer, and the mitigation is a
   sentence's worth of attention.

3. **The grouping finding is kept even though its candidate lost.**
   That a flowchart can hold order and independence together when
   grouped by moment, and cannot when chained, is a fact about the
   dialect that outlives this decision. It is the first time this
   method found that the fix was a different *use* of a dialect
   rather than a different dialect.

4. **`visual-comparison`'s merge-back trigger did not fire.**
   ADR-0030 decision 10 asks whether a comparison whose winner is
   *not* a picture ever happens. Round one's reading said no
   picture should win; the decision chose one. The trigger turns on
   the outcome, not the reading, so it stays open — recorded
   because the draft claimed it had fired and that claim was wrong.

## Consequences

Good: the relations between ten conventions are stated in one
place, and the comparison behind the shape is on record with seven
candidates rather than an assertion. §4 of `visual-comparison`
gains three entries, which is the answer to ADR-0028's standing
objection — a list that stops growing means the method was
distilled too early.

Bad: the chosen shape fails the requirement the section most exists
to state, and the mitigation is one line of prose. If a reader ever
acts on the picture alone — starts a typo fix at `decide-first`, or
believes a comparison must follow a `decide-first` — that is this
decision's cost arriving, and G is what it should become.

Also: `docs/conventions/README.md` now holds a section about things
it does not index. Foreseen and accepted, not discovered.
