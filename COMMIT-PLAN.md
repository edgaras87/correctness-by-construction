# Commit plan: round 2's work on layer 3, the other manuals, the models, the concept

## Summary — the state after all commits

Round 2's fixes for layer 3 have landed. Of the layer's 35
findings, 31 are fixed here (`temp/refinement-2026-10-18.md`,
*Round 2*). The other four: FINDING-180 was fixed in layer 1; 181
and 183 were declined; 176 waits for layer 4, its home's layer
(`.claude/approaches-on-trial/refinement.md` §2.7).

- **Numbered parts.** Four sections that held several subjects in
  bold parts are numbered: facts-in-sync §3 (3.1 to 3.3),
  agent-arrangement §1 (1.1 to 1.3), commit-plan §2 (2.1 to 2.13)
  and shapes §1 (1.1 to 1.3). Agent-arrangement's every-session
  rule is a part of its own, §3.9. Every living pointer into them
  lands on the part it means.
- **The note is told once.** Exchange §3.7 holds the note, §6.6 a
  note without files. §6.7 is merged into §6.5. "One pin" sits
  with the pin, in §2.2.
- **Pointers name their homes.** When a rule loads: agent-
  arrangement §5.6. The one-home rule: facts-in-sync. The model's
  claims: `docs/models/agent.md` §12. Commit-messages' two rules:
  its §2. Where the concept lands: exchange §3.3.
- **Lessons are stated in general.** The exchange, shapes, the
  retrospective, commit-plan, facts-in-sync and visual-comparison
  each state a rule in the body; the dated italic keeps the case.
  Three live claims leave their italics. The agent model drops a
  dated line.
- **Summaries say they are summaries.** The retrospective's run
  seat, the conventions index, and *The words*' "approach".
- **Three TODO items name the moment they are due,** in place of
  "the next change" to a manual.
- The refinement's file names each fixed finding's commits.

## Commits

**0. `docs(agent): add commit plan for layer 3's work`**
Opens the set.

**1. `docs: three TODO triggers name their moment`**
Three items are due at "the next change" to a manual this plan
edits. Each has passed that trigger before, unworked. The counts
are of the manual's commits since the item was added:

- "Weigh three candidate rules for what makes a note land": 39
  exchange commits. New trigger: the note that answers run 5's
  reading, before it is written.
- "Say once that a reading's decisions are the reviewer's": 27
  agent-arrangement commits. New trigger: an agent found settling
  what was the reviewer's.
- "Decide how an edit or a new text is shaped": 2 writing-manual
  commits, `e2ad2e4` and `a6a9e03`; commit 9 would fire it again.
  New trigger: round 3's rule check, which reads the writing rules
  anyway (`.claude/approaches-on-trial/refinement.md` §2.3).

First, so no later commit fires them.

### Layout first: the sections others point at get their numbers

**2. `docs: number facts-in-sync §3's parts`**
FINDING-175. §3.1 the fact reference; §3.2 a section's labelled
parts are numbered; §3.3 the grep when a commit renames or
renumbers. The numbering rule stays here: conventions §2.5 already
points at it (FINDING-135). The pointers outside `.claude/` move to
the part they mean: `ARCHITECTURE.md`, the conventions manual,
TODO, and the manual's own bare "(§3)". The sweep greps every old
"§3", path and bare, unwrapped.

**3. `chore(agent): point at facts-in-sync's new parts`**
`convention-manual.md`, `one-home.md`, and `foundation-check.md`,
its comment and *A moved section*. Agent files, next after 2.

**4. `docs: number agent-arrangement §1's parts`**
FINDING-151. §1.1 the closed list of paths; §1.2 detachable;
§1.3 not records. Commit-messages §2's pointer moves to §1.1.

**5. `docs: the every-session rule has its own part`**
FINDING-150. A new §3.9, last, so §3.3 to §3.8 keep their numbers.
§3.2 keeps the rules directory. Its first sentence points at §5.6
and stops retelling it. Its list of the container's four rules
goes: the run's seat lists them. That list holds one of
FINDING-149's two lines, which goes with it. The pointers that mean
the every-session rule move to §3.9: the writing manual's and
facts-in-sync's *Why it arrives this way*.

