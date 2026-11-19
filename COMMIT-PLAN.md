# Commit plan: the knowledge step ends, its work re-cut

## Summary — the state after all commits

The Plan Step "Find how what we know stays true" is closed, after 14 days and over 500 commits in its stage 1 of 3. Its goal was the goal of the whole knowledge work, not one piece of work. That goal already stands in the problem file's §1, *The purpose*, and §7, *What would show it's solved*. Its stages and own gate items are TODO items. Main holds its branch.

What holds after it:

- **`PLAN.md` holds no Plan Step.** Four leave it: ours, closed and re-cut; "Rebuild in cbc-concept", ended; "Birth CBC Run 6", closed, its work done since 2026-10-29; "Take CBC Run 5's lessons", ended, its open items findings for the rewrite.
- **ADR-0082** holds the decisions: the knowledge work is a goal, not a Plan Step; today's Maintainer Repo is rewritten into the layers model, here; the rebuild in `cbc-concept` ends, the repo kept only as a source until checked; CBC Runs are read and judged now, by meaning, and the kit is updated during the rewrite. ADR-0081 is superseded.
- **TODO** holds the re-cut work, one item each: the problem confirmed; where common ground was lost, counted; two real cases side by side; the way chosen; "Read and judge CBC Runs 4, 5 and 6", which takes in the two reading items, the by-needs item and CBC Run 5's open lessons; `cbc-concept` checked, then dropped. Triggers that named the old steps have new ones.
- **The plan's form says a Plan Step's goal is one piece of work,** and how a step whose goal grew past one is re-cut.
- **`TODO-CONVERSATION-MEMORY.md` §31 is gone,** by the file's rule, its item closed; its open threads each stand somewhere first. The new items point at it in git, at `60f692d`.
- **The drafts no longer say they go at the Plan Step's close.** They stay until what they hold lands in the rewrite.

## Commits

On `knowledge-2026-11-05`, commits 1 to 12; then main takes the branch by fast-forward, on the reviewer's word; then commits 13 and 14 on main.

**1. `docs: <record> passes the close checks`** (provisional; one commit per kind found, none if clean)
The close items agreed on 2026-11-19, run before any other commit: links and paths, ADR cites, the pair of copies, by script; "now", "today", "not yet" and the writing rules, on the records' changed lines since `ca5c422`, the drafts in `temp/` left out; `CLAUDE.md` read top to bottom. Each kind of fix found is a commit; a fix to `CLAUDE.md` is scoped `agent`, on its own. The commit-message and agent-split checks are reported in commit 11's ticks: history is not rewritten.

**2. `docs: TODO takes §31's open threads`** (provisional; none if every thread stands somewhere)
§31 read whole. Each open thread is placed: done, naming where; a TODO item already; a stage, moving in commit 4. A thread held nowhere becomes a TODO item here.

**3. `docs: ADR-0082 re-cuts the knowledge work`**
The decisions of 2026-11-19, with the options not taken: the step kept open; the step dropped as skipped; the goal moved into the layers document; the rebuild resumed or stopped again; the readings done after the rewrite; the readings with updates now. Opens Proposed.

**4. `docs: TODO takes the knowledge step's work`**
Four items from its stages and own gate items: the problem confirmed in the reviewer's words; where common ground was lost, sorted by cause with counts; two real cases side by side; the way chosen, set against one home per fact. Stage 2's labels of `concept/` go to the item that splits the concept, which already takes them. The Notes' ideas go to the item they belong to. The layers item's Ideas gains "a source goes once all it holds has landed", by ADR-0082. Each new item's See names §31 in git at `60f692d`.

**5. `docs: TODO joins the CBC Run readings`**
"Read and judge CBC Runs 4, 5 and 6": read each apart, CBC Run 6 first, then CBC Run 4 once its folder is unlocked; judge all together, CBC Run 5's Reading re-judged by needs; by the simulation's Judge, by meaning; no old text changed, no update sent. The items "Read CBC Run 6", "Read CBC Run 4 against `dac4dd1`" and "Read a CBC Run born before the refinement by its needs" leave, their ideas carried; its See names Conversation Memory §5 and §30. CBC Run 6's commit count, 254 in TODO and 233 by git, is checked and written as it is.

**6. `docs: TODO checks cbc-concept, then drops it`**
The reviewer reads `cbc-concept` first; then the agent checks for ideas not yet taken in here; then the repo is dropped. Trigger: the Agent Model's rewrite reaches the piece of work. The Maintainer Kit item's trigger loses "the rebuild in `cbc-concept` resuming".

**7. `docs: TODO triggers outlive the knowledge step`**
Every other trigger that names the closing step gets a new one: the concept's split, the Agent Model's rewrite, line 424's lessons, and any the unwrapped grep finds.

**8. `docs: drafts outlive the knowledge step`**
The headers of the problem file, the simulation, the change flow and the frozen between-repos simulation say they go at the Plan Step's close. They now say they stay until what they hold lands in the rewrite. The layers document's §4, question 1, stops calling `cbc-concept` close to a second Maintainer Repo.

**9. `docs: a Plan Step's goal is one piece of work`** (provisional in its split)
The lesson written back: the project-recording manual's §2.4, *How a plan is written*, and `PLAN.md`'s Plan Step Form. A goal grown past one piece of work is re-cut: the own items struck, each naming its TODO item. The manual is a Canonical Description, so the Foundation Check's Change Walk runs. If it reaches the CBC Run's playbook form, that follows in this commit or the next, with `CHANGELOG.md` if a shipped file changes.

**10. `chore(agent): auto-run notes CBC Run 6's birth`**
The auto-run Approach on Trial's dated note of its second use, the close item Birth CBC Run 6 still owes.

**11. `docs: PLAN strikes the knowledge step's items`**
Ours: its four own items struck, each naming its TODO item; the Goal line's note, re-cut 2026-11-19; the close items ticked, item 4 and 5's narrowing to records and item 8's one lesson said, as one-time choices. Birth CBC Run 6: its close items ticked. The commit-message and agent-split results, counted by script.

**12. `docs: ADR-0082 accepted, ADR-0081 superseded`**
The final records commit: ADR-0082 flips to Accepted; ADR-0081's status names it.

**13. `docs: PLAN closes the knowledge step`** (on main, after the fast-forward)
Removes the four Plan Steps from `PLAN.md`; deletes `TODO-CONVERSATION-MEMORY.md` §31; adds the devlog entry for the close, naming what diverged and the commit that holds the ticked Plan Step Gates.

**14. `docs(agent): close commit plan for the step's end`** (on main)

## Decisions taken inside this plan

- **The checks run first,** so their fixes land before the records that tick them.
- **§31's threads are placed before §31 goes,** so no open thread is lost with it.
- **The ADR opens Proposed** and flips in commit 12, after the TODO and PLAN commits it describes.
- **Four Plan Steps leave in one commit on main,** as the form's close: nothing is recorded before the fast-forward that it would make untrue.
- **The new items point at §31 in git at `60f692d`,** a commit that holds it whole; §31 has not changed since 2026-11-12.
- **The session's own devlog entry and its memory check come after the plan's close,** as a separate commit, not part of this plan.
