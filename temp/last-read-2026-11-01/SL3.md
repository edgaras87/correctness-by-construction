# SL3: Stale lines, layer 6 (the container, `delivery/README.md`, the playbook, the Pure Seed)

Reader SL3. Finding Kind: Stale lines, a line no longer true. Read at `70404e1`, all 28 files whole. The rule: none needed, a false line is wrong (`temp/refinement-2026-10-18.md`, *The last read*, *The rules' check (§2.3)*, the Stale lines row). The leftovers marked "stands" in the leftovers list are not listed again.

6 findings: 4 checked, 2 resting on the reader, 0 uncertain.

## Findings

### SL3-1

- **Where:** `delivery/installs/pure-seed.md`, the reader's checklist after step 6 ("What the agent is left to do"), line 329.
- **Quote:** `- Step 0 closed clean on the Plan Step Gate the container wrote for`
- **The rule:** a false line is wrong (Stale lines needs no rule).
- **What the text says:** the container wrote Step 0's Plan Step Gate. Nothing writes it. The Pure Seed replaces the PLAN Record Stub's placeholder Plan Steps, its Step 0 Gate with them, with the playbook's (`pure-seed.md` lines 161-164). The playbook's Step 0 has an empty `Gate:` (`delivery/fills/cbc-run-pure-playbook.md` line 148), and its Plan Step Form says the Plan Step Gate is written when the Plan Step opens (line 58). So the agent writes Step 0's Gate.
- **Stands:** checked.
- **Why it was missed:** missed at a change. Playbook v3 (2026-09-06) stripped Step 0's gates to "derived when this step opens"; the line, then "Step 0 closed clean on its container gates", was already false at `f9342dd`. `5d562d8` reworded it to name the Plan Step Gate and did not check the claim. Round 1's Stale lines read and its close read missed it too.
- **Proposed:** fix: "- Step 0 closed clean on the Plan Step Gate the agent wrote when it opened. No Plan Step Gate waits on the CBC Run Briefing: it opens CBC Framing."

### SL3-2

- **Where:** `delivery/installs/pure-seed.md`, step 4's bold lead, line 123; also line 6 and line 122.
- **Quote:** `Delivery Pin in the subjects.** One commit per delivery. The subject`
- **The rule:** a false line is wrong.
- **What the text says:** one commit per delivery (123); "commit the deliveries there" (122); "Every delivery is a commit on a Receipt Branch" (6). The same file says the CBC Run holds one delivery (line 94, "One Delivery Pin, because the CBC Run holds one delivery"; the prompt, lines 211-212, "one delivery ... in two halves"), and step 4 makes four commits of it (line 290, "Four commits on birth-seed").
- **Stands:** checked.
- **Why it was missed:** missed at a change. The words date from `f9342dd` (2026-09-07), when the seed made "the five deliveries". ADR-0025 and ADR-0036 made the container part of one delivery at one Delivery Pin; lines 94 and 173-175 were brought to that, these three were not. `5d562d8` reworded all three and kept the claim.
- **Proposed:** fix:
  - line 6: "The delivery is committed on a Receipt Branch, `birth-seed`, in four commits. That"
  - lines 122-123: "**4. Cut the Receipt Branch and commit the delivery there, the Delivery Pin in every subject.** One commit per part of the delivery. The subject"

### SL3-3

- **Where:** `delivery/container/docs/glossary/container.md`, the Decisions Log entry, line 91.
- **Quote:** `  decisions, the conventions held, and each delivery's Delivery Pin`
- **The rule:** a false line is wrong.
- **What the text says:** the Decisions Log holds "the conventions held". Since ADR-0078 (DECISION-32) a convention is its manual, and a CBC Run holds none, only the Work Approaches made from them. Leftover G3 lists the same claim in `decisions.md` 35-37, `.claude/CLAUDE.md` 54 and the Pure Seed, but not this line.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `3630ed9` (2026-10-31) moved the entry into this file the same day ADR-0078 was written; the Change Walk from ADR-0078 did not reach it, and Round 3's close read (reader G) listed its siblings and not this one.
- **Proposed:** question: fix it in the same words as G3's lines, in the same commit, so the four say one thing.

### SL3-4

- **Where:** `delivery/README.md`, §6 *When it lands*, line 90.
- **Quote:** `that run much later. Each Agent Skill's Stage 0 refuses to start`
- **The rule:** a false line is wrong.
- **What the text says:** every Agent Skill's Stage 0 refuses to start before its inputs exist. True of cbc-slice, cbc-bootstrap, infra-establish and infra-serve. False of the others that copy at birth:
  - the retrospective and apply-retrospective Agent Skills, for Plan Steps N-2 and N-1: their Stage 0 cuts a branch and opens the work, and checks no input;
  - the cbc-framing Agent Skill: its Stage 0 chooses the Falsifiable Promise;
  - commit-messages, commit-plan and visual-comparison: no Stage 0.
- **Stands:** checked.
- **Why it was missed:** missed at a change. Before `5d562d8` the line read "Each practice skill's readiness gate refuses to start", which was true of the Stack Group. The rewording to Glossary Names widened "practice skill" to every Agent Skill.
- **Proposed:** fix: "that run much later. The Stage 0 of the cbc-slice Agent Skill and of the Stack Group's three Agent Skills refuses to start" (the rest of the sentence as it stands).

### SL3-5

- **Where:** `delivery/container/.claude/rules/delivered-copies.md`, the frontmatter's `paths:` list, lines 2-8 (line 7 quoted).
- **Quote:** `  - "docs/concept/**"`
- **The rule:** a false line is wrong.
- **What the text says:** the `paths:` list names the delivered places, so the Agent Rule loads when a copy is touched. It omits `docs/glossary/**`. Rule 1 of the same file (lines 26-28) says the delivered Glossary Names in `docs/glossary/` are pinned copies under one Delivery Pin. An edit to `docs/glossary/method.md` loads no rule that says it is a copy.
- **Stands:** resting on the reader (whether a `paths:` list counts as a claim of what is delivered).
- **Why it was missed:** missed at a change. `3630ed9` made the delivered Names pinned copies, and its body says "every list of what is delivered names the three files"; it changed rule 1 and left the `paths:` list.
- **Proposed:** fix: add `  - "docs/glossary/**"` after line 7. The pattern matches the folder only, not the CBC Run's own `docs/glossary.md`.

### SL3-6

- **Where:** `delivery/installs/pure-seed.md`, step 6's prompt, line 215; also the check after it, lines 290-292.
- **Quote:** `- then docs/concept/, five method and stack Agent Skills, the`
- **The rule:** a false line is wrong.
- **What the text says:** the prompt lists what the second half of the delivery holds: the concept, five Agent Skills, four Output Shapes, the Plan Steps. The third seed commit also adds `docs/glossary/method.md` and `docs/glossary/stack.md` (line 158, `git add ... docs/glossary`). The check at lines 290-292 lists the same commit as "the method and stack Agent Skills with the method's Output Shapes", without them.
- **Stands:** resting on the reader (a list that reads as whole, short by two files).
- **Why it was missed:** missed at a change. `3630ed9` created the two files and added `docs/glossary` to line 158. It did not update the prompt or the check, though its body says every list of what is delivered names the three files.
- **Proposed:** fix:
  - line 215-216: "- then docs/concept/, five method and stack Agent Skills, the method's four Output Shapes, their Glossary Names, and the Plan Steps in PLAN."
  - line 292: "Agent Skills with the method's Output Shapes and their Glossary Names, the Plan Steps into PLAN."

## Found true, so not listed

- Every Fact Reference in the 28 files lands on a heading of that number and title: exchange §3.2, §3.3, §3.7, §3.8, §5, §5.8; shapes §4; project-recording §2.4, §3.4, §4.4, §5.4, §6.4, §7.4, §8.4, §13; agent-arrangement §2.4, §3.4; `ARCHITECTURE.md` §2, §2.2; shapes-lifecycle §1, §3, §4; commit-plan §4, §6; commit-messages *The agent's own files*; delivered-copies rules 2 and 5 by their bold leads; approach-drafting *Stages* §3 *Close*; the playbook's *At the close*; retrospective Stage 2 item 4 (the decision block).
- Every path a shipped file names exists in a CBC Run's tree after the Pure Seed, `docs/system/` aside, which the cbc-framing Agent Skill creates. Our own paths named in shipped text are labelled the Concept Deliverer's (`approach-evaluation`, `model-placing.md` and `4fedbb3` exist).
- The Pure Seed's script against the container: every placeholder it fills exists exactly once (`<delivery-pin>`, `<YYYY-MM-DD> Born`, `Date: <YYYY-MM-DD>`, `## <YYYY-MM-DD>`, `<working-name>` in both composed files, `<playbook> v<N> at <concept commit>`); the playbook's `## The Plan Step Form` and `Playbook version: v11` match its `sed`s; the five placeholders, the four commits, the five Agent Skills, the four Output Shapes, `docs/baselines/cbc-derived-claude-walk1.md` and devlog 2026-09-06 "the pure seed runs" all hold.
- `decisions.md`'s list of 11 conventions matches the Foundation Lines the container carries, repo-hygiene through the Hygiene Base. The counts "one Delivery Fill", "four Output Shapes", "five Agent Skills", "three files" in `docs/glossary/` hold.
- The playbook's v11 line: the edits since 2026-10-30 are rule fixes, not lessons, so no bump was owed.
- `commit-messages`' "`CLAUDE.md` and `.claude/`" and `container.md`'s Entry File "`CLAUDE.md`": a CBC Run's Entry File sits at `.claude/CLAUDE.md`, but both lines name the file, which is true, and the first is one text in both seats by DECISION-6.

## Met in passing

- `delivery/container/.claude/rules/one-home.md` lines 12-13: "the Concept Deliverer's facts-in-sync manual (CBC docs/conventions/facts-in-sync/ §1 …" still carries "CBC docs/", which DECISION-40 replaced with "the Concept Deliverer's" at each such line. Wiring or Dependencies.
- G7's `retrospective/SKILL.md` line 118 and the Pure Seed: confirmed still standing; and the playbook's Step 0 `[~]` with an empty Gate is consistent with SL3-1's fix.

## Not read

None. All 28 files read whole.
