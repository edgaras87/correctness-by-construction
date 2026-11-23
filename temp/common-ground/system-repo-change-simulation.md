# A System Repo's Copy Change, Simulated

<!-- A draft of the knowledge work (ADR-0082). It simulates the cases
     of a System Repo's Copy Change, step by step, and keeps how each
     rule was chosen: each step's options, why the others were not
     taken, and how today's ways compare. The rules, the cases and
     what is open are the layers document's, and each step points
     there (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.2, How a
     change travels). Depth c is simulated here first, then brought
     there (TODO.md, the item "Simulate depth c, then bring the
     Change idea to it"). Its input: the
     frozen temp/common-ground/between-repos-simulation.md, §5.2, *Work in a System
     Repo*, and §5.3, *Reading a System Repo*. It goes once what it
     holds has landed in the rewrite into the layers model, and git
     keeps every version. -->

This document simulates the cases of a System Repo's change (§2), step by step, and keeps how each rule was chosen. The rules are the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2, *How a change travels*). One case is simulated through every step: a System Repo changes one Adapted Case, and the System Kit takes the Copy Change: its Adapted Case changes (depth b, §5). The other cases are checked against it (§2). It uses the Defined Terms of the layers document and of the Common Ground Problem (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §2, *The layers*; `temp/common-ground/common-ground-problem.md`, *Defined Terms*).

It shortens ten Defined Terms to their last two words, as the layers document does, in its table (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §2, *The layers*).

The scope of that case: a Copy Change may touch the Adapted Understanding Text, an Instruction Text built on it, or both, in either order. Its reason may be the System Repo's own, or one any repo would meet. A stretch of work may hold several Copy Changes (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *The cases*). No fixed example is used: each step's choice must hold at each end of this scope.

## 1. How it is worked

Three moves, in order:

1. **Simulate:** each step below says what must happen, what could be done, and what is chosen.
2. **Read the rules together:** once all of a part's steps are seen together, their choices are read as one: they are the part's rules, written out in the layers document's §3.2.
3. **Check them:** each step is walked again against the rules. A step a rule does not hold for changes the rule or the step.

The steps make six parts. Who does each, and how they make one movement, are the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2, *How a change travels*):

| Part | Steps |
|---|---|
| Change a Kit Copy | §3, steps 1–2 |
| Read Copy Changes | §4, steps 1–4 |
| Judge Copy Changes | §5, steps 1–2 |
| Act on the verdicts | §6, step 1 |
| Deliver the Kit Update | §7, steps 1–2 |
| Take the Kit Update | §8, step 1 |

Each step has these fields. A field with nothing in it is left out.

- **Options:** what could be done here, today's way among them.
- **Chosen:** the option taken, and why the others were not.
- **Its rules:** where the rules it led to are written, in the layers document's §3.2.
- **Today:** what is borrowed from today, and what changes, each with its source. Today's things keep today's names, such as the Delivery Note.

A step simulated anew also says what must happen, which Adapted Case runs it, and what it leaves open, each with its trigger, until its part is read together and they move to the layers document.

## 2. The cases

The cases are simulated one at a time. The first is simulated whole; each other case is then checked against it, and what differs is written. A case that grows too complex goes to TODO, to be checked once the Common Ground Problem is finished. The cases themselves, what is known but not ruled, and the other sources are the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *The cases*).

**The whole flow.** The six parts of §1 and the depths of the layers document's table of cases (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *The cases*), in one picture. It is a summary: the layers document's §3.2 holds the facts, and each § in the picture names the section of this document that weighed them.

