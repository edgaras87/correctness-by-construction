# Commit plan: knowledge/ and Defined Terms

## Summary — the state after all commits

The layers model leaves `temp/`. A new top folder, `knowledge/`, holds layers 1 to 3, one folder per layer, with no numbers in the names, and each folder made when its first file lands:

- `knowledge/backbone-ideas/`: the Backbone Ideas, layer 1;
- `knowledge/problem-domain-ideas/keeping-knowledge/`: the Problem Domain Ideas of keeping knowledge, layer 2;
- `knowledge/adapted-cases/<Problem Domain>/`: layer 3, one set of Adapted Cases for each Problem Domain, a kind of project, such as the System Repos'. No file lands there in this plan.

Layer 3 holds one set of Adapted Cases for each Problem Domain, true for every project of it; a project's own texts are layer 4. With no Maintainer Kit, this repo's own Adapted Cases are layer 4, kept whole in `.claude/`: the Instruction Text where it loads, its understanding beside it in `.claude/understanding/`, which never loads. The two layers documents say so.

Defined Terms is the first idea written: its Backbone Idea and its Problem Domain Idea under `knowledge/`, and this repo's own Adapted Case in `.claude/`. Under `knowledge/`, a Defined Term is defined in bold at its home, a text that uses another text's Defined Terms lists them in a Borrow Table with Fact References, and the agent finds one by its bold mark. The glossary does not list them. The Adapted Case's Paths Rule loads when the agent works under `knowledge/`. Writing rule 9 points `knowledge/` at the idea; elsewhere rule 9 stands, and the glossary stays for today's texts until the rewrite retires them (ADR-0082).

The two layers documents then move in, by their ideas' names:

- `knowledge/backbone-ideas/layers-of-knowledge.md`, the general document;
- `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`, the Maintainer Repo's document.

Each takes the Defined Terms idea: its definitions in one section, and a borrow table. Every Living Text pointer at their old paths is fixed. The Maintainer Repo's document says where each layer is kept, with the rules for placing a text, and `CLAUDE.md` points every session at it. TODO says the model's place is decided, and the Change idea's split, then depth c, are next. ADR-0084 records the layout, ADR-0085 the Defined Terms idea.

What it gives us: the model has a home outside the drafts, the Change idea's split knows where each of its texts goes, and Defined Terms have one home each without a second list to drift.

## Before the plan

The TODO item "Split the Change idea", staged now, is committed on its own first. It was decided before this Change Set.

## Commits

**1. `docs(agent): add commit plan for knowledge/`**
This plan, once agreed.

**2. `docs: ADR-0084, knowledge/ by layer`**
Proposed. Decision-first, as it was settled in the chat of 2026-11-23: the layout, with the options rejected (staying in `temp/`; a folder per Work Domain; numbered folders; short file names); the model's place decided before the change work, against the order the layers item and the document's header state. The ADR holds why; the Maintainer Repo's document holds the layout itself, from commit 11b.

**2b. `docs: ADR-0085, Defined Terms at their homes`**
Proposed. A decision of its own: it would hold wherever the files lived. Defined Terms at three layers, with the glossary's options rejected (every Name in the glossary; some or none; a file per group; an index by script; an index of lines; a scoped sentence in rule 9 alone); `cbc-concept/ideas/names.md` read by the reviewer, nothing taken.

**3. `docs: Defined Terms at layer 1`**
`knowledge/backbone-ideas/defined-terms.md`, the Backbone Idea, bound to no Work Domain. It creates `knowledge/`, so `ARCHITECTURE.md`'s codemap gains the folder in this commit. Sources: the problem file's *Defined Terms*, writing rule 9's form, the glossary TODO item's ideas. The body says `cbc-concept/ideas/names.md` was read by the reviewer on 2026-11-23 and nothing taken, so the later check of `cbc-concept` skips it.

**4. `docs: Defined Terms in keeping knowledge`**
`knowledge/work-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md`, layer 2: a Defined Term defined at the highest layer it holds; a home's definitions in one section; the borrow table; lookup by grep; a new Defined Term grepped across `knowledge/` first. The System Kit's own terms text is open, with its first guess and trigger.

**4b. `docs: the codemap gains knowledge/'s layer 2`**
Commit 4 made `work-domain-ideas/` without its codemap line.

