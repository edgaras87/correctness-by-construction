# What this repo holds, for the rebuild

<!-- A kept file: every Work Approach this repo holds, the idea behind
     each, what it points at, the lessons it carries, and the facts
     many texts share. The list the
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

## 6. The shared facts

A shared fact is a section that 5 or more pointers from other files
name. 466 pointers name 151 sections. 31 sections take 5 or more,
228 pointers in all: half the pointers, on a fifth of the sections.

Sorted by what the rebuild does with them:

**A. Replaced by the layering itself:** 6 sections, 43 pointers. The
layering's three templates and its links-only-up say the same things.

| Pointers | Files | Section |
|---|---|---|
| 12 | 8 | conventions §1.3, *The Foundation Line* |
| 9 | 6 | the idea-to-output model §2, *The kinds* |
| 6 | 5 | the idea-to-output model §3.1, *The four Chain Links* |
| 6 | 4 | the idea-to-output model §4.2, *The upward direction* |
| 5 | 4 | conventions §2, *The Convention Manual* |
| 5 | 5 | conventions §2.4, *The seats* |

**B. Needed on the first day, from ideas the draft order puts late:**
7 sections, 50 pointers. They say how the agent is set up: the Entry
File, how an Agent Rule or an Agent Skill loads, what this repo is.

| Pointers | Files | Section |
|---|---|---|
| 13 | 10 | agent-arrangement §5.6, *Rules files* |
| 8 | 5 | agent-arrangement §2.4, *How the Entry File is written* |
| 7 | 3 | the agent model §4.1, *Ambient Channel* |
| 6 | 5 | the agent model §8, *Choosing a channel* |
| 6 | 4 | the tiers model §2.2, *Concept Repos* |
| 5 | 4 | agent-arrangement §3.4, *`.claude/decisions.md`* |
| 5 | 5 | the agent model §4.2, *Pulled Channel* |

**C. From ideas the draft order puts early:** 4 sections, 33 pointers.

| Pointers | Files | Section |
|---|---|---|
| 13 | 10 | commit-messages §2.3, *The `agent` scope* |
| 7 | 5 | commit-messages §2.4, *Commit on the word* |
| 7 | 6 | project-recording §13, *The records table* |
| 6 | 4 | writing §2, *Why each rule* |

**D. Exchange's, with the flow between repos:** 11 sections, 70
pointers. Ideas built before
exchange that rely on these write them as needs until exchange is
built.

| Pointers | Files | Section |
|---|---|---|
| 10 | 9 | exchange §3.2, *What goes* |
| 8 | 7 | exchange §3.4, *One group per file* |
| 7 | 6 | exchange §2.2, *The CBC Run* |
| 6 | 4 | exchange §1, *What cannot change* |
| 6 | 5 | exchange §6.3, *The CBC Run Reading* |
| 6 | 4 | exchange §3.3, *A group's place in the tree* |
| 6 | 4 | exchange §5.8, *Agent Skill Templates* |
| 6 | 4 | the tiers model §3.5, *What holds on every flow* |
| 5 | 5 | exchange §6, *Up from the CBC Run* |
| 5 | 4 | exchange §4, *The Delivery Take* |
| 5 | 4 | exchange §6.1, *Reading a CBC Run* |

**E. One each:** 3 sections, 32 pointers.

| Pointers | Files | Section | Where it goes |
|---|---|---|---|
| 19 | 7 | facts-in-sync §4, *A Canonical Description's rule* | facts-in-sync, the most pointed-at fact |
| 8 | 7 | the shapes-lifecycle Agent Rule §3, *A difference at the close* | the CBC Run's side, with the concept |
| 5 | 2 | the approach-drafting Approach on Trial §3, *Close* | trying a new way of working (§3) |

What it changes in the draft order (§5):

1. **Group B comes early.** How the agent is set up is needed at the
   first Entry File and the first Agent Rule, so before writing (§5,
   step 3). agent-arrangement and the agent model wait only for their
   other parts.
2. **Group A needs no idea of its own.** The layering, §5 step 1,
   holds it.
3. **Exchange is pointed at most,** 70 pointers on 11 sections. Every
   idea built before it that relies on these holds a need until
   exchange is built.

## 7. How it was built

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
- **Shared facts:** a path to another file followed by § and a number,
  in Living Text. A pointer by title alone, or inside its own file, is
  not counted. A shipped copy's pointers count with ours.
- **Not read:** what each text says. A row says what a text is for,
  from its own opening line, not whether that is true.
