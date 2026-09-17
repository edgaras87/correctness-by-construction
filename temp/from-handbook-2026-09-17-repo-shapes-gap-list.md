# From what exists to the model — gap list

DRAFT, 2026-09-16, companion to `repo-shapes-model-draft.md`. Not a
record. Nothing here is decided; it is the input a change-plan
would be written from.

Each item says what is true now, what the model asks for, and how
big the change is. The last section is what should *not* be done
yet, which is the part most likely to be skipped.

---

## A. Confirmed defects, ready now

These are wrong today regardless of whether the model is adopted.
A1 to A4 are residue from the manual-and-artifacts set
(HANDBOOK ADR-0040), three of them in a file that ships. A5 is
residue from the set after it (HANDBOOK ADR-0041) and is the only
one that is not a wording problem.

**A1. artifact-kinds still defines a convention as a document.**
The shipped entry reads "a normative agreement about how we do
things … Binds; consulted," with the exemplar "the commit-messages
convention, wherever this repo holds it." Since HANDBOOK ADR-0040
a convention is a directory holding a manual that binds nothing
and artifacts that bind. The exemplar points at no single thing.

Attempted and abandoned, 2026-09-16 (the vocabulary set, 955d79d
to 35926f4). The first rewrite replaced the staleness with this
repo's own shape — artifacts plus a manual — which is one
arrangement and not what a convention is anywhere else. Corrected
to say only that the agreement binds and need not be one file, then
dropped with the rest of the set as too small to carry a plan.

Still wrong, still worth one sentence when something next opens the
file: "consulted" says a convention is a document you read, and
here it is a directory. It matters most at the moment a second repo
asks what a convention is, which is about to happen.

**A2. "manual" is not in the vocabulary — and should not be.**
Decided 2026-09-16, against the first draft of this list. An entry
was written and rejected on two grounds. Its definition was bound
to this repo's structure, and it contradicted the ordinary sense of
the word: a user manual is exactly the thing that tells you how,
where this one states no rules at all. The vocabulary's own rules
were already against it — scope stays minimal, and a context may
specialise but not contradict.

Where it belongs instead: `conventions/README.md`, beside the
bucket shape it names, as a local specialisation. What a second
repo needs is the shape, not the word; it can call its own
explanation whatever its domain already says. If "manual" turns out
to be spoken in two repos, it earns an entry then, on the
vocabulary's own test.

**A3. The shape rule does not ship.** "A convention is a manual and
its artifacts" lives in `conventions/README.md`, which is
handbook-only. A receiver taking the current kit sees four skills
that got shorter and a frontmatter field that vanished, with
nothing explaining why and nothing telling it the shape. Medium:
decide whether the authoring rule ships at all, and if so in what.
See E1 — this is the one to hold.

**A4. "stub" is used for two different things.** artifact-kinds
defines a stub as a document whose content is holes. The record
stubs are that. Skills are not, yet the word gets reached for. The
model proposes *base*, which repo-hygiene already ships and which
the edit-between-pins rule already describes. Written 2026-09-16
and dropped with the set: it is new content rather than a
correction, and nobody has reached for the wrong word except us, in
conversation. Revisit if a second repo does.

**A5. The kit's masters are loadable as skills in this repo.**
Found 2026-09-16 when a kit skill changed: the tool discovered the
four files under `starter/kit/.claude/skills/` as skills scoped to
that directory, advising that they be preferred over the unscoped
ones when editing files there. Invisible until then, because the
copies were symlinks into the kit and could not differ from it.

Smaller than this list first said, which called it backwards
from HANDBOOK ADR-0041 and wanting a decision. The two files are
identical except inside a set that edits the kit, between the kit
commit and the update commit — one commit so far — and in that
window the master is the newer text the same session just wrote.
The pinned copies buy an agent reading shipped text with no manual
attached, and both files are that text.

Settled 2026-09-17 by recording rather than fixing: HANDBOOK
ADR-0041's consequences now say decision 4 is the intent and not a
guarantee.
A mechanism for a one-commit window costs more than it returns. If
skill discovery turns out to be scopable by a setting, one
exclusion beside `claudeMdExcludes` would close it; not worth
hunting for.

## B. Model work

**B1. The tiers model gains the function dimension.** Today the
maintainer/spender distinction appears once, near the end of §4, as
an aside about which work belongs to which tier. The model draft
makes it a dimension of its own. Medium: a new section in
`models/tiers.md`, plus a line in §2 for each tier naming its
function.

**B2. The concept repo's two layers get the boundary stated.** §2
names the mental layer and the executions. It does not say the
executions are derived from the mental layer and not the reverse,
and it does not say a concept repo is a concept repo first. That
sentence is what stops a concept repo reframing itself as an
agent-behaviour repo. Small.

**B3. Decide whether this is one model or two.** The draft is
written as a separate model. Folding it into tiers is probably
right, since both answer questions about the same picture and two
documents will drift. Folding is the recommendation; it is not
free, because tiers is already read by another repo.

## C. Concept repo (CbC) work

Not the handbook's to do. Listed because the sequencing depends on
it and because the handbook's next set should be written from what
it finds.

