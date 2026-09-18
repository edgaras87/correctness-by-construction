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
from. It also holds the **container** a run is born into — this repo's
own, taken from the handbook's starter kit at a pin and owned here
since (ADR-0024, ADR-0025) — so a run has one upstream instead of
two. Delivery flows down as pinned copies into run repos; learning
flows back up as harvested concept changes, after which executions
are re-derived.

```
  handbook ──── kit, vendored at a pin ────┐
     ▲                                     │
     │ findings                            ▼
┌────┴───────── this repo ──────────────────────┐
│  mental layer   (the statement)               │
│      │ derive — pinned at a                   │
│      ▼ concept version                        │
│  executions     (skills, checklists,          │
│                  templates)                   │
│  container      (starter/kit/, theirs + delta)│
└──────┬──────────────────────▲─────────────────┘
  copy │ one delivery,        │ harvest: a run's
       ▼ one pin              │ surprises
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

### Executions (`starter/bundle/`, `starter/fills/`)

Responsibility: the derived layer a run repo receives at birth,
covering the whole pipeline (cbc-framing → infra-establish /
infra-serve → cbc-bootstrap → cbc-slice), each file pinned to the
concept version it derives from or is checked against (ADR-0005).
Two kinds by how they land (ADR-0017): `bundle/` holds the five
skills with their references, copied as files the run keeps
pinned — cbc-framing and cbc-slice ship the same
`references/worked-example.md`, one document read in halves, Part 1
the framing and Part 2 the slice, duplicated so either skill's
directory stands alone; the two copies are byte-identical and a
change to one lands in both, which `diff` checks now that neither
carries a header (ADR-0022); `fills/` holds text the seed writes
into the container's own files and the run then owns. One member
since ADR-0024: the pure playbook's steps into PLAN (cbc-run-pure,
ADR-0016). The two entry-file fills retired there — their bodies
ship inside the container itself, which is the same
whole-file-never-merged rule at a new address (ADR-0015,
ADR-0019).
Content, not this repo's working arrangement: nothing here is
installed in this repo's own `.claude/`, and the archive's agent
definitions stayed behind (ADR-0006). Two skills carry copy-and-fill
template masters in `templates/` beside their references, extracted
from the first run's lived files; a run fills them and the filled
file is the run's own (ADR-0008). The stay-home delivery docs sit
beside the bundle, outside the copy set (ADR-0010): the starter doc
(`starter/README.md`) states the birth mapping and the
authoritative-vs-pinned rule; the install manual
(`starter/installs/pure-seed.md`) is the birth procedure
(ADR-0016) — the material-only seed, copying the container from
`starter/kit/` and the method beside it, its deliveries committed
on a receipt branch the newborn never merges (ADR-0018).
Why shaped this way: ADR-0004 (amended), ADR-0006, ADR-0008,
ADR-0010, ADR-0016, ADR-0017, ADR-0018, ADR-0019, ADR-0024.

### Container (`starter/kit/`, `docs/conventions/`)

Responsibility: what a run is born into — records, conventions,
hygiene, entry files — and this repo's to shape (ADR-0025). It
began as the handbook's starter kit, taken at `ba7eaa4` and
identical through their `8adb46f`; those coordinates stay written
down in `starter/README.md` and `docs/conventions.md`, and nothing
tracks that repo. Fourteen of sixteen files are still as they
arrived; what differs is listed beside the set as a reading aid
for a re-sync, not a gate. The seven convention manuals sit in
`docs/conventions/` — the *why* behind each rule, for a maintainer,
never shipped — and move with the rules they explain. Inside the
container the parts divide by how they reach a run: the four
convention skills travel again at an update; the record stubs, the
entry files and the hygiene files are the run's own from birth and
never travel twice.
Why shaped this way: ADR-0025 (ours, with the fork point recorded),
ADR-0024 (the take that brought it here).

## Invariants

<!-- What must never happen here, and where each rule is actually
     held. This repo has no runtime: a rule is held by a header that
     travels with a file, a standing comment, a procedure, or a check
     at commit review - so each entry names which. -->
- Concept substance never changes in the archive — this repo is
  authoritative, the archive a historical snapshot (retired
  2026-08-28: frozen, never consulted as a source again; provenance
  pins remain checkable against it). Enforced in each chapter's
  provenance header, which travels with the file.
- A substantive concept change never lands without a version entry.
  Enforced in CHANGELOG's standing comment and ADR-0003; checked at
  commit review — a review-grade wall, named as such.
- An execution never lands without stating which concept version it
  derives from. Enforced in each file's pin header, which travels
  with every copy into a run repo (ADR-0004).
- Taken material never loses its provenance: where it came from,
  and the last upstream state it was aligned with, stay written
  down even though nothing tracks that repo any more. Enforced in
  `starter/README.md`'s kit-half section, in `docs/conventions.md`,
  and in each model's own header — the coordinates a re-sync would
  start from, and the only protection against it becoming
  archaeology (ADR-0025, ADR-0026).
- A manual never outlives the rule it explains: a rule changed in
  `starter/kit/` moves its manual in `docs/conventions/` in the
  same commit. Enforced in `docs/conventions.md` — a stale manual
  is the kind of lie nothing catches, because it is read rarely and
  by whoever is least sure (ADR-0025).
- A pin never claims more than was checked. Enforced where this
  repo still reads what it does not own, which is now the runs: a
  compare is a reading over two diffs and the verdict is written
  every time, including "taught nothing" (ADR-0023, narrowed by
  ADR-0025).
- A record stub is never re-delivered to a live run. Enforced in
  `starter/installs/bundle-update.md`'s container-half rule: a kit
  re-pin moves four files, and the rest are the run's own work
  (ADR-0024).

## Codemap

<!-- Where to find things. Directory → what lives there. -->
| Path | What lives there |
|---|---|
| `concept/` | The mental layer: five chapters, `00-cbc.md` first (concept v1) |
| `starter/` | The delivery layout (ADR-0010, ADR-0017, widened by ADR-0024): `kit/` is the container, this repo's since ADR-0025, taken from the handbook's kit at `ba7eaa4` with the delta kept as a reading aid; `bundle/` is what a run copies as pinned files (the five skills); `fills/` is text written into the container's own files (the playbook's steps); `README.md` describes, maps, and carries the delta list and the kit pin; `installs/` holds the two operator manuals — `pure-seed.md` for birth (ADR-0016) and `bundle-update.md` for every update after it (ADR-0022) |
| `docs/baselines/` | Held baselines — artifacts withheld from delivery, blind to newborns, compared against lived results: the frozen playbook (ADR-0012) and the Spring slice reference, handed to a run only after its build is on record (ADR-0021) |
| `docs/models/` | Two models, this repo's (ADR-0026), taken from the handbook at the kit's pin; each header carries the coordinates |
| `docs/conventions/` | Seven convention manuals, this repo's (ADR-0025), taken at the kit's pin; `docs/conventions.md` beside them holds the coordinates and the rule that a manual moves with its rule |
| `docs/adr/` | Architecture decision records |
| `devlog/` | Session-by-session work history |
| `temp/` | Working drafts, tracked and deleted when served — handoffs, replies, briefings being molded (not records; `temp/README.md` holds the rule) |
| `CHANGELOG.md` | The concept-version log (ADR-0003) |
| `.claude/` | Working arrangement: skills, agent decisions log |
