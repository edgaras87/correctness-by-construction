# OHO: One home, our side

Reader OHO, the last read, at `70404e1`, 2026-11-01.
Finding Kind: One home. Rule homes read whole: `.claude/rules/one-home.md`; `docs/conventions/facts-in-sync/` §1, *One home*, and §3.1, *What a Fact Reference is*.
Files: the 56 of `lists/ours.txt`, each whole; `TODO-CONVERSATION-MEMORY.md` and `.claude/decisions.md` by header only. Then a grep sweep over all 118 living files for each fact seen told twice.

8 findings: 6 checked, 0 resting on the reader, 2 uncertain.

## Findings

### OHO-1

- **Where:** `ARCHITECTURE.md`, §3 *What must stay true*, line 212.
- **Quote:** `` the archive it came from is a frozen snapshot, never a source | §1.1, *The concept*; `CHANGELOG.md`'s `[v1]` entry ``
- **The rule:** history is not a first home either. A fact stated only in history gets a home in Living Text before anything retells it (`docs/conventions/facts-in-sync/` §1, *One home*; `.claude/rules/one-home.md`, *Not a second home*). A CHANGELOG's released entries are history (same §1, since `f028aa8`, ADR-0079 decision 5).
- **What the text says:** the row says where its rule is stated: §1.1 and the `[v1]` entry. §1.1 states only the first half, "canonical here". The second half, "the archive … is a frozen snapshot, never a source", is stated only in `CHANGELOG.md` lines 93 to 95, the released `[v1]` entry. So the row's first home for that half is history.
- **Both places:** the history entry, `CHANGELOG.md` `[v1]`, is the only telling. The other Living Text lines name the archive but state no rule: `README.md` line 33 is a success criterion, an aim ("the archive copy is demoted to a historical snapshot"), and line 38 another criterion.
- **Stands:** checked. A grep of all 118 files for "archive" finds the fact stated only in `CHANGELOG.md` 93–95.
- **Why missed:** missed at a change. `f028aa8` (2026-11-01) made released entries history. Its Change Walk re-read the glossary, project-recording and the refinement's §1, and did not grep Living Text for lines that cite a released entry as a home (the rename grep's "moves a fact to a new home", `docs/conventions/facts-in-sync/` §3.3). The row was reworded at `c0eb1e6`, the same day.
- **Proposed:** question: where the archive fact's living home is. Recommended: `ARCHITECTURE.md` §1.1 gains one bullet, "**Imported once.** The chapters came from the archive, `system-design-method`, at `fe0075d`; its copy is a frozen snapshot, never a source.", and the row cites §1.1 alone. Or: `README.md`'s success criterion is read as the home, and the row cites it.

### OHO-2

- **Where:** `README.md`, *Out of scope*, line 56.
- **Quote:** `` concept chapters taken from it (`CHANGELOG.md`, *[v1]*). ``
- **The rule:** as OHO-1: a Fact Reference names a living home; a released CHANGELOG entry is history and is never a first home (`docs/conventions/facts-in-sync/` §1, *One home*).
- **What the text says:** which chapters were taken from the archive is pointed at `[v1]`, a released entry. No Living Text states it.
- **Stands:** checked.
- **Why missed:** missed at a change. `943dafe` (2026-11-01) added this Fact Reference after DECISION-18 (2026-10-30) had chosen the released entry as history. Rule 6 of `.claude/rules/one-home.md`, the question at the commit, should have asked whether the target is Living Text. `f028aa8`'s Change Walk missed it again, as in OHO-1.
- **Proposed:** fix with OHO-1: the Fact Reference becomes (`ARCHITECTURE.md` §1.1, *The concept*), once §1.1 holds the import.

### OHO-3

- **Where:** `.claude/rules/one-home.md`, rule 2, lines 24–26.
- **Quote:** `copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial and the`
- **The rule:** change a fact at its home; each retelling whose Fact Reference names it is re-read in the same commit (`.claude/rules/one-home.md`, rule 4; `docs/conventions/facts-in-sync/` §1, *One home*, "A fact changes at its home"). A copy is a follower, checked against its owner (rule 5).
- **What the text says:** the rule's example retells what goes after a CBC Run Birth, with its Fact Reference to `docs/conventions/exchange/` §3.2, *What goes*. Since `3630ed9` (2026-10-31), §3.2 also lists "each group's Glossary Names, in `docs/glossary/`". The retelling leaves them out, so the follower no longer matches its home.
- **Stands:** checked. `exchange/README.md` line 205 holds the Glossary Names; `git log -S"docs/glossary/"` names `3630ed9`.
- **Why missed:** missed at a change. `3630ed9`'s body says "every list of what is delivered names the three files". Its Change Walk did not re-read this retelling, and the agent file did not follow in the next commit (`.claude/rules/foundation-check.md`, step 5). `2158499` (2026-11-01) reworded this very line and did not check it against §3.2.
- **Proposed:** fix: "After CBC Run Birth, only the copies go: Agent Skills, Agent Rules, Output Shapes, Approaches on Trial, the Glossary Names and the concept (`docs/conventions/exchange/` §3.2, *What goes*)."

