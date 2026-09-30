# Commit plan: the index, and what it led to

## Summary — the state after all commits

`docs/conventions/README.md`, the index, points and does not
restate. It holds what only it can hold: the list of names, each
with its manual's path, and the chain. Which conventions ship is
ARCHITECTURE §2.3's, and what each is made usable as is its
manual's. Its chain names the commit-plan skill's §4 and §5,
which exist, instead of the manual's, which do not, and lists every
domain skill.

The conventions manual says what is true after ADR-0042 and
ADR-0044. Adding a convention asks for no registry entry and no
copy of a skill, only the deliverer's own derivation. It no longer
names a table in `delivery/README.md` that does not exist. And
"the master" in its lists of descriptions is ARCHITECTURE.
`delivery/README.md` counts the container's skills and rules as
they are.

For us, the index's table is the one home of the list of
conventions. The container's decisions-log stub keeps its own list
in the birth entry, because it ships, and a run cannot open our
index.

## Commits

**1. `docs(agent): add commit plan for the index`**
This plan.

**2. `docs(conventions): the index points`**
- The chain's "`commit-plan` §4 and §5" becomes the skill's
  sections, since the manual has only §1 and §2.
- The Artifacts column goes. It restated each manual's list, and
  project-recording's row had already drifted, naming the record
  stubs and not the playbook's steps or the records-table stake.
  Which conventions ship is ARCHITECTURE §2.3's already. A marker
  column in its place would restate §2.3 instead (the reviewer's
  question at this step).
- `infra-serve` joins the chain's domain skills.

**3. `docs(conventions): adding a convention, as it is`**
The conventions manual's §4 and two lists of descriptions:
- Step 3 names a "shipped-conventions table" in `delivery/README.md`
  that does not exist. What a convention entering or leaving the
  container updates is the index's table and the container stub's
  birth entry. And adding any convention also updates ARCHITECTURE:
  §1.2's count and summary, and §2.3's line on which convention
  owns which container file, and the codemap's "nine manuals". The
  map states those counts, and no step named it.
- Step 5 asks for a registry entry and, for a skill, the deliverer's
  own copy. Since ADR-0042 the deliverer's log keeps no registry,
  and its skills are derivations.
- "The master", twice, as a description, which the one-map set's
  sweep missed because it looked for the file name. It is
  ARCHITECTURE now.

**4. `docs: delivery/README counts the container`**
"The seven convention skills and the rules file" becomes what the
container ships: three skills and two rules.

**5. `docs: devlog carries the index`**
The session's entry. TODO gains `delivery/README.md`'s own reading
against ARCHITECTURE §2, which it may retell since the one-map set.
Its trigger is the next change to `delivery/`, or the birth that
writes `exchange-birth`, whichever comes first.

**6. `docs(agent): close commit plan for the index`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The index's table is our home for the list; the stub keeps its
  own.** I first proposed that `delivery/README.md` and the
  decisions stub point at the index. The stub cannot: it ships, and
  a shipped file cannot point into a repo its reader cannot open.
  `delivery/README.md` holds no such list.
- **No rule for directory READMEs.** The one lived failure, the
  index gathering rules, is answered by ADR-0032 and ADR-0039, and
  restating is §3.1's. The trigger is a second README drifting on its
  own.
- **`delivery/README.md`'s wider reading waits.** Only its wrong count
  is fixed here.
