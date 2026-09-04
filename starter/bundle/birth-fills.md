<!-- Derives from concept v1 of correctness-by-construction
     (ADR-0003). Provenance — the first walked birth's stub fills
     (cbc-newborn e7a13f9, devlog entry 4def0b5), generalized
     2026-09-04 (ADR-0014): every fill was problem-agnostic, so
     every fill is a template. Variables, filled by the seed:
     <working-name>, <date>, <kit-pin>, <bundle-pin>.
     The records-carry-the-method mapping is distributed here,
     each rule riding in the record it governs (ADR-0014): the
     README fill carries the promise rule, the ARCHITECTURE fill
     the guarantee inventory, the ADR-0001 fill the refusals
     rule. PLAN's reading needs no fill — the playbook mapped
     into it is already cut as invariant slices (cbc-run.md,
     Steps 5..N-1).

     Use: assembly step 5 (starter/bundle/birth-scenario.md)
     applies each fragment to the stub its marker names — a fill
     replaces the stub's fill-comment or placeholder at the spot
     the marker describes; the stub's other text stays. Step 6
     appends the decisions entry. -->

# Birth fills — the bundle's templates for the kit stubs

<!-- fragment: readme-fill — replaces the README stub's title and
     purpose fill-comment. -->

# <working-name>

A backend service built by correctness-by-construction: one
falsifiable promise, derived down to the structures that make
breaking it impossible. The problem is not chosen yet — until the
briefing brings it, this repo is method and records, ready to
start, and the name is a working name.

<!-- When the briefing lands, this paragraph becomes the promise:
     one sentence, falsifiable, for a named audience — not a
     mission statement. That is the method's reading of this
     record. Birth provenance lives in .claude/decisions.md, step
     status in PLAN — never here: this is the front door. -->

The method: `docs/concept/`, starting with `00-cbc.md`.

<!-- /fragment -->

<!-- fragment: plan-title — the PLAN stub's title line. -->

# Plan: <working-name>

<!-- /fragment -->

<!-- fragment: adr-0001-fill — the date line replaces the stub's
     placeholder; the comment is appended at the end of the
     stub's Decision section. -->

Date: <date>

<!-- Under this project's method, ADRs also record refusals —
     features turned away, capabilities deliberately not owned —
     and any wall chosen weaker than the strongest available.
     That is the method's reading of this record. -->

<!-- /fragment -->

<!-- fragment: architecture-overview — replaces the ARCHITECTURE
     stub's Overview fill-comment. -->

Nothing is built. This file becomes true at Bootstrap (PLAN Step 4),
when a skeleton exists wired to its ground; the diagram, Components
and Codemap below are deferred to that step and keep the stub's form
until then. Invariants fills per slice close, as the guarantee
inventory: each never-event, the adversity against it, the wall that
holds it.

<!-- /fragment -->

<!-- fragment: changelog-versioning — replaces the CHANGELOG
     stub's versioning placeholder. -->

Versioning: deferred to Framing (PLAN Step 1) — what a version is
here depends on what the system turns out to be.

<!-- /fragment -->

<!-- fragment: todo-fill — the items for the TODO stub's four
     sections; each replaces the stub's empty placeholder in its
     section. -->

## Now (current plan step)

- [ ] Take the briefing: README purpose paragraph, devlog Briefing
      line — the Step 0 gate item left blocked, first prompt of Step 1.

## Next (upcoming steps — assign each to a step when triaged)

- [ ] Step 1 Framing: decide what a version is (CHANGELOG header).
- [ ] Step 2 Define: project name, repo name, repo description —
      "<working-name>" is a working name.
- [ ] Step 4 Bootstrap: ARCHITECTURE overview, diagram, Components,
      Codemap; stack overlay below the hygiene files' marker.

## Later / someday

- [ ] After the birth: keep or delete docs/birth-scenario.md — the
      trial's closing ADR (in the repo that owns the trial) decides.

## Known issues

- Step 0 closes with its briefing gate blocked. Accepted because the
  birth scenario places the briefing after Step 0 closes and forbids
  naming the problem before it. Revisit at the trial's closing ADR.

<!-- /fragment -->

<!-- fragment: devlog-birth-entry — the devlog's first entry. -->

## <date>  (Step 0: bootstrap)

- Project started. Repo initialized from the starter kit
  @ <kit-pin>, CbC bundle overlaid @ <bundle-pin> (both entries in
  .claude/decisions.md), assembled per docs/birth-scenario.md (in
  trial): seed from outside, three commits, this entry among them.
- Briefing: not yet. The scenario places it after Step 0 closes, so
  nothing here names the problem; README's purpose paragraph says so.
- Divergences from the scenario, if any, are recorded here for the
  trial — never fixed silently.
- Resume: the briefing.

<!-- /fragment -->

<!-- fragment: decisions-bundle-entry — appended to
     .claude/decisions.md beside the kit's birth entry (assembly
     step 6). -->

- <date> CbC bundle overlaid from correctness-by-construction
  @ <bundle-pin>, pinned to concept v1.
  Why: born to walk the CbC method — the bundle's birth scenario
  (in trial) drives Step 0.
  Rejected: none — see the concept repo's ADRs.

<!-- /fragment -->
