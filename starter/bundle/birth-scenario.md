<!-- Draft — provisional, untested. Authored 2026-08-31 from the
     birth-scenario discussion (devlog of that date); it has never
     been walked. First walk: the next birth. Until a trial-closing
     ADR adopts it, the install manual (starter/installs/cbc.md)
     remains the procedure of record — this draft changes only the
     order of introduction
     and who commits what, nothing about which files copy or where
     they land.
     2026-09-02: reordered around derivation (ADR-0012) — the walk
     now opens on concept/ and the newborn writes its own
     arrangement; the snippet merge is gone from the seed (the
     snippet is withdrawn, held blind at docs/baselines/); the
     playbook-into-PLAN copy placed, provisionally, in the Map
     step; the manual-step pointer fixed after two renumberings. -->

# Birth scenario — the introduction, in order

A birth is an introduction, not a file operation. The scenario
orders it — seed, walk, briefing — and ends where the problem
begins: everything before the briefing is problem-agnostic by
construction.

## Seed — mechanical, before the newborn's first session

Done from outside; the newborn cannot introduce its own boot.

1. Kit birth per the handbook's pure install manual
   (engineering-handbook/starter/installs/pure.md, their
   ADR-0028), through its hygiene commit. By pointer — no step of
   that manual is restated here.
2. Copy the bundle per the starter README's table — this scenario
   is in it, landing at the newborn's repo root, where a birth in
   flight is visible from a clean clone (the change-plan
   convention's own argument). One moment, one delivery, one pin.
   Nothing is committed; the walk commits it in order.
3. Append the bundle birth entry to .claude/decisions.md beside the
   kit's (install manual step 4, unchanged). Nothing is merged into
   CLAUDE.md — the newborn writes its own section in the walk
   (ADR-0012).

## Walk — the newborn's first session

The walk is how the kit's Step 0 gates are met — the step is the
interface, the scenario is the method, the same relation
cbc-framing has to the kit's Framing step. The newborn reads its
copy of this file first, then introduces each piece as its own
commit or commits, under the kit's agent/project split; read
top-down, the log is the introduction. The order below is the
draft's proposal — the first walk tests it.

1. **Concept** — read `concept/` whole (00-cbc.md first), then
   commit it. A project commit. What the method is; everything the
   newborn writes after this step is derived from it.
2. **Derive** — the newborn's own words, from the concept just
   read: CLAUDE.md's CbC section, the README purpose draft, the
   stub fills. No text is supplied — deriving this is the
   experiment (ADR-0012), and the derived section is compared
   against the held baseline at the trial's close, never shown to
   the newborn before. Kit split holds: CLAUDE.md is agent-scoped,
   the records are project commits.
3. **Map** — playbooks/cbc-run.md committed, its sequence replacing
   PLAN's STEPS region (the install manual's sed, step 3; "Steps
   from:" line filled). Where a run goes. Placed here, not in the
   seed, so the map's arrival is a read introduction, not a silent
   fact — provisional, the first walk decides.
4. **Skills** — the five skills, one by one or grouped (the
   newborn's Step 0 change-plan's call). Agent-scoped commits. How
   the method is executed.
5. **Records** — whatever of the kit's own Step 0 remains, per its
   rules. Nothing CbC-specific.

Boundaries within a step are the newborn's Step 0 change-plan's
call; correctness stays the install manual's checklist, verified
after Step 0 closes.

## Briefing — last, and outside

The briefing arrives only after Step 0 closes: the first prompt of
project work, walked per the playbook (Define, then Framing). The
scenario ends here — nothing above it may mention the problem.

## Trial protocol

This repo owns the trial, not the run. Each walk's divergences are
recorded in this repo's devlog at the birth; the draft is revised
after each walk. The trial closes with an ADR — adopt (the install
manual rewritten around the scenario) or kill (this file deleted,
the why in the ADR) — which also settles, on the walk's evidence:

- The snippet comparison (ADR-0012): the derived CLAUDE.md section
  read against docs/baselines/cbc-startup-snippet.md — the
  baseline stays, retires, or the two merge, each side kept where
  it won.
- The walk order above, and the Map placement (walk step vs seed
  mechanics).
- Whether the newborn's copy of this file is deleted when the walk
  completes or kept.
- How much of the seed becomes a rebuild script — it is
  deterministic from two pins, so a script that replays it fresh
  from the masters carries no staleness; whether the walk's
  commits also belong to a script, or to the newborn, is exactly
  what the walk shows.
