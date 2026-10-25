# 0065. The facts-in-sync convention

Date: 2026-10-25
Status: Proposed (2026-10-25, under the commit plan for
facts-in-sync).

## Context

The rules that keep a fact and the lines relying on it in
agreement were spread over two manuals:

- project-recording §11, rule 1: each fact has one home, and a copy
  is a follower;
- conventions §3.1: point and derive, the two relations;
- conventions §3.2: a pointer is a path;
- conventions §3.5: the rule for every description, the list, the
  `foundation` line and the walk;
- conventions §3.6: a disagreement, decided either way.

Two rules act on them: `one-home.md`, standing on
project-recording, and `foundation-check.md`, standing on the
conventions convention.

Round 1 of the refinement found the subject split, on 2026-10-20,
and named it "staying in step". ADR-0059 kept the rules in their
homes then: moving text between manuals is round 2's kind of fix.
ADR-0063 decision 7 gave them a convention of their own, in round
2.

Round 2's rule check (`d766e8f`) found the rules of its One home
and Dependencies kinds in doubt. Both would change their home
mid-read, and One home's findings rest on what a tag is, which no
text defines (TODO, the fact-reference item;
`TODO-CONVERSATION-MEMORY.md` §13).

## Options considered

- **Leave the rules where they are.** Rejected: round 2 would read
  against a subject split over two manuals, each holding more than
  its own.
- **Move them all into project-recording, or into the conventions
  manual.** Rejected, as in ADR-0059: each would then hold a subject
  wider than its own.
- **The name.** `staying-in-step`: rejected, since "step" is PLAN's
  word. `links`: plain, but any hyperlink is one. `traceability`:
  the engineering word, but long. `anchors` and `lineage`:
  metaphors, which would have needed a line in the writing rule.
  `in-sync`: no subject, and "sync" meant copying files between
  repos here. Taken: `facts-in-sync`.
- **The fact reference's full written form now,** path, section
  and title. Deferred: about 200 references would be rewritten, a
  change of its own, and round 2 does not need it.
- **A run's case now,** its ids as fact references, as ADR-0059
  decision 4 planned for this convention. Deferred: it rests on the
  written form, and round 2 reads our seat's text.
- **Renumber the conventions manual.** Rejected: references to
  §3.3, §3.4 and §3.7 would move for no change of meaning.
- **Rename `one-home.md`.** Rejected: the rule is one home; the
  convention is wider.

## Decision

1. **A convention, facts-in-sync,** its manual at
   `docs/conventions/facts-in-sync/`, standing on the
   idea-to-output model, whose §3 names the links it keeps.
2. **It holds one home, point and derive, the fact reference, the
   rule for every description, and a disagreement.**
3. **The fact reference** is what a line carries when it relies on
   a fact written elsewhere: the address of the fact's home,
   written today as a path and a section. It has two readers: the
   agent, which may follow it, and the walk, which re-reads the
   line when the home changes. "Tag" is no longer used for it.
4. **Its artifacts** are `one-home.md`, ours and the shipped one,
   and `foundation-check.md`, ours.
5. **The old homes keep a pointer.** The conventions manual keeps
   its numbers, with one line where §3.1, §3.2, §3.5 and §3.6 were;
   project-recording §11 keeps its pipeline, its rule 1 pointing at
   the new manual.

## Consequences

- Twelve manuals. A change to how facts are kept in sync is made in
  one.
- Round 2 reads its One home and Dependencies kinds against the new
  manual.
- The shipped `one-home.md` changes its `foundation` now, and again
  when a run's case is designed.
- The staying-in-step item closes. The fact-reference item keeps
  the written form and a run's case.