**6. `docs: number commit-plan §2, the sweep a part`**
FINDING-172. §2's 13 bold bullets become §2.1 to §2.13, since
facts-in-sync §3.2 numbers every part of a section's form. The
sweep's part also says what only the skill said: the sweep runs
again before the close. Facts-in-sync §3.3 points at that part.
The skill, in both seats, is checked against it. TODO's "Decide
whether each seat's copy is written for its seat" drops its sweep
Idea, which this answers.

**7. `docs: the exchange tells the note once`**
FINDING-159 and 160. "One pin" moves from §3.5 to §2.2, the pin's
home. §3.7 stays the note's home. §6.6 holds a note without files,
and §2.5 points at it. §6.7 merges into §6.5 and goes; nothing
points at it. FINDING-162's last part: shapes' and TODO's pointers
for one pin move to §2.2.

**8. `docs: number shapes §1's parts`**
FINDING-166. §1.1 what a shape is; §1.2 how one is born; §1.3
before one is written. The pointers to §1 move: the conventions
manual, TODO's three, and shapes' own two. `.claude/decisions.md`'s
is history (DECISION-13).

### Then the pointers

**9. `docs: point at §5.6 for when a rule loads`**
FINDING-154. Agent-arrangement §5.6 holds when a rule loads and its
limits. The conventions manual's and the exchange's *Why it arrives
this way*, and shapes' *What this does not cover*, point there in
place of §3.2. The writing manual states it with no reference, and
gains one. TODO points at §5.6 in place of `.claude/decisions.md`,
and its stale "only on a Read" goes (met in round 2).

**10. `chore(agent): point at §5.6 for when a rule loads`**
The comments of `convention-manual.md`, `exchange-reading.md` and
`foundation-check.md`.

**11. `docs: agent-arrangement names its sources`**
FINDING-149 and 153. *What the difference is* names facts-in-sync
as `one-home.md`'s convention. "Model claim M1" and "A2" name
`docs/models/agent.md` §12.

**12. `docs: point at commit-messages §2 by path`**
FINDING-173. Two rules are commit-messages §2's: an agent file
never shares a commit, and a commit waits for the word.
Facts-in-sync §4 step 3 and the commit-plan manual add the section.
TODO names the path. `PLAN.md`'s step form and the open step's
close items gain the reference.

**13. `chore(agent): point at commit-messages §2 by path`**
`foundation-check.md` step 5, and `working-a-reading.md`.

**14. `docs: pointers name the section they mean`**
FINDING-162's first and third parts. Facts-in-sync's run seat names
exchange §6. The visual-comparison manual names shapes §4.3 for the
pictures' rule.

**15. `chore(agent): the entry file's comment cites §2.6`**
FINDING-162's second part. `CLAUDE.md`'s comment says the file
loads on every task: agent-arrangement §2.6. It keeps §2.4 for the
three tests.

### Then the lessons: the body states the rule, the italic keeps the case

**16. `docs: the exchange states its lessons in its body`**
FINDING-155, 156 and 157. §3.7's body states the three rules about
verdicts; the italic keeps the case of 2026-09-20. §6.3's body says
a reading asks what the run teaches the worked example. The cases
in §3.1 (two), §4 step 4 and §5.1 become dated italics, dated from
the devlog, or go. §5.4's stays, declined as an example.

**17. `docs: live claims leave the dated italics`**
FINDING-158. Exchange §3.4's owed fill, repo-hygiene's open
overlay, and the retrospective's "Reopened if" move into their
bodies. An italic reads as history, and these say what is true
today.

**18. `docs: shapes states its lessons in its body`**
FINDING-163, 164 and 165. §1.1: when an output opens, extends and
closes is its owning convention's. §1.3: a shape catches a part
missing, not a part that lost half its meaning. §4.3: the pictures
never carry a fact alone. The italics keep their cases.

**19. `docs: the retrospective states its rules generally`**
FINDING-167 and 168. §3 gains two bullets from its italic: tests
are counted from this run's reports only; a tool that edits text is
checked on what it must not touch. §1 says in general why lessons
are applied before Release; run 3 moves to a dated italic.

**20. `docs: the retrospective's summary says it is one`**
FINDING-169 and 170. The run's seat says its list sums up the
skills, which stand on this manual. *Why it arrives this way*
points at §1 for the two steps.

**21. `docs: commit-plan's reasons stand in general`**
FINDING-171. §2.4, material-first, states its reason in general;
the seed's third run moves to a dated italic. §2.6's Step 10
session joins that part's italic.

