# Commit plan: round 2's work on layer 1, the conventions manual

## Summary — the state after all commits

The conventions manual is renumbered once, with no gap and no third
level, as the refinement's DECISION-9 chose
(`temp/refinement-2026-10-18.md`, *Round 2*). Its old §1, what a
convention is, has moved to the idea-to-output model, as ADR-0063
decision 7 left for round 2.

- **The model** holds what a convention is: a description, its
  manual, and the approaches made from it, its artifacts; and what
  a convention asserts, a rule and not a method (ADR-0031). It is
  general, so any repo can adapt it. Its labelled parts are
  numbered: §3's links and its rule for a disagreement, §4's Down
  and Up (FINDING-180).
- **The conventions manual** stands on the model, in frontmatter of
  its own. What of its old §1 belongs to this repo stays in it: the
  manual's path, the kinds of artifact and where they live.
- **Its numbers:**
  - §1 the artifact: 1.1 how a rule is written, 1.2 a skill's
    frontmatter, 1.3 the `foundation` line, 1.4 stages
    (FINDING-138);
  - §2 the manual: 2.1 to 2.9, one part for each section of the
    form (FINDING-136). The body's layout rules are §2.5's
    (FINDING-137). The lesson taken is §2.6;
  - §3 adding a convention.
- **One subject per section.** §2 no longer tells the channel,
  which *Why it arrives this way* holds, or the open question of a
  shape, which the TODO item "Decide whether our own forms become
  shapes" holds and which both manuals name (FINDING-137, 143). §2.5
  points at facts-in-sync §3 for when a section gets a number
  (FINDING-135).
- **The `foundation` line has one home** for which files carry it
  and what each holds: conventions §1.3. Facts-in-sync §4 step 2
  and exchange §3.5 point at it (FINDING-141).
- **The manual's lessons are dated italics,** and its history
  sentence is gone (FINDING-139, 140).
- **A footer line names the section it backs,** unless it backs the
  whole file (§1.1, FINDING-142), and the footers in both seats
  follow.
- Every living pointer into either text lands where its fact now
  is: the manual's 28, as DECISION-9 counted them, and the model's
  13, 7 of them in TODO.
- `docs/conventions/README.md`'s "The chain" is "The hand-off", so
  "chain" means one thing, the model's. *The words* defines
  "model" and "convention".
- ADR-0066 records the move and the renumbering ADR-0065 rejected,
  taken now for a change of form.
- The refinement's file names each fixed finding's commit. TODO's
  "Move conventions §1 to the idea-to-output model" goes; its idea
  of a `requires` grep in the walk moves to "Decide which way a
  fact reference may point".

## Commits

**0. `docs(agent): add commit plan for layer 1's work`**
Opens the set.

**1. `docs: PLAN's step enters round 2's work`**
The Now line still says round 2 reads next. Round 2 has read and
decided. A record, apart from the set's records commit, because it
is true now.

