# 0071. Which way a fact reference points

Date: 2026-10-28
Status: Proposed, opened under the commit plan for direction and
placing.

## Context

`docs/models/idea-to-output.md` §3.2 says every link points up, and
§3.1 that a line may point at a fact's home in any document. Nothing
said what "up" means between two texts of one level, or how a line
that names a text differs from one that relies on it. TODO's "Decide
which way a fact reference may point" fell due at round 2's close.
The talk is conversation-memory §16, of 2026-10-25 and 2026-10-28.

Measured on 2026-10-28, in living text:
- A model names a manual or the concept 4 times, a skill or shape
  3, a record 2. A manual names a skill, rule or approach 120
  times, a record 89. Most name what a manual describes, or list
  what stands on it.
- The lines that rely on something below are few. The tiers model
  sends its reader to the exchange three times and to
  `delivery/README.md` once, and holds this repo's "today" facts
  and three ADRs.
- `requires` sits in 4 skills, 7 names. Conventions §1.2 says it
  names conventions, and also that it refers to a skill by name;
  `commit-plan` names project-recording, which has no skill. Every
  name sits in its skill's own group, groups ship whole, and the
  tool ignores the field (`docs/conventions/agent-arrangement/`).
  ADR-0063 kept it, and owed a grep in the walk that was never
  added.

## Options considered

1. **Direction for every mention.** Rejected: it forbids a manual
   naming the records it describes, in about 200 lines.
2. **No direction.** Rejected: a model could lean on one repo's
   manual, and stop being general.
3. **A model says nothing of this repo.** Rejected: it loses the
   examples a reader learns from.
4. **A "This repo" section closing each model.** Rejected: the
   reader jumps to the end for every example.
5. **A model's reference down replaced by one general line.**
   Taken only where the lower text holds nothing general; where it
   does, the line loses what the next project could derive from.
6. **`requires` kept, grepped by the walk.** Rejected: its use,
   landing conventions together, ended when groups shipped whole,
   and the lines inside a skill say the same with fact references.
7. **`requires` as a fact reference.** Rejected: heavy frontmatter
   for what the lines already say.

## Decision

1. **A line that relies on a fact points at its home at its own
   level or above, never below.** Sideways is a fact whose home sits
   beside the line. A line that only names or lists a text, the
   record a manual describes or what stands on it, may name any
   level. Naming is not a link.
2. **A reference down is placed upward.** Where the lower text holds
   an idea general enough, the idea is written into the upper text
   in general words, and the lower text stands on it and points up.
   Where it holds only this repo's specifics, the upper text says
   one general line. Facts about this repo go to `README.md`
   (ADR-0068). A marked example, which the claim does not rest on,
   may stay.
3. **`requires` goes.** The links are four. This reverses ADR-0063's
   "kept".
4. **The first placing into a model is drafted as an approach on
   trial while it runs,** `.claude/approaches-on-trial/model-placing.md`,
   as first-time work is (`.claude/approaches-on-trial/approach-drafting.md`).
   "Placing" is the word `approach-evaluation.md` uses for the step
   below.

## Consequences

- Idea-to-output §3 states the direction, with four links;
  facts-in-sync §3.1, conventions §1.2, the glossary's *link* and
  our `convention-manual.md` follow.
- Four skills lose `requires`, one ours and three shipped.
- The tiers model's §3 states the general flows learned from the
  exchange, and the exchange stands on it. This repo's place in the
  tiers goes to `README.md`. The agent model's `PLAN.md` example is
  marked.
- Idea-to-output §2's "Here" column stays: it names, under a heading
  that marks it as this repo's.
- How a missing foundation is written, the step to a model above
  all, is TODO's "Decide how a text finds its foundation", with this
  placing as its first evidence.
