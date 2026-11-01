# DEO: Dependencies, our side

The last read, at `70404e1`. One Finding Kind: Dependencies. That is a retelling where a pointer would do, a pointer not needed, a line that relies on a fact written elsewhere with no Fact Reference, or a Fact Reference to the wrong level or not to the fact's home.

Rules read first:
- facts-in-sync §1, §2, §3.1, §3.4 and §4, whole;
- idea-to-output §3.2;
- ADR-0070 decision 7 and ADR-0072;
- refinement.md §2.4 and §2.5;
- DECISION-1 to DECISION-40, both lists of the agent's calls, and ADR-0079.

21 findings: 11 checked, 8 resting on the reader, 2 uncertain.

## Findings

### DEO-1

- **Where:** `docs/conventions/conventions/README.md`, §2 *The Convention Manual*, line 176.
- **Quote:** Approaches are made usable (`ARCHITECTURE.md` §1, *What is stated here*). It explains and
- **The rule:** a Fact Reference has one target, the home of the fact. That home sits at the line's level or above. A Canonical Description's line never points at a record for a fact (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*; `docs/models/idea-to-output.md` §3.2, *The direction of a link*).
- **What the text says:** "the manual is the convention stated, from which its Work Approaches are made usable" points at `ARCHITECTURE.md`, a record. That fact's home is the Idea-to-Output Model §6.1. `ARCHITECTURE.md` §1.2 itself points up to idea-to-output §6 for it. The reference points down, at a summary.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `c53eac8` (the reference rewrite, 2026-10-28) wrote it after ADR-0071. The per-commit question should have caught it (one-home rule 6).
- **Proposed:** fix: "(`docs/models/idea-to-output.md` §6.1, *The manual's level*)".

### DEO-2

