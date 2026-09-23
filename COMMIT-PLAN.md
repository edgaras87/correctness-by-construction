# Commit plan: what a shape is, and where each one lives

## Summary — the state after all commits

This repo names a thing it has been doing since 2026-09-06. A
**shape** — what a kind of a project's output looks like, its form
and never its content — gets a vocabulary word, a rule, and a
placement.

The container carries the universal half, and none of it is a model:
`artifact-kinds` knows the word, `shapes-lifecycle` is a rule saying
how a shape lives and moves, and a newborn is born with
`.claude/rules/` and `.claude/shapes/` and a stub in each. Nothing of
this concept is in that half, so the container can go to the
handbook whole.

The delivery carries the placement: a shape rides the group of the
thing it shapes, an exposed one ships as a pinned copy into a run's
`.claude/rules/`, and unexposed stock is held apart with a group tag
— stated as a rule, with no directory made, because we hold none.
`docs/baselines/` is left holding trial evidence only, whose
blindness is a measurement rather than a stage before delivery.

And one model is written, for us: `docs/models/shapes.md`, which
says how shapes relate to outputs, gates, groups and the conventions
beside them. It ships to nobody and binds nothing. Its job is that
the rule is still recallable in a month.

What it gives us: a rule where four artifacts each answered the
question in their own header, and an answer to never-oversold that
says what we do rather than accepting a role and declining half of
it.

What it does not do: sort `docs/baselines/`, or decide the
slice-record shape. Both are their own sets.

## Commits

**1. `docs(adr): propose 0035 — what a shape is, and where each lives`**
The decision came out of conversation, so it is recorded before it
is implemented. Opens Proposed. Every step below may contradict it;
step 10 is where it stops being provisional.

**2. `chore(agent): artifact-kinds gains the shape entry`**
never-oversold's in-place edit, taken into the container master. The
vocabulary is what everything below is written in, so it is first of
the work. The step weighs the wording, not the decision.

**3. `chore(agent): the shape lifecycle ships as a container rule`**
Their `shapes-lifecycle`, reshaped. It is written in general terms
already; what has to change is the collector — the ADR declines that
name — and §2's "the repository this project takes its method from",
which is wrong once a shape's home follows its group. The
container's first `.claude/rules/` artifact.

**4. Dropped at its own boundary — the container ships no shapes
directory.** It was to be a stub for `.claude/shapes/`. The stub was
written, staged and discarded: it said what `agent-arrangement` §3
and the rule's own §2 already say, and most of what was left was
making an empty directory trackable at all. A project creates the
directory when it writes its first shape.

What the drop exposes, and it is real: the rule loads only when a
file under `.claude/shapes/` is read, so a project with no shape
never meets it. Two other homes were weighed and rejected — a clause
in `artifact-kinds`, which has no moment and waits to be stumbled
on, and the stub itself. The answer is a default gate item at a
step's close, which is run 3's step form and is not in this set.
**Recorded at step 10 as a gap this set ships with**, not papered
over.

**4a. `docs: the arrangement names the shapes directory`**
*Added at step 3's boundary.* `agent-arrangement` §3 enumerates what
lives under `.claude/` — `skills/`, `rules/`, the decisions log — and
now omits one. Its manual is `docs/conventions/agent-arrangement/`,
which is ours and ships to nobody, so this is a project-side commit
and cannot share the agent-side one above. The plan had no step for
it; it was the reading's D4, carried in the ADR's decision 1 and
never given a commit.

**4b. `chore(agent): cbc-slice says what a test is for, and what a tripwire is`**
*Added at step 4a's boundary, with the swap below.* never-oversold's
Stage 3 edit — the last of its material not in this set. Each test
carries its criterion, its guarantee and its kill beside it in plain
words; a test that cannot fail for the invariant says on itself that
it is a tripwire on a decided face — and **a tripwire never
discharges a kill**, with the red run deciding which kind a test is
rather than its author. It closes a hole we shipped: the skill
demanded a red for every guarantee and said nothing about a test
that cannot be reddened, so such a test was either mislabelled as
evidence or deleted.

Numbered 4b rather than renumbering the tail, so the cross-references
already written into steps below keep pointing where they point. It
runs before step 5 because Stage 3 precedes Stage 4 in the file both
edit.

