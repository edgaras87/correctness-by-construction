# Commit plan: the Change split

## Summary — the state after all commits

Change is an idea of its own, at layers 1 and 2 (ADR-0088). The layers documents keep what is where; the Change documents keep how knowledge enters the layers and moves between them:

- **Change,** `knowledge/backbone-ideas/change.md`, a Backbone Idea: what a change is, how the layers fill, the arrows but *worked by*, their rules. The layers of knowledge keeps the layers, *worked by*, and a short §4 pointing at it.
- **Change, in keeping knowledge,** `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`: the arrows between the repos, how a change travels, the Maintainer Repo's lessons. Its §3 keeps what one part hands the next, the rules every part keeps, the tables, and the why of each, never pointing at the simulation. The Maintainer Repo's layers document keeps where each layer is kept.
- **Change, in CBC backend design,** `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md`: how a Backend Repo changes a Kit Copy and takes a Kit Update, the parent of the Backend Kit's Adapted Cases for keeping knowledge.

Each of the six parts of how a change travels has its Adapted Case, written whole from the simulation: its Adapted Understanding Text and its Instruction Text. Today's repo is not read for them; the rewrite compares it with them later.

- **The Maintainer Repo's parts, at layer 4,** kept whole in `.claude/`: Read Copy Changes; Judge Copy Changes with Act on the verdicts; Deliver the Kit Update. Each has its understanding in `.claude/understanding/` and an Agent Skill in `.claude/skills/`, standing on Change, in keeping knowledge.
- **The Backend Repo's parts, at layer 3,** in the Backend Kit's group for keeping knowledge, under `knowledge/adapted-cases/cbc-backend-design/`: Change a Kit Copy, and Take the Kit Update. The gate's part, *At the gate*, waits for how a Backend Repo closes a Plan Step (`TODO.md`, the item that rewrites the Agent Model). Nothing in them names backends.

Each picture shows one thing: the layers pictures what is where, the Change pictures how knowledge moves. The simulation keeps its steps, which depth c walks, and its *Today* lines, which the rewrite reads.

What it gives: a change to one part's steps changes its own Adapted Case, and no longer reads as a change to the Problem Domain Idea; a change to how the layers are kept no longer reads as a change to Change. The layers stand without `temp/`.

## Commits

**1. `docs(agent): add commit plan for Maintainer split`** (landed)

**2. `docs: ADR-0087, the Maintainer Repo's Change split`** (landed)
Proposed. Its decisions 2, 4 and 5 are replaced in commit 3c.

**3. `chore(agent): add Read Copy Changes understanding`** (landed)
It holds §4.2.2's steps, which are instructions. Commit 3d makes it the why.

**3b. `docs: TODO follows the revised Change split`**
The split item: one Change Set, both sides; every Adapted Case whole, from the simulation alone; the whys leave the simulation. The depth c item: every Agent Skill the split writes follows depth c, not Judge's alone. A new line: reuse of the Backend Kit's group for keeping knowledge, its trigger the second Problem Domain that needs a kit.

**3c. `docs: ADR-0087 revised, every Adapted Case whole`**
Still Proposed. Its title and decisions follow the talk of 2026-11-24: one Change Set; each Adapted Case whole, from the simulation alone, today's repo compared in the rewrite; the Backend Repo's parts in the Backend Kit's group for keeping knowledge, with no backend words; the whys moved out of the simulation, to layer 2 for a shared rule and to the understanding text for one part's steps. The rejected options follow.

**3d. `chore(agent): add the Read Copy Changes skill`**
`read-copy-changes.md` rewritten as the why of Read's own steps, from the simulation's §4, its *Chosen* fields; its header no longer names exchange-read. The steps go to the Agent Skill, `.claude/skills/read-copy-changes/`. Its `.claude/decisions.md` entry.

**4. `docs: Read Copy Changes keeps what it hands on`**
§4.2.2 cut, as drafted before the revision. It gains the why of what it keeps, from the simulation's §4, steps 2 and 4: where the stop is kept, and why the list is one line per Copy Change. Its pointer to the simulation for how each rule was chosen goes. The simulation's *Its rules* lines follow.

