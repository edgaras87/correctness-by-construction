# Model placing

**On trial.** How a model that leans on a manual below it takes the
general idea it borrows, and the manual comes to stand on the model.
Drafted for its first use: the tiers model, which sends its reader
to the exchange for how its flows work (ADR-0071, decision 2).

## What it is for

So that a model holds the facts it relies on, the next project can
derive its own convention from it, and the manual keeps only what is
this repo's. The tiers model points down at the exchange three times
and at `delivery/README.md` once, and holds this repo's "today"
facts. Placing a convention's idea into a model is the step
`docs/models/idea-to-output.md` §4.2 (*Up, work to an idea*) calls
"not yet lived here".

## When it opens

A model's line relies on a fact whose home is a manual or a lower
text (`docs/models/idea-to-output.md` §3.2, *Every link points up*).

## Stages

1. **Read the model whole, then list its lines that rely on
   something below,** each with the lower text's fact it borrows.
   The model may already hold part of that fact, in other words,
   and the lower text retell it without pointing up.
2. **Sort each fact:** general, true for any repo of the model's
   kind; or this repo's, true only here. The question: would the
   next concept repo, or a run, find it true? A "today" does not
   make a fact this repo's: it may be the model's own subject, such
   as the workspace the model maps.
3. **Write the general facts into the model,** in general words,
   where the model's own subject puts them, with a dated note of
   where they were learned.
4. **The manual stands on the model.** Its `foundation` names the
   model, as a manual whose idea a model states does
   (`docs/conventions/conventions/` §1.3, *The `foundation` line*).
   Its lines that told the general facts point up, and it keeps
   what is this repo's.
5. **This repo's facts leave the model:** about this repo, to
   `README.md` (ADR-0068); about how this repo works, to the manual.
6. **Mark what stays as an example:** "here, for example".
7. **Walk both:** what stands on the model, and what stands on the
   manual (`docs/conventions/facts-in-sync/` §4, *The rule for every
   description*).

## Not known yet

- Whether "general enough" can be judged by the one question in
  stage 2.
- Whether a model's dated note fits it: no form says what a model
  holds.
- Whether the manual's `foundation` always becomes the model, or only
  when its whole idea is the model's.

## Ways rejected

- **One general line for each reference down,** and nothing placed:
  the next project loses what it could derive from (ADR-0071).
- **A "This repo" section closing the model:** the reader jumps to
  the end for every example.
- **Writing the model's part first, then finding the manual's
  lines:** the work starts from what the model relies on, so nothing
  is placed that the model does not need.

## Uses
