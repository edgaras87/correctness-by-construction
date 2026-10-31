# Commit plan: round 3's work, layer 1

## Summary — the state after all commits

The conventions manual, `docs/conventions/conventions/README.md`,
Refinement Layer 1's one file, meets the writing rule. Its 21 fixed
findings, FINDING-282 to 289, 291 to 301, 303 and 304, are fixed as
round 3's endings took them, and each use of a word the four Names
tables named takes its Name (ADR-0078, decision 11). FINDING-290
and 302 stay declined. What the Foundation Check finds in the files
that stand on the manual is fixed beside it. The endings name each
fixed finding's commit.

## Commits

**1. `docs(agent): add commit plan for layer 1`**
This plan, once agreed.

**2. `docs: layer 1 meets the writing rule`**
The conventions manual: the 21 findings fixed, each as its proposal
or its decision says, read against the file as it stands now, since
the design's commits 4 and 5 already changed §1 and §1.1; its old
words given their Names from the tables, each use read by hand,
since some stay English. A Canonical Description changed, so the
Foundation Check walks what stands on it; the body names each
ending.

**3. `chore(agent): what layer 1 carries to our rules`**
What the walk finds in our agent files: at least
`.claude/rules/convention-manual.md`, whose line 36 holds FINDING-295's
"intent dressed as" and whose heading holds FINDING-294's "floor".
Dropped if the walk finds nothing.

**4. `fix(delivery): what layer 1 carries to shipped files`**
What the walk finds under `delivery/`. Dropped if it finds nothing.

**5. `docs(temp): layer 1's findings name their commits`**
The refinement's file: each of the 21 findings names the commit that
fixed it.

**6. `docs(agent): close commit plan for layer 1`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **One commit for the manual,** findings and Names together, so the
  file is opened once (ADR-0078, decision 11).
- **A finding whose text is gone is fixed by what replaced it,** or
  named as already fixed, with the design's commit.
