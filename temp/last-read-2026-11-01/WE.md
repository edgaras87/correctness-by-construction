# WE: Writing, Refinement Layer 4

Reader WE. Finding Kind: Writing, writing rules 1 to 10
(`.claude/rules/writing.md`; `docs/conventions/writing/` §2, *Why each
rule*). Files: `ARCHITECTURE.md`, `CHANGELOG.md` (header and
[Unreleased]; [v1] is history), `devlog/README.md`, `.editorconfig`,
`.gitattributes`, `.gitignore`, `PLAN.md`, `README.md`,
`temp/README.md`, `TODO.md`, `docs/adr/README.md`, each read whole;
`TODO-CONVERSATION-MEMORY.md` by header and headings. Tree at
`70404e1`.

15 findings: 11 checked, 2 resting on the reader, 2 uncertain.

Six of them (WE-1 to WE-5, and WE-15 in part) are fixes the round 3
close read's endings list as made that never landed, the kind
DECISION-34 named. I checked every FINDING-1152 to 1221 (reader E's)
against the tree. These are the ones still in place.

---

**WE-1.** rule 9; checked.
- **Where:** `temp/README.md`, body, line 18; `TODO.md`, Next, "Decide which ideas here are Idea Models", line 767.
- **Quote:** "the records map lists" (temp 18); "refinement's DECISION-12 map shows" (TODO 767).
- **The rule:** writing rule 9 (`.claude/rules/writing.md`): a defined thing is written by its Name or in plain words. DECISION-23 took "map" for anything but the Local Map. FINDING-1235's call names project-recording §1 "project-recording's list of the records".
- **What the text says:** both lines call project-recording §1 a "map", the word DECISION-23 keeps for the Local Map.
- **Why it was missed:** temp 18 is FINDING-1171's line. The endings list 1171 as fixed. The line never changed: `c57a713` and `a6f2a67` touched the file, and `fab7214` fixed only `CLAUDE.md` for 1235. TODO 767 was not in 1171's list. No grep for "map" ran at either fix.
- **Proposed:** fix: "which project-recording's list of the records names"; TODO 767: "as project-recording's list of the records shows (the refinement's DECISION-12)".

**WE-2.** rule 9; checked.
- **Where:** `TODO.md`, Next, the item's title, lines 885-886.
- **Quote:** "how to treat a Skill"
- **The rule:** writing rule 9: a Name built on another Name carries it whole: "Agent Skill Template, never Skill Template".
- **What the text says:** "a Skill Template".
- **Why it was missed:** this is FINDING-1199. Its ending was "fixed", but `bcf3010` changed only line 898. A miss at the fix, the DECISION-34 kind.
- **Proposed:** fix: "how to treat an Agent Skill Template". Grep the title's first words first, since a trigger may quote them.

**WE-3.** rule 9; checked.
- **Where:** `TODO.md`, Next, "Decide whether our own forms become Output Shapes", lines 480-481.
- **Quote:** "rules: a manual's, a CBC Run Reading's."
- **The rule:** writing rule 9. FINDING-1190: "rule" written for Agent Rule takes the Name.
- **What the text says:** "The open forms are those in rules". These are `convention-manual.md` and `exchange-reading.md`, both Agent Rules.
- **Why it was missed:** FINDING-1190 names line 480 and is listed as fixed. `bcf3010` did not change it.
- **Proposed:** fix: "The open forms are those in Agent Rules: a manual's, a CBC Run Reading's."

**WE-4.** rule 8; checked.
- **Where:** `TODO.md`, Later: "Name when a CBC Run is read", line 1138; "Decide how CBC Run Readings work…", line 1150; "Say once that a CBC Run Reading's decisions…", line 1158; "Harvest how public docs beyond the README live…", line 1257.
- **Quote:** "(2026-10-01, the working draft)" (1138); "the milestone that fires it" (1257).
- **The rule:** writing rule 8: before a label, ask whether the reader holds it. If not, say it in plain words first. TODO's form asks for "<who raised it>".
- **What the text says:** "the working draft" names a deleted draft, not who raised the item (devlog 2026-10-01, later: "The draft is gone"). "The milestone" is never named.
- **Why it was missed:** these are parts of FINDING-1214. It is listed as fixed, but `bcf3010` changed 248, 853, 1026 and 1139 only.
- **Proposed:** question: who raised the three, or else plain words, "(2026-10-01, from the draft of working a reading, now gone)". Which milestone fires the 1257 item: for example, "a CBC Run first writing public docs beyond its README"?

**WE-5.** rule 8; checked.
- **Where:** `temp/README.md`, body, line 15.
- **Quote:** "once it has served, and git history keeps every version."
- **The rule:** writing rule 8.
- **What the text says:** "Each is deleted once it has served". It does not say when that is.
- **Why it was missed:** FINDING-1167 named this line with the codemap's. The codemap was fixed (`ARCHITECTURE.md` 256); this line was not.
- **Proposed:** fix: "Each is deleted once the work that needed it is done, and git history keeps every version."

**WE-6.** rule 9; checked.
- **Where:** `TODO.md`, Next, "Rewrite the method's texts plain", lines 646-647.
- **Quote:** "the Output Shapes, the cbc-slice Agent Skill's" (646), then "Agent Skill and workflow (`2674c03`)." (647).
- **The rule:** writing rule 9. Agent Skill names the whole folder: its `SKILL.md` and what it references (`docs/glossary.md`, Agent Skill).
- **What the text says:** "the cbc-slice Agent Skill's Agent Skill and workflow". The line used to say "`cbc-slice`'s skill and workflow", meaning the `SKILL.md` file and its workflow reference. The kind-word replacement doubled the Name.
- **Why it was missed:** introduced at `bcf3010`, and its diff read missed it.
- **Proposed:** fix: "the cbc-slice Agent Skill's `SKILL.md` and workflow".

**WE-7.** rule 9; checked.
- **Where:** `TODO.md`, Next, "Read text for its level in the chain", line 629.
- **Quote:** "conventions §1 is the item above"
- **The rule:** writing rule 9, with DECISION-24 and the glossary's header. A one-word convention is named by its path, its word with its kind word, or its Name, never by the bare word. Line 620 of the same item writes "the conventions manual §1".
- **What the text says:** a bare "conventions §1". It is the only one in Living Text outside `temp/` (grep).
- **Why it was missed:** written at `580acdc`, 2026-10-31, after DECISION-24. Missed at that change and by round 3's close read.
- **Proposed:** fix: "the conventions manual §1 is the item above".

**WE-8.** rule 9; checked.
- **Where:** `TODO.md` 40 ("Read CBC Run 6"), 48 ("Unlock the folders"), 682 ("Run this repo's retrospective"), 705 ("Read the frozen CLAUDE template's…").
- **Quote:** "Trigger: the close of the Plan Step that runs CBC Run 5's birth." (682).
- **The rule:** writing rule 9, by DECISION-36. "Birth" as a noun for the event is the Name CBC Run Birth. "Born", "at birth" and "from birth" stay English.
- **What the text says:** four nouns for the event: "Its birth Plan Step" (40), "before its birth" (48), "CBC Run 5's birth" (682), "No birth can judge" (705). Line 927 already writes "CBC Run 5's CBC Run Birth".
- **Why it was missed:** DECISION-36's fix, `bcf3010`, took only the lines FINDING-1181 listed. No grep for "birth" ran. Line 682 is also leftover E8, as a passed trigger. This finding is about the word.
- **Proposed:** fix: "The Plan Step of its CBC Run Birth stopped"; "before its CBC Run Birth"; "CBC Run 5's CBC Run Birth"; "No CBC Run Birth can judge".

**WE-9.** rule 9; checked.
- **Where:** `TODO.md`, Known issues, line 1275.
- **Quote:** "The Runtime Ground template"
- **The rule:** writing rule 9. Agent Skill Template is a Name, and a particular one is named by its file (`docs/glossary.md`, Agent Skill Template).
- **What the text says:** the file meant is the infra-establish Agent Skill's `templates/compose.yaml`, which says `postgres:17` (checked). "Template" is lowercase. FINDING-1169 and 1200 fixed the same word elsewhere.
- **Why it was missed:** at `e5a874b`, which changed "The ground template" to this. The change took the Name Runtime Ground and left "template".
- **Proposed:** fix: "The infra-establish Agent Skill's Agent Skill Template `templates/compose.yaml`".

**WE-10.** rule 9; checked.
- **Where:** `TODO.md`, Next, "Decide whether a commit plan's look-back…", lines 84-85. Its home is `.claude/approaches-on-trial/auto-run.md` line 48, in Refinement Layer 5.
- **Quote:** "Real question being what the auto-run Approach on Trial calls one it must not decide" (TODO 85).
- **The rule:** writing rule 9. A thing a text gives a meaning English does not has a Glossary Name: two or more words, each capitalized, listed in the glossary. A lowercase word is English.
- **What the text says:** auto-run defines "a Real question, one the CBC Run must not decide alone". It has one capital, and neither glossary lists it (grep).
- **Why it was missed:** lines 84 and 85 were rewritten at `e5a874b` and `bcf3010` around the word. It was missed at both changes, and the round 3 reads never met it.
- **Proposed:** question: give it a Name, with an entry pointing at auto-run.md, or use plain words, "a question the CBC Run must not decide alone", here and at its home.

**WE-11.** rule 6; checked.
- **Where:** `PLAN.md`, Step: Birth CBC Run 6, own items, line 159.
- **Quote:** "CBC Run 6's CBC Run Briefing is the reviewer's: checkout, in"
- **The rule:** writing rule 6: write defined names exactly. FINDING-1210's ending puts a CBC Run's own name in backticks, as in the `ARCHITECTURE.md` §2.5 table. FINDING-1183 found that a bare "checkout" reads as English.
- **What the text says:** a bare "checkout". Line 138 of the same Plan Step writes `checkout`.
- **Why it was missed:** FINDING-1183 listed line 138 only, and 1210 listed TODO only.
- **Proposed:** fix: "is the reviewer's: `checkout`, in".

**WE-12.** rule 9; uncertain.
- **Where:** `PLAN.md`, the titles of two Plan Steps, lines 213 and 301.
- **Quote:** "(`.claude/rules/working-a-reading.md`, `commit-plan`, the Foundation Check)" (213).
- **The rule:** writing rule 9. DECISION-27 writes an agent part with its kind word always (`docs/conventions/conventions/` §1.5, *Naming a Work Approach*).
- **What the text says:** the titles list `commit-plan` (213, 301) and `approach-drafting`, `approach-evaluation` and `visual-comparison` (301). These are bare names in backticks: not paths, and with no kind word. Line 135 uses paths and a Name instead.
- **Why it was missed:** the rule is unclear here. FINDING-1158 asked whether a Plan Step title's parenthesis, a list the Plan Step Form defines, counts as a labelled list. Its ending was "fixed", and no call answered the question.
- **Proposed:** question: does the title's list take the kind word, "the commit-plan Agent Skill", or the path? Or does it stand as the form's list?

**WE-13.** rule 8; resting on the reader.
- **Where:** `README.md`, *Success criteria*, line 33 (also 38); `ARCHITECTURE.md` §3, *What must stay true*, line 212.
- **Quote:** "the archive copy is demoted to a historical snapshot." (README 33); "the archive it came from is a frozen snapshot, never a source" (ARCHITECTURE 212).
- **The rule:** writing rule 8: say a thing in plain words before the reader needs it.
- **What the text says:** README is for someone arriving from outside, as its header says. It names "the archive" at 33 and 38. It says what the archive is, "the archive repo, `system-design-method`", only at 55. `ARCHITECTURE.md` never says.
- **Why it was missed:** README 33 is older than the rule (`8032035`, 2026-08-27), and the round 3 reads did not list it.
- **Proposed:** fix: README 33: "the copy in the archive repo, `system-design-method`, is demoted to a historical snapshot"; ARCHITECTURE 212: "the archive repo it came from, `system-design-method`, is a frozen snapshot".

**WE-14.** rule 8; resting on the reader.
- **Where:** `TODO.md`, Next, "Read text for its level in the chain", line 619.
- **Quote:** "Found at the design's commit 5"
- **The rule:** writing rule 8. Writing rule 6 adds that a local number carries its owner.
- **What the text says:** "the design" is named nowhere in the item. It is the design of DECISION-19, 29 and 32, ADR-0078. The reader cannot tell which commit 5 is meant.
- **Why it was missed:** at `af6a3ea`, 2026-10-31, and not listed by round 3's close read.
- **Proposed:** fix: "Found at commit 5 of ADR-0078's commit plan".

**WE-15.** rule 5; uncertain.
- **Where:** `TODO.md` 703 ("Read the frozen CLAUDE template's…"); 1066 ("Name the discipline…").
- **Quote:** "from the method's first" (703); "not master text" (1066).
- **The rule:** writing rule 5, with DECISION-26's journey row ("the walk") and master row.
- **What the text says:** "the method's first walk", and a proposed name, "lived is evidence, not master text".
- **Why it was missed:** this is FINDING-1207's question part. Its ending was "fixed", and no call answered either question. "walk 1" may be a trial's label (`docs/baselines/cbc-derived-claude-walk1.md`).
- **Proposed:** question: is "walk" a label, so it stands? Is "master" in a quoted proposed name a figure? If both are figures: "from the method's first trial"; "lived is evidence, not text to copy".

---

## Found true, so not listed

- **Script hit, `PLAN.md` 12, "**Plan Step Gate** =":** it meets writing rule 9. The Name is bold once in the file at the line that defines it, and the file is the one its glossary entry names ("the Plan Step Form in our `PLAN.md`"). The legend sits just above the form's heading. The container's legend is reader G's.
- **Bold elsewhere:** each one in these files is a list item's bold lead (allowed by ADR-0079) or a bold sentence that is not a Name.
- **Numbered titles:** `ARCHITECTURE.md`'s titles are all 30 characters or fewer, with no gloss. The Conversation Memory headings are history (DECISION-18).
- **Reader E's 70 close-read findings, FINDING-1152 to 1221:** checked against the tree. All landed but those in WE-1 to WE-5 and WE-15.
- **Settled lines:** "made usable" lowercase (FINDING-525); "day zero" (DECISION-26); "app bootstrap" (FINDING-1287 declined); "records table" and "working arrangement" English (DECISION-23); a Plan Step's generic "stage" (FINDING-1176's call).
- **`devlog/README.md`'s "fragments fine":** this is leftover E12. Not listed again.
- **`TODO-CONVERSATION-MEMORY.md`:** its title takes the Name (FINDING-1219, fixed). Its header is plain.

## Met in passing

- **Leftover E6 is not gone:** `TODO.md` 397-403 still names "three Chain Links … derives … points … governs". The glossary lists four, and "derives" is not one of them. The quote failed to match only because the parentheses split it.
- **Two sentences start in lowercase:** `TODO.md` 208 "the cbc-framing Agent Skill hands over" and 210 "the approach-drafting Approach on Trial's Stage 1". Both come from the kind-word replacement. This is the same kind as leftover E15.
- **`ARCHITECTURE.md` disagrees with itself:** 131-132 lists the Stack Group as deriving from the concept. §2.2 (148) says it is "Not derived from the concept but checked against it".
- **`TODO.md` 593-595, "the manual by (`…` §2, …), each … from it by (`…` §1, …)":** a Fact Reference stands where a noun should be.
- **`ARCHITECTURE.md` 218:** its *Stated in* cell sits in parentheses. No other row's does.

## Not read

None.
