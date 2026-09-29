# Commit plan: the deliverer's TODO held to its manual

## Summary — the state after all commits

`TODO.md` holds open work only, as `docs/conventions/project-recording/`
§5 asks of both seats. No closed entry remains: what closed is told
by the devlog, the ADRs and git, and the prune checks that each one
is there before it goes. Every open item is still true today, or
it has been closed. Now mirrors Step 10's open work, the birth and
the reading of run 3. Known issues holds the problems we accepted
on purpose. The file drops from about 2,100 lines to under half
that, and the item that asked for this closes with it.

Then every open item has one shape, found on the cleaned file
rather than decided ahead of it. Checked against run 3's TODO, that
shape is written down as a rule, either for both seats or for the
deliverer's seat alone.

## Commits

**1. `docs(agent): add commit plan for the TODO pass`**
This plan.

**2. `docs: TODO drops its closed entries`**
Removes 28 closed entries, the 24 done and the 4 superseded or
moot, about 1,050 lines. The one skipped entry stays, because it
still holds open work (step 3). Each closing fact is checked
against the devlog, an ADR or a commit first. One that has no home
gets it in the devlog, in this same commit, before it leaves here.
This commit closes the item "The deliverer's TODO practice against
project-recording §5", by pruning rather than by a seat rule.

**3. `docs: TODO's stale items closed or given triggers`**
*Provisional.* This goes through the open items from before the
exchange with the reviewer, one at a time: the skipped hand-back
to run 3, whose line still waits on a birth's Step 2, the sixth
handoff material, Variant B, the absorb set's observations, header
audiences, the pure-seed experiment, and any others the reading
turns up. Each one is closed, or rewritten with a trigger. The
split into commits and their wording wait on those answers.

**4. `docs: TODO's sections follow the plan`**
Rebuilds Now around Step 10: the birth, plus reading and delivering
to run 3. Every other item there moves to Next or Later. Items that
describe a problem we accepted move to Known issues. This follows
step 3 so that no item gets sorted before we know it is still
alive.

**5. `docs: TODO items take one shape`**
*Provisional.* This step goes material-first: the open items are
rewritten until one shape holds for all of them. The shape and its
wording come out of the cleaned file, and the file can only be
read once steps 2–4 have landed.

**6. `docs(conventions): a TODO item's shape`**
*Provisional.* The shape from step 5 becomes a rule, and ADR-0040
opens as Proposed. Where the rule goes depends on run 3's TODO,
read against the shape at this boundary. If the run can use it, it
goes in project-recording §5, and `delivery/container/TODO.md`
changes with it. That stub reaches only the next birth, since
records never travel twice. If the run needs its own shape, the
rule goes in the deliverer's seat, with the reason the run differs.

**7. `docs(conventions): a TODO item may carry ideas`**
The reviewer's addition at step 6's boundary. An item gets an
optional `Ideas:` field for ideas about how to handle it, noted
when the item is written, one line each and none weighed. Weighing
is the work's, done when the item comes due. Each idea is then
taken, extended or declined, and the verdict goes where that work
is recorded. The stub, §5 and ADR-0040 gain the field; the ADR is
still Proposed, so it may change inside this set. Existing items
that already carry an unweighed idea in their Context move it
into the field.

**8. `docs: devlog carries the TODO pass`**
The session's entry, written with the pass done and the plan's
divergences known. ADR-0040 flips to Accepted here. Two more
records ride along, both asked for by the reviewer at step 6's
boundary. PLAN's decision index gains ADR-0035 to ADR-0040; it
had stopped at 0034. And TODO gains an item in the new shape, on
the word "step" naming both a PLAN step and a commit in a commit
plan. Its ideas are "commit" for the commit plan's unit and the
reviewer's "plan stage" for PLAN's; its context says "stage" is
already taken three ways.

**9. `docs(agent): close commit plan for the TODO pass`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The prune follows one rule for both seats, not a seat rule.**
  The case for keeping done entries was that they record what
  closed. The devlog, the ADRs and git already record that, so a
  seat rule would have the deliverer keep a second copy on purpose.
  The seats do differ, but in project end, playbooks and
  versioning, and none of these touches the backlog. Run 3 already
  keeps no done entries. The prune changes nothing in
  project-recording. Only step 6 may.
- **No ADR for the prune.** The prune follows the manual as it
  stands, so it makes no new rule. The devlog and commit 2's body
  hold the reasoning. The item shape is a new rule, so it gets
  ADR-0040.
- **Clean first, then the shape, then the run** (the reviewer,
  2026-09-29). A shape decided before the cleaning would be a
  guess. And the run can only be checked against a shape that
  already exists.
- **The prune, then the stale pass, then the re-sort.** Each step
  makes the next one smaller.
