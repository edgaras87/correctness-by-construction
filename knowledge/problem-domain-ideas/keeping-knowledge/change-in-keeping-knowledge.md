# Change, in keeping knowledge

<!--
What it is: a Problem Domain Idea of the Maintainer Repo's own Problem Domain, keeping knowledge, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/change.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it. Where each layer is kept is knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md's, the layers document here.
What stands on it: this repo's own Adapted Cases for a change, by their Adapted Understanding Texts: .claude/understanding/read-copy-changes.md, from §3.2; .claude/understanding/judge-copy-changes.md, from §3.3 and §3.4; .claude/understanding/deliver-the-kit-update.md, from §3.5. knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md, Change, in CBC backend design, borrows the Defined Terms of a change's travel.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Where it started: the layers document's §4, How knowledge moves, moved here whole, with the Defined Terms of a change's travel and the open questions on change (ADR-0088).
Its first sources, input and not rules:
- temp/common-ground/backend-repo-change-simulation.md, the six parts and depths, and how each rule was chosen;
- temp/common-ground/common-ground-problem.md §2.1 and §3.
How it is edited: §3's picture is checked at every change against §3's table of parts and §3.7's table of cases.
-->

This document is Change in the Maintainer Repo's Problem Domain: the arrows between the Maintainer Repo and the Backend Repos, how a Copy Change travels them, and the Maintainer Repo's own lessons. What a change is, and the rules every change keeps, are Change's (`knowledge/backbone-ideas/change.md`). Where each layer is kept, and what the Backend Kit holds, are the layers document's: the layers of knowledge, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`).

## 1. Its Defined Terms

- **Backend Kit Attention Note:** what a Backend Repo writes for the Maintainer Repo to look at in the Backend Kit, when no Backend Kit Copy Change carries it. Short form: **Attention Note**.
- **Backend Kit Copy Change:** a Backend Repo's change to a Backend Kit Copy, made against the Backend Kit Version that copy came from. Short form: **Copy Change**.
- **Backend Kit Copy Change Record:** what a Backend Repo writes with each Backend Kit Copy Change, saying what changed and why. What it holds and where it sits are §3.1's. Short form: **Change Record**.
- **Backend Kit Update:** what the Maintainer Repo sends a Backend Repo: a copy of every Backend Kit file at one Backend Kit Version, with its Backend Kit Update Note. Short form: **Kit Update**.
- **Backend Kit Update Note:** what the Maintainer Repo writes with a Backend Kit Update, for the Backend Repo that takes it. Short form: **Update Note**.
- **Backend Kit Update Take:** a Backend Repo taking a Backend Kit Update into its Backend Kit Copies. How it runs is §3.6's. Its *version snapshot* is the Backend Repo's commit where the Backend Kit Update Take put every Backend Kit Copy at the new Backend Kit Version, its hash written beside that Backend Kit Version. Short form: **Update Take**.
- **Backend Kit Version:** the Backend Kit as it stood at one Maintainer Repo commit. Each Backend Repo records the one its Backend Kit Copies came from. Short form: **Kit Version**.
- **Backend Repo Reading:** the draft that lists the Backend Kit Copy Changes one Look for Lessons found in a Backend Repo, nothing judged. With none found, none is written. Short form: **Repo Reading**.
- **Look for Lessons:** the Maintainer Repo taking one Backend Repo's work since its *settled snapshot* into account: read, judged and acted on. How it runs is §3's.
- **Maintainer Repo Register:** the Maintainer Repo's list of its Backend Repos: where each lives, and its *settled snapshot*, the Backend Repo's snapshot up to which the Maintainer Repo has read, judged and acted on. The *settled snapshot* holds the Backend Kit Version the Backend Repo had then, which may be behind the newest. Short form: **Repo Register**.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Failure Case | `temp/common-ground/common-ground-problem.md`, *Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Knowledge on Trial | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `docs/conventions/project-recording/` §2.1, *What a plan is* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. The arrows

- **adapt,** **lesson** and **set apart,** between layers 1, 2 and 3: as Change has them (`knowledge/backbone-ideas/change.md` §4, *The arrows*). A lesson, or a part set apart, can come from the Backend Kit's Adapted Cases or from the Maintainer Repo's own.
- **birth,** layer 3 to layer 4: a new Backend Repo receives Kit Copies of the Backend Kit, at one Backend Kit Version.
- **Kit Update,** layer 3 to layer 4: a Backend Kit Update (the layers document's §3) brings a Backend Repo's Kit Copies to a newer Backend Kit Version. The Backend Repo takes it by its own Kit Copy of the Adapted Case for taking a Kit Update.
- **Copy Change, read back,** layer 4 to layer 3: a Backend Repo changes a Kit Copy and records why. The Maintainer Repo reads it back and judges it against the Adapted Case the Kit Copy came from.
- **adapt,** **lesson** and **set apart,** between layer 2 and layer 4, for the Maintainer Repo's own Adapted Cases: they are written from its Problem Domain Ideas, and its lessons, and the parts it sets apart, go up to them (`knowledge/backbone-ideas/change.md` §4, *The arrows*).

## 3. How a change travels

A Copy Change travels through six parts, each done by one repo.

```
 Backend Repo              ┆ Maintainer Repo
 ────────────              ┆ ───────────────
                           ┆
 1. Change a Kit Copy ─────┼── reads; writes nothing there ──▶ 2. Read Copy Changes ──▶ 3. Judge Copy Changes ──▶ 4. Act on the verdicts
    §3.1                   ┆                                   §3.2                     §3.3                      §3.4
                           ┆                                                                                      │
 6. Take the Kit Update ◀──┼── writes only into its temp/ ──── 5. Deliver the Kit Update ◀────────────────────────┘
    §3.6                   ┆                                   §3.5

 How high each depth goes: 3. Judge Copy Changes sets it, 4. Act on the verdicts changes it

 depth                          b        c, at 2   c, at 1   d         e         f
                                         └─────────── not yet checked ────────────┘
 layer 1  Backbone Idea                            ●
 layer 2  Problem Domain Idea            ●         ●         ○         ○
 layer 3  Adapted Case          ●        ●         ●         ●         ●
 layer 4  a Backend Repo's work ●        ●         ●         ●         ●         ●
 ───────────────────────────────────────────────────────────────────────────────────────────
 highest layer                  3        2         1         3, or 2   3, or 2   none, open
