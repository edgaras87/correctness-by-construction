# WA: Writing, Refinement Layers 1 and 2

Reader WA. Finding Kind: Writing, rules 1 to 10. Read at `70404e1`.
Files, each read whole:
- `docs/conventions/conventions/README.md` (366 lines);
- `docs/conventions/project-recording/README.md` (898 lines).

Script hits for these files: none.

Read first: `.claude/rules/writing.md`, `docs/conventions/writing/README.md`
§2, the Writing row of *The rules' check* in the last read,
`.claude/approaches-on-trial/refinement.md` §2.4 and §2.5, ADR-0079,
DECISION-1 to DECISION-40 and both lists of the agent's calls. The
close read's findings were checked in git at `b8c7d99`, mainly
FINDING-926 to 969, Reader A's.

7 findings: 5 checked, 2 resting on the reader, 0 uncertain.

## Findings

### `docs/conventions/conventions/README.md`

**WA-1.**
- **Where:** `docs/conventions/conventions/README.md`, §2.3 *The list of what derives*, lines 224–225.
- **Quote:** "*What this is made usable as* is the list a change to the page"
- **The rule:** writing rule 9: a defined thing is written by its Glossary Name (`.claude/rules/writing.md`, rule 9; `docs/conventions/writing/` §2, *Why each rule*, rule 9). DECISION-39 applied it to this exact verb: "A change here walks it" became "A change here runs the Change Walk on it", in this manual and every manual.
- **What the text says:** "the list a change to the page walks". "Walks" is the Change Walk, written as a lowercase verb. The same section's last sentence, line 233, already says "runs the Change Walk on that list".
- **Stands:** checked. `0803717` fixed line 37 and the old line "a change here walks that list" (now 233), but left lines 224–225 as `ab4c2e6` wrote them.
- **Why it was missed:** missed at a change. `0803717` worked DECISION-39 in this file, and its sweep for "walk" stopped at the two sentences the decision quoted.
- **Proposed:** fix: "*What this is made usable as* is the list the Change Walk runs on when the page changes, placed as the answer to the need. Each entry has:"

**WA-2.**
- **Where:** `docs/conventions/conventions/README.md`, §3 *Adding a convention*, lines 326–328.
- **Quote:** "header comment); the PLAN has no per-convention Plan Steps."
- **The rule:** writing rule 3: when an argument has parts, give each its own line or label; don't chain them with dashes and semicolons (`.claude/rules/writing.md`, rule 3).
- **What the text says:** "No CHANGELOG line and no Plan Step." has two parts. Their two reasons follow in one sentence, joined by a semicolon.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `0803717` rewrote line 328 for the close read and kept the semicolon. The check that should have caught it is that commit's re-read of its changed lines.
- **Proposed:** fix: "No CHANGELOG line and no Plan Step. The CHANGELOG logs the concept's versions, and has no place for a convention's entry (`CHANGELOG.md`'s header comment). The PLAN has no Plan Step per convention."

### `docs/conventions/project-recording/README.md`

**WA-3.**
- **Where:** `docs/conventions/project-recording/README.md`, §4.4 *How the devlog is written*, lines 375–377.
- **Quote:** "Written for future-you, not an audience: fragments fine, spelling"
- **The rule:** the writing rule's *Where it applies* puts every new or changed record line under rules 1 to 10. Its *Other styles* says a kind of text gets another style only when plain has been shown to fall short there, and the writing rule then names that kind and its style (`.claude/rules/writing.md`, *Where it applies* and *Other styles*; `docs/conventions/writing/` §1, *What it governs*). ADR-0079 says this line is a finding for the last read, not a rule in doubt.
- **What the text says:** it gives devlog entries a style of their own ("fragments fine, spelling irrelevant"). The writing rule names no such style, and rule 2 asks for short sentences. `devlog/README.md`, the devlog form in our Convention Seat, follows this line; that copy is leftover E12.
- **Related line, for the reviewer:** §11, rule 4, line 767: "The devlog may be messy; ADRs and the playbook must be clean." It may mean the content is raw (dead ends, hunches) or that the prose is. Only the second breaks the rule.
- **Stands:** checked for line 375. Line 767 is uncertain.
- **Why it was missed:** older than the rule. The line dates from `9a1637d` (2026-09-18), and the writing rule from ADR-0053 (2026-10-15). Round 3 read it, and the question of the rule's reach was settled only in ADR-0079.
- **Proposed:** fix: "- Written for future-you, not an audience: short plain sentences, as every record is, and honest." The next sentence, about "I don't understand why this works", stays as it is. Fix this line before `devlog/README.md` (E12), since that file follows it. For line 767, question: if "messy" means the voice, write "The devlog may be raw: dead ends, hunches, open questions. ADRs and the playbook must be settled."

**WA-4.**
- **Where:** `docs/conventions/project-recording/README.md`, §5.5 *When an item is written*, line 450.
- **Quote:** "so it stops occupying your head"
- **The rule:** writing rule 5: use plain words, not metaphor (`.claude/rules/writing.md`, rule 5). FINDING-322 fixed the same figure in §5.2: "An open loop held in the head costs attention" became "A thing known and not written down costs attention". DECISION-26 fixed "empties your head" too (FINDING-701).
- **What the text says:** the reason for adding an item at once is given as a head occupied.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `29e3ce0` (Refinement Round 3) changed this line and kept the figure. FINDING-322's fix was not carried to the other lines that use the same figure.
- **Proposed:** fix, together with WA-5: "is found, so no one has to remember it (§11, *The flow between records*, rule 3)."

