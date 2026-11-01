# LAO: Layout, our side

Reader LAO. Finding Kind: Layout. Read at `70404e1`, 2026-11-01.

Rule homes read whole: `docs/conventions/conventions/` §2.5, *The body*; `docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*; `.claude/rules/convention-manual.md`. Read beside them: the refinement's DECISION-8 (Layout reaches the descriptions and the files derived from a convention), DECISION-9 (no third level of numbering), DECISION-15 (the bold-lead line, and its 16 sections left to this read), DECISION-20 (the concept chapters stay unnumbered), and *Met in round 3, of other kinds*.

10 findings. 2 checked (LAO-1, LAO-10), 5 resting on the reader (LAO-2 to LAO-5, LAO-9), 3 uncertain (LAO-6 to LAO-8, each a question).

DECISION-15 left 16 sections in 10 documents to be "judged against the line at the last read". Four are judged parts and listed (LAO-2 to LAO-5). Two are questions (LAO-6, LAO-7). The other ten are judged not parts, under *Found true*.

## Findings

### LAO-1

- **Where:** `docs/models/tiers.md`, §3.5 *What holds on every flow*, line 149; and §3.4 *The Delivery Pin and documents*, line 123.
- **Quote:** `And one number, the Delivery Pin: the commit of the tier above that a`
- **The rule:** each numbered section holds one subject, and a subject has one section. Other sections point at it and do not tell it again (`docs/conventions/conventions/` §2.5, *The body*). DECISION-8 extends this to the Idea Models.
- **What the text says:** §3.4 is titled with the Delivery Pin and defines it at line 123: "The Delivery Pin, the commit of the tier above that a delivery's copies equal". §3.5 defines it again at line 149 in the same words, with no pointer to §3.4. §3.4 in turn points at §3.5. The five facts do the same. Fact 1 (line 136) retells §3.4's "no tier's agent reads a tier above it". Fact 5 (lines 146-147) retells §3.3's "the Run Repo sends nothing". So the reader meets each of them twice in one file.
- **Stands:** checked for the duplicate definition. Whether the five facts may be listed again is uncertain: `.claude/approaches-on-trial/model-placing.md`, *Not known yet*, leaves open "Whether an Idea Model may list its own facts again, each with its reference".
- **Why it was missed:** missed at a change. `b06dc95` (2026-10-28, model-placing) made §3.5 after Refinement Round 2's close read at `d37a08f`. `9fce63c` (2026-11-01) added the definition at line 123. No check at a commit reads an Idea Model's layout: `convention-manual.md` loads only for manuals. Round 3's reader met the facts (*Met in round 3, of other kinds*, the item on `docs/models/tiers.md` §3.5). The leftovers step did not carry that list, so it is listed here.
- **Proposed:** question. (a) §3.5 keeps the Delivery Pin's definition, and §3.4 line 123 points at it: "The Delivery Pin (§3.5, *What holds on every flow*) follows the documents the tiers exchange." (b) The closing paragraph of §3.5 moves into §3.4, and exchange §2.2 line 117 takes the new reference. For the five facts, decide with model-placing's open question.

### LAO-2

- **Where:** `docs/conventions/facts-in-sync/README.md`, §1 *One home*, lines 83-108.
- **Quote:** `- **History is not a second home.** The devlog, closed ADRs, commit`
- **The rule:** a section divided into labelled parts numbers them, `### N.M`. A bold-led bullet is a part when it holds a paragraph of its own, with its own reason or story. A short list item, a phrase and a line, is not (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
- **What the text says:** §1 has seven bold-led bullets. Four of them hold paragraphs of 4 to 6 lines, each with its own reason:
  - "A fact changes at its home";
  - "A copy is a follower", which names two cases;
  - "History is not a second home": "They are never updated, so they cannot drift";
  - "History is not a first home either", with its reason and ADR-0070.

  So they are parts, and they are not numbered.
- **Stands:** resting on the reader. DECISION-15 named this section and left it to this read.
- **Why it was missed:** older than the rule. The bold-lead line came in `aa40496`, 2026-10-28.
- **Proposed:** fix. Number the seven as `### 1.1` to `### 1.7`, each titled by its bold lead under writing rule 10. "Living Text" becomes *Living Text*. The bullets' text stays word for word. Every pointer to §1 still lands.

### LAO-3

