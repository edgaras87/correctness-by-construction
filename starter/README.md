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

Three kinds of delivery, three directories (ADR-0017, widened by
ADR-0024). **The kit** is the container: `starter/kit/` copied
whole into the new repo, the handbook's kit as we hold it at a
pin, with the delta the section below lists. Inside it the parts
divide again, and the division is what an update obeys — the four
convention skills are pinned copies; the record stubs, the two
entry files and the hygiene files are the run's own from birth and
never travel again.

**Pinned copies** land as files at paths the container does not
claim; the run never edits them, only re-copies at a new pin:

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
place, never re-copied, no pin beyond the seed commit's subject.
One remains, the playbook: the two entry-file fills retired at
ADR-0024, their bodies now shipped inside the kit itself.

| From here | Into the run repo |
|---|---|
| `starter/fills/cbc-run-pure-playbook.md` | its steps replace everything between the PLAN stub's STEPS markers (the markers stay), and the "Steps from:" line names it at the bundle pin (`starter/installs/pure-seed.md` step 4; the newborn holds no playbook copy, HANDBOOK ADR-0031's model) |

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
the pin in the subjects, main left at the hygiene commit with the
same files untracked (ADR-0018), the newborn's agent finishing the
birth by committing them under its own sequence. Its peer for
everything after birth is `starter/installs/bundle-update.md`
(ADR-0022) — the note and the copy, staged in the run's own
`temp/`, taken whole, the pin recorded by the run. One birth from
one place: ADR-0009's two-copy composition is retired by ADR-0024,
the container now being ours to ship rather than the handbook's to
supply.

## The kit half — ours, and where it came from

`starter/kit/` is this repo's container: the records, the
conventions, the hygiene files and the entry files a run is born
into. It is ours to change when this repo needs it changed
(ADR-0025). It began as a copy of the handbook's starter kit and
keeps their path names, which costs nothing and keeps a comparison
possible.

**Provenance, recorded once.** The bytes came from the handbook at
`ba7eaa4`. Every path we took is identical through their `8adb46f`
— twelve commits later, none of them touching anything we hold —
so `8adb46f` is the last state this repo was aligned with, and
divergence starts after it. These are coordinates for a re-sync
that may never happen, not an obligation: nothing here tracks that
repo, and no update from it is owed a reading.

Kit pin: `ba7eaa4` — this line is the hash's one home, and
`installs/pure-seed.md` reads it from here for the birth entry, so
it moves in one place.

**What differs from what we took, and why.** A reading aid for
whoever attempts a re-sync — not a gate, with nothing counting its
rows:

| What differs | Why |
|---|---|
| `CLAUDE.md` is absent from the root; the kit ships it at `.claude/CLAUDE.md` | a run builds an app and the root is the app's. This was the seed's step-4 `sed` until the kit came here; now it is the artifact |
| `.claude/CLAUDE.md` carries a body composed here, not the kit's stub | two runs derived their entry file unaided and neither produced the pre-framing guard or the pin stance (ADR-0019). A whole file, copied never merged (ADR-0015) |
| `README.md` carries a body composed here, not the kit's stub | the same reading and the same delivery rule |
| `.claude/decisions.md`'s birth entry, and the comment above it, name both upstreams | the delivery has two parents and the record says so |
| `convention-lifecycle` §2 says "the deliverer" where it said "the handbook", in two places | never-oversold found the file pointing at a repo it no longer uses, on the first delivery after the take (2026-09-18). Its own manual already said "the deliverer's commit hash" — the skill and its manual had disagreed upstream, and this closes it |

Inside the two composed entry files, some text came from the kit's
own stubs — `.claude/CLAUDE.md`'s title line, records table and
guard comment; `README.md`'s records table and both its comments —
and the rest is this repo's, harvested from the runs' own
derivations. Recorded because it tells a re-sync which half is
which, not because anything must be re-verified against them.

## What replaced the contract

There was a contract here, and ADR-0024 ended it. It named three
things the overlay assumed of someone else's kit — the plan's
STEPS-marker region, the step/gate idiom, and the handbook's
playbook as the vendor base for our endpoint steps — and said a
bundle needing a fourth widens the contract handbook-side first.
That shape existed because the container arrived from a repo we did
not control. It arrives from here now, so there is nothing to
assume and no one to ask.

What stands in its place is one-directional and ours: the delta
list above, which says how our container departs from the master it
was taken from, and the re-verify duty that keeps the departures
honest at each re-pin. The handbook is owed no promise about shapes
it holds still; what it is owed is a report, and that is the
exchange (ADR-0022), not a contract.

Records stay the container's: CbC events are recorded as ordinary
project events under its rules, and the method's own artifacts
(`docs/system/`, the framing derivation) live beside the records,
not in place of them.

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

No longer absent, and this is the change ADR-0024 made to what a
birth delivers: recording conventions, commit conventions and the
hygiene base now ship, because the container ships. They are the
handbook's rules, held here at a pin and passed on unedited — what
a run receives is theirs, by way of us.

Still deliberately absent — the born project's own decisions: its
run files and its own versioning. Also absent: the archive's agent
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
