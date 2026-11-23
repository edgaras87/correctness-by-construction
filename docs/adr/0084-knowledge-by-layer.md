# 0084. knowledge/ by layer

Date: 2026-11-23
Status: Proposed, opened under the commit plan for knowledge/

## Context

The layers model is two drafts in `temp/common-ground/`: the general document, a Backbone Idea, and the Maintainer Repo's document, a Work Domain Idea of keeping knowledge. The second's header says its place in the repo is decided when today's Maintainer Repo is brought into it, after the change work (`TODO.md`, the item on the layers of knowledge).

The Change idea's split forced the question now. Its rules for each part go to Adapted Cases (`TODO.md`, the item "Split the Change idea"). Written in `temp/`, they would move twice.

Where each layer is kept is already the Maintainer Repo's document's to say: its row in its own table of Work Domain Ideas names "where each layer is kept" as what it adds (`temp/common-ground/knowledge-layers.md` §2.2.1, *Keeping knowledge*).

## Options considered

- **Stay in `temp/` until today's Maintainer Repo is brought in.** Rejected: the Change Adapted Cases would be drafted there and moved.
- **A folder per Work Domain, the layers inside.** Rejected: the path no longer says the layer, and layer 1 stands apart from the rest.
- **A folder per layer, numbered `1-` to `3-`.** Rejected: the numbers retell the order the general document holds, and its open question 1 may add a layer between 1 and 2, which would change every path.
- **Short file names,** such as `layers-in-the-maintainer-repo.md`. Rejected: the name would differ from the idea's row in the layers document's tables.
- **The layout as an idea of its own.** Rejected: it is where this repo keeps its layers, the Maintainer Repo's document's subject, and needed in no other Work Domain.
- **A Paths Rule on `knowledge/**` to point at the layout.** Rejected: it loads only once a file there is read, too late for a session about to place a new idea elsewhere.

## Decision

1. **The layers model leaves `temp/` for a top folder, `knowledge/`, one folder per layer:** `backbone-ideas/`; `work-domain-ideas/<Work Domain>/`; `adapted-cases/<Work Domain>/`, split into `own/` and `system-repos/` for keeping knowledge. No folder name carries a number. A folder is made when its first file lands.
2. **A file is named after its idea, as the layers document's tables list it,** its title matching. The general document is `layers-of-knowledge.md`; the Maintainer Repo's is `layers-of-knowledge-in-the-maintainer-repo.md`.
3. **The model's place is decided before the change work,** so the Change Adapted Cases are written into their home.
4. **The layout and the rules for placing a text live in the Maintainer Repo's document's §2.** `CLAUDE.md` points every session at it, in one line.

## Consequences

- The layers item's order, and the Maintainer Repo's document's header line on its place, change: the place is decided first.
- `ARCHITECTURE.md`'s codemap gains `knowledge/`.
- Today's `docs/models/` and `docs/conventions/` stay until what they hold has landed in `knowledge/` (ADR-0082, decision 2). For that while, the repo's understanding stands in two places, the old texts and the new.
- The simulation, the flow file and the problem file stay in `temp/` as sources. Their pointers at the two documents are fixed when the documents move.
