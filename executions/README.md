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
moment keeps the whole set at one pin. The run's middle plan steps
come from the playbook, which carries the pipeline (cbc-framing →
infra-establish → cbc-bootstrap → cbc-slice) as steps with gates;
only re-entry (infra-serve) arrives unplanned, and its trigger
covers that.

## Birth — starting a CbC project on the kit

A run repo is born in two copies: the handbook's starter kit
(`engineering-handbook/starter/kit/`) supplies the container, this
bundle overlays the method (ADR-0009). The sequence:

1. Copy the kit and follow its own instructions — repo, hygiene,
   records, the PLAN stub.
2. Copy this bundle per the table above.
3. Merge `cbc-startup-snippet.md` into the run's CLAUDE.md and
   delete the copy — the stub agent is now the CbC project agent.
4. Append the bundle's birth entry to `.claude/decisions.md`,
   beside the kit's: the date, this repo's commit at copy time,
   "pinned to concept v1". Mechanical, done at copy time like the
   kit's own pin fill — never left for the born agent to remember.
5. Run the stub's Step 0 (bootstrap) as the kit directs. The
   bundle files need no Step 0 decisions of their own: the kit's
   commit-messages rule already scopes them — the skills and
   CLAUDE.md's merged section are arrangement (agent commits);
   `concept/` and `playbooks/cbc-run.md` are project content and
   land with the records. State this in the Step 0 change-plan;
   do not re-derive it per birth.
6. At Framing, the step's gates are met *via* cbc-framing — the
   intent, definition, and registry are the problem statement,
   success criteria, and out-of-scope in the method's richer form —
   and the middle-steps gate item is where the playbook's steps are
   copied into PLAN.md and renumbered.

A correct birth is checkable, not judged — after Step 0 closes,
every item below is a verifiable fact:

- `concept/`, the five skills, and `playbooks/cbc-run.md` present
  and byte-identical to this repo's masters at the pinned commit.
- CLAUDE.md carries the snippet's content with its pin comment;
  the snippet copy is deleted.
- `.claude/decisions.md` carries both birth entries: the kit's
  (handbook commit) and the bundle's (this repo's commit, concept
  v1).
- No commit mixes bundle arrangement files with project records
  (the kit's split, held for bundle files too).
- No bundle file was edited at copy — a run's copies change only
  by re-copy from here, or by a fix its own records state
  (ADR-0007).

The overlay assumes exactly three things of the kit — a CLAUDE.md
to append to, a `playbooks/` directory, the plan step/gate idiom —
and must not depend on anything else; a handbook kit update is
checked against this list, nothing more. The kit names the same
contract from its side (starter/README.md, "The kit's overlay
surface", 2026-08-30): the handbook states what may be assumed,
each bundle states what it assumes, and a bundle needing a fourth
surface widens the contract handbook-side first. It touches one kit file
(CLAUDE.md, by append) and otherwise adds files in paths the kit
does not claim. Records stay the kit's: CbC events are recorded as
ordinary project events under the kit's rules, and the method's own
artifacts (`docs/system/`, the framing derivation) live beside the
records, not in place of them.

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