```

Key: each § is a section of this document. A Look for Lessons is 2 to 4; bringing a Backend Repo up to date adds 5 and 6, and needs the first. ● is a Copy Change's path, from its Kit Copy up to the highest layer it changes; ○ is "or up to here", when the case asks it (§3.7, its rows d and e). At every depth, 5. Deliver the Kit Update brings a Kit Update down.

Each part sits at a layer, or on an arrow of §2:

| Part | Who | Where |
|---|---|---|
| Change a Kit Copy | Backend Repo | layer 4, in a Kit Copy |
| Read Copy Changes | Maintainer Repo | the arrow *Copy Change, read back* |
| Judge Copy Changes | Maintainer Repo | layer 3: which layer the Copy Change holds for |
| Act on the verdicts | Maintainer Repo | the layer the verdict names; the arrows *lesson* and *adapt* |
| Deliver the Kit Update | Maintainer Repo | the arrow *Kit Update* |
| Take the Kit Update | Backend Repo | layer 4, its Kit Copies |

So the six parts are one movement: up from layer 4, as high as the Copy Change holds, and back down.

**The Look for Lessons.** Read Copy Changes, Judge Copy Changes and Act on the verdicts make one pass over one Backend Repo, the Look for Lessons. It starts when the human names a Backend Repo, for its lessons or to update it. It ends once Act on the verdicts is done, which sets the *settled snapshot* to the stop (§3.2). It falls into one of three cases (§3.2). Deliver the Kit Update and Take the Kit Update are outside it.

**Bringing a Backend Repo up to date.** It is a second job, which needs the first. It runs only when the human names the Backend Repo to update, and starts with a Look for Lessons. Its check, whether a Kit Update is due, belongs to Deliver the Kit Update. It comes after Act on the verdicts, since the Backend Kit moves for a Copy Change only once it is judged and acted on (§3.5).

Each depth names the highest layer a Copy Change reaches (§3.7). The arrows each travels:

| Depth | Arrows it travels |
|---|---|
| a. it stays in the Backend Repo | *Copy Change, read back*; nothing comes down |
| b. the Backend Kit's Adapted Case changes | *Copy Change, read back*; *Kit Update* |
| c, at layer 2. the idea above changes: its Problem Domain Idea | *Copy Change, read back*; *lesson*; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| c, at layer 1. the idea above changes: its Backbone Idea | *Copy Change, read back*; *lesson*, twice; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| d. the idea above already holds it | *Copy Change, read back*; *adapt*; *Kit Update* |
| e. it asks to narrow the idea above | *Copy Change, read back*; *Kit Update* |
| f. several Adapted Cases need it, but not all | *Copy Change, read back*; *Kit Update* |

Depth f's gap, text shared by several Adapted Cases of one Problem Domain but not all, is §3.7's, its row f.

### 3.1 Change a Kit Copy

The Backend Repo changes a Kit Copy during its own work, and the gate of its Plan Step decides each Copy Change. When a Kit Copy changes, how the change is committed, and why, are the Backend Repo's side, in Change, in CBC backend design (`knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` §2, *Changing a Kit Copy*). This section keeps what the Maintainer Repo relies on: where the Change Record sits, what it holds, and the gate.

**Where the Change Record sits.** In a footer of the Kit Copy's Adapted Understanding Text, which is not loaded for work. So the Copy Change and its why land in one diff, and the why cannot lose its Kit Copy. When only an Instruction Text changes, its Change Record goes there too. An Instruction Text with no Adapted Understanding Text, such as the Backend Kit's Defined Terms, carries its Change Record in its own footer.

**What the Change Record holds:**
- what changed, by meaning: the part, and what it says now. When some of the Adapted Case's texts were left as they were, it also says whether they still match the Copy Change (`temp/common-ground/common-ground-problem.md` §4, Failure Case 8);
- what happened, concretely, in the Backend Repo's own words. It is never written to sound general: rewording it is the Maintainer Repo's, after judging;
- which work found it;
- the Backend Repo's proposal, marked as one: its own problem, or one any repo would meet. The Maintainer Repo judges every Copy Change, and says whether it agrees, and why if not.

**At the gate.** At the close of the Backend Repo's Plan Step, its Copy Changes are seen together, now that the whole step is seen. The agent compares the Kit Copies against where the step began, checks that each Copy Change has a Change Record that says it, and shows each with its Change Record. The human decides each, the agent proposing: kept, edited or reversed, its Change Record with it. One edited gets its Change Record rewritten. Copy Changes that share one reason are linked: the reason is written in full in one Change Record, and each other one says how its own Kit Copy was affected and points at that one. If the one holding the reason is reversed, the reason moves to one that stays, and the others point there.

**Its Adapted Cases:** the Backend Repo's, in Change, in CBC backend design (`knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` §4, *Its Adapted Cases*).

**Open:**
- whether a reversed Copy Change leaves a trace for the Maintainer Repo. One tried and undone may be evidence that the Kit Copy was right. Its trigger: the first Copy Change reversed at a gate.

### 3.2 Read Copy Changes

The Maintainer Repo finds what changed in one Backend Repo since it last looked, and lists it, judging nothing.

**Where a stretch ends.** At the gate where one of the Backend Repo's Plan Steps closed, the last one on main. Main moves only at a gate's close, so main is always at a closed gate. Work past it, in a branch or not yet committed, is left for the next Look for Lessons: a Copy Change the gate has not yet looked at may still be edited or reversed there (§3.1). An open Plan Step changes nothing here: its work waits for the next Look for Lessons, and a Kit Update waits for the step's gate (§3.5). If a stretch's history is cleaned before main moves, the Change Records are unharmed: they are in the Kit Copies, not in the commits.

**Two snapshots.** Read Copy Changes compares two snapshots of the Backend Repo, the older snapshot and the stop, and never walks its commits. The commits between them are history, opened only to understand something deeper.
- **The older snapshot** is the Repo Register's *settled snapshot*, and it is never empty. It is kept in the Maintainer Repo, not carried to the Backend Repo by the next Kit Update: a Look for Lessons may have no Kit Update after it, and the Backend Repo would then hold an old stop, so the next Look for Lessons would find again what was judged. Nor is it each Repo Reading's first line, which would keep every Repo Reading for good, for that line alone. At birth, the Maintainer Repo's check of the delivery writes the Backend Repo's row, its *settled snapshot* set to the start: the commit holding the Kit Copies as they arrived (`temp/common-ground/between-repos-simulation.md` §5.1, step 2). Nothing before the start is the Backend Repo's own Copy Change. So every Look for Lessons, the first among them, starts at the *settled snapshot*.
- **After an Update Take,** the first Look for Lessons starts at the *version snapshot* instead, found at main (§3.6, *At the Update Take, in order*, item 4). The *settled snapshot* still holds the Kit Copies of the previous Kit Version, and starting there would read the Update Take's changes as the Backend Repo's. The *version snapshot*'s Kit Copies are not checked against the new Kit Version: Deliver the Kit Update and the Update Take check the files three times before (§3.5; §3.6, items 2 and 6).
- **The stop** is the Backend Repo's main as it stands when the Look for Lessons begins, named by its commit. Everything is compared against that commit, never against main as it moves, so a commit landing during the Look for Lessons falls into the next one.
- **The Backend Repo's Kit Version** is read from the *settled snapshot*, never stored anywhere else. It may be behind the newest.

A Look for Lessons ends in one of three cases:

| Case | Main moved | Kit Copy changed | What follows |
|---|---|---|---|
| *not moved* | no | — | nothing new; Act on the verdicts sets the *settled snapshot* to the stop, as it was |
| *no Copy Change* | yes | no | nothing is judged, no Repo Reading is written, and Act on the verdicts sets the *settled snapshot* to the stop |
| *Copy Change read* | yes | yes | the Copy Changes are listed in a Repo Reading, judged and acted on |

When the human named the Backend Repo to update, the check in Deliver the Kit Update follows, once Act on the verdicts is done.

**The Repo Reading.** One line per Copy Change, nothing judged. One line per Kit Copy would merge two Copy Changes to it, and lose one of their reasons. A line holds the Kit Copy and its part, what it says now, what happened, which work found it, and the Backend Repo's proposal, marked as one. A Copy Change with no Change Record says "no entry". Copy Changes linked by one reason are listed together, under it. The Repo Reading names its stop. When the list is empty, none is written. The Repo Reading stays a draft, and goes once its work is done.

**When the stop moves.** Act on the verdicts sets the *settled snapshot* to the stop, in the Repo Register, at every Look for Lessons, whether or not a Copy Change was found. With no verdicts, that is right after judging. It never moves before: a Look for Lessons left half done must not mark its Copy Changes taken into account. Whether the Backend Repo takes the Kit Update does not hold it back.

**Its Adapted Cases:**
- the Backend Repo's gate list: main moves only at a gate's close. It is there today;
- the Maintainer Repo's own, for reading a Backend Repo's Copy Changes. It holds this part's own steps, and why each is so.

### 3.3 Judge Copy Changes

The Maintainer Repo judges each line of the Repo Reading, and writes its verdict.

**Who judges.** The agent proposes each answer, with what it read; the human decides each line. The Backend Repo's own view of its Copy Change is input, never the verdict. An empty list gives no verdicts, and only the stop goes on to Act on the verdicts. Two other ways were weighed. The agent judging, and the human looking only where it disagrees with the Backend Repo's proposal, lets their agreement pass unchecked: two views agreeing is not a verdict (`temp/common-ground/common-ground-problem.md` §4, Failure Case 20). The human judging alone reads every text the judging needs, which the agent reads faster, with nothing written down to check.

**The verdict.** Each judged line, or part of one, gets a verdict, the agent drafting and the human deciding. It holds the answer, its why, and one line on the proposal: "the proposal holds" or "the proposal does not hold, because …". It is the Maintainer Repo's decision, written for its own work: what it changes starts from it. The answer alone would leave the change made from it with nothing to check against, and a proposal judged wrong would go unseen. What the Maintainer Repo changes for it is not in the verdict: Act on the verdicts works that out, with the survey where the depth needs one. A verdict is one of:
- unsound, saying what the Copy Change breaks or leaves unfixed;
- misread: the Kit Copy already said it;
- covered by a Backend Kit change since the Backend Repo's Kit Version;
- its own, depth a;
- lost in narrowing, depth d;
- a lesson for its Problem Domain Idea, depth c at layer 2;
- a lesson for its Backbone Idea, depth c at layer 1;
- a lesson for its Adapted Case, depth b;
- held, with its trigger.

Lines under one reason share one verdict, and each line says how its own Kit Copy is affected. No verdict goes down to the Backend Repo, and what becomes of a Copy Change the Backend Kit does not take is not ruled (§3.7, *Known, not ruled*). What the Backend Repo gets reaches it with the next Kit Update.

**Its Adapted Case.** The Maintainer Repo's own, for judging a Repo Reading and acting on its verdicts. It holds this part's own steps, and why each is so.

**Open:**
- which other texts are checked for a loss in narrowing. Nothing comes down the arrow *adapt*, since the idea above did not change (`knowledge/backbone-ideas/change.md` §6, *Open questions*, question 1). A first guess: the texts built on the idea that holds the part, as the survey asks (§3.4). If several lost it, the idea's wording may be too weak, and is reworded clearer, never narrower. Its trigger: the first depth-d verdict.

### 3.4 Act on the verdicts

The Maintainer Repo makes what each verdict asks, then moves the *settled snapshot*.

**What each verdict asks.** From each verdict, the Maintainer Repo makes what its depth asks, the agent drafting and the human deciding. For depth b, the lesson is reworded for every Backend Repo, and the Backend Kit's Adapted Case gains it. It is committed in the Maintainer Repo, and the Backend Kit stands at a new Kit Version. The Backend Repo the lesson came from gets it back with the next Kit Update, though its Kit Copy already holds the Copy Change in its own words. Two other ways were weighed for depth b. The Copy Change taken into the Backend Kit as the Backend Repo wrote it carries one project's words to every Backend Repo (§3.1). Waiting until a second Backend Repo makes the same Copy Change waits for a second proof of what judging already found.

**The other depths, not yet done.** This part holds their work too, each checked here later:
- depth c changes the idea above at its layer, after the survey: its Problem Domain Idea at layer 2, its Backbone Idea at layer 1;
- depth d fixes the Adapted Case from the idea above, after fixing the Problem Domain Idea from its Backbone Idea when the loss sits at layer 2;
- depth e marks a narrowing with its why, in the text just below the idea that does not fit.

**The survey.** Before a lesson enters the idea above, every other text built on that idea is asked whether it fits, the one the lesson came from excepted (`knowledge/backbone-ideas/change.md` §4, *The arrows*, its **Rules**; `knowledge/backbone-ideas/layers-of-knowledge.md` §3.3, *The Adapted Case layer*). At layer 2, that is the other Adapted Cases of that Problem Domain Idea, the Maintainer Repo's own only when they share it. At layer 1, it is every Problem Domain Idea on that Backbone Idea. It is the arrow *adapt*'s check, run before the idea changes, so a conflict shows first. Each text answers "holds as it is", "must change", with what and why, or "conflicts", with why. A conflict is input to the human's decision, never a veto, and what the survey finds must change, changes. Its answers are also evidence of how high the lesson is true: if every answer conflicts, it is not true that high.

**Rewording.** A lesson is reworded here, never before: for every Backend Repo at depth b; at depth c, naming no Adapted Case at layer 2, and no Problem Domain at layer 1 (`knowledge/backbone-ideas/change.md` §4, *The arrows*, its **Rules**).

**Then the stop moves.** Once the verdicts are acted on, the Repo Reading goes: nothing in the Kit Update is read from it. Act on the verdicts sets the *settled snapshot* to the stop, in the Repo Register (§3.2). With no verdicts, as in cases *not moved* and *no Copy Change*, that is all it does.

**Its Adapted Case.** The Maintainer Repo's own, for judging a Repo Reading (§3.3), which acts on the verdicts too.

**Open:**
- at layer 1, how far down the survey reaches before the change: only the Problem Domain Ideas, each checking its own Adapted Cases when it changes, or every Adapted Case below them at once. The first is cheaper; the second may catch a conflict two layers down. Its trigger: the first lesson judged at layer 1;
- how a part of a Backbone Idea is known not to fit a whole Problem Domain, when one Backend Repo's Copy Change shows one Adapted Case. A first guess: the same survey, over that Problem Domain Idea's Adapted Cases. Its trigger: the first depth-e verdict.

### 3.5 Deliver the Kit Update

The Maintainer Repo makes a Kit Update for one Backend Repo, when its work resumes, and stages it there.

**When one is due.** A Kit Update is due when the Backend Repo's Kit Version, which the Backend Repo holds, is behind the newest. It goes only when it carries a Backend Kit change. It is never sent empty, to carry where a Look for Lessons stopped: the *settled snapshot* is in the Repo Register (§3.2), so nothing needs carrying. Two Kit Versions are compared by the Backend Kit's files at their two commits, never by the commits themselves: a Maintainer Repo commit that touches no Backend Kit file leaves every Backend Repo where it was. A Backend Repo cannot see the Maintainer Repo, so it cannot learn this itself. For depth b, the Backend Kit has moved for the Copy Change, so a Kit Update is due: it carries the Backend Kit's Adapted Case at the new Kit Version, with the lesson as its why. Depth c is not yet walked through this part (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it").

**When the check runs.** Only when work resumes. Work resumes when the human, about to open the Backend Repo's next Plan Step, names it to update; neither repo can see that moment itself (§3.6). Nothing is made for, or sent to, a Backend Repo whose work has not resumed, nor while one of its Plan Steps is open. A check at every Look for Lessons would answer a question nothing acts on: nothing is made until work resumes, and the Backend Kit may move again before then.

**What a Kit Update is.** Two things: every Kit Copy, whole, at the newest Kit Version, and an Update Note. The Backend Repo then has the new version of each file, and finds its old one in its own history. The Update Note holds:
- the new Kit Version;
- the Backend Repo's *settled snapshot* it was built against, whether a Repo Reading was written or not. The Update Take checks it before anything moves. The Update Note names the check, so a Backend Repo whose Adapted Case for taking is older still meets it;
- what changed since the Backend Repo's Kit Version, from the same comparison of files: each path changed, new, gone or renamed, and how many. The Backend Repo checks the files against it when they arrive, and a file that is gone cannot say so itself;
- the why of each Backend Kit change since then, whatever its source: a Look for Lessons at this Backend Repo or at another, or the Maintainer Repo's own work. It is read from the bodies of the Maintainer Repo's commits that changed a Backend Kit file between the two Kit Versions, since a body says why (`docs/conventions/commit-messages/` §1, *What a commit message is*). Each why stands on its own, and names no other repo; a change that comes from a lesson, at any depth, quotes the lesson as it was reworded (§3.4). With it, the Backend Repo judges a change against its own needs without seeing the Maintainer Repo;
- which files are taken first: the Adapted Case for taking a Kit Update, so a Kit Update is never taken by instructions older than it (`temp/common-ground/common-ground-problem.md` §4, Failure Case 10);
- the Kit Update it replaces, when one was waiting.

The Update Note is no summary of the Maintainer Repo's work, which the Backend Repo cannot check. It is not a record either: it goes once the Kit Update is taken, and what the Backend Repo decides goes in its records. Nothing in it cites what the Backend Repo cannot open: no path, record or word of the Maintainer Repo's own.

**One at a time.** A Repo Reading stays open until its verdicts are acted on. One Repo Reading is open per Backend Repo at a time: a Repo Reading made while one is open extends it, and its lines are judged with the rest, so judging already done is kept. One Kit Update waits for the Backend Repo at a time: a newer one replaces one not yet taken, since it carries every Backend Kit change since the Kit Copies' Kit Version.

**Staging.** A Kit Update reaches the Backend Repo on the human's word, in a step of its own: nothing crosses without that word. It is staged by the human, or by the agent. The Kit Update is written only into the Backend Repo's `temp/`, nowhere else there, and replaces one already waiting. Nothing in `temp/` is in force until the Backend Repo takes it. The Kit Update is named by the Maintainer Repo's commit at which its files and Update Note were final, so its Kit Version is exact. Once staged, each file is compared with the new Kit Version; the Backend Repo checks the Update Note against the files when it takes them.

**Its Adapted Case.** The Maintainer Repo's own, for making and staging a Kit Update. It holds this part's own steps, and why each is so.

### 3.6 Take the Kit Update

The Backend Repo takes a waiting Kit Update, at the opening of its next Plan Step. How it takes one, from its own side, is Change, in CBC backend design (`knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` §3, *Taking a Kit Update*). This section keeps what the Maintainer Repo relies on.

**Before the Update Take.** A Kit Update is taken between two of the Backend Repo's Plan Steps, when the next is about to open, never in the middle of one, the agent proposing and the human deciding. Before that step opens, in a fixed order: a Look for Lessons runs to main, and the Backend Repo's Kit Update, when one is due, is made, delivered and taken. Then the step opens on the new Kit Copies, or on the same ones when no Kit Update was due. An open Repo Reading is extended. The human works on one project at a time, so the Backend Repo waits at little cost. A Backend Repo's Plan Step open when the human returns finishes on the old Kit Copies first, and the human names the Backend Repo to update at the next opening (§3.5). The Update Take checks first, from the Update Note, what the Backend Repo itself can see:
- case 1, its main is still the *settled snapshot* the Update Note names: the Kit Update is taken. Its Kit Version needs no check of its own: it is recorded in main, so it cannot change while main stands still;
- case 2, anything else: there is no Update Take, and the Backend Repo says so. The human names it to update again, and the Look for Lessons finds that main has moved (§3.2). The check in Deliver the Kit Update then finds a new Kit Update due, made against the Backend Kit as it is now, and it replaces the waiting one (§3.5).

**At the Update Take, in order.** Once the check finds case 1, the Update Take cuts a branch from main, the *settled snapshot*. Its first commit is the Kit Update as it arrived, in `temp/`, not yet in force: a record of what came, before the Update Take changes anything. Each item below is then a commit of its own, but item 2, a check. Main moves to the branch's last commit by fast-forward at the gate's close, so it still moves only at a gate's close (§3.2).
1. the Adapted Case for taking a Kit Update is taken first, on its own, so the rest is taken by the new one (`temp/common-ground/common-ground-problem.md` §4, Failure Case 10);
2. the files are checked against the Update Note: what changed, and how many (§3.5). A mismatch is said before anything moves;
3. every Kit Copy is taken whole, at the new Kit Version; each path gone is removed, and each renamed is moved. A part the Backend Repo never changed is taken, and work shows whether it fits (`knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` §2, *Changing a Kit Copy*). A Kit Copy taken whole takes its Change Records away with it, so clearing them is no act of its own. Nothing is lost: main is the *settled snapshot*, so each was read and judged;
4. the new Kit Version is recorded, with the commit that holds it: item 3's, the *version snapshot*, every Kit Copy at the new Kit Version. So the check in Deliver the Kit Update can compare it with the newest. It names item 3's commit because a commit cannot hold its own hash, and item 3's is the last before it. Both are written in `.claude/kit-version.md`, rewritten at each Update Take, so Read Copy Changes and Deliver the Kit Update find them at one fixed path. At birth, it holds the Kit Version alone;
5. the Kit Update and its Update Note are removed from `temp/`;
6. the Update Take's gate, last. It checks that the Update Take finished: the files matched the Update Note, every Kit Copy is at the new Kit Version, the Kit Version is recorded, and `temp/` holds no Kit Update.

**What a Change Record stands against.** Every Change Record stands against the last Kit Version taken, or birth's, and every Change Record goes at an Update Take. This is confirmed at the first Kit Update to reach a Backend Repo whose Kit Copies have Change Records.

**Its Adapted Case.** The Backend Repo's, in Change, in CBC backend design (`knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` §4, *Its Adapted Cases*).

**Open:**
- postponing an Update Take after its Kit Update is staged, so the step opens on the old Kit Copies and the Kit Update waits. For now there is no such choice: a staged Kit Update is taken at the opening, unless the Update Take's check finds main moved (case 2). Once an Update Take can be postponed, main can move before it, so decide then whether the Maintainer Repo must check main before delivery, and whether main alone is enough: a Plan Step on a branch leaves main where it is. Its trigger: the first staged Kit Update the human does not want taken.

### 3.7 The cases

A Copy Change varies in two ways. What was changed varies how the Backend Repo records it, and how the Maintainer Repo finds it; it is the same however deep the Copy Change turns out to go, since that is known only once it is judged. How deep it goes varies how the Maintainer Repo decides, and how the Kit Update is written. The rules above are worked for the first case and depth b. Each row not yet checked is checked when practice first meets it, depth c's by its own item (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it").

| Kind | Case | Status | Differs so far |
|---|---|---|---|
| what changed | one Adapted Case, any of its texts | worked, §3.1 to §3.6 | — |
| what changed | a Defined Term | not yet checked | — |
| what changed | delivered Knowledge on Trial | not yet checked | read: compared like any Kit Copy; decided: the original was never proven, so the Copy Change is evidence for its trial |
| what changed | one reason behind Copy Changes to several Adapted Cases | not yet checked | recorded: one why, naming every Kit Copy it changed; read: the Copy Changes are listed together |
| how deep | b. the Backend Kit's Adapted Case changes: layer 3 | worked, §3.3 to §3.6 | — |
| how deep | c, at layer 2. the idea above changes: its Problem Domain Idea | not yet checked | the other Adapted Cases of that Problem Domain Idea are surveyed, the Maintainer Repo's own only when they share it (§3.4) |
| how deep | c, at layer 1. the idea above changes: its Backbone Idea | not yet checked | every Problem Domain Idea on that Backbone Idea is surveyed; how far down the survey reaches is open (§3.4) |
| how deep | d. the idea above already holds it: layer 3, or layer 2 | not yet checked | the loss sits at layer 2 when the Problem Domain Idea lost a part its Backbone Idea holds: the Problem Domain Idea is fixed from its Backbone Idea, then the Adapted Case from the Problem Domain Idea. Which other texts are checked for the same loss is open (§3.3) |
| how deep | e. it asks to narrow the idea above: layer 3, or layer 2 | not yet checked | the narrowing goes into the text just below the idea that does not fit, marked with its why (`knowledge/backbone-ideas/change.md` §4, *The arrows*, its **Rules**, *Narrowing, never shrinking*): the Adapted Case, or the Problem Domain Idea when a part of its Backbone Idea does not fit its whole Problem Domain. How that is known is open (§3.4) |
| how deep | f. several Adapted Cases need it, but not all: no layer | not yet checked | it cannot enter the idea above. When it holds for every Adapted Case of one Problem Domain, it is depth c, at layer 2. One case is left: several Adapted Cases of one Problem Domain, but not all. Across Problem Domains, each writes it into its own adaptation (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The Problem Domain layer*, its **Rules**). Each Adapted Case gains it, and the same text has no shared home. Open; its trigger: the first change two Adapted Cases need, but not every one |

How deep a Copy Change goes is how high it goes: each depth names the highest layer it changes, since a lesson goes as high as it is true (`knowledge/backbone-ideas/change.md` §3, *How the layers fill*). The idea above is the Problem Domain Idea an Adapted Case is written from, or the Backbone Idea that one is adapted from.

A stretch of work may hold several Copy Changes, alike or mixed. Each is recorded and read on its own, so they add no row but one: one reason behind Copy Changes to several Adapted Cases.

New text of the Backend Repo's own, on trial, is not a case here. It comes from no Kit Copy, so it is not a Copy Change. It is Knowledge on Trial, handed over at the Backend Repo's close (the layers document's §3.3). It is one of the other sources, below.

**Known, not ruled.** These can happen, and have no rules until practice meets them. Rules once written for them are in git. Each says what can happen, and its trigger:

- **an Attention Note:** a Backend Repo has something for the Maintainer Repo that no Copy Change carries: a misfit worked around with no Copy Change made, a doubt about a line left as it is, something the Backend Kit lacked, a Kit Copy no longer used. Its trigger: the first such thing a Backend Repo needs to tell.
- **a Copy Change the Backend Kit does not take:** judged its own, depth a, the Copy Change staying in the Backend Repo at layer 4; or unsound, misread or held. It stays only in the Backend Repo's Kit Copy, and the Update Take takes every Kit Copy whole. Whether the Kit Copy keeps it past the Update Take is not ruled. Only such a verdict lets a Look for Lessons end in *Copy Change read* with no Kit Update due after (§3.5). Its trigger: the first such verdict.
- **a verdict sent down:** a verdict the Backend Repo would act on: unsound, misread, or a proposal that did not hold. In the case worked, every Copy Change is taken, and the Kit Update brings it back with the lesson as its why. A proposal that did not hold is cleared with its Change Record at the Update Take, and the human already decided it when it judged Copy Changes (§3.3). Today's Update Note sends every verdict (`docs/conventions/exchange/` §6.5, *Verdicts*). Its trigger: the first Copy Change the Backend Kit does not take, or a Backend Repo that needs a verdict it was not sent.

**Other sources.** A Copy Change is one source of new knowledge. Others exist, and are not yet taken into account here, each left on purpose until Change is finished:
- a lesson found in the Maintainer Repo's own work (§4). Its start may differ (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it");
- Knowledge on Trial a Backend Repo hands over at its close (§5, question 5);
- new knowledge from the human.

Birth stays outside, as the start: it gives a Backend Repo its first Kit Copies and its *settled snapshot* (§3.2).

## 4. The Maintainer Repo's lessons

A lesson from the Maintainer Repo's own work starts in layer 4. Since that work is done by its own Adapted Cases, kept with it, the lesson changes its own Adapted Case at once. It is then judged as a Copy Change read back is, by whether the idea above already holds it and how high it is true, and goes up the arrow *lesson* as far as it holds (§3.3). If it reaches layer 1, it comes down the arrow *adapt*, to the Backend Repos' Adapted Cases too, and reaches Backend Repos by a Kit Update.

It has no Read Copy Changes, Deliver the Kit Update or Take the Kit Update of its own: nothing crosses between repos until a Kit Update carries it to a Backend Repo.


## 5. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **A name for the movement:** what runs from a Copy Change to the Update Take of the next Kit Update, as one thing (§3), so the simulation can name it.
2. **Where Judge Copy Changes sits:** §3 puts it at layer 3, since a Copy Change is judged against the Adapted Case its Kit Copy came from. The sources say only that it runs in the Maintainer Repo.
3. **Depth d and the layer above:** which other texts are checked for a loss in narrowing that Judge Copy Changes finds, and whether the idea above is reworded clearer when several lost the same part. Its first guess and its trigger are §3.3's, under *Open*.
4. **When a change is judged:** a Backend Repo's Copy Change is judged before it reaches layer 3 (§3). The Maintainer Repo's own change reaches its own Adapted Case at once, and is judged after (§4). Does the difference matter? The change work answers it.
5. **Knowledge on Trial offered back:** a Backend Repo's Knowledge on Trial is handed over at its close (the layers document's §3.3). It is not a Copy Change, so the arrow *Copy Change, read back* does not carry it, and the picture has no arrow that does. The change work answers it, when the simulation takes its other sources.
