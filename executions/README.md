<!-- Provenance — adapted from archive/cbc/system-design-method
     birth-materials/README.md @ fe0075d (PLAN Step 3, 2026-08-28).
     Changes on adaptation: paths rewritten from the bundle's
     copy-me layout to this repo's tree (ADR-0004); the
     authoritative-vs-pinned rule and the concept-version pin made
     explicit. Carries no "derives from" pin of its own — this is
     delivery instructions, not a derived execution. -->

# Executions — what a run repo copies at birth

The executions derived from the concept, each pinned to the concept
version its own header names (ADR-0003). This repo's copies are
authoritative; a run's copies are pinned — they change only by
copying anew from here, and a run's surprises come back as harvest,
never as edits (docs/models/tiers.md).

At a run repo's birth, copy:

| From here | Into the run repo |
|---|---|
| `concept/` (repo root) | `concept/` — read `00-cbc.md` first |
| `cbc-framing/` | `.claude/skills/cbc-framing/` |
| `cbc-slice/` | `.claude/skills/cbc-slice/` |
| `infra-establish/` | `.claude/skills/infra-establish/` |
| `infra-serve/` | `.claude/skills/infra-serve/` |
| `cbc-bootstrap/` | `.claude/skills/cbc-bootstrap/` |
| `cbc-startup-snippet.md` | merged into the run's CLAUDE.md, then the copy deleted |

Everything copies at birth, including the phases that run much
later: each practice skill's readiness gate refuses to start before
its inputs exist, so an early copy is inert, and one delivery
moment keeps the whole set at one pin. In the run's PLAN, author an
infrastructure step and a bootstrap step that invoke their skills
(the pipeline: cbc-framing → infra-establish → cbc-bootstrap →
cbc-slice); only re-entry (infra-serve) arrives unplanned, and its
trigger covers that.

Deliberately absent — the born project's own decisions: recording
conventions, commit conventions, run files, the run's own
versioning. Also deliberately absent: the archive's agent
definitions (ADR-0006) — the skills carry the method whole.
