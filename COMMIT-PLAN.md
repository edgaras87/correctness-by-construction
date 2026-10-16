# Commit plan: the foundation check

## Summary — the state after all commits

This repo loads one more rule in every session,
`.claude/rules/foundation-check.md`. Before a commit that changes a
skill, rule, shape or concept chapter is staged, the manual or
chapter its `foundation` line names is opened beside it. Before a
commit that changes a manual is staged, what derives from it is
walked. The mismatch is decided one of four ways: the change is
wrong, the other side is wrong, both change, or they agree. The
commit body says which.

The rule makes `docs/conventions/conventions/` §3.5 and §3.6 fire
at the commit, where they waited to be remembered. The conventions
manual lists it among what it makes usable, and
`working-a-reading.md` step 4 points at it instead of retelling the
check. W12 of the reading of run 3 is done.

## Commits

D10 is marked settled in the reading's commit before this plan.

**1. `docs(agent): add commit plan for foundation rule`**
The approved plan.

**2. `chore(agent): check foundations before a commit`**
The rule, with no `paths:`; its entry in `.claude/decisions.md`,
with the options rejected: a paths rule, a `CLAUDE.md` line, a hook
now; and `working-a-reading.md` step 4 pointing at the rule. Agent
files only, so one commit.

**3. `docs: the conventions manual lists its check`**
The manual's *What this is made usable as* gains the rule, and
§3.6 a pointer: the disagreement is raised at every commit that
touches either side. Checked against itself by the rule just
landed, so its body says which ending it was.

**4. `docs(agent): close commit plan for foundation rule`**
Deletes this file; the body says what diverged.

After the close, the reading marks W12 done:
`docs(temp): the reading closes W12`.

## Decisions taken inside this plan

- **The rule before the manual.** The manual's list names the
  rule's path, so the rule must exist first; the rule's foundation,
  the conventions convention, exists already.
- **No ADR.** It is agent setup, recorded where `CLAUDE.md`'s table
  sends it: `.claude/decisions.md`, with the options rejected.
- **Ours only.** A run holds no manuals; how it edits its copies is
  `delivered-copies.md`.
