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

Two kinds of delivery, two directories (ADR-0017). **Pinned
copies** land as files at paths the kit does not claim; the run
never edits them, only re-copies at a new pin:

| From here | Into the run repo |
|---|---|
| `concept/` | `docs/concept/` — read `00-cbc.md` first |
| `starter/bundle/cbc-framing/` | `.claude/skills/cbc-framing/` |
| `starter/bundle/cbc-slice/` | `.claude/skills/cbc-slice/` |
| `starter/bundle/infra-establish/` | `.claude/skills/infra-establish/` |
| `starter/bundle/infra-serve/` | `.claude/skills/infra-serve/` |
| `starter/bundle/cbc-bootstrap/` | `.claude/skills/cbc-bootstrap/` |

**Fills** are text the seed writes into a file the kit already
put there; from that moment the text is the run's own — edited in
place, never re-copied, no pin beyond the seed commit's subject:

| From here | Into the run repo |
|---|---|
| `starter/fills/cbc-run-pure-playbook.md` | its steps replace everything between the PLAN stub's STEPS markers (the markers stay), and the "Steps from:" line names it at the bundle pin (pure-seed step 3; the newborn holds no playbook copy, their ADR-0031's model) |
| `starter/fills/claude-md-template.md` | its body, from the title line down with `<working-name>` filled, written over the kit's CLAUDE.md stub by the seed's semi-pure step (pure-seed step 4, ADR-0019) — whole, headless, no merge (ADR-0015); with the step off, the newborn derives its own from the stub (ADR-0016) |
| `starter/fills/readme-md-template.md` | the same, over the kit's README.md stub, in the same commit — composed from the kit's README stub @ c670fe5 and the runs' harvested fills |

Everything copies at birth, including the phases that run much
later: each practice skill's readiness gate refuses to start before
its inputs exist, so an early copy is inert, and one delivery
moment keeps the whole set at one pin. The run's plan steps come
from the playbook, which carries the full sequence (ADR-0011),
with the pipeline (cbc-framing → infra-establish → cbc-bootstrap
→ cbc-slice) as its middles — under the v5 provisional cut every
step's gate is derived when the step opens, Release included,
its three kit facts riding as Known already; only re-entry
(infra-serve) arrives unplanned, and its trigger covers that.

The birth procedure itself is the install manual,
`starter/installs/pure-seed.md` (ADR-0016) — the material-only
seed: every delivery a commit on the receipt branch `birth-seed`,
pins in the subjects, main left at the kit's hygiene commit with
the same files untracked (ADR-0018), the newborn's agent finishing
the birth by committing them under its own sequence. The two-birth composition
stands (ADR-0009): their kit supplies the container, this bundle
overlays the method.

## The contract

The overlay assumes exactly three things of the kit — the plan's
STEPS-marker region (the markers stay; only what sits between
them is replaced), the step/gate idiom those steps are written
in, and the handbook's `starter/playbooks/default.md` as the
vendor base for our playbook's endpoint steps (their ADR-0031
contract; `playbooks/` is no longer a kit directory) — and must
not depend on anything else; a handbook kit update is checked
against this list, nothing more. CLAUDE.md is not on the list and
does not return even though the semi-pure step writes over it: a
fill replaces the stub whole and assumes nothing of its shape
(ADR-0015, ADR-0019) — what it depends on is the kit's entry-file
text at the pin, carried verbatim in the fill's kit half and
re-verified at each re-pin, which is a harvest duty here, not a
surface the kit must hold still.
The kit names the same contract from its side (the handbook's
`starter/README.md` contract list, 2026-08-30; narrowed by their
ADR-0031): the handbook states what may be assumed, each bundle
states what it assumes, and a bundle needing a new surface
widens the contract handbook-side first — the fourth handoff
told them CLAUDE.md stays off our list, and ADR-0015 holds it.
The overlay adds files in paths the kit does not claim
(ADR-0012) and performs one non-additive act, switched on per
run: the semi-pure step replaces the kit's two entry stubs,
CLAUDE.md and README.md, whole with the fills (ADR-0019); with
the step off, the stubs stay the newborn's own to fill
(ADR-0016). Records stay the kit's: CbC events are
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
