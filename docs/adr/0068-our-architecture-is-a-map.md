# 0068. Our ARCHITECTURE is a map: a two-page record, its glossary apart

Date: 2026-10-27
Status: Proposed, opened under the commit plan for layer 4's work.
Supersedes ADR-0044 in part, decision 3.

## Context

TODO's "Decide what kind of text our ARCHITECTURE is, and its size"
fell due at round 2's work on layer 4, before its fixes: FINDING-145,
179 and 184 rest on it. The talk behind it is conversation-memory
§17, of 2026-10-25 and 2026-10-26.

Three texts named its kind differently. `docs/conventions/facts-in-sync/`
§4 listed it as a description, beside the concept, the models and the
manuals. `docs/models/idea-to-output.md` §2 lists only manuals and the
concept as descriptions. `docs/conventions/project-recording/` §8
calls it a record, the map of what stands now. It carried no list of
what derives from it, which a description must, and nothing is made
from it: no skill writes or reads ours.

Its size was 3,765 words, where project-recording §8 asks for one or
two pages. ADR-0044 decision 3 let it run past two pages for its own
words and its list of what it knows is wrong. *The words* was 1,053
words, 28% of the page, and the list 33. Of the rest, most retold
other homes: the delivery map, the exchange, facts-in-sync,
agent-arrangement, and each container file's `foundation` line. What
it owned was the pairing of what is stated with what ships, the table
of runs, how each rule that must stay true is held, the codemap, and
the list.

A run keeps its glossary as a file of its own, `docs/glossary.md`.
Writing rule 6 makes ours the one home of each coined word.

Five texts said what this repo is, each in its own words, and none
pointing at another: the README, `CLAUDE.md`, ARCHITECTURE's opening,
the CHANGELOG's header and the tiers model. They agreed, but the
README's "harvested concept changes" was too narrow, since a reading
changes any master, and only `CLAUDE.md` said "the deliverer".

## Options considered

1. **Its kind.**
   - A description. Rejected: it would owe a list of what derives
     from it, and that list would be empty.
2. **The glossary.**
   - Kept inside ARCHITECTURE, as ADR-0044 had it. Rejected: the
     page could not come near two pages, and a map that owns its
     vocabulary owns its largest part for no map's sake.
3. **What it keeps.**
   - Its parts kept, *The words* removed, only the findings fixed:
     about 2,600 words. Rejected: it stays mostly retelling, and
     every new convention or file changes its counts and lists.
   - Run-only, our map moved into the README. Rejected: the table of
     runs, how each rule is held and the codemap each have a reader,
     and none of them is a front door's.
4. **What this repo is.**
   - One sentence, copied into all five. Rejected: five copies to
     keep in step by hand, where one-home rule 5 allows copies only
     when they cannot be avoided, and project-recording §7.1 asks the
     README and the entry file to share no text.
   - All five left as they are. Rejected: the README's narrow line
     stays, and nothing ties the five together.

## Decision

1. **Our ARCHITECTURE is a record, not a description.** It maps the
   repo as it stands, points at owners, and owns a few facts. Its
   header comment is its form. It is checked as a record whose
   header carries a `foundation` line.
2. **The glossary is a file of its own, `docs/glossary.md`,** the
   path a run's has. Its header comment holds the form of an entry
   and `foundation: the writing convention`. It is a record both
   seats keep.
3. **ARCHITECTURE is a map of about two pages.** It keeps: what it
   is, pointing at the README for what this repo is; the pairing,
   the models included; the delivery, one line a group, and the
   table of runs; what must stay true, as a table of rule, home and
   how it is held; the codemap; and what it knows is wrong. Every
   other part points at its home. Project-recording's deliverer seat
   lists these parts, each with what it holds and who reads it; a
   part no one reads goes.
4. **The README is the home of what this repo is.** It holds every
   fact the others tell about it. `CLAUDE.md`'s opening keeps its own
   words for the agent and carries a fact reference to the README.
   ARCHITECTURE's opening points at it. The CHANGELOG's header says
   only what it logs, and the tiers model only where a tier sits.

## Consequences

- Facts-in-sync §4, the foundation check's step 1 and the
  glossary's "description" stop listing ARCHITECTURE as a
  description.
- Writing rule 6, ours and the writing manual's, and project-
  recording §1 name `docs/glossary.md`. One difference between the
  seats goes.
- ARCHITECTURE drops from about 3,765 words to about 1,200. Its §1
  and §2 keep their numbers; its old §3 and §4 go, and §5 and §6
  become §3 and §4.
- ADR-0044 decision 3 is superseded: our map no longer carries its
  words, nor runs past two pages for them. Its list of what it knows
  is wrong stays. ADR-0044's status names this ADR when this one is
  accepted.
- The tiers model still holds this repo's instance. Where that goes
  waits for TODO's "Decide which way a fact reference may point".
