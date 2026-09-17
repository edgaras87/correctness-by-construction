# 0023. The compare is a reading; the diff is its evidence

Date: 2026-09-17
Status: Proposed (change-plans §4; opened at the head of the set
that takes the handbook's kit, and to be accepted or rewritten at
that set's boundaries — this decision defines what taking the kit
means, so it lands before the taking)

## Context

Taking the handbook's kit into this repo, so that a run has one
upstream, puts an objection in the way: if we hold flavoured
artifacts here while the handbook purifies its own, there are two
masters and the compare dies. Our update procedure is
`git diff <hash>..HEAD -- starter/kit/` — it works because only one
side moves. Once both sides move, every update is a merge, and the
recurring cost that decides the whole question arrives in its worst
form.

The objection is real about the instrument and wrong about the
compare. It assumes a compare asks *are these the same*. The
question worth asking of two repos that have both grown is *has
either side learned something the other should have* — and that
question does not care which side moved.

This repo has run one pass of the second kind, and its result is
the evidence. On 2026-09-09 a reading of the handbook at `af16eb7`
produced five findings, and they split cleanly by what could
possibly have found them:

Only a reading would ever find these. *(5)* Every ADR number inside
a pinned copy is the handbook's, and the bare ones below 0020
collide with this repo's own sequence on other subjects — the
copies were byte-perfect and still wrong here, the defect living in
the relation between a correct copy and its new home. *(2)* The
entry file's Conventions list, which the lifecycle copy now says a
project does not keep, stands here and must go by injection or stay
by decision.

Only a mechanism would ever find these. *(3)* The installed
conventions had drifted — `repo-hygiene`'s base gained the
operator's-file line, `project-recording`'s stubs moved across
`f9371e4..af16eb7` — and nobody suspected it. *(4)* The pin had
been lying since 2026-09-07: the `c670fe5` changes were absorbed
through TODO and the reply loop with no registry entry, which that
entry calls "§8's own warning, lived here."

Finding (4) is the failure mode of a reading with no mechanism
under it, lived here, in this repo, two days before it was caught.
The content was absorbed by conversation, everyone was satisfied,
nothing recorded it, and the pin was false meanwhile. A compare made
only of judgment has no way to notice that it did not happen.

The shape this decision adopts is not new. ADR-0022 built it one
tier down — a note and a copy, the same both directions — and it
ran in both directions within hours of being written. Both
receivers read a note, read their own records, decided for
themselves, wrote their verdict into their own logs and deleted the
paper; both caught things the note had not spelled out. What
changes here is the pair of parties: between us and the handbook
both sides are maintainers, both grow, and learning has to travel
up as readily as delivery travels down.

The models already carry the second half of the mechanism.
`models/tiers.md` §3, taken at `ba7eaa4`, says an edited copy is
not a third form of delivery — delivery comes down, an edit goes up
— and that an edited copy's diff against its pin is one of the
records the tier above reads. That diff is well defined however far
the other side has moved.

## Options considered

1. **Keep the byte compare alone.** Cheapest, mechanical, and it is
   what runs today. Rejected: it found two of the five. It cannot
   see a defect in a byte-perfect copy, and it cannot see shape — our
   CHANGELOG stub "had to be replaced, not filled — app-repo
   assumptions" (2026-08-28), and no diff or grep would have raised
   it, because the file had not changed. The target had.

2. **Replace it with a reading.** Answers the two-masters objection
   outright and matches what a compare is actually for. Rejected on
   finding (4): absorption through conversation with nothing
   mechanical underneath is how the pin came to lie, and a reading
   cannot detect its own absence. It also found two of five.

3. **Run both, as two unrelated procedures at unrelated times.**
   Rejected: a reading with no diff in hand is unanchored — "read
   the other repo and think" does not survive a working session —
   and a diff with no reading over it is what we have now.

4. **A reading, with the diffs underneath as its evidence.** Chosen.
   The mechanical half stays cheap and produces the hunks; the
   reading works from them and decides; a verdict is written either
   way. Nothing is built that does not exist already in some form.

## Decision

