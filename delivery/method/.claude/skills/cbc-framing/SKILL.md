---
name: cbc-framing
description: Frame a new backend system with correctness-driven design. Turn a standing project idea into one Falsifiable Promise, a System Definition of five layers, and an Invariant Slice Registry, BEFORE any code or tech choices. Use this whenever the user wants to start, design, or plan a backend or service where being wrong is expensive, such as orders, payments, inventory, bookings, anything owning facts or money. Use it too when they mention framing, a promise, invariants, idempotency, "what must never happen", CbC, or correctness-driven design, even if they just say "I have an idea for a service" or "help me design a backend". Do NOT use for throwaway prototypes, experiments, or low-stakes tools. Do NOT use for implementing code: that is the cbc-slice Agent Skill, which runs only after CBC Framing AND the system's bootstrap.
foundation: concept v1
---

# CBC Framing — one Falsifiable Promise worked into an Invariant Slice Registry

Turn a standing project idea into three CBC Framing Exports:

- the CBC Framing Intent: the Falsifiable Promise;
- the System Definition: its five System Layers;
- the Invariant Slice Registry: the work, cut and ready.

Documents only: no code, no tech choices. They live in the CBC Run's
repo, born from Record Stubs. A CBC Framing may end in "no
project". That is a valid exit.

The full procedure is `.claude/skills/cbc-framing/references/cbc-framing-workflow.md`.
Read it before Stage 0 and keep it open. This file is the operating
rules, not a substitute.
`.claude/skills/cbc-framing/references/worked-example.md` shows a
complete CBC Framing of a tiny order service. Consult it whenever
unsure what an Agent Skill Stage's output looks like.
`.claude/skills/cbc-framing/references/the-whole-system-in-plain.md`
is the one-page orientation, if the reviewer or you need the whole
method reloaded first.

## The mode — non-negotiable

CBC Framing is **joint work**. You open each question and derive
visibly, and the reviewer works it with you. The hard rule, from the
method itself:

- **You never close an Agent Skill Stage, never call Enemy Census
  Saturation, never resolve a fork alone.** Every exit is the
  reviewer's verdict. Present your derivation, then ask for the
  call.
- A first-time CBC Framing may ask for **Demonstration Mode**: derive
  with reasoning fully visible, teaching the moves.
- **Every "outside" is written.** Rejected candidate Falsifiable Promises, System
  Refusals, facts out of scope: each is recorded, never silently
  dropped.

**Delegated-Verdict Mode.** A CBC Run may hand these verdicts to the
agent. It does so only through an explicit decision recorded in its
own Decisions Log, `.claude/decisions.md`. The decision names what is
delegated, why, and the cost accepted. The cost: the CBC Framing
Derivation becomes the only review, so its legibility is part of the
product. Every Agent Skill Stage's Exit is still presented, decided,
and recorded inline in the CBC Framing Derivation, as *The record*
says. Delegation changes who
calls the verdict, never whether it is written. Without that
recorded decision, the default above stands.

## The derivation order (not the presentation order)

```
Stage 0 choose the Falsifiable Promise  (CBC Framing Intent)   one claim, falsifiable, worth proving
Stage 1 what must be ours?              (LAYER-2-SYSTEM)       System Possession Test; System Refusals in writing
Stage 2 name the enemies                (LAYER-1-ENVIRONMENT)  Enemy Census: vanishes / duplicates / lies
Stage 3 run the Enemy Collisions        (LAYER-4-PROBLEMS)     Enemy Facts × System Possessions → Enemy Collision Kills
Stage 4 sort into owners                (LAYER-3-AREAS)        only if Enemy Collisions force Responsibility Areas
Stage 5 check between owners            (LAYER-5-INTERACTION)  only if owners exist; else empty-with-reasons
Stage 6 cut the Invariant Slice Registry                       Invariant Slices vs Invariant Slice Folds
```

Run them in this order. Each Agent Skill Stage consumes exactly the
previous one's output. An upward correction is made only as a CBC
Framing Export Revision. Example: an Enemy Census finding that shows
a missed System Possession becomes a CBC Framing Export Revision of
LAYER-2-SYSTEM. A scheduled re-read is never one.

## Each Agent Skill Stage's Exit

Check these before asking the reviewer to close an Agent Skill Stage.

- **Stage 0:** exactly one Falsifiable Promise, one sentence,
  falsifiable: the scenario that breaks it can be described
  concretely. The **Falsifiable Promise Audience** is named: who the
  Falsifiable Promise is made to. Those who only use the system belong in the
  Enemy Census. What done demonstrably means is stated. A second real
  purpose means the CBC Framing Intent is overloaded: force the
  choice. Record the rejected candidates.
- **Stage 1:** every System Possession passes the **System Possession
  Test**: if someone else owned this, could they break the
  Falsifiable Promise? Every System Refusal, a fact or responsibility the system
  deliberately does not own, is written with the **System Refusal Test**: can the Falsifiable Promise stay true if
  this goes wrong elsewhere? Yes means refused. **Enemy Sketches**,
  rough enemies, are fine here. Stage 2 replaces them with Enemy
  Facts.
