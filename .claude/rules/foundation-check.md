---
foundation: the conventions convention
---

<!-- Makes docs/conventions/conventions/ §3.5 and §3.6 fire at the
     commit, where they waited to be remembered. Loaded in every
     session, with no paths: a paths rule loads only when a file is
     opened with the Read tool, and an edit made by script never
     opens it. Ours, shipped nowhere: a run holds no manuals. -->

# The foundation check

**Governs:** the moment before a commit is staged, when the commit
changes a file that stands on a foundation, or a foundation itself.
Which side is right, never how either reads.

## The check

1. **Look at the staged paths first.** Only these are checked:
   - files with a `foundation` line: `.claude/skills/`,
     `.claude/rules/`, and `.claude/` under `delivery/`;
   - descriptions: `docs/conventions/*/README.md`, `concept/`,
     `ARCHITECTURE.md`.

   If none is staged, the check is done.
2. **A file with a `foundation` line changed:** open what the line
   names beside the change. For a convention, its manual,
   `docs/conventions/<name>/README.md`. For `concept v1`, the
   chapters under `concept/`. Read the parts the change touches.
3. **A description changed:** walk what derives from it, as
   `docs/conventions/conventions/` §3.5 step 3 says.
4. **List every disagreement before deciding any.** For each, show
   the reviewer what the foundation says, what the change says, and
   which side the agent thinks is wrong, and why. The reviewer
   decides each (§3.6).
5. **The commit body names each ending,** one of four:
   - **the change is wrong:** it is brought back to the foundation;
   - **the foundation is wrong:** it changes;
   - **both change;**
   - **they agree:** one line names the foundation read.

   A change on the other side goes in the same commit, or in the
   next when one side is an agent file and the other is not
   (`commit-messages`).
6. **A foundation that changes is a description changed.** Step 3
   runs on it again, and what it finds goes through steps 4 and 5.
   The check ends when a walk finds nothing new. When the changes
   need more than one commit, they are a commit plan.

## What this does not cover

- **What a description and its derived things are** —
  `docs/conventions/conventions/` §3.5.
- **How a run's edit to its copy is taken** —
  `.claude/rules/working-a-reading.md`, step 4.
- **How a run edits a copy it holds** —
  `delivery/container/.claude/rules/delivered-copies.md`.

---

## Decisions

- `.claude/decisions.md`, 2026-10-17 — the check at the commit,
  loaded in every session; why not a paths rule, a `CLAUDE.md`
  line, or a hook now
