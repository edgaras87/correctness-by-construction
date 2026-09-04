<!-- Draft — provisional, walked once. Authored 2026-08-31 from the
     birth-scenario discussion (devlog of that date). Until a
     trial-closing ADR adopts it, the install manual
     (starter/installs/cbc.md) remains the procedure of record.
     2026-09-02: reordered around derivation (ADR-0012) — the walk
     opened on the concept and the newborn wrote its own CLAUDE.md
     section; the snippet withdrawn, held blind at docs/baselines/.
     2026-09-03: after the first walk (cbc-newborn) — rewritten as
     assembly, in the newborn's copy. The walk showed the
     derivation needs the whole bundle in view and the concept
     read first, nothing more; the staged introduction lived only
     in the commit log. So the CLAUDE.md section is written once,
     in this repo, from the whole bundle, and ships as text; every
     birth-time fill is problem-agnostic and so a template; the
     bundle lands under docs/, only the chosen playbook copies. No
     per-birth derivation, no change-plan, no ladder.
     2026-09-04: carried back to this master from the newborn's
     revision (cbc-newborn 3b27b46 + 260a39e), the trial
     protocol's post-walk revision step. -->

# Birth scenario — assembly

A birth is assembly. Everything before the briefing is
problem-agnostic, so everything before the briefing is a copy, a
template fill, or a commit of those — deterministic from two pins,
the kit's and the bundle's. The newborn's first act of judgment is
the briefing. The scenario ends where the problem begins.

## Seed — mechanical, from outside

1. Kit birth per the handbook's pure install manual
   (engineering-handbook/starter/installs/pure.md, their
   ADR-0028), through its hygiene commit. By pointer — no step of
   that manual is restated here.
2. Copy the bundle per the starter README's table, under docs/:
   the concept at docs/concept/, the run's playbook alone at
   docs/playbooks/cbc-run.md, this scenario at
   docs/birth-scenario.md. One moment, one delivery, one pin.
3. Copy the CbC skills to .claude/skills/. Merge the bundle's
   CLAUDE.md text — the CbC section, the Method row, the stance
   and local-rule lines — into the kit's CLAUDE.md stub. Shipped
   text, merged once from the first walk's evidence; not derived
   per birth.
4. Map the playbook into PLAN: its steps replace the stub's STEPS
   region, "Steps from:" filled.
5. Fill the stubs from the bundle's birth fills: README's
   problem-agnostic purpose paragraph and method line, PLAN's
   title, ADR-0001's date, ARCHITECTURE's "nothing built"
   overview, CHANGELOG's versioning deferral, TODO's deferrals and
   the one known issue, the devlog's birth entry. Variables: the
   working name, the date, the two pins.
6. Append the bundle birth entry to .claude/decisions.md beside
   the kit's.

Nothing is committed by the seed on the newborn's main line — that
log stays the newborn's own. The seed does commit, on its own
branch: a receipt branch (`birth-seed`, cut from the hygiene
commit, never merged, deletable anytime) with one commit per seed
step, recording what each step brought, so kit and bundle delivery
can be checked against the pins before the newborn's first
session. The first walk's receipt (cbc-newborn `birth-seed`) has
five commits for the five steps of the scenario as it then stood;
under this revision the receipt is six, with the CLAUDE.md merge
and the stub fills among the things it records.

## Commits — the newborn's first session, or the same script

Three, under the kit's agent/project split. Reviewed as any change
set is; no change-plan, the split is fixed here.

1. `chore(agent): install the arrangement` — CLAUDE.md, every
   skill (kit and CbC), .claude/decisions.md.
2. `docs: add the CbC bundle and the records at birth` — the
   concept, the playbook, this scenario, every stub filled.
3. `docs: close Step 0 in PLAN` — gates ticked on verified facts;
   the briefing gate left blocked, unblocked by the briefing
   prompt.

Read top-down: the actor, its material, the door closed behind it.

## Briefing — last, and outside

The briefing arrives only after Step 0 closes: the first prompt of
project work, walked per the playbook (Framing, then Define). The
scenario ends here — nothing above it may mention the problem.

## Trial protocol

This repo owns the trial, not the run. Each walk's divergences are
recorded in this repo's devlog at the birth; the draft is revised
after each walk — this text is the first such revision, authored
in the first newborn and carried back.

What the first walk settled, and what remains:

- The bundle's CLAUDE.md text has two candidates: the section the
  first newborn derived (cbc-newborn 8f167c4) and the held
  baseline (docs/baselines/cbc-startup-snippet.md). Read against
  each other once, merged, frozen into the bundle. That closes
  ADR-0012: the comparison was a review of the concept's clarity,
  not a birth step, and it does not repeat.
- The seed and the three commits are one script from two pins. The
  trial's closing ADR adopts this scenario by rewriting the
  install manual around it and writing that script — after which
  this file is not copied into newborns; the manual is the
  procedure and the script is the proof. Until then this file
  ships and the newborn's copy is the procedure its Step 0 trials.
- The kit's Step 0 comment ("take the briefing", "draft
  CHANGE-PLAN.md", "plan open first") disagrees with this shape on
  all three points. A finding for the handbook, not fixed in a
  pinned copy.
