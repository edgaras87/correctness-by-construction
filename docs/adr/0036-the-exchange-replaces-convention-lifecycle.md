# 0036. The exchange replaces convention-lifecycle

Date: 2026-09-26
Status: Proposed (opened under the commit plan for the exchange;
flips to Accepted in that set's records commit)

## Context

Everything that passes between this repo and a run — files down,
edits back, a pin, a verdict — was governed from four places in two
repos. `convention-lifecycle`, 154 lines and our longest skill, was
the receiver's protocol for convention copies, held by this repo
though this repo stopped being a receiver at the fork (ADR-0025) and
has never run it. Run 3 wrote `.claude/rules/skills-changed-in-place.md`
for the method-skill copies because our protocol did not reach them,
and its header says so. `delivery/installs/bundle-update.md`, 527
lines, was our side, with fourteen dated lessons welded into the
steps where each had happened; its staging script had no line for a
rules file, so `shapes-lifecycle.md` was copied by hand. The harvest
direction lived as six paragraphs in `delivery/README.md`. And the
entry file we ship said the method skills are "never edited in
place" while we had taken three such edits from run 3 under seven
rules we adopted on 2026-09-17 and never shipped.

Reading run 3's registry: eight takes with from→to hashes, three
receipt branches, four in-place edits. Heavy use of the protocol on
their side; none on ours. The same three conditions and three
records for editing a copy were written twice — once in our skill
for conventions, once in their file for method skills — and theirs
was the superset.

The reviewer's frame: version sync cannot be fixed until one
document says what this repo is, what a run is, and how they relate
(`docs/master.md`, placed 2026-09-25); then design the exchange
from what cannot change, ignoring the current artifacts.

## Options considered

1. **Widen `convention-lifecycle` to cover method skills and the
   concept.** Rejected: it stays the receiver's half, held by a
   non-receiver, opened by name at no moment — the failure it has
   had since it shipped — and the deliverer's half stays a 527-line
   procedure nobody has open when a step is skipped.

2. **Sync a skeleton and let each run keep local flesh in its
   copies.** Rejected: the compare becomes a judgement where it is a
   `diff` — the miscount problem made permanent; a run's edit could
   stay local and never reach the next run, which the loop exists to
   prevent; and the need has a home, the run's own records. Reopens
   if a run re-applies the same declined edit after two re-pins.

3. **A per-run table here — pin and read point.** Proposed by the
   agent, withdrawn on the reviewer's reading: the run is the only
   place the deliverer can look, so both numbers belong in the run's
   registry entry, and we hold nothing per run.

4. **Keep every note verbatim on the run's side**, since a run
   cannot open our history. Rejected: the run's registry entry is
   written at the take with the note on screen; our side holds the
   note at the pin; no run has needed our exact words in three
   deliveries. A record ahead of its trigger.

5. **A second reading when the run moves before the note.**
   Rejected: one reading per run, extended — new items take the next
   numbers. Two open readings on one run is a named hazard.

6. **A name for the description's home: `docs/system/`,
   `docs/structure/`, `docs/models/`.** All three rejected. `system`
   is the concept's L2, the thing being built, and `cbc-framing`
   writes `docs/system/` into every run. `structure` is static and
   half the content is flow. `models` was defined by `artifact-kinds`,
   deleted the same day; what remained was inference from directory
   contents. The description turned out to be a convention's manual
   and its home follows from that.

## Decision

1. **One convention, the exchange, governs everything that passes
   between deliverer and run.** Its manual is
   `docs/conventions/exchange/README.md` and never ships. Five facts
   it is designed under cannot change: a run is blind; nothing
   arrives by itself; the run holds copies and the deliverer
   masters; a run edits a copy when it fails it; nothing moves
   upward as files.

2. **Four artifacts, split between the two arrangements.** The
   run's rule, `delivered-copies.md`, ships in the container at
   `.claude/rules/`. Two skills, `exchange-read` and
   `exchange-deliver`, and the reading's shape,
   `exchange-reading.md`, are this repo's own. The first convention
   whose artifacts are not all shipped: the two sides do different
   jobs (`master.md` §4).

3. **The run's rule is built from run 3's text.** Read side by side,
   six elements of the two edit rules were one rule; theirs was the
   superset and ours carried a provisional clause that expired on
   09-20. Theirs is renamed for what it governs, widened to every
   delivered copy and `temp/`, its nineteen lines of header history
   removed by its own rule 2, *source* → *deliverer*, and rule 5 made
   the take — opening with the check that would have caught every
   miscount from the receiving side.

4. **Both coordinates are held by the run.** The pin, our commit its
   copies equal, from the staging's name; the read-through, its
   commit we last read up to, from the note. We hold nothing per
   run. Read from the read-through, deliver from the pin; only a
   note moves either, and every read ends with a note, even an empty
   one.

5. **At the pin, the bytes match.** Between pins the copy is the
   master plus the run's edits, and that difference is what the
   deliverer reads. The records are the one exception, because they
   never update.

6. **A copy carries presence and content, never absence.** The note
   names every deletion and rename by path; the take removes them;
   a run does not rename or delete a copy, it asks.

7. **Each group is a piece of the run's tree; every shipped file is
   in exactly one group; every shipped file says what it derives
   from.** Decided here, landed in a second plan: the layout move
   and the field are not in this set.

8. **`convention-lifecycle` goes**, from our arrangement, from the
   container, from the manuals. `bundle-update.md` goes, after its
   one homeless lesson — the rename sweep — lands in `commit-plan`'s
   close step. The shipped entry file's "never edited in place"
   goes; it forbade what the shipped rule permits.

9. **How this repo works a reading is arrangement, not exchange.**
   `temp/working-a-reading.md` stays a draft until its second
   firing; where it lands waits on the records question
   (`TODO.md`, the arrangement item, fact four).

## Consequences

Good: one description, six artifacts that correspond, checked
against each other before anything ships. A run following its rule
records the number the next read starts from; a take removes what a
delivery cannot carry; the skill that stages runs the check that
five deliveries missed. The receiver's protocol is no longer held
by a repo that cannot run it.

Cost: run 3 is told, in the next note, to drop a rule it wrote and
that worked, for one derived from it. Fair only because the shipped
rule is theirs made ours, and the diff is exact from a verbatim
copy in our history. And a convention with artifacts on both sides
is a shape the conventions index has not had to describe.

Held: the trigger for skeleton-sync (option 2); the trigger for
naming when to read at all, which this leaves unnamed.