1. **A compare is a reading over two diffs, ending in a written
   verdict.** Its question is not whether two copies match. It is
   what either side has learned that the other should have — which
   is asked of both sides, in both directions, in the same pass.

2. **Two diffs, both mechanical, both cheap.** First, the master
   since our pin: what the other side changed, as hunks, without
   anyone having decided in advance that it mattered. Second, our
   own copy against our own pin: the delta list, what we flavoured
   and why. The second is the one that survives two masters — it is
   well defined however far the master has moved, and the tiers
   model already names it as a record the tier above reads (§3).

3. **The reading asks three questions of the material.** What does
   the change teach us — do we take it, reshape it, or decline it?
   What does our own growth teach them — including the growth that
   is not a change to any file they hold? And what does our shape
   show about their artifact that their own repo cannot show them,
   which is the question a single-repo master can never ask itself.

4. **A verdict is written every time, including "taught nothing."**
   A reading that produces no writing is indistinguishable from a
   reading that did not happen — finding (4) is exactly that gap.
   The verdict is a registry entry when it moves a pin, and a devlog
   entry when it moves nothing. This is the handbook's own rule
   about `starter/installs/bundle-update.md`, asked of us on
   2026-09-17 — say what it taught, or that it taught nothing —
   generalised to every compare.

5. **The trigger is a re-pin, or either side's signal.** Not a date.
   At a re-pin the mechanical half must run anyway, so the reading
   rides a moment we already stop at; beyond that either side may
   say it has something to show. A repo that has merely grown is not
   an event, and a compare with no trigger becomes either never or
   constant.

6. **A note may ride with it, on ADR-0022's terms.** Where the
   sender knows what deserves attention it says so — where the
   receiver stands, what changed, why it matters to them, what it
   recommends — told and not delivered, and never a substitute for
   the material. The receiver reads the note, reads its own repo,
   and decides for itself. If it must reach for something neither
   the note nor the diff carries, the note was thin; that diagnostic
   stands as ADR-0022 wrote it.

7. **Each side writes its verdict in its own log, and nobody reaches
   into anybody.** The rule held twice on its first day, in both
   directions, and it is what makes a two-master arrangement
   tractable at all.

8. **A pin's claim changes, and the registry must say so.** Where a
   copy is held verbatim the pin means what it always meant:
   identical to the master at that hash. Where a copy is flavoured,
   the pin means derived from that hash, with this delta list, last
   read on this date. An entry carrying the old wording over a
   flavoured copy is a pin that lies, and this repo has caught one
   already.

9. **The protocol is the handbook's; the procedure is ours.** As
   ADR-0022 decision 8 held: how tiers compare and write to each
   other is method, and method has one owner. This decision states
   how this repo runs its own side and binds nobody else; the case
   goes up as a hand-off with our evidence attached, the 09-09 pass
   and its five findings being that evidence.

This does not amend our copy of `convention-lifecycle`. The copy
stays verbatim at its pin (ADR-0022 decision 7); what changes is the
procedure this repo runs around it, and a rule change there is
theirs to make.

## Consequences

Good: the two-masters objection to taking the kit is dissolved
rather than answered, because the compare that dies was never the
one that taught us anything; the reading catches the two classes of
defect a diff structurally cannot, both of which this repo has
already been bitten by; learning gains a route upward as mechanical
as delivery's route down, which the tiers model asks for and nothing
here provided; and the verdict-every-time rule makes a skipped
compare visible instead of silent.

Bad, and accepted: a compare now costs a reading of another repo's
records every time, where it cost a `diff` before — the recurring
cost is real and it is the one this repo must watch. The reading is
a judgment, so two passes over the same material may differ, and
nothing makes them converge except the written verdicts
accumulating. A flavoured copy's pin makes a weaker claim than a
verbatim copy's, and the registry now has two entry shapes where it
had one. And the trigger rides a re-pin, so a side that stops
re-pinning stops comparing, with nothing to notice it.

Not settled here: which artifacts are held verbatim and which are
flavoured — that is the taking decision, and it comes next; how many
deltas are too many before the take was wrong; and whether the
handbook wants this protocol at all, which is theirs to answer.