```
 System Repo               ┆ Maintainer Repo
 ───────────               ┆ ───────────────
                           ┆
 1. Change a Kit Copy ─────┼── reads; writes nothing there ──▶ 2. Read Copy Changes ──▶ 3. Judge Copy Changes ──▶ 4. Act on the verdicts
    §3                     ┆                                   §4                       §5                        §6
                           ┆                                                                                      │
 6. Take the Kit Update ◀──┼── writes only into its temp/ ──── 5. Deliver the Kit Update ◀────────────────────────┘
    §8                     ┆                                   §7

 How high each depth goes: 3. Judge Copy Changes sets it, 4. Act on the verdicts changes it

 depth                          b        c, at 2   c, at 1   d         e         f
                                         └─────────── not yet checked ────────────┘
 layer 1  Backbone Idea                            ●
 layer 2  Problem Domain Idea            ●         ●         ○         ○
 layer 3  Adapted Case          ●        ●         ●         ●         ●
 layer 4  a System Repo's work  ●        ●         ●         ●         ●         ●
 ───────────────────────────────────────────────────────────────────────────────────────────
 highest layer                  3        2         1         3, or 2   3, or 2   none, open
```

At every depth, 5. Deliver the Kit Update brings a Kit Update down.

Key: ● is the Copy Change's path, from its Kit Copy up to the highest layer it changes. ○ is "or up to here", when the case asks it (that table, rows d and e). The line after the picture follows the layers document's arrows (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2, *How a change travels*). A § is a section of this document.

## 3. Change a Kit Copy

Two steps:

1. A Kit Copy is changed, with its Change Record.
2. The gate of the System Repo's Plan Step decides each Copy Change.

**Step 1. A Kit Copy is changed, with its Change Record.**

- **Options:**
  - a. the Kit Copy is changed when the work shows it does not fit, and its Change Record written with it;
  - b. the Kit Copy is changed ahead, for what the agent foresees;
  - c. the misfit is noted, and the Kit Copy changed at the gate of the System Repo's Plan Step;
  - d. the Kit Copy stays as it is, and the System Repo writes what it does instead in its own records.
- **Chosen:** a. The others:
  - b is a speculation, with nothing that happened behind it;
  - c gains nothing by waiting. A Change Record lets any Copy Change be edited or reversed later. And until the gate, the Kit Copy would say what the System Repo no longer does;
  - d leaves the Kit Copy saying it for good, and the next agent reads the Kit Copy, not the System Repo's records.

  **Weighed and dropped:** a check at each session's end, comparing the Kit Copies with their Change Records. It would run every session, needs an Adapted Case of its own, and never runs when a session stops with no warning. The commit's check and the gate's comparison (step 2) cover what it would find. It comes back if a gate finds a Copy Change committed in an earlier session with its Change Record missing or wrong.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.1, *Change a Kit Copy*).
- **Today:**
  - borrowed: an edit comes from something that happened, never a speculation (`delivery/container/.claude/rules/delivered-copies.md`, rule 2; `docs/conventions/exchange/` §5.1, *When a copy may be edited*);
  - borrowed: the rule for changing a copy loads when a copy is touched (`delivery/container/.claude/rules/delivered-copies.md`, its `paths:`);
  - borrowed: the Change Record names which work found the Copy Change, as a Decisions Log entry names the CBC Run's Plan Step (`delivery/container/.claude/rules/delivered-copies.md`, rule 2);
  - changed: today d is required when the need is the CBC Run's own: "never this CBC Run's own answer", and what only it needs goes in its records (`docs/conventions/exchange/` §5.1). So today forbids an edit for the System Repo's own reason. Here the System Repo makes it; what becomes of it at the Update Take is not ruled (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *Known, not ruled*);
  - changed: today nothing is written into a copy but the edit, since "a file says how to use it, never its own history", and the why goes in the Decisions Log (`docs/conventions/exchange/` §5.1). Here the why goes in the Kit Copy's Adapted Understanding Text, which is not read while working;
  - changed: today every edit must claim to be for any CBC Run. Here the System Repo proposes, and the Maintainer Repo judges;
  - borrowed: a check fires at the commit because, before, it had to be remembered (`.claude/rules/foundation-check.md`, its header comment). That one is the Maintainer Repo's own.

**Step 2. The gate of the System Repo's Plan Step decides each Copy Change.**

- **Options:**
  - a. the gate looks at the step's Copy Changes together: the comparison, a decision on each, and the links;
  - b. the gate only checks that each Copy Change has a Change Record that says it, and decides nothing;
  - c. the gate does nothing with Kit Copies: the Maintainer Repo reviews the Copy Changes when it reads them;
  - d. the gate writes one line per changed Kit Copy, asking the Maintainer Repo to read it.