- **Where:** `docs/conventions/writing/README.md`, §2 *Why each rule*, rule 5, line 94.
- **Quote:** Skill's phase is an Agent Skill Stage (`docs/glossary.md`).
- **The rule:** one target, the fact's home, at the line's level or above (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **What the text says:** a manual points at the glossary, a record, for what an Agent Skill's phase is called. The glossary entry is only a pointer. It sends the reader on to the home, `docs/conventions/conventions/` §1.4.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `86bbea6` (2026-10-29, Names and labels) added the sentence after ADR-0070 and ADR-0071. The per-commit question should have caught it.
- **Proposed:** fix: "(`docs/conventions/conventions/` §1.4, *Agent Skill Stages*)".

### DEO-3

- **Where:** `docs/conventions/facts-in-sync/README.md`, §5 *A disagreement*, line 339.
- **Quote:** The concept's meaning has changed once since v1 (`CHANGELOG.md`).
- **The rule:** a Canonical Description's line points at a Canonical Description or an Idea Model, never at a record for a fact. A manual cites a decision inside its sentence (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*; §3.4, *A decision citation*, rule 1).
- **What the text says:** the manual points down at the CHANGELOG, a record, for the claim that the concept changed. The decision that changed it is ADR-0048, which `ARCHITECTURE.md` §1.1 already cites. This line is not DECISION-14's case: that decision covers the bump rule in the CHANGELOG's header comment, not an entry.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `5747b32` rewrote the line on 2026-11-01 and kept the pointer. The per-commit question should have caught it.
- **Proposed:** fix: "The concept's meaning has changed once since v1 (ADR-0048)."

### DEO-4

- **Where:** `docs/conventions/shapes/README.md`, §4 *An Output Shape between repos*, line 167.
- **Quote:** thing it shapes: the same rule by which an Agent Skill belongs to
- **The rule:** a retelling of another convention's subject carries a Fact Reference to its section. Without one it is a second statement (`docs/conventions/facts-in-sync/` §2, *Point and derive*).
- **What the text says:** "the same rule by which an Agent Skill belongs to exactly one group and is delivered whole" retells exchange §3.4 ("An Agent Skill belongs to one group and travels whole"). It carries no Fact Reference.
- **Stands:** checked.
- **Why it was missed:** older than the rule. `3590e39`, 2026-09-27, before facts-in-sync existed.
- **Proposed:** fix: add "(`docs/conventions/exchange/` §3.4, *One group per file*)" after "delivered whole".

### DEO-5

- **Where:** `docs/conventions/commit-plan/README.md`, §2.8 *Counting subjects*, line 118.
- **Quote:** A subject's characters are counted against the 50 limit when it is
- **The rule:** a line that relies on a fact written elsewhere carries a Fact Reference (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*). Text that touches another convention's subject points at its manual (§2, *Point and derive*).
- **What the text says:** "the 50 limit" relies on the commit-messages manual's subject limit (§2.1) and does not say where.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `103a301` (2026-11-01) rewrote the line. The per-commit question should have caught it.
- **Proposed:** fix: "against the subject's 50-character limit (`docs/conventions/commit-messages/` §2.1, *Conventional Commits*)".

### DEO-6

- **Where:** `docs/conventions/project-recording/README.md`, §7.5 *When a README changes*, line 560.
- **Quote:** item on every Plan Step Gate: 7 of the playbook's 9 Plan Steps make
- **The rule:** a line that relies on a fact points at its home, at its level or above. Where the lower text holds only one repo's specifics, the upper text says one general line. A marked example may stay (`docs/models/idea-to-output.md` §3.2, *The direction of a link*).
- **What the text says:** the manual's reason rests on a count taken from the playbook, `delivery/fills/cbc-run-pure-playbook.md`, a text below it. The count is neither marked as an example nor pointed at.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `eb57bcf` (2026-11-01) rewrote it. The direction rule, ADR-0071, came earlier.
- **Proposed:** question: is it a general line ("most of a playbook's Plan Steps make nothing true that the README says"), or a marked example ("Here, for example, 7 of the playbook's 9 Plan Steps…", with the playbook's path named)?

### DEO-7

- **Where:** `README.md`, *Out of scope*, line 56.
- **Quote:** concept chapters taken from it (`CHANGELOG.md`, *[v1]*).
- **The rule:** history is not a first home. A fact stated only in history gets a home in Living Text before anything retells it (`docs/conventions/facts-in-sync/` §1, *One home*). A released CHANGELOG entry is history (ADR-0079, decision 5).
- **What the text says:** the README rests on the released `[v1]` entry for where the chapters came from (`system-design-method`). No Living Text states it: `ARCHITECTURE.md` §1.1 does not mention the archive.
- **Stands:** checked. A grep for "archive" and "system-design-method" finds the fact only in the `[v1]` entry, the devlog and the README.
- **Why it was missed:** missed at a change. ADR-0079 made released entries history, in `f028aa8` and `71ad729`. The Change Walk on facts-in-sync §1 did not look for Living Text that rests on a released entry.
- **Proposed:** question: give the archive fact a Living home, such as `ARCHITECTURE.md` §1.1 *The concept* ("imported from `system-design-method` at `fe0075d`; the archive is a frozen snapshot, never a source"), then point the README there. Fixed with DEO-8.

### DEO-8

- **Where:** `ARCHITECTURE.md`, §3 *What must stay true*, line 212.
- **Quote:** | The concept is canonical here; the archive it came from is a frozen snapshot, never a source | §1.1, *The concept*; `CHANGELOG.md`'s `[v1]` entry | commit review |
- **The rule:** as DEO-7 (`docs/conventions/facts-in-sync/` §1, *One home*; ADR-0079).
- **What the text says:** the rule's "Stated in" names a released entry, which is history. The archive half of the rule is stated nowhere else: §1.1 says nothing of the archive.
- **Stands:** checked.
- **Why it was missed:** as DEO-7.
- **Proposed:** fix with DEO-7: once §1.1 states the archive fact, the cell reads "§1.1, *The concept*".

### DEO-9

- **Where:** `.claude/skills/commit-messages/SKILL.md`, the whole file. Quoted at *The agent's own files*, line 104.
- **Quote:** `CLAUDE.md` and `.claude/` are the working arrangement.
- **The rule:** a derived file carries a Fact Reference to the part of its foundation it uses. Where a section's lines all use one part, the section carries it once (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; ADR-0070 decision 7; ADR-0072).
- **What the text says:** the Agent Skill stands on the commit-messages manual and carries no Fact Reference to any of its parts. A grep finds 0 references. *Format* uses §2.1 and §2.2. *The agent's own files* uses §2.3. *Rules* uses §2.4. This line also relies on agent-arrangement §1.1.
- **Stands:** checked.
- **Why it was missed:** missed at a change. ADR-0072's rewrite (`ed96ed0`) gave references to four files only: `writing.md`, `exchange-reading.md`, `exchange-deliver` and `exchange-read`. The other derived files were not walked.
- **Proposed:** question: our copy is held identical to the container's (ADR-0069; DECISION-6). Should references land in both, in the form DECISION-40 gives shipped text ("the Concept Deliverer's `docs/conventions/…`")? In ours alone, breaking the identity? Or should §4 step 2 exempt a copy held identical to a shipped Master Copy?

### DEO-10

- **Where:** `.claude/skills/commit-plan/SKILL.md`, the whole file. Quoted at §4 *The lifecycle*, line 116.
- **Quote:** - **Before the close, sweep for every name the Change Set moved.** When a
- **The rule:** as DEO-9 (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; ADR-0072).
- **What the text says:** the file holds no Fact Reference to its manual. The sweep bullet retells commit-plan §2.10 and facts-in-sync §3.3 with no reference. §3 and §6 carry references only to commit-messages.
- **Stands:** checked.
- **Why it was missed:** as DEO-9. ADR-0070's consequences named "both `commit-plan` skills", but ADR-0072's rewrite left this one out.
- **Proposed:** question: as DEO-9. Ours differs from the container's by 3 hunks already, so references in ours alone are possible.

### DEO-11

- **Where:** `.claude/skills/visual-comparison/SKILL.md`, the whole file. Quoted at §1 *When this fires*, line 32.
- **Quote:** **The candidate set must contain at least one thing that is not a
- **The rule:** as DEO-9 (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; ADR-0072).
- **What the text says:** §1 restates visual-comparison §2.1 (a non-picture in the set) and §2.4 (the buildable notations). No section carries a Fact Reference to its manual.
- **Stands:** checked.
- **Why it was missed:** as DEO-9.
- **Proposed:** question: as DEO-9.

### DEO-12

- **Where:** `.claude/rules/convention-manual.md`, *The sections, in this order*, line 26 (items 1 to 4, 8 and 9).
- **Quote:** 1. **The opening statement.** One bold sentence: the manual's
- **The rule:** a section whose lines use different parts of the foundation carries a Fact Reference on each line (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; ADR-0072).
- **What the text says:** items 5, 6 and 7 point at conventions §2.5, §2.6 and §2.7. Items 1 to 4, 8 and 9 restate §2.1, §2.2, §2.3, §2.4, §2.8 and §2.9 with none. The header comment's "(§2, The Convention Manual)" gives the why of the whole file. It is not a section's reference.
- **Stands:** checked.
- **Why it was missed:** missed at a change. ADR-0072's rewrite (`ed96ed0`) did not include this file.
- **Proposed:** fix: each item gains its part: (§2.1, *The opening statement*), (§2.2, *The need*), (§2.3, *The list of what derives*), (§2.4, *The seats*), (§2.8, *The boundary*), (§2.9, *Where to look*), each with the path `docs/conventions/conventions/`.

### DEO-13

- **Where:** `.claude/decisions.md`, header comment, line 10.
- **Quote:** Division of labor: a standing rule is written as a comment in
- **The rule:** a retelling carries a Fact Reference to its source. A record's form uses a part of its foundation and carries a reference to it (`docs/conventions/facts-in-sync/` §1, *One home*; §4, *A Canonical Description's rule*, step 2).
- **What the text says:** lines 10 to 17 retell agent-arrangement §3.4 almost word for word: the rule sits in the file it governs, the log keeps the why, and "Neither repeats the other". The line's Foundation Line names agent-arrangement, but no Fact Reference is given. Every other record header carries "Why the form is as it is: (…)". This one does not.
- **Stands:** checked.
- **Why it was missed:** older than the rule. `3cad065`, 2026-08-27.
- **Proposed:** fix: before the Foundation Line, add "Why the form is as it is: (docs/conventions/agent-arrangement/ §3.4, .claude/decisions.md)". In a comment, the title takes no asterisks.

### DEO-14

- **Where:** `.claude/rules/working-a-reading.md`, *The steps*, step 7, line 70.
- **Quote:** lands where the Exchange Convention says.
- **The rule:** a line that relies on a fact written elsewhere carries a Fact Reference. A name in prose is not one (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **What the text says:** where each ending lands is exchange §6.5. The step names the convention in prose only.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change, at the reference rewrite of 2026-10-28. It looked for written references, and this line has none to rewrite.
- **Proposed:** fix: "It lands where the Exchange Convention says (`docs/conventions/exchange/` §6.5, *Verdicts*)."

### DEO-15

- **Where:** `.claude/skills/exchange-read/SKILL.md`, *What this does not do*, line 99. Also Stage 1, lines 17 to 21.
- **Quote:** the work that follows, where the Exchange Convention says each lands.
- **The rule:** as DEO-14. A derived file carries a reference per section to the part it uses (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2; ADR-0072).
- **What the text says:** line 99 names the convention in prose for exchange §6.5. Stage 1 retells exchange §2.2: the two numbers, what each is, and that the last delivery entry carries them. It has no reference. The file's one line on §6.1 covers Stage 3, not Stage 1.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. ADR-0072's rewrite (`ed96ed0`) gave this file references for some sections only.
- **Proposed:** fix: line 99 gains (`docs/conventions/exchange/` §6.5, *Verdicts*). Stage 1 opens "Why both numbers are in the CBC Run: (`docs/conventions/exchange/` §2.2, *The CBC Run*)."

### DEO-16

- **Where:** `.claude/rules/foundation-check.md`, *The check*, step 1, line 28 (and line 23).
- **Quote:** - Canonical Descriptions: `docs/models/`, `docs/conventions/*/README.md`,
- **The rule:** every line that uses a part of a document, the Foundation Line's own included, carries a Fact Reference to that part (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2).
- **What the text says:** the third bullet relies on which texts are Canonical Descriptions, from facts-in-sync §4, the file's own foundation. It carries no reference. The first bullet relies on conventions §1.3 too. Only the second bullet carries that reference, at its end.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `ecda44f` (2026-10-30) wrote the bullet after ADR-0070.
- **Proposed:** fix: move "(`docs/conventions/conventions/` §1.3, *The Foundation Line*)" to step 1's lead line, covering bullets 1 and 2. Bullet 3 gains "(`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*)".

### DEO-17

- **Where:** `.claude/rules/one-home.md`, *The rules*, rule 5, line 41.
- **Quote:** the worked example sits in the cbc-framing and cbc-slice Agent Skills, and
- **The rule:** a line that relies on a fact written elsewhere carries a Fact Reference (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **What the text says:** where the worked example's two copies sit, and that one follows the other, is stated in exchange §6.3. The rule says it with no reference.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `fab7214` (2026-11-01) rewrote the line. The sentence itself dates from `0148ce1` (2026-10-20), before the Fact Reference had a form.
- **Proposed:** fix: "…and the two must stay identical (`docs/conventions/exchange/` §6.3, *The CBC Run Reading*)."

### DEO-18

- **Where:** `concept/01-layered-system.md`, *Two readings to keep apart*, line 96. The same pattern is in `concept/03-cbc-framing.md` line 22 and `concept/04-cbc-slice.md` line 35.
- **Quote:** belongs to CBC Framing and is described there.
- **The rule:** a line that relies on a fact written elsewhere carries a Fact Reference. A name in prose is not one (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **What the text says:** the chapters lean on each other by name. Chapter 01 sends the reader to "CBC Framing" for the derivation order. Chapter 03 retells the Layered System's outside-in order. Chapter 04 uses "the ranking of Structural Walls" from chapter 02. None gives a path. A section with no number can be addressed by its title.
- **Stands:** uncertain. The five chapters may be read as one text. TODO's "Number the concept chapters' sections" says "nothing points into a chapter's section today" and waits for the first reference.
- **Why it was missed:** older than the rule. `66d28b2`, 2026-08-28.
- **Proposed:** question: do the chapters, copied whole as one concept, need Fact References between themselves? If yes, the three lines take (`concept/03-cbc-framing.md`, *The derivation order*), (`concept/01-layered-system.md`, *Two readings to keep apart*) and (`concept/02-guarantees-and-walls.md`, *The ownership map*). Each is a concept change, editorial, and fires that TODO item's trigger.

### DEO-19

- **Where:** `docs/conventions/conventions/README.md`, §3 *Adding a convention*, line 301.
- **Quote:** own (`.claude/approaches-on-trial/approach-evaluation.md`). The
- **The rule:** a Canonical Description's line points at a Canonical Description or an Idea Model, not at a Work Approach, for a fact (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*; `docs/models/idea-to-output.md` §3.2, *The direction of a link*).
- **What the text says:** "when its evaluation places a piece as a convention of its own" points down at an Approach on Trial. The step it relies on, from an Approach on Trial to a convention, is stated in idea-to-output §4.2 and §4.3. This manual's §1.3 already cites idea-to-output §4.2 for the same placing.
- **Stands:** uncertain. The pointer may only name the text that does the evaluating, and naming may go to any level.
- **Why it was missed:** older than the rule. `a9e8b961`, 2026-10-20, before ADR-0071.
- **Proposed:** question: naming or relying? If relying, use "(`docs/models/idea-to-output.md` §4.2, *The upward direction*)", with the Approach on Trial named in prose.

### DEO-20

- **Where:** `TODO.md`, *Next*, item "Read a CBC Run born before the refinement by its needs, not its diff", line 559.
- **Quote:** (`.claude/skills/exchange-read/SKILL.md`, Stage 3, *Read three things*). The
- **The rule:** a Fact Reference has one target, the home of the fact. It names the text that states the fact, not one that applies it (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **What the text says:** "a CBC Run Reading takes three things" is stated in exchange §6.1. The Agent Skill derives from it and points there itself.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `683febc` (2026-11-01) rewrote the line.
- **Proposed:** fix: "(`docs/conventions/exchange/` §6.1, *Reading a CBC Run*)".

### DEO-21

- **Where:** `TODO.md`, *Next*, item "Decide how commits cited by hash can still be regrouped", line 371.
- **Quote:** its close (`.claude/skills/commit-plan/SKILL.md` §4, *The lifecycle*), and a regroup gives them new hashes. This repo cites
- **The rule:** as DEO-20 (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **What the text says:** the look back that regroups a Change Set's commits is stated in commit-plan §2.12. The reference names the Agent Skill that applies it.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `9435842` (2026-10-30).
- **Proposed:** fix: "(`docs/conventions/commit-plan/` §2.12, *The look back*)".

## Found true, so not listed

- No ADR is cited inside a sentence in our Agent Skills, Agent Rules or Approaches on Trial. The five hits outside a footer are examples: commit-messages' code blocks, convention-manual's "*Its story: ADR-0059.*", and writing rule 6's labels.
- `exchange-reading.md`, `writing.md`, `one-home.md` and `exchange-deliver` carry their foundation's part per section (ADR-0072).
- facts-in-sync §4 points at "`CHANGELOG.md`'s standing comment" for the concept's edges. DECISION-14 made that comment the home.
- The Tiers Model §3.1 points down at `delivery/README.md`. It is a marked example ("Here, for example"), which idea-to-output §3.2 allows. model-placing's first use made it so.
- agent-arrangement §2.6, "The retrospective Agent Skill's close asks it", names what stands on it. retrospective §2 points back at agent-arrangement §2.6 as the home.
- The manuals' lines that say where drafting and evaluating are written (agent-arrangement §3.1 and §3.8; the conventions index) name a text. They do not rely on its content.
- Glossary entries with no reference (Newborn CBC Run, Made Usable) have no manual that defines them. The entry is the home.
- Record headers other than `.claude/decisions.md` carry "Why the form is as it is" to their project-recording part.
- `CLAUDE.md`'s records table comment points at project-recording §1 and §13.

## Met in passing

- `docs/conventions/conventions/README.md` line 35 and `docs/conventions/README.md` line 8 write "`ARCHITECTURE.md`…(§1.2, *The conventions*)" in the same-document form. It lands on this file's §1.2 (*An Agent Skill's frontmatter*, or none in the index). Wiring.
- `docs/conventions/commit-messages/README.md` lines 15 to 16 cite claim A1 at "`docs/models/agent.md` §12, *Claims*". A1 sits in §12.1, *Claims on the Ambient Channel*. Wiring.
- `docs/models/agent.md` line 414: "the commit-messages manual states '≤50 chars, imperative, **no period**'". The manual now says "Either mood" and says nothing of a period. Stale lines.
- `PLAN.md` lines 105, 201 and 283: "(`.claude/approaches-on-trial/approach-drafting.md`, *Stages*, §3, *Close*)" mixes a title and a number in one address. Wiring.
- The `.claude/rules/one-home.md` text loaded into this session's context lacked "`CHANGELOG.md`'s released entries". The tree has it (`71ad729`). This is not a finding of the tree.

## Not read

None. `TODO-CONVERSATION-MEMORY.md` and `.claude/decisions.md` were read by their header comments only, as assigned.
