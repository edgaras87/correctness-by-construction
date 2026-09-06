# Change-plan: fills beside the bundle

## Summary — the state after all commits

`starter/` has three directories with one rule each. `bundle/`
holds what the newborn keeps as pinned copies — the five skills;
`concept/` at the root ships the same way. `fills/` holds text the
seed writes into the kit's own files, which the newborn then owns
and edits freely: the playbook's steps into PLAN's STEPS region,
the CLAUDE body over the kit's entry stub, the README body over the
kit's README stub. `installs/` holds the manuals. ADR-0017 records
the split and amends ADR-0010's "nothing outside bundle/ ships";
the starter doc's copy table and the ARCHITECTURE codemap describe
it; every live path points at the new home. Nothing about delivery
changes: the pure seed still writes only the playbook's steps, and
both templates stay parked for the semi-pure install, which gets
its own ADR when it is designed.

## Commits

**1. `docs(adr): propose ADR-0017, fills beside the bundle`**
Decision-first — the split was decided in conversation
(2026-09-07): the bundle was never "what travels as a document"
(the playbook already went in as text), the real line is pinned
copy vs text that becomes the newborn's own. Lands Proposed,
flips in step 4.

**2. `refactor(starter): move the playbook and both templates to fills/`**
Three `git mv`s and every live reference in the same commit, so a
revert leaves nothing dangling: the pure seed manual's playbook
path, the starter doc's copy-table rows, the two baselines'
"continues at" pointers, CHANGELOG's Unreleased lines. Historical
ADR bodies and the devlog stay as written (ADR-0010's rule).

**3. `docs(starter): the starter doc and codemap describe fills/`**
The copy table gains a fills section stating the rule (written
into a kit file, the newborn's own from then on); the structural
sentence "nothing outside bundle/ ships" becomes the three-way
rule; the ARCHITECTURE codemap row for `starter/` names fills/.

**4. `docs: records catch up, ADR-0017 accepted`**
CHANGELOG Unreleased: the layout split. TODO: the three-way reading
item's rule revised to what already happened — birth templates
harvest at Step 0 readings (the README template did, 166bc7e); the
semi-pure item notes fills/ as the templates' home. ADR-0017 flips
to Accepted with the boundaries as evidence.

## Decisions taken inside this plan

- **The playbook moves too.** User's call, all three: a rule that
  is two-thirds true is not a rule. Cost: one path in pure-seed.md
  and two baseline pointers.
- **Layout only.** The semi-pure install (receipt branch, entry
  files overwritten, the contract paragraph's "no non-additive
  act") is a separate decision and waits for its own ADR; this set
  prepares the ground and claims nothing about delivery.
- **Name: `fills/`.** The word the repo already uses for text that
  goes into a kit file (the fill variables, the retired
  birth-fills). Not `templates/`: the skills' own `templates/`
  directories are copy-and-fill masters that land as new files,
  a different act.
- **The devlog is not a step.** It fires at session end, outside
  the set, as before.