- **Chosen:** a. The others:
  - b keeps a Copy Change made early in the step, though the end of the step may show it wrong, and leaves Copy Changes with one reason unlinked;
  - c leaves the review to the side that cannot see what happened, and a wrong Copy Change then reaches the Maintainer Repo's judging;
  - d adds nothing to the Change Records: Read Copy Changes compares every Kit Copy, and reads the Change Records. It comes back if Read Copy Changes misses a changed Kit Copy because nothing asked it to look.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.1, *Change a Kit Copy*).
- **Today:**
  - borrowed: the gate is a list of outcomes checked at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: each Approach on Trial the CBC Run's Plan Step used has its dated note at the close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). A Change Record checked at the gate is the same shape;
  - changed: today the close writes one CBC Run Ask per edited copy (`delivery/container/.claude/rules/delivered-copies.md`, rule 4), option d. Here the Change Records are what Read Copy Changes reads;
  - changed: today nothing at the close looks at the step's changes to copies together.

## 4. Read Copy Changes

Four steps:

1. The stretch of work ends, and the Maintainer Repo is told.
2. The Maintainer Repo finds the two snapshots it compares.
3. It compares the Kit Copies, and reads each Change Record.
4. It lists what changed, nothing judged.

**Step 1. The stretch of work ends, and the Maintainer Repo is told.**

- **Options,** for where a stretch ends:
  - a. at any commit, the System Repo's latest;
  - b. at the gate where one of the System Repo's Plan Steps closed, the last one on main.
- **Options,** for how the Maintainer Repo learns:
  - c. the human tells it, and its Repo Register is marked by hand;
  - d. the human names a System Repo, and the agent compares its main with its *settled snapshot*. Every System Repo's main is compared with its *settled snapshot* when the human asks which have new work;
  - e. only when work resumes in the System Repo, by the fixed order: a Look for Lessons, then the Kit Update.
- **Chosen:** b and d. The others:
  - a reads Copy Changes the gate has not yet looked at, which the System Repo may still edit or reverse (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.1, *Change a Kit Copy*);
  - c depends on the human remembering, and the Repo Register then says a System Repo has nothing new when it has new work (Failure Case 2);
  - e alone gives no Look for Lessons to a System Repo whose work does not resume, so what it learned is lost (Failure Case 1). The Look for Lessons when work resumes still runs, as d: the human names the System Repo to update, which starts a Look for Lessons (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.5, *Deliver the Kit Update*).
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2, *Read Copy Changes*).
- **Today:**
  - borrowed: a CBC Run's Plan Step reaches main by fast-forward at its close, on the reviewer's word (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*);
  - borrowed: the Maintainer Repo keeps where each System Repo lives (`ARCHITECTURE.md` §2.5, *The CBC Runs*);
  - changed: today the state of the list of CBC Runs, such as "through Release, not yet read", is written by hand (`ARCHITECTURE.md` §2.5). Here it is found by comparison when asked;
  - changed: today a CBC Run Reading runs to the CBC Run's `HEAD`, and names work not yet committed (`.claude/skills/exchange-read/SKILL.md`, Stages 2 and 3). Here a Look for Lessons runs to main, and work past it waits.

**Step 2. The Maintainer Repo finds the two snapshots it compares.**

- **Options,** for where the last stop is kept:
  - a. in the System Repo, carried there by the next Kit Update;
  - b. in the Repo Register, the *settled snapshot*'s commit beside where each System Repo lives;
  - c. in the Maintainer Repo, as the first line of each Repo Reading, every Repo Reading kept.
- **Chosen:** b. The others:
  - a fails when a Look for Lessons has no Kit Update after it, which step 1 allows, since one may come between two resumptions of work: the System Repo still holds the old stop, and the next Look for Lessons finds again what was judged;
  - c keeps every Repo Reading for good, only for its first line.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2, *Read Copy Changes*).
