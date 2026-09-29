<!-- Provenance — adapted from archive/cbc/system-design-method
     birth-materials/README.md @ fe0075d (PLAN Step 3, 2026-08-28).
     Changes on adaptation: paths rewritten from the bundle's
     copy-me layout to this repo's tree (ADR-0004); the
     canonical-vs-pinned rule and the concept-version pin made
     explicit. Carries no "derives from" pin of its own — this is
     delivery instructions, not a derived execution.
     2026-09-01: split under the starter layout (ADR-0010) — the
     Birth section moved to delivery/installs/cbc.md; this file describes. -->

# CbC delivery — what a run repo copies at birth

The executions derived from the concept, each pinned to the concept
version its own `foundation` field names (ADR-0003, ADR-0036). This repo's copies are
canonical; a run's copies are pinned — they change only by
copying anew from here, and a run's surprises come back as harvest,
never as edits (docs/models/tiers.md).

**Three groups, three directories** (ADR-0029): `container/`,
`method/`, `spring-postgres/`. A skill belongs to exactly one and
travels whole; a group is copied whole or not at all. A run on
Spring and PostgreSQL takes all three. A run on another stack takes
`container/` and `method/` and leaves `spring-postgres/` — two
directories of three, decided by reading their names, and it gets
no ground or bootstrap skill at all.

**A shape belongs to the group of the thing it shapes** (ADR-0035),
by the same rule and for the same reason, and only an exposed one
travels, as a pinned copy into the run's `.claude/rules/`. The rest —
unexposed stock held apart, what a gate does with a staged one — is
the shapes convention's, `docs/conventions/shapes/` §4 (ADR-0037).

Beside the groups and never inside one sit the things *about*
delivery: `fills/`, `installs/` and this file.

There are also three kinds of delivery, which is a different
question — how a thing lands, not which group it is in (ADR-0017,
widened by ADR-0024). **The container** is what a run is born
into:
`delivery/container/` copied whole into the new repo — this
repo's, and the section below says what it holds. Inside it the
parts
divide again, and the division is what an update obeys — the seven
convention skills and the rules file are pinned copies; the record
stubs, the two entry files and the hygiene files are the run's own
from birth and never travel again.

**Pinned copies** land as files at paths the container does not
claim; the run never edits them, only re-copies at a new pin.
**Each group is a piece of the run's tree**: inside
`delivery/<group>/`, every path is the path it lands at, so
`delivery/method/.claude/skills/cbc-framing/` lands at
`.claude/skills/cbc-framing/` and the three groups copied on top of
one another *are* the run's tree. No mapping, and nothing to
forget; a group is left out by not naming its directory. One
exception, stated here and in the exchange's manual and nowhere
else:

| From here | Into the run repo |
|---|---|
| `concept/` | `docs/concept/` — read `00-cbc.md` first |

The concept stays at this repo's root because the repo *is* the
concept. A run on another stack receives two skills, not five, and
its tree is the same shape.

**Fills** are text the seed writes into a file the container
already put there; from that moment the text is the run's own — edited in
place, never re-copied, no pin beyond the seed commit's subject.
One remains, the playbook: the two entry-file fills retired at
ADR-0024, their bodies now shipped inside the container itself.

| From here | Into the run repo |
|---|---|
| `delivery/fills/cbc-run-pure-playbook.md` | its steps replace everything between the PLAN stub's STEPS markers (the markers stay), and the "Steps from:" line names it at the bundle pin (`delivery/installs/pure-seed.md` step 4; the newborn holds no playbook copy) |

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
`delivery/installs/pure-seed.md` (ADR-0016) — the material-only
seed: every delivery a commit on the receipt branch `birth-seed`,
the pin in the subjects, main left at the hygiene commit with the
same files untracked (ADR-0018), the newborn's agent finishing the
birth by committing them under its own sequence. Its peer for
everything after birth is the exchange (ADR-0036,
`docs/conventions/exchange/`) — the note and the copy, staged in the
run's own `temp/` on the reviewer's word, taken whole under the
run's `delivered-copies.md`, the pin and the read-through recorded
by the run. One birth from
one place: ADR-0009's two-copy composition is retired by ADR-0024;
the container ships from here.

## The container half — ours

`delivery/container/` is the run's container, which this repo keeps:
the records, the conventions, the hygiene files and the entry files
a run is born into. This repo's own arrangement is not taken from
it; both derive from the manuals (ADR-0042). It is ours to change
when this repo needs it changed (ADR-0025). Where it came from is a
fact recorded once, in ADR-0038, and nothing here tracks that repo
or prepares to.

