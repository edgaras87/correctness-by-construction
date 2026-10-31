# <working-name>

A backend service to be built by correctness-by-construction —
the design derived from one falsifiable promise, what must never
happen first, features last. The problem arrives with the
Run Briefing.

<!-- This paragraph states only what never changes: the method,
     the problem once the Run Briefing names it, its framing date. No
     current state — a state clause has a moment and stales at
     every Plan Step's close; where the project stands is PLAN's, by
     the records table. -->

## Correctness by construction

The method is in `docs/concept/` — read `docs/concept/00-cbc.md` first; the
other chapters deepen it. It is not restated here: the order of
questions lives there, and the method's reading of each record
lives in that record's own comments.

Until the framing artifacts exist (cbc-framing creates them, under
`docs/system/`), the project is pre-framing: the only method work
is running cbc-framing jointly with the human — never invent the
artifacts to fill the gap.

`docs/concept/`, and the skills, Agent Rules, Output Shapes and Approaches on Trial
that arrived with a delivery, are copies, pinned; what may be done to
them is `.claude/rules/delivered-copies.md`. A skill, Agent Rule or Approach on Trial
this project writes is its own. The words these files are written in
arrive with them, in `docs/glossary/`; this project's own are
`docs/glossary.md`'s.

## Records

<!-- When to open which record. The record teaches the rest, but only
     once opened, and nothing else says when. Three things per row —
     the moment, what it holds, the path — never the rule itself: what
     an ADR contains is inside the ADR. Adding a record means adding
     its row (CBC docs/conventions/project-recording/ §13, The records
     table). -->

| When | What's in it | Record |
|---|---|---|
| Starting work, or closing a Plan Step's gate | Current state, next Plan Steps, gates | PLAN.md |
| A decision taken, options rejected | Decisions and why | docs/adr/ |
| Noticed something, not doing it now | Backlog | TODO.md |
| Session ending, a dead end hit, or a TODO item added | Work history, dead ends, a TODO item's story | devlog/devlog.md |
| Shipped something users can see | What changed, for users | CHANGELOG.md |
| The system's structure changed, or asking what a slice may rely on | The system as it stands: its components, what a slice may rely on, one row per invariant | ARCHITECTURE.md |
| The promise, the layers, or the slices are in question | Intent, system definition, slice registry | docs/system/ |
| Meeting a Glossary Name or a tag you do not know, or defining a thing | The Glossary Names and tag kinds this project defines, one plain sentence each; the delivered ones are in `docs/glossary/` | docs/glossary.md |
| Something became true the outside should see | The front door: what this is, how to use it | README.md |
| Agent setup changed, or a convention arrives | Decision, why, rejected options; the conventions held, the Delivery Pin | .claude/decisions.md |
| The CBC Run has finished building, before Release | What the next CBC Run does differently, and where each lesson lands | RETRO.md (when present) |
| Work needs more than one commit | In-flight Change Set | COMMIT-PLAN.md (when present) |

<!-- This file is loaded in full on every task, relevant or not, so
     every line below passes three tests or leaves
     (CBC docs/conventions/agent-arrangement/ §2.4, How the entry file is written):
     1. True of this project and nowhere else — else it is a
        convention, stated once, there.
     2. No moment — else it goes where the moment is: the record's
        Record Stub, README, a project skill, or .claude/rules/ with a
        paths: list for a rule about one directory.
     3. Nothing else would deliver it — a stance, or a fact whose
        failure is not noticing it.
     Longer than a screen means a line is failing. Shrinking it is
     maintenance, not tidying.
     foundation: the agent-arrangement convention -->

## Local rules

- Nothing before the Run Briefing names the problem.
