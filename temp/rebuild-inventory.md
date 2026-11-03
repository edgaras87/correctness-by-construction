# What this repo holds, for the rebuild

<!-- A kept file: every Work Approach this repo holds, the idea behind
     each, what it points at, and the lessons it carries. The list the
     rebuild in a new repo reads this repo by, idea by idea. Counted
     2026-11-03 at `ee8f3b0`. -->

28 Work Approaches stand on 16 written ideas: 12 manuals, 3 Idea
Models and the concept. 6 more stand on no written idea. A pair of
copies, ours and the shipped one, counts once: 6 Work Approaches
exist twice.

## 1. The Work Approaches

By the idea each names in its Foundation Line. **Seat:** ours, shipped
to CBC Runs, or both. **Lessons:** ADRs cited, and mentions of a
numbered CBC Run.

| Idea | Work Approach | Seat | Lines | Case | Lessons |
|---|---|---|---|---|---|
| agent-arrangement | `CLAUDE.md`, our Entry File | ours | 47 | what this repo is, and which record holds what | 0 |
| agent-arrangement | `delivery/container/.claude/CLAUDE.md`, the CBC Run's Entry File | shipped | 74 | what a CBC Run is, and which record holds what | 0 |
| commit-messages | the commit-messages Agent Skill | both | 140 + 140 | writing a commit message | 4 ADRs |
| commit-plan | the commit-plan Agent Skill | both | 206 + 206 | work of more than one commit | 3 ADRs |
| conventions | the convention-manual Agent Rule | ours | 102 | writing a manual | 1 ADR |
| exchange | the exchange-read Agent Skill | ours | 114 | reading a CBC Run | 1 ADR |
| exchange | the exchange-reading Agent Rule | ours | 76 | the form of a CBC Run Reading | 1 ADR |
| exchange | the working-a-reading Agent Rule | ours | 137 | working a CBC Run Reading's list | 1 ADR, 2 CBC Runs |
| exchange | the exchange-deliver Agent Skill | ours | 214 | delivering to a CBC Run | 1 ADR |
| exchange | the delivered-copies Agent Rule | shipped | 194 | taking a delivery; editing a copy | 3 ADRs, 1 CBC Run |
| facts-in-sync | the one-home Agent Rule | both | 78 + 60 | where a fact lives | 6 and 5 ADRs |
| facts-in-sync | the Foundation Check | ours | 88 | the check before a commit | 1 ADR |
| project-recording | our records' forms, in each header comment | ours | — | `PLAN.md`, `TODO.md`, the devlog, the ADRs, `CHANGELOG.md`, the glossary, `temp/` | — |
| project-recording | the Record Stubs, `delivery/container/` | shipped | 316 | a CBC Run's records at birth | — |
| project-recording | the playbook, `delivery/fills/cbc-run-pure-playbook.md` | shipped | 250 | a CBC Run's plan, from birth to Release | 6 ADRs |
| repo-hygiene | the three repo files, and their templates | both | 27 | `.gitignore`, `.gitattributes`, `.editorconfig` | — |
| retrospective | the retrospective Agent Skill | shipped | 144 | a CBC Run looking back | 1 ADR, 1 CBC Run |
| retrospective | the apply-retrospective Agent Skill | shipped | 156 | applying the look back before Release | 1 ADR, 1 CBC Run |
| shapes | the shapes-lifecycle Agent Rule | shipped | 119 | how an Output Shape is born and changed | 3 ADRs, 1 CBC Run |
| shapes | 4 Output Shapes, `delivery/method/.claude/shapes/` | shipped | 688 | Evidence Test, Enemy Collision Kill, Invariant Slice Entry, Invariant Slice Record | 0 |
| visual-comparison | the visual-comparison Agent Skill | both | 157 + 158 | how a structure is shown | 3 ADRs |
| writing | the writing Agent Rule | both | 140 + 129 | how a text reads | 8 ADRs |
| concept | the cbc-framing Agent Skill, with references | shipped | 1,354 | framing a new system | 1 ADR |
| concept | the cbc-slice Agent Skill, with references | shipped | 968 | building one Invariant Slice | 0 |
| concept | the cbc-bootstrap Agent Skill, with references | shipped | 1,431 | the first running skeleton, Spring and Postgres | 2 ADRs |
| concept | the infra-establish Agent Skill, with references | shipped | 1,033 | the Runtime Ground | 2 ADRs |
| concept | the infra-serve Agent Skill | shipped | 90 | changing the Runtime Ground later | 0 |
| concept | the Glossary Names, method and stack | shipped | 352 | the concept's and the stack's words | — |

The 6 with no written idea are in §3.

## 2. The ideas behind them

**Points at:** the other ideas the text names, by path or name. A
mention, not yet a need: the rebuild decides which are needs.
**Lessons:** *Its story* lines, then ADRs cited.

