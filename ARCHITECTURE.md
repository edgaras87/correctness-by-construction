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
from. It also holds the **container** a run is born into —
the handbook's starter kit, vendored here at a pin (ADR-0024) —
so a run has one upstream instead of two. Delivery flows down as
pinned copies into run repos; learning flows back up as harvested
concept changes, after which executions are re-derived.

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
hygiene, entry files — held here as the handbook's kit at a pin
rather than taken by the run from the handbook itself (ADR-0024).
Fourteen of sixteen files are byte-identical to the master; the
delta is listed in `starter/README.md` beside the set, never
inside it, one line per departure with its reason and a ceiling of
a third of the files. The seven convention manuals ride along at
the same pin in `docs/conventions/`, read-only, explaining
artifacts we hold verbatim; `docs/conventions.md` beside them
carries that pin and the rule. Inside the container the parts
divide by how they update: the four convention skills are pinned
copies that travel at a re-pin; the record stubs, the entry files
and the hygiene files are the run's own from birth and never
travel again.
Why shaped this way: ADR-0024 (the take), ADR-0023 (what a pin
claims and how a compare runs), ADR-0002 (the vendoring rule the
manuals follow).

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
- The container never departs from its master without a line in the
  delta list saying so and why. Enforced in `starter/README.md`'s
  kit-half section, with a ceiling — past a third of the files, or
  a departure not stateable in one sentence, the take was the wrong
  shape (ADR-0024).
- A pin never claims more than was checked: verbatim means
  identical at that hash, flavoured means derived from it with this
  delta, last read on this date. Enforced in the registry entry and
  the delta list; a compare is a reading over two diffs, and the
  verdict is written every time, including "taught nothing"
  (ADR-0023).
- A record stub is never re-delivered to a live run. Enforced in
  `starter/installs/bundle-update.md`'s container-half rule: a kit
  re-pin moves four files, and the rest are the run's own work
  (ADR-0024).

## Codemap

<!-- Where to find things. Directory → what lives there. -->
| Path | What lives there |
|---|---|
| `concept/` | The mental layer: five chapters, `00-cbc.md` first (concept v1) |
| `starter/` | The delivery layout (ADR-0010, ADR-0017, widened by ADR-0024): `kit/` is the container, the handbook's kit at a pin with a stated delta; `bundle/` is what a run copies as pinned files (the five skills); `fills/` is text written into the container's own files (the playbook's steps); `README.md` describes, maps, and carries the delta list and the kit pin; `installs/` holds the two operator manuals — `pure-seed.md` for birth (ADR-0016) and `bundle-update.md` for every update after it (ADR-0022) |
| `docs/baselines/` | Held baselines — artifacts withheld from delivery, blind to newborns, compared against lived results: the frozen playbook (ADR-0012) and the Spring slice reference, handed to a run only after its build is on record (ADR-0021) |
| `docs/models/` | Handbook models, vendored pinned copies (ADR-0002) |
| `docs/conventions/` | The handbook's seven convention manuals, vendored read-only at the kit's pin; `docs/conventions.md` beside them holds the pin and the rule (ADR-0024) |
| `docs/adr/` | Architecture decision records |
| `devlog/` | Session-by-session work history |
| `temp/` | Working drafts, tracked and deleted when served — handoffs, replies, briefings being molded (not records; `temp/README.md` holds the rule) |
| `CHANGELOG.md` | The concept-version log (ADR-0003) |
| `.claude/` | Working arrangement: skills, agent decisions log |
