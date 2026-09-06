# Change-plan: the seed lands on a receipt branch

## Summary — the state after all commits

The pure seed delivers on a branch, `birth-seed`, cut from the
kit's hygiene commit: five commits, pins in the subjects, never
merged. Main stays at the hygiene root with the same files in its
worktree, untracked — the agent commits them itself, under its own
split and sequence, which is the assembly judgment the experiment
says it measures and which a seed on main had already taken away.
The firing prompt gains one line naming the branch as where the
pins live. ADR-0018 records the shape and amends the manual's
"five commits on main, no other branch"; the manual, the starter
doc, CHANGELOG and the two experiment items carry it. Runs 1 and
2 stay the old shape as history. The semi-pure delta — one more
commit on the branch, the two fills over the kit's stubs — is not
in this set; it gets its own ADR on this ground.

## Commits

**1. `docs(adr): propose ADR-0018, the seed lands on a receipt branch`**
Decision-first — decided in conversation (2026-09-07). Context:
the pure experiment's measured object is the commit sequence the
agent chooses, and a seed on main leaves it nothing to choose;
run 2's known issue (the straddling kit commit); newborn-v1's
receipt branch as the lived precedent. Options: seed on main as
today; a single squash on main; the branch with main's worktree
untracked — taken. Lands Proposed, flips in step 4.

**2. `feat(installs): the seed commits on birth-seed, main holds it untracked`**
pure-seed.md: the opening paragraph, step 3 (branch cut first),
a new step for returning to main and restoring the worktree
untracked, the prompt's branch line, the checkable-seed list
(five on the branch, main at the hygiene root, worktree identical
to the branch tip, everything delivered showing untracked), and
the reader's checklist (the deliveries committed under the agent's
own split). Material-first for the restore mechanism: the exact
git commands are proven on a scratch repo at this boundary before
the manual states them. Header gains its seventh revision line.

**3. `docs(starter): the starter doc carries the branch shape`**
starter/README.md's birth-procedure sentence ("every delivery a
commit on main") and ARCHITECTURE's installs sentence if it says
the same.

**4. `docs: records catch up, ADR-0018 accepted`**
CHANGELOG Unreleased; TODO — the pure-seed item's variant-B note
(seed commits on main) superseded with a dated line, the gates
item told that the next pure run differs from run 2 in branch
shape; ADR-0018 flips to Accepted.

## Decisions taken inside this plan

- **Branch name `birth-seed`,** newborn-v1's, so the two
  histories read the same way across generations: the branch is
  what arrived, main is how it was understood.
- **Untracked on main, not a squash.** A squash keeps the seed in
  main's log as one straddling commit and still leaves the agent
  no sequence to choose. Untracked is the only shape where the
  first commit on main after hygiene is the agent's.
- **The pins reach the agent through the prompt,** one line: the
  seed arrived on branch birth-seed, pins in its subjects, main's
  worktree holds the same files untracked. Nothing is written into
  main for it. The prompt is the session channel; a branch is
  session-shaped truth (deletable, never merged).
- **Runs 1 and 2 are not reseeded.** They stay the old shape;
  every reading against them says so.
- **Semi-pure stays out.** This set makes the ground the same for
  both installs; the templates commit is the next ADR's.
