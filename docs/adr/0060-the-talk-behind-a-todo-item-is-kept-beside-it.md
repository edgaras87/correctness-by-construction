# 0060. The talk behind a TODO item is kept beside it

Date: 2026-10-21
Status: Accepted (2026-10-21, at the set's records commit; opened
Proposed under the commit plan for the memory file, and changed
twice before acceptance on the reviewer's questions: the file moved
to the root and is read when its item is worked; an item may be an
open question another record holds).

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

Two questions followed the same day. Nothing said to read the talk
when its item is worked, so it could be kept and never used, and
the trial could gather no evidence. And the reviewer expects
something to save for nearly every item, so the file is always in
use, not a draft on its way somewhere.

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
- **The file in `temp/`.** Where the ideas file began. Rejected: a
  file always in use is not temporary, and its rules need a header
  comment, as the records have.
- **The file in `.claude/memory/`.** Rejected: the talk is about the
  work, not about how the agent works. Agent and project files never
  share a commit, so every item would take two. And "memory" there
  would sit beside the agent tool's own memory, which is personal
  and outside the repo.
- **Save every talk, without asking.** Rejected: the reviewer
  decides what is worth keeping.
- **Both seats now.** Rejected: it has been tried once, here. A run
  gets it when it has worked on our seat.

## Decision

1. **The talk behind a TODO item is kept in
   `TODO-CONVERSATION-MEMORY.md`,** at the root, next to `TODO.md`:
   what was asked, what exists, the options weighed, what was said
   for and against. It is a record that decides nothing and tells
   no story: the item's ADR decides, and the devlog tells.
2. **One file, a section per item.** An item is a TODO item, or
   an open question another record holds, such as a step's list for
   a later round; that record names the section, as an item's See
   does. The section names its item. Each talk adds a dated part to
   it, and a part is never rewritten. The file's header comment
   holds its form, its `foundation:` line and the date of its last
   touch.
3. **The item stands alone.** Its Context is enough for triage, and
   its See names the section. A lost section breaks no record.
4. **A section goes in the commit that works its item.** The file
   stays, empty or not, as `TODO.md` does.
5. **The agent asks each time** a talk raises or shapes a TODO
   item: a new section, a part added to one, or nothing, with its
   recommendation. The reviewer decides.
6. **The section is read when its item is worked,** before the
   item's Ideas are weighed. The devlog entry that works the item
   says whether the section changed the work.
7. **Our seat only, on trial,** in
   `docs/conventions/project-recording/` §5.5. The evidence is
   decision 6's devlog lines. It is looked at when the third item
   with a section is worked, or at the refinement step's close,
   whichever comes first. If it holds, it reaches runs through the
   container; if not, it goes.

## Consequences

- Project-recording's deliverer's seat names a seventh difference,
  §5.5 says what the file is, and its list names it among the
  deliverer's records.
- `temp/ideas-2026-10-20.md` becomes `TODO-CONVERSATION-MEMORY.md`.
  TODO's pointers and its header follow it, and so do
  `ARCHITECTURE.md`'s *The words* and codemap and `README.md`'s
  records table.
- `CLAUDE.md`'s records table gains a row for both moments, saving
  and reading, so they are in front of the agent in every session.
- Today's talk is kept: a part on the tiers and chain models in the
  text-division item's section, and sections for the changelog,
  run 4's reading, the method's plain rewrite, and the footers in
  shipped files. The last serves the refinement's list for round 2,
  not a TODO item, which is why an item may be another record's
  open question.
- The cost is one more record kept in step with TODO. A dated part
  says what was thought that day, so an old part is not wrong, only
  old.
