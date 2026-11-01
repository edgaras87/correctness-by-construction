# LEO: Lessons, our side

Reader LEO. Finding Kind: Lessons, a case written as the rule. Read at `70404e1`.

Rule read first: `docs/conventions/conventions/` §2.6, *A lesson taken*; `.claude/rules/convention-manual.md` item 6; ADR-0073. Also read: refinement.md §2.4 and §2.5; DECISION-7, DECISION-18 and every other decision; both lists of the agent's calls; ADR-0079; the leftovers. Round 2's Lessons findings (FINDING-139 to 267, in git at `1a9f76d`) were checked for anything already ended.

Reach. DECISION-7 puts §2.6 on the manuals and on the files derived from a convention in both seats. So it reaches the 12 manuals, our Agent Rules, our Agent Skills, and the record forms that carry a Foundation Line. It does not reach the concept, the Idea Models, or the Approaches on Trial. A manual's *What it is for* holds its need's evidence by design (§2.2; ADR-0073, *Consequences*).

8 findings: 3 checked, 4 resting on the reader, 1 uncertain.

## Refinement Layer 3: the other manuals

**LEO-1.** commit-plan §2.9's italic tells the case.
- **Where:** `docs/conventions/commit-plan/README.md`, §2.9 *The agent's files*, lines 128–129.
- **Quote:** split when it opens. *CBC Run 3's Step 10 plan put two changes under
- **The rule:** a manual states the lesson in general. The case goes to the history that tells it, and the manual keeps one italic line pointing there, "*Its story: ADR-0059.*". A case told nowhere else is first written into a devlog entry (`docs/conventions/conventions/` §2.6, *A lesson taken*; `.claude/rules/convention-manual.md` item 6).
- **What the text says:** the section ends with an italic sentence that tells CBC Run 3's case, not a line that points at its story. §2.8 next to it shows the form: "*Its story: devlog 2026-10-08; …*".
- **Stands:** checked. The leftovers file marks §2.9 "gone" under B5. It is still in the tree.
- **Why it was missed:** missed at a change. The case dates from `489ecf2` (2026-10-08). Round 2 accepted it as an italic, which was the rule's form then. When ADR-0073 turned notes into pointers, `ae53ed7` ("the other lessons point at stories") moved only the *dated* notes. This italic has no date, so it stayed. That commit plan counted dated notes, not cases. Round 3's *Met in round 3* listed it, and so did the close read (reader B).
- **Proposed:** fix: lines 128–129 become "split when it opens." and then, on its own line, "*Its story: devlog 2026-10-08.*". That entry tells the take ("agent files their own step") but maybe not the case. If it does not, the italic's words are first copied into a devlog entry, as ADR-0073 decision 2 did for the others, and the line names that entry too.

**LEO-2.** commit-plan §2.12's italic tells the case.
- **Where:** `docs/conventions/commit-plan/README.md`, §2.12 *The look back*, lines 160–161.
- **Quote:** *CBC Run 3's polish regrouped 36 small commits into 7, after the fact
- **The rule:** as LEO-1 (`docs/conventions/conventions/` §2.6, *A lesson taken*).
- **What the text says:** the section's last line is the case itself, CBC Run 3's count, not a line that points at its story. ADR-0050 tells the case: "regrouped by kind, 36 into 7" (its line 18).
- **Stands:** checked. The leftovers file marks §2.12 "gone" under B5. It is still in the tree.
- **Why it was missed:** missed at a change, as LEO-1: the case dates from `1e50055` (2026-10-15), and `ae53ed7` moved only dated notes. Round 3's met list and the close read's met list both named it.
- **Proposed:** fix: "*Its story: ADR-0050.*" replaces lines 160–161.

