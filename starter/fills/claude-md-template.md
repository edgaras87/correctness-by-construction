<!-- Derives from concept v1 of correctness-by-construction
     (ADR-0003). Re-cut fresh 2026-09-06, user's design: the
     past-run harvest — the five stance bullets, walk-1's own
     derivation text merged by ADR-0014, earned under a different
     arrangement than the current skills — is stripped and frozen
     at docs/baselines/claude-md-template-v1.md for the three-way
     reading after the next full run. Harvest re-enters only from
     a run reading, each line traceable to the run that earned it
     under the current skills. The pre-framing guard was stripped
     with them, then restored same day: it is garden-authored
     (the withdrawn snippet's line, no run's text), the pure seed
     ships no template so the derivation measurement is
     untouched, and the assembly path keeps its brake.
     — the kit half: engineering-handbook starter/kit/CLAUDE.md
       @ af16eb7 — the title line, the records table and its
       comment, the guard comment, all verbatim; their
       agent-arrangement convention holds this half's rules. At
       each kit re-pin, re-verify this half against their entry
       file at the new pin. (Re-pinned 2026-09-09 from c670fe5:
       the guard names .claude/rules/ and drops its example.)
     — this repo's own fills, no run's text: the orientation
       (the kit's orientation comment, filled problem-agnostic),
       the CbC pointer, the pre-framing guard, the pin stance,
       the docs/system/ row in the records table (2026-09-09, the
       handbook's checkout reading: a record gets a row), and the
       Local rules (the briefing rule; the trial line
       that stood beside it left with ADR-0016 — its own removal
       clause honored, the scenario it named retired).
     Use: delivered by the seed's semi-pure step (pure-seed.md
     step 4, ADR-0019, 2026-09-07 — ADR-0016's parking condition
     fired at run 2's Step 0 reading): the copy is whole from the
     title line down, this header stays here, no merge into the
     kit's stub (ADR-0015), the seed filling <working-name>. With
     the step off, the newborn derives its own and this file is
     the reading's comparison object.
     Authoring: every edit to the body below answers to the
     copy's own guard comment, read at authoring time — a line
     here is loaded by every future project on every task and is
     rarely pruned once shipped; the three tests and the screen
     budget bind this file harder than any live copy. -->

# <working-name>

A backend service to be built by correctness-by-construction —
the design derived from one falsifiable promise, what must never
happen first, features last. Until the briefing brings the
problem, this repo is method and records, ready to start:
nothing to build, no tests, no runtime.

## Correctness by construction

The method is in `docs/concept/` — read `00-cbc.md` first; the
other chapters deepen it. It is not restated here: the order of
questions (promise → guarantees → structure → features → code,
never backwards) lives there, and the method's reading of each
record lives in that record's own comments.

Until the framing artifacts exist (cbc-framing creates them, under
`docs/system/`), the project is pre-framing: the only method work
is running cbc-framing jointly with the human — never invent the
artifacts to fill the gap.

`docs/concept/` and the method skills under `.claude/skills/` are
pinned copies: never edited in place — a change is a new copy
from the source, logged in `.claude/decisions.md`.

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
| The system's shape changed | Shape of the system | ARCHITECTURE.md |
| The promise, the layers, or the slices are in question | Intent, system definition, slice registry | docs/system/ |
| Something became true the outside should see | The front door: what this is, how to use it | README.md |
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

## Local rules

- Nothing before the briefing names the problem.
