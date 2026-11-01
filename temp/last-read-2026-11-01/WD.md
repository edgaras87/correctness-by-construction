# Reader WD: Writing, the 3 Idea Models and the 5 concept chapters

Read at `70404e1`, each file whole: `concept/00-cbc.md` to `concept/04-cbc-slice.md`, `docs/models/agent.md`, `docs/models/idea-to-output.md`, `docs/models/tiers.md`. Read against writing rules 1 to 10 (`.claude/rules/writing.md`, and `docs/conventions/writing/README.md` §2, *Why each rule*), after ADR-0079, DECISION-16 to 40 and both lists of the agent's calls.

6 findings: 2 checked, 3 resting on the reader, 1 uncertain. Each fix to a concept chapter is marked editorial or not.

## Findings

### WD-1

- **Where:** `concept/03-cbc-framing.md`, *The derivation order*, line 54.
- **Quote:** "is more than one Responsibility Area, examine the seams between them"
- **The rule:** writing rule 9 (`.claude/rules/writing.md`, rule 9): a lowercase word is English and only English, and a defined thing is written by its Glossary Name. A word with a rival among the delivered Names is fixed (DECISION-19, (a)'s line kept under (b); FINDING-1086 "bootstrap" and FINDING-1115 "fold" were fixed on this ground).
- **What the text says:** "the seams between" two Responsibility Areas. The method's glossary defines exactly this thing as the Responsibility Area Seam, "the line between two Responsibility Areas" (`delivery/method/docs/glossary/method.md`, line 145). The same file a CBC Run receives with the concept lists it, so a reader meets the lowercase word beside its Name and must decide which is meant.
- **Stands:** checked. The Name is in the method's glossary, and the word is at line 54.
- **Why it was missed:** missed at a change. `1f0c17e` rewrote the line on 2026-11-01, after ADR-0078 had delivered the method's Names, and kept "the seams". The close read's rule 9 check for a word with a rival should have caught it.
- **Proposed:** fix, editorial (the same thing, said in plain words): "is more than one Responsibility Area, examine where each two of them meet". Plain words, not the Name, since the Name's home is the method's workflow, below the concept.

### WD-2

- **Where:** `concept/01-layered-system.md`, *LAYER-3-AREAS — Responsibility Areas*, lines 59-60.
- **Quote:** "owner.** Often the honest answer is a single Responsibility Area — that"
- **The rule:** writing rule 2 (`.claude/rules/writing.md`, rule 2): short sentences, one idea each. Writing rule 5: plain words, not metaphor; DECISION-26 fixes "honest, honestly".
- **What the text says:** a dash joins two clauses, "the answer is a single Responsibility Area" and "that is a confirmed answer, not a gap". The close read fixed this exact form in the same chapter, a dash joining two clauses (FINDING-1136), and "honestly" two sections down (FINDING-1135, "can rightly become"). This line was in neither list.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `1f0c17e` rewrote the line. The close read's FINDING-1136 listed the chapter's other dashes (then lines 45, 49-50, 92) and not this one (then line 57).
- **Proposed:** fix, editorial: "owner.** Often the right answer is a single Responsibility Area. That is a confirmed answer, not a gap."

### WD-3

- **Where:** `concept/03-cbc-framing.md`, *The derivation order*, line 59; `concept/04-cbc-slice.md`, *The four phases*, line 35.
- **Quote:** "Invariant Slice Registry's ordering is an expectation, not a commitment; evidence from"
- **The rule:** writing rule 2 (`.claude/rules/writing.md`, rule 2): short sentences, one idea each. The close read fixed a semicolon that joins two ideas with a full stop (FINDING-1149, three lines in these two chapters).
- **What the text says:** a semicolon joins two ideas: the order is an expectation; evidence may reorder what is left. The same at chapter 04 line 35, "ranking of Structural Walls, the strongest available; choosing a weaker Structural": the Structural Wall is the strongest available; a weaker one needs a stated reason. 2 lines.
- **Stands:** resting on the reader. The chapters' other semicolons join a parallel pair ("Tests sample; structure forbids.") and are not listed.
- **Why it was missed:** missed at a change. `1f0c17e` wrote 03 line 59, and `eefdced` rewrote 04 line 35, after FINDING-1149's fix set the form. The close read listed 03's opening and 04's opening, not these.
- **Proposed:** fix, editorial: 03, "Invariant Slice Registry's ordering is an expectation, not a commitment. Evidence from built Invariant Slices is allowed to reorder what remains."; 04, "ranking of Structural Walls, the strongest available. Choosing a weaker Structural Wall than possible is a decision that needs a stated reason."

### WD-4

- **Where:** `docs/models/idea-to-output.md`, §2, *The kinds*, line 38; the Name used at lines 24, 93 and 155.
- **Quote:** "| Work Approach | how a piece of work is done | an Agent Skill, an Agent Rule, an Approach on Trial, a record's form in its header comment |"
- **The rule:** writing rule 9 (`.claude/rules/writing.md`, rule 9): a Name goes into the glossary "pointing at the home that defines it". Writing rule 8: before a Glossary Name, say in plain words what it is if the reader does not hold it.
- **What the text says:** `docs/glossary.md`'s Output Form entry points at this section, "(`docs/models/idea-to-output.md` §2, *The kinds*)". §2's table never names an Output Form or says what one is; it writes "a record's form" in lowercase. The model then uses the Name three times, in the drawing (24), §4.1 (93) and §6.1 (155), and nowhere says what it is. A grep finds no defining line in any file under `docs/models/`.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `11389e9` (round 3's work, FINDING-513) brought "Output Forms" into lines 24, 93 and 155, and left §2 as it was. FINDING-513 judged "a record's form" fine as the glossary's own wording, but did not check that §2 is the Name's home. The close read did not catch it.
- **Proposed:** fix: line 38's last cell, "an Agent Skill, an Agent Rule, an Approach on Trial, an Output Form"; and line 42 opens with one sentence, "An Output Form is how one output is written, read while it is written, such as a record's header comment." It states what the glossary entry already says. As a change to an Idea Model, it runs the Change Walk.

### WD-5

- **Where:** `docs/models/tiers.md`, §3.3, *Upward harvest*, line 114; the drawing, line 29.
- **Quote:** "Up is harvest, and only through records: the tier above reads a"
- **The rule:** writing rule 9 (`.claude/rules/writing.md`, rule 9): write a defined thing by its Glossary Name; a lowercase word is English only. Rule 9 reaches drawn text (DECISION-21).
- **What the text says:** the glossary's Record Harvest entry points here, "(`docs/models/tiers.md` §3.3, *Upward harvest*)". The section defines the thing as "harvest", lowercase, and never writes the Name. The drawing writes "▲ harvest:" too (line 29). Elsewhere a lowercase "harvest" that means this thing was fixed to the Name: FINDING-580, `TODO.md`'s "the harvest discipline"; FINDING-690, the playbook's "Harvest lands here". DECISION-26 keeps "harvest" as a figure, which settles rule 5 only. Line 75's "it is harvested" is a verb, and stays English.
- **Stands:** resting on the reader. That the Name does not appear in §3.3 is checked.
- **Why it was missed:** missed at a change. `2ccc26a` rewrote line 114 for FINDING-526, which read it for rule 7 only. The close read did not read it for the Name.
- **Proposed:** fix: "Up is the Record Harvest, and only through records: the tier above reads a"; line 29, "▲ Record Harvest: a Run Repo's surprises". Question for the title *Upward harvest*: it stays, read as an English direction word, or it is retitled with the Name and the rename grep. Its references include the glossary entry and §3.5 line 147.

### WD-6

- **Where:** `concept/00-cbc.md`, *The two components*, line 65; `concept/03-cbc-framing.md`, *The derivation order*, lines 26 and 57.
- **Quote:** "**The world model — the Layered System.** A containment description of"
- **The rule:** writing rule 9 as ADR-0079 changed it (`.claude/rules/writing.md`, rule 9): "No Markdown mark marks a Name, but bold once, at the line that defines it. A list item's bold lead may begin with a Name."
- **What the text says:** three paragraph leads, not list items, hold a Name in bold away from its home. At 00 line 65 it is the Layered System, whose home is chapter 01. At 03 line 26, "**Choose the Falsifiable Promise.**", the home is chapter 01. At 03 line 57, "**Cut into Invariant Slices.**", the home is chapter 04. ADR-0079's reason, that the bold marks the item, fits a paragraph lead as well. Its words name only a list item. The script sent the worked example's paragraph leads to their reader on the same question.
- **Stands:** uncertain: whether ADR-0079 decision 2 reaches a paragraph's bold lead.
- **Why it was missed:** the rule is unclear. ADR-0079, 2026-11-01, wrote the exception for list items only.
- **Proposed:** question: (a) decision 2 reaches a paragraph's bold lead, and the rule's line says "a bold lead"; the three stand. (b) It does not; the six paragraphs of 03's *The derivation order* and 00's two components become list items, which decision 2 covers. That fix is editorial, and no wording changes. A third way, the bold dropped from the leads, would cost every other step's lead.

## Found true, so not listed

- The script's one hit, `concept/00-cbc.md` line 92, "**CBC Framing**" away from chapter 03: a list item's bold lead that begins with a Name (ADR-0079, decision 2).
- Each Name bolded in these files is bolded at its home: System Guarantee and the four failure modes in 00; Falsifiable Promise in 01; Structural Wall in 02; Enemy Collision Kill and the three CBC Framing Exports in 03; Concept Repo, Concept Garden and Run Repo in the Tiers Model.
- A sweep of all 173 Names in the four glossaries, matched across line breaks, found no Name spelled in another case. The only hits were the verb "made usable" (allowed, FINDING-525's call) and the drawing labels in chapter 01.
- Every numbered title in the 3 Idea Models is 30 characters or fewer, with no gloss. The chapters' headings are unnumbered (DECISION-20).
- `docs/models/tiers.md` line 154, "the tiers model": a devlog entry's title, quoted exactly (rule 6).
- Line 9 of `docs/models/tiers.md`, "earns machinery": FINDING-527 counted it near dead and left it.
- The handbook is said in plain words at first use in each model, as DECISION-23 asks: agent 283, idea-to-output 112, tiers 44.
- "promise" in `concept/00-cbc.md` lines 9-11, *In one sentence*, is the object of "what it promises", which is English. Its one-sentence form is what the heading names.
- The leftovers D1 to D6 and D8, and FINDING-1127's gap line, are still in place as listed. They are not listed again.

## Met in passing

- `docs/models/agent.md` lines 397-400, W2: the claim's *Refuted by:* runs on at the end of its second incident's sub-item. A2, P1, P2 and O1 give it its own line (Layout).
- `docs/models/tiers.md` lines 93-95, §3.1 item 2: the continuation "Steps are written into a CBC Run's plan" starts at column 0. It renders by lazy continuation, as E14 notes for `ARCHITECTURE.md` (Layout).

## Not read

None.
