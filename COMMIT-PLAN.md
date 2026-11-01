# Commit plan: round 3's work, layer 5

## Summary — the state after all commits

Refinement Layer 5's files, our agent setup, meet the writing rule:
`CLAUDE.md`, `CLAUDE.local.md`, the six Agent Rules, the five Agent
Skills, the five Approaches on Trial and the header of
`.claude/decisions.md`. Their 69 findings, FINDING-604 to 672, end as
round 3's endings took them, and each use of a word the four Names
tables named takes its Name in their living text (ADR-0078, decision
11). The Decisions Log's entries are history and keep their words.
Where a finding names the container's copy beside ours, the
container's is fixed in the next commit. The work names each fixed
finding's commit.

## Commits

Each commit fixes its files' findings and gives their old words
their Names, each use read by hand, a scripted pass only for the
Names that map one to one, checked by structure counts and a second
run. A file with a Foundation Line goes through the Foundation Check
against its manual. A retitled section takes its rename grep. What a
commit reaches under `delivery/` follows in the next, as a
sub-commit, dropped when nothing is found.

**1. `docs(agent): add commit plan for layer 5`**
This plan, once agreed.

**2. `chore(agent): the Entry File meets the writing rule`**
`CLAUDE.md`, 3 findings; `CLAUDE.local.md`, 1, shown to the reviewer
line by line, since it is the operator's own file.

**3. `chore(agent): our Agent Rules meet the writing rule`**
The six under `.claude/rules/`, 13 findings.

**4. `chore(agent): our Agent Skills meet the writing rule`**
The five under `.claude/skills/`, 20 findings, the two the
container's copies share among them.

**5. `chore(agent): our Approaches on Trial meet the writing rule`**
The five under `.claude/approaches-on-trial/`, 23 findings.

**6. `chore(agent): the Decisions Log's header meets the rule`**
`.claude/decisions.md`'s header, 3 findings; its entries are history.

**7. `docs(temp): layer 5's findings name their commits`**
The refinement's *The work*: layer 5's line.

**8. `docs(agent): close commit plan for layer 5`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **One commit per kind of agent file,** since each kind loads at
  its own moment and is read as one set.
- **`CLAUDE.local.md` is changed only as the reviewer approves,**
  line by line: it holds the operator's settings.
