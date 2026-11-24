# Commit plan: the Maintainer Repo's side of the Change split

## Summary — the state after all commits

The Maintainer Repo's layers document, `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`, keeps in §4.2.2 to §4.2.5 only what each part hands the next, and the rules every part keeps. The Maintainer Repo's own steps for those parts sit in three Adapted Understanding Texts of its own, at layer 4, in `.claude/understanding/`:

- `read-copy-changes.md`, for Read Copy Changes;
- `judge-copy-changes.md`, for Judge Copy Changes and Act on the verdicts;
- `deliver-the-kit-update.md`, for making and staging a Kit Update.

Judge Copy Changes has its Instruction Text too, an Agent Skill, `.claude/skills/judge-copy-changes/`. Read and Deliver have none yet: each header says so, and the exchange-read and exchange-deliver Agent Skills do that work until the rewrite.

What it gives: a change to one of the Maintainer Repo's steps changes its own Adapted Case, and no longer reads as a change to the Problem Domain Idea. §4.2.1 and §4.2.6, the Backend Repo's parts, stand as they are, for the second Change Set.

## Commits

**1. `docs(agent): add commit plan for Maintainer split`**
The approved plan.

**2. `docs: ADR-0087, the Maintainer Repo's Change split`**
Proposed. Decision-first: what is settled in the chat. The Maintainer Repo's parts go to its own Adapted Cases at layer 4. Two Change Sets, this one first. Judge gets its Instruction Text now, and depth c rewrites it if it must; Read and Deliver get understanding only. One Adapted Understanding Text per part. Rejected: one Change Set; Instruction Texts for all three; none for any.

**3. `chore(agent): add Read Copy Changes understanding`**
`.claude/understanding/read-copy-changes.md`, from §4.2.2's own steps, its open point with them. Its header names the layer-2 document as what it stands on, and the exchange-read Agent Skill as what does the work until its Instruction Text is written. Lands before the cut, so no step is lost between commits.

**4. `docs: Read Copy Changes keeps what it hands on`**
§4.2.2 cut to what stays at layer 2. The layer-2 header names what stands on it. Pointers into the moved paragraphs followed: from `temp/`, to the understanding text; from text that stays at layer 2, reworded, since layer 2 never points down.

**5. `chore(agent): add the Judge Copy Changes case`**
`.claude/understanding/judge-copy-changes.md`, from §4.2.3's and §4.2.4's own steps; the Agent Skill built on it; its `.claude/decisions.md` entry, which names the other two understanding texts too. Asked here, since its trigger fires: §4.2.4's open point, whether Act on the verdicts gets an Adapted Case of its own, and whether a Look for Lessons is one of the Maintainer Repo's Plan Steps.

**6. `docs: Judge and Act keep what they hand on`**
§4.2.3 and §4.2.4 cut, as commit 4.

**7. `chore(agent): add Deliver understanding`**
`.claude/understanding/deliver-the-kit-update.md`, from §4.2.5's own steps, making and staging both. Its header names the exchange-deliver Agent Skill, as commit 3.

**8. `docs: Deliver keeps what it hands on`**
§4.2.5 cut, as commit 4. Its *Its Adapted Cases* becomes one, with two Instruction Texts to come.

**9. `docs: TODO follows the Maintainer split`** (provisional)
The split item keeps the Backend Repo's side only. The item on CBC Runs 4, 5 and 6 judges by the Agent Skill, not the simulation. Any open point the cuts answer, or move, followed. Wording and content set at its boundary.

**10. `docs: ADR-0087 accepted`**

**11. `docs(agent): close plan for the Maintainer split`**
After the sweep and the look back. The body names what diverged.

## Decisions taken inside this plan

- **Add, then cut.** Each part's understanding text lands first, in `agent`; its cut follows, in `docs`. For one commit both hold the steps, and none is ever missing. The other order leaves the steps nowhere for one commit.
- **Three understanding texts, not four.** §4.2.5 names two Adapted Cases, making and staging a Kit Update. With no Instruction Text yet, staging alone is one paragraph. One understanding text under two Instruction Texts is what §5, question 8, allows.
- **Names:** each file is named after its part, and titled "<part>, in this repo", as `defined-terms.md` is.
- **No `.claude/decisions.md` entry for commits 3 and 7.** An understanding text never loads, so the agent's setup does not change. The entry comes with the Agent Skill, in commit 5.
- **What stays at layer 2, a first sort.** Each cut is drafted and shown at its boundary, and decided there:
  - §4.2.2 keeps its purpose line, *Where a stretch ends*, *Two snapshots*, the three cases, what a Repo Reading holds, and *When the stop moves*. Goes: *How it starts*, the two checks at main, *Finding each Copy Change*, the checked list, its open point.
  - §4.2.3 keeps *Who judges* and *The verdict*, the list of verdicts, and that no verdict goes down. Goes: question 0, the four questions, *From the reason, never the wording*, *Lines together, lines split*, *A line with no Change Record*, its open points.
  - §4.2.4 keeps *What each verdict asks*, *Rewording* and *Then the stop moves*. The survey is a call shown at commit 6: it is the arrow *adapt*'s check across every text built on an idea, so my first guess is that it stays.
  - §4.2.5 keeps *When one is due*, *What a Kit Update is*, its Update Note, and *One at a time*. Goes: *When the check runs*, and *Staging*'s steps.
- **The picture waits for the second Change Set.** The whole travel at layer 2 is known only once both sides are cut.
