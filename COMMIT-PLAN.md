# Commit plan: approaches on trial

A design change inside the refinement (`docs/conventions/refinement/`
§2.7), from round 1's DECISION-1.

## Summary — the state after all commits

Work never done before starts from an approach on trial: one file
at `.claude/approaches-on-trial/<work>.md`, the same in both seats.
It is drafted for the work at hand, corrected as the work goes,
and evaluated at the work's close. Each piece is placed, kept on
trial and rewritten in general, left as the project's own, or
dropped. A piece used again gets a dated note, and each use is
evaluated again, until the approach is placed into conventions or
dropped.

Two approaches on trial hold this way of working:

- `approach-drafting.md`, both seats, shipped: how a new approach
  is drafted and handed over. It replaces the first-time-work
  convention: its manual and both skills go.
- `approach-evaluation.md`, ours only: how an approach is judged
  and placed, in its three situations. It holds the core ideas:
  the stages, the split by seat, placing per piece.

A step finds its approach in its skills and rules, then in the
approaches on trial, and drafts one if neither covers it.
Approaches ship to runs as pinned copies; a run's note of a use
comes back as an edit to its copy. The refinement's own manual
becomes `.claude/approaches-on-trial/refinement.md`. DECISION-1
and DECISION-4 end, with the first-time-work findings.

## Commits

**1. `docs(agent): add commit plan for approaches`**
This file.

**2. `docs(adr): ADR-0058 approaches on trial, proposed`**
The decisions and the ways rejected: a draft in `temp/`, "draft"
and "ways" as names, one file per seat, a polished manual, shipping
later, the ability written into every step form. It supersedes
ADR-0056's provisional manual and one lasting form, and amends
ADR-0057's opening item. Decision-first: settled in conversation.

**3. `chore(agent): approach-drafting replaces our skill`**
`.claude/approaches-on-trial/approach-drafting.md`, rewritten in
general from the manual and both skills by the stays/goes/changes
list; the run's close marked inline. Our first-time-work skill
goes. A `.claude/decisions.md` entry. Agent files only.

**3b. `chore(agent): approach-drafting points, not retells`**
Three lines of commit 3 retold what other files own: the step
form's Notes and gate, what the pin covers, and the agent and
project split. Each becomes a pointer, as one-home rule 2 asks.

**3c. `docs: TODO holds tagged retelling for round 2`**
The reviewer's idea, met in 3b: a retelling that names its source,
kept true by a walk from it. A doubt on one-home rule 2, due before
round 2 reads against it.

**4. `chore(agent): approach-evaluation, on trial`**
`.claude/approaches-on-trial/approach-evaluation.md`: its steps,
its three situations, the stages, the split by seat, ideas living
where acted on, self-judging and the reviewer's check, and what is
not known yet (whether a manual still goes on trial; retiring
"stages from earlier work").

**5. `docs: first-time-work leaves the conventions`**
Its manual goes. What pointed at it follows: the index's chain and
line; `ARCHITECTURE.md` §1.2's count and phrase, §2.3's line, the
codemap, and *The words* gaining "approach" and "approach on
trial"; conventions §4, where a convention now comes from an
evaluation; agent-arrangement §3.1, its run seat, and a new §3.8
for `approaches-on-trial/`. Foundation check on each description.

**6. `docs: a step's approach may be on trial`**
Both step forms, ours and the playbook's: the opening item checks
skills and rules, then approaches on trial, then drafts one; the
heading names "the skills, rules and approaches it uses"; a closing
item when an approach on trial was used.

**7. `feat(delivery): approaches on trial ship to runs`**
The container gains `.claude/approaches-on-trial/approach-drafting.md`,
identical to ours, and loses its first-time-work skill. The pin
covers approaches: exchange §3.2 and §5, `delivered-copies.md`
rules 1 and 2, the entry file's pinned list, the decisions stub's
birth entry, `delivery/README.md`.

**8. `chore(agent): the exchange skills carry approaches`**
`exchange-deliver` step 2.2 and `exchange-read`'s held copies take
`.claude/approaches-on-trial/`. Agent side of commit 7.

**9. `chore(agent): the refinement's approach moves in`**
*Provisional.* `.claude/approaches-on-trial/refinement.md`, from
the refinement's manual, with only the lines the move makes untrue
changed. Its reshaping waits for its evaluation.

**10. `docs: the refinement's manual goes`**
*Provisional.* The manual is deleted; every pointer to
`docs/conventions/refinement/` moves to the approach, in `PLAN.md`,
`TODO.md` and the refinement's file.

**11. `docs: the refinement step names its approach`**
*Provisional.* The step's heading, its opening and closing gate
items and Notes name `approach-drafting`, the refinement's
approach and its evaluation, in place of first-time-work.

**12. `docs: TODO follows the approaches`**
*Provisional.* The items this answers or changes: the rule that
writes a skill or rule from its convention, run 5's birth line,
delivering a rule on trial.

**13. `docs(temp): round 1 ends what the design settled`**
DECISION-1 and DECISION-4, and FINDING-2, 25, 26, 27, 49 and 50,
each with its ending and commit.

**14. `docs: ADR-0058 accepted; devlog names the change`**
The final records commit: the ADR flips, and the devlog entry
names the design change.

**15. `docs(agent): close commit plan for approaches`**

## Decisions taken inside this plan

- **Agent and project apart.** The approaches are agent files, so
  each lands in its own commit, and the project side follows in
  the next (`docs/conventions/conventions/` §3.5, step 3). Between
  3 and 5 the manual names a skill already gone, for one commit.
- **Agent-arrangement's new place is §3.8,** not §3.4: inserting
  it among the places would renumber four sections and their
  pointers for order alone.
- **The refinement's approach moves as it is.** Reshaping it into
  an approach's form is its own evaluation's work, at the
  refinement's close.
- **The seed is not touched:** a birth copies the container whole,
  so the folder arrives with it.
- **Round 1's other findings in these files are not fixed here,**
  even where a commit touches the same lines: FINDING-12, 20 and
  74 among them. They wait for round 1's work.
