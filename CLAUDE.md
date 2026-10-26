# correctness-by-construction

A concept repo (concepts tier, see docs/models/tiers.md): the
plain-words statement of one concept and the executions derived from
it. Documents only — no code, no runs.

## Records

<!-- When to open which record. The record teaches the rest, but only
     once opened, and nothing else says when. Three things per row —
     the moment, what it holds, the path — never the rule itself: what
     an ADR contains is inside the ADR. What it holds summarizes the
     record's item in the records map,
     `docs/conventions/project-recording/` §1. Adding a record means
     adding its row (`docs/conventions/project-recording/` §13). -->

| When | What's in it | Record |
|---|---|---|
| Opening a step, or closing its gate | The step form, and the open step | PLAN.md |
| A decision taken, options rejected | Decisions and why | docs/adr/ |
| Starting work, or noticed something not doing it now | What's next; the backlog | TODO.md |
| A talk shaped a TODO item or an open question, or one is being worked | The talk behind each item, on trial | TODO-CONVERSATION-MEMORY.md |
| Session ending, a dead end hit, or a TODO item added | Work history, dead ends, a TODO item's story | devlog/<YYYY-MM>.md |
| The concept changed, or an execution derived from or checked against it | What changed, for those who pin a concept version | CHANGELOG.md |
| Something became true the outside should see | The front door: what this is, how to use it | README.md |
| How the repo's parts tie together changed | What stands now, and how its parts tie | ARCHITECTURE.md |
| Agent setup changed | Decision, why, rejected options | .claude/decisions.md |
| Work needs more than one commit | In-flight change set | COMMIT-PLAN.md (when present) |

<!-- This file is loaded in full on every task, relevant or not, so
     every line below passes three tests or leaves
     (`docs/conventions/agent-arrangement/` §2.4):
     1. True of this project and nowhere else — else it is a
        convention, stated once, there.
     2. No moment — else it goes where the moment is: the record's
        stub, README, a project skill, or .claude/rules/ with a
        paths: list for a rule about one directory.
     3. Nothing else would deliver it — a stance, or a fact whose
        failure is not noticing it.
     Longer than a screen means a line is failing. Shrinking it is
     maintenance, not tidying.
     foundation: the agent-arrangement convention -->
