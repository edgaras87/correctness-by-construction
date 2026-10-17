# Commit plan: the container's templates

## Summary — the state after all commits

A run is born with four templates that carry run 3's RETRO D1, D10
and D16 (the reading's W14, decisions 1 to 4):

- `ARCHITECTURE.md` keeps its invariants as a table, one row per
  rule, each linking the slice that proved it. A slice's close adds
  or changes rows, never a paragraph.
- ARCHITECTURE answers what a slice may rely on. Each component says
  it, and the entry file's records table sends the question there.
- `devlog/devlog.md` asks for what happened, the dead ends and where
  to resume, and links what another record holds.
- `.claude/decisions.md` opens on the rules in force now. An entry
  has three parts, not three lines.

The two manuals say the same: project-recording §8, agent-arrangement
§3.4. `cbc-slice`'s close names the table the template has. F2's and
F3's holds end, and so does TODO's item on a decisions entry's length.

## Commits

**1. `docs: ARCHITECTURE keeps its invariants as a table`**
Decision 1. The template's Invariants become a table: Rule, Computed
by, Refused by, Guarded by, Proved by, with an example row from the
order service. Its header comment says by rule, not by slice.
project-recording §8.4 gains a line and a dated lesson from run 3.
`cbc-slice`'s close names "the Invariants table". One change: the
table, the manual that explains it, and the skill that writes rows
into it.

**2. `docs: ARCHITECTURE answers what a slice relies on`**
Decision 2. The entry file's ARCHITECTURE row opens on "or asking
what a slice may rely on". Each component in the template gains "A
slice may rely on:", which `cbc-bootstrap`'s close writes.
project-recording §8.1 too, if the foundation check finds it behind.
On its own, because it reverts apart from the table.

**3. `docs: a devlog entry links what it would retell`**
Decision 3. One line in the devlog stub's comment. The manual's §4.1
agrees and stays.

**4. `docs: the decisions log lists the rules in force`**
Decision 4. The stub opens on "Rules in force now" and "Replaced, and
by what". An entry has three parts, not three lines.
agent-arrangement §3.4 says the same. TODO's item on an entry's
length ends, and the refinement item gains our own log's list.

**5. `docs(temp): the reading closes W14`**
W14 marked done with its commits. F2's and F3's holds end. The pass
over every open item, by `working-a-reading.md` step 5.

## Decisions taken inside this plan

- **No CHANGELOG commit.** A delivery's change is no entry
  (ADR-0039), and `cbc-slice`'s change is a name. F2's own take of
  the skill, `2674c03`, added none.
- **TODO changes in commit 4, not in a records commit of its own.**
  The item ends because that commit answers it. Reverting the commit
  brings back both.
- **Our own records are untouched** unless a foundation walk finds
  one behind. Our `ARCHITECTURE.md` maps the delivery, not a run's
  system, and our decisions log's list waits for the refinement.
- **The devlog entry comes at the session's end,** not in this plan.
