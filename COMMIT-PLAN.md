# Commit plan: the chain, as a section of the conventions index

## Summary — the state after all commits

`docs/conventions/README.md` gains a section stating how the ten
conventions relate across a piece of work — what fires when, what
is standalone, what specialises what, and where the domain skills
supply the sequences the conventions deliberately do not. It holds
**relations only**: no rule that lives in a manual or a skill. Its
shape is settled by `visual-comparison` rather than chosen, which
is the fourth use that skill's own merge-back trigger has been
waiting for.

## Commits

**1. `docs(agent): add commit plan for the chain`**
This file.

**2. `docs(temp): the chain's shape, candidates compared`**
Requirements written before any candidate, then every candidate
built: a Mermaid picture, a table, a numbered list, and prose. The
non-picture rule applies — the set must hold something that is not
a drawing, or a drawing wins by construction.

**3. `docs(adr): the chain is a section, and its shape`**
ADR-0032, opening **Proposed**. Carries the requirements, the
candidates and why each lost, which is what lets step 5 delete the
draft. Also records the two decisions taken before the comparison:
that the map is a *guide* by `artifact-kinds` and does not ship,
and that it lands as a section rather than its own file.

**4. `docs(conventions): the chain, in the index`**
The section itself, in the shape step 3 settled.

**5. `docs(adr): accept 0032, and the records catch up`**
ADR-0032 flips; `decide-first`'s findings list gains its first
entry that is **not** marked retrospective, if the run produced
one; the two temp drafts go; devlog takes the session.

**6. `docs(agent): close the plan`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **A section, not a file, and the cost is accepted knowingly.**
  The map names the domain skills — `cbc-framing`, `cbc-bootstrap`,
  `cbc-slice`, `infra-establish`, `infra-serve` — because they
  supply the sequences `commit-plan` deliberately does not. Those
  are not conventions and do not live under `docs/conventions/`, so
  the index will hold a section about more than it indexes, and
  will grow by roughly half again. The user's call, made against
  that argument; recorded here so it is not rediscovered as a
  defect.

- **The shape is compared, not chosen**, though the work is small
  enough to justify either. Two reasons it is worth the two extra
  commits: `visual-comparison`'s merge-back trigger turns on
  whether a comparison whose winner is *not* a picture ever
  happens, and this is a candidate for exactly that; and
  `decide-first` has now run once for real, so its findings list
  can gain a first non-retrospective entry only if the run is
  written down.

- **`decide-first` ran before this plan and its draft is kept
  until the close.** `temp/deciding-the-map.md` holds the five
  questions and the count that was not sayable until Q1 was
  answered. It is evidence of the first live run of that skill, and
  step 5 is where it goes.