**4c. `docs: ADR-0084 takes layer 4 into .claude/`**
ADR-0084, still Proposed, gains the reviewer's reading of 2026-11-23: layer 3 holds only what is true for every project of its use, and a project's own texts are layer 4. With no Maintainer Kit, this repo's own Adapted Cases are layer 4, kept whole in `.claude/`, their understanding in `.claude/understanding/`. `knowledge/` holds layers 1 to 3; `adapted-cases/keeping-knowledge/own/` goes. Rejected: own Adapted Cases at layer 3, used in place; layer 4 with instructions only; a layer-4 folder in `knowledge/`.

**4d. `docs: layer 2 sets apart the form and search`**
The Defined Terms Work Domain Idea takes the parts of commit 5's draft true for any repo keeping knowledge, by the arrow *set apart*: each definition a list item, the line "Borrowed:", the Borrow Table's two columns; and why the agent searches instead of reading a text whole.

**4e. `docs: layer 4 holds a project's own texts`**
One model change, both layers documents, so neither contradicts the other and no renumbered question is pointed at wrongly. The general document: an Adapted Case is written for every project of its use (§2.3); layer 4 holds a project's own texts, its own Adapted Cases among them, written from layer 2 where no layer-3 one covers the use (§2.4); the arrows *adapt*, *lesson* and *set apart* reach layer 4 (§3.2); its question 5 answered and gone; the picture to match. The Maintainer Repo's document: its own Adapted Cases leave layer 3 for layer 4, in `.claude/` (§2.3, §2.3.1, §2.4); the arrow *used in place* goes (§3.1, §3.3); its question 2 answered and gone, and question 12 follows; the picture to match. Every pointer at a renumbered question is fixed, and the problem file's table lines this makes false.

**4f.** Merged into 4e.

**4g. `docs: TODO adds renaming System Repo and Kit`**
Inserted: a TODO line decided while talking. System Repo and System Kit name no Problem Domain; they are renamed right after this plan, before the Change idea's split, whose trigger now waits for it.

**4h. `docs: ADR-0084 groups layer 3 by Problem Domain`**
ADR-0084, still Proposed, takes three decisions of 2026-11-23: layer 3 is grouped by Problem Domain, a kind of project, not by Work Domain; "Adapted Case" names the form, wherever it sits, and its owner says the layer; the System Kit is the System Repos' set at layer 3. Its decision 1's folder becomes `adapted-cases/<Problem Domain>/`, and decision 5 is reworded by Problem Domain. Rejected: layer 3 by Work Domain; a new Name for a project's own text, or for layer 3's; the System Kit apart from layer 3.

**4i. `docs: layer 3 is grouped by Problem Domain`**
Both layers documents, as one change. The general document: Problem Domain defined (§2); an Adapted Case is a Work Domain Idea written for one piece of work, as understanding with instructions (§2.3); layer 3 holds one set for each Problem Domain, true for every project of it; layer 4 is one project, its copies of its Problem Domain's Adapted Cases and its own where none covers its work (§2.4); the picture's labels to match. The Maintainer Repo's document: the System Repos' Problem Domain and its own named; the System Kit is the System Repos' set at layer 3, and "not a layer" goes (§2); its question 6 follows; its picture's label "the System Repos' problem" leaves the Work Domain box.

**4j. `docs: ADRs merge Work Domain into Problem Domain`**
ADR-0084 and ADR-0085, still Proposed, take the reviewer's reading of 2026-11-23: layer 2 is grouped by Problem Domain too, so Work Domain merges into it, and a layer-2 text is a Problem Domain Idea. The Maintainer Repo's Problem Domain is keeping knowledge, the System Repos' CBC backend design. A layer-2 title is its layer-1 title, ", in" and its Problem Domain. Rejected: layer 2 by Work Domain, a sort of work beside a kind of project; "keeping a concept" as the Maintainer Repo's Problem Domain; titles by the repo.

**4k. `docs: layer 2 is grouped by Problem Domain`**
One word and one grouping, across living text, so no text borrows a Name its home no longer defines. The general document: Work Domain gone, Problem Domain Idea defined (§2, §2.1, §2.2, §2.3), its question 1 answered, each Problem Domain writing its own adaptation, and the picture's layer-2 labels. The Maintainer Repo's document: its two Problem Domains by their names; its §2.2 tables regrouped by Problem Domain. The two Defined Terms texts, the problem file, the simulation and TODO follow; the Defined Terms Backbone Idea's question 1 is answered too. Every pointer at a renumbered question is fixed.

