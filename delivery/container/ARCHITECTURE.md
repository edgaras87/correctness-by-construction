# Architecture

<!-- Describes the system AS IT IS NOW — not the aspiration. 1–2 pages max.
     Update trigger: a plan step's gate closes and this no longer matches
     reality. For the WHY behind any shape, link the ADR. By rule, not
     by slice: a slice's close adds or changes rows in Invariants, never
     a paragraph; how the slice got there is its record's. -->

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
Why shaped this way: ADR-000N.

## Invariants

<!-- One row per rule the system keeps: where the arithmetic or the
     decision is made, what refuses a wrong result, the test that goes
     red if either went, and the slice that proved it, linked. A "—"
     says a column holds nothing, on purpose. Example, from an order
     service, a row whose rule nothing computes:
     | a key never maps to two orders | — | the unique constraint on the key | the hammering test | SLICE-1 GUARANTEE-1 | -->

| Rule | Computed by | Refused by | Guarded by | Proved by |
|---|---|---|---|---|
| <rule> | <where it is computed> | <what refuses a wrong result> | <the test that goes red> | <SLICE-n GUARANTEE-m> |

## Codemap

<!-- Where to find things. Directory → what lives there. -->
| Path | What lives there |
|---|---|
| `src/...` | |
