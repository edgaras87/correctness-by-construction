# Commit plan: round 2's layer 2, its layout and references

## Summary — the state after all commits

The first of layer 2's three commit plans. It fixes the findings
that move text or add a reference in project-recording and its
neighbours, so the two larger plans after it are written against
final section numbers (`temp/refinement-2026-10-18.md`, *Round 2*).

- **Conversation-memory is project-recording §14,** a numbered
  section of its own after §13 (FINDING-146). TODO's *When* and
  *Anti-patterns* are §5.5 and §5.6 again. Every living pointer to
  the old §5.5 lands on §14.
- **§7.1 says who the README is for** and that the entry file is
  the agents' front door. §7.6 holds only anti-patterns
  (FINDING-147).
- **The `CBC ADR-nnnn` tag has one home,** project-recording §3.5.
  Exchange §3.7 keeps its sentence, with a fact reference to it.
  `exchange-deliver` drops the clause: a note's writer does not act
  on what a shipped file carries (FINDING-148).
- The refinement's file names each fix's commit.

## Commits

**0. `docs(agent): add commit plan for layer 2's layout`**
Opens the set.

**1. `docs: conversation-memory moves to §14`**
FINDING-146. §5.5 becomes §14, placed last; §5.6 and §5.7 become
§5.5 and §5.6. Its opening says "a TODO item", since it no longer
sits under TODO. Pointers move in the same commit: project-recording
(two), *The words* in `ARCHITECTURE.md`, and the header comment of
`TODO-CONVERSATION-MEMORY.md`. The sweep greps §5.5, §5.6 and §5.7
at once, the text unwrapped.

**2. `docs: README's audience line moves to §7.1`**
FINDING-147. "README is the front door for people; the entry file
is the one for agents" leaves §7.6 for §7.1, the README's *What*.

**3. `docs: exchange §3.7 points at the tag's home`**
FINDING-148, the manual's half. The sentence on the tag a shipped
file carries gains a fact reference to project-recording §3.5.

**4. `chore(agent): exchange-deliver drops the tag clause`**
FINDING-148, the skill's half. Item 7's "A shipped file carries
`CBC ADR-nnnn` instead" goes. Agent file, next after 3.

**5. `docs: round 2's layer 2 layout is worked`**
The records commit. The refinement's file: FINDING-146, 147 and 148
name their commits.

**6. `docs(agent): close commit plan for layer 2's layout`**
Deletes this file; the body says what diverged.

## Decisions for you to object to

- **§14, not a renumbered §5.** FINDING-146 asked for "a numbered
  section of its own, placed last". Project-recording numbers by
  creation, its §13 italic says; §14 keeps that, and moves only
  §5.6 and §5.7, which nothing outside cites.
- **The skill cuts the clause, not adds a reference.** Item 7 tells
  the writer what a note never carries. What a shipped file carries
  is not the writer's act, so the skill does not need it; the
  exchange manual keeps the why.
- **No ADR.** Each fix follows a finding's ending the reviewer
  already took.
