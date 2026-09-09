# correctness-by-construction

A concept repo (concepts tier, see docs/models/tiers.md): the
plain-words statement of one concept and the executions derived from
it. Documents only — no code, no runs.

## Records

<!-- When to open which record. The record teaches the rest, but only
     once opened, and nothing else says when. Three things per row —
     the moment, what it holds, the path — never the rule itself: what
     an ADR contains is inside the ADR. Adding a record means adding
     its row. -->

| When | What's in it | Record |
|---|---|---|
| Starting work, or closing a step's gate | Current state, next steps, gates | PLAN.md |
| A decision taken, options rejected | Decisions and why | docs/adr/ |
| Noticed something, not doing it now | Backlog | TODO.md |
| Session ending, or a dead end hit | Work history, dead ends | devlog/devlog.md |
| Shipped something users can see | What changed, for users | CHANGELOG.md |
| Something became true the outside should see | The front door: what this is, how to use it | README.md |
| The system's shape changed | Shape of the system | ARCHITECTURE.md |
| Agent setup changed, or a convention arrives | Decision, why, rejected options; the conventions held, with versions | .claude/decisions.md |
| Work needs more than one commit | In-flight change set | CHANGE-PLAN.md (when present) |

<!-- This file is loaded in full on every task, relevant or not, so
     every line below passes three tests or leaves (agent-arrangement):
     1. True of this project and nowhere else — else it is a
        convention, stated once, there.
     2. No moment — else it goes where the moment is: the record's
        stub, README, a project skill, or .claude/rules/ with a
        paths: list for a rule about one directory.
     3. Nothing else would deliver it — a stance, or a fact whose
        failure is not noticing it.
     Longer than a screen means a line is failing. Shrinking it is
     maintenance, not tidying. -->
