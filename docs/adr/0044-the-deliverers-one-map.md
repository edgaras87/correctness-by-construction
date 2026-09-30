# 0044. The deliverer's one map

Date: 2026-09-30
Status: Accepted (2026-09-30, at the set's records commit; opened
Proposed under the commit plan for one map, and amended at step 6
with decision 6, the codemap's form, the reviewer's choice)

## Context

This repo has two maps of itself. `ARCHITECTURE.md` is the record
`docs/conventions/project-recording/` §8 defines: components,
invariants, a codemap. `docs/master.md` was placed on 2026-09-25,
loose under `docs/`, as "a picture of what is tied to what in this
repo". Since then it has been the better kept of the two: organised
by what is stated, what ships, how it changes and the arrangement,
current, and pointed at by the manuals. Its own list of what it
knows is wrong says that `ARCHITECTURE.md` "describes section 2 a
second time".

ARCHITECTURE shows the cost. Its components repeat the master's §1
and §2, and its *Executions* entry runs to fifty lines of how things
came to be. Its codemap has rows of 1,097 and 782 characters, full
of history, and leaves out this repo's own records. What it holds
that the master does not is its seven invariants, each naming where
the rule is held.

§8 is one description for both seats. A run's ARCHITECTURE maps a
built system: modules, runtime invariants, a `src/` codemap. The
deliverer builds nothing. What it maps is documents and delivery,
which is what the master already does.

## Options considered

- **Two maps, split roles**: ARCHITECTURE holding only the codemap
  and the invariants, pointing at the master for the map. Rejected:
  a thin record beside a non-standard map that is the real one, and
  one fact still a pointer away from its home.
- **One map, named master.** Rejected: ARCHITECTURE is the record
  both seats have and the one a newcomer reads second, after the
  README. "Master" was a name for a working map, placed loose on
  purpose.
- **Merge ARCHITECTURE into the master's shape but keep §8's two
  pages.** Rejected: the deliverer's map carries its vocabulary and
  its list of what it knows is wrong, and neither fits two pages.

## Decision

1. **One map, `ARCHITECTURE.md`.** `docs/master.md` goes, and its
   live pointers name ARCHITECTURE's sections.
2. **Its content comes mostly from the master**: what is stated,
   what ships, how it changes, the arrangement, what must stay true.
   ARCHITECTURE's invariants and the master's "what must stay true"
   become one list.
3. **The deliverer's ARCHITECTURE differs in content, not in file.**
   It maps documents and delivery, keeps its own words and its list
   of what it knows is wrong, and runs past two pages for them. That
   is project-recording's fifth seat difference. A run's §8, its
   stub and its seat do not change.
4. **The map says what is.** How a part came to be is the ADRs' and
   the devlog's, and the map points there.
5. **The word "master" stays** for the canonical file every copy
   comes from. Only the document named for it goes.
6. **The codemap is a tree** in a code block, one line per path,
   descriptions from column 22 (the reviewer's choice). Settled by
   `visual-comparison` on 2026-09-30. The requirements were: a path's
   contents in one look (R1); every tracked top-level path, this
   repo's records included (R2); each entry whole on a line of 100
   characters or fewer, so that one word changed is one line diffed
   (R3); what is there with a pointer for why, and no history (R4);
   which paths sit inside which (R5). The candidates:
   - the table as it stood, which failed R2, R3 and R4, with a
     longest row of 1,097 characters and five words of history;
   - a table with short rows, which held R5 only as a shared path
     prefix;
   - a nested list, which held all five with nothing to maintain;
   - the tree, which shows nesting best, and was chosen with its cost
     accepted. The column is aligned by hand, so a path longer than
     it would move every line. A new path is fitted to the column
     instead.
   Measured on the raw text. GitHub's rendering was not seen, which
   leaves the table's and the list's rendered verdicts as
   predictions. The tree's code block renders as written.

## Consequences

- The master's erratum closes: there is one map.
- Eight pointers into `docs/master.md §N` move, in the exchange,
  conventions and project-recording manuals and the tiers model.
- The codemap is a tree that holds this repo's own records, and the
  map's list of what it knows is wrong is empty.
- The TODO items "Decide whether the master becomes ARCHITECTURE"
  and "Re-render the ARCHITECTURE codemap" close.
