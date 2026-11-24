# Commit plan: the Change split

## Summary — the state after all commits

Each of the six parts of how a change travels has its Adapted Case, written whole from the simulation: its Adapted Understanding Text and its Instruction Text. Today's repo is not read for them; the rewrite compares it with them later.

- **The Maintainer Repo's parts, at layer 4,** kept whole in `.claude/`: Read Copy Changes; Judge Copy Changes with Act on the verdicts; Deliver the Kit Update. Each has its understanding in `.claude/understanding/` and an Agent Skill in `.claude/skills/`.
- **The Backend Repo's parts, at layer 3,** in the Backend Kit's group for keeping knowledge, under `knowledge/adapted-cases/cbc-backend-design/`: Change a Kit Copy, and Take the Kit Update. Nothing in them names backends.

The Maintainer Repo's layers document, `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`, keeps in §4.2 what one part hands the next, the rules every part keeps, the tables, and the why of each. It no longer points at the simulation for how a rule was chosen. The simulation keeps its steps, which depth c walks, and its *Today* lines, which the rewrite reads.

What it gives: a change to one part's steps changes its own Adapted Case, and no longer reads as a change to the Problem Domain Idea. The layers stand without `temp/`.

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

**8a3. `docs: Change, in keeping knowledge, moved out`**
`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`: the Maintainer Repo's layers document's §4 moved whole, its arrows between the repos, how a change travels, and the Maintainer Repo's lessons, with the Defined Terms of a change's travel and the open questions on change. The layers document keeps the layers, where each is kept, and its picture, a key line naming Change, in keeping knowledge, and points at it. Its row in the §3.2.1 table. Every pointer to a moved section followed by script, from `docs` paths: the rename grep, unwrapped.

**8a4. `chore(agent): understanding follows Change's move`**
The three Maintainer Repo Adapted Cases, their understanding and Agent Skills, point at Change, in keeping knowledge: headers, Fact References and Borrow Tables. The agent's side of 8a3's rename grep.

**8b. `docs: Change, in CBC backend design`** (provisional)
The draft written for "the layers of knowledge, in CBC backend design", renamed and adapted from the Backbone Idea Change. Its row in the §3.2.2 table; the planned row for the layers of knowledge in CBC backend design kept or dropped at its boundary.

**8c. `docs: the Backend Kit's Defined Terms`** (provisional)
ADR-0085's decision 4 is decided here: its first guess is one terms text in the Backend Kit. A Backend Repo reads its Kit Copies without layers 1 and 2.

**8d. `docs: the Backend Kit's Change a Kit Copy case`** (provisional)
Understanding and Instruction Text, from the simulation's §3; and the gate list's part, *At the gate*. Asked here: the Backend Kit's folder layout, and each Instruction Text's form.

**8e. `docs: Change a Kit Copy keeps what it hands on`** (provisional)
Change, in keeping knowledge, its Change a Kit Copy section cut to the Maintainer Repo's view, as commit 4.

**8f. `docs: the Backend Kit's Take the Kit Update case`** (provisional)
Understanding and Instruction Text, from the simulation's §8.

**8g. `docs: Take the Kit Update keeps what it hands on`** (provisional)
Change, in keeping knowledge, its Take the Kit Update section cut to the Maintainer Repo's view, as commit 4.

**8h. `docs: the cases take their whys`** (provisional)
How each case and depth was weighed, from the simulation's §2, into Change, in keeping knowledge, its cases section. No pointer from the layers to the simulation stays.

**8i. The pictures** (provisional, likely several commits)
By the visual-comparison Agent Skill, its candidates committed before the choice, each picture showing one thing: the two layers pictures redrawn without the arrows Change took; a picture for Change, its arrows over the layers drawn plainly; one for Change, in keeping knowledge, the whole travel between the repos. A picture whose point fits in a few lines may end as none. It settles whether the simulation's picture *The whole flow* moves or goes.

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
- **Backend Kit files are `docs`, not `agent`.** They are under `knowledge/`, outside the agent's closed list of paths.
- **What stays at layer 2, a first sort,** each cut shown and decided at its boundary:
  - §4.2.2 keeps its purpose line, *Where a stretch ends*, *Two snapshots*, the three cases, what a Repo Reading holds, and *When the stop moves*.
  - §4.2.3 keeps *Who judges*, *The verdict*, the list of verdicts, and that no verdict goes down.
  - §4.2.4 keeps *What each verdict asks*, *Rewording* and *Then the stop moves*. The survey is a call shown at commit 6; my first guess is that it stays.
  - §4.2.5 keeps *When one is due*, *What a Kit Update is*, its Update Note, and *One at a time*.
  - §4.2.1 and §4.2.6 are sorted at 8e and 8g.
- **What moves with Change, a first sort,** decided at 8a3: the Defined Terms of a change's travel, Copy Change, Change Record, Kit Update, Update Note, Update Take, Kit Version, Look for Lessons, Repo Reading, Repo Register, Attention Note and their short forms; §4.2 and §4.3; §5's questions 2, 3, 4, 10 and 11. Staying in the layers document: Backend Kit, Kit Copy, Backend Repo, Maintainer Repo; §3; the arrows of §4.1; the picture.
- **Section numbers change with the move.** The plan names the moved sections by title from 8a3 on.
- **The boundary between the layers and Change:** a sentence still true if nothing ever changed stays in the layers; one about something added, moved or changed goes to Change. Change holds how a text is checked when an idea above it changes; the layers hold what that text must hold.
