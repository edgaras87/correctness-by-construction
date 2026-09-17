# 0022. The notes stay home; a run hears back as a document

Date: 2026-09-17
Status: Proposed

## Context

Two questions arrived within two days of each other and turned out
to be one.

Run 3 asked the first, in a handoff of 2026-09-17. It has a rule of
its own — seven rules, `.claude/rules/skills-changed-in-place.md` —
under which it corrects its copy of a method skill from lived work
instead of writing a prose note, logs the edit in the copy's header
and its decisions log, and asks us to evaluate the diff since its
pin. Its ask is that ADR-0007's harvest section say the change may
arrive already made, so a harvest is a diff against the pin rather
than a reading of prose. It names how our verdict comes back: "as a
document or as the header line the run sees at its next copy."

We asked the second. The handbook, at `ba7eaa4`, rewrote its four
conventions to rules only and moved every explanation into a manual
that stays in the handbook and never ships — roughly two thirds of
each file. The same shape appeared to apply here. Measured: 455 of
4,091 bundle lines are provenance-and-harvest note blocks, 147 of
them in the five `SKILL.md` files; `cbc-framing/SKILL.md` opens with
51 lines of notes before its first instruction. A run reads all of
it and uses none of it — the notes say which archive commit a file
came from, which run taught us what, and which of our ADRs governs,
in our vocabulary, about work the run did not do.

The two meet at one fact: the notes run 3 would read our verdict in
are exactly the notes the second question would remove.

ADR-0007 decision 3 put them there on purpose, and gave its reason:
"the record travels with every future copy (self-containment, S1)."
That reason is load-bearing because a run cannot read this repo —
the tiers model has a run reading only its own, and `temp/README.md`
already forbids a citation a run cannot follow. So anything taken
out of the file is not moved for the run; it is gone for the run.

Against that sits what the notes cost every run that never asked for
them, and a third fact neither question raised: our records hold our
readings of run 3 — what it got wrong, what we declined, what we are
waiting to see it do.

## Options considered

1. **Leave it.** Cheapest, and self-containment stays whole. Rejected:
   it accepts that one line in nine of what ships is our bookkeeping,
   and that a skill can open with 51 lines a run should skip.

2. **Move the notes out; let a run read this repo at defined moments** —
   a step's close, or its re-pin. The shape has precedent one tier up:
   a concept repo opens a handbook checkout for the lifecycle update.
   Rejected on two grounds. A moment named in prose is not a moment:
   this repo lived that at ADR-0021, where a read-after-the-plan guard
   on a shipped reference was found to stop nothing, a prose guard
   being the code-review rung. And the tiers model is the handbook's,
   so a run reading its source is not ours to decide alone.

3. **Move the notes out; no reply at all.** At the re-pin the run
   copies the master whole, and could diff its old edited copy against
   it to see which of its edits survived. Rejected: the diff shows what
   changed, never why, and cannot tell a decline from an oversight —
   which is the one thing run 3's rule 5 needs, since a declined edit
   is gone and never edited back.

4. **Move only the provenance; keep the harvest lines.** Half the
   bytes, and the channel survives. Rejected: it keeps the shape whose
   cost grows — every future harvest adds a line to a shipped file
   forever — and it splits one block by a rule a harvester would have
   to remember.

5. **Move the notes out; the verdict goes back as a document handed at
   the re-pin.** Chosen. It is the option run 3 named first, it is
   ADR-0021's shape applied to a second case, and the re-pin is already
   an operator step, so the document rides with the copy.

## Decision

1. **A shipped file carries instruction only.** The test is the reader:
   a line a run acts on stays; a line about where the file came from,
   which run taught us, or which of our decisions governs, goes. One
   line survives the test as instruction — what the skill derives from,
   concept v1 — because it tells a run the skill is not freestanding
   and that the concept chapters are the theory above it.

2. **Every note moves to a manual, verbatim.** One manual per skill
   under `starter/manuals/`, holding that skill's provenance and every
   harvest line as written. Nothing is rewritten and nothing is
   dropped; a line's wording is the record of what a run said, and
   re-deriving it would lose parts (ADR-0007's own M1).

3. **The manuals stay home, structurally.** ADR-0010 made stay-home
   versus ships a matter of place: nothing under `bundle/` stays,
   nothing outside it ships. `starter/manuals/` is outside. ADR-0010 is
   not amended; this is the rule working.

4. **A run may edit its copy between two pins**, on the terms run 3
   wrote and the handbook reshaped for its own conventions
   (HANDBOOK ADR-0038): from lived work only, as a question or outcome
   any project would want, never project-specific, logged in the copy
   and the run's decisions log, with one TODO line per edited copy
   asking us to evaluate since the pin. We read it when we read the
   run, read-only, at a handoff or a close — never at every step's
   close. The harvest is then a diff against the pin, not a reading of
   prose, and the run's provenance carries into our harvest line as it
   does today.

5. **The verdict goes back as a document, handed at the re-pin.** It
   names each edit taken, reshaped or declined, and why, and the hash
   the master is at. It is written here, carried by the operator with
   the copy, and deleted from `temp/` once served. A declined edit is
   gone at the re-pin and never edited back; what the run still needs
   goes into the run's own records, per its rule 3.

6. **A run does not read this repo.** Not at a step's close, not at its
   re-pin, not under a guard. Two reasons, and the second is the one
   that does not soften: a moment named in prose is not enforced
   (ADR-0021), and our records hold our readings of the run — a run
   that can read its own assessment stops being an independent
   instance and starts writing for its reader.

ADR-0007 is amended in its decision 3 only. Its flow — records are the
source, read-only; the master updated in the run's own wording; the
pin untouched; no concept version bumped; the archive copy left stale —
stands unchanged. Its self-containment argument is answered, not
denied: a copy no longer carries its own history, and what replaces it
is a document that arrives with the copy.

## Consequences

Good: a skill reads as instruction from its first line; 455 lines
leave the shipped set and stop growing; the manuals give each skill
the place the handbook's conventions have for saying why it is shaped
as it is; run 3's edit right is granted on terms already lived one
tier up; and the tiers model needs no change.

Bad, and accepted: self-containment is gone — a copy that outlives
contact with this repo carries no account of itself, and only the
pin in the run's seed commit says where it came from. A verdict now
depends on an operator carrying a document; if that is skipped, a run
learns nothing, where before the header line would have told it at the
next copy. The told channel is unpinned by design (tiers model §3), so
a run leaning on the verdict document carries that diagnostic.

Not settled here: whether a manual, once it exists, should also hold
the why that currently lives only in this repo's ADRs. The manuals
open as a home for the notes and nothing more; what else they earn is
a later decision, and the handbook's invitation of 2026-09-16 — say
what you had to invent because nothing told you — is where that goes.