- **Stage 2:** Enemy Facts only, concrete enough to attack with
  ("responses get lost", never "networks are unreliable"),
  consequence first. **An Enemy Census is not a list of
  assumptions.** List what can hurt, never what you trust. The
  workflow allows two labelled blocks beside the Enemy Facts:
  - the Trust Assumptions, accepted deliberately and kept short.
    They answer who besides the system can write what it stores,
    whether that writer is trusted or defended;
  - the Runtime Ground, with the size the system is built for.

  Exit only by Enemy Census Saturation: two Enemy Census Probes in a
  row find no new Enemy Fact. The Enemy Census Probe Log is
  recorded in LAYER-1-ENVIRONMENT.
- **Stage 3:** each Enemy Collision Kill states **what dies, never
  how it is saved.** Set any mechanism aside the moment it comes up.
  Write each Enemy Collision Kill shaped as an invariant, its
  adversity named, so the cbc-slice Agent Skill can take it with no
  translation. A CBC Framing Concern with no enemy, shaped as a
  contract, becomes an Invariant Slice Fold Candidate, not an
  Invariant Slice.
- **Stage 4:** a division is real only with separate state AND
  separate decision authority. One Responsibility Area is a
  *confirmed* answer, not a gap. Name the Responsibility Area Seams
  that fail the test, and refuse to draw them.
- **Stage 5:** empty is fine, but empty **with its reasons**, each
  traced to an earlier decision.
- **Stage 6:** two Enemy Collision Kills are two Invariant Slices
  only if their evidence must create *different adversity*. That is
  the Invariant Slice Split Test. An Invariant Slice Fold goes into
  the Correctness Specification of the Invariant Slice that consumes
  it. The Invariant Slice Registry carries the CBC Framing
  Reconciliation: every CBC Framing Concern accounted for as
  Invariant Slices and Invariant Slice Folds, nothing silently
  dropped. It also carries one `chosen-next` Invariant Slice. The
  order is an expectation, decided again at each Invariant Slice
  Close.

## The record — the CBC Framing Exports, and one CBC Framing Derivation

**The CBC Run Briefing comes first.** CBC Framing opens by committing
it, unchanged, at `docs/system/framing/briefing.md`: the problem as
brought, in its own words. Anything private is removed before that
commit, and the file's first line says what was removed. After it,
the CBC Run Briefing is history, never edited. So a claim like "no
divergence from the CBC Run Briefing" can be checked against it.

**The glossary is already there.** `docs/glossary.md`, born with the
CBC Run, holds this project's own Glossary Names. The Names the
delivered files are written in arrive in `docs/glossary/`. Each thing
CBC Framing defines, and each tag kind, gets its Glossary Name in
`docs/glossary.md`, in one plain sentence, when CBC Framing first
uses it. Every later record adds to it.

**Each Agent Skill Stage's result is written once, straight into its
CBC Framing Export,** when the reviewer gives the verdict: the CBC
Framing Intent at Stage 0, the System Definition's layer at Stages 1
to 5, the Invariant Slice Registry at Stage 6. The CBC Framing Export
is the result's only home. It carries a draft line at its top until
CBC Framing's close. Example, in the System Definition: "FACT-CALLER-5. A
caller reuses an idempotency key with a different order body → a
lie: 'this is a repeat' when it isn't."

**The CBC Framing Derivation keeps how each Agent Skill Stage ran.**
It is `docs/system/framing/derivation.md`, beside the CBC Framing
Exports it leads to, kept as the archive forever, never deleted. It
links to each result and never restates it. Three rules:

1. **One section per Agent Skill Stage:** what was considered, the
   Enemy Census Probes, the dead ends, the reviewer's questions, and
   the verdict, written inline where it happens. Then a link to where
   the result lives. Example: "Stage 2. Considered 'a caller resends
   a key with only the quantity changed'; merged into FACT-CALLER-5.
   Asked: is a changed quantity the same fact as a changed delivery
   address? Yes: both are a different body under a reused key.
   Verdict: accepted. Results: System Definition,
   LAYER-1-ENVIRONMENT."
2. **A section freezes at its verdict.** It is append-only after
   that. A CBC Framing Export Revision changes the CBC Framing
   Export, and adds one line here: what changed, and why.
3. **The one exception:** a bulky mechanical sweep may live in a
   **CBC Framing Derivation Appendix**, a file beside it in the same
   directory, plainly named (`collision-grid.md`, say). The file
   carries sweep output only, never decisions. The CBC Framing
   Derivation stays the single record of how the CBC Framing ran.

Where each kind of record lives:

- CBC Framing's verdicts: inline in the CBC Framing Derivation;
- a delegation arrangement: the CBC Run's Decisions Log, since it is
  agent setup, not project truth;
- the CBC Framing's adoption: one ADR in the CBC Run's `docs/adr/`,
  at CBC Framing's close.

## The CBC Framing Exports

The three CBC Framing Exports live under `docs/system/`, the
internal truth at one path:

- `intent.md`: the Falsifiable Promise, and the candidates rejected;
- `definition.md`: the five System Layers, each filled or empty with
  reasons;
