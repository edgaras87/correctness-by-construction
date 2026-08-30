# 0009. CbC delivered as an overlay on the handbook kit

Date: 2026-08-30
Status: Accepted

## Context

The bundle doc (ADR-0004) says what a run repo copies from here at
birth, but not how that copy composes with the other birth: run
repos start from the handbook's starter kit
(`engineering-handbook/starter/kit/`), which supplies the container
— records, PLAN skeleton, hygiene, CLAUDE.md. Two deliveries, one
run repo; the composition was undecided, and with it the question
of what happens here when the handbook updates its kit.

## Options considered

1. Keep a pre-baked CbC stub in this repo — the kit's files with
   the CbC material already merged, one copy at birth. Rejected:
   every kit file in it becomes a second master of the handbook's
   copy, and two masters diverge — the projection law this repo
   harvested (2026-08-30) applied to the kit. Every handbook update
   would need mirroring here, a standing sync burden with no
   mechanism; drift would be invisible until a run is born stale.
2. Deliver the plan shape as edit instructions — prose telling the
   born agent how to rewrite the kit's PLAN.md into CbC steps.
   Rejected: the kit already has a native slot for a reusable step
   sequence, `playbooks/` ("middle steps copied from a playbook
   where one fits"); instructions that reproduce a mechanism the
   kit carries are the same second-master problem at smaller scale.
3. Overlay: kit first, bundle second, plan authored from a playbook
   shipped here — chosen.

## Decision

A run repo is born in two copies. The kit from the handbook
supplies the container; then this repo's bundle is copied onto it
per the bundle doc's table, the startup snippet is merged into the
kit's CLAUDE.md, and the run's PLAN is authored from a cbc-run
playbook that ships with the bundle. The bundle doc carries the
birth manual — the numbered sequence and the mapping.

The overlay is additive by construction: it touches one kit file
(CLAUDE.md, by append) and otherwise adds files in paths the kit
does not claim. The kit surface it assumes is named in the birth
manual — a CLAUDE.md to append to, a `playbooks/` directory, the
plan step/gate idiom — and anything not on that list the overlay
must not depend on.

Record layering follows the same line: the kit owns the record
system, CbC owns method content. CbC events are recorded as
ordinary project events under the kit's rules; the method's own
artifacts (`docs/system/`, the framing derivation) live beside the
records, not in place of them. The bundle ships no recording
conventions — that stays deliberately absent (bundle doc).

## Consequences

Good: one master per fact — the handbook keeps the kit, this repo
keeps the method; a kit update costs nothing here and cannot break
existing runs, since both copies pin at birth (the ADR-0002
discipline at run scope); if a kit change breaks the named surface,
it surfaces loudly at the next birth, with a human present, and the
fix is one file.
Bad: birth is two copy operations plus a merge instead of one copy
— accepted, a birth is deliberate work anyway (ADR-0004 took the
same trade). The playbook's shape tracks the kit's plan convention,
so a kit reshape there means re-deriving one file here — the named
surface makes that check a list lookup, not archaeology.