**5. `chore(agent): cbc-slice reads a slice against the project's shapes`**
*Provisional.* The Stage 4 edit, which was dead text before this ADR
because a project had no notion of a shape, and is live after it.
Belongs to `method`, not the container, which is why it is here
rather than beside step 2.

**6. `docs: a shape rides the group of the thing it shapes`**
*Provisional in extent.* `delivery/README.md` — the placement rule,
and a pinned-copies row for an exposed shape. Whether the row is
written with no occupant, or deferred until one exists, is decided
at step 4's boundary.

**7. `docs: the baselines drawer holds evidence, not shapes`**
The distinction written where the drawer is described. Its own step
because it is what stops the next reader shipping trial evidence
under a shape's rule, and because the sort it implies is
deliberately not in this set.

**8. `docs(models): how shapes relate to everything else`**
`docs/models/shapes.md`. Written **here and not earlier** on purpose:
a model describes what held, and what held is only visible once the
rule, the placement and the drawer's line exist. It says what a
shape is against what it is not — a template, a specification, a
convention, trial evidence — how exposure relates to the two places,
how a shape's group follows its output, and which of those a project
may disagree with without violating anything, which is all of it.

**9. `docs: ARCHITECTURE carries the shape rule`**
*Provisional in extent, firm in existence.* The codemap row for
`docs/baselines/` states the withheld-and-blind mechanism and goes
wrong the moment shapes are named elsewhere. A components paragraph
and a codemap row for the new model may be owed; decided at step 8's
boundary.

**10. `docs(adr): accept 0035, and the records catch up`**
The ADR flips to Accepted, and `TODO.md` takes what this set found
and is not doing — the drawer sort, the slice-record shape, and the
finding owed back to never-oversold. Never the close commit.

## Decisions taken inside this plan

- **The container half runs first and can stand alone.** Steps 2–4
  are the word, the rule, the two places. If everything after them is
  abandoned, what landed is still true and still universal. That
  ordering is deliberate: the container half has evidence behind it,
  and the delivery half describes traffic that has never moved.
- **The model is written late, and it is the one step that is
  material-first.** Steps 1–7 are a decision settled in conversation
  being implemented. Step 8 is the opposite — it records what the
  implementation turned out to be, so writing it earlier would make
  it a guess we then had to correct.
- **A model is not what reaches other projects.** It describes and
  demands nothing, and `docs/models/` is delivered to nobody
  (ADR-0026). What has to reach a project is the rule. The model
  exists so we can recall in a month why the rule says what it says.
- **The ADR opens the set rather than closing it.** `commit-plan` §3
  puts a conversation-settled decision first. What is material-first
  here is the *wording*, and the steps below are expected to correct
  it through §5 revisions.
- **No directory is created for unexposed stock.** The ADR states
  the rule and makes nothing. We hold no unexposed shape, and a
  named, ruled, empty directory is machinery ahead of its use.
- **`docs/baselines/` is not sorted here.** This set says which kind
  stays in the drawer; moving anything is a separate set with its own
  reading, because a wrong move there destroys a measurement that
  cannot be remade.
- **Two divergences at step 3's boundary, both found by doing the
  work rather than by planning it.** Step 4 shrank because step 3
  gave `.claude/rules/` an occupant, and 4a was missing entirely —
  the container half claimed to be three parts and the third had no
  commit. Recorded here rather than absorbed, per `commit-plan` §5.
- **Then step 4 was dropped at its own boundary**, on the reviewer's
  reading that a third statement of one fact is not a stub but
  duplication. Kept in the list as a dropped step rather than
  deleted, so the close reads what was planned and did not happen,
  and so the gap it leaves is visible rather than inferred.
- **Steps 5 and 6 swapped, and 4b added, 2026-09-23.** The
  reviewer's order is take first, decide our own side after:
  everything never-oversold edited or offered lands, and only then
  does this repo choose where it keeps and ships shapes. The old
  step 5 was ours and stood ahead of a take. The tripwire edit was
  in no step at all — it had been sitting in the reading as its own
  future set, and under this order it belongs here beside the other
  edit to the same file. Steps 6, 7 and 8 are now all our side and
  sit together behind the last take.
- **Steps 6, 7 and 9 are provisional and say so.** The count is
  sayable at four and soft after that; the honest form is a firm head
  and a marked tail rather than confidence about steps whose shape
  earlier boundaries decide.
