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
are re-derived.

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

### Mental layer (`concept/`)

Responsibility: the authoritative plain-words statement of the
concept — five chapters, read `00-cbc.md` first. The only place the
concept's substance changes; a state of this directory is what a
concept version names.
Why shaped this way: ADR-0003 (versioning); several documents because
the statement's own split is by chapter (Framing, Step 2).

### Executions (`starter/bundle/`)

Responsibility: the derived layer — the five skills, their
references, the cbc-run playbook, and the
birth scenario (in trial) a run repo copies at birth, covering the
whole pipeline (cbc-framing → infra-establish / infra-serve →
cbc-bootstrap → cbc-slice), each file pinned to the concept
version it derives from or is checked against (ADR-0005).
Content, not this repo's working arrangement: nothing here is
installed in this repo's own `.claude/`, and the archive's agent
definitions stayed behind (ADR-0006). Two skills carry copy-and-fill
template masters in `templates/` beside their references, extracted
from the first run's lived files; a run fills them and the filled
file is the run's own (ADR-0008). The stay-home delivery docs sit
beside the bundle, outside the copy set (ADR-0010): the starter doc
(`starter/README.md`) states the birth mapping and the
authoritative-vs-pinned rule; the install manual
(`starter/installs/cbc.md`) is the birth procedure, peer of the
handbook's `installs/handbook.md`.
Why shaped this way: ADR-0004 (amended), ADR-0006, ADR-0008,
ADR-0010.

## Invariants

<!-- What must NEVER happen to the data / system, and where each rule
     is enforced (DB constraint, module boundary, ...). -->
- Concept substance never changes in the archive — this repo is
  authoritative, the archive a historical snapshot (retired
  2026-08-28: frozen, never consulted as a source again; provenance
  pins remain checkable against it). Enforced in each chapter's
  provenance header, which travels with the file.
- A substantive concept change never lands without a version entry.
  Enforced in CHANGELOG's standing comment and ADR-0003; checked at
  commit review — a review-grade wall, named as such.
- Vendored models are never edited locally — changes arrive only as
  a fresh pinned copy. Enforced in their provenance headers
  (ADR-0002).
- An execution never lands without stating which concept version it
  derives from. Enforced in each file's pin header, which travels
  with every copy into a run repo (ADR-0004).

## Codemap

<!-- Where to find things. Directory → what lives there. -->
| Path | What lives there |
|---|---|
| `concept/` | The mental layer: five chapters, `00-cbc.md` first (concept v1) |
| `starter/` | The delivery layout (ADR-0010): `bundle/` is the derived layer a run copies at birth (skills, playbook, scenario); `README.md` describes and maps; `installs/cbc.md` is the birth manual |
| `docs/baselines/` | Held baselines — theory artifacts withheld from delivery, blind, compared against lived results (ADR-0012) |
| `docs/models/` | Handbook models, vendored pinned copies (ADR-0002) |
| `docs/adr/` | Architecture decision records |
| `devlog/` | Session-by-session work history |
| `CHANGELOG.md` | The concept-version log (ADR-0003) |
| `.claude/` | Working arrangement: skills, agent decisions log |
