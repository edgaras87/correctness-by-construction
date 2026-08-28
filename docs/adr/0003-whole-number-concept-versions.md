# 0003. Whole-number concept versions, logged in CHANGELOG

Date: 2026-08-28
Status: Accepted

## Context

Everything downstream pins to a concept version: executions state
which version they derive from, run repos take execution copies
pinned to one, and a harvest closes by re-deriving against a new one.
So a version must be decided before the first execution lands (Step
3): what a version names, where it is declared, and how it is cited.
The briefing already speaks of "concept v1" without defining it.

## Options considered

1. SemVer over the concept — the kit CHANGELOG stub's default. Its
   major/minor/patch semantics encode API compatibility; prose has
   no such interface, so the three numbers would be false precision
   nobody can assign consistently.
2. Per-chapter versions — finer pins, but executions derive from the
   concept as a unit, not from a chapter; chapter granularity has no
   consumer and multiplies pinning bookkeeping.
3. Git commits as versions — free and exact, but unreadable as a
   citation and indiscriminate: every typo fix is a new "version",
   so a pin cannot say whether re-derivation is needed.
4. Whole-number versions (v1, v2, …) over the mental layer as a
   whole, logged in CHANGELOG — chosen.

## Decision

A concept version is a whole number naming a state of the mental
layer as a whole (everything under `concept/`). CHANGELOG.md is the
concept-version log and the sole place versions are declared: each
released entry is one version — what changed in the concept and why,
with run provenance when the change was harvested, and which
executions were reviewed or re-derived. Executions cite the version
in their provenance headers ("derives from concept v1").

The bump rule: a change bumps the version when it could invalidate a
derived execution — a change of substance. Editorial fixes that
could not invalidate anything accumulate under [Unreleased] and ride
with the next substantive version; nothing pins to them.

v1 is the five chapters as imported at Step 2, unchanged in
substance from the archive statement
(birth-materials/concept/ @ fe0075d).

## Consequences

Good: a citation is one readable token; a pin's staleness is
answerable by reading the entries between two numbers; the version
log and the user-facing changelog are the same file because here
they are the same thing — this repo's users are the pinners.
Bad: "could invalidate a derived execution" is a judgment, not a
mechanical test — accepted; the judgment is recorded per entry, and
a wrong call is visible in the entry that made it.