**LEO-3.** shapes §4.1's italic paragraph tells the case.
- **Where:** `docs/conventions/shapes/README.md`, §4.1 *Nothing fetched*, lines 192–196.
- **Quote:** staged for a Plan Step Gate on its own. *A fetch of Output Shapes at
- **The rule:** as LEO-1 (`docs/conventions/conventions/` §2.6, *A lesson taken*; `.claude/rules/convention-manual.md` item 6).
- **What the text says:** a five-line italic tells the case: ADR-0037 named a fetch that was never built, and CBC Run 3 looked in `temp/` at two closes. The lesson, "Nothing is staged for a Plan Step Gate on its own", already stands in the body. ADR-0052 tells the case (its line 28: "looked in at two closes").
- **Stands:** checked.
- **Why it was missed:** missed at a change. The case is from `ec64d6a` and `61fcc5d` (2026-09-27 and 2026-10-15). `ae53ed7` moved shapes' dated notes and left this undated one. Round 3's *Met in round 3* listed it. It is not in *Met at the close read* or in the leftovers, so nothing carried it on.
- **Proposed:** fix: lines 192–196 become "staged for a Plan Step Gate on its own." and then, on its own line, "*Its story: ADR-0052.*".

**LEO-4.** retrospective's seat argues from CBC Run 3's apply guide.
- **Where:** `docs/conventions/retrospective/README.md`, *The CBC Run's seat*, lines 78–81.
- **Quote:** would drift. CBC Run 3's apply guide restated nearly every rule of its
- **The rule:** the body states the lesson in general. The case goes to its history, with one italic line pointing there (`docs/conventions/conventions/` §2.6, *A lesson taken*).
- **What the text says:** the general reason is stated: "it would repeat them, and the two would drift". Then the case that taught it stays in the body as a sentence of its own. ADR-0054 tells it: "in run 3 the apply guide restates nearly every rule" (its lines 45–47). The lesson reads clearly without it, so §2.6's allowance for an example does not apply.
- **Stands:** resting on the reader: one could read the sentence as a short example.
- **Why it was missed:** older than the rule. The text is from `fa7fd41` (2026-10-15), and §2.6 came on 2026-10-18. Then missed at round 2's Lessons read and at `ae53ed7`. Round 3's FINDING-450 read it for rule 4 only.
- **Proposed:** fix: cut "CBC Run 3's apply guide restated nearly every rule of its Agent Skill." Then end the paragraph with "*Its story: ADR-0054.*".

**LEO-5.** visual-comparison §1 ends on ADR-0028's case.
- **Where:** `docs/conventions/visual-comparison/README.md`, §1 *What a comparison is*, line 58.
- **Quote:** set. ADR-0028's best answer to one requirement was one of those.
- **The rule:** as LEO-4 (`docs/conventions/conventions/` §2.6, *A lesson taken*).
- **What the text says:** the lesson is stated in general: a name that named a picture would keep the table and the list out of the set. Then the case follows as evidence, in the body. *What it is for* already tells the same case (lines 20–22), and *Where to look* names ADR-0028.
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule: `1e5d42e` (2026-09-19). Round 2's FINDING-265 moved this case out of the Agent Skill and "the manual holds them". That read as cover for the body sentence. Then reworded in `7a54776` (round 3) for writing alone.
- **Proposed:** fix: cut the sentence. §1 gains "*Its story: ADR-0028.*".