**The directory is named for what it is**, as of ADR-0029:
`delivery/container/`, where "kit" had named where the files came
from.

**What the container holds that its tree does not show.**

| What | Why |
|---|---|
| `CLAUDE.md` sits at `.claude/CLAUDE.md`, not at the root | a run builds an app and the root is the app's. This was the seed's step-4 `sed` until the container came here; now it is the artifact |
| `.claude/CLAUDE.md` carries a body composed here, not a stub | two runs derived their entry file unaided and neither produced the pre-framing guard or the pin stance (ADR-0019). A whole file, copied never merged (ADR-0015) |
| `README.md` carries a body composed here, not a stub | the same reading and the same delivery rule |
| `.claude/decisions.md`'s birth entry carries one pin and a read-through | one pin, ours (ADR-0025); the read-through is the exchange's second number (ADR-0036). It carried two pins until 2026-09-26 |
| No `convention-lifecycle` | replaced by the exchange (ADR-0036). The run's half is `.claude/rules/delivered-copies.md`; the receiver's protocol is no longer held by a repo that is not a receiver |
| `visual-comparison` | written here (CBC ADR-0031). A run is born with eight conventions, and its decisions are cited `CBC ADR-nnnn` because they are ours to explain. Two siblings shipped beside it and were discarded unused, 2026-09-24 |

Inside the two composed entry files, the title line, the records
tables and the standing comments are the stubs' own shape; the
rest is this repo's, harvested from the runs' own derivations.

## What replaced the contract

There was a contract here, and ADR-0024 ended it. It named three
things the overlay assumed of a container it did not own — the
plan's STEPS-marker region, the step/gate idiom, and a playbook
held elsewhere as the vendor base for our endpoint steps — and
said a bundle needing a fourth widens the contract on the other
side first. That shape existed because the container arrived from
a repo we did not control. It arrives from here now, so there is
nothing to assume and no one to ask. What stands in its place is
the exchange (ADR-0036): what a run receives, what it changes and
what comes back are read, never contracted.

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

**What a run on another stack does not get is worth saying
plainly**: no infra-establish, no infra-serve, no cbc-bootstrap —
not the walkthroughs, and not their stack-free stages either. All
three are practice-born (ADR-0005), harvested from lived Spring and
PostgreSQL runs rather than derived from the concept. Another
stack's versions are that stack's to harvest, and would land here
as a fourth group beside `spring-postgres/`. The pipeline this repo
describes is therefore whole only for this stack; everyone else
gets its two ends. No such birth has happened yet, and the first
one is where that judgment gets tested (ADR-0029).
At use, the run copies a template to the path its walkthrough
names — or merges a section fragment into its README — and fills
the placeholders; the filled file becomes the run's own — not a
pinned copy — and the run's infrastructure contract notes it was
filled from the skill's templates. Fills never harvest back; a change to a
template's *shape* harvests like any execution change (ADR-0007).

No longer absent, and this is the change ADR-0024 made to what a
birth delivers: recording conventions, commit conventions and the
hygiene base now ship, because the container ships. They are this
repo's rules (ADR-0025), and a run receives them from here.

Still deliberately absent — the born project's own decisions: its
run files and its own versioning. Also absent: the archive's agent
definitions (ADR-0006) — the skills carry the method whole.

## Harvest — how a run's lesson lands here

The up-flow of the exchange, `docs/conventions/exchange/` §6: we
read the run — read-only, a harvest never edits a run — from its own
read-through forward, write the reading, work it, and change the
masters here for what is taken. The verdicts go back in the next
note. A run's edit may arrive already made in its copy, and then the
harvest is a diff against the pin rather than a reading of prose
(ADR-0022). The commit that changes a master is the record of the
change; no shipped file carries a harvest line.

One thing the manual does not say, kept here because it was learned
here: **ask what the run teaches the worked example.** It is bundle
content like the rest and sat untouched through three runs because
nobody asked.

The pin is untouched by a harvest and no concept version bumps
unless the mental layer itself changed; CHANGELOG carries concept
versions only. The archive's copy stays a historical snapshot —
visibly stale is its job.

Every citation of this repo's decisions in a file the bundle ships
writes the number as `CBC ADR-nnnn`: the bundle is copied verbatim
into runs, where a bare number is the run's own (ADR-0020). Text
that stays in this repo — this doc, the fills, the seed, the
records — cites bare.
