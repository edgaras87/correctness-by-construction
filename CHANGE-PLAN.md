# Change-plan: the harvest notes leave the bundle, and the exchange replaces them

## Summary — the state after all commits

A bundle skill ships instructions and nothing else. The provenance and
harvest notes that now open twenty-one files are gone, not moved: git
history and the devlog already hold them, with more detail than the
header lines carried.

What takes over is the exchange ADR-0022 names — a note and a copy,
the same both directions. The note says where the receiver stands,
what changed, why it matters to them and what it recommends, told not
delivered; the receiver reads its own repo and decides. A run gets the
files in its own `temp/` at a named hash, never a path to this repo.

Two documents leave with this set. Run 3 gets its answer, owed since
its handoff of 2026-09-17. The handbook gets the hand-off its own
parked item is waiting for — it wrote half the protocol at `da93a88`
and said the trigger was a second endpoint speaking it; this is that.
And the procedure that never existed gets written: `pure-seed.md`
covers a run's birth and nothing covered its update.

Measured: 455 of 4,091 bundle lines are header notes, 147 of them in
the five `SKILL.md` files.

## Commits

**1. `docs(agent): add change-plan …`** — landed `6c08eff`, revised
`31f7bce`, revised again here.

**2. ADR-0022** — landed `7395ab9`, rewritten `c2a5c13`. Proposed;
flips at commit 12.

**3–7. `docs(starter): <skill>'s notes go`**, one commit per skill —
cbc-framing, cbc-bootstrap, cbc-slice, infra-establish, infra-serve.
Deletion only now; no manual is written. One skill per commit because
the cut is per line, not per block: a template's header keeps its
copy-and-fill instruction and any lived trap, and loses its extraction
and harvest lines. `SKILL.md` keeps what it derives from.

**8. `docs(starter): the Harvest section names the exchange`**
`starter/README.md`'s Harvest section rewritten from the harvester's
seat: a run's change may arrive already made in its copy, so a harvest
is a diff against the pin; the verdict goes back as a note; the
provenance is git's.

**9. `docs(starter): the bundle's update procedure, for a born run`**
A new install doc beside `pure-seed.md`: what the operator copies,
where it lands in the run's `temp/`, what the note carries, how the
run records the new pin, and what is deleted when served. The gap
TODO has carried for the kit, answered for the bundle.

**10. `docs(temp): hand the exchange protocol to the handbook`**
Our lived case as the evidence its parked item wants: the note we
received on 09-16, what we did with it, and what this repo then built
on it. No ADR numbers or paths of ours in it that the handbook cannot
follow — it can, so ours cite as CBC.

**11. `docs(temp): the note to run 3`**
Its ask answered — the edit right granted, the header-line channel
declined and what replaces it — plus the second item its handoff did
not carry: whether infra-establish should say a contract carries a
facility paragraph and where the face is chosen.

**12. `docs: records for the notes leaving the bundle`**
Devlog, TODO lines for what the set leaves open, PLAN's decision index,
and ADR-0022 flipped to Accepted. The set's final records commit.

**13. `docs(agent): close change-plan …`**
Deletes this file; the body carries what diverged. Run 3's handoff
leaves `temp/` here too, served.

## Decisions taken inside this plan

**The manual is abandoned, and the abandonment is on the record.** It
was drafted, cbc-framing's written and staged, and thrown away when the
check showed `git log --follow` already returns the header's own lines
as commit subjects. ADR-0022 keeps it as option 5 so the idea is not
re-proposed in three months. This plan keeps the scar because the close
commit's body is the set's retrospective.

**The strip stays five commits although it is now pure deletion.** The
cut is a judgment per line and a template's header is mixed; one diff
over twenty-one files would hide every call inside it.

**Two outbound documents, not one.** They go to different parties, say
different things, and neither waits on the other. Run 3's is owed; the
handbook's has a trigger that has fired. Splitting them also keeps each
one's deletion-when-served independent.

**The install doc is an install doc, not a skill.** `pure-seed.md` is
read by the operator, and so is this. The run's agent gets its
instructions from the note and the session prompt, as it did for its
kit update.

**This set runs on a branch, `harvest-notes-and-the-reply-channel`,
merging by fast-forward.** Second use of the practice; the handbook
delivery was the first. The branch name predates the ADR's rewrite and
is left alone — renaming a branch mid-set buys nothing and the close
commit names what it was.