### OHO-4

- **Where:** `TODO.md`, *Next*, "Unlock the folders locked for CBC Run 6", lines 47–48.
- **Quote:** `` `Read` deny rule does not stop a shell. ``
- **The rule:** retell only where the reader acts on it, with a Fact Reference to the source. Without one it is a second home (`.claude/rules/one-home.md`, rule 2; `docs/conventions/facts-in-sync/` §1, *One home*, "A copy is a follower").
- **What the text says:** the Context retells what a `Read` deny rule reaches, with no Fact Reference. The home, `docs/conventions/agent-arrangement/` §5.4, *Permission rules*, says a `Read` deny does cover shell file commands such as `cat`, `head` and `sed`, and does not cover `grep -r` or a script. The second home has drifted: "does not stop a shell" is wider than the home. `.claude/approaches-on-trial/auto-run.md` lines 70–72 retell the same fact correctly, with its Fact Reference.
- **Stands:** checked.
- **Why missed:** missed at a change. `337788a` (2026-10-29) wrote the line, after §5.4 was checked on 2026-10-24. Rule 6 of `.claude/rules/one-home.md`, the question at the commit (ADR-0070), should have asked where the fact lives.
- **Proposed:** fix, lines 47–48: "Context: CBC Run 6 must not read another repository, and a `Read` deny rule stops `cat` and `sed` but not `grep -r` or a script (`docs/conventions/agent-arrangement/` §5.4, *Permission rules*). So, before its birth,".

### OHO-5

- **Where:** `ARCHITECTURE.md`, §2.2 *The Stack Group*, lines 150–152.
- **Quote:** `` another stack takes no `spring-postgres/`; another stack's Agent ``
- **The rule:** each fact has one home; elsewhere, link, or retell with a Fact Reference (`.claude/rules/one-home.md`, rules 1 and 2). A closed ADR is history and no home (`docs/conventions/facts-in-sync/` §1, *One home*).
- **What the text says:** "A CBC Run on another stack takes no `spring-postgres/`" is the home's fact, `docs/conventions/exchange/` §3.4, *One group per file*: "a CBC Run on another stack takes the Container Group and the Method Group and leaves the Stack Group (ADR-0029)". §2.2 retells it with only ADR-0029. Others now take the second telling as the home: `delivery/README.md` §5, lines 84–85, points at `ARCHITECTURE.md` §2.2 for it. `ARCHITECTURE.md`'s own §3 row 9 points at exchange §3.4.
- **Stands:** checked.
- **Why missed:** missed at a change, reopening Refinement Round 2's FINDING-256, which moved §3's row off ADR-0029 to exchange §3.4 and left §2.2's line. `5d0f5ca` (2026-11-01) reworded the line; rule 6's question at the commit did not catch it.
- **Proposed:** fix: "A CBC Run on another stack takes no `spring-postgres/` (`docs/conventions/exchange/` §3.4, *One group per file*); another stack's Agent Skills would be a group beside this one." `delivery/README.md` line 85's Fact Reference then names exchange §3.4 (the ships reader's file; noted here so the pair is fixed together).

### OHO-6

- **Where:** `docs/conventions/conventions/` §3 *Adding a convention*, step 6, lines 320–322; and step 3, lines 309–311.
- **Quote:** `A CBC Run's Decisions Log lists, in its birth entry, the`
- **The rule:** retell only with a Fact Reference to the source (`.claude/rules/one-home.md`, rule 2); a manual never restates another convention's subject but for such a retelling (`docs/conventions/facts-in-sync/` §2, *Point and derive*).
- **What the text says:** step 6 retells that a CBC Run's Decisions Log lists its conventions in its birth entry, and that the Concept Deliverer receives none (ADR-0042). Step 3 retells that a CBC Run holds that list. The home is the agent-arrangement manual, `docs/conventions/agent-arrangement/` §3.4, *`.claude/decisions.md`*, which its own §2.1 already points at. Neither step carries a Fact Reference; ADR-0042 is the why, not the fact's home.
- **Stands:** checked.
- **Why missed:** missed at a change. `0803717` (2026-11-01) rewrote step 6's sentences; `b00ba18` (2026-10-29) step 3's. Rule 6's question at the commit should have asked where the fact lives.
- **Proposed:** fix: step 6's last two sentences become "The Concept Deliverer's Decisions Log lists no conventions, since it receives none (`docs/conventions/agent-arrangement/` §3.4, *`.claude/decisions.md`*)." Step 3's "a CBC Run holds that list, and cannot open this repo's" gains the same Fact Reference.

### OHO-7