- `registry.md`: the Invariant Slices, the Invariant Slice Folds, the
  CBC Framing Reconciliation and the `chosen-next` Invariant Slice.

At CBC Framing's close, **check that each CBC Framing Export reads alone**, then
remove its draft line. Nothing is composed or copied. A result copied
from one file to another drifts, and a rewording can turn true into
false.

The **CBC Framing Export Filter** holds throughout: a CBC Framing
Export never refers to the CBC Framing Derivation's machinery. Its
conclusions stand on the CBC Framing Exports themselves. The same
filter refuses **Agent Language**: nothing in a CBC Framing Export
names this Agent Skill, an Agent Skill Stage, or the CBC Run's
arrangement. A reader without the Agent Skills directory must not
need it to read them.

**The CBC Framing Exports are living records, not written once.** The
Invariant Slice Registry already lives: its statuses change at every
Invariant Slice Close. The other two stay true the same way. Later
work may change what a CBC Framing Export claims. A gap the CBC
Framing Intent named may close, or a later Agent Skill Stage may find
facts the System Definition must carry. Then the CBC Framing Export
is updated **only through a CBC Framing Export Revision**: dated,
saying what changed, why, and what set it off. It is the same rule
as during CBC Framing, kept after its close.

## The commit order

By default, **commit in derivation order:**

1. the CBC Framing Intent;
2. the System Definition, growing LAYER-2-SYSTEM → LAYER-1-ENVIRONMENT
   → LAYER-4-PROBLEMS → LAYER-3-AREAS → LAYER-5-INTERACTION, each
   Agent Skill Stage's result committed at its verdict;
3. the Invariant Slice Registry;
4. the adoption record;
5. the README, last, since it derives from what is committed.

So the CBC Run's own history tells the derivation story. The order
is the commits', not the file's. Each layer's commit places its
section where the workflow presents it, so the System Definition ends
LAYER-1-ENVIRONMENT to LAYER-5-INTERACTION, from the outside in, and
no reorder is needed after. Skipping the order departs from the
default: log why in the Decisions Log.

## The Invariant Slice Registry's outcomes

What the file must carry, whatever its layout:

1. every Invariant Slice Entry states its invariant, the adversity
   its evidence must *create*, its owning Responsibility Area, the
   Enemy Collision Kills it covers, and what it presumes already
   stands;
2. its statuses are trustworthy:
   `open · chosen-next · in-progress · closed (date, evidence)`;
3. an Evidence Precondition, a condition the Invariant Slice checks
   but never attacks, and an Adversity Flag, an adversity that
   cannot be created the normal way, sit on the Invariant Slice Entry they concern;
4. any grouping is headings for the reader, never a boundary;
5. the CBC Framing Reconciliation accounts for every Enemy Collision
   Kill, and states even its absences, the written zero;
6. exactly one Invariant Slice is `chosen-next` while open work
   remains.

The default layout is the Agent Skill Template
`.claude/skills/cbc-framing/templates/registry.md`. Declining it is
off-template: derive your own layout from the outcomes above. How it
is used is the delivered-copies Agent Rule's (`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill Template is…*).

## The README

The CBC Run's README is **derived from the three CBC Framing Exports, never written
on its own.** Every claim on it has its home in `docs/system/`. A
fact the reader needs that lives only in the CBC Framing Derivation
marks a gap in the CBC Framing Exports. Fix the CBC Framing Export
first, then derive the README again. A README patched on its own is
a second home, and two homes diverge. What each piece derives from:

| From | Becomes | How much |
|---|---|---|
| the CBC Framing Intent | why this exists | one paragraph |
| the System Definition's System Possessions and System Refusals | what this is | one paragraph, no parts named |
| the Invariant Slice Registry | the planned invariants | one line per invariant |
| the method | a note that points at the method | two lines, never a restatement |
| the repo's observable state | a status line that says what the repo does now | one line |

Depth is a link into the CBC Framing Exports, never more prose. At
the CBC Framing close, the thin README is the whole public page. With
each home linked, a restatement in the README fails: the reader reads
the home instead. A CBC Run whose conditions differ may argue against
this, departing from the default, logged in the Decisions Log. The README is refreshed at
milestones: an Invariant Slice Close moves the status line. The CBC
Framing Export Filter applies with full force: the README tells what
the system is and guarantees, never how the work ran.

## The handoff

At CBC Framing's close, say this to the reviewer plainly: **the handoff is to the
Runtime Ground and the skeleton, not to Invariant Slices.** Between
CBC Framing and the first Invariant Slice sits real project work:

- the Runtime Ground the system runs on, its store among it;
- then the skeleton and its Adversity Harness.

System Readiness defines what must stand
(`.claude/skills/cbc-slice/references/system-readiness.md`). Invariant
Slice work begins only when the reviewer signs off System Readiness.
The cbc-slice Agent Skill will check.

---

## Decisions

- ADR-0008 — *The Invariant Slice Registry's outcomes*: the Invariant Slice Registry's
  default layout is an Agent Skill Template, copied and filled