- **Today:**
  - changed: today the stop is written first, as the Repo Reading's first line, before anything is read (`.claude/skills/exchange-read/SKILL.md`, Stage 2). Here it is taken when the Look for Lessons begins, and the Repo Reading names it when it is written;
  - borrowed: the Repo Register keeps where each System Repo lives, as today's list of CBC Runs does (`ARCHITECTURE.md` §2.5, *The CBC Runs*). It gains the *settled snapshot*;
  - borrowed: a CBC Run Reading is a draft in `temp/`, deleted once the work that needed it is done (`temp/README.md`; `.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today the stop, the Read-Through Commit, is kept in the CBC Run, carried there by the next Delivery Note, because "it is the only place the Concept Deliverer can look" (`docs/conventions/exchange/` §2.2, *The CBC Run*). Today every CBC Run Reading is followed by a delivery, so the stop always arrives. Here a Look for Lessons may have no Kit Update after it;
  - changed: today a CBC Run is born with its Read-Through Commit written as *none*, and the exchange-read Agent Skill names no span for it (`delivery/installs/pure-seed.md`, step 2). Here birth writes the start as the *settled snapshot*, and the first Look for Lessons starts there.

**Step 3. The Maintainer Repo compares the Kit Copies, and reads each Change Record.**

- **Options,** for how Copy Changes are found:
  - a. each Kit Copy compared between two snapshots of the System Repo's own: the older one and the stop;
  - b. each Kit Copy compared with the Kit Version the Kit Copies came from;
  - c. only the Change Records read, with no comparison;
  - d. the commits between walked one by one.
- **Chosen:** a. The others:
  - b finds the same as a at the first Look for Lessons after birth or an Update Take. After it, a Copy Change already judged differs from that Kit Version until the next Update Take, and is found again at every Look for Lessons before it;
  - c misses a Copy Change with no Change Record, which the commit's check should have stopped, but which can still land (Failure Case 22);
  - d shows every edit on the way, and Copy Changes the gate reversed. The gate has settled those (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.1, *Change a Kit Copy*); what stands at the stop is what is read.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2, *Read Copy Changes*).
- **Today:**
  - borrowed: every item is read from the copies' diff, the whys, and the lines to the Concept Deliverer (`docs/conventions/exchange/` §6.1, *Reading a CBC Run*; `.claude/skills/exchange-read/SKILL.md`, Stage 3). Here the whys are in the diff, and nothing else is sent to the Maintainer Repo, so it is one: the diff;
  - borrowed: the CBC Run is only read, never written (`.claude/skills/exchange-read/SKILL.md`, *Gates*);
  - changed: today the diff runs against what was delivered, the Receipt Branch or the last delivery entry (`.claude/skills/exchange-read/SKILL.md`, Stage 3). That works because a Delivery Take makes every copy equal its original again. Here a Look for Lessons may come before the Update Take, while a Kit Copy still holds Copy Changes already judged;
  - borrowed: a Receipt Branch holds the delivery as it arrived, and makes the next diff exact (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 4). The *version snapshot* does the same after an Update Take;
  - changed: today the whys are read from the Decisions Log. Here they are read from the Change Records, in the Kit Copies.

**Step 4. It lists what changed, nothing judged.**

- **Options:**
  - a. one line per Copy Change, nothing decided; judging is §5's;
  - b. each Copy Change judged as it is listed;
  - c. only the Copy Changes the System Repo proposed as any repo's are listed;
  - d. one line per Kit Copy, its Copy Changes summed.
- **Chosen:** a. The others:
  - b judges before the whole list is seen, so Copy Changes with one reason are judged apart, and each verdict tends to follow the System Repo's proposal (Failure Case 20). Listing is cheap and judging is not, so the list is checked whole first;
  - c takes the proposal for the verdict, and a lesson for every repo stays in one System Repo (Failure Case 20);
  - d merges two Copy Changes to one Kit Copy, and one of their reasons is lost.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2, *Read Copy Changes*).
- **Today:**
  - borrowed: one line per item, what it is and where, nothing decided (`.claude/skills/exchange-read/SKILL.md`, Stage 4 and *Gates*);
  - borrowed: the Repo Reading is a draft to its form (`.claude/rules/exchange-reading.md`);
  - changed: today a line is one per edit, per CBC Run Ask and per finding, read from three places (`.claude/skills/exchange-read/SKILL.md`, Stage 3). Here a line is one per Copy Change, with its Change Record;
  - changed: today the proposal is not asked for: every edit must claim to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each line carries it, as input to judging.

## 5. Judge Copy Changes

§5 to §8 are simulated first for depth b, the System Kit's Adapted Case changing: the shortest path into the System Kit through every step. Depth c, the idea above changing, at either layer, is then checked against them (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *The cases*).

Two steps:

1. The list is judged.
2. The verdict is written.

**Step 1. The list is judged.**

- **Options,** for who judges:
  - a. the agent proposes each answer, with what it read, and the human decides each line;
  - b. the agent judges, and the human looks only at the lines where the agent disagrees with the System Repo's proposal;
  - c. the human judges alone.
- **Options,** for a line marked "no entry":
  - d. judged from the comparison alone;
  - e. held, until the human brings its why from the System Repo;
  - f. its why looked for in the System Repo first, in the commit that made the Copy Change and in the System Repo's records, then asked of the human. The line says where its why was found, and is held while neither gives it.
- **Chosen:** a and f. The others:
  - b lets the agent's agreement with the proposal pass unchecked: two views agreeing is not a verdict (Failure Case 20);
  - c leaves the human to read every text the questions need, which the agent reads faster, and with nothing written down to check;
  - d judges on a guess at the why (Failure Case 22);
  - e asks the human for what the System Repo may already have written.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.3, *Judge Copy Changes*).
- **Today:**
  - borrowed: the four questions, from the rules on deciding written in the problem file before this simulation. They leave how each is answered, and by whom, open; step 1 answers it for questions 1 to 3;
  - borrowed: a change may be declined as "not worth the change" (`docs/conventions/exchange/` §6.5, *Verdicts*). Question 0 asks it first, for every depth;
  - changed: the four questions gain question 0, and a line may be split into parts. The rules on deciding had neither;
  - borrowed: a verdict that cannot be reached yet is held, with its trigger and a line so it is not lost (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today a verdict says whether the Concept Deliverer takes a hunk: taken, declined or held (`docs/conventions/exchange/` §6.5). Here it says how deep the Copy Change goes. Depth b is near today's taken: the Copy Change enters the System Kit.

**Step 2. The verdict is written.**

- **Options,** for what a verdict holds:
  - a. the answer only: unsound, misread, or its depth;
  - b. the answer, its why, and whether it agrees with the System Repo's proposal, with why if not;
  - c. b, and what the Maintainer Repo changes for it.
- **Chosen:** b. The others:
  - a leaves the change made from it with nothing to check it against, and a proposal judged wrong goes unseen;
  - c decides what changes before it is worked out: that is the work of Act on the verdicts, with the survey where the depth needs one (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.4, *Act on the verdicts*).
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.3, *Judge Copy Changes*).
- **Today:**
  - borrowed: a verdict carries its why (`docs/conventions/exchange/` §6.5, *Verdicts*);
  - changed: today every verdict goes down in the Delivery Note (`docs/conventions/exchange/` §6.5). Here the verdict is the Maintainer Repo's, and none goes down (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *Known, not ruled*);
  - changed: today a verdict is taken, declined or held (`docs/conventions/exchange/` §6.5). Here it is a depth, or unsound, misread, covered or held;
  - changed: today no verdict answers a proposal, since every edit claims to be for any CBC Run (`docs/conventions/exchange/` §5.1). Here each says whether the proposal holds.

## 6. Act on the verdicts

**Step 1. The Maintainer Repo makes its changes. For depth b, the System Kit's Adapted Case.**

- **Options,** for depth b:
  - a. the lesson is reworded for every System Repo, and the System Kit's Adapted Case gains it;
  - b. the Copy Change goes into the System Kit's Adapted Case as the System Repo wrote it;
  - c. the lesson waits until a second System Repo makes the same Copy Change.
- **Chosen:** a. The others:
  - b carries one project's words to every System Repo, since the System Repo writes what happened in its own words, on purpose (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.1, *Change a Kit Copy*);
  - c waits for a second proof of what judging already found: question 2 found the Copy Change is not that System Repo's own.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.4, *Act on the verdicts*).
- **Today:**
  - borrowed: a taken change is committed here, and the next delivery carries it (`docs/conventions/exchange/` §6.5, *Verdicts*). It is depth b's path, and the other depths'.

## 7. Deliver the Kit Update

Two steps:

1. The Kit Update is made: the System Kit at its newest Kit Version.
2. The Kit Update is delivered.

**Step 1. The Kit Update is made: the System Kit at its newest Kit Version.**

- **Options,** for when a Kit Update goes:
  - a. after every Look for Lessons, even with nothing to carry;
  - b. only when it carries a System Kit change.
- **Options,** for when the check in Deliver the Kit Update runs:
  - c. after Act, at every Look for Lessons;
  - d. only when the human names the System Repo to update, after the Look for Lessons that starts.
- **Chosen:** b and d. The others:
  - a sends an empty Kit Update to carry where the Look for Lessons stopped. The *settled snapshot* is in the Repo Register now (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2, *Read Copy Changes*), so nothing needs carrying;
  - c answers, at a Look for Lessons, a question nothing acts on: nothing is made until work resumes, and the System Kit may move again before then.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.5, *Deliver the Kit Update*).
- **Today:**
  - borrowed: the delivery is staged into the CBC Run's `temp/` on the reviewer's word, the CBC Run's tree checked clean first, and named by the commit it was final at (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: files go whole, every copy at every delivery after birth (`docs/conventions/exchange/` §3.2, *What goes*);
  - borrowed: a delivery goes after a CBC Run Reading, or when something a CBC Run holds has changed in the Concept Deliverer (`.claude/skills/exchange-deliver/SKILL.md`, its description);
  - borrowed: the Delivery Note says what changed since the Delivery Pin, as paths the CBC Run can check, and why it matters to this CBC Run; it never describes the Concept Deliverer's own practice (`docs/conventions/exchange/` §3.7, *The Delivery Note*; `.claude/skills/exchange-deliver/SKILL.md`);
  - borrowed: the Delivery Note carries what is gone (`docs/conventions/exchange/` §3.6, *Absence in a delivery*);
  - borrowed: one CBC Run Reading is open per CBC Run at a time, and a new read extends it (`.claude/skills/exchange-read/SKILL.md`, Stage 4);
  - changed: today every read ends with a Delivery Note, even an empty one, to carry the Read-Through Commit (`docs/conventions/exchange/` §6.6). Here a Kit Update goes only when it carries a System Kit change;
  - changed: today the Delivery Note gives a verdict on everything the CBC Run addressed to the Concept Deliverer (`docs/conventions/exchange/` §3.7). Here none goes down (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *Known, not ruled*).

**Step 2. The Kit Update is delivered.**

- **Options,** for checking what was staged:
  - a. a second Adapted Case of the Maintainer Repo's checks it, apart from the one that delivered, as at birth;
  - b. the delivering Adapted Case compares each staged file with the new Kit Version, once staged, and the System Repo checks the Update Note against the files when it takes them;
  - c. only the System Repo's check, at the Update Take.
- **Chosen:** b. The others:
  - a was chosen at birth because the start becomes the base of every Look for Lessons (`temp/common-ground/between-repos-simulation.md` §5.1, step 2). Here a wrong file is held in `temp/`, never in force, and a comparison of files leaves little mistake to share. It comes back if a staged file is found, after an Update Take, to differ from the System Kit;
  - c leaves only the System Repo to check, and it cannot open the System Kit, so a staged file that differs from it passes.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.5, *Deliver the Kit Update*).
- **Today:**
  - borrowed: the delivery and its Delivery Note are copied into the CBC Run's `temp/` on the reviewer's word, by the reviewer or by the agent when told; the agent never stages unasked; the tree is checked clean first; the Delivery Staging is named by the commit at which files and Delivery Note are final (`docs/conventions/exchange/` §3.1, *Delivery Staging*);
  - borrowed: nothing in `temp/` is in force until it is copied into place (`delivery/container/.claude/rules/delivered-copies.md`, rule 5);
  - borrowed: one Agent Skill both writes the Delivery Note and stages the delivery (`.claude/skills/exchange-deliver/SKILL.md`). It also compares the staged files here;
  - borrowed: the CBC Run's `temp/` gains exactly the staging and its Delivery Note, and nothing tracked in the CBC Run changes (`.claude/skills/exchange-deliver/SKILL.md`, *Gates*);
  - changed: today the staged files are copied by a script, so they equal the Master Copies by how they are made, and no comparison follows; the CBC Run's Delivery Take checks the Delivery Note against the files (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 1).

## 8. Take the Kit Update

**Step 1. The System Repo takes the Kit Update.**

- **Options,** for when a Kit Update is taken:
  - a. whenever it arrives;
  - b. at the opening of the System Repo's next Plan Step, right after a Look for Lessons that reached main;
  - c. at the opening of the System Repo's next Plan Step, whatever the Look for Lessons reached.
- **Options,** for the System Repo's Change Records at the Update Take:
  - d. kept, since the merge keeps what only the System Repo added;
  - e. all cleared, every Kit Copy taken whole.
- **Options,** for where the Update Take is committed:
  - f. on a branch of its own, one commit per part, a gate last, main moving by fast-forward at the gate's close;
  - g. as the first commit of the System Repo's next Plan Step;
  - h. as the System Repo's Plan Step, for the Update Take alone;
  - i. as one commit on main, the rule that main moves only at a gate's close (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2, *Read Copy Changes*) narrowed so that only the work of the System Repo's Plan Steps waits for a gate.
- **Chosen:** b, e and f. The others:
  - a lands in the middle of a step, which then runs on two sets of rules;
  - c takes the Kit Update over Copy Changes not yet judged. The Kit Update answered none of them, and clearing their Change Records loses them before they are judged;
  - d keeps Change Records that say how a Kit Copy differed from the old System Kit. After the Update Take some describe nothing, and none says how the Kit Copy differs from the new one;
  - g leaves main on the old Kit Version until the step's gate closes, so naming the System Repo to update in between finds the Kit Update due again;
  - h gives the Update Take an opening, as the System Repo's Plan Steps have, for work the Update Note already orders. f keeps what it needs from one: the gate;
  - i narrows that rule for the Update Take alone. f keeps the rule whole, its gate checking that the Update Take finished.
- **Its rules:** the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.6, *Take the Kit Update*).
- **Today:**
  - borrowed: nothing in `temp/` is in force until it is copied into place (`delivery/container/.claude/rules/delivered-copies.md`, rule 5);
  - borrowed: the Delivery Take's order: the Delivery Note checked against the staging first, copies taken whole, what is gone removed, one entry with the new Delivery Pin, the staging removed (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, steps 1, 4, 5, 6 and 7);
  - borrowed: a CBC Run's Plan Step reaches main by fast-forward from its branch, at its close (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). The Update Take's branch does the same;
  - borrowed: a Receipt Branch may hold the delivery as it arrived (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 4). Here the Kit Update is committed as it arrived, on the Update Take's branch;
  - changed: today, with more than one commit, the Delivery Take's entry goes in the last, where every copy equals the Delivery Pin (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Here the Kit Version names the *version snapshot*, item 3's commit, where the next Look for Lessons starts (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2, *Read Copy Changes*);
  - changed: today nothing at the Delivery Take is decided at a gate. Here the Update Take's gate checks that the Update Take finished;
  - borrowed: being behind the Concept Deliverer is acceptable (`delivery/container/.claude/rules/delivered-copies.md`, rule 6). A System Repo not named to update is that;
  - changed: today an edit made after the Read-Through Commit is re-applied on top, its record standing (`delivery/container/.claude/rules/delivered-copies.md`, rule 5, step 3). Here the opening order leaves no such edit;
  - changed: today a declined edit is gone at the Delivery Take, and never edited back in (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Here what becomes of a Copy Change the System Kit did not take is not ruled (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.7, *Known, not ruled*);
  - changed: today work continues on the edited copy when a CBC Run's Plan Step opens before the reply (`delivery/container/.claude/rules/delivered-copies.md`, rule 6). Here the next step waits for the Update Take, once the human has named the System Repo to update.

