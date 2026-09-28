# Commit plan: the conventions manual

## Summary — the state after all commits

A ninth convention, `conventions`: what a convention is here, its
two parts kept apart, how an artifact is written, how a manual is
written, the rules the container holds about them, and how one is
added. Its manual is born from the four rule sections the index
accreted — the opening definition, *A skill file*, *Writing an
artifact*, *The container's rules*, *Adding a convention* — and the
index returns to what ADR-0032 scoped it to: the table and the
chain, relations only. Every manual answers the seats question in
one sentence or a section. The shape of a manual is a rule of ours
under `.claude/rules/`, loading on the manuals' paths, born from
the pair that recurred in the exchange and shapes manuals. The
convention ships nothing: `foundation` is already in every shipped
file, and the run's own descriptions earn their rule later.

The shared core — one description, everything derived points back,
a change walks the list, a forced change is checked back, a
disagreement is decided with practice as the evidence — is stated
once, in the conventions manual, which is the one truth for the
relation between a description and what comes from it; the concept
is its other instance. The master is a map, an entry point one
level in from the README, and its section 3 narrates the loop and
points at the manual for the rule. Two relations are named and both
are findable: a derivative names its description in `foundation`,
and a pointer names the manual by its path from the repo root, so
that a change to a manual walks its list and greps its path. The
edges that differ stay where they are. The words are decided: a
description is any body of writing things derive from, a manual is
a convention's, `foundation` is the derived side's claim, and the
split carries meaning — versioning, shipping, the kind of
derivative, seats, and what each asserts. Four TODO items close.

## Commits

**1. `docs(agent): add commit plan for the conventions manual`**
This file.

**2. `docs(adr): ADR-0039 — conventions are a convention`**
Opens Proposed. Decides: the manual, named `conventions`, from
what the index held, and the index back to relations; the seats
rule; the shape of a manual as a rule here, its artifact; the
words, with the five differences that make the split meaningful;
the master's section 3 as the rule for every description, and the
trigger for a descriptions manual of its own — that section
outgrowing the page, the master's own rule for itself. Records
what was checked before writing: the last three conventions got a
registry entry and a table row, and none got a CHANGELOG line or a
PLAN step, so the index's *Adding a convention* stated two steps
nobody took. Decision-first: settled in conversation on
2026-09-27 and 28.

**3. `docs: the master's section 3 is the rule for every description`**
Landed as planned (69aceb2), and reversed by 4a below: the
reviewer read the master as a map and the rule as a truth split in
two. What survives of it is the counts, the words, and the loop
narrative; the rule moves.

**4. `docs(conventions): the conventions manual, and the index returns to relations`**
`docs/conventions/conventions/README.md` written from the index's
four rule sections and ADR-0031's claim about what a convention
asserts, in the manual shape: header, opening, what ships (nothing
— what a repo holds is the shape rule and the `foundation` line),
the seats (this repo writes manuals; a run holds artifacts), *what
this is made usable as*. *Adding a convention* is rewritten from
what the last three did. The index keeps the table, with a ninth
row, and the chain; every rule leaves it. Widened at its boundary,
on the reviewer's two readings: §3 gains *one place* — the subject
stated in the manual and nowhere else, two relations, point and
derive — and states the rule for every description in full, the
five steps plus the pointer relation: a pointer is the manual's
path from the repo root, so the walk on a change is the list for
derivatives and a grep for pointers. Until 4a lands the rule is
stated twice, which is the mode inside a set.

**4a. `docs: the master points at the rule, and ADR-0039 says where it lives`**
The master's section 3 keeps the loop, the record of where
practice already bent a description, and one paragraph pointing at
the conventions manual for the rule; the five steps and the
"a rule since" italic leave it. *The words* gains **project**, and
the shapes manual's local definition of it becomes a pointer.
ADR-0039 is revised while Proposed: decision 6 says the rule lives
in the manual and the master is a map; decision 4 lists the
boundary section, *what this does not cover*, as the shape's
seventh, born when this manual needed one four times in one
reading; a decision is added that pointers are paths, and a change
to a manual greps for them, the rename case being commit-plan's
sweep; and the birth case is stated — a newborn description with
existing derivatives walks them in the set that follows, not the
same commit. Widened at step 4's boundary, on the reviewer's
readings of the manual against its own rule. Widened once more
after the plan's second revision, on the reviewer's question:
`foundation` moves home. The conventions manual §2 states the
field — its name, that every derived file carries one, and what
it holds for each kind: the concept and its version, the concept
checked against, the convention by name — and §5's boundary
bullet no longer leaves the values to the exchange; the exchange's
§3 paragraph becomes a pointer and keeps what is the exchange's,
that the field travels with the copy as a live claim, with its
dated history. ADR-0039 gains the decision, amending ADR-0036
decision 7 in the ownership respect.

