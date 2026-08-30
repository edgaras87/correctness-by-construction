# Change-plan: run birth delivery — kit first, CbC as overlay

## Summary — the state after all commits

The repo states, for the first time, how a run repo is born: a
numbered birth manual in the bundle doc — copy the handbook's starter
kit, then copy this repo's bundle onto it, then author the run's PLAN
from a playbook that now exists here — with the kit surface the
overlay assumes named explicitly. ADR-0009
records the delivery choice — CbC as an overlay on the kit — and
rejects the alternative of a pre-baked CbC stub kept here (a second
master of the kit's files; the projection law's two-masters argument
applied to the kit, plus a standing sync burden with no mechanism).
The playbook, `executions/cbc-run-playbook.md`, is harvested from the
two lived runs: checkout-system's PLAN gives the step sequence
(bootstrap → framing → ground → system bootstrap → slice waves →
release), safe-reservations' log gives the define phase between
framing and ground. The define-phase TODO item is resolved at the
sequence level; its skill-level half stays parked.

## Commits

**1. `docs(agent): add change-plan for birth delivery`**
The approved plan, committed before the work.

**2. `docs(adr): deliver cbc as overlay on the kit`**
ADR-0009: runs are born from the handbook's `starter/kit/`; CbC
arrives as a second copy on top (bundle doc's table + the playbook);
rejected: a pre-baked stub here (two masters diverge, handbook
updates would need mirroring), and delivery-as-edit-instructions
(the kit already has a native slot — `playbooks/`). Plus the PLAN
decision-index row. Its own step because it is the decision the rest
of the set executes.

**3. `docs(executions): add cbc-run playbook`**
The playbook in the kit's TEMPLATE.md shape, practice-born so pinned
"checked against concept v1" (ADR-0005), provenance naming both
lived sources. Rides with its bundle-table row and the one-line
ARCHITECTURE executions-component update — reverting the playbook
alone must not leave the table pointing at a missing file.

**4. `docs(executions): add birth manual to bundle doc`**
New section in `executions/README.md` — the birth manual: a numbered
sequence a person follows to start a CbC project on the stub (copy
the kit and fill its stubs → copy the bundle per the table → merge
the snippet into CLAUDE.md, delete the copy → copy the playbook to
`playbooks/`, then to PLAN.md, fill → begin at framing). It also
names the assumed kit surface explicitly — a CLAUDE.md to append to,
a `playbooks/` directory, the plan step/gate idiom — so a handbook
update is checked against a written list, not archaeology; anything
not on that list the overlay must not depend on. One line states the
record layering: records stay the kit's — CbC events are recorded as
ordinary project events under the kit's rules; the method's own
artifacts live under `docs/system/`, beside the records, not in
place of them. Supersedes the
existing "author an infrastructure step and a bootstrap step"
paragraph by pointing at the playbook. After step 3 so it never
references a file that does not exist yet.

**5. `docs: update TODO after birth delivery`**
The define-phase item rewritten: sequence-level landing done (the
playbook carries the step), the cbc-bootstrap skill addition still
parked with its original trigger (next time bootstrap gets touched).

**6. `docs: add devlog entry for birth delivery`**
Session record + Resume line.

**7. `docs(agent): close change-plan for birth delivery`**
Deletes this file; body records what diverged.

## Decisions taken inside this plan

- **Playbook home and name:** flat beside the snippet as
  `executions/cbc-run-playbook.md`, copied at birth to the run's
  `playbooks/cbc-run.md`; the run then follows the kit's own playbook
  usage (copy to PLAN.md, fill, delete inapplicable steps). Not a
  `playbooks/` directory here — one file does not earn one.
- **Slice waves are not hard-coded.** checkout's V1/V2/V3 grouping
  enters as a lived example in a warning/note, not as steps; the
  playbook's slice step defers ordering to the registry, re-decided
  at each close, matching the startup snippet's rule.
- **Define phase enters as a playbook step only.** safe-reservations
  lived it as a phase between framing and ground (log Entry 0001:
  name under a naming rule, repo name, remote description, each with
  verdicts) — that is the lived shape; folding it into cbc-bootstrap
  would be unlived speculation and the skill is not being touched.
- **Harvest sources, read-only:** checkout-system `PLAN.md`;
  safe-reservations `log.md` Entry 0001 and the node materials
  already checked 2026-08-30. Runs are never edited (ADR-0007).
- **checkout-system's plan predates the define phase** — the playbook
  records the merged sequence anyway, because both parts are lived,
  just in different runs; provenance says which run contributed what.
