# 0025. The kit is ours; the handbook becomes provenance

Date: 2026-09-18
Status: Accepted (standalone. Replaces a draft of the same number,
written and staged earlier the same day and never committed — it
added a per-delta convention check, and this decision removes the
thing that check existed to manage)

## Context

Three decisions in two days built a protocol for holding another
repo's material: ADR-0024 took the kit at a pin with a delta list
and a ceiling and held the manuals read-only; ADR-0023 defined what
a compare means between two repos that have both grown; and a
draft ADR-0025, staged and not committed, added a check that every
delta name the convention governing it and prove it still complies.

Each solved a real problem. All three exist to manage being
governed by an upstream.

The user's observation at that draft's boundary: we are designing a
two-party protocol for a party of one. The second party — a repo
that needs this kit and is not a CbC project — does not exist. What
it will want cannot be specified until it exists, so everything
built for it now is guessed.

This repo applies "do not derive the general form from one
instance" to conventions, to playbooks, to stack overlays, and told
the handbook the same thing in the letter still held in `temp/`. It
never applied it to the relationship itself.

And the taking is already done. The kit is here, the manuals are
here, the seed copies from here, and a run can be born on a machine
with no handbook checkout. What the protocol adds from here on is
not material. It is recurring obligation: a delta list with a
ceiling to police, a read-only rule to respect, a compliance check
to run at every delta and every re-pin, and a letter owed upward.

**The fork point, measured rather than assumed.** Our copy holds
the handbook at `ba7eaa4`. Their HEAD at this decision is
`8adb46f`, twelve commits later. Across that span `starter/kit`,
`conventions`, `models`, `starter/playbooks` and `starter/installs`
are **all unchanged**. So our copy is current to their HEAD in
every path we hold: the fork is lossless, and the point is exact.

## Options considered

1. **Keep the protocol as built.** Rejected. It is paid weekly,
   forever, for a relationship whose shape is a guess. The cost
   was named honestly when the take was decided — every handbook
   update evaluated twice — and justified as "a transition cost
   with an end only if their purification happens and our copy
   stays derivable". Neither condition is in our hands.

2. **Fork silently — take the files, record nothing.** Rejected.
   The provenance is what keeps a future re-sync possible, and
   this repo has already lost one bridge exactly that way: the
   only live link between our "run 3" and their "never-oversold"
   was the bundle's harvest lines, and deleting them cost the
   handbook a staged mistake the same day (ADR-0022's first-day
   cost).

3. **Full ownership, provenance recorded once.** Chosen. The
   material is ours; where it came from is a fact written down;
   the obligations go.

## Decision

1. **The kit and the conventions' manuals are this repo's.** They
   are edited when this repo needs them edited, with the ordinary
   care every other file here gets and no justification owed to
   anyone. `starter/kit/` and `docs/conventions/` stop being
   vendored copies and become content.

2. **The provenance is recorded once, as two hashes.** The bytes
   came from the handbook at `ba7eaa4`. Every path we hold is
   verifiably identical through their `8adb46f`, so that is the
   last state we are aligned with and divergence starts after it.
   Both are written in `starter/README.md` and neither is a
   standing obligation — they are the coordinates a future re-sync
   would start from, nothing more.

3. **What goes.** The ceiling on the delta count (ADR-0024
   decision 6). The read-only rule on the manuals (decision 5).
   The re-verify duty on the entry files' kit halves. The
   derivable-from-pure constraint and the letter owed before or
   after the take (decisions 9 and 10). And the draft ADR-0025's
   per-delta convention check, entire.

4. **What stays, in a smaller role.** The delta list in
   `starter/README.md` stays as a *reading aid*: what our files
   differ from in the state we took them from, and why. It is a
   record for whoever attempts a re-sync, not a gate with a limit.
   Nothing blocks on it and nothing counts its rows.

5. **ADR-0023 narrows rather than dies.** Its subject was two
   repos that have both grown, and its claim — that a compare is a
   reading over two diffs, ending in a written verdict — holds
   wherever this repo still reads material it does not own. That is
   now the runs: what we send them, what they edit, what their
   records teach us. The mechanical half and the
   write-a-verdict-every-time rule stand there unchanged. What
   lapses is its application upward, which had one party and no
   longer has a relationship to govern.

6. **What we give up, named rather than glossed.** Improvements
   stop arriving free. They fixed the CHANGELOG stub without being
   asked twice, and their rewrite of 2026-09-17 cut roughly two
   thirds of the four conventions' text while keeping the rules.
   Both landed here at no cost. From now on an improvement in their
   repo is something we notice, or do not.

7. **The trigger for reopening: a second repo that needs this kit
   and is not a CbC project.** Not a date, and not the handbook
   asking. Until one exists we do not design the sharing
   relationship, because until one exists we cannot know what it
   needs. The fork point in decision 2 is what makes reopening a
   one-time merge rather than an archaeology.

8. **Nothing is sent, and the letter is parked rather than
   deleted.** `temp/`'s held hand-off keeps its holding block; what
   it waits for changes from "the take, then a delivery run" to
   "something we actually have to say". The one thing the handbook
   asked for — what `bundle-update.md` taught, once it has run for
   real — is still worth sending when it is true, and costs
   nothing to hold until then.

## Consequences

Good: the work this repo exists for stops paying a tax to a
relationship with one party. Every obligation removed here was
being carried for a repo that has not asked for any of it, and the
removal is deletion rather than construction — the files are
already ours. The ARCHITECTURE invariants leak, the
`commit-messages` unique-index example and anything else that fits
a generic kit badly can now be fixed here, today, instead of
reported and waited on. And the grouping in PLAN Step 9 gets to
draw its lines without negotiating a boundary with anyone.

Bad, and accepted: a maintained upstream stops feeding us. Their
conventions will keep improving and we will not receive it, and
"we will notice" is a weaker mechanism than a pin and a procedure.
If a second non-CbC repo does arrive, whatever we have built here
by then may be further from a general form than the handbook's own
kit would have been, and the merge in decision 7 is paid at that
moment rather than now. The provenance in decision 2 is the whole
of our protection, so if it is ever lost the re-sync becomes
archaeology.

Not settled: what this repo's kit becomes now that nothing
constrains its shape — whether it stays close to the handbook's on
purpose, so a re-sync stays cheap, or drifts toward what CbC runs
actually need. That is a question for the day a shape wants
changing, not a decision to take in advance.
