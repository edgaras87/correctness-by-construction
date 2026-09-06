<!-- Derives from concept v1 of correctness-by-construction
     (ADR-0003). Composed 2026-09-05 (ADR-0015) from two masters,
     each half attributable:
     — the kit half: engineering-handbook starter/kit/CLAUDE.md
       @ c670fe5 — the title line, the records table and its
       comment, the guard comment, all verbatim; their
       agent-arrangement convention holds the rules this half
       answers to, and names the two section headings below.
       Refreshed at each kit re-pin: re-read their entry file at
       the new pin and re-verify this half against it.
     — the method half: the shipped text merged once from the
       first walked birth (ADR-0014; the fragment history is
       claude-md-cbc.md's, retired 2026-09-05 — see git). The CbC
       section, the stance lines, the local rules. Changes flow
       back as harvest, never as per-birth rewrites.
     The orientation lines are this repo's fill of the kit's
     orientation comment, problem-agnostic by design.
     Trial note: the first Local-rules line ships only while the
     birth-scenario trial runs; the trial-closing ADR removes it
     from this file. The second is permanent until the briefing
     lands, after which the newborn may retire it from its copy.

     Use: assembly step 3 copies everything from the title line
     down, whole, as the newborn's CLAUDE.md — no merge into the
     kit's stub, no section anchors assumed (ADR-0015). The seed
     fills <working-name>. After birth the copy is the newborn's
     own arrangement, maintained by it.
     2026-09-06 harvest from pure-seed run 1, whose agent derived
     a CLAUDE.md blind to this file: the orientation gains the
     falsifiable-promise line and the CbC section the
     pinned-copies stance — both that run's inventions. The
     counter-evidence is also on file: its lean derivation
     dropped the framing guard and the stance bullets — kept
     here deliberately, as harvested brakes a fresh derivation
     does not reproduce (the reading, concept-repo TODO). The
     file's delivery fate — the pure seed excludes it — is the
     trial-close ADR's question, not this comparison's.
     Authoring rules (2026-09-06): every edit to the body below
     answers to the copy's own guard comment, read at authoring
     time — a line here is loaded by every future project on
     every task, and a shipped line is rarely pruned, so the
     three tests and the screen budget bind this template harder
     than any live copy. At each bundle harvest or concept
     re-pin, re-read the stance bullets and the CbC section
     against docs/concept/ — they are its compressed reading and
     drift silently otherwise. "A backend service" is a
     harvested presumption (every run so far has been one);
     unhardcode at the first non-backend run. -->

# <working-name>

A backend service to be built by correctness-by-construction —
the design derived from one falsifiable promise, what must never
happen first, features last. Until the briefing brings the
problem, this repo is method and records, ready to start:
nothing to build, no tests, no runtime.

## Correctness by construction

The method is in `docs/concept/` — read `00-cbc.md` first; the
other four chapters deepen it. It is not restated here: the order
of questions (promise → guarantees → structure → features → code,
never backwards) lives there, and each record's birth fill carries
the method's reading of that record.

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
| Something became true the outside should see | The front door: what this is, how to use it | README.md |
| Agent setup changed, or a convention arrives | Decision, why, rejected options; the conventions held, with versions | .claude/decisions.md |
| Work needs more than one commit | In-flight change set | CHANGE-PLAN.md (when present) |

<!-- This file is loaded in full on every task, relevant or not, so
     every line below passes three tests or leaves (agent-arrangement):
     1. True of this project and nowhere else — else it is a
        convention, stated once, there.
     2. No moment — else it goes where the moment is: the record's
        stub, README, a project skill.
     3. Nothing else would deliver it — a stance, or a fact whose
        failure is not noticing it, like a generated directory nobody
        may edit by hand.
     Longer than a screen means a line is failing. Shrinking it is
     maintenance, not tidying. -->

## How to work here

- Design conversations before build conversations. Framing runs on
  paper; no language, store, or framework is named before the first
  slice.
- When asked for a feature, ask which guarantee it serves. If none,
  the answer is a recorded refusal, not a quiet yes.
- Name the kill, not the cure: state what dies under an attack before
  choosing a mechanism.
- Prefer the wall over the test. A green test proves the wall was
  there once; only structure makes the attack meaningless.
- Watch for the rot: a feature shipped without re-checking guarantees,
  an admin path around the single entry, guarantees drifting into the
  test suite, theory before the world is bounded.

## Local rules

- Step 0 here is a trial of `docs/birth-scenario.md`: it is the
  procedure, and every divergence from it is written into the
  devlog, not fixed silently.
- Nothing before the briefing names the problem.