**C1. Take the delivery.** Four skill copies and a registry entry,
by convention-lifecycle §3. Small, and it comes first: the
procedure and the commit and change-plan rules that govern the rest
of the work are all inside it.

**C2. Run the diagnostic before restructuring anything.** One
question per file: does this file both explain to the maintainer
and instruct an agent? Only the files answering yes need splitting.
In the handbook that was four of seven. A concept repo already
separates a mental layer from executions, so it may already be in
the right shape and the restructure may be mostly unnecessary.

**C3. Restructure what the diagnostic finds, as its own decision.**
Recorded in the concept repo's own ADRs, not ordered by the
handbook. The handbook tells it the shape through the handoff,
which is the told channel and explicitly not delivery.

**C4. Keep the mental layer beside the buckets, not inside them.**
The failure mode the model names in §2.

**C5. Do not call the buckets conventions.** Same shape, different
word. Method has one owner; a concept repo naming its parts
conventions claims method it does not own.

## D. Already on the backlog

**D1. convention-lifecycle names one upstream** where a run already
holds two. The skill should speak of an upstream and its delivered
set, with the registry entry naming which. Already a TODO item,
with the downstream bound folded into it.

**D2. The downstream bound.** A receiver's pin on the base never
runs ahead of the composer's pin on it. Same TODO item.

**D3. §3 step 4 has no words for a required convention the receiver
holds as stubs.** Found by running the procedure on this repo. Same
TODO item.

**D4. Step 10's first gate item** asks whether artifact-kinds earns
its place, on the evidence that no run in five reached for the
vocabulary. This list first claimed A1, A2 and A4 answered it,
because the vocabulary would carry the shape to a second repo. That
collapsed when A2 was decided against: what ships is a corrected
definition and nothing else, which is thin. The item stays open,
and F is the strongest answer to it — not that the words are used,
but that the convention was aimed at the wrong moment.

## E. What not to do yet

**E1. Do not ship the authoring rule.** A3 is real, but the fix is
a rule written from one instance. The second instance is the
concept repo's restructure, and it has not happened. Ship it after
that, written from two, or discover it was a property of
conventions all along.

**E2. Do not alter conventions to fit the model.** The model binds
nothing by construction. Changing a convention so the picture is
tidier, before a second repo has lived the picture, is the move
this repo's own records flag as a mistake made once already
(HANDBOOK ADR-0020's consequences).

**E3. Do not rename `conventions/`.** If a convention is the
agreement and the directory holds its manual and artifacts, the
directory name is still accurate. A rename is churn across every
record and both models for no gain.

**E4. Do not restructure the handbook further before the delivery.**
Three sets have landed with no field contact. The two defects found
today were both found by asking what a receiver would do, which is
a poor substitute for a receiver.

## F. The meta convention — for after the delivery

Proposed 2026-09-16, unbuilt. The best answer so far to D4, whether
artifact-kinds earns its place.

**The problem it answers.** artifact-kinds is a word list, and a
word list has no moment. That is why no run in five reached for it.
But *what an artifact must carry and how it is written* has a very
clear moment: whenever anyone authors one, which happens
constantly. The convention may have been aimed at the wrong moment
rather than been unnecessary.

**What would move in.** The frontmatter schema, the writing rules,
and eventually the bucket shape, all of which live in
`conventions/README.md` today and therefore never ship. A receiver
authoring its own artifacts gets none of it. This is the same gap
as A3, answered by giving it a home rather than by inventing one.

**What would move out of convention-lifecycle.** Its §1 only, the
requires-chain, which is a fact about how an artifact is built
sitting inside a delivery procedure. The registry, the hash and the
update stay: none of that is meta. The move creates a dependency,
since the delivery procedure would then need the meta convention
present, which the kit satisfies but which should be deliberate.

**What is ready and what is not.** The frontmatter schema is lived
— four skills carry it, two repos read it. The writing rules are
lived, from the HANDBOOK ADR-0039 set. The manual-and-artifacts
shape is not: one repo has done it. Ship the first two, hold the
third, same line as E1.

**Why it waits.** A concept repo is about to author its own
artifacts for the first time outside this repo. What it reaches
for, and what it has to invent because nothing told it, is the
specification for what this convention should contain. Building
first means guessing, then finding out. Needs an ADR when taken: it
changes what two conventions are for.

## Suggested order

1. ~~A1, A2, A4 as one small set here.~~ Tried 2026-09-16 and
   abandoned. A2 was decided against, A4 was cosmetic, and A1 alone
   does not carry a change-plan. What is left of A1 rides with
   whatever next opens the file.
2. **B2**, one sentence, since the concept repo needs it before C4.
   **A5** wants a decision before the next set edits the kit.
3. **C1**, the delivery, with the corrected vocabulary in it.
4. **C2 and C3**, the concept repo's diagnostic and whatever
   restructure it justifies, as its own change set and its own
   decisions.
5. **Read what C3 produced.** Then B1, B3, D1 and **F** written
   from two instances instead of one. F absorbs A3: the authoring
   rule gets a home rather than a patch.
