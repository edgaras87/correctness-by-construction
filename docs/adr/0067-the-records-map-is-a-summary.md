# 0067. The records map is a summary: a list, and a picture per seat

Date: 2026-10-26
Status: Accepted (2026-10-26, at the set's records commit; opened
Proposed under the commit plan for the records map, the render added
since).

## Context

What each record holds was told in four places that differed:
`CLAUDE.md`'s records table, `README.md`'s "What it answers" column,
`ARCHITECTURE.md`'s codemap and `temp/README.md` (the refinement's
FINDING-145). No text showed both seats' records side by side. The
refinement step's gate asks for project-recording §1 to show, in one
view, which record answers what in both seats, its form chosen by
`visual-comparison`.

The refinement's DECISION-12 (2026-10-25) made §1 the home of what
each record is and why. But each record's what and why already has
a home: its section in project-recording, or the manual of the
convention or method that owns it. How the seats differ has one too,
project-recording's *The seats*.

The comparison ran in `temp/records-map.md` (`6acc334`, `ca6ca58`).
Ten requirements were written first, as what the map's reader must
get: what each record answers, with its home; which seats keep it;
where they differ; all thirteen records, with their owners; a record
found from a question; how the records feed each other; no moment
and no how; one view of about 40 lines; plain text that renders and
diffs; and saying it is a summary. The verdicts were predictions,
marked so; the reviewer chose by reading the draft, then rendered
every candidate in the IDE before acceptance: all render, and the
choice stands.

## Options considered

- **The map as the home of what each record is and why,**
  DECISION-12 as written. Rejected: it would make the map a second
  home for every record's section and for three conventions'
  manuals.
- **A table** of record, what it answers, seats and home, with one
  sentence for how the records feed each other. Predicted to pass
  every requirement. Not taken: a sentence carries the relations
  thinly, and one table mixes two seats a reader holds one at a
  time.
- **The numbered list alone.** The same sentence for the relations.
- **A Mermaid picture.** Its labels cut each record's answer short,
  a record is hard to find from a question, and the IDE needs its
  Mermaid support switched on.
- **Unicode box drawing of all thirteen.** Each line cut to fit a
  column says less than a list item.
- **Today's §1 picture.** Seven records of thirteen, no seats, no
  homes, and its arrows labelled with moments, which are the records
  table's.

## Decision

1. **The map is a summary.** It answers which record answers what,
   and is home to nothing. Each item carries a fact reference to its
   home, and says it is a summary.
2. **Its form is the numbered list by seat, then one picture per
   seat,** the run's and ours, for how the records feed each other.
   A reader holds one seat at a time.
3. **The pictures' arrows say what a record holds for the plan,**
   never when it is written: the moment is each seat's records
   table's (project-recording §13).
4. **The one-view requirement is struck.** The chosen form runs to
   about 65 lines; each part fits a screen, and a reader reads one
   seat's picture at a time.
5. **Each seat's records table derives from the map:** its *When*
   is its own, and its *What's in it* is a summary. Ours names the
   map; the run's does not, since a run cannot open our manuals.

## Consequences

- Project-recording §1 is rewritten as the map, under a heading
  that names records.
- Both entry files' tables, the README's column and
  `temp/README.md` follow it. The codemap waits for TODO's "Decide
  what kind of text our ARCHITECTURE is", due before layer 4's
  fixes.
- The refinement's DECISION-12 is refined as decision 1 says.
