# Commit plan: the Take, a Defined Term

## Summary — the state after all commits

The System Repo's act of taking a System Kit Update has a Defined Term, the System Kit Update Take, in the Common Ground Problem's Defined Terms, pointing at the simulation's §8 for how it runs. The simulation's short-forms table shortens it to Take, as it does Update and Version. Every noun use of the act in the drafts and TODO reads "the Take", "a Take", "the Take's branch", so it no longer reads as the English word. The verb stays English: "the System Repo takes the Update", "the Update is taken".

## Commits

**1. `docs(agent): add commit plan for the Take`**
This plan, agreed before any of the work.

**2. `docs: temp defines the System Kit Update Take`**
The name exists before any text uses it: the Defined Term in the problem file, and the row "Take | System Kit Update Take" in the simulation's short-forms table.

**3–5. One commit per file group, in this order:**

- **3. `docs: temp's simulation writes the Take`** — about 60 hits. Four bold leads change with them: §4's *After a Take*, and §8's *Before the Take*, *At the Take, in order* and *A postponed Take*. The flow file's six Fact References to them follow in this commit, by the rename grep.
- **4. `docs: temp's flow writes the Take`** — about 72 hits, and the flow file's list of the simulation's short forms gains Take.
- **5. `docs: temp's drafts and TODO write the Take`** — the problem file's §2.1 block, the layers document's §3.3, and TODO's items.

Each hit is judged by hand: the act's noun is capitalized, and the verb and plain English stay. One commit per file group, so each diff can be read against one text.

**6. `docs(agent): close commit plan for the Take`**
Deletes this file. Before it, a grep for "the take", "a take" and "take's" across Living Text in `temp/common-ground/` and TODO, unwrapped, and each changed sentence re-read for what it now claims. The body records what diverged.

## Decisions taken inside this plan

- **The name: System Kit Update Take, short form Take.** It carries "System Kit Update" whole (writing rule 9), and is 4 words. Rejected: "Update Take", which drops part of the Name it is built on.
- **Its home: the problem file's Defined Terms,** like System Repo Reading, pointing at the simulation's §8, the one home of the facts of Change. Rejected: the layers document's §2, which defines the layers and their parts, not the steps of Change.
- **Only the noun is capitalized.** "take", "takes", "taken" and "taking" as verbs stay English. The part's label, Take, in the simulation's §8 heading and §1 table and the layers document's §3.2 table, is already capitalized and stays.
- **Not in `docs/glossary.md`.** The drafts' Defined Terms have their one home in the problem file; none is in the glossary.
- **The frozen `temp/common-ground/between-repos-simulation.md` is left as it is,** since it is frozen input. History keeps its words.
- **The flow file's "short words" becomes "short forms"** in commit 4, the simulation's word since 2026-11-19. The line changes there anyway.
- **The pictures keep their alignment:** "take" and "Take" are the same length, so no column moves.
