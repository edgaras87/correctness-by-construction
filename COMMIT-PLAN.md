# Commit plan: when a bold lead is a part

## Summary — the state after all commits

`docs/conventions/facts-in-sync/` §3.2 says when a bold-led bullet
is a part, as the refinement's DECISION-15 chose: when it holds a
paragraph of its own, with its own reason or dated case. A short
list item is not. TODO's "Write when a bold lead is a part" is
worked, and leaves TODO.

- **The rule:** facts-in-sync §3.2, and our `convention-manual.md`,
  which retells it.
- **FINDING-252, worked:** commit-messages §2 and visual-comparison
  §2 number their bold-led bullets as parts, `### 2.1` to `### 2.4`.
  Commit-messages §3's bullets are short list items, and stay.
- **The 15 references to commit-messages §2** name the part they
  mean: 8 its §2.3, the agent's files apart; 7 its §2.4, commit on
  the word. They take the settled form, since each line changes.
  No reference names visual-comparison §2.
- The 16 other sections DECISION-15 named are judged against the
  rule at the refinement's last read, not here.

## Commits

**0. `docs(agent): add commit plan for bold-lead parts`**
Opens the set.

**1. `docs: facts-in-sync says when bold leads are parts`**
The rule, with a dated italic for its case: commit-plan §2,
numbered in `79bc4a2`.

**2. `chore(agent): the manual rule follows §3.2`**
`.claude/rules/convention-manual.md`, its body item.

**3. `docs: two manuals number their bold-led parts`**
Commit-messages §2 and visual-comparison §2. In the same commit,
the 10 project-side references to commit-messages §2 name their
part: `ARCHITECTURE.md`, `PLAN.md` twice, `TODO.md`, commit-plan
four times, facts-in-sync §4 (`docs/conventions/facts-in-sync/`
§3.3, *A rename is grepped at its commit*).

**4. `chore(agent): our references name the part`**
The 5 references in our agent files: `foundation-check.md`,
`working-a-reading.md` twice, the `commit-plan` skill twice.

**5. `docs: TODO's bold-lead item is worked`**
The item leaves TODO.

**6. `docs(agent): close commit plan for bold-lead parts`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A commit
that changes a description walks what stands on it; a derived file
that then disagrees gets a lettered commit after it.

## Decisions for you to object to

- **Visual-comparison §2's closing italic moves above its parts.**
  "Settled 2026-09-24…" is about the whole method, not the fourth
  bullet; under `### 2.4` it would read as that part's lesson.
- **The parts' titles are their bold leads, cut where long:**
  commit-messages 2.1 *Conventional Commits, not just 50/72*, 2.2
  *Either mood, in the present tense*, 2.3 *The agent's files never
  share a commit*, 2.4 *Commit on the word*; visual-comparison 2.1
  *One candidate is not a picture*, 2.2 *The render decides*, 2.3
  *Fighting a notation is losing*, 2.4 *The buildable notations are
  few*. Each bullet's text loses its bold lead to the heading, and
  keeps the rest word for word.
- **No skill changes.** Neither `commit-messages` skill nor either
  `visual-comparison` skill points at §2.
