# Model placing

**On trial.** How a model that leans on a text below it takes the
general idea it borrows, so the lower text comes to stand on the
model. Rewritten in general at its first evaluation, 2026-10-28, from
one use: the tiers model and the exchange.

## What it is for

So that a model holds the facts it relies on, the next project can
derive its own text from the model, and the lower text keeps only
what is its repo's. It is the step from a convention to a model
(`docs/models/idea-to-output.md` §4.2, *Up, work to an idea*).

## When it opens

A model's line relies on a fact whose home is a manual or another
text below it (`docs/models/idea-to-output.md` §3.2, *Every link
points up*).

## Stages

1. **Read the model whole, then list its lines that rely on
   something below,** each with the fact it borrows. The model may
   already hold part of that fact, in other words, and the lower
   text retell it without pointing up.
2. **Sort each fact:** general, true for any repo the model maps; or
   this repo's, true only here. The question: would another repo the
   model maps find it true? A "today" alone does not make a fact
   this repo's: it may be the model's own subject.
3. **Write the general facts into the model,** in general words,
   where its own subject puts them, with a dated note of where they
   were learned.
4. **The lower text stands on the model.** A manual's `foundation`
   names the model (`docs/conventions/conventions/` §1.3, *The
   `foundation` line*). Its lines that told the general facts point
   up and keep what each means here, numbered as before, so every
   reference to them still lands.
5. **This repo's facts leave the model:** about the repo, to
   `README.md` (ADR-0068); about how it works, to the manual.
6. **Mark what stays as an example:** "here, for example".
7. **Grep, then walk.** Grep every living reference to the facts' old
   home (`docs/conventions/facts-in-sync/` §3.3, *A rename is grepped…*); then walk what stands on the model and on the
   lower text (`docs/conventions/facts-in-sync/` §4, *The rule for
   every description*).

## Not known yet

- Whether stage 2's one question is enough to judge "general".
- Whether a dated note fits a model: no form says what a model
  holds.
- Whether the lower text's `foundation` always becomes the model, or
  only when its whole idea is the model's.
- Whether a model may list its own facts again, each with its
  reference, so a reader sees them together.
- Where it is placed when settled. An approach never stands on a
  model (`docs/models/idea-to-output.md` §3.1, *The four links*), so
  a manual: likely the conventions manual, beside its part on adding one
  (`docs/conventions/conventions/` §3, *Adding a convention*).

## Ways rejected

- **One general line for each reference down,** and nothing placed:
  the next project loses what it could derive from (ADR-0071).
- **A "This repo" section closing the model:** the reader jumps to
  the end for every example.
- **Writing the model's part first, then finding the lower text's
  lines:** the work starts from what the model relies on, so nothing
  is placed that the model does not need.

## Settled when

It has placed a second model's borrowed facts, from a different
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
