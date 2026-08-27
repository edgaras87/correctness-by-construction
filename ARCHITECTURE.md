# Architecture

<!-- Describes the system AS IT IS NOW — not the aspiration. 1–2 pages max.
     Update trigger: a plan step's gate closes and this no longer matches
     reality. For the WHY behind any shape, link the ADR. -->

## Overview

A documentation system, not code: one concept repo on the concepts
tier of the three-tier workspace (handbook → concepts → runs — see
docs/models/tiers.md, vendored here pinned). It holds two layers: the
**mental layer** — the plain-words statement of correctness by
construction, its rationale, open questions, and the log of what
changed it — and the **executions** derived from it (agent skills,
checklists, templates), each pinned to the concept version it derives
from. Delivery flows down as pinned copies into run repos; learning
flows back up as harvested concept changes, after which executions
are re-derived. Provisional (Step 0, from the briefing's hunches) —
Framing confirms or overturns.

```
┌────────────── this repo ──────────────┐
│  mental layer   (the statement)       │
│      │ derive — pinned at a           │
│      ▼ concept version                │
│  executions     (skills, checklists,  │
│                  templates)           │
└──────┬──────────────────────▲─────────┘
  copy │ pinned               │ harvest: a run's
       ▼                      │ surprises
     runs   (other repos) ────┘
```

## Components

### <component>

Responsibility: <one sentence — what it owns, what nothing else may do>.
Why shaped this way: ADR-000N.

## Invariants

<!-- What must NEVER happen to the data / system, and where each rule
     is enforced (DB constraint, module boundary, ...). -->
- <invariant> — enforced in <where>.

## Codemap

<!-- Where to find things. Directory → what lives there. -->
| Path | What lives there |
|---|---|
| `src/...` | |