**4l. `docs: layer 2's folder by Problem Domain`**
`knowledge/work-domain-ideas/` becomes `knowledge/problem-domain-ideas/`. The Defined Terms Problem Domain Idea, moved with it, holds for keeping knowledge, no longer for every repo that keeps knowledge. The codemap and every pointer at the old path follow.

**4m. `docs: the general picture shows Problem Domains`** *(provisional: its shape is chosen at the commit)*
The general document's picture redrawn: layers 2 and 3 by Problem Domain, a Problem Domain's ideas above its set of Adapted Cases; layer 4 as projects, each with its copies and its own Adapted Cases; the arrows for a project's own Adapted Case kept. Chosen by the visual-comparison Agent Skill: what the reader must get, written first, and the candidates rendered and committed before the choice.

**5.** Dropped. Its draft held a layer-4 text; its parts went to 4d and to commit 8.

**6. `docs: writing rule 9 sends knowledge/ to its idea`**
The writing manual, the home of rule 9, gains one sentence: under `knowledge/`, rule 9 does not apply, a defined thing there follows the Defined Terms Problem Domain Idea of keeping knowledge, and the glossary does not list it. All of rule 9 steps aside, not its glossary part alone: the Defined Terms texts allow a short form, which rule 9 forbids. A Canonical Description changes, so the Change Walk runs: the glossary's header, "every thing this repo defines", gains "outside `knowledge/`" in this commit; our Agent Rule follows in commit 7; the copy delivered to CBC Runs stays, since a CBC Run has no `knowledge/`. Rule 9 says a hyphenated word counts as one; the Defined Terms texts do not, so the Problem Domain Idea's open questions gain it in this commit, its trigger the first hyphenated Defined Term.

**7. `chore(agent): writing rule follows rule 9`**
`.claude/rules/writing.md` follows the manual.

**7b. `docs: own Adapted Cases carry no Foundation Line`**
The conventions manual's §1.3 gains one exception, beside the Approach on Trial's: this repo's own Adapted Cases in `.claude/` carry no Foundation Line until the rewrite brings it into the layers model, the trigger written beside the exception. A Canonical Description changes, so the Change Walk runs; `.claude/rules/foundation-check.md` reads only files with a Foundation Line, and is checked for a line this makes false.

**7c. `docs: rule 9 steps aside for own Adapted Cases`**
Inserted: commit 8's two files sit in `.claude/`, where rule 9 still applied, and both must use Defined Terms. Rule 9 now does not apply under `knowledge/`, under `.claude/understanding/`, or in an Agent Skill or Agent Rule whose understanding sits there: the set 7b names. The glossary's header says it lists what is defined where rule 9 applies, pointing at rule 9 instead of naming the folders.

**7d. `chore(agent): writing rule follows the wider scope`**
`.claude/rules/writing.md` follows 7c, and `CLAUDE.md`'s records table row sends a thing defined where rule 9 applies to the glossary.

**8. `chore(agent): add the Defined Terms Adapted Case`**
This repo's own Adapted Case for Defined Terms, at layer 4, both halves in one commit: its understanding, `.claude/understanding/defined-terms.md`, the parts of commit 5's draft true only here (`knowledge/` only while the rewrite runs, the twin names, the glossary in the collision search, why a Paths Rule); and its Instruction Text, the Paths Rule `.claude/rules/defined-terms.md` on `knowledge/**`. Its `.claude/decisions.md` entry. The Paths Rule carries no Foundation Line (7b). The understanding half's header names what it stands on, the Defined Terms Problem Domain Idea of keeping knowledge, and what stands on it, the Paths Rule.

**8b. `docs: the codemap gains .claude/understanding/`**
`ARCHITECTURE.md` maps the new folder; a commit of its own, since the `agent` scope touches nothing else.

**8c. `docs: Defined Terms names what stands on it`**
The Defined Terms Problem Domain Idea's header gains "What stands on it": this repo's Adapted Case, `.claude/understanding/defined-terms.md`. With no Foundation Line, the headers carry the link, so a change to the idea finds the Adapted Case (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, its Rules).

**9. *(provisional)* Whether `knowledge/` is a Canonical Description**
Asked here, and whether it waits for the rewrite with the Foundation Line (7b). If yes: the facts-in-sync manual's §4 gains `knowledge/`, then `.claude/rules/foundation-check.md` follows, two commits. If no: no commit, and ADR-0084 says why.

