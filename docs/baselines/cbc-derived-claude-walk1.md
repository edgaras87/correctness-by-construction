<!-- Derivation capture — trial evidence, NOT a master (ADR-0012).
     The first walked birth's derived CLAUDE.md, verbatim below the
     line: cbc-newborn @ 56352d1 (walk 1 pristine close,
     2026-09-03), derived from concept v1 with no arrangement text
     supplied. Captured here because run repos die and trial
     evidence must not share a run's lifespan.
     Blind, like the snippet beside it: never shown to a newborn —
     a future derivation that has seen this one measures imitation,
     not the concept's legibility. Comparison input for the next
     walk's reading and the trial-close ADR (stay/retire/merge of
     cbc-startup-snippet.md); convergence between independent
     derivations is the metric. Nothing copies this file at birth.
     First reading vs the snippet (devlog 2026-09-03): standing
     guards re-derived in own words; missed the human sign-off
     gates and the docs/system/ framing-artifact home; novel and
     best: the records-carry-the-method mapping.
     2026-09-04: comparison consumed (ADR-0014) — merged with the
     snippet into starter/bundle/claude-md-cbc.md, this derivation
     the base: its stance and local-rule lines ship verbatim, its
     records mapping ships through the birth fills; its concept
     summary and step-routing rows were dropped at the merge
     review as restatement and staleness, not comparison losses.
     The experiment does not repeat; held as the comparison's
     record, still blind. -->


# cbc-newborn

A backend not yet named, born to be built by correctness-by-
construction: one falsifiable promise, derived down to the structures
that make breaking it impossible. Problem and stack are still open —
the briefing arrives after Step 0, the stack with the first slice.

## Correctness by construction

The method is in `concept/` — read `00-cbc.md` first; the other four
chapters deepen it. Everything below is this repo's reading of it.

The first question here is never "what should it do" but "what must
never happen, and what throws it at us." From that, in this order and
never backwards: promise → guarantees → structure → features → code.
A feature list is an output. Staying small is the discipline.

What the kit's records carry under this method:

- README opens with the promise: one sentence, falsifiable, for a
  named audience. Not a mission statement.
- ARCHITECTURE's Invariants are the guarantee inventory: each
  never-event, the adversity it stands against, and the one wall that
  holds it. A guarantee whose wall is "the code is careful" is a defect.
- ADRs record refusals — what we deliberately do not own, features
  turned away — and any wall chosen weaker than the strongest available.
- PLAN cuts the work by invariant, not by feature: one slice per step,
  closed only by a test that creates the attack and shows the
  invariant surviving.

How the run is executed, by PLAN step — skills, each with its own
Stage 0 readiness check:

- Framing (Step 1) — `.claude/skills/cbc-framing/`
- Ground (Step 3) — `.claude/skills/infra-establish/`; a service added
  later — `.claude/skills/infra-serve/`
- Skeleton (Step 4) — `.claude/skills/cbc-bootstrap/`
- Slices (Steps 5..N-1) — `.claude/skills/cbc-slice/`

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
| The system's shape changed | Shape of the system | ARCHITECTURE.md |
| Something became true the outside should see | The front door: what this is, how to use it | README.md |
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
- Convention arrivals — `.claude/skills/convention-lifecycle/`
- Hygiene — `.gitignore` `.gitattributes` `.editorconfig` (repo-hygiene)
- Method — `concept/` (correctness-by-construction; not a rulebook,
  an ordering of questions)

## How to work here

<!-- The stance this project expects, where it is not the obvious one:
     "sessions here are design conversations, decide before building",
     "this is research code, prefer exploring over shipping", "ask
     before touching migrations". A few lines at most.

     Stance only — NOT rules. If a sentence would be true in another
     project, it is a convention and belongs in one. This slot exists
     because stance is the one thing that is genuinely different per
     project and has no other home; that is also why it is the easiest
     place to start rebuilding the rulebook. -->

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

<!-- Genuinely project-specific things an agent must know and could not
     infer: a directory that is generated, a service that must be
     running, a file nobody may edit by hand.

     NOT for anything general. If a rule would be true in another
     project, it belongs in a convention, not here. This section is
     where entry files go wrong — it grows, and every line added makes
     every other line matter less. -->

- Step 0 here is a trial of `birth-scenario.md`: it is the procedure,
  and every divergence from it is written into the devlog, not fixed
  silently.
- Nothing before the briefing names the problem.

<!-- SIZE BUDGET: this file is loaded in full, on every task, relevant
     or not. It is the only text that costs something even when it is
     useless. If it is longer than a screen, something in it belongs in
     a convention, a record, or a skill. Shrinking it is maintenance,
     not tidying. -->