**WA-5.**
- **Where:** `docs/conventions/project-recording/README.md`, §5.5 *When an item is written*, lines 450–451.
- **Quote:** "(§11, *The flow between records*, rule 3: moments,"
- **The rule:** writing rule 6: write references exactly (`.claude/rules/writing.md`, rule 6). A Fact Reference to a numbered step gives the step after the title, and a numbered rule's title is its bold lead (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
- **What the text says:** the reference ends "rule 3: moments, not schedules". The rule's bold lead, line 762, is "Update at natural moments, not on a schedule." The tail rewords it inside the address.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `29e3ce0` fixed the reference's title and kept the reworded tail. The Wiring script checks the title, not text after the step.
- **Proposed:** fix: "(§11, *The flow between records*, rule 3)", in WA-4's line.

**WA-6.**
- **Where:** `docs/conventions/project-recording/README.md`, §9.4 *How a playbook is written*, line 671.
- **Quote:** "1. **Birth:** the playbook's Plan Steps fill the plan, and its \"Steps"
- **The rule:** writing rule 9, as DECISION-36 reads it: "birth" as a noun for the event is the Name, CBC Run Birth; "born", "at birth" and "from birth" stay English.
- **What the text says:** the first of the playbook's four moments is labelled "Birth", a noun for the event.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `f435e8d` worked DECISION-36 in this file: "CBC Run Birth by name" at line 74, and the idioms at 175 and 244. It left this lead.
- **Proposed:** fix: "1. **At birth:** the playbook's Plan Steps fill the plan, …". The other three leads stay.

**WA-7.**
- **Where:** `docs/conventions/project-recording/README.md`, §12 *The fewest records needed*, lines 784–785.
- **Quote:** "The test for adding any record is always the same: *will someone —"
- **The rule:** writing rule 3, as the close read applied it: a dash that sets off an aside inside a sentence is fixed (FINDING-964, eight such dashes in this file, taken by the reviewer).
- **What the text says:** "*will someone — probably future-you — need this answer and be unable to reconstruct it?*" The aside sits between two dashes.
- **Stands:** checked.
- **Why it was missed:** older than the rule (`9a1637d`, 2026-09-18). FINDING-964's list of this file's dash asides missed it.
- **Proposed:** fix: "*will someone, probably future-you, need this answer and be unable to reconstruct it?*"

## Found true, so not listed

- **Numbered titles:** none is longer than 30 characters, and none carries a gloss, so rule 10 holds. "13.1 What a records table row holds" is exactly 30. §4.5 *When an entry is written*, §5.4 *How an item is written* and §5.5 *When an item is written* were retitled by Refinement Round 3, from *When* and *How*, so they stand alone. They have the same form as rule 10's own example, *How a plan is written*.
- **Conventions §2's titles:** §2.2 *The need*, §2.7 *The channel* and §2.8 *The boundary* were chosen by DECISION-20 (FINDING-303). §2.4 *The seats* and the per-seat headings with "seat" were declined at FINDING-942.
- **Line 49 of the conventions manual,** "What a convention is, its manual, with its Work Approaches one level down, …": this is FINDING-926's proposed text, taken by the reviewer.
- **"consumer"** (conventions line 77): English, the agent's call at FINDING-290.
- **"the birth entry"** (conventions lines 309 and 320): DECISION-23's own wording.
- **"the handbook"** (project-recording line 13): said in plain words once, as DECISION-23 asks.
- **Foundation Line values** (conventions §1.2 and §1.3): written as given, under ADR-0079 decision 3.
- **No Glossary Name is spelled in lowercase** in either file, apart from WA-1 and WA-6. Checked by grep for every Name in all four glossaries.
- **Bold:** "**The form**" (conventions line 182) is not a Name. "**Both Convention Seats**" (project-recording line 135) is a group label, which DECISION-15 already read as a lead. Local Map (§8.6) and Conversation Memory (§14) are defined without bold. Rule 9 allows bold there but does not require it.
- **Other semicolons in both files:** each joins a contrast pair or ends a list item, and none chains the parts of an argument. Round 3 read these lines twice. WA-2 is the one place where two labelled parts are chained.
- **"Steps from" line** (project-recording line 657): the sentence itself says what the line names, so rule 8 holds.

## Met in passing

- **Conventions §3, step 3 (line 308) and step 6 (lines 320–321):** "A convention entering or leaving the Container Group" and "lists … the conventions it received". DECISION-32 says a CBC Run holds no convention, only Work Approaches made from ours. This is the same as leftover B3, in this file.
- **Conventions *Where to look*, line 363:** "§1.3, *The Foundation Line*, above" is not a root path, and §2.9 asks for "Fact References only, as root paths". The bullet also joins two addresses with a semicolon.
- **Project-recording §13.1, lines 810–813:** a row names three things, but the text speaks of "the half that is new" and of a table read "in both directions". FINDING-335 judged only the figure.
- **Project-recording *What it is for*, line 16:** "four CBC Runs kept their records under these Record Stubs". CBC Runs 5 and 6 have been born since. Uncertain whether both count.
- **Project-recording *Why it arrives this way*, lines 866–868:** a rule read inside `PLAN.md` is cited to the Installed Channel. The glossary says the Installed Channel delivers nothing to the context window. Uncertain.
- **Leftover A5:** item 4 of *The Concept Deliverer's seat*, lines 92–93, now says "The index in §3.3, *Where ADRs live*, is the CBC Run's". §3.3 itself, line 296, still states the index for every repo. The leftover stands, but only in part.

## Not read

None. Both files were read whole.
