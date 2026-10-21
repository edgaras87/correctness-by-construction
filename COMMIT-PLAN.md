# Commit plan: round 1's close read

The fixes from round 1's close read
(`.claude/approaches-on-trial/refinement.md` §2.8), FINDING-89 to
134, with the endings the agent proposed and the reviewer took on
2026-10-21. One plan for all layers, in their order: descriptions
first, then what derives from them.

## Summary — the state after all commits

Every line the close read found untrue is true again, and the eight
round 1 fixes that missed a place reach every place: a `paths:`
rule loads on a read wherever that is said; the deliverer's half of
the exchange is two skills and two rules; a person or the agent
stages; a TODO item's story goes to the devlog in both seats; every
pointer carries its path; the seed says container; the concept's
list in ARCHITECTURE holds only what derives from it. The
refinement's file records each ending, and round 1 closes.

## Commits

**1. `docs(agent): add commit plan for the close read`**
This file.

**2. `docs: the close read's fixes to the manuals`**
Layers 1 to 3, the descriptions: FINDING-89 in the conventions
manual and the exchange; 90, 92 to 96, 98 to 101, 103 and 104 (the
writing manual); FINDING-97 in agent-arrangement; FINDING-102 in the
shapes manual.

**3. `docs: the close read's fixes to the records`**
Layer 4: FINDING-89 and 97 in `TODO.md` and `PLAN.md`; FINDING-102
in `ARCHITECTURE.md`'s diagram; FINDING-105 to 115.

**4. `chore(agent): the close read's fixes to ours`**
Layer 5: FINDING-89 in `exchange-reading.md`; FINDING-104 in our
`writing.md`; FINDING-118 in `working-a-reading.md`; FINDING-119 to
123.

**4a. `docs: TODO holds what our changelog tracks`**
The reviewer's question at commit 3: the changelog's reader and
what it tracks. A TODO item in Later, its story in today's devlog
entry. With it, `TODO.md`'s pointer to `exchange-deliver`'s old §5,
which commit 4 renamed.

**5. `fix(delivery): the close read's fixes, shipped`**
Layer 6: FINDING-97 in the stack walkthrough; FINDING-118 in the
container's devlog stub and entry file; FINDING-127 to 129 and 131
to 134.

**6. `docs(temp): the close read's endings`**
Each of FINDING-89 to 134 gets its ending and commit; the counts of
the reviewer's take; round 1 closes, and round 2 is next.

**7. `docs(agent): close commit plan for the close read`**

## Decisions taken inside this plan

- **One plan, not one per layer:** the findings are few per layer,
  and the order of layers holds inside the plan.
- **Any rewrap is by hand,** or checked for structure as well as
  words.
- **A fix that changes a description walks it,** as in round 1;
  what follows on the other side of the agent line goes in the next
  commit.
