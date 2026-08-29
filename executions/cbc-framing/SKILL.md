---
name: cbc-framing
description: Frame a new backend system with correctness-driven design - turn a raw project idea into one falsifiable promise, a layered system definition (L1-L5), and a registry of provable slices, BEFORE any code or tech choices. Use this whenever the user wants to start, design, or plan a backend/service where being wrong is expensive (orders, payments, inventory, bookings, anything owning facts or money), mentions framing, a promise, invariants, idempotency, "what must never happen", CbC, or correctness-driven design - even if they just say "I have an idea for a service" or "help me design a backend". Do NOT use for throwaway prototypes, experiments, or low-stakes tools, and do not use for implementing code (that is cbc-slice, which runs only after framing AND bootstrap).
---

<!-- Derives from concept v1 of correctness-by-construction
     (ADR-0003). Provenance — archive/cbc/system-design-method
     birth-materials/.claude/skills/cbc-framing/SKILL.md
     @ fe0075d (imported 2026-08-28, PLAN Step 3). Changes on
     import: none — verbatim below this header.
     Harvested 2026-08-29: the registry export's lived format from
     checkout-system's nine-slice run, read read-only (ADR-0007) —
     outcomes stated in the export section, copy-and-fill master in
     templates/slices.registry.md (ADR-0008). -->

# CbC framing — one promise worked into a slice surface

Turn a standing project idea into three artifacts: **intent** (the promise),
**system definition** (L1–L5), **slice registry** (the work, cut and ready).
All paper — no code, no tech choices, no repo. A framing may honestly end in
"no project"; that is a valid exit.

The full procedure is `references/cbc-framing-workflow.md` — read it before
step 0 and keep it open; this file is the operating rules, not a substitute.
`references/worked-example.md` shows a complete framing of a tiny order
service — consult it whenever unsure what a step's output looks like.
`references/the-whole-system-in-plain.md` is the one-page orientation if the
user (or you) needs the whole method reloaded first.

## The mode — non-negotiable

Framing is **joint work**. You open each question and derive visibly; the
human works it with you. The hard rule, from the method itself:

- **You never close a step, never call saturation, never resolve a fork
  alone.** Every exit is the human's verdict. Present your derivation, then
  ask for the call.
- A first-time walker may ask for **demonstration mode** — derive with
  reasoning fully visible, teaching the moves. Even then, every verdict
  stays human.
- **Every "outside" is written.** Rejected candidate promises, refused
  responsibilities, out-of-scope facts — recorded, never silently dropped.
  Silence is the only forbidden channel.

## The derivation order (not the presentation order)

```
step 0  choose the promise      (intent)  one claim, falsifiable, worth proving
step 1  what must be ours?      (L2)      hostage test; refusals in writing
step 2  name the enemies        (L1)      census: vanishes / duplicates / lies
step 3  run the collisions      (L4)      facts × possessions → kills
step 4  sort into owners        (L3)      only if collisions force divisions
step 5  check between owners    (L5)      only if owners exist; else empty-with-reasons
step 6  cut the slice surface             slices vs folds; registry
```

Run them in this order — each step consumes exactly the previous step's
output. Upward corrections only as logged return trips (a census finding
that reveals a missed possession → logged L2 revision), never scheduled
polish passes.

## Per-step gates (check before asking the human to close a step)

- **Step 0:** exactly one promise, one sentence, falsifiable — the breaking
  scenario can be described concretely. A second real purpose means the
  intent is overloaded: force the choice. Bank rejected candidates.
- **Step 1:** every possession earned by the hostage test ("if someone else
  owned this, could they break the promise?"); every refusal written with
  the mirror test. Sketch-enemies are fine here — they are debt step 2 pays.
- **Step 2:** facts only, concrete enough to attack with ("responses get
  lost", never "networks are unreliable"), consequence-first. **A census is
  not an assumption inventory** — list what can hurt, never what you trust.
  Exit only by saturation: two consecutive fresh probes finding nothing new.
- **Step 3:** each kill states **what dies, never how it's saved** — park
  any mechanism the instant it surfaces. Land kills invariant-shaped with
  adversity named, consumable by the slice workflow with zero translation.
  Enemy-less contract-shaped concerns → fold-candidates, not slices.
- **Step 4:** a division is real only with separate state AND separate
  decision authority. One area is a *confirmed* answer, not a gap. Name
  seams that fail the bar; refuse to draw them.
- **Step 5:** empty is fine — but empty **with its reasons**, each traced to
  a prior decision.
- **Step 6:** two kills are two slices only if their evidence must create
  *different adversity*. Folds ride into the spec of the slice consuming
  them. The registry carries the fold-reconciliation line (concerns ↔
  slices + folds — nothing silently dropped) and a chosen-next slice.
  Ordering is an expectation, re-decided at each slice close.

## Export and handoff

At close, write the three artifacts into the project repo:

- `project.intent.md` — the promise + banked rejections
- `system.definition.md` — L1–L5, filled or empty-with-reasons
- `slices.registry.md` — slices + folds + reconciliation line + chosen-next

**The registry's outcomes** (what the file must carry, whatever its
shape): every slice entry states its invariant, the adversity its
evidence must *create*, its owning area, the kills it covers, and
what it presumes already stands; statuses are trustworthy
(`open · chosen-next · in-progress · closed (date, evidence)`);
the reconciliation line accounts for every kill; exactly one slice
is chosen-next while open work remains. The default shape is the
copy-and-fill master `templates/slices.registry.md` beside this
skill's references (ADR-0008). Declining it is **off-template**:
derive your own shape from the outcomes above and record the
deviation in the run's log.

Then say this explicitly to the user: **the handoff is to bootstrap, not to
slicing.** Between framing and the first slice sits real project work —
repo skeleton, store, adversity harness — defined by the readiness
checklist (`system-readiness.md`, bundled with the cbc-slice skill). Slicing
begins only when the human signs off readiness; the cbc-slice skill will
check.