**2. `docs: ADR-0066 the conventions manual renumbered`**
Proposed. The move of §1 to the model, the manual standing on it,
the one renumbering, and the `foundation` line's one home. Rejected:
a gap (ADR-0065's choice), `### 3.3.1` parts, new numbers after
§3.7, two conventions.

**3. `docs: number the model's labelled parts`**
FINDING-180. §3's bold parts and §4's Down and Up become numbered
parts. The pointers to model §3 for a disagreement (agent model,
tiers model, facts-in-sync) move to its part. Before commit 4, so
the new section lands in a numbered model.

**4. `docs: the model says what a convention is`**
A new model section, "A convention", after §5, "A model and a
concept"; §6 and §7 become §7 and §8. Nothing points at those two.
The conventions manual's §1 leaves. What belongs to this repo goes
into §2 and §3 as their opening paragraphs. The manual gains
`foundation: the idea-to-output model`. `ARCHITECTURE.md`'s two
pointers to conventions §1 move: to the model, and to exchange §3.2
for "a manual never ships". The foundation check runs on both
descriptions. The gap at §1 lasts one commit.

**5. `docs: renumber the conventions manual once`**
§2, §3, §4 become §1, §2, §3, with the parts in the Summary.
FINDING-135, 136, 137, 138, 140 and 143's two lines, here and in
shapes. Every living pointer outside `.claude/` moves in this
commit (`docs/conventions/facts-in-sync/` §3). The sweep greps
every old number at once, the text unwrapped.

**6. `chore(agent): point at the renumbered manual`**
`convention-manual.md`, `approach-evaluation.md`,
`refinement.md`: their pointers. The rule's comment and items 5 to
7 checked against §2's new parts. Agent files, next after 5.

**7. `docs: give the foundation line one home`**
FINDING-141. §1.3 says which files carry the line and what each
holds. Facts-in-sync §4 step 2 keeps what the line is for, the
root, and points at §1.3. Exchange §3.5 and *The words* already
point and move to §1.3.

**7b. `chore(agent): the foundation check points at §1.3`**
If commit 7 moves the fact `foundation-check.md` step 1 cites.
Provisional: only when it does.

**8. `docs: date the conventions manual's lessons`**
FINDING-139. Three cases: each becomes a dated italic, or goes when
no date is found in the devlog or the ADRs.

**9. `docs: a footer line names the section it backs`**
FINDING-142. One line in §1.1.

**9b. `fix(delivery): shipped footers name their section`**
**9c. `chore(agent): our footers name their section`**
Provisional: the footers in each seat read against the new line,
the master first. Only lines that back one section change. A skill
both seats hold is two commits. Their count and wording are known
only once read.

**10. `docs: rename the index's chain to the hand-off`**
`docs/conventions/README.md`'s heading and its two uses; the
pointers in the conventions and commit-plan manuals and TODO's
local-map item. Conventions §1.2's "lands a convention together
with its chain" says what it means: what it requires.

**11. `docs: The words define model and convention`**
`ARCHITECTURE.md`'s *The words*: two entries, each pointing at the
model.

**12. `docs: round 2's layer 1 is worked`**
The records commit. ADR-0066 Accepted. The refinement's file:
FINDING-135 to 143 and 180 name their commits. TODO: the §1-move
item goes; its `requires` idea moves to "Decide which way a fact
reference may point".

**13. `docs(agent): close commit plan for layer 1's work`**
Deletes this file; the body says what diverged.

## Decisions for you to object to

- **An ADR, 0066.** ADR-0065 rejected the renumbering; ADRs are not
  edited, so taking it now needs its own record. DECISION-9 holds
  the reason today, but the refinement's file goes at the step's
  close.
- **The conventions manual stands on the model.** Its subject, a
  convention, is the idea the model now states. That is what model
  §4 asks after a birth, and what agent-arrangement does with the
  agent model.
- **What a convention asserts moves too.** ADR-0063 moves §1 whole,
  and the claim is general: any repo's conventions make it.
- **The `foundation` line's home is conventions §1.3,** not
  facts-in-sync. The line is this convention's artifact, its *What
  this is made usable as* says so, and §2 already lists each
  kind's value. Facts-in-sync keeps what the line is for.
- **No italic for the old numbers** (FINDING-140). Its fix was a
  dated italic for a kept gap; with no gap, nothing is kept. Git
  keeps the old numbers, and history cites what was true then.
- **The footers are fixed here,** not in layers 5 and 6, so
  FINDING-142 is fixed whole and no trigger waits unseen.
- **The `requires` grep moves to the direction item.** It adds a
  grep to facts-in-sync's walk, a rule round 2 reads against. The
  direction item already weighs `requires` as a sideways link, and
  is due between rounds 2 and 3.
- **"The hand-off" for the index's heading.** The index says the
  conventions "hand to each other". A plainer name, with no second
  meaning.
