<!-- Provenance — adapted from archive/cbc/system-design-method
     birth-materials/README.md @ fe0075d (PLAN Step 3, 2026-08-28).
     Changes on adaptation: paths rewritten from the bundle's
     copy-me layout to this repo's tree (ADR-0004); the
     authoritative-vs-pinned rule and the concept-version pin made
     explicit. Carries no "derives from" pin of its own — this is
     delivery instructions, not a derived execution.
     2026-09-01: split under the starter layout (ADR-0010) — the
     Birth section moved to starter/installs/cbc.md; this file describes. -->

# CbC starter — what a run repo copies at birth

The executions derived from the concept, each pinned to the concept
version its own header names (ADR-0003). This repo's copies are
authoritative; a run's copies are pinned — they change only by
copying anew from here, and a run's surprises come back as harvest,
never as edits (docs/models/tiers.md).

At a run repo's birth, copy:

| From here | Into the run repo |
|---|---|
| `concept/` | `concept/` — read `00-cbc.md` first |
| `starter/bundle/cbc-framing/` | `.claude/skills/cbc-framing/` |
| `starter/bundle/cbc-slice/` | `.claude/skills/cbc-slice/` |
| `starter/bundle/infra-establish/` | `.claude/skills/infra-establish/` |
| `starter/bundle/infra-serve/` | `.claude/skills/infra-serve/` |
| `starter/bundle/cbc-bootstrap/` | `.claude/skills/cbc-bootstrap/` |
| `starter/bundle/cbc-run-playbook.md` | `playbooks/cbc-run.md` — its full sequence then replaces the PLAN stub's STEPS region (starter/installs/cbc.md step 3) |
| `starter/bundle/birth-scenario.md` | the newborn's repo root (in trial — kept or deleted per the trial's open point) |
| `starter/bundle/claude-md-cbc.md` | not copied as a file — its fragments merge into the kit's CLAUDE.md stub at the slots their markers name (assembly step 3, ADR-0014) |

Everything copies at birth, including the phases that run much
later: each practice skill's readiness gate refuses to start before
its inputs exist, so an early copy is inert, and one delivery
moment keeps the whole set at one pin. The run's plan steps come
from the playbook, which carries the full sequence (ADR-0011): the
kit's endpoint steps vendored at their pin, and the pipeline
(cbc-framing → infra-establish → cbc-bootstrap → cbc-slice) as its
middles, each a step with gates; only re-entry (infra-serve)
arrives unplanned, and its trigger covers that.

The birth procedure itself is the install manual,
`starter/installs/cbc.md` — the peer of the handbook's
`starter/installs/handbook.md` in the two-birth composition
(ADR-0009): their kit supplies the container, this bundle overlays
the method.

## The contract

The overlay assumes exactly three things of the kit — a `playbooks/`
directory, the plan's STEPS-marker region with
`playbooks/default.md` as its base (their ADR-0028), and the
CLAUDE.md stub's slots (opening paragraph, Conventions list, "How
to work here", "Local rules") — and must not depend on anything
else; a handbook kit update is checked against this list, nothing
more. CLAUDE.md left the list with the startup snippet (ADR-0012)
and returned with the assembled text (ADR-0014): the bundle ships
its CbC fragments in claude-md-cbc.md, merged into the stub's slots
at birth — text earned from the first walked derivation, not
theory.
The kit names the same contract from its side (the handbook's
`starter/README.md` contract list, 2026-08-30; step item updated
2026-09-01): the handbook states what may be assumed, each bundle
states what it assumes, and a bundle needing a new surface
widens the contract handbook-side first — the stub's slots
re-entering our list is owed to theirs (fourth handoff). The
overlay's one write into a kit file is that merge (ADR-0014);
everything else only adds files in paths the kit does not claim
(ADR-0012). Records stay the kit's: CbC events are
recorded as ordinary project events under the kit's rules, and the
method's own artifacts (`docs/system/`, the framing derivation)
live beside the records, not in place of them.

Three skills (cbc-framing, infra-establish, cbc-bootstrap) carry a
`templates/` directory beside their references — copy-and-fill
masters for the slice registry and the repeating ground and harness
files, plus the README section fragments the infra skills project
at their moments of need (ADR-0008, ADR-0013). They ride the
skill copy at birth like everything else.
At use, the run copies a template to the path its walkthrough
names — or merges a section fragment into its README — and fills
the placeholders; the filled file becomes the run's own — not a
pinned copy — and the run's infrastructure contract notes it was
filled from the skill's templates. Fills never harvest back; a change to a
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