**5. `docs(conventions): six manuals say their seats`**
One sentence each — project-recording, commit-messages,
repo-hygiene, commit-plan, agent-arrangement, visual-comparison —
placed where the shape says, after *what ships*. Material-first:
the sentence is written from each manual, and if one turns out to
need a section, the boundary says so. Not widened to the boundary
section and the pointer sweep: those are the walk (below), and a
set with one decision does not pick up a second on the way past.

**6. `chore(agent): the shape of a manual, as a rule here`**
`.claude/rules/convention-manual.md`, a Governs line and
`paths: docs/conventions/*/README.md`, stating the sections a
manual has: the header on what derives from it and how a
disagreement ends; the opening statement; what ships; the seats;
lessons as dated italics; what this does not cover; what it is
made usable as. Registry entry "Convention held: conventions".
And the rule's step 2 applied to our own side: the three artifacts
of ours that carry no `foundation` line — `exchange-read`,
`exchange-deliver`, `.claude/rules/exchange-reading.md` — gain
`foundation: the exchange convention`, found by the check at the
third revision. Agent-scoped, alone.

**7. `docs: records, and ADR-0039 accepted`**
ARCHITECTURE's conventions row says nine; the master's 2.3 count
stands (nothing entered the container). TODO: the descriptions
convention item closes into the ADR, the seats item into step 5,
the words item into the ADR, the maintenance rule into step 4. One
item filed: the master and ARCHITECTURE are two maps of one thing
— the master's own erratum says so — and whether the master
becomes ARCHITECTURE waits on project-recording's revision, which
ARCHITECTURE derives from; trigger, that revision or the next
change that updates both maps for one fact. A second item filed,
at the top of Now: **the walk** — the first firing of the rule on
this description. Every manual read against the conventions
manual: a boundary section, pointers by path where a neighbour's
subject is named, restatements turned into pointers, seats where a
sentence turned out not to be enough; each disagreement about
whose a subject is, decided one at a time. Its own set, opened
next; the trigger has fired. ADR-0039 flips.

**8. `docs(agent): close commit plan for the conventions manual`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **Named `conventions`, so the path reads
  `docs/conventions/conventions/`.** The manual is about
  conventions whole — the artifact, the manual, the container's
  rules, adding one — not manuals alone, so `manuals` would name a
  part. The doubled word is the cost.
- **No descriptions convention.** Two kinds of description is two
  instances, and ADR-0038's rule of three binds here too. The
  shared core is one section of the master, and the master already
  says what happens when a section outgrows it.
- **The shape rule is written now, not held.** The shapes manual
  says a shape is born when a pair recurs; the exchange and shapes
  manuals share six sections and both were written from nothing
  telling the writer to. That is the pair. It is ours, exposed,
  ships nowhere.
- **Nothing ships, so no CHANGELOG entry** — and *Adding a
  convention* stops asking for one. The CHANGELOG is the
  concept-version log (ADR-0003); the last three conventions wrote
  no line in it and were right not to.
- **The master is a map, not a truth** (revision at step 4's
  boundary, reversing the plan's step 3 and the previous day's
  call). The argument for the master was that it already narrated
  the loop for both kinds and that a descriptions convention would
  be built from two instances. The second misapplied ADR-0038's
  rule of three: that rule is about building ahead of evidence, and
  the rule for descriptions has fourteen shipped derivatives, nine
  manuals and two walks by hand behind it. Splitting the truth
  between a map and a manual was the defect the manual's own *one
  place* paragraph names. The manual holds it; the master points.
- **A pointer is a path.** Derivatives were findable by
  `foundation`; pointers were not, and the previous day's sweep of
  a word across twenty files was the pointer walk done by hand. A
  manual's path from the repo root is unique, already the
  container's rule for pointers that leave a directory, and
  greppable; a rename is the case commit-plan §4's sweep already
  covers. A name in prose is not a pointer, because names are words.
- **The master and ARCHITECTURE are not merged here.** Both are
  maps and the master says it duplicates ARCHITECTURE. ARCHITECTURE
  is project-recording's record, and that convention is queued for
  revision; deciding the merge before it would decide it twice.
  Filed, with the trigger.
- **The walk is the next set, not this one's step 5** (revision at
  step 4's boundary, on the reviewer's question). The rule this
  set writes demands it — a change to a description walks its
  derivatives — and this description was born with nine. Eight
  manuals read in full, each likely to raise a disagreement about
  whose a subject is, is a set with its own decisions; folding it
  into a step here would make this set two. The birth case is
  written into the ADR so the rule's "same commit" is not a lie on
  the day the rule lands.
- **`foundation` is the conventions convention's, not the
  exchange's** (revision after the second, on the reviewer's
  question). The field is the derived side's claim in the
  description-and-derivative relation, which is this manual's
  subject; the exchange's is what passes between repos, and it
  keeps the one fact that is its own — the field travels with the
  copy. The exchange never listed the field among its four
  artifacts, so nothing it is made usable as changes.
- **The index is cut, not rewritten.** What leaves it goes to the
  manual with its wording; a sentence that is a relation stays. The
  test is ADR-0032's: does it restate a rule that lives in a manual
  or a skill.
