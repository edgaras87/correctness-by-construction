---
foundation: the facts-in-sync convention
---

<!-- Makes the Change Walk, the disagreement and the grep for a moved name
     (docs/conventions/facts-in-sync/ §4, A Canonical Description's rule;
     §5, A disagreement; §3.3, The rename grep) fire at the commit;
     before, they had to be remembered. Loaded in every session, with no paths: an
     Agent Rule with paths: loads only when a file is touched with the agent's
     tools, and an edit made by script never loads it
     (docs/conventions/agent-arrangement/ §5.6, Rules files). Ours, shipped
     nowhere: a CBC Run holds no manuals. -->

# The Foundation Check

**Governs:** the moment before a commit is staged, when the commit
changes a file that stands on a foundation, or a foundation itself,
or moves a section. Which side is right, never how either reads.

## The check

1. **Look at the staged paths first.** Only these are checked:
   - files with a Foundation Line: `.claude/skills/`,
     `.claude/rules/`, `.claude/` under `delivery/`, and a manual
     that names its Idea Model;
   - records whose header comment carries a Foundation Line,
     in either Convention Seat (`docs/conventions/conventions/` §1.3, *The Foundation Line*);
   - Canonical Descriptions: `docs/models/`, `docs/conventions/*/README.md`,
     `concept/`.

   If none is staged, the check is done.
2. **A file with a Foundation Line changed:** open what the line
   names beside the change. For a convention, its manual,
   `docs/conventions/<name>/README.md`. For an Idea Model,
   `docs/models/<name>.md`. For `concept v1`, the chapters under
   `concept/`. Read the parts the change touches. A file names one
   `foundation`; a second is a Fact Reference to a part
   (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2).
3. **A Canonical Description changed:** run the Change Walk on what derives from it
   (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 3).
4. **List every disagreement before deciding any.** For each, show
   the reviewer what the foundation says, what the change says, and
   which side the agent thinks is wrong, and why. The reviewer
   decides each (`docs/conventions/facts-in-sync/` §5, *A disagreement*).
5. **The commit body names each ending,** one of four:
   - **the change is wrong:** it is brought back to the foundation;
   - **the foundation is wrong:** it changes;
   - **both change;**
   - **they agree:** one line names the foundation read.

   A change on the other side goes in the same commit, or in the
   next when one side is an agent file and the other is not
   (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).
6. **A foundation that changes is a Canonical Description changed.** Step 3
   runs on it again, and what it finds goes through steps 4 and 5.
   The check ends when a Change Walk finds nothing new. When the changes
   need more than one commit, they are a commit plan.

## A moved section

When the commit renames a file, renumbers or retitles a section, in
any file, or moves a fact to a new home, grep all Living Text for
each old path, number and title, and fix what points at them in
this commit (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*).

## What this does not cover

- **What a Canonical Description and its derived things are** —
  `docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*.
- **How a CBC Run's edit to its copy is taken** —
  `.claude/rules/working-a-reading.md`, step 4.
- **How a CBC Run edits a copy it holds** —
  `delivery/container/.claude/rules/delivered-copies.md`.

---

## Decisions

- `.claude/decisions.md`, 2026-10-17 — the check at the commit,
  loaded in every session; why not an Agent Rule with paths:, a `CLAUDE.md`
  line, or a hook now
- ADR-0065 — the check stands on the facts-in-sync manual