- **Where:** `docs/conventions/writing/README.md`, §1 *What it governs*, lines 67-77.
- **Quote:** `- **Plain is the default for every kind of text.** A kind of text`
- **The rule:** as LAO-2 (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
- **What the text says:** three bold-led bullets, each a paragraph with its own reason. The third carries a story: "CBC Run 3 put off a specification style … (its `RETRO.md`, D14)". They are parts left unnumbered.
- **Stands:** resting on the reader. DECISION-15 named this section.
- **Why it was missed:** older than the rule (`aa40496`).
- **Proposed:** fix. `### 1.1 History keeps its words`, `### 1.2 Dense Agent Skills and Agent Rules`, `### 1.3 Plain as the default`, or titles the reviewer prefers. `.claude/rules/writing.md` cites §1 whole, so its references still land.

### LAO-4

- **Where:** `docs/conventions/shapes/README.md`, §2 *What an Output Shape is not*, lines 122-140.
- **Quote:** `- **Not trial evidence.** This is the one that will be got wrong,`
- **The rule:** as LAO-2. "So does every section of the same form in the document": §1, §4 and §5 of this manual already number their parts.
- **What the text says:** four bold-led bullets of 3 to 7 lines. Each gives its own reason why an Output Shape is not that thing. They are parts left unnumbered.
- **Stands:** resting on the reader. DECISION-15 named this section.
- **Why it was missed:** older than the rule (`aa40496`).
- **Proposed:** fix. `### 2.1 Not a template` to `### 2.4 Not trial evidence`, the text word for word. The pointers to §2 (*What it is for*, §1's *Its story*, *What this does not cover*) still land.

### LAO-5

- **Where:** `docs/models/agent.md`, §5 *The context window*, lines 170-193.
- **Quote:** `- **Ranked by role above that.** The harness marks three things`
- **The rule:** as LAO-2. DECISION-8 extends Layout to the Idea Models. §4 and §12 of this model already number their parts.
- **What the text says:** four bold-led bullets. "Undifferentiated within a role" holds a paragraph of its own, its "Consequence". "Ranked by role above that" holds 11 lines with its reason and claim W2. "Finite" and "Ordered, not prioritised" are one line each. Two of the four are parts, so the section is divided into labelled parts.
- **Stands:** resting on the reader. DECISION-15 named this section.
- **Why it was missed:** older than the rule (`aa40496`).
- **Proposed:** fix. `### 5.1` to `### 5.4`, each titled by its bold lead. The three pointers to §5 (§8's table and closing line, §12.5 W1) still land.

### LAO-6

- **Where:** `docs/conventions/retrospective/README.md`, §2 *How the look back decides* (lines 108-128) and §3 *How the lessons are applied* (lines 134-153).
- **Quote:** `- **The order of the commits follows influence.** Removing repeats`
- **The rule:** as LAO-2.
- **What the text says:** each section is a list of bold-led rules. Most items are a rule and one sentence of reason, 2 lines. A few run to 4 sentences, such as this one and "New proof is not this Plan Step's". No item carries a story. The items sit at the line's edge: longer than "a phrase and a line", shorter than LAO-2's paragraphs.
- **Stands:** uncertain. DECISION-15 named both sections.
- **Why it was missed:** the rule is unclear at its edge. "A paragraph of its own" and "a phrase and a line" leave the 2-to-4-sentence item undecided.
- **Proposed:** question. (a) Not parts: a rule list keeps bullets, and §3.2 says so ("a rule and its one reason is a list item"). (b) Parts: number both, as `79bc4a2` numbered commit-plan §2, whose §2.2 is two lines. Recommended: (a). The line then gains the words that decide the next case.

### LAO-7

- **Where:** `.claude/approaches-on-trial/refinement.md`, §3 *Not known yet*, lines 340-367.
- **Quote:** `- **Whether a refinement is the second check on text kept true.** The`
- **The rule:** as LAO-2. Its reach is DECISION-8: "the descriptions, and the files derived from a convention".
- **What the text says:** ten bold-led bullets. Two carry a dated story of their own, "On 2026-10-19 the reviewer…" and "The reviewer's view, 2026-10-31…". The page uses the manual's numbered form, and §1 and §2 number their parts.
- **Stands:** uncertain. An Approach on Trial is neither a description nor derived from a convention, and carries no Foundation Line (`docs/conventions/conventions/` §1.3, *The Foundation Line*). Yet DECISION-15 named "the refinement's §1 and §3" for this read. §1 now has its part, §1.1.
- **Why it was missed:** the rule is unclear: its reach over an Approach on Trial is not stated.
- **Proposed:** question. Does Layout reach an Approach on Trial written in the manual's form? If yes, number §3's ten items as `### 3.1` to `### 3.10`. If no, DECISION-15's naming of it is closed as out of reach. The refinement's close already asks whether an Approach on Trial follows the manual's form (*Met in round 3*, the item on `refinement.md` lines 182-299).

### LAO-8

- **Where:** `.claude/skills/commit-plan/SKILL.md`, §6 *Review protocol*, line 151; also §3 *How the commits are split* (lines 74-96) and §4 *The lifecycle* (lines 112-130). `.claude/skills/visual-comparison/SKILL.md`, §4 *What the render has caught* (lines 99-135).
- **Quote:** `**Small commits inside a planned commit, where the reviewer has`
- **The rule:** as LAO-2. DECISION-8 extends Layout to "the files derived from a convention", which these two Agent Skills are.
- **What the text says:**
  - **commit-plan §6:** a bold label on its own paragraph, the only labelled part of the section. DECISION-15 named it.
  - **commit-plan §3 and §4:** bold-led bullets of 7 to 10 lines, each with its own reason: "Order follows where the decision lives", "Plan the records commits", and the sweep.
  - **visual-comparison §4:** five bold-led bullets, each with the case it came from, which is a story.

  By the line's letter, all are parts left unnumbered in numbered sections.
- **Stands:** uncertain. DECISION-15 weighed only manuals and models, and the Agent Skill's §6 as a bold label. An Agent Skill writes its rules as bullets by its own form (`docs/conventions/conventions/` §1.1, *How a rule is written*).
- **Why it was missed:** the rule is unclear: whether §3.2's line reaches an Agent Skill's rule bullets is not stated. Both files are older than the line.
- **Proposed:** question. (a) The line reaches Agent Skills: number commit-plan §3, §4 and §6 and visual-comparison §4. Copy each change to the container's copy, as ADR-0069 allows. (b) Agent Skills are outside it: §3.2 says that a rule in an Agent Skill stays a bullet. Commit-plan §6's bold label then becomes plain prose, or a paragraph after the first. Recommended: (b). A rule bullet is acted on, not pointed at.

### LAO-9

- **Where:** `.claude/skills/visual-comparison/SKILL.md`, §1 *When this fires*, lines 26-47; and §2 *The comparison's steps*, steps 2 and 3, lines 56-64.
- **Quote:** `**The candidate set must contain at least one thing that is not a`
- **The rule:** each numbered section holds one subject, and a subject has one section (`docs/conventions/conventions/` §2.5, *The body*; DECISION-8 for derived files).
- **What the text says:** §1 holds three subjects:
  - when the Agent Skill fires, and when it does not (lines 28-30 and 43-47);
  - the rule that the candidate set holds a non-picture (lines 32-35);
  - which notations are buildable (lines 37-41).

  The second subject is told again in §2. Step 2 says "whenever the candidate set includes a non-picture, and the set usually should". Step 3 says "List the candidates, including the plain ones". So one subject is spread over two sections, and the step that acts on it is not its home. The manual gives each its own part: `docs/conventions/visual-comparison/` §2.1, *A non-picture in the set*, and §2.4, *The buildable notations*.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule. Lines 32-41 date from September 2026. Layout reached Agent Skills from DECISION-8, 2026-10-25. Refinement Round 2's read passed it.
- **Proposed:** fix. Move lines 32-35 into step 3, which then holds the non-picture rule once. Move lines 37-41 into step 4, as what "for real" can build. §1 keeps when it fires. The container's copy follows (one hunk differs today, the seat's).

### LAO-10

- **Where:** `.claude/skills/commit-messages/SKILL.md`, *Rules*, line 117; and *Format*, lines 19-20.
- **Quote:** `- **The subject alone makes sense** in `git log --oneline`.`
- **The rule:** a subject has one section; other sections point at it and do not tell it again (`docs/conventions/conventions/` §2.5, *The body*; DECISION-8 for derived files).
- **What the text says:** *Format* already says the subject "makes sense alone in `git log --oneline`" (line 20). *Rules* states the same rule again as its own bullet. One rule sits in two sections.
- **Stands:** checked. The container's copy is byte-identical, so the same lines stand in `delivery/container/.claude/skills/commit-messages/SKILL.md`.
- **Why it was missed:** older than the rule. *Format* gained the clause in `8fa62c6` (2026-10-09), beside the *Rules* bullet from `df9d5ed` (2026-09-17). Refinement Round 2's read passed it.
- **Proposed:** fix. Delete line 117. *Format* holds the rule. Make the same change in the container's copy in the same plan, so the two stay identical.

## Found true, so not listed

- **DECISION-15's other sections, judged not parts:**
  - project-recording §12: four items, each a phrase and a line;
  - project-recording §14: six items, each 1 to 3 lines of rule, with no story; the one 4-line item points at the file's header;
  - repo-hygiene §2: two definitions of one line each;
  - idea-to-output §5: two short items; §8: an address list;
  - agent model §10: two items, a lead and one sentence each; §11: an address list;
  - agent-arrangement §4: an anti-pattern list, items of 2 to 5 lines; every anti-pattern list in the manuals keeps bullets;
  - project-recording §1's group labels: labels over one numbered list, holding no paragraph;
  - the refinement's §1: now has its part, §1.1.
- **Parts already numbered:** commit-messages §2.1-2.4 and visual-comparison §2.1-2.4 (`b4b9737`). Every manual's numbered sections that already have parts number them all.
- **Sections added since `d37a08f`, each holding one subject:**
  - conventions §1.5;
  - exchange §3.8 and §5.8;
  - facts-in-sync §3.4;
  - project-recording §13.1 and §13.2;
  - idea-to-output §6.3: it compares, and its cells point at §5 and §6.2;
  - refinement §1.1.
- **Bold leads inside a part are not counted:** agent-arrangement §2.4, §5.6, §5.7; tiers §3.5's numbered facts; ARCHITECTURE §1.1. DECISION-9 rules out a third level.
- **The concept chapters:** their headings are unnumbered by DECISION-20, so §3.2's `### N.M` has nothing to number. Chapter 03's derivation steps and chapter 04's four phases stand as bold-led paragraphs. No chapter section holds two subjects.
- **The nine sections of `.claude/rules/convention-manual.md`:** every manual has them in order.
- **The other Agent Skills and Agent Rules:** exchange-read, exchange-deliver, the six rules, and the Approaches on Trial but the refinement's have unnumbered sections, or numbered rules and steps. Nothing is left unnumbered under §3.2. No section holds two subjects.
- **Exchange:** the Delivery Note is told in §3.7, and §2.5 and §6.6 point at it. agent-arrangement §3.9 is a part of §3 by FINDING-150's choice (`d2df7ff`).
- **ARCHITECTURE.md and README.md:** one subject a section. Overview's pairing is a summary that points at §1.
- **Read by headings:** `PLAN.md`, `TODO.md`, `CHANGELOG.md`, `devlog/README.md`, `temp/README.md`, `docs/adr/README.md`, `docs/glossary.md`, `TODO-CONVERSATION-MEMORY.md`, `.claude/decisions.md`, `CLAUDE.md`, `CLAUDE.local.md`, the three templates and the three dotfiles. None has a numbered section with parts left unnumbered. The Conversation Memory's numbering gaps are parts gone with their items, as its header says.

## Met in passing

- `docs/conventions/agent-arrangement/README.md` §3 is titled `.claude/`, yet its §3.7 (line 356) opens "Not under `.claude/`, but the arrangement's neighbour". Nor is `CLAUDE.local.md` in §1.1's closed list of paths. A Layout question for the reviewer if wanted: §3's subject is wider than its title.
- `.claude/rules/convention-manual.md` line 20 says each of the nine is "a `##` heading". So does conventions §2 lines 182-183: "each a heading after the opening". But item 6, "A lesson points at its story", and conventions §2.6, *A lesson taken*, are a rule for the body, not a heading (DECISION-9 counted it among the nine).
- `docs/conventions/conventions/README.md` §1.5 line 157-158: "A sentence that points at where a fact is written gives the path, as a Fact Reference" retells facts-in-sync §3.1 with no Fact Reference. Its "written with its kind" is the writing convention's subject.
- `PLAN.md`: the Plan Step being worked, Refine (line 301), sits below the two Plan Steps stopped for it (lines 135, 213). project-recording's seat, item 4, says "and below it any Plan Step stopped for it".
- The *Met in round 3, of other kinds* list (`temp/refinement-2026-10-18.md` lines 2203-2298) was not part of the leftovers step. Items still in place include `docs/models/tiers.md` §3.5 (taken here as LAO-1) and "Tests sample; structure forbids" in three chapters (one home). The other readers may not have been told this list.

## Not read

None. Every assigned file was read whole, or by headings where the assignment said so.
