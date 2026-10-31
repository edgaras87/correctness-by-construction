# Model placing

**On trial.** How an Idea Model that leans on a text below it takes the
general idea it borrows, so the lower text comes to stand on the
Idea Model. Rewritten in general at its first evaluation, 2026-10-28, from
one use: the Tiers Model and the Exchange Convention.

## What it is for

So that an Idea Model holds the facts it relies on, the next project can
derive its own text from the Idea Model, and the lower text keeps only
what is its repo's. It is the step from a convention to an Idea Model
(`docs/models/idea-to-output.md` §4.2, *Up, work to an idea*).

## When it opens

An Idea Model's line relies on a fact whose home is a manual or another
text below it (`docs/models/idea-to-output.md` §3.2, *The direction of a link*).

## Stages

1. **Read the Idea Model whole, then list its lines that rely on
   something below,** each with the fact it borrows. The Idea Model may
   already hold part of that fact, in other words, and the lower
   text retell it without pointing up.
2. **Sort each fact:** general, true for any repo the Idea Model maps; or
   this repo's, true only here. The question: would another repo the
   Idea Model maps find it true? A "today" alone does not make a fact
   this repo's: it may be the Idea Model's own subject.
3. **Write the general facts into the Idea Model,** in general words,
   where its own subject puts them, with one line pointing at the
   story of where they were learned, as a lesson does in a manual
   (`docs/conventions/conventions/` §2.6, *A lesson taken*).
4. **The lower text stands on the Idea Model.** A manual's Foundation Line
   names the Idea Model (`docs/conventions/conventions/` §1.3, *The Foundation Line*). Its lines that told the general facts point
   up and keep what each means here, numbered as before, so every
   reference to them still lands.
5. **This repo's facts leave the Idea Model:** about the repo, to
   `README.md`; about how it works, to the manual.
6. **Mark what stays as an example:** "here, for example".
7. **Grep, then walk.** Grep every living reference to the facts' old
   home (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*); then walk what stands on the Idea Model and on the
   lower text (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).

## Not known yet

- Whether stage 2's one question is enough to judge "general".
- Whether a story's pointer fits an Idea Model: no form says what an
  Idea Model holds.
- Whether the lower text's Foundation Line always becomes the Idea Model, or
  only when its whole idea is the Idea Model's.
- Whether an Idea Model may list its own facts again, each with its
  reference, so a reader sees them together.
- Where it is placed when settled. A Work Approach never stands on an
  Idea Model (`docs/models/idea-to-output.md` §3.1, *The four Chain Links*), so
  a manual: likely the conventions manual, beside its part on adding one
  (`docs/conventions/conventions/` §3, *Adding a convention*).

## Ways rejected

- **One general line for each reference down,** and nothing placed:
  the next project loses what it could derive from.
- **A "This repo" section closing the Idea Model:** the reader jumps to
  the end for every example.
- **Writing the Idea Model's part first, then finding the lower text's
  lines:** the work starts from what the Idea Model relies on, so nothing
  is placed that the Idea Model does not need.

## Settled when

It has placed a second Idea Model's borrowed facts, from a different
lower text, and that use changed nothing in its stages.

## Uses

*The deliverer, the tiers model and the exchange, 2026-10-28,
`c94438e`..`a22529d`.* The tiers model sent its reader down four
times: three to the exchange, one to `delivery/README.md`. Sorted,
three of the exchange's five facts and its pin were general, and
went into a new tiers §3.5; the other two the model already held,
and the exchange had retold them without pointing up. The fill was
this repo's, and became a marked example. The exchange came to
stand on the model, its §1 pointing up and keeping what each fact
means here. The README step planned at the start was dropped: the
model's "today" facts map the workspace, its own subject.

Taught: read the model whole before sorting (`4fedbb3`); a "today"
alone does not make a fact this repo's (`4fedbb3`); keeping the
lower text's numbering keeps every reference to it landing. Three
references to exchange §1 were left at the facts' old home and
found by a later check (`b7c17ae`): stage 7 now greps first.

*Its first evaluation, 2026-10-28.* One use, so every piece stayed
on trial and nothing was placed. Rewritten in general, with what
would settle it.

---

## Decisions

- ADR-0068 — stage 5: this repo's facts about itself go to
  `README.md`
- ADR-0071 — *Ways rejected*: one general line for each reference
  down
