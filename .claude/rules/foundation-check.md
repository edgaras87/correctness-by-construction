---
foundation: the facts-in-sync convention
---

<!-- Makes docs/conventions/facts-in-sync/ §4 and §5, and §3.3's
     grep for a moved section, fire at the commit, where they waited
     to be remembered. Loaded in every session, with no paths: a
     paths rule loads only when a file is touched with the agent's
     tools, and an edit made by script never loads it
     (docs/conventions/agent-arrangement/ §5.6). Ours, shipped
     nowhere: a run holds no manuals. -->

# The foundation check

**Governs:** the moment before a commit is staged, when the commit
changes a file that stands on a foundation, or a foundation itself,
or moves a section. Which side is right, never how either reads.

## The check

1. **Look at the staged paths first.** Only these are checked:
   - files with a `foundation` line: `.claude/skills/`,
     `.claude/rules/`, `.claude/` under `delivery/`, and a manual
     that names its model;
   - records whose header comment carries a `foundation:` line,
     in either seat (`docs/conventions/conventions/` §1.3);
   - descriptions: `docs/models/`, `docs/conventions/*/README.md`,
     `concept/`, `ARCHITECTURE.md`.

   If none is staged, the check is done.
2. **A file with a `foundation` line changed:** open what the line
   names beside the change. For a convention, its manual,
   `docs/conventions/<name>/README.md`. For a model,
   `docs/models/<name>.md`. For `concept v1`, the chapters under
   `concept/`. Read the parts the change touches. A file names one
   `foundation`; a second is a fact reference to a part
   (`docs/conventions/facts-in-sync/` §4, step 2).
3. **A description changed:** walk what derives from it, as
   `docs/conventions/facts-in-sync/` §4 step 3 says.
4. **List every disagreement before deciding any.** For each, show
   the reviewer what the foundation says, what the change says, and
   which side the agent thinks is wrong, and why. The reviewer
   decides each (`docs/conventions/facts-in-sync/` §5).
5. **The commit body names each ending,** one of four:
   - **the change is wrong:** it is brought back to the foundation;
   - **the foundation is wrong:** it changes;
   - **both change;**
   - **they agree:** one line names the foundation read.

   A change on the other side goes in the same commit, or in the
   next when one side is an agent file and the other is not
   (`docs/conventions/commit-messages/` §2).
6. **A foundation that changes is a description changed.** Step 3
   runs on it again, and what it finds goes through steps 4 and 5.
   The check ends when a walk finds nothing new. When the changes
   need more than one commit, they are a commit plan.

## A moved section

When the commit renames a file or renumbers a section, in any
file, grep all living text for each old path and number, and fix
what points at them in this commit
(`docs/conventions/facts-in-sync/` §3.3).

## What this does not cover

- **What a description and its derived things are** —
  `docs/conventions/facts-in-sync/` §4.
- **How a run's edit to its copy is taken** —
  `.claude/rules/working-a-reading.md`, step 4.
- **How a run edits a copy it holds** —
  `delivery/container/.claude/rules/delivered-copies.md`.

---

## Decisions

- `.claude/decisions.md`, 2026-10-17 — the check at the commit,
  loaded in every session; why not a paths rule, a `CLAUDE.md`
  line, or a hook now
- ADR-0065 — the check stands on facts-in-sync
