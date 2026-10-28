# 0070. How a fact reference is written

Date: 2026-10-27
Status: Accepted (2026-10-28, at the set's records commit; opened
Proposed under the commit plan for the reference's homes. Since then,
the off-template rule's home moved from one skill to the exchange
and the run's `delivered-copies.md`). Decision 7 superseded in part
by ADR-0072.

## Context

ADR-0065 named the fact reference: the address a line carries when
it relies on a fact written elsewhere. It wrote it as a path and a
section, and deferred a title, since about 200 references would be
rewritten. TODO's "Decide how a fact reference is written" fell due
at round 2's close. The talk is conversation-memory §13, of
2026-10-24 and 2026-10-27.

Measured on 2026-10-27, in living text:
- 329 references carry a path and a section, in 73 files, 16 of them
  shipped. 200 sit in parentheses; 129 are part of their sentence.
- 252 numbered section titles: a mean of 17 characters, 32 over 30.
- "Pointer" is used 39 times in 17 files. The agent model's claims
  P1 and P2 use it for any text that sends an agent to a file; most
  other uses mean a fact reference.
- Inside skills, 28 paths are relative to the skill and about 13
  name a sibling bare. Two skills hold `references/worked-example.md`.
- The run's `writing.md` rule 8 asks "KILL-2, the second charge for
  one order, fails". Its `one-home.md` rule 2 says "Elsewhere, link;
  don't retell". ADR-0059 left a run's case to be designed.
- The off-template rule is told in four shipped files that disagree,
  and stated whole only in the devlog of 2026-08. The method's
  no-stack rule is stated only in ADR-0029.
- A line with no fact reference is found by nothing: the walk sees
  only lines that carry one. The 11 manuals' channel sections went
  without one until 2026-10-24.

## Options considered

1. **The title.** None, with a writing rule deciding when a line
   says what a section is. Rejected: a rule that needs judgment is
   applied unevenly, and a title lets a stale number show.
2. **Parentheses.** Only where they fit the sentence. Rejected: one
   shape lets the walk and the reader find a reference, and the
   sentence says its point in words.
3. **"Pointer".** Dropped everywhere, the model included. Rejected:
   the model's P1 and P2 are about more than fact references.
4. **A skill's own files.** A "same skill" relative case. Rejected:
   two skills share a file name, so a grep cannot tell them apart.
5. **A run's retelling.** Waited for a run to show the need.
   Rejected: the run's two shipped rules already disagree.
6. **History as a fact's only home.** Rejected: nothing changes at a
   history entry, so the walk never re-reads what tells it.
7. **The foundation.** A line applying its own foundation carries no
   reference, or only where it sends the reader there. Rejected: in a
   foundation as large as project-recording, a line's fact is not
   found without its section, and every change would mean searching
   the manual again.

## Decision

1. **A fact reference carries its title,** always in parentheses:
   (`<path>` §<number>, *<title>*). In the same document it drops
   the path; to another repo it leads with that repo's tag, CBC; a
   section with no number gives its title alone; a long title is cut
   to its first words.
2. **"Pointer" stays the agent model's wider word.** Where it means
   a fact reference, it becomes one.
3. **A skill names its own files by a path from the root.**
4. **A run may retell beside an id where the reader acts on it.** An
   id is a run's fact reference, written bare. A change at the home
   greps the id, in the same commit.
5. **A shipped line never sends a run into our manual.** A CBC
   reference there is for our walk; the line stands alone.
6. **A fact stated only in history gets a living home first.**
7. **A derived file's lines carry fact references to its foundation
   too.** The reference re-reads its line; the `foundation` line
   re-reads the whole file when its root changes.
8. **At each commit, each new or changed line is asked** whether it
   relies on a fact written elsewhere and says where. Our seat only.
9. **A rename's grep also covers a retitled section and a fact moved
   to a new home,** a placed approach among them.

## Consequences

- Facts-in-sync §1, §3.1, §3.3, §4 step 2 and both seats state the
  decisions; the glossary, commit-plan §2.10, both `one-home.md`,
  `foundation-check.md` and both `commit-plan` skills follow.
- Exchange §3.4 states the no-stack rule. Exchange §5.8 and the
  run's `delivered-copies.md` rule 8 state how a skill's template is
  filled, and the off-template rule; five shipped tellings point at
  rule 8.
- The rewrite follows as a plan of its own: 329 titles, 129
  sentences, 34 uses of "pointer", 41 skill paths, and the shipped
  retellings of the refinement's FINDING-202, 204, 216, 219 and 220.
- Every reference grows by about 20 characters, and a retitled
  section is grepped like a renumbered one.
- **Trigger to revisit decision 7:** a file where references sit on
  most lines and add nothing. One reference per section of the
  derived file is then weighed.
- **Trigger for a standing full read:** TODO's "Decide whether a
  standing full read looks for missing fact references".
