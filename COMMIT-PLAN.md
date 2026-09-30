# Commit plan: the index, and what it led to

## Summary — the state after all commits

`docs/conventions/README.md`, the index, is the home of the chain
and of nothing else: how the conventions relate across a piece of
work. It is what the reviewer called a small architecture at step
5's boundary, a local map, though the word waits for a pair before
it is written down. It carries no list, no count and no description.
The folder shows the names, ARCHITECTURE §1.2 says what they are and
how many, and each manual says what it is and ships. Its chain names
the commit-plan skill's §4 and §5, which exist, instead of the
manual's, which do not, and lists every domain skill.

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

**6. `docs(conventions): the index is the chain`**
The reviewer's question at step 5's boundary: what does "the nine"
give? Names and paths, which the folder already shows. "The nine"
goes. The opening says the README is where the conventions' chain
lives, and points to ARCHITECTURE §1.2 for the list. The last
paragraph loses its count and names: "the remaining six …" becomes
"the other conventions", so that adding one changes nothing here
unless it joins the chain.

**7. `docs: the index's pointers follow`**
- The conventions manual lists the index as "the table and the
  chain"; it becomes "the chain".
- §4 step 4, "A row in the index's table", goes: a new convention
  touches the index only when it takes part in the chain.
- ARCHITECTURE §1.2's "The nine, and how they relate" becomes "How
  they relate".
- The codemap's "nine manuals and their index" keeps its count,
  which is the map's, and calls the index what it holds.

**8. `docs: records carry the index's second pass`**
The session's devlog entry gains the second pass. TODO's
`delivery/README.md` item gains the idea: a local map, like the
conventions index. If its reading lands that way, the pair is
there, and "local map" and its rule go into project-recording §8
and ARCHITECTURE's words.

**9. `docs(agent): close commit plan for the index`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The index's table is our home for the list; the stub keeps its
  own.** I first proposed that `delivery/README.md` and the
  decisions stub point at the index. The stub cannot: it ships, and
  a shipped file cannot point into a repo its reader cannot open.
  `delivery/README.md` holds no such list.
- **No rule for directory READMEs yet.** A README that maps how an
  area's parts relate is a local map, and so is this one. The file
  keeps the name `README.md`, because that is what a reader sees on
  arriving at the folder, and the name is the tool's while the
  content is ours (agent-arrangement §1). The rule and the word wait
  for a pair: `delivery/README.md`'s reading is the second candidate.
  `temp/README.md` holds rules, not a map, and is not one.
- **`delivery/README.md`'s wider reading waits.** Only its wrong count
  is fixed here.
