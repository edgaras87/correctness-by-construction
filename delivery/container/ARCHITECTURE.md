# Architecture

<!-- Describes the system AS IT IS NOW — not the aspiration. 1–2 pages max.
     Update trigger: a Plan Step's gate closes and this no longer matches
     reality. For the WHY behind any shape, link the ADR. By rule, not
     by slice: a slice's close adds or changes rows in Invariants, never
     a paragraph; how the slice got there is its record's.
     Why the form is as it is: (CBC docs/conventions/project-recording/
     §8.4, How the map is written).
     foundation: the project-recording convention -->

## Overview

<!-- One paragraph: what kind of system this is, in one breath.
     Fill-comment: the paragraph replaces this comment. -->

```
┌──────────┐      ┌──────────┐      ┌──────────┐
│  <comp>  │ ───▶ │  <comp>  │ ───▶ │  <comp>  │
└──────────┘      └──────────┘      └──────────┘
```

## Components

### <component>

Responsibility: <one sentence — what it owns, what nothing else may do>.
A slice may rely on: <what stands now, one line each>.
Why shaped this way: ADR-000N.

## Invariants

<!-- One row per invariant the system keeps: where the arithmetic or the
     decision is made, what refuses a wrong result, the test that goes
     red if either went, and the slice that proved it, linked. A "—"
     says a column holds nothing, on purpose. Example, from an order
     service, a row whose rule nothing computes:
     | a key never maps to two orders | — | the unique constraint on the key | the hammering test | SLICE-1 GUARANTEE-1 | -->

| Rule | Computed by | Refused by | Guarded by | Proved by |
|---|---|---|---|---|
| <rule> | <where it is computed> | <what refuses a wrong result> | <the test that goes red> | <SLICE-n GUARANTEE-m> |

## Codemap

<!-- Where to find things. Directory → what lives there. An area
     whose directory README says how its parts relate is pointed at
     here, not retold. -->
| Path | What lives there |
|---|---|
| `src/...` | |
