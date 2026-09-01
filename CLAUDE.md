
# correctness-by-construction

A concept repo (concepts tier, see docs/models/tiers.md): the
plain-words statement of one concept and the executions derived from
it. Documents only — no code, no runs.

## Records

<!-- Where project state lives, and WHEN to go there. This table is the
     ONE thing that must be in context every session. The records teach
     their own use through the comments inside them — but only once you
     have opened them, and nothing else tells you when to.

     Three things per row — the moment, what the record holds, the path
     — and never the rule itself: what an ADR contains, or how a devlog
     entry is written, is inside the record. Adding a record means
     adding its row (ADR-0018). -->

| When | What's in it | Record |
|---|---|---|
| Starting work, or closing a step's gate | Current state, next steps, gates | PLAN.md |
| A decision taken, options rejected | Decisions and why | docs/adr/ |
| Noticed something, not doing it now | Backlog | TODO.md |
| Session ending, or a dead end hit | Work history, dead ends | devlog/devlog.md |
| Shipped something users can see | What changed, for users | CHANGELOG.md |
| Something became true the outside should see | The front door: what this is, how to use it | README.md |
| The system's shape changed | Shape of the system | ARCHITECTURE.md |
| Agent setup changed | Decision, why, rejected options | .claude/decisions.md |

## Conventions

<!-- Which conventions this project follows. Paths only — NEVER restate
     a rule here. A path cannot be a lossy copy of a rule; a summary
     can, and will be (ADR-0014).

     Conventions delivered as skills live in .claude/skills/ and load
     themselves. List them anyway, so a human can see what the project
     adopted without going digging.

     The record system is not listed: it is delivered by the record
     files themselves, each carrying its rules in its own comments, so
     there is nothing to point at. -->

- Records — the stubs carry their own rules (project-recording)
- Commits — `.claude/skills/commit-messages/`
- Multi-commit work — `.claude/skills/change-plans/`
- Artifact kinds — `.claude/skills/artifact-kinds/`
- Hygiene — `.gitignore` `.gitattributes` `.editorconfig` (repo-hygiene)

<!-- SIZE BUDGET: this file is loaded in full, on every task, relevant
     or not. It is the only text that costs something even when it is
     useless. If it is longer than a screen, something in it belongs in
     a convention, a record, or a skill. Shrinking it is maintenance,
     not tidying. -->