**LEO-6.** writing §1 gives CBC Run 3's case as the reason no style is named.
- **Where:** `docs/conventions/writing/README.md`, §1 *What it governs*, lines 75–77.
- **Quote:**   named yet: CBC Run 3 put off a specification style until its claims
- **The rule:** as LEO-4. A case told nowhere else is first written into a devlog entry (`docs/conventions/conventions/` §2.6, *A lesson taken*).
- **What the text says:** the lesson is general: "A kind of text gets another style only when plain has been shown to fall short there." The text then gives CBC Run 3's RETRO D14 as the case, in the body. No ADR or devlog entry here tells it. ADR-0053 does not mention it, and the devlog has no "specification style".
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule: `83acdfe` (2026-10-15). It was reworded in `efb8cef` (round 3's close read) for writing alone. Lessons was not read then.
- **Proposed:** fix: "None is named yet." stays. The CBC Run 3 clause is copied into a devlog entry, and the bullet ends with "*Its story: devlog <that entry>.*".

**LEO-7.** writing's *Why it arrives this way* tells CBC Run 3's cases.
- **Where:** `docs/conventions/writing/README.md`, *Why it arrives this way*, lines 186–187, and lines 190–191.
- **Quote:**   draft loaded on Markdown files, and was dropped for this.
- **The rule:** as LEO-4 (`docs/conventions/conventions/` §2.6, *A lesson taken*).
- **What the text says:** each rejected channel has its general reason. "A Paths Rule loads when a file is touched, after a new one's first draft is written. Chat has no path." Then comes the case: "CBC Run 3's first draft loaded on Markdown files, and was dropped for this." Lines 190–191 do the same: "held the lesson in CBC Run 3 and did not act." ADR-0053's *Options considered* tells both: "Load them on Markdown paths only" and "Keep the voice in memory or in `CLAUDE.local.md`".
- **Stands:** resting on the reader.
- **Why it was missed:** older than the rule: `83acdfe` (2026-10-15). Round 2's Lessons read, `ae53ed7` and round 3 reworded it (`86bbea6`, `efb8cef`). None of them moved the case.
- **Proposed:** fix: cut "CBC Run 3's first draft loaded on Markdown files, and was dropped for this." Line 190 becomes "**Memory or `CLAUDE.local.md`** holds a lesson the agent does not act on." The list ends with "*Its story: ADR-0053.*".

**LEO-8.** facts-in-sync §5 keeps a case as "It has happened".
- **Where:** `docs/conventions/facts-in-sync/README.md`, §5 *A disagreement*, lines 335–337.
- **Quote:** It has happened: CBC Run 3 showed a clause of `convention-lifecycle`,
- **The rule:** a case goes to its history, with one italic line pointing there. A short plain example may stay where the lesson does not read clearly without it, as long as the statement does not stand on it (`docs/conventions/conventions/` §2.6, *A lesson taken*).
- **What the text says:** the general rule is complete above it: "a Canonical Description is downstream of practice". The paragraph that follows is a case offered as evidence. The story line at 343 already names ADR-0034.
- **Stands:** uncertain. `08025aa` kept it on purpose, as "one plain example". Its body says the reviewer saw that commit at its boundary. Round 3's *Met in round 3* still listed it as a case in the body. Nothing since has ended it.
- **Why it was missed:** the rule is unclear where a plain example ends and a case begins.
- **Proposed:** question: is "It has happened: …" the short plain example §2.6 allows? If so, it stays. If it is the case, it goes, and the story line at 343 already points at ADR-0034.

## Found true, so not listed

- Every manual's *What it is for* tells its lived case. §2.2 asks for that, and ADR-0073 keeps it out of the rule.
- exchange §5.4, "CBC Run 3's text says *source*": round 2 declined it as an example (FINDING-157).
- agent-arrangement §5.3 and §5.6 name what this repo saw on each release. §5 asks every Tool Binding fact to name the release it was checked on.
- project-recording §5.4, "When it was capped tighter, it lost meaning": the reviewer took this wording as FINDING-959's fix. §7.5's "7 of the playbook's 9 Plan Steps" counts today's playbook. It is not a case.
- writing rule 5 names CBC Run 3's dropped words as an example. Rule 5's statement does not stand on it.
- The visual-comparison Agent Skill's §4 keeps its cases by design. The reviewer took that at `08025aa`'s boundary.
- Our 6 Agent Rules and 5 Agent Skills state their rules in general. Their decisions sit in the footers.
- The record forms with a Foundation Line state rules in general: PLAN's Plan Step Form, TODO's header, the CHANGELOG, README, ARCHITECTURE, glossary, devlog and ADR headers. The Plan Step Form's CBC Run 5 example is an example. TODO's items and PLAN's Plan Steps tell cases by their nature and state no rule.
- The Approaches on Trial's *Uses*, *Found* and *Lived* notes are dated notes kept by DECISION-18. DECISION-7 puts them outside §2.6. The concept and the 3 Idea Models are outside it too, and the Agent Model's claims carry evidence by their own form.
- conventions §1.1 lets a Work Approach name a CBC Run that lived a misreading. No derived file of ours does so wrongly.

## Met in passing

- The leftovers file is wrong on B5. It says commit-plan §2.9 and §2.12 are "gone". Both still stand, at lines 128–129 and 160–161, and are listed here as LEO-1 and LEO-2. B5's §2.7 italic now sits at lines 111–114.
- commit-plan §2.9's case says "CBC Run 3's Step 10 plan". `489ecf2`, which brought it in, says the SL-3 plan taught it. That may be a stale case detail. Not checked further.

## Not read

None. All 56 were read whole. `TODO-CONVERSATION-MEMORY.md` and `.claude/decisions.md` were read by header only, as assigned.
