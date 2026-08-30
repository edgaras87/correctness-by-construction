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
| `cbc-run-playbook.md` | `playbooks/cbc-run.md` — its middle steps are copied into PLAN.md at Framing |

Everything copies at birth, including the phases that run much
later: each practice skill's readiness gate refuses to start before
its inputs exist, so an early copy is inert, and one delivery
moment keeps the whole set at one pin. In the run's PLAN, author an
infrastructure step and a bootstrap step that invoke their skills
(the pipeline: cbc-framing → infra-establish → cbc-bootstrap →
cbc-slice); only re-entry (infra-serve) arrives unplanned, and its
trigger covers that.

Two skills (infra-establish, cbc-bootstrap) carry a `templates/`
directory beside their references — copy-and-fill masters for the
repeating ground and harness files (ADR-0008). They ride the skill
copy at birth like everything else. At use, the run copies a
template to the path its walkthrough names and fills the
placeholders; the filled file becomes the run's own — not a pinned
copy — and the run's infrastructure contract notes it was filled
from the skill's templates. Fills never harvest back; a change to a
template's *shape* harvests like any execution change (ADR-0007).

Deliberately absent — the born project's own decisions: recording
conventions, commit conventions, run files, the run's own
versioning. Also deliberately absent: the archive's agent
definitions (ADR-0006) — the skills carry the method whole.

## Harvest — how a run's lesson lands here

A run's surprise about an execution travels through records
(docs/models/tiers.md): the run records it in its own log and may
fix its own copy; this repo reads that record — read-only, a
harvest never edits a run — and updates the authoritative copy
here, in the run's own wording. The change is logged as one dated
harvest line in that execution's provenance header, which travels
with every future copy. The pin is untouched and no concept
version bumps unless the mental layer itself changed; CHANGELOG
carries concept versions only. The archive's copy stays a
historical snapshot — visibly stale is its job. Why this shape:
ADR-0007.