- **Where:** `docs/models/idea-to-output.md`, §5 *An Idea Model and a concept*, lines 138–139; and §6.3 *A convention and the concept*, line 179.
- **Quote:** `only its outputs vary. A CBC Run edits its copy only after a`
- **The rule:** each fact has one home; a second telling is a link or a follower (`.claude/rules/one-home.md`, rules 1 and 5; `docs/conventions/facts-in-sync/` §1, *One home*).
- **What the text says:** the Idea Model says a CBC Run edits its concept copy only after a mistake it met, and the Concept Deliverer reads the edit. The Exchange Convention says the same, `docs/conventions/exchange/` §5.6, *Editing a chapter*: "only from a mistake lived in the CBC Run". `ARCHITECTURE.md` §1.1 points at exchange §5.6 as the home. Neither of the two tellings points at the other. The Idea Model cannot point down (`docs/models/idea-to-output.md` §3.2, *The direction of a link*), and the exchange stands on the Tiers Model, not on this one.
- **Stands:** uncertain: whether the Idea Model's line is the general idea of a concept, which the exchange would then point up to, or this repo's specific, which the Idea Model would say in one general line (ADR-0071).
- **Why missed:** the rule is unclear on an Idea Model naming this repo's actors. `9fce63c` (2026-11-01) reworded lines 138–139.
- **Proposed:** question: (a) the Idea Model's line is general: "A project edits its copy of a concept only from a mistake it met, and the concept's repo reads the edit"; exchange §5.6 points up to it. (b) It is this repo's: the line goes, and §6.3's cell points at §5's general sentence only.

### OHO-8

- **Where:** `TODO.md`, header comment, lines 23–25.
- **Quote:** `read before the Ideas are weighed. When an item changes, rewrite`
- **The rule:** retell only with a Fact Reference to the source (`.claude/rules/one-home.md`, rule 2).
- **What the text says:** TODO's form says a Conversation Memory section named in See is read before the Ideas are weighed. When a section is read is the Conversation Memory's form, its header comment, as `docs/conventions/project-recording/` §14, *Conversation Memory*, names it ("when one is read … is the file's header comment"). `TODO-CONVERSATION-MEMORY.md` lines 16–17 state it. TODO's line names the file in prose, which is not a Fact Reference (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **Stands:** uncertain: the moment is shared by two forms, and TODO's form may own it from the item's side, where a triager acts on it.
- **Why missed:** the rule is unclear on a fact two records' forms both act on.
- **Proposed:** question: TODO's line keeps its words and gains (`TODO-CONVERSATION-MEMORY.md`, its header comment); or it stays, as TODO's own fact, and the Conversation Memory's header points at TODO's.

## Found true, so not listed

- **The bump rule:** one home, `CHANGELOG.md`'s header comment (DECISION-14). `ARCHITECTURE.md` §1.1 and §3, the conventions manual §3, project-recording and exchange point at it.
- **The records at a glance:** `README.md`'s records table, `CLAUDE.md`'s records comment, the codemap and `temp/README.md` each say they summarize and name project-recording §1.
- **Commit on the word:** home in the commit-messages manual §2.4; the commit-plan manual §2.11 and §2.13, both Agent Skills and working-a-reading step 4 point at it. `CLAUDE.local.md`'s repeat is TODO's (Refinement Round 2's FINDING-194).
- **The Entry File's three tests:** home in agent-arrangement §2.4; `CLAUDE.md`'s guard comment and the Plan Step Form's close item point at it.
- **The five facts of every flow:** home in the Tiers Model §3.5; exchange §1, shapes §4.1 and `ARCHITECTURE.md` §3 retell them with Fact References.
- **Agent Skill Stages:** home in conventions §1.4; the glossary's entry retells it with a Fact Reference (the agent's call on FINDING-1176).
- **The Concept Deliverer's retrospective trial:** home in the retrospective manual's *The seats*; project-recording's seat item 1 points at it.
- **The worked example's two copies:** one-home rule 5 and exchange §6.3 name the owner, the cbc-framing Agent Skill's copy.
- **A record's description and its form:** project-recording §2.4 to §8.4 explain, each record's header states, and each header points back (DECISION-11).
- **The off-template rule:** on our side only in exchange §5.8; TODO's item points at it.

## Met in passing

- Our `commit-messages` Agent Skill, *The agent's own files*: `chore(agent)` covers Agent Skills and Agent Rules; the commit-messages manual §3 also puts Approaches on Trial under it. Agreement, if anything.
- `.claude/skills/exchange-deliver/SKILL.md` Stage 2, step 2 copies `.claude/approaches-on-trial/` and `.claude/shapes/` from every group; exchange §3.2 lists Approaches on Trial for the Container Group only and Output Shapes for the Method Group and the Stack Group. Harmless today; Agreement.
- Project-recording §1, item 12, retells its own seat item 1, "Ours has none: lessons are written back at each Plan Step's close", inside one manual. Layout (conventions §2.5).
- Agent-arrangement's *The seats* and its §3.4 both tell the birth entry's list and ADR-0042, inside one manual. Layout.
- Leftovers: none of those I met is wrong.

## Not read

None. Every file of the 56 was read whole, and the two history files by header only, as assigned.
