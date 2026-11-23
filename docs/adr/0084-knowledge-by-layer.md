# 0084. knowledge/ by layer

Date: 2026-11-23
Status: Proposed, opened under the commit plan for knowledge/

## Context

The layers model is two drafts in `temp/common-ground/`: the general document, a Backbone Idea, and the Maintainer Repo's document, a Work Domain Idea of keeping knowledge. The second's header says its place in the repo is decided when today's Maintainer Repo is brought into it, after the change work (`TODO.md`, the item on the layers of knowledge).

The Change idea's split forced the question now. Its rules for each part go to Adapted Cases (`TODO.md`, the item "Split the Change idea"). Written in `temp/`, they would move twice.

Where each layer is kept is already the Maintainer Repo's document's to say: its row in its own table of Work Domain Ideas names "where each layer is kept" as what it adds (`temp/common-ground/knowledge-layers.md` §2.2.1, *Keeping knowledge*).

The first text drafted for layer 3, the Maintainer Repo's own Adapted Case for Defined Terms, named this repo's folders, its glossary and its ADRs: a text for this repo, not for any Maintainer Repo. The layers model put such texts at layer 3, "used in place", since no copy stands between them and the work (`temp/common-ground/knowledge-layers.md` §2.3.1, *Keeping knowledge*; §2.4, *The layer of a repo's work*). But the System Kit's Adapted Cases are written for every System Repo, and a Copy Change judged a System Repo's own stays at layer 4 (`temp/common-ground/knowledge-layers.md` §3.2.7, *The cases*). The general document left open whether layer 4 holds texts of its own, a question decision 5 answers. In it, layers 3 and 4 both hold understanding and instructions (§2, *The layers*).

Layer 3 was grouped like layer 2, by Work Domain (`temp/common-ground/knowledge-layers.md` §2.3, *The Adapted Case layer*). But the System Kit, copied whole to each System Repo, holds Adapted Cases of two Work Domains, designing a backend and keeping knowledge, for one kind of project. And "Adapted Case" had come to name two things: a text for every project of a kind, and a project's own text.

Layer 2 stayed grouped by Work Domain, so one layer-2 text served several kinds of project: "Defined Terms, in keeping knowledge" claimed every repo that keeps knowledge, the Maintainer Repo and each System Repo.

## Options considered

- **Stay in `temp/` until today's Maintainer Repo is brought in.** Rejected: the Change Adapted Cases would be drafted there and moved.
- **A folder per Work Domain, the layers inside.** Rejected: the path no longer says the layer, and layer 1 stands apart from the rest.
- **A folder per layer, numbered `1-` to `3-`.** Rejected: the numbers retell the order the general document holds, and its open question 1 may add a layer between 1 and 2, which would change every path.
- **Short file names,** such as `layers-in-the-maintainer-repo.md`. Rejected: the name would differ from the idea's row in the layers document's tables.
- **The layout as an idea of its own.** Rejected: it is where this repo keeps its layers, the Maintainer Repo's document's subject, and needed in no other Problem Domain.
- **A Paths Rule on `knowledge/**` to point at the layout.** Rejected: it loads only once a file there is read, too late for a session about to place a new idea elsewhere.
- **This repo's own Adapted Cases at layer 3, in `adapted-cases/keeping-knowledge/own/`,** used in place. Rejected: no copy between a text and its work does not make the text true for every project of its use.
- **Layer 4 with its instructions only,** their reasons in a *Decisions* footer and `.claude/decisions.md`. Rejected: layer 4 holds understanding and instructions, as layer 3 does.
- **A layer-4 folder in `knowledge/`.** Rejected: `knowledge/` holds what the Maintainer Repo keeps as knowledge, layers 1 to 3. Layer 4 is the work, done here through `.claude/`, where the agent loads what it acts on.
- **Layer 3 grouped by Work Domain, as layer 2.** Rejected: a kind of project draws on several Work Domains, and its set travels whole.
- **A new Name for a project's own text at layer 4, or for layer 3's.** Rejected: two Names for one form. The owner says the layer, as for any shared Name.
- **The System Kit apart from layer 3,** a delivery made from it. Rejected: two things for what is, in every part but one, the same set of texts.
- **Layer 2 by Work Domain, a sort of work, beside layer 3 by Problem Domain.** Rejected: one set of Adapted Cases would draw on ideas grouped another way, and one layer-2 text would serve several kinds of project.
- **"Keeping a concept" as the Maintainer Repo's Problem Domain.** Rejected: the model already names its problem keeping knowledge, and a System Repo's own knowledge keeping is part of CBC backend design.
- **Layer-2 titles by the repo,** "…, in the Maintainer Repo". Rejected: a title names its Problem Domain, as its folder does.

## Decision

1. **The layers model leaves `temp/` for a top folder, `knowledge/`, one folder per layer, for layers 1 to 3:** `backbone-ideas/`; `problem-domain-ideas/<Problem Domain>/`; `adapted-cases/<Problem Domain>/`, one set of Adapted Cases for each Problem Domain, such as the System Repos'. No folder name carries a number. A folder is made when its first file lands.
2. **A file is named after its idea, its title matching.** A layer-2 title is its layer-1 title, ", in" and its Problem Domain. The general document is `layers-of-knowledge.md`; the Maintainer Repo's is `layers-of-knowledge-in-keeping-knowledge.md`, "The layers of knowledge, in keeping knowledge".
3. **The model's place is decided before the change work,** so the Change Adapted Cases are written into their home.
4. **The layout and the rules for placing a text live in the Maintainer Repo's document's §2.** `CLAUDE.md` points every session at it, in one line.
5. **Layer 3 holds one set of Adapted Cases for each Problem Domain, a kind of project, true for every project of it; a project's own texts are layer 4.** With no Maintainer Kit, this repo's own Adapted Cases are layer 4, kept whole in `.claude/`: the Instruction Text where the agent loads it, and its understanding beside it in `.claude/understanding/`, which never loads. The two layers documents say so, and the general document's question 5 is answered.
6. **"Adapted Case" names the form:** a Problem Domain Idea written for one piece of work, as understanding with instructions. Its owner says its layer: a Problem Domain's Adapted Case is layer 3, a project's own is layer 4.
7. **The System Kit is the System Repos' set at layer 3,** and what is copied to each System Repo.
8. **Layer 2 is grouped by Problem Domain too, and Work Domain merges into it.** A layer-2 text is a Problem Domain Idea: a Backbone Idea adapted to one Problem Domain. Each Problem Domain writes its own adaptation; what is true for all goes up to layer 1. The Maintainer Repo's Problem Domain is keeping knowledge; the System Repos' is CBC backend design.

## Consequences

- The layers item's order, and the Maintainer Repo's document's header line on its place, change: the place is decided first.
- `ARCHITECTURE.md`'s codemap gains `knowledge/` and `.claude/understanding/`.
- `knowledge/adapted-cases/` stays unmade until the first Adapted Case for the System Repos is written.
- System Repo and System Kit name no Problem Domain. They are renamed after this plan (`TODO.md`, the item that renames them).
- A change to one of this repo's own Adapted Cases, either half, is a commit of the agent's files.
- If a Maintainer Kit is wanted, the part of this repo's own Adapted Cases true for every Maintainer Repo is set apart up to layer 3.
- Today's `docs/models/` and `docs/conventions/` stay until what they hold has landed in `knowledge/` (ADR-0082, decision 2). For that while, the repo's understanding stands in two places, the old texts and the new.
- The simulation, the flow file and the problem file stay in `temp/` as sources. Their pointers at the two documents are fixed when the documents move.
