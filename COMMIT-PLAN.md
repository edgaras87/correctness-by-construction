# Commit plan: round 3's work, layer 3

## Summary — the state after all commits

Refinement Layer 3's 21 files meet the writing rule: the three Idea
Models, the concept's five chapters, the other ten manuals, the
hygiene templates, the conventions index and our glossary. Their 205
findings, FINDING-341 to 545, end as round 3's endings took them, and
each use of a word the four Names tables named takes its Name
(ADR-0078, decision 11). What the Foundation Check finds in the
files that stand on each, and what cites a retitled section, is
fixed beside it. The work names each fixed finding's commit.

## Commits

Each file commit fixes its findings and gives its old words their
Names, read against the file as it stands now, each use read by
hand. A Canonical Description changed, so the Foundation Check walks
what stands on it; a retitled section takes its rename grep, the
records and docs in the same commit. What the walk finds in our
agent files, or under `delivery/`, follows in the next commit, one
per side, dropped when the walk finds nothing.

**1. `docs(agent): add commit plan for layer 3`**
This plan, once agreed.

**The sources first: the Idea Models and the concept**

**2. `docs: the Agent Model meets the writing rule`**
`docs/models/agent.md`, 18 findings, FINDING-492 to 509; 492 to 494
span the three models, and land here and in 3 and 4.

**3. `docs: the Idea-to-Output Model meets the writing rule`**
`docs/models/idea-to-output.md`, 8 findings, FINDING-510 to 517.

**4. `docs: the Tiers Model meets the writing rule`**
`docs/models/tiers.md`, 12 findings, FINDING-518 to 529.

**5. `docs: the concept's chapters meet the writing rule`**
`concept/00` to `04`, 16 findings, FINDING-530 to 545, and the
concept's 23 Names in their text. An editorial change to the
concept: `CHANGELOG.md`'s *[Unreleased]* gains a *Fixed* line in the
same commit, since editorial fixes ride with the next version
(its standing comment, ADR-0003). The Method Group's copies under
`docs/concept/` follow at the next delivery.

**The manuals every other is read against**

**6. `docs: the writing manual meets the writing rule`**
`docs/conventions/writing/README.md`, 3 findings, FINDING-483 to 485.

**7. `docs: facts-in-sync meets the writing rule`**
`docs/conventions/facts-in-sync/README.md`, 21 findings, FINDING-414
to 434.

**The other manuals, in the index's order**

**8. `docs: agent-arrangement meets the writing rule`**
26 findings, FINDING-343 to 368.

**9. `docs: commit-messages meets the writing rule`**
12 findings, FINDING-369 to 380.

**10. `docs: commit-plan meets the writing rule`**
8 findings, FINDING-381 to 388.

**11. `docs: the exchange meets the writing rule`**
25 findings, FINDING-389 to 413.

**12. `docs: repo-hygiene meets the writing rule`**
The manual and its three templates, 9 findings, FINDING-435 to 443.

**13. `docs: retrospective meets the writing rule`**
13 findings, FINDING-444 to 456.

**14. `docs: shapes meets the writing rule`**
18 findings, FINDING-457 to 474.

**15. `docs: visual-comparison meets the writing rule`**
8 findings, FINDING-475 to 482.

**What points at the rest**

**16. `docs: the index and the glossary meet the writing rule`**
`docs/conventions/README.md`, 2 findings, FINDING-341 and 342;
`docs/glossary.md`, 6, FINDING-486 to 491.

**17. `docs(temp): layer 3's findings name their commits`**
The refinement's *The work*: layer 3's line.

**18. `docs(agent): close commit plan for layer 3`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **One commit per file,** or per family of small files, so each
  boundary shows one text whole.
- **The followers come right after the file they follow,** numbered
  as its sub-commits: 8a, 8b. They are not listed ahead, since only
  the walk finds them.
- **A follower changes only where the change reaches it.** Its own
  findings wait for its layer.
