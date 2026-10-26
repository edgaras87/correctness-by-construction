<!-- A visual-comparison draft for the records map, project-recording
     §1 (the commit plan for the records map, commits 2 to 4). Data
     only: how it is worked is `visual-comparison`. Deleted when
     ADR-0067 records the outcome; git keeps it. -->

# The records map: a comparison

## The defect

What each record holds is told in four places that differ:
`CLAUDE.md`'s records table, `README.md`'s "What it answers" column,
`ARCHITECTURE.md`'s codemap and `temp/README.md` (round 2's
FINDING-145). For the devlog, README says "open questions" and
`CLAUDE.md` "a TODO item's story". No text shows both seats' records
side by side. The refinement's DECISION-12 makes project-recording
§1 the overview each seat's table and the README derive from.
Refined by the reviewer on 2026-10-26: the map is a summary, home
to nothing. Each row points at the home of its fact: the record's
section in project-recording, or its owner's manual; how the seats
differ stays in project-recording's *The seats*.

## The records

Thirteen, from the stubs, both entry files' tables and
project-recording:

- **both seats:** `README.md`, `PLAN.md`, `TODO.md`,
  `CHANGELOG.md`, `ARCHITECTURE.md`, `docs/adr/`, `devlog/`,
  `.claude/decisions.md` (agent-arrangement's), `COMMIT-PLAN.md`
  (commit-plan's), when present;
- **the run's only:** `docs/system/` and `docs/glossary.md`, both
  the method's, from framing; `RETRO.md` (the retrospective's),
  when present;
- **ours only:** `TODO-CONVERSATION-MEMORY.md`, on trial.

## Requirements

What a reader of the map must get. Each can fail.

1. **What each record answers,** a line each, with a fact
   reference to where its full what and why live: its section in
   project-recording, or the manual of the convention or method
   that owns it.
2. **Which seats keep it:** both, ours only, or the run's only, for
   every record, without reading a seat's section.
3. **Where the seats differ,** the row says so and points at where
   the difference is stated, project-recording's *The seats*. Seven
   differences today.
4. **Every record,** the thirteen above, with the convention or the
   method that owns it where that is not project-recording.
5. **Which record answers a question:** a reader holding "where is
   the why of X recorded?" finds the record from the question.
6. **How the records feed each other** where it matters: the plan
   as the spine, a decision summarized into the map of the system,
   the lessons folding back into the playbook. Today's §1 picture
   carries this.
7. **No moment and no how:** when a record is opened is each seat's
   table's (§13), and how it is written is its form's. The map
   holds neither, so it is no second home for them.
8. **One view:** all thirteen readable without scrolling past one
   screen, about 40 lines.
9. **Plain text that renders** on GitHub and in the IDE with no
   build step, and reads in a diff.
10. **It says it is a summary,** and names its owners, so nobody
    reads it in their place (`.claude/rules/one-home.md`, rule 3).

## Candidates

Built in the next commit: a table, a numbered list, a Mermaid
picture, Unicode box drawing, and today's §1 picture.
