# Commit plan: the eval's group 1, what reaches a run

## Summary — the state after all commits

What a run receives says only what is true for a run.

- **An update carries copies only.** The exchange's §3.2 says what
  goes: at birth the whole container, at an update only its copies
  — the container's skills and rules, the method, the stack, the
  concept. The records never travel again (§2.4). `exchange-deliver`
  diffs and stages exactly that, so a delivery can no longer land
  stubs over a run's filled records (F1).
- **What every delivery re-sends is true in a run.**
  `visual-comparison` speaks to either seat: a project that holds to
  plain text, the deliverer's Mermaid trial that does not travel
  (F3). Its citation of a deleted model goes (F8, part).
  `delivered-copies.md` says the entry file arrives composed (F9).
  Our own `visual-comparison` stays byte-identical to the
  container's.
- **What only a birth sees is true in a run.** The PLAN
  retrospective keeps a run's lessons in its own retrospective,
  where the deliverer reads them (F2). The entry file names what was
  delivered, not whole directories (F4), and the decisions row
  drops "with versions" (F5). The stubs name nothing a run cannot
  resolve (F8, the rest).
- **The seed speaks the run's words.** Its subjects and prompt drop
  "bundle", "kit remainder", "container half" and "groups" (F11),
  and its comment counts two method skills (F10).

F6, the concept headers, is held by the TODO item "Split a shipped
file's header between its two readers", due at the next birth. F7,
run history inside the method skills, moves to group 2's set, which
edits the same files. The list says both.

## Commits

**1. `docs(agent): add commit plan for group 1`**
This plan.

**2. `docs(conventions): an update carries copies only`**
The exchange's §3.2, "What goes": the whole container at birth,
only its copies after, with §2.4 as the reason.

**3. `fix(agent): exchange-deliver stages copies only`**
§1.1's diff and §2.2's overlay name the container's
`.claude/skills/` and `.claude/rules/`, not the whole group. An agent
file, a commit of its own.

**4. `fix(delivery): what every delivery re-sends`**
The container's `visual-comparison` (F3, F8's citation) and
`delivered-copies.md` (F9).

**5. `chore(agent): visual-comparison, seat-neutral`**
Our copy follows, byte-identical.

**6. `fix(delivery): what only a birth sees`**
The container's `PLAN.md` (F2, F8), `.claude/CLAUDE.md` (F4, F5, F8)
and `devlog/devlog.md` (F8).

**7. `fix(installs): the seed speaks the run's words`**
`delivery/installs/pure-seed.md`: the seed subjects and the prompt
(F11), the step 4 comment (F10), and the checklist lines that quote
the subjects.

**8. `docs: records carry group 1`**
The eval's list marks F1–F5 and F8–F11 done with their commits, F6
held by its TODO item, F7 moved to group 2. CHANGELOG gains a Fixed
line for what a run now receives. TODO's "Read run 3 and deliver"
is due now. The devlog's entry.

**9. `docs(agent): close commit plan for group 1`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The rule before the script.** §3.2 says what an update carries
  before `exchange-deliver` does it, so the skill follows its
  manual.
- **Seat-neutral words, not a split.** `visual-comparison` is
  byte-identical in both seats, and whether it stays so is the
  eval's D1. Words true in both seats fix F3 without deciding D1.
- **F6 and F7 are not in this set.** F6 has an item already; F7
  would double this set's size in files group 2 opens anyway, and
  run 3 already holds those texts, so a delivery makes nothing
  worse.
- **CHANGELOG gets one line**, not a rewrite. Its [Unreleased] is
  the eval's F48, group 5's.
