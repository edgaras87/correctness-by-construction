# 0022. The notes go; the exchange is a note and a copy

Date: 2026-09-17
Status: Accepted (2026-09-17, at the set's final records commit;
opened Proposed per change-plans §4 and rewritten twice at
boundaries — the manual per skill drafted and abandoned when git
history proved it a third copy, then the decision widened from a
reply document to the exchange itself, the user's design. The
strip is in place across 28 files; the procedure it needs is
starter/installs/bundle-update.md; the first run to exercise the
exchange is never-oversold, whose note went out with this set)

## Context

Two questions arrived within two days of each other and turned out to
be one.

Run 3 asked the first, in a handoff of 2026-09-17. Under seven rules
of its own it corrects its copy of a method skill from lived work
instead of writing a prose note, logs the edit in the copy's header
and its decisions log, and asks us to evaluate the diff since its pin.
Its ask is that the harvest section say the change may arrive already
made, so a harvest is a diff against the pin rather than a reading of
prose. It names how our verdict comes back: "as a document or as the
header line the run sees at its next copy."

We asked the second. The handbook, at `ba7eaa4`, rewrote its four
conventions to rules only and moved every explanation into a manual
that stays home. Measured here: 455 of 4,091 bundle lines are
provenance-and-harvest note blocks, 147 of them in the five `SKILL.md`
files; `cbc-framing/SKILL.md` opens with 51 lines of notes before its
first instruction. A run reads all of it and uses none of it — the
notes say which archive commit a file came from, which run taught us
what, and which of our decisions governs, in our vocabulary, about
work the run did not do.

The two meet at one fact: the notes run 3 reads our verdict in are
exactly the notes the second question removes. Run 3's own registry
entry says so — "the bundle's own harvest lines, dated 2026-09-07 to
2026-09-15 and naming this run, are the record of what was taken."

ADR-0007 decision 3 put them there on purpose: "the record travels
with every future copy (self-containment, S1)." That reason is
load-bearing because a run cannot read this repo. So anything taken
out of a shipped file is not moved for the run; it is gone for the
run — unless something else carries it.

Something else already does, once, and we have the instance. The
handbook's note of 2026-09-16 arrived in `temp/` before this
delivery: it read our registry, said which state we were in, said why
our procedure could no longer run, gave three corrections and an
order to apply them, and opened "Told, not delivered. Nothing here is
a rule you owe compliance to." We then read the kit ourselves and
checked its claims in the material — the `conventions/` stubs really
are symlinks into the kit, the old compare really does still resolve
at our pin. The note oriented; the material decided. The handbook
recorded the same shape at `da93a88`: a note is owed when a change
breaks the ability to update; it carries what a diff cannot; it
explains while the kit delivers; it stays optional; and it never
substitutes for the update.

That is the channel the header lines were standing in for, done
better, and it already works in both tiers above us.

## Options considered

1. **Leave it.** Cheapest, and self-containment stays whole. Rejected:
   it accepts that one line in nine of what ships is our bookkeeping,
   and that a skill can open with 51 lines a run should skip.

2. **Move the notes out; give the run a path to this repo, read at
   defined moments.** Rejected. A moment named in prose is not a
   moment — ADR-0021 lived that, where a read-after-the-plan guard on
   a shipped reference stopped nothing. A path also outlives its
   session: a note naming a checkout is committed in the run's
   history, and run 3's own TODO already complains that a pointer to
   a checkout on disk does not carry what it needs. And the tiers
   model has a run reading only its own repo; that model is the
   handbook's, not ours to amend.

3. **Move the notes out; no reply at all.** At the re-pin the run
   could diff its old copy against the new master to see which edits
   survived. Rejected: the diff shows what changed, never why, and
   cannot tell a decline from an oversight — the one thing run 3's
   rule 5 needs, since a declined edit is gone and never edited back.

4. **Move only the provenance; keep the harvest lines.** Half the
   bytes, and the channel survives. Rejected: it keeps the shape whose
   cost grows — every future harvest adds a line to a shipped file
   forever — and splits one block by a rule a harvester must remember.

5. **Copy the notes into a manual per skill before deleting them.**
   Drafted and abandoned at the boundary. ADR-0007 already listed and
   rejected its shape — "a separate execution changelog, a second log
   for what git history and the file itself can already record" — and
   its consequences accepted the trade: the question belongs to git,
   and a document answering it would be a third copy of the truth. The
   check bore that out. `git log --follow` on `templates/registry.md`
   returns the header's own harvest lines as commit subjects, in
   order; "the residue filter refuses agent language" is `ec8e504`,
   "the file ends L1 → L5" is `dd481ea`, the Ryuk trap is `7531281`.
   The commit bodies carry more than the header lines do — what was
   harvested, what was not adopted, and why. The devlog holds each
   harvest a third time, per session.

6. **Delete the notes; the exchange is a note and a copy, both ways.**
   Chosen. It is the option run 3 named first, it is the shape the
   handbook used on us two days ago and recorded at `da93a88`, and it
   needs nothing built.

