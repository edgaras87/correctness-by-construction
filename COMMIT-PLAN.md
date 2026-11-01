# Commit plan: round 3's work, layer 4

## Summary — the state after all commits

Refinement Layer 4's files meet the writing rule: `ARCHITECTURE.md`,
`README.md`, `PLAN.md`, `TODO.md`, `CHANGELOG.md`, the header of
`TODO-CONVERSATION-MEMORY.md`, `devlog/README.md`,
`docs/adr/README.md` and `temp/README.md`. Their 58 findings,
FINDING-546 to 603, end as round 3's endings took them, and each use
of a word the four Names tables named takes its Name in their living
text (ADR-0078, decision 11). History keeps its words: closed Plan
Steps' lines, released changelog entries, the devlog's months and
the Conversation Memory's parts. What cites a retitled section is
fixed beside it. The work names each fixed finding's commit.

## Commits

Each file commit fixes its findings and gives its living text's old
words their Names, each use read by hand. A retitled section takes
its rename grep, the records and docs in the same commit; what the
grep finds in agent files or under `delivery/` follows in the next,
one per side, numbered as a sub-commit and dropped when nothing is
found.

**1. `docs(agent): add commit plan for layer 4`**
This plan, once agreed.

**2. `docs: ARCHITECTURE meets the writing rule`**
11 findings. Its gloss titles, §1.1 to §1.3 and §2.1 to §2.4, are
retitled under rule 10, as FINDING-341 asked at their home, with the
rename grep.

**3. `docs: README meets the writing rule`**
8 findings.

**4. `docs: PLAN meets the writing rule`**
8 findings, in the Plan Step Form and the open Plan Step; closed
Plan Steps' lines are history.

**5. `docs: TODO meets the writing rule`**
17 findings, and the old words of every open item.

**6. `docs: CHANGELOG meets the writing rule`**
5 findings, in its standing comment and *[Unreleased]*; released
entries are history.

**7. `docs: the smaller records meet the writing rule`**
`TODO-CONVERSATION-MEMORY.md`'s header, 2 findings;
`devlog/README.md`, 2; `docs/adr/README.md`, 1; `temp/README.md`, 3.

**8. `docs(temp): layer 4's findings name their commits`**
The refinement's *The work*: layer 4's line.

**9. `docs(agent): close commit plan for layer 4`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **One commit per record,** the four small ones together.
- **History keeps its words,** by writing rule *Where it applies*:
  only living text is rewritten.
