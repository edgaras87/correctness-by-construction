# LAS: Layout, what ships

Reader LAS. Finding Kind: Layout. Read at `70404e1`.

Rule homes read whole: `docs/conventions/conventions/` §1.4, §2.5;
`docs/conventions/facts-in-sync/` §3.2; `.claude/approaches-on-trial/refinement.md`
§2.4, §2.5. Decisions read: DECISION-1 to DECISION-40, both lists of
the agent's calls, ADR-0079, *Before the readers* and the leftovers list.

The reach, as I read it. DECISION-8 took Layout to the descriptions
and to the files derived from a convention. It left the method's and
the stack's texts to the plain rewrite. DECISION-16 then made Refinement
Round 3 that rewrite, but Round 3 read Writing only. So Layout never read
the method's and the stack's texts after FINDING-227 and 228. I read them
here, as the last read's setup assigns. Each finding on them says so.

12 findings: 4 checked, 6 resting on the reader, 2 uncertain.

## Findings

### LAS-1

- **Where:** `delivery/README.md`, §2 *Three ways a file lands*, lines 26–56; quote at line 30.
- **Quote:** `- **Pinned copies:**`
- **The rule:** a section divided into labelled parts numbers them, `### N.M`. A bold-led bullet is a part when it holds a paragraph of its own (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*; DECISION-15).
- **What the text says:** §2 is three bold-led bullets, each a paragraph: the CBC Run's own from birth, pinned copies, Delivery Fills. They are its three parts, unnumbered. The paragraph on Agent Skill Templates (49–51) is about pinned copies, but stands after the third part's table. The paragraph on the method's own files (53–56) is about files the CBC Run writes, not a way a file lands.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule's bold-lead line (`aa40496`, DECISION-15), which left all but 16 named sections to this read. Refinement Round 2's Layout reader read layer 6's Agent Skills, Agent Rules, Output Shapes and references, not this page.
- **Proposed:** fix: `### 2.1 Own from birth`, `### 2.2 Pinned copies`, `### 2.3 Delivery Fills`, the Agent Skill Templates paragraph moved into 2.2. Question: where the method's-own-files paragraph goes; recommended §1, *The groups and the tree*, which says where things sit in the tree. `docs/models/tiers.md` line 94 points at §2 and still lands.

### LAS-2

- **Where:** `delivery/README.md`, §2 *Three ways a file lands*, line 36.
- **Quote:** `  - the concept, at `docs/concept/``
- **The rule:** a subject has one section. Other sections point at it, and do not tell it again (`docs/conventions/conventions/` §2.5, *The body*).
- **What the text says:** where the concept lands is §3's subject, *The one exception*. §2's list tells it again, with no pointer.
- **Stands:** resting on the reader.
- **Why it was missed:** older than this read. Refinement Round 2's Layout read did not take this page (LAS-1).
- **Proposed:** fix: `  - the concept (§3, *The one exception*)`.

### LAS-3

