# Commit plan: round 2's work on layer 5, our agent setup

## Summary — the state after all commits

Round 2's fixes for layer 5 have landed, on the two decisions taken
for TODO's "Decide whether each seat's copy is written for its
seat" (2026-10-27). ADR-0069 records them.

- **No text claims a copy identical.** The commit-messages,
  commit-plan and visual-comparison manuals' lists of what derives
  from them, agent-arrangement's *What the difference is*, and
  conventions §1.1's tag exception for a file byte-identical to its
  shipped master all go.
- **Our three convention skills are written for our seat.** Their
  footers cite `ADR-nnnn`, as every other agent file of ours does,
  in place of `CBC ADR-nnnn` (17 lines). Visual-comparison's §5
  speaks of our Mermaid trial, not of "the deliverer's". The
  decisions log records the change and points at the ADR.
- **`approach-drafting.md` stays one text in both seats** until its
  evaluation at the refinement's close (decision 2). TODO asks
  whether it becomes a convention then.
- **FINDING-193, 197 and 198 are fixed.** `working-a-reading.md`
  points at the records table for when the devlog is written;
  `exchange-reading.md` names exchange §6.3 and §6.4; the
  refinement's layers sit in its §2.2, where the files are listed.
- The refinement's file names each layer 5 finding's ending. TODO's
  seat-copy item goes, its Ideas weighed, and conversation-memory
  §15 with it.
- The run's copies are written for a run in layer 6's plan.

## Commits

**0. `docs(agent): add commit plan for layer 5's work`**
Opens the set.

**1. `docs: ADR-0069 each seat's copy is its own`**
Proposed. Decision 1: each seat's copy is written for its seat,
never claimed the same, and follows its seat's rules. It takes the
option ADR-0042 rejected, for a reason that came later: the
tracking. Rejected: the files kept identical with the claims
dropped, which still needs the tag exception; and the claims kept,
with `approach-drafting.md`'s added. Decision 2:
`approach-drafting.md`, which no manual lists, stays one text until
its evaluation. Rejected: ours as its source, naming the run's
copy; both written per seat, unlinked.

**2. `docs: TODO asks if drafting becomes a convention`**
The reviewer's idea, as agreed on 2026-10-27, its trigger
`approach-drafting`'s evaluation at the refinement's close, stage 5.
Right after the ADR it cites, so no pointer names a missing file.

### Decision 1: descriptions first, then our copies

**3. `docs: no manual claims a copy identical`**
The commit-messages, commit-plan and visual-comparison manuals:
"identical to it today" becomes "written for this seat"
(ADR-0069). Agent-arrangement's *What the difference is* says each
seat's copy is written for its seat, not that three skills are
identical. Conventions §1.1 drops the exception for a file
byte-identical to its shipped master. The claims go while our
copies are still identical, so no line is false at any commit. The
walk reads what stands on the five manuals.

**4. `chore(agent): our skills are written for our seat`**
The three skills' footers cite `ADR-nnnn` (commit-messages 4 lines,
commit-plan 8, visual-comparison 5). Visual-comparison's §5 line on
"the deliverer's Mermaid trial" is written for our seat. The
decisions log gains a short entry pointing at ADR-0069. Agent
files, next after 3; each skill is read against its manual.

### The layer's findings

**5. `chore(agent): working-a-reading cites the records`**
FINDING-193. Step 8's own list of when the devlog is written points
at `CLAUDE.md`'s records table instead.

**6. `chore(agent): exchange-reading names exchange §6.3`**
FINDING-197. "When it opens, extends and closes is the exchange's"
names `docs/conventions/exchange/` §6.3 and §6.4.

**7. `chore(agent): the refinement's layers sit in §2.2`**
FINDING-198. The six layers move from §2.5, the findings, to §2.2,
the files. §2.5 points at them. The pointers in §1, §2.2, §2.7 and
§3 move. A commit of its own, as the refinement's step Notes ask of
a change to the approach.

### Records and close

**8. `docs: round 2's layer 5 is worked`**
The records commit. ADR-0069 Accepted. The refinement's file:
FINDING-193, 197 and 198 name their commits; 194 and 196 the TODO
items they went to; 195 ADR-0069; 221's decline gains decision 2's
reason. TODO's seat-copy item goes, each Idea's verdict in the
body, and conversation-memory §15 with it.

**9. `docs(agent): close commit plan for layer 5's work`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A commit
that changes a manual walks what stands on it; a derived file that
then disagrees gets a lettered commit after it.

## Decisions for you to object to

- **One ADR for the two decisions.** ADR-0042's status stays: it
  rejected an option, and taking one is no change to its decisions,
  as when ADR-0066 took the renumbering ADR-0065 rejected.
- **The claims go before our copies change** (commit 3 before 4),
  so no line says "identical" while the files differ.
- **The decisions log's entry rides in commit 4,** with the change
  it records; both are agent files.
- **The run's copies wait for layer 6.** Only visual-comparison §5
  addresses both seats. Layer 6 writes it for a run, beside
  FINDING-222, which reaches that skill in both seats and stays
  layer 6's.
- **The record forms' shared text needs nothing.** TODO's header
  shares 18 lines with the run's stub, the README's comment some
  more; each is already written for its seat, and none claims the
  other. The item's Idea on it is answered so.
- **Round 2's met items in layer 5's files:**
  - `commit-plan`'s `requires: project-recording` is not fixed here.
    Conventions §1.2 says `requires` names conventions, and also
    that it refers to a skill by name; project-recording is a
    convention with no skill. "Decide which way a fact reference
    may point" already weighs `requires`; commit 8 adds this to it
    as an Idea.
  - `exchange-read` naming its phases steps: no commit here opens
    it, so the last read takes it.
  - `approach-drafting.md`'s "The refinement is open." goes stale at
    the close, which decision 2 leaves it for.
- **No CHANGELOG, README or ARCHITECTURE change.** None of them
  says which copies are the same.
