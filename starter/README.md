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
| `starter/fills/claude-md-template.md` | its body, from the title line down with `<working-name>` filled, written to `.claude/CLAUDE.md` by the seed's semi-pure step, the kit's root stub removed (pure-seed step 4, ADR-0019; the address since 2026-09-09) — whole, headless, no merge (ADR-0015); with the step off, the newborn derives its own from the stub, at root (ADR-0016) |
| `starter/fills/readme-md-template.md` | the same, over the kit's README.md stub, in the same commit — composed from the kit's README stub @ af16eb7 and the runs' harvested fills, plus the System row (2026-09-09) |

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
the birth by committing them under its own sequence. Its peer for
everything after birth is `starter/installs/bundle-update.md`
(ADR-0022) — the note and the copy, staged in the run's own
`temp/`, taken whole, the pin recorded by the run. The two-birth composition
stands (ADR-0009): their kit supplies the container, this bundle
overlays the method.

## The kit half — held here at a pin

`starter/kit/` is this repo's copy of the handbook's starter kit,
at their path names so a compare is a directory diff with nothing
to map. Fourteen of its sixteen files are byte-identical to the
master; two carry a composed body and a third a changed birth
entry (ADR-0024).

Kit pin: `ba7eaa4` — taken 2026-09-18. This line is the pin's one
home: `installs/pure-seed.md` reads the hash out of it, so a
re-pin moves one line and the birth procedure follows.

A run receives the kit and the bundle as one delivery with one
pin, and that pin claims what ADR-0023 decision 8 says it claims:
derived from the handbook at this hash, with the delta below, last
read on the date the registry entry names. Both hashes are written
down, here and in the delivered birth entry — one pin standing for
two states would be a pin that lies.

**The delta — one line per departure, with its reason.**

| What departs from the master | Why |
|---|---|
| `CLAUDE.md` is absent from the root; the kit ships it at `.claude/CLAUDE.md` | a run builds an app and the root is the app's. This was the seed's step-4 `sed` until the kit came here; now it is the artifact |
| `.claude/CLAUDE.md` carries a body composed here, not the kit's stub | two runs derived their entry file unaided and neither produced the pre-framing guard or the pin stance (ADR-0019). A whole file, copied never merged (ADR-0015) |
| `README.md` carries a body composed here, not the kit's stub | the same reading and the same delivery rule |
| `.claude/decisions.md`'s birth entry, and the comment above it, name both upstreams | the delivery has two parents and the record must say so (ADR-0023 decision 8) |

Three files of sixteen. The ceiling is a third — pass it, or find a
departure that cannot be stated in one sentence with its reason,
and the take was the wrong shape and ADR-0024 is revisited rather
than extended.

**The re-verify duty inside the two composed files.** Each carries
text that is the kit's own, held verbatim, and their
agent-arrangement convention holds that half's rules:
`.claude/CLAUDE.md` keeps the title line, the records table with
its comment, and the guard comment; `README.md` keeps the records
table and both its comments. The rest of each file is this repo's,
harvested from the runs' own derivations — the orientation, the
CbC pointer, the pre-framing guard, the pin stance, the
`docs/system/` and System rows, the Local rules. At every re-pin,
re-verify the kit's half against their entry files at the new pin;
a re-pin that moves the four skills and leaves these unchecked
leaves the record claiming a check it did not make.

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
(docs/models/tiers.md): the run records it in its own log, and it
may have fixed its own copy already. This repo reads that record —
read-only, a harvest never edits a run — and updates the
authoritative copy here, in the run's own wording.

**The change may arrive already made.** A run may edit its copy
between two pins, under rules it keeps and logs (ADR-0022). When it
has, the harvest is a diff of that copy against the pin rather than
a reading of prose, and each hunk is taken, reshaped or declined;
the run's provenance carries into the commit that takes it. When it
has not, the harvest is the reading it always was. Either way the
run sends nothing and this repo reaches into nothing.

**The commit is the record.** There is no harvest line in a shipped
file any more: a file here carries instruction only, and what
changed is the commit that changed it, whose subject states it and
whose body says why (ADR-0022). `git log --follow` over a bundle
path is that file's history; the devlog entry of the date is the
session around it.

**Ask what the run teaches the worked example.** The harvest walks
the skills and their workflows by habit, and the worked example
sat untouched through three runs because nobody asked. It is
bundle content like the rest. Its smallness is deliberate, so the
question is what this run teaches the example — not whether a
lived framing would make a better one.

**The verdict goes back as a note**, carried to the run with its
next copy: what was taken, reshaped or declined, and why. A
declined edit is gone at the re-pin and never edited back; what the
run still needs goes into the run's own records.

The pin is untouched and no concept version bumps unless the mental
layer itself changed; CHANGELOG carries concept versions only. The
archive's copy stays a historical snapshot — visibly stale is its
job. Why this shape: ADR-0007, amended by ADR-0022.

Every citation of this repo's decisions in a file the bundle ships
writes the number as `CBC ADR-nnnn`: the bundle is copied verbatim
into runs, where a bare number is the run's own (ADR-0020). Text
that stays in this repo — this doc, the fills, the seed, the
records — cites bare.
