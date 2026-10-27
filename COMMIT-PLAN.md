# Commit plan: round 2's work on layer 6, `delivery/`, what ships

## Summary — the state after all commits

Round 2's fixes for layer 6 have landed: what ships to a run, and
the delivery's own map. Of the layer's 30 findings, 17 are fixed
here, in whole or in part (`temp/refinement-2026-10-18.md`, *Round
2*). The rest were ended earlier: 11 moved to TODO items, 205 and
221 declined. The run's copies are written for a run (ADR-0069).

- **`delivered-copies.md`** says what a footer is and how a run
  goes against one (FINDING-199), and keeps only the run's half of
  the exchange: rule 4 keeps the three verdicts, and rule 1 no
  longer holds part of rule 2's subject (FINDING-215).
- **The container:** its entry file stops restating the order of
  questions (FINDING-214); `visual-comparison` §5 is written for a
  run (ADR-0069), and the skill states in its body that "one obvious
  answer" means a clear answer, in both seats' copies (FINDING-222).
- **Retellings point:** the container README's count of chapters,
  `infra-establish`'s runtime ground lines and `cbc-slice`'s
  Invariants columns point at their sources (FINDING-217); the
  plain-words page names its owners by path (FINDING-218); four
  pointers into another skill give root paths (FINDING-219).
- **The playbook** states its rule for a *For run <n> only* list in
  general (FINDING-206, in part). Its version does not move: a fix is
  not a fold.
- **The seed** reads the playbook's version from its line
  (FINDING-200), and points at exchange §3.2 for what is pinned,
  with no counts (FINDING-201).
- **The method:** the worked example's two copies have an owner,
  `cbc-framing`'s (FINDING-212); `cbc-slice`'s stages share one
  heading level (FINDING-225); two shapes list what they leave out
  once (FINDING-226).
- **The stack:** `cbc-bootstrap`'s walkthrough owns each trap and the
  ground's authority split (FINDING-209, 210); three template
  comments give full paths (FINDING-207, in part); two texts stop
  calling the container's README a stub.
- **`delivery/README.md`** points at the playbook for its steps
  (FINDING-213).
- The refinement's file names each layer 6 finding's ending, and
  round 2's work is done.

## Commits

**0. `docs(agent): add commit plan for layer 6's work`**
Opens the set.

### The container

**1. `fix(delivery): delivered-copies explains footers`**
FINDING-199. Rule 1 gains one sentence: a footer names the
decisions a copy rests on, and to go against one, the run quotes it
under *To the deliverer*. The footers stay.

**2. `fix(delivery): delivered-copies is the run's half`**
FINDING-215. The header says the deliverer's side is not here, yet
rule 4 tells our read; rule 4 keeps the three verdicts the run acts
on. The part of rule 2's subject that rule 1 holds moves to rule 2.

**3. `fix(delivery): the entry file stops restating`**
FINDING-214. "It is not restated here", then a parenthesis restating
the order of questions without "world": the parenthesis goes.

**4. `fix(delivery): visual-comparison speaks to a run`**
ADR-0069 decision 1. §5's line on "the deliverer's Mermaid trial"
is written for the run's seat.

**5. `fix(delivery): visual-comparison states its rule`**
FINDING-222, the run's copy. §1's "one obvious answer" says in its
body that it means a clear answer, not a simple form; the case in §4
stays as its example.

**6. `chore(agent): visual-comparison states its rule`**
FINDING-222, our copy, the same rule written for our seat.

### What a newborn is given

**7. `fix(delivery): playbook states its run-only rule`**
FINDING-206, its fixed part. The rule for a list under *For run 5
only* is stated in general, for any run named. Run 5's lists stay,
for run 5's reading. The citations of run 3's RETRO are the plain
rewrite's. No version bump: the playbook bumps its version when a
harvest folds a lesson in, and this is a fix.

**8. `fix(delivery): the seed reads the playbook version`**
FINDING-200. The seed's three "v9" go: it reads the version from the
playbook's version line at birth.

**9. `fix(delivery): the seed points at exchange §3.2`**
FINDING-201. "Every pinned copy (`docs/conventions/exchange/`
§3.2)", with no counts. The prompt to the newborn keeps its counts,
and the seed's check compares them with the tree.

### The method

