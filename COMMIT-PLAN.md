# Commit plan: the fact reference's homes

## Summary — the state after all commits

The seven decisions of 2026-10-27 on how a fact reference is written
(`TODO.md`, "Write down how a fact reference is written, then
rewrite each one to it"; `TODO-CONVERSATION-MEMORY.md` §13) stand in
an ADR and in their homes. The rewrite of the existing references is
the item's second part, and not this plan's.

- **The ADR:** ADR-0070 records the seven decisions, what each
  rejected, and decision 6's trigger.
- **The home, facts-in-sync:**
  - §3.1 gives the form: (`<path>` §<number>, *<title>*), always in
    parentheses, with its cases; "pointer" as the agent model's
    wider word; a skill's own files by root path; a shipped line
    that never sends a run into our manual;
  - §1: a fact stated only in history gets a living home first;
  - §3.3: the grep also covers a retitled section and a moved fact;
  - §4 step 2: a fact reference re-reads its line, the `foundation`
    line re-reads the whole file;
  - the deliverer's seat: each new or changed line is asked at the
    commit;
  - the run's seat: a run may retell beside an id.
- **Its followers:** the glossary's *fact reference*; commit-plan
  §2.10; our `one-home.md`, `foundation-check.md` and `commit-plan`
  skill; the run's `one-home.md` and `commit-plan` skill.
- **Two facts stated only in history get a home:** the method's
  no-stack rule in exchange §3.4; the off-template rule in one skill,
  stated whole, the other three pointing.
- TODO's item keeps only the rewrite.

New and changed lines take the settled form. Lines a commit does not
otherwise touch keep today's form until the rewrite.

## Commits

**0. `docs(agent): add commit plan for reference homes`**
Opens the set.

**1. `docs: ADR-0070 how a fact reference is written`**
Proposed. The seven decisions, the rejected options, the trigger.

**2. `docs: facts-in-sync writes the settled reference`**
§1, §3.1, §3.3, §4 step 2 and both seats, as the summary lists.

**3. `docs: the reference's followers take the form`**
The glossary's *fact reference*; commit-plan §2.10, whose sweep
greps titles and moved facts too.

**4. `docs: exchange §3.4 states the no-stack rule`**
"Nothing that needs Spring, PostgreSQL, Maven or podman sits under
`method/`", from ADR-0029. `ARCHITECTURE.md` §3's row already cites
§3.4, and is re-read.

**5. `chore(agent): our rules take the settled reference`**
`.claude/rules/one-home.md`: rule 2's form, rule 4's wider grep, the
check at the commit. `.claude/rules/foundation-check.md`, *A moved
section*. Our `commit-plan` skill's sweep.

**6. `fix(delivery): a run may retell beside an id`**
The run's `one-home.md`, rules 2 and 4; the container's
`commit-plan` skill's sweep.

**7. `fix(delivery): the off-template rule has one home`**
One skill states it whole: derive from the outcomes or the model,
record the deviation in the run's log, expect a harvest, never bend
a decided constraint to fit a template. The other three point at it.

**8. `docs: ADR-0070 is accepted, TODO keeps the rewrite`**
ADR-0070's status; TODO's item says its first part is done.

**9. `docs(agent): close commit plan for reference homes`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A commit
that changes a description walks what stands on it; a derived file
that then disagrees gets a lettered commit after it.

## Decisions for you to object to

- **Homes first, rewrite later.** This plan writes the rule where
  it lives, and its followers. The 329 references, 129 sentences, 34
  uses of "pointer" and 41 skill paths are the rewrite's, a plan of
  their own, so each diff here stays readable.
- **New lines in the new form now.** A line this plan writes takes
  the settled form; the lines around it wait for the rewrite.
- **The off-template rule's home is chosen at commit 7's boundary,**
  with the four files read whole. The likely home is `cbc-framing`'s
  `SKILL.md`: the first skill a run uses, and in the method group, so
  the stack's walkthroughs may point at it. The method never points
  at the stack.
- **The check at the commit goes in our `one-home.md`,** not in
  `foundation-check.md`. The check asks of every staged line, while
  the foundation check runs only on files with a foundation.
- **ADR-0070 opens Proposed** and is accepted at commit 8, as
  ADR-0069 was.