## Decision

1. **A shipped file carries instruction only.** The test is the
   reader: a line a run acts on stays; a line about where the file
   came from, which run taught us, or which of our decisions governs,
   goes. One line survives as instruction — what the skill derives
   from, concept v1 — because it tells a run the skill is not
   freestanding and that the concept chapters are the theory above it.
   A template's header keeps its copy-and-fill instruction and any
   lived trap it carries, and loses its extraction and harvest lines:
   the test runs per line, not per block.

2. **The notes are deleted, not moved.** Nothing is built to hold
   them, because two records already do. Every harvest line has the
   commit that made it, whose subject is the same statement and whose
   body says more. The devlog carries each harvest session besides. A
   page repeating either would be the third copy ADR-0007 refused.

3. **Where to look is named, not built.** The history of a bundle
   file is `git log --follow -- starter/bundle/<path>`; the session
   around a harvest is the devlog entry of that date; the why is the
   commit body. Nothing under `starter/` changes shape, and ADR-0010's
   stay-home-versus-ships rule is untouched.

4. **The exchange is a note and a copy, and it runs the same way in
   both directions.** The sender reads the receiver's records —
   read-only, scoped to what the change touches and the records around
   it, never the whole repo — evaluates, and writes a note: where the
   receiver stands, what changed, why it matters to them, and what it
   recommends. The note is told, not delivered: the receiver reads it,
   reads its own repo, and decides for itself. Downward the note
   travels with the new files; upward it travels alone, because a run
   describing its own edits needs nothing of ours to write it.

   **A note carries what a copy cannot, and never substitutes for
   one.** The files are the what; the note is the why. If a receiver
   must reach for something neither carries, the note was thin — that
   is the diagnostic, and it is more use than a rule forbidding the
   reach.

5. **A run receives a copy, not a path.** What it needs to read is
   placed in its own `temp/` at a named hash, and deleted when served.
   This is not a guard on a path; it is the absence of one. Nothing
   else is reachable, so nothing has to be forbidden, and no path to
   this repo enters the run's history.

6. **A run may edit its copy between two pins**, on the terms run 3
   wrote and the handbook reshaped for its own conventions
   (HANDBOOK ADR-0038): from lived work only, as a question or outcome
   any project would want, never project-specific, logged in the copy
   and the run's decisions log, with one TODO line per edited copy
   asking us to evaluate since the pin. We read it when we read the
   run, at a handoff or a close — never at every step's close. The
   harvest is then a diff against the pin, not a reading of prose, and
   the run's provenance carries into our commit as it does today.

7. **At the re-pin the master is copied whole, never re-derived.** A
   receiver evaluates freely and may accept or decline, but what it
   accepts it takes verbatim: a pin naming a state the receiver then
   reworded is a pin that lies, and the next diff would compare
   against something never delivered. What a project needs that the
   bundle declines goes into that project's own committed records —
   its entry file, a PLAN gate item, an ADR — not into the copy and
   not into an operator's local file, which belongs to one person on
   one checkout. The per-project overlay stays named and unbuilt, run
   3's own fallback, for the day a declined-but-needed edit becomes a
   pattern rather than a possibility.

8. **The protocol is the handbook's; the procedure is ours.** How
   tiers write notes to each other is method, and method has one
   owner; the handbook has the item parked at `da93a88` awaiting a
   second instance, and this is it, so it goes up as a hand-off with
   our case as the evidence. How this bundle reaches a run is ours and
   does not exist yet: `starter/installs/pure-seed.md` covers birth
   and nothing covers update. It is written as an install doc, its
   peer, read by the operator.

ADR-0007 is amended in its decision 3 only. Its flow — records are the
source, read-only; the master updated in the run's own wording; the
pin untouched; no concept version bumped; the archive copy left stale
— stands unchanged. Its self-containment argument is answered, not
denied: a copy no longer carries its own history, and what replaces it
is a note that arrives with the copy and says more than the header
line could.

## Consequences

Good: a skill reads as instruction from its first line; 455 lines
leave the shipped set and stop growing; no new machinery is added, so
nothing new can fall out of step; the channel that replaces the header
line explains rather than lists, and is the one already proven on us;
run 3's edit right is granted on terms it wrote itself; and the tiers
model needs no change, because no run reads another tier's repo.

Bad, and accepted: self-containment is gone — a copy that outlives
contact with this repo carries no account of itself, and only the pin
in the run's seed commit says where it came from. The exchange now
depends on someone writing the note and carrying it; skipped, a run
learns nothing, where the header line would have told it at the next
copy. The told channel is unpinned by design (tiers model §3), so a
run leaning on a note carries that diagnostic. And a note is work — it
costs a reading of the receiver's records every time, which the header
line did not.

Not settled here: whether this repo ever wants the handbook's manual
shape, a page per skill saying why it is shaped as it is. This
decision says only that such a page is not where the harvest notes go.
