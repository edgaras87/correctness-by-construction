# Commit plan: two derivations of the conventions

## Summary — the state after all commits

The convention manuals are the one source, and two things derive
from them. `delivery/container/` is the run's: what a CbC run is
born into and receives, a builder's arrangement. This repo's own
records and `.claude/` are the deliverer's, a maintainer's, and
ours. Where a file ends up identical in both, that is an outcome and
not a dependency. When a convention changes, each derivation is
updated from its manual, and neither is copied from the other.

No text says any longer that the deliverer keeps its records "under
the same stubs" or renews its skills "from the container". The
decisions log stops pinning our own skills to a commit of this repo.
A maintainer's container does not exist. A TODO item names the
trigger for one: a second maintainer repo, filtered out of this one.
Nothing changes on the run's side, and nothing goes to run 3 about
it.

## Commits

**1. `docs(agent): add commit plan for the split`**
This plan.

**2. `docs(adr): ADR-0042 — two derivations of one set`**
The decision was settled in conversation, so it is recorded first
and then carried out. ADR-0042 opens as Proposed. It gives the
evidence: our PLAN no longer matches the container's stub, the entry
files were never the same, and the decisions log flagged the
circularity on 2026-09-19 ("we are the deliverer and a receiver of
the same artifacts"). It also notes that every skill and rule we
hold already names its convention as its `foundation`, not the
container. And it cites ADR-0038, which already answered what the
container is for: what CbC runs need.

**3. `docs: each seat derives from the manuals`**
The texts that tie us to the container change together, because
any one of them left standing would contradict the others:
- project-recording's "made usable as" list and its seats, which
  say "under the same stubs".
- agent-arrangement's seats: "nearly the same files", and "three
  skills are the same files".
- commit-messages' line on "the deliverer's own skill copies renewed
  from the container".
- `docs/master.md` §4: "two exist here, tied to each other".
- `delivery/README.md`: "`delivery/container/` is this repo's
  container".
- ARCHITECTURE's container section, which gains the sentence that
  our own arrangement is not taken from it.

**4. `chore(agent): our skills are derived, not copied`**
The decisions log gets an entry. The three convention skills are
ours, derived from their manuals and identical to the container's
today. Its "copies renewed … at <commit>" entries and the pins on
our own skills stop, and the 2026-09-19 entry's open question is
answered. The agent's files never share a commit with the records.

**5. `chore(agent): the log and its row say what is true`**
Found at step 4. The reviewer asked what the log is for, and it
was re-evaluated on its 44 entries. About 20 are the registry of a
receiver: conventions injected and updated at a pin, and copies
renewed. They are history now, since ADR-0038 and ADR-0042. About
12 are arrangement choices with no other home, such as commit
attribution and the path rule. About 12 record what our
arrangement did about an ADR, and those run to 20–50 lines retelling
it. The log stays, because it holds how this repo's own agent works,
which the ADRs do not. Its header keeps what the file is and the
division of labour, and gains one rule: an entry that follows from
an ADR says in a line or two what changed here, and points at the
ADR. The paragraphs on a handbook retrospective, a birth pin and a
repeated commit rule go. `CLAUDE.md`'s row for the log becomes
"Agent setup changed | Decision, why, rejected options", since here
a convention is written, not received. Both are agent files, so
they share one commit.

**6. `docs(conventions): our log holds no registry`**
agent-arrangement's deliverer seat gains the sentence: our decisions
log holds arrangement decisions only, and no registry of received
conventions (CBC ADR-0042). A run's log keeps both, and it is the
channel `exchange-read` reads, which is why its entries are longer.

**7. `docs: devlog carries the split`**
The session's entry. ADR-0042 flips to Accepted here. TODO gains
two items. One is the maintainer container: the trigger is a second
maintainer repo, and the idea, the reviewer's, is to filter this
repo, keeping the functionality and layout and dropping what is
this concept's. The other asks whether a run's log entries should
be shorter too. We read them, so that waits on a reading of run 3.

**8. `docs(agent): close commit plan for the split`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **Decision first.** The split was agreed before the plan opened,
  so the ADR comes before the texts it changes, unlike the last two
  sets, whose rule came out of the material.
- **Identical is allowed.** Three skills stay byte-identical to the
  container's. Diverging them for the sake of separation would be a
  change nobody needs. What changes is the direction: each is
  checked against its manual.
- **No maintainer container now.** It would be built ahead of its
  second user. A trigger is named instead.
- **The run's side is untouched.** The container, its stubs and
  what it ships stay as they are, so there is no delivery.
