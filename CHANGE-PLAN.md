# Change-plan: the harvest notes leave the bundle, and the reply becomes a document

## Summary — the state after all commits

A bundle skill ships instructions and nothing else. The provenance
and harvest notes that now sit at the top of twenty-one files live
here instead, one manual per skill under `starter/manuals/`, and a
run never sees them. What a run does see, when we take or decline
one of its edits, is a document handed to it at its re-pin — the
same shape ADR-0021 chose for the Spring reference, for the same
reason: a prose guard is not a wall, so the moment is guaranteed by
what the run holds, not by what it is told.

That answers both open questions at once. Run 3 asked whether a run
may edit its copy between two pins and hear back through the header
line; we answer yes to the edit and no to the channel, and give it
the document instead. Our own question — can the skills be as lean
as the handbook made its conventions — is the same decision seen
from the other end, because the notes it would remove are the
channel run 3 was going to use.

Measured: 455 of 4,091 bundle lines are header notes, 147 of them
in the five `SKILL.md` files. `cbc-framing/SKILL.md` is 51 lines of
notes before its first instruction.

## Commits

**1. `docs(agent): add change-plan for the harvest notes leaving the bundle`**
This file, agreed before any of it lands.

**2. `docs(adr): ADR-0022 — the notes stay home, the reply is a document`**
Opens Proposed per change-plans §4. Amends ADR-0007, whose decision 3
chose the header line for self-containment, and cites ADR-0021 for
why a read is not guarded by asking. States what a skill still
carries, what a manual holds, how a verdict reaches a run, and that
a run still does not read this repo.

**3. `docs(starter): the notes move to manuals, the skills ship lean`**
Five manuals under `starter/manuals/`, one per skill, each holding
that skill's provenance and every harvest line verbatim — nothing
is rewritten and nothing is lost. The twenty-one bundle files lose
their note blocks in the same commit: split apart, a revert of
either half would drop the notes on the floor. Provisional in one
respect: if the diff proves unreviewable at the boundary it splits
per skill, five commits, and the plan is revised first.

**4. `docs(starter): the Harvest section names the new reply channel`**
`starter/README.md`'s Harvest section rewritten from the harvester's
seat: a run's change may arrive already made in its copy, so the
harvest is a diff against the pin, not a reading of prose; the
verdict goes back as a document at the re-pin; the provenance stays
in the manual. This is the half of run 3's ask that it can act on.

**5. `docs(temp): the reply to run 3`**
The verdict document, in this repo's `temp/` for the operator to
carry: its ask taken, what changed about the channel and why, and
the second item its handoff did not carry — whether infra-establish
should say that a contract carries a facility paragraph and where
the face is chosen.

**6. `docs: records for the notes leaving the bundle`**
The devlog entry, TODO lines for what the set leaves open, and
ADR-0022 flipped to Accepted — the set's final records commit, never
the close.

**7. `docs(agent): close change-plan for the harvest notes leaving the bundle`**
Deletes this file; the body carries what diverged. Run 3's handoff
leaves `temp/` here too, served.

## Decisions taken inside this plan

**One line stays in the shipped skill: what it derives from.** "Derives
from concept v1" is instruction, not record — it tells a run the skill
is not freestanding and that the concept chapters are the theory above
it. Everything else in the block is addressed to us: which archive
commit it was imported from, which run taught us what, which of our
ADRs governs. The ADR states the test as this, not as a line count.

**The manuals sit outside `bundle/`.** ADR-0010 made stay-home versus
ships structural — nothing under `bundle/` stays, nothing outside it
ships — and the seed copies `starter/bundle/<skill>/` whole. A manual
beside a `SKILL.md` would ship and would break the seed's
byte-identical check. `starter/manuals/` needs no amendment to
ADR-0010; it is the rule working.

**Not `conventions/`, and no symlinks.** The word means method and
method has one owner, the handbook's caution of 2026-09-16, already
in TODO Later. Our skills are executions derived from `concept/`, and
that derivation is the thing the repo exists to hold. Symlinks would
consolidate nothing either: the handbook needed them because it had
the same file in two places, and `starter/bundle/` is already our
only copy.

**ADR-0020's tag rule survives untouched.** Its `CBC ADR-nnnn` spelling
covers every citation of ours in a file a run holds. Most such
citations are in the note blocks, but not all: the templates cite in
their bodies — `verify-database-model.sql` seven times, `.env.example`
and `application.yaml` five each. The rule keeps its subject after the
notes leave.

**Run 3's edit right is granted, its channel is not.** Its seven rules
are sound and its reviewer already improved two of them. What we
decline is only the return path: a header line the run reads at its
next copy requires the notes to ship, and they are the thing leaving.
Its own TODO offers "a document or the header line", so this takes the
option it already wrote down.

**Runs still do not read this repo.** The tiers model says a run reads
only its own, and the model is the handbook's, not ours to change. It
would not help anyway: our records hold our readings of run 3 — what
it got wrong, what we declined, what we are waiting to see it do — and
a run that can read its own assessment stops being an independent
instance. ADR-0022 records this as the reason, so the question is
settled rather than re-opened each time the notes look heavy.

**This set runs on a branch, `harvest-notes-and-the-reply-channel`,
merging by fast-forward.** Second use; the handbook delivery was the
first, and its close said the retrospective decides whether the
practice becomes anything. Two uses is not yet a rule.
