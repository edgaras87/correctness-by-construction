# correctness-by-construction

A Concept Repo (`docs/models/tiers.md` §2.2, *Concept Repos*): one
concept in plain words, and what is made from it. It is the
Concept Deliverer. A CBC Run is a separate repository that builds a
real system by the concept. Each is born from what this repo ships,
and is read back from here. Documents only — no code, no CBC Runs
(`README.md`).

## Records

<!-- When to open which record. The record teaches the rest, but only
     once opened, and nothing else says when. Three things per row:
     the moment, what it holds, the path. Never the rule itself: what
     an ADR contains is inside the ADR. What it holds summarizes the
     record's item in project-recording's list of the records
     (docs/conventions/project-recording/ §1, The records at a glance). Adding a record means
     adding its row (`docs/conventions/project-recording/` §13, The records table). -->

| When | What's in it | Record |
|---|---|---|
| Opening a Plan Step, or closing its Plan Step Gate | The Plan Step Form, and the open Plan Step | PLAN.md |
| A decision taken, options rejected | Decisions and why | docs/adr/ |
| Starting work, or noticing something to do later | What's next; the backlog | TODO.md |
| A talk shaped a TODO item or an open question, or one is being worked | The Conversation Memory of each item, on trial | TODO-CONVERSATION-MEMORY.md |
| Session ending, a dead end hit, or a TODO item added | Work history, dead ends, a TODO item's story | devlog/<YYYY-MM>.md |
| The concept changed, or an Agent Skill derived from or checked against it | What changed, for those who pin a concept version | CHANGELOG.md |
| Something became true the outside should see | The first page: what this is, how to use it | README.md |
| How the repo's parts tie together changed | What stands now, and how its parts tie | ARCHITECTURE.md |
| Meeting a Glossary Name, or defining a thing | The Glossary Names, each pointing at its home | docs/glossary.md |
| Agent setup changed | Decision, why, rejected options | .claude/decisions.md |
| Work needs more than one commit | In-flight Change Set | COMMIT-PLAN.md (when present) |

<!-- This file is loaded in full on every task, relevant or not
     (`docs/conventions/agent-arrangement/` §2.6, The Entry File's size), so every line
     below passes three tests or leaves
     (`docs/conventions/agent-arrangement/` §2.4, How the Entry File is written):
     1. True of this project and nowhere else. Otherwise it belongs in a
        manual, stated once.
     2. No moment. Otherwise it goes where the moment is: the record's
        Record Stub, README, a project Agent Skill, or a Paths Rule in
        .claude/rules/ for one directory.
     3. Nothing else would deliver it: a stance, or a fact nobody
        would notice was missing.
     Longer than a screen means a line is failing. Shrinking it is
     maintenance, not tidying.
     foundation: the agent-arrangement convention -->
