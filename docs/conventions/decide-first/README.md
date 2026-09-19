# Decide first

What a piece of work has not yet decided is named, ordered by what
rests on it, and settled — before its commits are planned. The unit
is the question, and the scope is narrow: only questions whose
answer changes the *shape* of the work.

**What ships:** [`SKILL.md`](SKILL.md), which a project holds at
`.claude/skills/decide-first/` and an agent opens before a commit
plan. This page explains it; the skill states it.

## What it is

Triage, and only triage. It finds the questions and puts them in
order; the answering happens elsewhere — in a sentence to the
reviewer, in a measurement, or in `option-comparison`. A skill that
found the question and also answered it would be two things, and
the second one already exists.

It fills a gap that had a shape before it had a name. `commit-plan`
sequences the commits of a change set and says, in §3, that order
follows where the decision lives — decision-first when it is
settled in conversation, material-first when it is only visible in
the material. What neither it nor anything else covered was the
case where the decision is *not settled and nobody has noticed*.
A plan written there is not material-first; it is a guess wearing a
plan's shape.

The form is not invented. It is the winner of a comparison of four
ways to shape a plan's step list (CBC ADR-0030), and it won on
something the other three could not do: it contained a question
none of them could express. That is why it is a separate artifact
rather than a paragraph in `commit-plan` — the paragraph would have
been read inside the frame that hid the question.

## Why it is shaped this way

- **Ordered by what rests on each, not by difficulty or by
  dependency.** The cost of a wrong answer is everything built on
  top of it, not the answer itself. Dependency order usually
  agrees, because a question everything rests on is usually also
  the one you know least about — and when they disagree, this
  ordering is the one that saves the commits.

- **Every question names how it will be settled, and there are
  only three ways.** Not because three is a natural number, but
  because a question with no method named is not ready to be
  settled, and naming it is what exposes that. "We should decide
  this" survives a review; "settled by: — " does not.

- **`ask` is first and is called the most often skipped.** The
  groups set (CBC ADR-0029) turned on whether "the groups are
  named" meant prose or directories. One sentence would have
  settled it. It was never asked, and the answer cost four commits
  and a mid-set revision. The cheapest method is the one an agent
  is least likely to reach for, so it is named first.

- **It does not fire on every change set.** A gate on all work is
  ceremony, and ceremony is ignored. The scope line — a question
  that changes the *shape* is settled first, one that changes *a
  step* is discovered inside — is what keeps it rare enough to be
  obeyed.

- **Its findings are marked retrospective, and the file says why.**
  All three were read backwards out of the set that prompted it,
  not out of running it. The mark is not modesty; it is what makes
  the first unmarked entry mean something.

## An open question

Whether this is a convention at all. A convention asserts *you may
ignore this, with a reason you can give* — and this one has run
zero times. CBC ADR-0031 records the claim and what would falsify
it: a run that skips it, gives no reason, and comes to no harm.
That is a method filed in the wrong place, and this page is where
it would be written down.

A second: its three ways currently have one destination with a
skill behind it. If it only ever routes to a comparison, it is a
wrapper and the two should merge (ADR-0030 decision 10).

## Where to look

- The rule: [`SKILL.md`](SKILL.md).
- What it hands to: [`../commit-plan/`](../commit-plan/).
- Where `compare` routes: [`../option-comparison/`](../option-comparison/),
  and [`../visual-comparison/`](../visual-comparison/) when the
  question is how something is shown.
- The comparison that produced its shape, and the objections
  against it: CBC ADR-0030.
