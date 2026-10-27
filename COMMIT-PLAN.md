# Commit plan: DECISION-13's change

## Summary — the state after all commits

The one-home rule's *Not a second home* names the two logs round 2
judged to be history (`temp/refinement-2026-10-18.md`, DECISION-13):
the entries of `.claude/decisions.md` and the parts of
`TODO-CONVERSATION-MEMORY.md`. Each file's header comment stays
living.

- **The home:** `docs/conventions/facts-in-sync/` §1 names both, the
  conversation memory as the deliverer's only.
- **Ours:** `.claude/rules/one-home.md` names both. The refinement's
  §1, which retells the list with a fact reference, follows.
- **What ships:** the run's `one-home.md` names its decisions log.
  A run keeps no conversation memory.
- The refinement's file says DECISION-13's change is made.

## Commits

**0. `docs(agent): add commit plan for DECISION-13`**
Opens the set.

**1. `docs: history names the decisions log and talks`**
Facts-in-sync §1's *History is not a second home* bullet, with a
dated italic for the widening. The refinement's file marks
DECISION-13 made.

**2. `chore(agent): our one-home rule names both logs`**
`.claude/rules/one-home.md`, *Not a second home*; the refinement's
§1, *living text*.

**3. `fix(delivery): the run's one-home rule is widened`**
`delivery/container/.claude/rules/one-home.md`, *Not a second home*.

**4. `docs(agent): close commit plan for DECISION-13`**
Deletes this file; the body says what diverged.

## Decisions for you to object to

- **Three commits, one per side.** The manual, our agent files and
  what ships never share a commit (`docs/conventions/commit-messages/`
  §2). The foundation check carries the change down in the next
  commit (`.claude/rules/foundation-check.md`, step 5).
- **The run's rule names only its decisions log.** The container
  has no `TODO-CONVERSATION-MEMORY.md`.
- **No line saying "a living line never takes an entry as a fact's
  home".** DECISION-13 noted it, but in a run it would clash with
  `delivered-copies.md` rule 1. That rule reads the pin from the
  decisions log's last delivery entry. The entry is still history:
  it records the take, and the next take adds a new entry rather
  than editing it.
- **The retrospective's "never history" lists stay.**
  `apply-retrospective` Stage 1 and the retrospective manual list
  what the apply step must not touch. They are their own lists, not
  tellings of this rule.