- **Where:** `delivery/container/.claude/skills/commit-plan/SKILL.md`, §3 *How the commits are split*, line 81; the same form in §2 (lines 59–70) and §4 (lines 112–130). Our copy, `.claude/skills/commit-plan/SKILL.md`, has the same lines.
- **Quote:** `- **Order follows where the decision lives.** A decision settled in`
- **The rule:** a bold-led bullet with a paragraph of its own and its own reason is a part. A section of parts numbers them, and so does every section of the same form in the document (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
- **What the text says:** §3's four bullets each hold a paragraph with its reason. §2 has two such bullets ("The list may change past a point", "A planned commit may repeat over a series"). §4 has three ("An ADR inside the Change Set opens as Proposed", the sweep, the look back). None is numbered. The commit-plan manual gives the same subjects numbered parts: §2.4 *Material-first*, §2.5 *The records commits*, §2.7 *Inserted and repeated commits*, §2.10 *The sweep*, §2.12 *The look back*.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule's bold-lead line (`aa40496`). Refinement Round 2's Layout reader read this Agent Skill before the line existed. DECISION-15 left the rest to this read.
- **Proposed:** question: (a) number §2's, §3's and §4's parts; or (b) cut each bullet to a short item, its reason left to the manual's numbered part. Recommended (b): DECISION-7 reads facts-in-sync §4 as "a derived file applies, it does not explain", and the manual already holds each reason. Both copies change together.

### LAS-4

- **Where:** `delivery/container/.claude/skills/commit-plan/SKILL.md`, §6 *Review protocol*, line 151. Our copy has the same lines.
- **Quote:** `**Small commits inside a planned commit, where the reviewer has`
- **The rule:** each numbered section holds one subject (`docs/conventions/conventions/` §2.5, *The body*). A labelled part is numbered (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
- **What the text says:** §6 holds two subjects: the stop at every boundary (147–149), and small commits with the `-detail` branch (151–161), marked by a bold lead. All three pointers into §6 mean the second subject: §4's table row, `retrospective/SKILL.md` line 125 and `apply-retrospective/SKILL.md` line 142. They name it *Review protocol*, since it has no title of its own. The manual splits the two: §2.11 *Small commits*, §2.13 *The stop at every boundary*.
- **Stands:** resting on the reader.
- **Why it was missed:** the rule is unclear. DECISION-15 named this bold lead as an open question, and §3.2's line speaks only of bullets.
- **Proposed:** question: (a) `### 6.1 The stop at each boundary` and `### 6.2 Small commits`, with the three pointers made §6.2 *Small commits*, in both copies of commit-plan and in both retrospective Agent Skills; or (b) small commits become §7, and the anti-patterns §8. Recommended (a): no section renumbers.

### LAS-5

- **Where:** `delivery/container/.claude/skills/visual-comparison/SKILL.md`, §1 *When this fires*, line 32. Our copy has the same lines.
- **Quote:** `**The candidate set must contain at least one thing that is not a`
- **The rule:** each numbered section holds one subject, and a subject has one section (`docs/conventions/conventions/` §2.5, *The body*).
- **What the text says:** §1 holds three subjects: when the comparison fires (28–30, 43–47); the rule that the candidate set holds a non-picture (32–35); and which notations a project can build (37–41). The candidate set's rule is told again in §2, step 2 (lines 59–60) and step 3 (62–64). The manual gives each its own part: §2.1 *A non-picture in the set*, §2.4 *The buildable notations*.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at Refinement Round 2's Layout read, which read layer 6's Agent Skills whole. The lines are from `2505f78` and `b3c35a6`, before it.
- **Proposed:** question: (a) the candidate set's rule moves to §2, step 3, as its one home; the buildable notations get a section of their own; §1 keeps when it fires; or (b) §1 is retitled to cover all three. Recommended (a). Both copies change together.

### LAS-6

- **Where:** `delivery/container/.claude/skills/visual-comparison/SKILL.md`, §4 *What the render has caught*, line 99. Our copy has the same lines.
- **Quote:** `- **The dialect built for the job can be the one that fails.**`
- **The rule:** a bold-led bullet with a paragraph of its own and its own story is a part, and parts are numbered (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*; DECISION-15).
- **What the text says:** §4's five entries are bold-led bullets. Each holds a paragraph and the case it came from, as §4's own lead asks. None is numbered. The *Decisions* footer, in both copies, points at one by quoting it: "§4's 'using a dialect is not fighting it'".
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule's bold-lead line (`aa40496`).
- **Proposed:** fix: `### 4.1` to `### 4.5`, each titled by its subject, in both copies; the footer line points at §4.5.

### LAS-7

- **Where:** `delivery/method/.claude/skills/cbc-framing/SKILL.md`, *Export and handoff*, lines 184–294; *The record*, lines 128–182.
- **Quote:** `## Export and handoff`
- **The rule:** a section holds one subject, and a subject has one section (`docs/conventions/conventions/` §2.5, *The body*).
- **What the text says:** the section holds 7 subjects: the 3 export files; reading each alone at the close; the CBC Framing Export Filter; the commit order; the Invariant Slice Registry's outcomes and its Agent Skill Template; the exports as living records; the README; and the handoff to the Runtime Ground. The exports' draft line is split across the two sections: added in *The record* (line 148), removed here (195–196). This is FINDING-227's first part, still standing.
- **Stands:** checked.
- **Why it was missed:** missed at a change. DECISION-8 moved FINDING-227 to the plain-rewrite item. DECISION-16 put it in Refinement Round 3's layer 6. `4884a12`, cbc-framing's Agent Skill in Round 3, did not work it, and Round 3's endings say it was worked.
- **Proposed:** question: split by subject. For example: *The CBC Framing Exports* (files, draft line, reading alone, living records, the filter), *The commit order*, *The Invariant Slice Registry's outcomes*, *The README*, *The handoff*. Or leave it to the plain-rewrite item, which still names it.

### LAS-8

- **Where:** `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md`, *Records and outputs*, line 179; also its Stage 6 Gate (lines 109–113); `references/establishment-walk.md` Stage 6 (158–168); `references/postgres-setup-walkthrough.md` §9 (225–228).
- **Quote:** `  - `infrastructure-contract.md`, the Infrastructure Contract: the`
- **The rule:** a subject has one section. Other sections point at it, and do not tell it again (`docs/conventions/conventions/` §2.5, *The body*).
- **What the text says:** what the Infrastructure Contract holds is told in four places. Two are in one file. The lists differ: the Agent Skill gives 4 items, and the walk gives 5, adding "what Infrastructure Services exist". `infra-serve/SKILL.md` lines 70–73 name *Records and outputs* as the form's home. This is FINDING-227's second part, still standing.
- **Stands:** checked.
- **Why it was missed:** missed at a change, as LAS-7. `580f7dc`, infra-establish in Refinement Round 3, did not work it.
- **Proposed:** question: one home. Recommended *Records and outputs*, which infra-serve already points at, carrying the walk's fifth item if the reviewer keeps it. The Stage 6 Gate, the walk's Stage 6 and the setup walkthrough's §9 then point at it.

### LAS-9

- **Where:** `delivery/method/.claude/skills/cbc-framing/references/worked-example.md`, *Part 2*, line 256; the copy, `delivery/method/.claude/skills/cbc-slice/references/worked-example.md`, is byte-identical.
- **Quote:** `**Stage 1, specify-correctness,** takes the Invariant Slice Entry`
- **The rule:** every section of the same form in a document numbers its parts the same way, so a reader meets one structure (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
- **What the text says:** Part 1 gives each Agent Skill Stage a heading, `## Stage 0 — …` to `## Stage 6 — …`. Part 2's four Agent Skill Stages are bold-led paragraphs (lines 256, 281, 296, 306). This is FINDING-227's third part, still standing.
- **Stands:** checked.
- **Why it was missed:** missed at a change, as LAS-7. `8316ce0`, cbc-framing's references in Refinement Round 3, did not work it.
- **Proposed:** fix: `## Stage 1 — specify-correctness`, `## Stage 2 — plan`, `## Stage 3 — build`, `## Stage 4 — document` under Part 2, in cbc-framing's copy first, then cbc-slice's word for word.

### LAS-10

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, §4 *The Adversity Harness*, line 134; also line 164.
- **Quote:** `### The test runtime (once per machine; the Operator Manual's)`
- **The rule:** a section divided into labelled parts numbers them, `### N.M` (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
- **What the text says:** §4 has two parts with headings and no numbers, where §1 to §5 are numbered. The harness reference's three Fact References into it name the part by title and label: "step 4, *The Adversity Harness in the codebase*, *Traps, exact*, item 3" (`spring-harness-reference.md` lines 151–152, 158–159, 207–208). This is FINDING-228, still standing.
- **Stands:** checked.
- **Why it was missed:** missed at a change. FINDING-228 was proposed "fix, 4.1 and 4.2", and DECISION-8 moved it to the plain-rewrite item. DECISION-16 put it in Refinement Round 3's layer 6. `63bb1db`, cbc-bootstrap in Round 3, did not work it.
- **Proposed:** fix: `### 4.1 The test runtime` and `### 4.2 The harness in code`. Writing rule 10 then applies: the parenthesis goes, and the second title is 37 characters. The three pointers become "step 4.2, *The harness in code*", with the rename grep.

### LAS-11

- **Where:** `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`, §1 *The database base*, line 139, under "**Bound facts.**" (line 131). The same in §2 to §4, and elsewhere as listed below.
- **Quote:** `- **The mounted `bootstrap.sql` is the one source.** The Adversity`
- **The rule:** §3.2's line covers a bold-led bullet. DECISION-15 named "bold labels on their own line" as the same question, and left them to this read (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
- **What the text says:** labels that recur in every section of one form, and the bold-led bullets under them, each with its own reason. Counted:
  - the harness reference, "**Bound facts.**" in §1 to §4, then 6, 2 (numbered), 3 and 5 bold-led bullets; §5, 4 more;
  - the walkthrough, "**Verified:**" and "**Traps:**" in each step, and §5's "**As one CBC Run built it:**" with 6 bold-led bullets;
  - the setup walkthrough, §9's two bold-led paragraphs (186, 213) and §6's trap (130);
  - `apply-retrospective/SKILL.md`'s "**How a row is decided:**" (48) and "**The plain pass,**" (95), which DECISION-15 named. I judge these two not parts: they sit inside an Agent Skill Stage, which is a label of its own, not a numbered section (`docs/conventions/conventions/` §1.4, *Agent Skill Stages*).
  Read as parts, the harness reference's §1 alone needs 6 numbers.
- **Stands:** uncertain.
- **Why it was missed:** the rule is unclear. The line says nothing of a label on its own line or a bold-led paragraph. DECISION-8 kept the stack's texts out of Layout's reach until the plain rewrite. The setup walkthrough's §9 got its second bold-led paragraph in `580f7dc`, after the line stood.
- **Proposed:** question: (a) a label that recurs in every section of one form, and the bullets under it, are that form's fixed labels, as an Output Shape's *Skeleton:* is. A bold-led paragraph outside such a form is judged as a bullet is. §3.2 gains that line. (b) Each is a part and is numbered. Recommended (a). Under (a), only the setup walkthrough's §9 and the walkthrough's §5 are left to judge.

### LAS-12

- **Where:** `delivery/installs/pure-seed.md`, after step 6, line 287; also step 5, lines 201–204.
- **Quote:** `**A correct Pure Seed is checkable.** Before the agent starts, every`
- **The rule:** a subject has one section (`docs/conventions/conventions/` §2.5, *The body*).
- **What the text says:** the Pure Seed's numbered steps are its only parts. The seed's check says it runs "before the agent starts", but it stands after step 6, *Start the agent*. After it come the CBC Run Reading's checklist (316–333) and the CBC Run Reading itself (335–338): two more subjects in step 6. Step 5 holds part of the same check (201–204), which the later list points back to: "the check in step 5 lists nothing".
- **Stands:** uncertain. Is the Pure Seed in Layout's reach? DECISION-8 named the descriptions: the manuals, the models, `ARCHITECTURE.md`, the concept. The page has no headings, so where step 6 ends is read from its bold leads.
- **Why it was missed:** older than this read. Refinement Round 2's Layout read did not take this page.
- **Proposed:** question: (a) the check becomes step 6, *Check the seed*, holding lines 201–204 and 287–314. Starting the agent becomes step 7, and the CBC Run Reading's checklist closes the page under a label of its own. The one pointer that moves is "step 6's prompt" (line 299). (b) It stays. Recommended (a).

## Found true, so not listed

- `shapes-lifecycle.md` §1 to §6: one subject each. §1's two questions and §3's four endings are short list items, not parts.
- `delivered-copies.md`, `one-home.md`, `writing.md`: their numbered rules are rules, not sections. Their headed sections hold one subject each.
- `approach-drafting.md`: its Approach on Trial Stages each sit under their own numbered heading. *Not known yet* is an unnumbered form section, with no N.M to give.
- `commit-messages`, `retrospective`, `apply-retrospective`: each Agent Skill Stage or section holds one subject. retrospective's *Rules for a decision* is the content rule for Stage 2's decisions, one subject.
- The four Output Shapes: no numbered sections. *Two layers* and *Skeleton:*/*Illustration:* are the shapes manual's form (§4.2, *An Output Shape's two layers*).
- `cbc-slice/SKILL.md`, its workflow, `system-readiness.md`, `the-whole-system-in-plain.md`, `cbc-bootstrap/SKILL.md`, `infra-serve/SKILL.md`, `app-structure.md`, `spring-pom-convention.md`, `postgres-role-split.md`: one subject per section. Stage-labelled sections are labels (conventions §1.4).
- The harness reference's §6 variation points: a numbered list, so numbered. The walkthrough's §1 to §5: one subject each, apart from LAS-10.
- The playbook: the Plan Step Form's bold-led paragraphs are the form's rules, and Plan Step headings are labels.
- The worked example: byte-identical in both Agent Skills (`cmp`).
- The Record Stubs, the 3 delivered glossary files, the Agent Skill Templates, the config templates and the container's dotfiles, by headings: one subject per heading. None has a numbered section.

## Met in passing

- `temp/refinement-2026-10-18.md`, Round 3's *Endings*, "Moved to TODO: none" (lines 2354–2357): it says FINDING-227 and 228 "are worked in this round's layer 6". The tree shows neither was (LAS-7 to LAS-10). TODO's "Rewrite the method's texts plain" still names both.
- `cbc-framing/SKILL.md` gives its Agent Skill Stages no headings, only a code block (57–65) and the *Each Agent Skill Stage's Exit* list. Conventions §1.4 puts each Agent Skill Stage under its own heading (Agreement).
- `spring-harness-reference.md`: §1's and §3's *Bound facts* are bullets, and §2's are a numbered list.

## Not read

None. All files were read whole or by headings, as the assignment says.