**10. `fix(delivery): the worked example has an owner`**
FINDING-212. `cbc-framing`'s copy owns; `cbc-slice-workflow.md`'s
header says its copy follows. The worked example itself is not
edited.

**11. `fix(delivery): cbc-slice's stages share one level`**
FINDING-225. Stage 0 to Stage 4 all at `##`, as conventions §1.4
asks of the skill it takes as its example.

**12. `fix(delivery): two shapes list exemptions once`**
FINDING-226. `evidence-test.md` and `kill.md` say what they leave out
under *What is exempt* only.

### Retellings and pointers

**13. `fix(delivery): three retellings point at sources`**
FINDING-217. The container README's "five chapters",
`infra-establish`'s five runtime ground lines, and `cbc-slice`'s
retelling of the Invariants columns each point at their source, a
file the run holds.

**14. `fix(delivery): the plain-words page names owners`**
FINDING-218. "The detailed docs" become their paths.

**15. `fix(delivery): pointers into skills give paths`**
FINDING-219, its four: `cbc-framing` and `infra-serve` name a file
in another skill by root path. The paths within a skill are the
fact-reference item's.

### The stack

**16. `fix(delivery): the walkthrough owns each trap`**
FINDING-209. Each trap told in two or three of `cbc-bootstrap`'s
files is told in the walkthrough; the skill and the harness
reference point at it, and the reference's "the lived traps live
here" goes. Provisional: the traps' split is read at the boundary.

**17. `fix(delivery): the walkthrough holds the split`**
FINDING-210. The ground's authority split, held in evidence runs,
moves from the harness reference to the walkthrough's step 4.

**18. `fix(delivery): template comments give full paths`**
FINDING-207, its three: comments naming `bootstrap.sql`,
`testcontainers.properties` and `verify-database-model.sql` by a
name that stops resolving once copied out give the path. The ten
headers stay, declined.

**19. `fix(delivery): the container's README is composed`**
Met in round 2, in files this plan opens: `cbc-bootstrap` and
`establishment-walk.md` call the container's README a stub;
`delivery/README.md` §4 says it ships a composed body.

### The map

**20. `docs: the delivery map points at the playbook`**
FINDING-213. `delivery/README.md` stops retelling the playbook's
steps and points at the playbook.

### Records and close

**21. `docs: round 2's layer 6 is worked`**
The records commit. The refinement's file: each of FINDING-199 to
228 names its ending, the moved ones their TODO items; round 1's
DECISION-3 names the shipped `writing.md` beside `one-home.md`
(FINDING-205).

**22. `docs(agent): close commit plan for layer 6's work`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A shipped
skill or rule stands on a manual or on practice; a commit that finds
its foundation disagreeing gets a lettered commit after it.

## Decisions for you to object to

- **No TODO trigger fires.** Two sit near this work:
  - "Decide how a run learns that the rule for taking deliveries
    changed" waits for a delivery to a run still building, with
    `delivered-copies.md` changed since its pin. Commits 1 and 2
    change that rule, so the next such delivery fires it.
  - "Decide how the worked example's two copies are kept" waits for
    the worked example's next edit. Commit 10 gives the pair an owner
    and leaves the example itself alone.
- **FINDING-206 lands without a version bump.** The finding said
  "in the next playbook version". The playbook's own header bumps the
  version when a harvest folds a lesson in, and a fix of its rule's
  form is no fold. Run 5's reading, which folds the next lessons,
  moves the version.
- **FINDING-222 is fixed in both seats here,** each copy for its
  seat, as ADR-0069 asks. Our copy is an agent file, so it has its
  own commit.
- **The worked example's owner and ADR-0069 do not meet.** ADR-0069
  is about the two seats' copies; the worked example's two copies
  sit in one seat, and `one-home.md` rule 5 makes one follow the
  other.
- **Round 2's met items in layer 6's files:**
  - fixed where a commit opens the file: the container README's
    "stub" claim (commit 19);
  - left: the container's `.gitignore` line on a `settings.json` it
    does not ship, and `system-readiness.md` against `cbc-slice` on
    where a red is taken: no commit opens them, so the last read
    takes them; the 29 mid-sentence `CBC ADR` citations and
    `cbc-framing-workflow.md`'s "so far": the plain rewrite and run
    5's reading; `apply-retrospective`'s labels: the fact-reference
    item.
- **Commit types:** `fix(delivery)` for what ships, `docs:` for
  `delivery/README.md`, which stays here.