**5. `chore(agent): add the Judge Copy Changes case`**
Understanding and Agent Skill, from the simulation's §5 and §6; its `.claude/decisions.md` entry. Asked here, since its trigger fires: §4.2.4's open point, whether Act on the verdicts gets an Adapted Case of its own, and whether a Look for Lessons is one of the Maintainer Repo's Plan Steps.

**6. `docs: Judge and Act keep what they hand on`**
§4.2.3 and §4.2.4 cut, as commit 4.

**7. `chore(agent): add the Deliver the Kit Update case`**
Understanding and Agent Skill, from the simulation's §7; its `.claude/decisions.md` entry. One Agent Skill in two stages, making and staging, with the human's word between.

**8. `docs: Deliver keeps what it hands on`**
§4.2.5 cut, as commit 4. *Its Adapted Cases* becomes one.

**8a. `docs: TODO makes Change an idea of its own`** (landed)

**8a1. `docs: ADR-0088, Change an idea of its own`** (landed)

**8a1b. `docs: ADR-0088 revised, Change takes §4`**
Still Proposed. Change takes all that is about knowledge moving, at both layers: the general layers document's §4, and the Maintainer Repo's layers document's §4. The boundary test: a sentence still true if nothing ever changed stays in the layers; one about something added, moved or changed goes to Change. *worked by* stays in the layers. Each document gets its own picture, by the visual-comparison Agent Skill. Its option "a Backbone Idea Change that takes the rules now" moves from rejected to decided; "Change as one section of the layers of knowledge, layer 2 adapted from it" is added as rejected.

**8a2. `docs: Change, a Backbone Idea`**
`knowledge/backbone-ideas/change.md`: what a change is, and the general layers document's §4 moved in, how the layers fill, the arrows but *worked by*, their rules, and its open question 3. The arrow named *change* gets its new name here, decided at this boundary. The layers document keeps the layers and their rules, *worked by* in its layer 4, and one short section pointing at Change in place of §4. Its picture keeps its arrows until 8i, a key line naming Change. The reviewer's guesses as Change's open questions, each with its trigger. Its row in the §3.1 table. Every pointer into the general §4 followed: 12 outside Change itself.

**8a2b. `chore(agent): Judge's understanding follows Change`** (landed, inserted)
The agent's follower of 8a2: two pointers in Judge's understanding into the layers of knowledge's old §4. Inserted, since an agent follower comes in the next commit.

**8a3. `docs: Change, in keeping knowledge, moved out`**
`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`: the Maintainer Repo's layers document's §4 moved whole, its arrows between the repos, how a change travels, and the Maintainer Repo's lessons, with the Defined Terms of a change's travel and the open questions on change. The layers document keeps the layers, where each is kept, and its picture, a key line naming Change, in keeping knowledge, and points at it. Its row in the §3.2.1 table. Every pointer to a moved section followed by script, from `docs` paths: the rename grep, unwrapped.

**8a4. `chore(agent): understanding follows Change's move`**
The three Maintainer Repo Adapted Cases, their understanding and Agent Skills, point at Change, in keeping knowledge: headers, Fact References and Borrow Tables. The agent's side of 8a3's rename grep.

**8b. `docs: Change, in CBC backend design`** (landed)
The draft written for "the layers of knowledge, in CBC backend design", untracked at `knowledge/problem-domain-ideas/cbc-backend-design/layers-of-knowledge-in-cbc-backend-design.md`, renamed and adapted from the Backbone Idea Change. Asked first: where its §2, "What a Backend Repo keeps", goes, since it is what is where, not change: to the planned Layers of knowledge, in CBC backend design, with its trigger, or dropped with that row. Its 7 Borrow Table rows for the Defined Terms of a change's travel point at their old home, and are re-pointed to Change, in keeping knowledge. Its row in the §3.2.2 table. Answered: §2 cut, each of its four facts already held by the layers document or Change, in keeping knowledge; the planned row dropped, with no trigger kept.

