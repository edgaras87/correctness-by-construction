# Commit plan: round 2's layer 2, the records map

## Summary — the state after all commits

The last of layer 2's three commit plans. It builds the records map
the refinement step's goal names, and applies the refinement's
DECISION-12 (a): project-recording §1 is the home of what each
record is and why, for both seats (`temp/refinement-2026-10-18.md`,
*Round 2*). It fixes FINDING-145, all but its codemap part.

- **Project-recording §1 is the records map:** one row per record,
  each marked held by both seats, ours only or the run's only, each
  difference between the seats said once. It includes `RETRO.md`,
  `COMMIT-PLAN.md`, `docs/system/`, and the records another
  convention owns, such as `.claude/decisions.md`. Its form was
  chosen by `visual-comparison`, which keeps a non-picture among the
  candidates; ADR-0067 records the requirements, the candidates and
  why each lost.
- **Each seat's records table derives from the map.** Its *When* is
  its own (§13). Its *What's in it* is a summary: ours names the
  map; the run's cannot, since a run never opens our manuals, and is
  checked against the map row by row instead.
- **What else told it points at the map:** README's "What it
  answers" column, and `temp/README.md`'s "Not records" line. The
  README and `CLAUDE.md` no longer share an opening phrase (§7.1:
  two audiences, no shared text).
- **Not here:** the codemap's descriptions in `ARCHITECTURE.md`.
  TODO's "Decide what kind of text our ARCHITECTURE is" is due
  before layer 4's fixes, which rest on it, FINDING-145's codemap
  part among them.
- PLAN's two gate items for the map are ticked: one view of which
  record answers what, and its form chosen by `visual-comparison`
  with that skill's gates held.

## Commits

**0. `docs(agent): add commit plan for the records map`**
Opens the set.

**1. Provisional: TODO's "Decide what our ADR form keeps".**
Its trigger is the next ADR this repo writes, and commit 4 writes
ADR-0067. The item is worked in talk before it: what the form keeps
of the one-page rule and the status words. Its commits, if any, are
settled then: a change to `docs/adr/README.md` and §3.4, and the
item's removal.

**2. `docs(temp): the records map's requirements`**
`visual-comparison` stages 1 and 2: a `temp/` draft of what the
reader of the map must get, each requirement able to fail, written
before any candidate. Taken from the PLAN gate and DECISION-12. The
reviewer confirms them before any candidate is built.

**3. `docs(temp): the records map's candidates`**
Stages 3 to 5: at least a table, a numbered list, a Mermaid
picture, Unicode box drawing, and today's §1 picture. Each built in
full and judged per requirement. The reviewer renders them where
they will be read, GitHub and the IDE; a verdict not yet rendered
is marked a prediction. This repo has no Mermaid renderer.

**4. `docs: ADR-0067 the records map's form`**
Stage 6: the reviewer's choice, the requirements, the candidates
and why each lost. Opened Proposed. The draft is deleted in this
commit; git keeps it.

**5. `docs: project-recording §1 is the records map`**
§1 is rewritten around the chosen form, under a heading that names
records, not "the model". The differences between the seats are
said once, in the map; the seats sections keep what each seat does
and point at the map for which records differ. §13 says a table's
*What's in it* summarizes the map. Provisional: how much of today's
§1 stays, the repository layout and the reading order, is settled
at this boundary.

**6. `chore(agent): our records table names the map`**
`CLAUDE.md`'s table: *What's in it* checked against the map, and a
line naming it. Agent file, next after 5.

**7. `fix(delivery): the run's table follows the map`**
The container's entry file: each row checked against the map's
run-seat rows. No pointer to the map, which a run cannot open; its
reference to project-recording §13 stays until FINDING-204's item
settles the shipped form.

**8. `docs: README's records column points at the map`**
The "What it answers" column becomes a pointer, or the map's words
by its fact reference, settled at the boundary. The opening phrase
it shares with `CLAUDE.md` goes.

**9. `docs: temp's README points at the map`**
"Not records" names the map for what the records are.

**10. `docs: round 2's layer 2 is worked`**
The records commit. ADR-0067 Accepted. PLAN's two map items ticked.
The refinement's file: FINDING-145's ending, fixed but its codemap
part, which waits for layer 4.

**11. `docs(agent): close commit plan for the records map`**
Deletes this file; the body says what diverged.

## Decisions for you to object to

- **The ADR-form item is worked first.** Its trigger fires inside
  this plan, at ADR-0067. Left standing, it would fire unseen, as
  three triggers did in round 2's read.
- **The comparison's outcome is an ADR.** `visual-comparison`
  records it where the records table puts a decision with options
  rejected, as ADR-0032 did for the index's chain.
- **The run's table derives without naming the map.** A run cannot
  open our manuals; naming one is FINDING-204's case, waiting in
  "Decide how a fact reference is written".
- **The codemap waits for layer 4,** as TODO's ARCHITECTURE item
  asks.
- **§1 keeps its number.** PLAN's goal and its gate item point at
  project-recording §1; only §1's content and heading change.
