<!-- Draft — provisional, untested. Authored 2026-08-31 from the
     birth-scenario discussion (devlog of that date); it has never
     been walked. First walk: the next birth. Until a trial-closing
     ADR adopts it, README.md's Birth section remains the procedure
     of record — this draft changes only the order of introduction
     and who commits what, nothing about which files copy or where
     they land. -->

# Birth scenario — the introduction, in order

A birth is an introduction, not a file operation. The scenario
orders it — seed, walk, briefing — and ends where the problem
begins: everything before the briefing is problem-agnostic by
construction.

## Seed — mechanical, before the newborn's first session

Done from outside; the newborn cannot introduce its own boot.

1. Kit birth per the handbook's manual
   (engineering-handbook/starter/README.md), through its hygiene
   commit. By pointer — no step of that manual is restated here.
2. Copy the bundle per README.md's table, plus this scenario to the
   newborn's repo root, at one moment — one delivery, one pin. A
   scenario at the root makes a birth in flight visible from a
   clean clone, the change-plan convention's own argument. Nothing
   is committed; the walk commits it in order.
3. Merge cbc-startup-snippet.md into CLAUDE.md and delete the copy;
   append the bundle birth entry to .claude/decisions.md beside the
   kit's (README.md Birth steps 3–4, unchanged).

## Walk — the newborn's first session

The walk is how the kit's Step 0 gates are met — the step is the
interface, the scenario is the method, the same relation
cbc-framing has to the kit's Framing step. The newborn reads its
copy of this file first, then introduces each piece as its own
commit or commits, under the kit's agent/project split; read
top-down, the log is the introduction.

1. **Boot** — the arrangement: CLAUDE.md with its merged CbC
   section, .claude/, the five skills. Agent-scoped commits. Who
   runs this project.
2. **Concept** — concept/. A project commit. What the method is.
3. **Map** — playbooks/cbc-run.md and the plan opened. Where a run
   goes.
4. **Records** — the kit's records, per its own Step 0. Nothing
   CbC-specific.

Boundaries within a step are the newborn's Step 0 change-plan's
call; correctness stays the Birth section's checklist, verified
after Step 0 closes.

## Briefing — last, and outside

The briefing arrives only after Step 0 closes: the first prompt of
project work, walked per the playbook (Define, then Framing). The
scenario ends here — nothing above it may mention the problem.

## Trial protocol

This repo owns the trial, not the run. Each walk's divergences are
recorded in this repo's devlog at the birth; the draft is revised
after each walk. The trial closes with an ADR — adopt (the Birth
section rewritten around the scenario, the snippet question
decided) or kill (this file deleted, the why in the ADR).

Open, deliberately, deciding at trial close and not before:
whether the newborn's copy of this file is deleted when the walk
completes (the snippet's merge-then-delete precedent, the birth
entry citing the scenario) or kept; whether the scenario absorbs
the snippet's CLAUDE.md content, retiring cbc-startup-snippet.md.
