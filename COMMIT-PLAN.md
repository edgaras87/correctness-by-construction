# Commit plan: shapes become a convention, and the model is its manual

## Summary — the state after all commits

One convention, `shapes`, governs what a shape is and how one lives,
on the exchange's pattern: a manual that never ships, and artifacts
held where each side does its part. The manual is
`docs/conventions/shapes/README.md` — the model moved there and
reshaped, written from what cannot change, listing what derives from
it. The run's rule, `shapes-lifecycle.md`, stays the shipped
artifact, now derived from the manual: it carries a `foundation`
line, cites the decision, and gains one sentence the last shape
taught — a shape says its form and nothing of its own lifecycle.
Our side holds no artifact of its own and the manual says why: this
repo keeps exposed shapes only, in `.claude/rules/` with `paths:`,
marked by the Governs line, with no gate and nothing staged to it.
Placement — a shape rides the group of the thing it shapes — is the
manual's, and the delivery README points at it. `docs/models/` holds
two models. Eight conventions where there were seven; `master.md`'s
first erratum closes; ADR-0037 is Accepted.

Named and not built: an unexposed shape staged for a gate is not a
pinned copy, and the copies rule that loads on `temp/` does not know
that. No such shape exists; the manual states the gap and what
closes it.

Not in this set: the handbook filtered out (its own set, next); the
delivery to run 3, whose note will name the rule's new sentence
against its slice-record shape; the maintenance rule for core
descriptions, whose first step this manual happens to run.

## Commits

**1. `docs(agent): add commit plan for the shapes convention`**
This file.

**2. `docs(adr): propose 0037 — shapes are a convention; the model is its manual`**
The decision, Proposed. Context: three documents say what a shape
is and none is a manual; the rule is written from the run's seat;
our one shape runs a subset nothing states; run 3's shape and ours
both restated their lifecycle. Options rejected: keep the three as
they are; a fresh manual beside the model; the rule rewritten for
both seats. Decision: the convention, the manual from the model, the
rule kept whole as the run's only source, placement owned by the
manual, our seat stated not built, the gap named. Supersedes
ADR-0035 decision 9 in part — the description is a manual, not a
model. First, so the manual and the rule cite it.

**3. `docs: the shapes model becomes the manual`**
`git mv docs/models/shapes.md docs/conventions/shapes/README.md`,
then reshaped in place: the header stops calling itself a model and
says what a manual is for; the two pictures stay, their prose still
covering every fact; §4 becomes the owner of placement between
repositories; a section on this repo's seat — exposed only, rules
with `paths:`, the Governs line the marker, no gate; the lesson as
an italic finding, dated 2026-09-26 and naming both firings; the gap
with `delivered-copies.md` as *intended*, with what closes it; and a
closing section, *what this is made usable as*, listing what derives
from it — the shipped rule, the shapes held here as instances, the
delivery README's pointer. `docs/conventions/README.md` gains the
row: eight. `ARCHITECTURE.md`'s codemap: `docs/models/` holds two,
and the shapes row moves to `docs/conventions/`.

**4. `docs: the shipped rule follows the manual`**
`shapes-lifecycle.md`: `foundation: the shapes convention`; one
sentence after the Governs paragraph — a shape says its form and
nothing of its own lifecycle, which is this file's, and a shape that
restates it drifts; the Decisions footer cites CBC ADR-0037 beside
ADR-0035. The shipped birth entry lists `shapes` among the
conventions. `delivery/README.md`'s two shape paragraphs become two
sentences and a pointer to the manual. The rule's definition of a
shape stays: a run cannot read the manual.

**5. `chore(agent): the shapes convention is registered`**
One decisions-log entry: the convention held; what of it this repo
holds — nothing that loads, because we have no `.claude/shapes/` and
no gate; our shapes are rules with a Governs line, `exchange-reading.md`
the one instance; why no copy of the shipped rule sits here.

**6. `docs: master.md catches up, and ADR-0037 is accepted`**
The records commit. `master.md`: §1.2 counts eight and names the
newcomer; §2.3 maps seventeen of seventeen and its italic paragraph
goes; §4.1 names the reading shape as an instance of the convention;
§4.2 unchanged; errata #1 closes. `ARCHITECTURE.md`'s container
paragraph names the convention where it said "the shape lifecycle"
and its counts are made true. The TODO item closes. The sweep: no
live `docs/models/shapes.md`, no "three models". ADR-0037 flips to
Accepted. The devlog carries the set.

**7. `docs(agent): close commit plan for the shapes convention`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The rule repeats the definition, and that is not the drift.**
  The manual explains and the rule states, the relation every
  convention here has; a run holds the rule and cannot open the
  manual, so the rule must say what a shape is. What must not be
  repeated is a *derived* artifact restating its *owner's* lifecycle
  — a shape saying when it opens and closes — and that is the
  sentence step 4 adds. Named because the maintenance-rule item
  could read the two as one case.
- **The manual is the model reshaped, not rewritten.** Its facts
  were measured against the implementation on 09-23 and hold; what
  changes is posture (a manual, not a model), ownership (placement),
  and two additions (our seat, the lesson). A rewrite would have
  produced the same 249 lines from memory of these.
- **The pictures stay.** The model's header records a measurement:
  five facts once lived only in a chart, and the prose grew to cover
  them. Keeping the pictures costs nothing that check did not
  already pay; cutting them is a `visual-comparison` question this
  set does not open.
- **Our seat is a section of the manual, not an artifact.** The
  exchange split its artifacts because each side runs a different
  procedure. Here our side runs no procedure: a shape is a rule with
  `paths:`, and the reviewer moves it. A file that only said "we
  hold nothing" would be the stub ADR-0035 dropped.
- **The gap is named as intended, not closed.** No unexposed shape
  exists on either side, so no rule fires wrongly today. What closes
  it — a line in the note naming a staged shape as one, and the
  copies rule's take excluding it — is written when a first shape is
  staged, from that staging.
- **Step 4 ships one new sentence.** Run 3 will receive it in the
  next delivery and its own shape has the section the sentence
  argues against. That is the note's business, not this set's; here
  it is named so the delivery does not surprise anyone.