| Idea | Its text | Lines | Points at | Lessons |
|---|---|---|---|---|
| agent-arrangement | `docs/conventions/agent-arrangement/` | 604 | 10: agent, commit-messages, conventions, exchange, facts-in-sync, idea-to-output, project-recording, repo-hygiene, shapes, writing | 6, 9 |
| commit-messages | `docs/conventions/commit-messages/` | 136 | 5: agent, agent-arrangement, commit-plan, project-recording, tiers | 3, 4 |
| commit-plan | `docs/conventions/commit-plan/` | 194 | 5: agent, commit-messages, facts-in-sync, project-recording, tiers | 11, 5 |
| conventions | `docs/conventions/conventions/` | 376 | 8: agent, agent-arrangement, concept, exchange, facts-in-sync, idea-to-output, project-recording, shapes | 8, 7 |
| exchange | `docs/conventions/exchange/` | 606 | 11: agent, agent-arrangement, commit-messages, commit-plan, concept, conventions, facts-in-sync, idea-to-output, project-recording, shapes, tiers | 17, 6 |
| facts-in-sync | `docs/conventions/facts-in-sync/` | 414 | 10: agent, agent-arrangement, commit-messages, commit-plan, concept, conventions, exchange, idea-to-output, project-recording, writing | 7, 12 |
| project-recording | `docs/conventions/project-recording/` | 905 | 10: agent, agent-arrangement, commit-messages, commit-plan, concept, conventions, exchange, facts-in-sync, retrospective, writing | 5, 12 |
| repo-hygiene | `docs/conventions/repo-hygiene/` | 120 | 5: agent, agent-arrangement, exchange, project-recording, tiers | 2, 2 |
| retrospective | `docs/conventions/retrospective/` | 195 | 8: agent, agent-arrangement, commit-plan, exchange, project-recording, shapes, tiers, writing | 4, 1 |
| shapes | `docs/conventions/shapes/` | 345 | 4: agent, agent-arrangement, exchange, tiers | 7, 4 |
| visual-comparison | `docs/conventions/visual-comparison/` | 113 | 3: agent, commit-plan, tiers | 3, 6 |
| writing | `docs/conventions/writing/` | 225 | 8: agent, agent-arrangement, commit-messages, conventions, facts-in-sync, project-recording, shapes, tiers | 3, 5 |
| the agent model | `docs/models/agent.md` | 459 | 2: idea-to-output, tiers | 0, 3 |
| the idea-to-output model | `docs/models/idea-to-output.md` | 205 | 4: agent, concept, facts-in-sync, tiers | 0, 3 |
| the tiers model | `docs/models/tiers.md` | 173 | 3: agent, exchange, idea-to-output | 1, 4 |
| the concept | `concept/`, 5 chapters | 507 | none | 0, 0 |

## 3. Ideas with no home

Six Work Approaches name no foundation. The idea behind each is
written only inside the Work Approach itself.

| Idea | Work Approach | Seat | Lines | Lessons |
|---|---|---|---|---|
| trying a new way of working | the approach-drafting Approach on Trial | both | 141 + 141 | 1 CBC Run |
| trying a new way of working | the approach-evaluation Approach on Trial | ours | 164 | 3 ADRs |
| bringing old text up to a new rule | the refinement Approach on Trial | ours | 437 | 4 ADRs, 2 CBC Runs |
| a CBC Run on full auto | the auto-run Approach on Trial | ours | 133 | 1 ADR, 11 CBC Runs |
| an Idea Model taking what it borrows | the model-placing Approach on Trial | ours | 111 | 2 ADRs |
| making a CBC Run Birth | the Pure Seed, `delivery/installs/pure-seed.md` | ours | 338 | 7 ADRs |

Two more ideas have a home but no Work Approach:

- **Conversation Memory:** `TODO-CONVERSATION-MEMORY.md`, on trial.
- **The layering:** `temp/model-example/layers.md`, the new repo's first idea.

## 4. What the table shows

1. **Every manual points at the agent model, and 8 of 12 at the tiers
   model.** The manual's form asks for it: *Why it arrives this
   way* rests on the agent model, and *The seats* on the tiers. So
   these come from the form, not from the ideas.
2. **The concept and its Work Approaches point at nothing:** 507 lines of
   concept and about 5,900 shipped. The largest part is already
   independent. It may move nearly whole.
3. **The lessons gather in 3 ideas:** exchange, 17 *Its story* lines;
   commit-plan, 11; conventions, 8. These are where a fresh rewrite
   loses most if it skips them.
4. **6 Work Approaches exist twice,** ours and the shipped one, about
   1,700 lines in both copies: commit-messages, commit-plan, visual-comparison,
   one-home, writing and approach-drafting.
5. **6 Work Approaches have no written idea,** 1,465 lines in all. The
   rebuild writes their ideas or drops them.

## 5. A draft order

By what the new repo needs first. Each idea goes in whole: idea,
project text, Work Approach.

1. **The layering:** the three templates.
2. **repo-hygiene and commit-messages:** before the first commit.
3. **writing:** every text after that uses it.
4. **project-recording:** plan, devlog, TODO and ADRs, only the parts
   used.
5. **facts-in-sync:** once there are enough texts to drift apart.
6. **commit-plan:** at the first work of more than one commit.
7. **exchange,** with the Pure Seed: when the new repo first ships to
   a CBC Run.
8. **The concept, with its Work Approaches, shapes and retrospective:**
   what a CBC Run uses.

**Waits until an idea needs it:** the agent model, the tiers model,
the idea-to-output model, conventions and agent-arrangement. §4 point
1 suggests few ideas will.

**Not decided:** the 5 Approaches on Trial and Conversation Memory
(§3): each is rebuilt when its work comes up, or dropped.

## 6. How it was built

- **Work Approaches:** every Agent Skill, Agent Rule, Approach on Trial
  and Output Shape under a `.claude/`, the playbook, the Pure Seed,
  both Entry Files, the Record Stubs and the repo files.
- **The idea behind each:** its Foundation Line. "Practice, checked
  against concept v1" counts as the concept.
- **Points at:** another idea's path or name in the text: a manual's
  path or "the <name> convention", an Idea Model's path or "the <name>
  model", `concept/` or "concept v1".
- **Lessons:** distinct ADR numbers, "CBC Run" followed by a digit,
  and *Its story* lines. A lesson told without these is not counted.
- **Not read:** what each text says. A row says what a text is for,
  from its own opening line, not whether that is true.