**22. `docs: facts-in-sync names what enforces its walk`**
FINDING-174. §4 says what enforces steps 3 to 5 today, the
foundation check. The two checks run by hand go to a dated italic.

**23. `docs: the render decides, for a general reason`**
FINDING-177. Visual-comparison §2 gives one general reason. The
Mermaid case stays as its example.

**24. `docs: agent-arrangement tells its rename once`**
FINDING-152. §2.3 drops "which one run showed to be a pure rename".
*What it is for* keeps the case.

**25. `docs: the agent model drops a dated line`**
FINDING-182. "Added 2026-10-24." goes: a description states what is
true today (`docs/conventions/facts-in-sync/` §4).

### Last, one home

**26. `docs: the concept's landing is told once`**
FINDING-161. Exchange §3.3 is the home, and says so already.
`delivery/README.md` §1 and §3 and `delivery/installs/pure-seed.md`
point at exchange §3.3 and §3.2 by root paths, in place of their
retellings and bare names.

**27. `chore(agent): exchange-deliver cites exchange §3.3`**
The skill keeps its command, and cites §3.3 in place of "this is
the one line that says so".

**28. `docs: the conventions index keeps to relations`**
FINDING-178. The index keeps who hands to whom. Its retellings go:
commit-plan's "plans the commits, not the change",
visual-comparison's boundary, each convention's "fires when", each
domain skill's order. TODO's "Make the conventions index a full
local map" drops its Idea about the retold triggers, which this
takes.

**29. `docs: The words' approach points at the model`**
FINDING-179, "approach". *The words* keeps its plain definition and
points at `docs/models/idea-to-output.md` §2, as its "model" and
"convention" entries do. The model is unchanged. "Description"
stays in TODO's ARCHITECTURE item.

### Records and close

**30. `docs: round 2's layer 3 is worked`**
The records commit. The refinement's file: each fixed finding names
its commits, and FINDING-176 says it moved to layer 4.

**31. `docs(agent): close commit plan for layer 3's work`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A commit
that changes a manual walks what stands on it
(`docs/conventions/facts-in-sync/` §4). A derived file that then
disagrees gets a lettered commit after it: the shipped master
first, `fix(delivery)`, then our copy, `chore(agent)`. Most likely
after 6 (`commit-plan`), 7 and 16 (the exchange's skills and
rules), 18 (`shapes-lifecycle.md`), 19 (the retrospective's two
skills) and 23 (`visual-comparison`).

## Decisions for you to object to

- **The three fired items are retriggered, not worked** (commit 1).
  Each would add a rule, and this round places text; it adds no
  rules. A trigger of "the next change" to a manual fires at every
  pointer fix, so it was passed each time unnoticed. Each new
  trigger is the moment the item's answer would first be used.
- **FINDING-176 waits for layer 4.** DECISION-14 put the bump
  rule's home in `CHANGELOG.md`'s comment, a layer 4 record, and a
  fact is fixed with its home's layer
  (`.claude/approaches-on-trial/refinement.md` §2.7). Layer 4 opens
  with the ARCHITECTURE item, which may reshape §1.1, the other end
  of the move.
- **FINDING-179's direction is reversed.** Its ending had the model
  point at *The words*. Layer 1 did the opposite for "model" and
  "convention": *The words* points at the model. A model is written
  for any repo, so it should not point at this repo's
  ARCHITECTURE. If you keep the ending, commit 29 edits the model
  instead.
- **Commit-plan §2 is numbered whole, 13 parts,** so the sweep can
  be one. The rule numbers every part of a section's form, not one.
- **The order: layout, pointers, lessons, one home.** The four
  sections are numbered before anything new points at them, so each
  pointer is fixed once, and each renumbering is swept once.
- **One plan, 31 commits.** Each fix is small. Splitting into plans
  would add an open and a close commit per plan, and no subject
  needs a plan of its own.
- **No ADR.** Each fix is a finding's ending, decided in the
  refinement's file.
- **The local-map item stays due.** Its map is new work, not a
  refinement; commit 28 takes only its retold-triggers Idea.
- **Round 2's met items, the ones of other kinds,** are fixed where
  a commit opens their line: TODO's "only on a Read", in commit 9.
  `one-home.md` rule 3's example rests on the ARCHITECTURE item, so
  it waits for layer 4, though commit 3 opens the file. The rest
  wait for layers 5 and 6, or the last read.
