# Commit plan: conversation-memory

The talk behind a TODO item, kept beside it, as the reviewer
decided on 2026-10-21. `temp/ideas-2026-10-20.md` becomes
`TODO-CONVERSATION-MEMORY.md` at the root, next to `TODO.md`, and
project-recording says what it is, on our seat only, on trial.
Descriptions first, then what derives from them.

## Summary — the state after all commits

A TODO item still stands alone. Beside it,
`TODO-CONVERSATION-MEMORY.md` keeps the talk that shaped it: one
file, a section per item, each talk a dated part, the date of its
last touch and its form in its header comment. A section goes when
its item is worked; the file stays. The agent asks the reviewer
before saving any talk, with a recommendation, and reads an item's
section before its Ideas are weighed; the devlog says whether the
section changed the work. The rule is project-recording's, in the
deliverer's seat, on trial: it reaches runs only if it works here.
Today's talk is in it: the changelog, the footers, the tiers and
chain models, layer 6's moves.

## Commits

**1. `docs(agent): add commit plan for the memory file`**
This file.

**2. `docs: ADR-0060 keeps the talk beside TODO`**
Proposed. The decisions: one file, dated sections, the last touch
inside; the agent always asks, with a recommendation; our seat
only, on trial; the item stands alone. Rejected: a new dated file
per talk; the talk in the item's Context or the devlog; both seats
now.

**3. `docs: project-recording takes conversation-memory`**
The manual: the deliverer's seat gains a seventh difference; §5
gains a section on it, marked *on trial*, with what would make it
evidence and when to look again. The foundation check walks what
derives from the manual.

**3a. `docs: the memory sits beside TODO, and is read`**
Inserted on the reviewer's questions after commit 3. ADR-0060 and
§5.5 change together: the file is `TODO-CONVERSATION-MEMORY.md` at
the root, a record whose header comment holds its form, and it
stays when empty; the section is read when its item is worked,
before its Ideas are weighed, and the devlog says whether it
changed the work. Rejected, added to the ADR: `temp/`, for a file
always in use; `.claude/memory/`, for the talk is the work's, not
the agent's, and every item would take two commits.

**4. `docs: temp's ideas become TODO's memory`**
`git mv temp/ideas-2026-10-20.md TODO-CONVERSATION-MEMORY.md`; its
header comment holds its form, with a `foundation:` line and the
date of its last touch; its sections dated. In the same commit,
every pointer to the old path and what follows the rule:
`TODO.md`'s three pointers, and its header, where Ideas are weighed
with the item's section; the deliverer's records in
project-recording's list; `ARCHITECTURE.md`'s *The words* and its
codemap; `README.md`'s records table; `temp/README.md` drops the
example it gave.

**5. `docs: TODO's memory takes today's talk`**
Four new sections, rebuilt from this session's transcript, not
from memory: what our changelog tracks; the footers in shipped
files; the tiers and chain models behind `abae9c4`; why layer 6's
three items moved (`7db58ed`). Each TODO item they serve points at
its section from its See line.

**6. `chore(agent): the entry file asks for the talk`**
`CLAUDE.md`'s records table gains the row, with both moments: a
talk that raised or shaped an item, and an item being worked. One
entry in `.claude/decisions.md`.

**7. `docs: ADR-0060 accepted`**
The ADR flips to Accepted; today's devlog entry gets the story.

**8. `docs(agent): close commit plan for the memory file`**

## Decisions taken inside this plan

- **The rule lands before the file moves,** so the rename follows a
  rule that already says what the file is.
- **The rename and its pointers are one commit,** so nothing points
  at a missing path (`.claude/rules/foundation-check.md`, *A moved
  section*).
- **The agent's file comes after the project's,** its own commit, as
  every set does.
- **Any rewrap is by hand.**
