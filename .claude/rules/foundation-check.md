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

1. **A file with a `foundation` line changed** (a skill, a rule, a
   shape): open what the line names beside the change. For a
   convention, its manual, `docs/conventions/<name>/README.md`. For
   `concept v1`, the chapters under `concept/`. Read the parts the
   change touches.
2. **A description changed** (a manual, a concept chapter,
   `ARCHITECTURE.md`): walk what derives from it, its list and a
   grep for its path (`docs/conventions/conventions/` §3.5, step 3).
3. **Where the two disagree, show the reviewer both:** what the
   foundation says, what the change says, and which side the agent
   thinks is wrong, and why. The reviewer decides (§3.6).
4. **The commit body names the ending,** one of four:
   - **the change is wrong:** it is brought back to the foundation;
   - **the foundation is wrong:** it changes, and its walk runs
     again;
   - **both change;**
   - **they agree:** one line names the foundation read.

   A change on the other side goes in the same commit, or in the
   next when one side is an agent file and the other is not
   (`commit-messages`).

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
