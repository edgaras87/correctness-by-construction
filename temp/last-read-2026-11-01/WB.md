# Reader WB: Writing, layer 3 (the index and five manuals)

Read whole at `70404e1`: `docs/conventions/README.md`,
`docs/conventions/agent-arrangement/README.md`,
`docs/conventions/commit-messages/README.md`,
`docs/conventions/commit-plan/README.md`,
`docs/conventions/exchange/README.md`,
`docs/conventions/facts-in-sync/README.md`.
Read first: the Writing row of *The rules' check* (last read), `.claude/rules/writing.md`, `docs/conventions/writing/README.md` whole, `refinement.md` §2.4 and §2.5, ADR-0079, DECISION-16 to DECISION-40 and both lists of the agent's calls, the leftovers.

10 findings. 4 checked, 5 resting on the reader, 1 uncertain.

## Findings

**WB-1.** Rule 9, "birth" as a noun for the event.
- **Where:** `docs/conventions/exchange/README.md`, *What this is made usable as*, line 48. Also *What this does not cover*, line 594.
- **Quote:** "preceded it or not. Birth is a delivery into the root plus the"
- **The rule:** writing rule 9: a defined thing is written by its Glossary Name (`.claude/rules/writing.md`, rule 9). DECISION-36 settled it for this word: "Birth" as a noun for the event is the Name CBC Run Birth; "born", "at birth" and "from birth" stay English.
- **What the text says:** line 48 uses "Birth" as a noun for the event, capitalized only because it opens a sentence. Line 594, "**The birth procedure**", uses it the same way.
- **Stands:** checked, for lines 48 and 594. Uncertain for "birth entry": agent-arrangement lines 92-93, 159, 173 and 330 (and conventions manual 309, 320, reader A's file) use the noun as a modifier, "the birth entry". DECISION-36 does not say whether a compound counts.
- **Why it was missed:** older than the rule (`e22d7f6`, 2026-09-29). Then missed at a change: `b379c2d` worked DECISION-36's "other uses" in the glossary's Pure Seed entry, repo-hygiene and shapes §4.3, and did not grep the exchange manual.
- **Proposed:** fix: line 48, "A CBC Run Birth is a delivery into the root plus the Delivery Fills"; line 594, "**How a CBC Run is born**". Question: is "birth entry" the noun DECISION-36 names? If yes, "the entry written at CBC Run Birth" or "the Decisions Log's first entry"; if no, it stands as English.

**WB-2.** Rule 9, Local Rule written in lowercase at its home.
- **Where:** `docs/conventions/agent-arrangement/README.md` §2.4, *How the Entry File is written*, line 229. Also §3.1 line 298 and §4 line 412.
- **Quote:** "5. local rules that have no moment."
- **The rule:** writing rule 9: a defined thing is written by its Glossary Name; a lowercase word is English only (`.claude/rules/writing.md`, rule 9). `docs/glossary.md` lists Local Rule, "a rule written in the Entry File's *Local rules* slot, true of this project only", and points at §2.4.
- **What the text says:**
  - line 229, at the Name's home, writes the thing as "local rules";
  - line 412, "**A local rule with a moment**", is a rule in that slot, so the Name;
  - line 298, "a moment-bound local rule the Entry File must not hold", means a rule that is not in the slot. Written lowercase, it reads as the Name it is not. DECISION-23 settles a clash with a Name by plain words.
- **Stands:** checked: the entry exists and points at §2.4; §2.4 never writes the Name.
- **Why it was missed:** missed at a change: `b379c2d` gave Local Rule its glossary entry, pointing at §2.4. The home's three lines were not given the Name. Rule 9 says the Name goes in with the home that defines it.
- **Proposed:** fix: line 229, "5. Local Rules, rules of this project only that have no moment."; line 412, "**A Local Rule with a moment**"; line 298, "for a rule of this project only that has a moment, which the Entry File must not hold".

**WB-3.** Rule 5, "travels", which DECISION-26 fixes.
- **Where:** `docs/conventions/exchange/README.md` §3.4, *One group per file*, line 231. Also §3.5, *The Foundation Line in a copy*, line 254.
- **Quote:** "Agent Skill belongs to one group and travels whole, never split"
- **The rule:** writing rule 5: plain words, not metaphor (`.claude/rules/writing.md`, rule 5). DECISION-26's journey row lists "travels" as a figure to fix.
- **What the text says:** line 231 says an Agent Skill "travels whole". Line 254 says "the line travels with the copy as a live claim". These are the last two living uses in the repo. The same words were fixed in shapes ("is delivered whole", `efb8cef`) and `ARCHITECTURE.md` ("which every copy carries", `5d0f5ca`).
- **Stands:** checked.
- **Why it was missed:** missed at a change: `a60a357`, "the exchange meets the writing rule", 2026-11-01, rewrote both lines after DECISION-26 (2026-10-30) and kept the word. The round 3 close read passed them too.
- **Proposed:** fix: line 231, "An Agent Skill belongs to one group and is delivered whole, never split across two."; line 254, "every copy carries the line as a live claim."

**WB-4.** Rule 5, "tail" for a plan's last commits.
- **Where:** `docs/conventions/commit-plan/README.md` §1, *What a commit plan is*, line 62. Also §2.4, *Material-first*, line 89.
- **Quote:** "held. The second kind makes the tail of a plan provisional, and the"
- **The rule:** writing rule 5: plain words, not metaphor (`.claude/rules/writing.md`, rule 5).
- **What the text says:** the manual says "the tail of a plan" (line 62) and "the provisional tail" (line 89). Both commit-plan Agent Skills dropped the same figure for "provisional commits" (ours `31156de`; the container's on FINDING-1310, as the figures of DECISION-26's journey row). The manual is their foundation and still says "tail".
- **Stands:** resting on the reader. "Tail" may be read as dead English, as "the tail of a list".
- **Why it was missed:** missed at a change: `31156de` changed the derived Agent Skill. The check of a forced change against the manual should have found the manual's word (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 4).
- **Proposed:** fix: line 62, "The second kind makes the plan's last commits provisional, and the plan says so."; line 89, "the provisional commits, the revision commit and the Proposed-then-Accepted ADR are the normal course".

**WB-5.** Rule 2, one sentence of four ideas.
- **Where:** `docs/conventions/facts-in-sync/README.md`, *What it is for*, lines 27-30.
- **Quote:** "Refinement Round 2 found two Finding Kinds, One home and"
- **The rule:** writing rule 2: short sentences, one idea each (`.claude/rules/writing.md`, rule 2).
- **What the text says:** "Refinement Round 2 found two Finding Kinds, One home and Dependencies, the checks of a fact's home and of what a text stands on, resting on rules split that way, and the rules came here before it read (ADR-0065)." That is two appositives, a participle clause and a second main clause in one sentence. "It" in "before it read" has to be traced back to Refinement Round 2.
- **Stands:** checked.
- **Why it was missed:** missed at a change: `0cdd102`, the close read's fix, wrote this sentence. Nothing read it after.
- **Proposed:** fix: "Two of Refinement Round 2's Finding Kinds rested on rules split that way. One home checks a fact's home. Dependencies checks what a text stands on. The rules came here before that round read (ADR-0065)."

**WB-6.** Rule 2, a gloss pushed into a chained sentence.
- **Where:** `docs/conventions/commit-messages/README.md`, *What it is for*, lines 17-20.
- **Quote:** "sentence, the rule that the agent waits at each commit, alone with"
- **The rule:** writing rule 2: short sentences, one idea each (`.claude/rules/writing.md`, rule 2).
- **What the text says:** "Lived here since: 480 commits under it by 2026-09-19, and CBC Run 3 held forty-four commits on the stop sentence, the rule that the agent waits at each commit, alone with no Enforcement Gate." The inserted gloss splits "the stop sentence" from "alone". "Alone with no Enforcement Gate" now reads as if it belongs to "each commit".
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change: `103a301`, the close read's fix, added the gloss inside the sentence.
- **Proposed:** fix: "Lived here since: 480 commits under it by 2026-09-19. CBC Run 3 held forty-four commits on the stop sentence alone, with no Enforcement Gate. The stop sentence is the rule that the agent waits at each commit."

**WB-7.** Rules 3 and 1, a Delivery Note's parts as fragments in one paragraph.
- **Where:** `docs/conventions/exchange/README.md` §3.7, *The Delivery Note*, lines 271-280.
- **Quote:** "Why it matters to this CBC Run — the part a diff cannot carry. A verdict"
- **The rule:** writing rule 3: when an argument has parts, give each its own line or label; don't chain them with dashes. Writing rule 1: the first line says the point (`.claude/rules/writing.md`, rules 1 and 3).
- **What the text says:** the section opens with three fragments in running prose, joined by a dash: what changed, why it matters, and a verdict. Then a fourth, "Nothing that needs our repo to verify:". The reader must work out that these are a Delivery Note's parts, and how many there are. No line says so first.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule (`523798e`, 2026-09-25). The pass (`1576044`) and round 3's two reads changed only its words.
- **Proposed:** fix: open with "A Delivery Note says three things:", then a list:
  - "what changed since the CBC Run's Delivery Pin, so the CBC Run can diff the Delivery Staging against what it holds and find the Delivery Note wrong;"
  - "why it matters to this CBC Run, the part a diff cannot carry;"
  - "a verdict on everything the CBC Run addressed to us since we last read it, in the CBC Run's order."

  The sentences on verdicts and "Nothing that needs our repo to verify" follow as they stand.

**WB-8.** Rule 3, two defined numbers chained after a dash.
- **Where:** `docs/conventions/exchange/README.md` §2.2, *The CBC Run*, lines 99-105. Also §4, *The Delivery Take*, lines 334-337.
- **Quote:** "Log carrying two numbers — **the Delivery Pin**, the Concept Deliverer's commit its"
- **The rule:** writing rule 3: give each part its own line or label; don't chain them with dashes and semicolons (`.claude/rules/writing.md`, rule 3).
- **What the text says:** one sentence opens with a fragment, then a dash, then two numbers, each with its definition, joined by commas. The next sentence adds a second dash. These lines are the home of both Names. Lines 334-337 use the same form: "Nothing in `temp/` is in force until it is copied into place — a staged Agent Skill is a file, not an Agent Skill, and a Plan Step that opens meanwhile runs on the held copy". That is two consequences chained after a dash.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule (`f95dd0d`, 2026-09-25). The pass (`1576044`) changed only its Names.
- **Proposed:** fix: "The copies. And one line in its own Decisions Log per Delivery Note, which carries two numbers:", then a list, "**the Delivery Pin**, the Concept Deliverer's commit its copies equal;" and "**the Read-Through Commit**, its own commit the Concept Deliverer last read up to." Then "Its edits since the Delivery Pin need no record of their own. They are the diff against what was delivered, and git holds it." At 334-337: "Nothing in `temp/` is in force until it is copied into place. A staged Agent Skill is a file, not an Agent Skill. A Plan Step that opens meanwhile runs on the held copy."

**WB-9.** Rule 9, a paragraph lead that holds a Name.
- **Where:**
  - `docs/conventions/exchange/README.md` §2.2, *The CBC Run*, line 116;
  - the same file, *The seats*, lines 68 and 69;
  - `docs/conventions/commit-messages/README.md` §3, *The Concept Deliverer's habit*, line 96;
  - `docs/conventions/README.md`, *The order of the conventions*, line 39.
- **Quote:** "**One Delivery Pin** for everything delivered, as on every flow"
- **The rule:** writing rule 9 as ADR-0079 left it: "No Markdown mark marks a Name, but bold once, at the line that defines it. A list item's bold lead may begin with a Name" (`.claude/rules/writing.md`, rule 9). ADR-0079 decision 1 says a Name is "bold nowhere else". Its script checks that each bold Name is bold once in Living Text.
- **What the text says:**
  - line 116 bolds Delivery Pin a second time in its own home, after line 100;
  - lines 68 and 69, "**The CBC Run's**" and "**The Concept Deliverer's**", bold two Names away from their home, the Tiers Model;
  - line 96, "**The Concept Deliverer did not take it**", and line 39, "**Work no Agent Skill or Agent Rule covers**", bold a phrase that holds a Name.

  None of these is a list item. Each is a paragraph's bold lead or a bold phrase in running prose. The rule's letter allows neither. The script missed them because each bold span holds more than the Name.
- **Stands:** uncertain. ADR-0079's reason for a list item's lead, "the bold marks the item, not the Name", may reach a paragraph's lead too. The rule does not say.
- **Why it was missed:** the rule is unclear. ADR-0079 answered FINDING-1384 for list items only.
- **Proposed:** question: does a paragraph's bold lead, or a bold phrase in prose, that holds a Name count as marking the Name? Recommended: yes for line 116, where its home file then shows two bolds for one Name: drop the bold there. For the other four, the reviewer decides. Either the rule names a paragraph's lead beside a list item's, or the bold goes.

**WB-10.** Rule 9, "stages" beside Agent Skill Stage, and "this" with no subject.
- **Where:** `docs/conventions/README.md`, *The order of the conventions*, lines 50-52.
- **Quote:** "the records they govern, are not stages of this and fire on their"
- **The rule:** writing rule 9: a lowercase word is English only, and a word with a rival among the Names is fixed (DECISION-19, "stage" beside Skill Stage, FINDING-792). Writing rule 8: start from what the reader holds (`.claude/rules/writing.md`, rules 8 and 9).
- **What the text says:** "The other conventions, and the records they govern, are not stages of this and fire on their own moments." "Stages" means steps of the order, where Agent Skill Stage and Approach on Trial Stage are Names. "This" stands for the order, which the sentence does not name.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule (`722357d`, 2026-09-30). `103a301` renamed "the chain" to "this order" on line 48 and left this line.
- **Proposed:** fix: "The other conventions, and the records they govern, are not steps in this order. Each fires at its own moment."

## Found true, so not listed

- **Titles:** every numbered title in the six files is 30 characters or fewer. None has a dash, colon, comma gloss or parenthesis. Glossary Names inside them keep their capitals.
- **Bold at a Name's home:** each is bold once, at its defining line, in the file its entry points at: Fact Reference, Living Text and the Change Walk in facts-in-sync; the Read-Through Commit, Delivery Fill, Receipt Branch and CBC Run Ask in the exchange manual. Delivery Pin is bold at its home too, but also at line 116 (WB-9).
- **Script hits:** both are judged in WB-2. Line 298 has a clash; line 412 is the Name.
- **Kind words:** Agent Skills and manuals carry their kind word in prose, as DECISION-27 and conventions §1.5 ask. In agent-arrangement lines 60 and 80-84, the kind word comes first and the names follow in backticks. That meets "written with its kind".
- **Owners:** local numbers carry their owner: claims A1, A2, M1 and P1 with their Fact References; CBC Run 3's D1 and its Step 10; ADR-0038's 1a to 1f.
- **Foundation Lines and `foundation`:** written as conventions §1.3 gives them (ADR-0079).
- **"Rules files":** agent-arrangement §5.6 uses Claude Code's own term, which the Tool Binding records.
- **Fixed headings:** the "seat" subheadings, *The CBC Run's seat* and *The Concept Deliverer's seat*, are the manual form's.
- **"The sweep" and "Small commits":** judged right as labels at round 3's rule check, Doubt 2.
- **Leftovers:** commit-plan 139 (B6), exchange 487 (B7), agent-arrangement 220 and 251, 330 (B3) and 386 (B4) are still in place, as listed. None was listed again.

## Met in passing

- **Stale lines:** facts-in-sync §3.1, lines 149-150 and 179-181, says a shipped file's reference to our text "leads with CBC". DECISION-40 changed shipped text to "the Concept Deliverer's docs/conventions/…", as `delivery/container/.claude/rules/delivered-copies.md` line 163 now has it.
- **Wiring:** index lines 7-8, "`ARCHITECTURE.md`'s (§1.2, *The conventions*)", puts the path outside the parentheses, in the form for the same document. Facts-in-sync line 120-121, "`docs/conventions/agent-arrangement/`'s, its *What it is for*", is a reference not in the parenthesized form.
- **Agreement:** the glossary's Paths Rule entry points at agent-arrangement §5.6, which never writes the Name.
- **Stale lines:** commit-messages lines 27-28 and commit-plan line 27 say the shipped Agent Skill carries "the decisions it rests on in its footer". Since ADR-0078 the delivered copy has its footer stripped; only the Master Copy keeps it.
