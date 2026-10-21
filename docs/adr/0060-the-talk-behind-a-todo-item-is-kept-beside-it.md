# 0060. The talk behind a TODO item is kept beside it

Date: 2026-10-21
Status: Proposed (2026-10-21, under the commit plan for the memory
file).

## Context

A TODO item holds what triage needs, and no more. Its Context is
eight lines at most, so an item reads without opening its pointer
(ADR-0040). Its story goes in that session's devlog entry when the
item is added (`docs/conventions/project-recording/` §5.4). Neither
keeps the talk that shaped the item: what was asked, the options
weighed, what was said for and against, the reviewer's own words.

On 2026-10-20 the reviewer's ideas raised three TODO items. Their
talk was kept in `temp/ideas-2026-10-20.md` (`8734c3b`): a section
per item, not a record and not a decision, each section going when
its item is worked.

On 2026-10-21 a talk on the changelog weighed nine considerations,
and the TODO item kept seven lines of Ideas from it. The reasons
behind each were in the chat only. The reviewer asked to make the
ideas file part of how a TODO item is kept: the item does not
change, and the talk is kept beside it, so the work has it when the
item comes due. If the talk is lost, the item still stands.

## Options considered

- **A new dated file per talk.** The agent's recommendation: each
  file written once, so it cannot drift. Rejected by the reviewer:
  one file is one place to look, and dated parts keep what was
  thought that day as well.
- **The talk in the item's Context.** Rejected: the eight-line cap
  is what lets triage read an item in one look (ADR-0040).
- **The talk in the devlog.** Rejected: the devlog is history and
  never changes, while a talk goes when its item is worked; and the
  talk would bury what happened.
- **Save every talk, without asking.** Rejected: most items need
  none, and the reviewer decides what is worth keeping.
- **Both seats now.** Rejected: it has been tried once, here. A run
  gets it when it has worked on our seat.

## Decision

1. **The talk behind a TODO item may be kept in
   `temp/conversation-memory.md`:** what was asked, what exists,
   the options weighed, what was said for and against. It is not a
   record and not a decision. The item's ADR decides.
2. **One file, a section per item.** The section names its item.
   Each talk adds a dated part to it, and a part is never
   rewritten. The header carries the date of the file's last touch.
3. **The item stands alone.** Its Context is enough for triage, and
   its See names the section. If the file is lost, no record
   breaks.
4. **A section goes in the commit that works its item.** The file
   goes with its last section, and the next talk worth keeping
   starts it again.
5. **The agent asks each time** a talk raises or shapes a TODO
   item: a new section, a part added to one, or nothing, with its
   recommendation. The reviewer decides.
6. **Our seat only, on trial,** in
   `docs/conventions/project-recording/` §5. The evidence is an
   item worked with its section in hand, and whether the section
   changed the work. It is looked at when the third such item is
   worked, or at the refinement step's close, whichever comes
   first. If it holds, it reaches runs through the container; if
   not, it goes.

## Consequences

- Project-recording's deliverer's seat names a seventh difference,
  and §5 gains a section on trial.
- `temp/ideas-2026-10-20.md` becomes `temp/conversation-memory.md`.
  TODO's three pointers follow it, `temp/README.md` names it, and
  `ARCHITECTURE.md`'s *The words* defines the word.
- `CLAUDE.md`'s records table gains a row, so the ask is in front of
  the agent in every session.
- Today's talk gets four sections: the changelog, the footers in
  shipped files, the tiers and chain models, and layer 6's moves.
- The cost is one more file kept in step with TODO. A dated part
  says what was thought that day, so an old part is not wrong, only
  old.