**8b1. `docs: a shared Defined Term has one home`** (landed, inserted)
Decided on 2026-11-25, by the reviewer: no Defined Term is defined twice. One several Problem Domains share is defined in one of their Problem Domain Ideas, and the others borrow it. The 11 Defined Terms Change, in CBC backend design uses from keeping knowledge stay defined there, and it keeps borrowing them. Defined Terms §4, its second rule, says the opposite, "defined in each one's own adaptation", and changes. The general layers document's §3.2, "Text shared by several Problem Domains, but not by all, is written into each one's own adaptation", is checked for the same, and excepts a Defined Term if it must. The Paths Rule already forbids a second definition, so no agent follower.

**8b2. `docs: ADR-0088 revised, one home a term`** (landed, inserted)
ADR-0088's decisions 9 and 10: the Backend Kit's terms text, and a shared Defined Term's one home. Where 8c's decision is recorded, asked there and answered first.

**8c. `docs: Defined Terms, in CBC backend design`** (landed)
ADR-0085's decision 4, decided on 2026-11-25: one terms text in the Backend Kit, its first guess. Where the decision is recorded is asked here. The layer-2 parent of that terms text, its row in the §3.2.2 table: where a Backend Repo finds a Defined Term, the terms text, never the Maintainer Repo; each entry adapted from its one home, and checked when that home changes, by Change's rule; the mark; finding one. Open, with its trigger: a Defined Term a Backend Repo coins, the first one. A Borrow Table, short forms and the collision check are written only when the terms text shows a need. The terms text itself starts at 8d. Answered: its §2 narrows Defined Terms' one text, and marks it.

**8c1. `docs: TODO holds At the gate for the close`** (landed, inserted)
*At the gate* waits for how a Backend Repo closes a Plan Step: an Ideas line in the item that rewrites the Agent Model.

