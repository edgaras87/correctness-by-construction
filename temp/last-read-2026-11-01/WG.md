# Reader WG: Writing, layer 6 (the container, `delivery/README.md`, the playbook, the Pure Seed)

Read at `70404e1`. All 22 files on the list were read whole, `.claude/decisions.md` among them. Every quote below was checked against `git show 70404e1:<path>` by script, at the line named.

## Findings

**WG-1.**
- **Where:** `delivery/fills/cbc-run-pure-playbook.md`, *The Plan Step Form*, the close item on stale words, line 99.
- **Quote:** "No living line in a record the Plan Step touched, or one that"
- **The rule:** writing rule 9: write a defined thing by its Glossary Name; a lowercase word is English only (`.claude/rules/writing.md`, rule 9). DECISION-35 says every lowercase use takes the Name Living Text. The container's glossary lists Living Text, so a CBC Run holds the Name.
- **What the text says:** "living line" means a line of Living Text, written in lowercase. Our `PLAN.md` holds the same item, and it now reads "No line of Living Text in a record the Plan Step touched" (lines 91, and the other Plan Steps' copies).
- **Stands:** checked.
- **Why it was missed:** missed at a change. `bcf3010` (DECISION-35's work) fixed the twin line in our `PLAN.md` but not the playbook it was copied from. `a456f4c` then edited the playbook and left the line. The Foundation Check at `bcf3010` should have caught the twin. The script's lowercase sweep looks for "living text", so it never finds "living line".
- **Proposed:** fix: "No line of Living Text in a record the Plan Step touched, or one that", as our `PLAN.md` reads.

**WG-2.**
- **Where:** `delivery/container/devlog/devlog.md`, header comment, line 5.
- **Quote:** "For your later self: fragments fine, honesty mandatory. Never rewrite an earlier entry."
- **The rule:** writing rule 2: write short sentences, one idea each (`.claude/rules/writing.md`, rule 2). The rules' check of the last read, doubt 8, settled that the writing rule covers every new record line. So a line telling the writer that "fragments" are fine is a finding (`temp/refinement-2026-10-18.md`, *The rules' check (§2.3)* under *The last read*; ADR-0079, *Context*).
- **What the text says:** the Record Stub tells every CBC Run that its devlog entries may be fragments. The line is also written in fragments. Doubt 8 named only our `devlog/README.md` and project-recording §4, the leftover E12. This is a third place, and it ships.
- **Stands:** checked.
- **Why it was missed:** missed at a change. `2fca3bf` edited this line and kept "fragments fine". Doubt 8 was decided later, and it named only our two lines.
- **Proposed:** question, decided with E12 and project-recording §4. If they change, this changes too, for example: "Write for your later self: short sentences, honestly. Never rewrite an earlier entry."

**WG-3.**
- **Where:** `delivery/container/README.md`, the opening paragraph, line 7.
- **Quote:** "adversity proves the wall. The problem is not yet chosen. It arrives"
- **The rule:** writing rule 9: a defined thing is written by its Glossary Name. A Name built on another carries it whole (`.claude/rules/writing.md`, rule 9). DECISION-19's table for the concept's group, row 16, turned "wall" into Structural Wall.
- **What the text says:** the sentence before it names the Structural Wall. This clause then calls it "the wall", a short form of the Name. The method and the concept write a bare "the wall" in prose nowhere else. The 5 bare uses in `delivery/method/` and `concept/` are field labels in an Output Shape.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `b451eb9` rewrote this paragraph and gave the first "wall" its Name. The second was left. The round 3 close read at `f5dfbbe` came after `b451eb9` and did not list it.
- **Proposed:** fix: "adversity proves the Structural Wall."

**WG-4.**
- **Where:** `delivery/installs/pure-seed.md`, step 4, the seed commits' subjects, lines 159 and 170.
- **Quote:** `git commit -m "chore: seed — method and stack skills, shapes, pin @ $deliverer_pin"`
- **The rule:** writing rule 9 (`.claude/rules/writing.md`, rule 9). The writing rule governs commit messages ("**Governs:** … commit messages"). DECISION-37 keeps Names out of code identifiers only, and a commit subject is not one.
- **What the text says:** the subjects write Agent Skills as "skills", Output Shapes as "shapes", and Plan Steps as "steps". Line 170 reads `git commit -m "chore: seed — steps into PLAN, cbc-run-pure $playbook_version @ $deliverer_pin"`. Every Newborn CBC Run reads these subjects, because the prompt tells it to read "every seed commit". Step 6's prompt (lines 215–216) and the checklist (lines 290–292) already write the Names. Our own commit subjects use the Names too, for example `fix(delivery): the cbc-slice Agent Skill meets the rule again`.
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. `5d562d8` edited both lines to rename the variable and left the words. The lines sit inside a code block, so a reader may have taken them for code.
- **Proposed:** fix: "chore: seed — method and stack Agent Skills, Output Shapes, pin @ $deliverer_pin" and "chore: seed — Plan Steps into PLAN, cbc-run-pure $playbook_version @ $deliverer_pin". The line 131 subject waits on the leftover G3.

**WG-5.**
- **Where:** `delivery/container/.claude/rules/delivered-copies.md`, rule 1, lines 21 and 23. These are script hits.
- **Quote:** "- the **Delivery Pin:** the Concept Deliverer's commit these copies equal, but for"
- **The rule:** writing rule 9: no Markdown mark marks a Name, except bold once, at the line that defines it. A list item's bold lead may begin with a Name (`.claude/rules/writing.md`, rule 9; ADR-0079, decisions 1 and 2).
- **What the text says:** Delivery Pin, and Read-Through Commit on line 23, are bold. Our glossary points both at `docs/conventions/exchange/` §2.2, which does not bold them. So these are the only bold uses in Living Text outside the glossaries, and they sit away from the home. Each item opens with "the", so the bold does not open the item, and ADR-0079's allowance for a list lead does not reach it as written. DECISION-22 took the same bold out of the exchange-read Agent Skill (FINDING-639). In a CBC Run, though, this Agent Rule is the only text that defines the two numbers, and the container's glossary entries name no home.
- **Stands:** uncertain.
- **Why it was missed:** the rule is unclear. It does not say which line defines a shared Name in a CBC Run when the delivered entry names no home.
- **Proposed:** question. Either (a) the bold goes at both lines, as at FINDING-639, recommended because the bold-once check counts our Master Copies; or (b) delivered-copies rule 1 is the CBC Run's defining line, and each item drops its "the" so the bold opens the item: "- **Delivery Pin:** the Concept Deliverer's commit …".

**WG-6.**
- **Where:** `delivery/container/.claude/decisions.md`, header comment, line 27.
- **Quote:** "fix it before the bootstrap commit."
- **The rule:** writing rule 8: before a label, ask whether the reader knows it, and if not, say it first in plain words (`.claude/rules/writing.md`, rule 8).
- **What the text says:** no text the CBC Run holds defines "the bootstrap commit". The phrase appears nowhere else in the repo. The Pure Seed names "the hygiene commit" and "the seed commits". Step 0 is "Bootstrap", and CBC Bootstrap is a Stack Group Name for a later Plan Step, so a reader can take the phrase three ways.
- **Stands:** resting on the reader.
- **Why it was missed:** the round 3 reads missed it. The line dates from `c3a737b` (2026-10-21), after the writing rule (ADR-0053), and has not changed since.
- **Proposed:** fix: "fix it before this file is first committed."

**WG-7.**
- **Where:** `delivery/container/CHANGELOG.md`, the *Versioning* placeholder, lines 5–7.
- **Quote:** "[SemVer](https://semver.org/); a Concept Repo versions its concepts;"
- **The rule:** writing rule 3: when an argument has parts, give each its own line or label, and don't chain them with dashes and semicolons (`.claude/rules/writing.md`, rule 3).
- **What the text says:** the placeholder chains three parts with semicolons: "An app releases SemVer; a Concept Repo versions its concepts; CBC Framing decides."
- **Stands:** resting on the reader. Two-part semicolons are common across the repo and were not listed. Only the chains of three are listed here and in WG-8.
- **Why it was missed:** missed at a change. The sentence is older than the rule (`e418e9d`, the starter kit), but `b451eb9` edited it ("Framing" to "CBC Framing") and left the chain.
- **Proposed:** fix: "Versioning: <what is a version here? An app releases [SemVer](https://semver.org/). A Concept Repo versions its concepts. CBC Framing decides. The answer replaces this placeholder.>"

**WG-8.**
- **Where:** `delivery/container/README.md`, the closing header comment, line 29.
- **Quote:** "outside. What changes weekly is PLAN.md's; why is the ADRs'; how"
- **The rule:** writing rule 3 (`.claude/rules/writing.md`, rule 3).
- **What the text says:** three homes are chained with semicolons: "What changes weekly is PLAN.md's; why is the ADRs'; how it went is the devlog's."
- **Stands:** resting on the reader.
- **Why it was missed:** missed at a change. The line is older than the rule (`dc3b7db`). `b451eb9` split the chained sentence right after it ("Chained comments split") and left this one.
- **Proposed:** fix: "What changes weekly is PLAN.md's. Why is the ADRs'. How it went is the devlog's."

## Found true, so not listed

- **Script hits, judged:**
  - `delivery/README.md:42`, "**Delivery Fills.**", is a list item's bold lead (ADR-0079, decision 2).
  - `delivery/container/PLAN.md:22`, "**Plan Step Gate** =", is at the home. The container's glossary makes the Plan Step Form "`PLAN.md`'s own", and our glossary points Plan Step Gate at our `PLAN.md`.
  - `pure-seed.md:260`, "the pure seed runs", quotes a devlog title exactly (rule 6).
- **Bold at home:** `shapes-lifecycle.md` line 9 bolds Output Shape, and the container's glossary points that Name there.
- **Titles:** no numbered title in the 22 files breaks rule 10. The Plan Step headings, the Agent Skill Stage headings and the TODO slot headings are form or unnumbered (DECISION-20).
- **Agent Skill names:** every one in prose carries its kind word (DECISION-27). The bare ones are in paths, `name:` lines or the Plan Step Form's parenthesis.
- **Settled words:**
  - "the shapes manual" (`delivery/README.md:21`): the glossary header allows the word with its kind word;
  - "birth entry", "birth dates", "at birth": attributive or idiom (DECISION-36, and DECISION-23's own wording);
  - "its birth" (`container.md:47`) and "(birth)" (`PLAN.md:68`): the CBC Run holds no CBC Run Birth Name;
  - "To the deliverer": a fixed label (FINDING-721);
  - "Local rules": the Entry File's slot heading;
  - "app bootstrap" in `.editorconfig`: FINDING-1287 was declined;
  - "day zero": kept (DECISION-26);
  - the playbook's Goals with bullets: DECISION-39;
  - "staged": the act is "stage a delivery" (FINDING-404's call).
- **Numbers:** the Pure Seed's "five placeholders" (lines 107, 307) count five. "the five of both groups" (line 145) counts 2 and 3 Agent Skills. The playbook's "Stage 2, item 4" lands on the decision-block item.
- **Leftovers for my files:** G2, G3, G4, G5, G6, G7 (`shapes-lifecycle.md` 73, `apply-retrospective` 89, `retrospective` 114–115 and 118), G11, the playbook's "Steps 5..N-3" and the Pure Seed's `git add`. All are still in the tree as described.

## Met in passing

- `delivery/fills/cbc-run-pure-playbook.md` line 165, "## Step 2: Identity (name, description, remote)". The Plan Step Form's parenthesis holds "the Agent Skill or Approach on Trial it runs" (line 29). Step 2 runs neither, and its parenthesis lists its stages. Layout or Agreement.
- `delivery/container/CHANGELOG.md` line 6 offers "a Concept Repo versions its concepts" as an answer in a CBC Run's own changelog, which is never a Concept Repo. Stale lines, perhaps.
- `delivery/installs/pure-seed.md` line 133 calls `concept/` "the mapping's one exception", while `delivery/README.md` line 17 says there is "No mapping". Agreement, minor.

## Not read

None.