**10. `docs: move the layers document to knowledge/`**
The general document to `knowledge/backbone-ideas/layers-of-knowledge.md`: its title "The layers of knowledge"; its header; every Living Text pointer at its old path, about 34, in the same commit.

**11. `docs: move the Maintainer Repo's layers document`**
To `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`: its title gains ", in keeping knowledge"; its header's "Its place in the repo" now says where; every Living Text pointer at its old path, about 69, in the same commit.

**11b. `docs: where each layer is kept, and its rules`**
The Maintainer Repo's document's §2 says where each layer is kept, replacing its line that this is decided later. With the folder list go the rules for placing a text: one folder per layer; no numbers in folder names; a folder made when its first file lands; a file named after its idea, its title matching; layers 1 to 3 under `knowledge/`, layer 3 by Problem Domain; this repo's own Adapted Cases whole in `.claude/`, their understanding in `.claude/understanding/`; a new text's row in the document's table, with its Home. Its own commit, since the move is a rename and this is the layout's home.

**11c. `chore(agent): CLAUDE.md points at knowledge/`**
One line in the Entry File, loaded in every session: `knowledge/` holds the layers model, and where a text goes is the Maintainer Repo's document's §2. A pointer, not a retelling: a Local Rule, since nothing announces the moment a new text is placed (`docs/conventions/agent-arrangement/` §2.4, *How the Entry File is written*). No understanding text: the line holds no rule of its own, its reasons are ADR-0084's, and `CLAUDE.md` comes into the layers model whole, with the Agent Model's rewrite. Not an Agent Rule loaded in every session: placing is not every task, and it would restate §2.5. A Paths Rule would load only once a file under `knowledge/` is read, too late for a session about to place a new idea elsewhere. After 11b, since it points at it.

**12. `docs: the layers document takes Defined Terms`** *(provisional: shaped by commits 3 to 4m)*
The general document's definitions gathered into one section, and its borrow table.

**13. `docs: Maintainer layers doc takes Defined Terms`** *(provisional: shaped by commits 3 to 4m)*
The same for the Maintainer Repo's document, its short forms with them. Asked here: the Defined Terms it borrows from the problem file, which stays in `temp/`; and its bold leads that begin with a Defined Term, such as "**Kit Update,**", which rule 9 allows and the Defined Terms texts do not say, since commit 6.

**14. `docs: TODO follows knowledge/ and Defined Terms`**
The layers item: the model's place decided, its order as now. The depth c item: due after the Change idea's split. The glossary item, "Decide which names go in the glossary": closed, if the Defined Terms texts answer it, what is left going to their open points; the reviewer decides at the commit. A new item: the System Kit's Defined Terms, first guess one terms text in the System Kit, its trigger the first System Repo Adapted Case written.

**15. `docs: ADR-0084 and ADR-0085 accepted`**
The final records commit.

**16. `docs(agent): close commit plan for knowledge/`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **Defined Terms before the move,** so the moved documents have their rules the moment they land.
- **Each move is a commit of its own, and its fit to Defined Terms another.** The move is a rename with its pointers, the fit a change of content; each reverts alone, and git sees the rename.
- **The pointers go with their move,** as the rename grep asks (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*). History keeps its old paths: the devlog, the ADRs, `TODO-CONVERSATION-MEMORY.md`.
- **The manual before the Agent Rule,** home before follower, two commits since the `agent` scope stands alone.
- **The delivered writing rule is not touched.**
- **The simulation, the flow file and the problem file stay in `temp/`,** as sources.
- **Two ADRs, one per decision:** the layout and Defined Terms each stand without the other.
- **No idea of its own for the layout:** where each layer is kept is what the Maintainer Repo's document adds, by its own table row.
- **The model changes before the Adapted Case lands** (4e before 8): the Adapted Case stands at layer 4, which the model says holds a project's own texts only from 4e.
- **The two halves of the Adapted Case in one commit** (8): understanding with no instruction, or the reverse, is not an Adapted Case.
- **No Foundation Line for this repo's own Adapted Cases until the rewrite** (7b): the Foundation Line is brought into the layers model once, with the facts-in-sync manual, never patched for a path value first. Until then the headers carry what a text stands on.
- **Commit 5's number is kept, and marked dropped,** so the numbers already cited stay true.
- **The devlog entry comes after the close,** at the session's end.