**8d. `docs: the Backend Kit's Change a Kit Copy case`** (landed)
Change a Kit Copy's Adapted Understanding Text, and its Instruction Text, a Paths Rule that loads when a Kit Copy is touched, from the simulation's §3, step 1. The Backend Kit's terms text starts here, with the Defined Terms this case uses. The layers document's §3.5 gains the layer-3 folders. Answered before it: the folder layout, and each Instruction Text in its final form, both under *Decisions taken inside this plan*; *At the gate* waits (8c1). Asked here: whether the terms text has an Adapted Understanding Text (the layers document's §5, question 3). Answered: none; its Change Records go in its own footer, and question 3 loses that case. The Adapted Understanding Text holds only this case's own whys; the shared ones stay in Change, in CBC backend design (2026-11-25, the reviewer). Files in a case folder are named by their kind, `understanding.md` and `rule.md`; a Kit Copy is told by its header.

**8d1. `chore(agent): follow the Backend Kit's first case`** (landed, inserted)
The Defined Terms Paths Rule leaves out the Backend Kit's files; Deliver the Kit Update's understanding gains the open point on where each kind of Backend Kit file lands; its `.claude/decisions.md` entry.

**8e. `docs: Change a Kit Copy keeps what it hands on`** (landed)
Change, in keeping knowledge, its Change a Kit Copy section cut to the Maintainer Repo's view, as commit 4. *At the gate* stays there until the Backend Kit's own is written, since part of it has no other home yet: add, then cut.

**8f. `docs: the Backend Kit's Take the Kit Update case`** (landed)
Understanding and Instruction Text, from the simulation's §8. Answered: an Agent Skill, written now, not waiting as *At the gate* does: a whole piece of work between two Plan Steps, its moment a Kit Update in `temp/` and the human's word. The Kit Version and the *version snapshot* are written in `.claude/kit-version.md`, a file of its own, rewritten at each Update Take; at birth, the Kit Version alone (2026-11-25, the reviewer).

**8f1. `chore(agent): skills read .claude/kit-version.md`** (landed, inserted)
Read Copy Changes and Deliver the Kit Update read the two values from that path.

**8g. `docs: Take the Kit Update keeps what it hands on`** (landed)
Change, in keeping knowledge, its Take the Kit Update section cut to the Maintainer Repo's view, as commit 4. The six items stay, against the first sort: Read Copy Changes relies on items 2, 4 and 6, and on main moving only at a gate.

**8h. `docs: the cases point no more at the simulation`** (landed, renamed)
How each case and depth was weighed, from the simulation's §2, into Change, in keeping knowledge, its cases section. No pointer from the layers to the simulation stays. Found: §2 held only how the simulation was worked and its picture, each case's weighing already in §3.7; one pointer went. The header lines naming the simulation as a first source stay.

**8i. The pictures** (landed, six commits)
By the visual-comparison Agent Skill, its candidates committed before the choice, each picture showing one thing: the two layers pictures redrawn without the arrows Change took; a picture for Change, its arrows over the layers drawn plainly; one for Change, in keeping knowledge, the whole travel between the repos. A picture whose point fits in a few lines may end as none. It settles whether the simulation's picture *The whole flow* moves or goes. Landed:
- `262a6dea`, the two layers pictures without Change's arrows, *worked by* kept; no comparison, the form settled on 2026-11-23;
- `28b26691` and `befc9138`, Change's picture: the draft, then C, a box drawing of the four arrows, its list kept below it;
- `7f3ba8f3`, inserted: four lines of Change, in keeping knowledge followed the redraw;
- `ec9ec541` and `ed287006`, Change, in keeping knowledge's picture: the draft, then C, *The whole flow* whole, moved out of the simulation.
Each picture with a second form of its facts, a list or a table, has a header line checking one against the other.

**9. `docs: TODO follows the Change split`** (provisional)
The split item closes. The item on CBC Runs 4, 5 and 6 judges by the Agent Skill. Any open point the cuts answer, or move, followed.

**10. `docs: ADR-0087 and ADR-0088 accepted`**

**11. `docs(agent): close plan for the Change split`**
After the sweep and the look back. The body names what diverged.

## Decisions taken inside this plan

- **Lettered commits keep the numbers already cited.** Commit 2's body names commit 10 for the acceptance, so 4 to 11 keep their numbers.
- **Commits 1 to 3 stay, not reset.** Commit 3's file is reworked by 3d. A reset is the reviewer's call.
- **Add, then cut.** Each Adapted Case lands first; its cut follows. For one commit both hold the steps, and none is ever missing.
- **Each part's three pieces, by three tests:**
  - layer 2: what more than one part relies on, and its why; the test, whether a change to the line would change more than one Adapted Case;
  - Adapted Understanding Text: why the part's own steps are as they are, what was rejected, the open points with their triggers; the test, the agent does not need it to do the work;
  - Instruction Text: when it starts, the steps in order, the checks, what it writes, where it stops for the human; the test, the agent acts on it in the work.
- **The simulation's *Today* lines go to no piece.** They compare with today's repo, and wait for the rewrite.
- **The simulation stays whole until depth c is done.** Its *Chosen* fields and the layers hold the same whys meanwhile: the layers are the home, the simulation the draft that goes.
- **Maintainer Repo's side first, then the Backend Repo's.** Neither needs the other; the Backend Repo's side has three questions to settle first (8b, 8c, 8d).
- **The new Agent Skills' descriptions name Backend Repos and the Look for Lessons.** "Read a CBC Run" still fires the exchange-read Agent Skill. The item on CBC Runs 4, 5 and 6 says which it uses.
- **Names:** each file is named after its part. A Maintainer Repo understanding text is titled "<part>, in this repo", as `defined-terms.md` is.
- **Layers 1 and 2 are not delivered with the Backend Kit,** decided on 2026-11-25. Delivering layer 2 alone would not spare the terms text: the Backend Kit's Defined Terms are defined in keeping knowledge and in layer 1. Delivering both is the layers document's §5, question 3, still open.
- **The Backend Kit's folders,** decided on 2026-11-25: under `knowledge/adapted-cases/cbc-backend-design/`, a folder per group, such as `keeping-knowledge/`, and in it a folder per Adapted Case, named after it, its Adapted Understanding Text and Instruction Texts together. The terms text has a folder of its own, `defined-terms/`, beside the groups. Not the Backend Repo's own layout, a `.claude/` inside `knowledge/`; not a split by kind.
- **Each Instruction Text in its final form,** decided on 2026-11-25: the file as it loads in a Backend Repo, such as a Paths Rule with its `paths:`. Delivery is a plain copy, and Read Copy Changes compares a Kit Copy with its Backend Kit file line by line. Where each kind lands in a Backend Repo is Deliver the Kit Update's, not yet written there; asked at 8d whether it goes in as an open point with its trigger, the first Kit Update carrying a file from `knowledge/adapted-cases/`.
- **Backend Kit files are `docs`, not `agent`.** They are under `knowledge/`, outside the agent's closed list of paths.
- **What stays at layer 2, a first sort,** each cut shown and decided at its boundary:
  - §4.2.2 keeps its purpose line, *Where a stretch ends*, *Two snapshots*, the three cases, what a Repo Reading holds, and *When the stop moves*.
  - §4.2.3 keeps *Who judges*, *The verdict*, the list of verdicts, and that no verdict goes down.
  - §4.2.4 keeps *What each verdict asks*, *Rewording* and *Then the stop moves*. The survey is a call shown at commit 6; my first guess is that it stays.
  - §4.2.5 keeps *When one is due*, *What a Kit Update is*, its Update Note, and *One at a time*.
  - §4.2.1 and §4.2.6, since 8a3 Change, in keeping knowledge, §3.1 and §3.6, are sorted below.
- **The Backend Repo's two parts, sorted into three places,** agreed before 8b was drafted. CK is Change, in keeping knowledge, the Maintainer Repo's view; CB is Change, in CBC backend design; Kit is the Backend Kit's Adapted Cases. Five handoffs are written in both CK and CB, each in its own words, as two Problem Domains' ideas must be.
  - *Change a Kit Copy,* §3.1:
    - when a Kit Copy changes, only where work shows a misfit, and why not ahead, at the gate or in records: CB;
    - where the Change Record sits, and what it holds: CK, since Read and Judge rely on it, and CB;
    - rewritten with its Copy Change; the commit, an Update Take's commits passing: CB;
    - the gate decides each Copy Change; main moves only at a gate: CK, already in §3.2, and CB;
    - *At the gate*'s steps, and why the gate decides: Kit, the gate's part, waiting (8c1);
    - the simulation's two "it comes back if" lines, as open points with their triggers: the session-end check, Kit, Change a Kit Copy; the gate note, with *At the gate*;
    - the open point on a reversed Copy Change leaving a trace: CK.
  - *Take the Kit Update,* §3.6:
    - taken between Plan Steps, at the next opening, after a Look for Lessons, and why not mid-step or over unjudged changes: CK, since Deliver relies on it, and CB;
    - the check, main still at the *settled snapshot*, or refused: CK and CB;
    - the taking Adapted Case taken first: CK, since the Update Note names it, and CB;
    - every Kit Copy taken whole, every Change Record going with it, and why: CK, since Read relies on it, and CB;
    - the *version snapshot* recorded: CK and CB;
    - when the Backend Kit moves on: CB;
    - the branch, items 1 to 6, the gate last, and why: Kit; the items stay in CK too, since Read relies on them (8g);
    - the open points on finished work under a changed rule, dropping an open step, and asking at each opening: CB;
    - the open point on postponing a staged Kit Update: CK;
    - where the Kit Version and the *version snapshot* are written: Kit, its trigger firing at 8f; answered there, `.claude/kit-version.md`, in CK and CB too, since Read and Deliver rely on it.
  - The gate is part of how a Backend Repo closes any Plan Step; only *At the gate* belongs here. Answered on 2026-11-25: it waits for the close, in how an agent works, in CBC backend design (8c1).
- **What moves with Change, a first sort,** decided at 8a3: the Defined Terms of a change's travel, Copy Change, Change Record, Kit Update, Update Note, Update Take, Kit Version, Look for Lessons, Repo Reading, Repo Register, Attention Note and their short forms; §4.2 and §4.3; §5's questions 2, 3, 4, 10 and 11. Staying in the layers document: Backend Kit, Kit Copy, Backend Repo, Maintainer Repo; §3; the arrows of §4.1; the picture.
- **Section numbers change with the move.** The plan names the moved sections by title from 8a3 on.
- **The boundary between the layers and Change:** a sentence still true if nothing ever changed stays in the layers; one about something added, moved or changed goes to Change. Change holds how a text is checked when an idea above it changes; the layers hold what that text must hold.
