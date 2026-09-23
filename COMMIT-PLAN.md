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

**4. `chore(agent): a project is born with the two places`**
The stubs for `.claude/rules/` and `.claude/shapes/`. Ships the
place, never the contents: an unexposed shape in a birth copy spends
the one thing that cannot be got back. Its own step because it is
the container half's last piece, and because after it that half
stands alone if the rest is abandoned.

**5. `docs: a shape rides the group of the thing it shapes`**
*Provisional in extent.* `delivery/README.md` — the placement rule,
and a pinned-copies row for an exposed shape. Whether the row is
written with no occupant, or deferred until one exists, is decided
at step 4's boundary.

**6. `chore(agent): cbc-slice reads a slice against the project's shapes`**
*Provisional.* The Stage 4 edit, which was dead text before this ADR
because a project had no notion of a shape, and is live after it.
Belongs to `method`, not the container, which is why it is here
rather than beside step 2.

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
- **Steps 5, 6 and 9 are provisional and say so.** The count is
  sayable at four and soft after that; the honest form is a firm head
  and a marked tail rather than confidence about steps whose shape
  earlier boundaries decide.
