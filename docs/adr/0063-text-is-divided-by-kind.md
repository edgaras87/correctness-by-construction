# 0063. Text is divided by kind

Date: 2026-10-24
Status: Accepted (2026-10-24, at the set's records commit; opened
Proposed under the commit plan for text division, decision 10
widened and decision 11 added since).

## Context

On 2026-10-20 the reviewer asked how this repo's text is divided.
The deliverer's role was spread over `ARCHITECTURE.md` §2 and §3,
`docs/models/tiers.md`, the exchange, eleven seats sections and
project-recording §9. Staying in step was split over
project-recording §11 and conventions §3.1 to §3.6. Only the agent
had a model, a manual and the files made from it: the agent model,
agent-arrangement and `.claude/`.

The talk ran on 2026-10-20, 10-21, 10-23 and 10-24
(`30eb42e:TODO-CONVERSATION-MEMORY.md` §1). The reviewer asked to
settle the chain of kinds first, "and this will answer itself". Seven
questions were worked in order. The sixth, the agent's chain, waited
for the agent model and agent-arrangement to be checked against
Claude Code's documentation and community practice, done in
`36eb0c1` to `8a7ef70`.

Rechecked, the agent's chain was not the one drawn on 2026-10-20.
agent-arrangement named its model only in prose; `.claude/`'s
skills and rules stand on their own conventions, not on it; the
model's §8 is what every manual's *Why it arrives this way* reasons
from, with no link back; and both entry files carried two
`foundation` lines.

## Options considered

- **One big convention for the deliverer's role.** Rejected: its
  opening could not name one subject, and part of it would have to
  move when the delivery leaves for a repo of its own.
- **A convention for every idea.** Rejected: each pays a manual,
  seats, an index entry and an ADR, even where there are no rules.
- **The chain inside the tiers model.** Rejected on 2026-10-21:
  tiers answers which repo a thing belongs to, the chain what kind
  of text it is. Every repo holds several kinds, so one model
  holding both would be the mix this item is about.
- **A model stays free and binds nothing.** Rejected: if nothing
  makes a manual follow its model, the model drifts.
- **A model above correctness by construction.** Rejected: a
  concept has one form and one home. What a concept is waits for a
  second concept repo.
- **A `foundation` line for each part of a file,** in a comment
  beside it. Rejected: a second root in one file is a reference to
  a part, and the walk already greps for those.
- **A pointer to the agent model in the form of a manual only.**
  Rejected: when the model changes, the walk would find the form,
  never the eleven sections that reason from it.

## Decision

1. **Five kinds:** a model; a description, a manual or the concept;
   an approach, a skill, a rule, an approach on trial or a record's
   form; an output, a record, a slice or code; and a shape, which
   governs an output at the gate. `docs/models/idea-to-output.md`,
   the idea-to-output chain, states them.
2. **A model is the top description of its chain,** and binds what
   stands on it. "Binds nothing" leaves the models' headers. The
   foundation check's four endings let either side be wrong.
3. **A model and a concept differ by where things vary.** A model's
   rules vary by repo, like an interface. A concept has one form and
   one home, is copied whole, and only its outputs vary.
4. **The links:**
   - **stands on**, the `foundation` line;
   - **points**, a path and section on a line, called a tag today
     and to be named the fact reference (TODO);
   - **governs**, a shape over an output;
   - **written from**, the up direction;
   - **requires**, one skill delegating to another convention,
     kept.

   No link runs from a model to an approach. Its trigger: an
   approach whose rules no convention could hold.
5. **One root per file, tags for parts.** A file names one
   `foundation`, what the whole of it was written from: in
   frontmatter, or in a record's header comment. A manual's root may
   be a model. Every line that uses a part of any document, its root
   included, carries a tag to that part. The root tells the
   foundation check which document to open; a tag tells the walk
   which line to re-read.
6. **The up direction:** unfamiliar work, then an approach on trial,
   then a convention, then a model; outputs, then a shape. The steps
   between repos stay tiers §3.
7. **The conventions convention stays, smaller.** Its §1 goes to the
   model. §3.1, §3.2, §3.5 and §3.6 go to a convention for staying
   in step. Both moves are round 2's.
8. **A record's form stays project-recording's.** A form in a
   header comment is an approach, not a shape.
9. **The agent's chain:** the agent model stands above
   agent-arrangement, which stands above the entry file's guard and
   the decisions log's header. Each manual's *Why it arrives this
   way* tags the part of the agent model it reasons from.
10. **Questions held with a trigger are TODO items:** whether a
    model ships; a link from a model to an approach; a model for a
    single convention; which ideas here are models; and the
    staying-in-step convention, which only this ADR named.
11. **Decided while the plan ran:**
    - every link points up: a lower text relies on an upper one,
      which at most lists what stands on it. A model points only at
      its own sections, at other models, or at nothing;
    - when two linked texts disagree, the disagreement is settled,
      by changing the lower, the upper, or both;
    - after a birth, the lower text is rewritten to stand on the
      new one;
    - a model is a description; the grep for its name in
      `foundation` lines is its list of what stands on it.

## Consequences

- `docs/models/idea-to-output.md` is written.
- Conventions §2 and §3.5, the form of a manual, the foundation
  check and *The words* say one root per file and tags for parts.
- agent-arrangement names `the agent model` as its root. The eleven
  manuals' channel sections tag the agent model. Both entry files'
  records tables tag project-recording §13, and the guard's
  `foundation` is each file's one root.
- The agent model's §1 points at tiers §2.3 instead of retelling
  how the repos relate.
- The text-division item, the records-table item and conversation
  memory §1 go. The two items waiting on this one are freed.
- Round 2 keeps its part: the conventions convention's moves, the
  staying-in-step convention, the hand-off chain's rename, *The
  words*' "model" entry, and the requires grep in the walk.
