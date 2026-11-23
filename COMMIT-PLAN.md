# Commit plan: knowledge/ and Defined Terms

## Summary — the state after all commits

The layers model leaves `temp/`. A new top folder, `knowledge/`, holds it, one folder per layer, with no numbers in the names, and each folder made when its first file lands:

- `knowledge/backbone-ideas/`: the Backbone Ideas, layer 1;
- `knowledge/work-domain-ideas/keeping-knowledge/`: the Work Domain Ideas of keeping knowledge, layer 2;
- `knowledge/adapted-cases/keeping-knowledge/own/`: the Maintainer Repo's own Adapted Cases, layer 3.

Defined Terms is the first idea written there, at all three layers. Under `knowledge/`, a Defined Term is defined in bold at its home, a text that uses another text's Defined Terms lists them in a borrow table with Fact References, and the agent finds one by grep. The glossary does not list them. A Paths Rule, the Instruction Text of the Defined Terms Adapted Case, loads when the agent works under `knowledge/`. Writing rule 9 points `knowledge/` at it; elsewhere rule 9 stands, and the glossary stays for today's texts until the rewrite retires them (ADR-0082).

The two layers documents then move in, by their ideas' names:

- `knowledge/backbone-ideas/layers-of-knowledge.md`, the general document;
- `knowledge/work-domain-ideas/keeping-knowledge/layers-of-knowledge-in-the-maintainer-repo.md`, the Maintainer Repo's document.

Each takes the Defined Terms idea: its definitions in one section, and a borrow table. Every Living Text pointer at their old paths is fixed. The Maintainer Repo's document says where each layer is kept, with the rules for placing a text, and `CLAUDE.md` points every session at it. TODO says the model's place is decided, and the Change idea's split, then depth c, are next. ADR-0084 records the layout, ADR-0085 the Defined Terms idea.

What it gives us: the model has a home outside the drafts, the Change Adapted Cases have a layer-3 folder to be written into, and Defined Terms have one home each without a second list to drift.

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

**5. `docs: Defined Terms' own Adapted Case`** *(provisional: its name and file name are decided at the commit)*
The Maintainer Repo's own Adapted Case, under `knowledge/adapted-cases/keeping-knowledge/own/`: its Adapted Understanding Text, saying why its Instruction Text, commit 8, is as it is.

**6. `docs: writing rule 9 sends knowledge/ to its idea`**
The writing manual, the home of rule 9, gains one sentence: under `knowledge/`, Defined Terms follow the Defined Terms idea, and the glossary does not list them. A Canonical Description changes, so the Change Walk runs: our Agent Rule follows in commit 7; the copy delivered to CBC Runs stays, since a CBC Run has no `knowledge/`.

**7. `chore(agent): writing rule follows rule 9`**
`.claude/rules/writing.md` follows the manual.

**8. `chore(agent): add Paths Rule for Defined Terms`**
The Adapted Case's Instruction Text: a Paths Rule on `knowledge/**`, saying how to write a Defined Term, borrow one, and look one up. Its `.claude/decisions.md` entry. Asked here: what its Foundation Line names, since the conventions manual's values name no text under `knowledge/`.

**9. *(provisional)* Whether `knowledge/` is a Canonical Description**
Asked here. If yes: the facts-in-sync manual's §4 gains `knowledge/`, then `.claude/rules/foundation-check.md` follows, two commits. If no: no commit, and ADR-0084 says why.

**10. `docs: move the layers document to knowledge/`**
The general document to `knowledge/backbone-ideas/layers-of-knowledge.md`: its title "The layers of knowledge"; its header; every Living Text pointer at its old path, about 34, in the same commit.

**11. `docs: move the Maintainer Repo's layers document`**
To `knowledge/work-domain-ideas/keeping-knowledge/layers-of-knowledge-in-the-maintainer-repo.md`: its title gains ", in the Maintainer Repo"; its header's "Its place in the repo" now says where; every Living Text pointer at its old path, about 69, in the same commit.

**11b. `docs: where each layer is kept, and its rules`**
The Maintainer Repo's document's §2 says where each layer is kept, replacing its line that this is decided later. With the folder list go the rules for placing a text: one folder per layer; no numbers in folder names; a folder made when its first file lands; a file named after its idea, its title matching; an Instruction Text in `.claude/`, pointed at from its Adapted Understanding Text; a new text's row in the document's table, with its Home. Its own commit, since the move is a rename and this is the layout's home.

**11c. `chore(agent): CLAUDE.md points at knowledge/`**
One line in the Entry File, loaded in every session: `knowledge/` holds the layers model, and where a text goes is the Maintainer Repo's document's §2. A pointer, not a retelling. With §2's rules, it is a small Adapted Case: the rules its understanding, the line its Instruction Text. A Paths Rule would load only once a file under `knowledge/` is read, too late for a session about to place a new idea elsewhere. After 11b, since it points at it.

**12. `docs: the layers document takes Defined Terms`** *(provisional: shaped by commits 3 to 5)*
The general document's definitions gathered into one section, and its borrow table.

**13. `docs: Maintainer layers doc takes Defined Terms`** *(provisional: shaped by commits 3 to 5)*
The same for the Maintainer Repo's document, its short forms with them. Asked here: the Defined Terms it borrows from the problem file, which stays in `temp/`.

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
- **The devlog entry comes after the close,** at the session's end.
