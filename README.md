# correctness-by-construction

One authoritative home for a single concept: **correctness by
construction** — the design principle that correctness is built into
the structure of a thing rather than tested in afterwards. The repo
holds the plain-words statement of the concept (with its rationale,
open questions, and the log of what changed it and why) and the
executions derived from it — agent skills, checklists, templates —
each pinned to the concept version it derives from. It is the middle
tier of a three-tier workspace (handbook → concepts → runs; see
docs/models/tiers.md): runs happen in other repos pinned to a concept
version, and their surprises come back here as harvested concept
changes. It exists so its author's understanding improves in a
recorded way instead of living in a head and scattered notes.

## Success criteria

- The concept statement here is the single authoritative version;
  the archive copy is demoted to a historical snapshot.
- The harvest loop has run end-to-end at least once: a real run's
  surprise recorded as a concept change with provenance, and the
  affected execution re-derived. First queued: checkout-system's
  Boot 4.1 testing-trap improvement.
- At least one new run is born from executions copied from this
  repo, not from the archive.
- Months-scale: the concept doc is actually consulted and updated
  after runs.

## Out of scope

- Running projects or experiments here — runs happen in their own
  repos, pinned to a concept version (runs tier).
- Authoring method or working-arrangement conventions — the
  handbook owns method.
- Garden machinery — none until the garden rule triggers: a second
  concept repo, a rule written twice.
- Graduating an execution to its own concept repo — same trigger,
  not now.
- Everything in the archive repo outside the two directories named
  in the birth briefing.

## Project records

| Record | Where | What it answers |
|---|---|---|
| Plan | [PLAN.md](PLAN.md) | Where are we, what's next, what does *done* mean |
| Decisions | [docs/adr/](docs/adr/) | Why is it built this way |
| Architecture | [ARCHITECTURE.md](ARCHITECTURE.md) | What is the current shape of the system |
| Backlog | [TODO.md](TODO.md) | What's known but not done |
| Changelog | [CHANGELOG.md](CHANGELOG.md) | What changed per version (for users) |
| Devlog | [devlog/](devlog/) | Day-to-day work, dead ends, open questions |

<!-- Keep this file short and CORRECT. Live status belongs in PLAN.md,
     not here. Release gate: README verified on a clean machine. -->
