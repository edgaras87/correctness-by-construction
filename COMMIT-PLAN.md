# Commit plan: conversation-memory

The talk behind a TODO item, kept beside it in `temp/`, as the
reviewer decided on 2026-10-21. `temp/ideas-2026-10-20.md` becomes
`temp/conversation-memory.md`, and project-recording says what it
is, on our seat only, on trial. Descriptions first, then what
derives from them.

## Summary — the state after all commits

A TODO item still stands alone. Beside it, when a talk held more
than the item can, `temp/conversation-memory.md` keeps that talk:
one file, a dated section per item, the date of its last touch in
its header. Each section goes when its item is worked. The agent
asks the reviewer before saving any, with a recommendation. The
rule is project-recording's, in the deliverer's seat, on trial: it
reaches runs only if it works here. Today's talk is in it: the
changelog, the footers, the tiers and chain models, layer 6's
moves.

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

**4. `docs: temp's ideas become conversation-memory`**
`git mv` to `temp/conversation-memory.md`; its header says what it
is now, with the date of its last touch; its sections dated. In the
same commit, every pointer to the old path: `TODO.md`'s three;
`temp/README.md`'s kept-file line names it; `ARCHITECTURE.md`'s
*The words* defines the word.

**5. `docs(temp): conversation-memory takes today's talk`**
Four new sections, rebuilt from this session's transcript, not
from memory: what our changelog tracks; the footers in shipped
files; the tiers and chain models behind `abae9c4`; why layer 6's
three items moved (`7db58ed`). Each TODO item they serve points at
its section from its See line.

**6. `chore(agent): the entry file asks for the talk`**
`CLAUDE.md`'s records table gains the row, with the ask; one entry
in `.claude/decisions.md`.

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
