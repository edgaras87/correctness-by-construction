# <working-name>

A backend service to be built by correctness-by-construction. Its
design is derived from one Falsifiable Promise: what must never
happen first, features last. The problem arrives with the CBC Run
Briefing.

<!-- This paragraph states only what never changes: the method,
     the problem once the CBC Run Briefing names it, its CBC Framing
     date. No current state. A state clause is true at one time, and
     stales at every Plan Step's close. Where the project stands is
     PLAN's, by the records table. -->

## Correctness by construction

The method is in `docs/concept/`. Read `docs/concept/00-cbc.md` first.
The other chapters deepen it. It is not restated here: the order of
questions lives there, and the method's reading of each record
lives in that record's own comments.

Until the CBC Framing Exports exist (the cbc-framing Agent Skill
creates them, under `docs/system/`), the project is before CBC
Framing. The only method work then is running the cbc-framing Agent
Skill jointly with the reviewer. Never invent the CBC Framing
Exports to fill the gap.

`docs/concept/`, and the Agent Skills, Agent Rules, Output Shapes and Approaches on Trial
that arrived with a delivery, are copies, pinned; what may be done to
them is `.claude/rules/delivered-copies.md`. An Agent Skill, Agent Rule or Approach on Trial
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
| Starting work, or closing a Plan Step Gate | Current state, next Plan Steps, Plan Step Gates | PLAN.md |
| A decision taken, options rejected | Decisions and why | docs/adr/ |
| Noticed something, not doing it now | Backlog | TODO.md |
| Session ending, a dead end hit, or a TODO item added | Work history, dead ends, a TODO item's story | devlog/devlog.md |
| Shipped something users can see | What changed, for users | CHANGELOG.md |
| The system's structure changed, or asking what an Invariant Slice may rely on | The system as it stands: its components, what an Invariant Slice may rely on, one row per invariant | ARCHITECTURE.md |
| The Falsifiable Promise, the System Layers or the Invariant Slices are in question | CBC Framing Intent, System Definition, Invariant Slice Registry | docs/system/ |
| Meeting a Glossary Name or a tag you do not know, or defining a thing | The Glossary Names and tag kinds this project defines, one plain sentence each; the delivered ones are in `docs/glossary/` | docs/glossary.md |
| Something became true the outside should see | The first page: what this is, how to use it | README.md |
| Agent setup changed, or a convention arrives | Decision, why, rejected options; the conventions held, the Delivery Pin | .claude/decisions.md |
| The CBC Run has finished building, before Release | What the next CBC Run does differently, and where each lesson lands | RETRO.md (when present) |
| Work needs more than one commit | In-flight Change Set | COMMIT-PLAN.md (when present) |

<!-- This file is loaded in full on every task, relevant or not, so
     every line below passes three tests or leaves
     (CBC docs/conventions/agent-arrangement/ §2.4, How the Entry File is written):
     1. True of this project and nowhere else — else it is a
        convention, stated once, there.
     2. No moment — else it goes where the moment is: the record's
        Record Stub, README, a project Agent Skill, or .claude/rules/ with a
        paths: list for a rule about one directory.
     3. Nothing else would deliver it — a stance, or a fact whose
        failure is not noticing it.
     Longer than a screen means a line is failing. Shrinking it is
     maintenance, not tidying.
     foundation: the agent-arrangement convention -->

## Local rules

- Nothing before the CBC Run Briefing names the problem.
