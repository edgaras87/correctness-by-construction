# The map of today's Maintainer Repo, for the rewrite

<!-- A kept file: the map the rewrite into the layers model reads
     this repo by (ADR-0082, decision 2). Each text, the parts it
     holds, the layer each part goes to, and which text needs
     another first; and the TODO items that land with a text (§8).
     Counted at `491e673e` (§7). It began as the inventory of
     2026-11-03, for the rebuild in `cbc-concept`, which ended
     (ADR-0082, decision 3). That rebuild's draft order, §5, went
     with it; the numbers after it are kept. -->

41 Work Approaches. 35 stand on 17 written ideas: 12 manuals, the
concept and 4 Problem Domain Ideas under `knowledge/`. 6 stand on no
written idea (§3). A pair of copies, ours and the shipped one, counts
once: 6 Work Approaches exist twice.

## 1. The Work Approaches

By the idea each names in its Foundation Line, or in its header's
"What it stands on". **Seat:** ours, shipped to CBC Runs, both, or
the Backend Kit's, kept here for Backend Repos. **Lessons:** ADRs
cited, and mentions of a numbered CBC Run.

| Idea | Work Approach | Seat | Lines | Case | Lessons |
|---|---|---|---|---|---|
| agent-arrangement | `CLAUDE.md`, our Entry File | ours | 51 | what this repo is, and which record holds what | 0 |
| agent-arrangement | `delivery/container/.claude/CLAUDE.md`, the CBC Run's Entry File | shipped | 74 | what a CBC Run is, and which record holds what | 0 |
| commit-messages | the commit-messages Agent Skill | both | 141 + 141 | writing a commit message | 5 ADRs |
| commit-plan | the commit-plan Agent Skill | both | 206 + 206 | work of more than one commit | 3 ADRs |
| conventions | the convention-manual Agent Rule | ours | 102 | writing a manual | 1 ADR |
| exchange | the exchange-read Agent Skill | ours | 114 | reading a CBC Run | 1 ADR |
| exchange | the exchange-reading Agent Rule | ours | 76 | the form of a CBC Run Reading | 1 ADR |
| exchange | the working-a-reading Agent Rule | ours | 137 | working a CBC Run Reading's list | 1 ADR, 2 CBC Runs |
| exchange | the exchange-deliver Agent Skill | ours | 214 | delivering to a CBC Run | 1 ADR |
| exchange | the delivered-copies Agent Rule | shipped | 194 | taking a delivery; editing a copy | 3 ADRs, 1 CBC Run |
| facts-in-sync | the one-home Agent Rule | both | 78 + 60 | where a fact lives | 6 ADRs |
| facts-in-sync | the Foundation Check | ours | 88 | the check before a commit | 1 ADR |
| project-recording | our records' forms, in each header comment | ours | — | `PLAN.md`, `TODO.md`, the devlog, the ADRs, `CHANGELOG.md`, the glossary, `temp/` | — |
| project-recording | the Record Stubs, `delivery/container/` | shipped | 316 | a CBC Run's records at birth | 1 ADR |
| project-recording | the playbook, `delivery/fills/cbc-run-pure-playbook.md` | shipped | 254 | a CBC Run's plan, from birth to Release | 6 ADRs |
| repo-hygiene | the three repo files, and their templates | both | 131 + 95 | `.gitignore`, `.gitattributes`, `.editorconfig` | 0 |
| retrospective | the retrospective Agent Skill | shipped | 144 | a CBC Run looking back | 1 ADR, 1 CBC Run |
| retrospective | the apply-retrospective Agent Skill | shipped | 156 | applying the look back before Release | 1 ADR, 1 CBC Run |
| shapes | the shapes-lifecycle Agent Rule | shipped | 119 | how an Output Shape is born and changed | 3 ADRs, 1 CBC Run |
| shapes | 4 Output Shapes, `delivery/method/.claude/shapes/` | shipped | 688 | Evidence Test, Enemy Collision Kill, Invariant Slice Entry, Invariant Slice Record | 0 |
| visual-comparison | the visual-comparison Agent Skill | both | 161 + 162 | how a structure is shown | 3 ADRs |
| writing | the writing Agent Rule | both | 145 + 129 | how a text reads | 9 ADRs, 1 CBC Run |
| writing | the Glossary Names, container, method and stack | shipped | 461 | the shared Names, the concept's and the stack's | 0 |
| concept | the cbc-framing Agent Skill, with references | shipped | 1354 | framing a new system | 1 ADR, 3 CBC Runs |
| concept | the cbc-slice Agent Skill, with references | shipped | 968 | building one Invariant Slice | 0 |
| concept | the cbc-bootstrap Agent Skill, with references | shipped | 1431 | the first running skeleton, Spring and Postgres | 2 ADRs |
| concept | the infra-establish Agent Skill, with references | shipped | 1033 | the Runtime Ground | 2 ADRs |
| concept | the infra-serve Agent Skill | shipped | 90 | changing the Runtime Ground later | 0 |
| change, in keeping knowledge | the read-copy-changes Agent Skill, with its understanding | ours | 152 | reading one Backend Repo's Copy Changes | 3 ADRs |
| change, in keeping knowledge | the judge-copy-changes Agent Skill, with its understanding | ours | 168 | judging a Repo Reading, line by line | 3 ADRs |
| change, in keeping knowledge | the deliver-the-kit-update Agent Skill, with its understanding | ours | 135 | making a Kit Update for one Backend Repo | 3 ADRs |
| defined terms, in keeping knowledge | the defined-terms Agent Rule, with its understanding | ours | 109 | the Defined Terms of a text under `knowledge/` | 4 ADRs |
| change, in CBC backend design | change-a-kit-copy, `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/` | Backend Kit | 50 | every change to a Kit Copy | 1 ADR |
| change, in CBC backend design | take-the-kit-update, `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/take-the-kit-update/` | Backend Kit | 65 | taking a Kit Update into the Kit Copies | 1 ADR |
| defined terms, in CBC backend design | the Backend Kit's Defined Terms, `knowledge/adapted-cases/cbc-backend-design/defined-terms/` | Backend Kit | 27 | every Defined Term a Kit Copy uses | 1 ADR |

## 2. The ideas behind them

**Points at:** the other ideas the text names, by path or name. A
mention, not yet a need: the map's *Needs first* decides which are
needs (§9). **Lessons:** *Its story* lines, then ADRs cited.

| Idea | Its text | Lines | Points at | Lessons |
|---|---|---|---|---|
| agent-arrangement | `docs/conventions/agent-arrangement/` | 604 | 10: agent, commit-messages, conventions, exchange, facts-in-sync, idea-to-output, project-recording, repo-hygiene, shapes, writing | 6, 9 |
| commit-messages | `docs/conventions/commit-messages/` | 148 | 5: agent, agent-arrangement, commit-plan, project-recording, tiers | 3, 5 |
| commit-plan | `docs/conventions/commit-plan/` | 194 | 5: agent, commit-messages, facts-in-sync, project-recording, tiers | 11, 5 |
| conventions | `docs/conventions/conventions/` | 377 | 8: agent, agent-arrangement, concept, exchange, facts-in-sync, idea-to-output, project-recording, shapes | 8, 7 |
| exchange | `docs/conventions/exchange/` | 606 | 11: agent, agent-arrangement, commit-messages, commit-plan, concept, conventions, facts-in-sync, idea-to-output, project-recording, shapes, tiers | 17, 6 |
| facts-in-sync | `docs/conventions/facts-in-sync/` | 414 | 10: agent, agent-arrangement, commit-messages, commit-plan, concept, conventions, exchange, idea-to-output, project-recording, writing | 7, 12 |
| project-recording | `docs/conventions/project-recording/` | 909 | 10: agent, agent-arrangement, commit-messages, commit-plan, concept, conventions, exchange, facts-in-sync, retrospective, writing | 5, 13 |
| repo-hygiene | `docs/conventions/repo-hygiene/` | 120 | 5: agent, agent-arrangement, exchange, project-recording, tiers | 2, 2 |
| retrospective | `docs/conventions/retrospective/` | 195 | 8: agent, agent-arrangement, commit-plan, exchange, project-recording, shapes, tiers, writing | 4, 1 |
| shapes | `docs/conventions/shapes/` | 345 | 4: agent, agent-arrangement, exchange, tiers | 7, 4 |
| visual-comparison | `docs/conventions/visual-comparison/` | 113 | 3: agent, commit-plan, tiers | 3, 6 |
| writing | `docs/conventions/writing/` | 227 | 9: agent, agent-arrangement, commit-messages, conventions, defined-terms-in-keeping-knowledge, facts-in-sync, project-recording, shapes, tiers | 3, 6 |
| the agent model | `docs/models/agent.md` | 459 | 2: idea-to-output, tiers | 0, 3 |
| the idea-to-output model | `docs/models/idea-to-output.md` | 205 | 4: agent, concept, facts-in-sync, tiers | 0, 3 |
| the tiers model | `docs/models/tiers.md` | 173 | 3: agent, exchange, idea-to-output | 1, 4 |
| the concept | `concept/`, 5 chapters | 507 | none | 0, 0 |
| change | `knowledge/backbone-ideas/change.md` | 96 | 3: change-in-cbc-backend-design, change-in-keeping-knowledge, layers-of-knowledge | 0, 2 |
| defined-terms | `knowledge/backbone-ideas/defined-terms.md` | 70 | 4: defined-terms-in-cbc-backend-design, defined-terms-in-keeping-knowledge, layers-of-knowledge, writing | 0, 2 |
| layers-of-knowledge | `knowledge/backbone-ideas/layers-of-knowledge.md` | 130 | 3: change, defined-terms, layers-of-knowledge-in-keeping-knowledge | 0, 2 |
| change-in-cbc-backend-design | `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` | 90 | 6: agent, change, change-in-keeping-knowledge, layers-of-knowledge, layers-of-knowledge-in-keeping-knowledge, project-recording | 0, 3 |
| defined-terms-in-cbc-backend-design | `knowledge/problem-domain-ideas/cbc-backend-design/defined-terms-in-cbc-backend-design.md` | 63 | 5: change, change-in-keeping-knowledge, defined-terms, layers-of-knowledge, layers-of-knowledge-in-keeping-knowledge | 0, 2 |
| change-in-keeping-knowledge | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` | 311 | 8: change, change-in-cbc-backend-design, commit-messages, defined-terms, exchange, layers-of-knowledge, layers-of-knowledge-in-keeping-knowledge, project-recording | 0, 2 |
| defined-terms-in-keeping-knowledge | `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` | 85 | 6: change, defined-terms, facts-in-sync, layers-of-knowledge, layers-of-knowledge-in-keeping-knowledge, writing | 0, 2 |
| layers-of-knowledge-in-keeping-knowledge | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` | 215 | 12: agent, agent-arrangement, change, change-in-cbc-backend-design, change-in-keeping-knowledge, concept, defined-terms, defined-terms-in-cbc-backend-design, defined-terms-in-keeping-knowledge, layers-of-knowledge, project-recording, tiers | 0, 3 |

## 3. Ideas with no home

Six Work Approaches name no idea. The idea behind each is written
only inside the Work Approach itself.

| Idea | Work Approach | Seat | Lines | Lessons |
|---|---|---|---|---|
| trying a new way of working | the approach-drafting Approach on Trial | both | 141 + 141 | 1 CBC Run |
| trying a new way of working | the approach-evaluation Approach on Trial | ours | 164 | 3 ADRs |
| bringing old text up to a new rule | the refinement Approach on Trial | ours | 437 | 4 ADRs, 2 CBC Runs |
| a CBC Run on full auto | the auto-run Approach on Trial | ours | 155 | 2 ADRs, 17 CBC Runs |
| an Idea Model taking what it borrows | the model-placing Approach on Trial | ours | 111 | 2 ADRs |
| making a CBC Run Birth | the Pure Seed, `delivery/installs/pure-seed.md` | ours | 338 | 7 ADRs |

Some ideas have a home, and no Work Approach stands on them:

- **Conversation Memory:** `TODO-CONVERSATION-MEMORY.md`, on trial.
- **The 3 Idea Models:** `docs/models/`.
- **The 3 Backbone Ideas:** `knowledge/backbone-ideas/`. A Work
  Approach stands on a Problem Domain Idea, which adapts one.
- **Layers of knowledge, in keeping knowledge:**
  `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`.

## 4. What the table shows

1. **Every manual points at the agent model, and 8 of 12 at the tiers
   model.** The manual's form asks for it: *Why it arrives this
   way* rests on the agent model, and *The seats* on the tiers. So
   these come from the form, not from the ideas.
2. **The concept and its Work Approaches point at nothing:** 507 lines
   of concept and 4,876 in its five Agent Skills. The largest part is
   independent.
3. **The lessons gather in 3 ideas:** exchange, 17 *Its story* lines;
   commit-plan, 11; conventions, 8. These are where a rewrite loses
   most if it skips them.
4. **6 Work Approaches exist twice,** ours and the shipped one, 1,711
   lines in both copies: commit-messages, commit-plan,
   visual-comparison, one-home, writing and approach-drafting.
5. **6 Work Approaches have no written idea,** 1,487 lines in all.
6. **Part of the rewrite already stands:** 8 ideas under
   `knowledge/`, 1,060 lines, and 7 Work Approaches built on 4 of
   them, 706 lines. Each is at its layer by its path
   (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
   §3.5, *Where each layer is kept*).
7. **The most pointed-at sections are the `knowledge/` texts' §1,**
   *Its Defined Terms*: 4 sections, 163 pointers, from the texts that
   borrow their Defined Terms.

## 6. The shared facts

A shared fact is a section that 5 or more pointers from other files
name. 790 pointers name 216 sections. 41 sections take 5 or more,
452 pointers in all. What the rewrite does with each is decided
where its text is mapped (§9).

| Pointers | Files | Section |
|---|---|---|
| 63 | 15 | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| 52 | 9 | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| 40 | 12 | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| 19 | 7 | facts-in-sync §4, *A Canonical Description's rule* |
| 17 | 13 | agent-arrangement §5.6, *Rules files* |
| 17 | 13 | conventions §1.3, *The Foundation Line* |
| 13 | 8 | writing §2, *Why each rule* |
| 11 | 11 | agent-arrangement §3.1, *`.claude/skills/`* |
| 11 | 10 | commit-messages §2.3, *The `agent` scope* |
| 10 | 9 | exchange §3.2, *What goes* |
| 10 | 6 | `knowledge/backbone-ideas/change.md` §4, *The arrows* |
| 8 | 7 | `delivery/container/.claude/rules/shapes-lifecycle.md` §3, *A difference at the close* |
| 8 | 7 | exchange §3.4, *One group per file* |
| 8 | 5 | the idea-to-output model §2, *The kinds* |
| 8 | 8 | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| 8 | 6 | `knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The Problem Domain layer* |
| 7 | 6 | commit-messages §2.1, *Conventional Commits* |
| 7 | 5 | commit-messages §2.4, *Commit on the word* |
| 7 | 6 | exchange §2.2, *The CBC Run* |
| 7 | 6 | project-recording §13, *The records table* |
| 7 | 7 | project-recording §2.1, *What a plan is* |
| 7 | 3 | the agent model §4.1, *Ambient Channel* |
| 6 | 1 | `TODO-CONVERSATION-MEMORY.md` §31, *Keeping what we know true*, in git at `60f692d`* |
| 6 | 5 | agent-arrangement §2.4, *How the Entry File is written* |
| 6 | 5 | agent-arrangement §3.4, *`.claude/decisions.md`* |
| 6 | 4 | exchange §1, *What cannot change* |
| 6 | 4 | exchange §3.3, *A group's place in the tree* |
| 6 | 4 | exchange §5.8, *Agent Skill Templates* |
| 6 | 5 | exchange §6.3, *The CBC Run Reading* |
| 6 | 5 | the agent model §8, *Choosing a channel* |
| 6 | 5 | the idea-to-output model §3.1, *The four Chain Links* |
| 6 | 4 | the tiers model §2.2, *Concept Repos* |
| 6 | 4 | the tiers model §3.5, *What holds on every flow* |
| 6 | 2 | `temp/common-ground/common-ground-problem.md` §4, *What goes wrong* |
| 5 | 4 | conventions §2, *The Convention Manual* |
| 5 | 5 | conventions §2.4, *The seats* |
| 5 | 4 | exchange §4, *The Delivery Take* |
| 5 | 5 | exchange §6, *Up from the CBC Run* |
| 5 | 4 | exchange §6.5, *Verdicts* |
| 5 | 5 | the agent model §4.2, *Pulled Channel* |
| 5 | 4 | the idea-to-output model §4.2, *The upward direction* |

## 7. How it was built

Counted at `491e673e`, by script.

- **Work Approaches:** every Agent Skill, Agent Rule, Approach on Trial
  and Output Shape under a `.claude/` outside `temp/`, the playbook,
  the Pure Seed, both Entry Files, the Record Stubs, the repo files
  and their templates, the Glossary Names, and the Backend Kit's files
  under `knowledge/adapted-cases/`. An Agent Skill counts with its
  `references/` and `templates/`. An Adapted Understanding Text counts
  with the Instruction Text it stands under.
- **The idea behind each:** its Foundation Line, or its header's
  "What it stands on". "Practice, checked against concept v1" counts
  as the concept. The repo files carry no Foundation Line; they count
  under repo-hygiene, whose manual describes them.
- **Points at:** another idea's path or name in the text: a manual's
  path or "the <name> convention", an Idea Model's path or "the <name>
  model", `concept/` or "concept v1", a `knowledge/` text's path.
- **Lessons:** distinct ADR numbers, mentions of "CBC Run" followed by
  a digit, and *Its story* lines. A lesson told without these is not
  counted.
- **Shared facts:** a path to another file followed by § and a number,
  in Living Text outside `temp/`. A pointer by title alone, or inside
  its own file, is not counted. A shipped copy's pointers count with
  ours, and a path written as a CBC Run sees it counts at its place
  under `delivery/`.
- **Not read:** what each text says. A row says what a text is for,
  from its own opening line, not whether that is true.
- **Against 2026-11-03:** the same scripts, run at `ee8f3b0`, give
  §2's rows exactly and §6's 31 sections with their counts; their
  total there is 493 pointers on 170 sections, against the 466 on 151
  then counted. Changed since: the Glossary Names take the container's
  shared Names, the repo files count whole in both seats, and the
  Backend Kit's files and the texts on `knowledge/` ideas are new.

## 8. Items from TODO

Each TODO item here lands with a text, and is decided when that text
is rewritten. Each left `TODO.md` on 2026-11-26; its words are in git
at `f83d146b:TODO.md`, at the line given, and its Conversation Memory
section, if any, at `f83d146b:TODO-CONVERSATION-MEMORY.md`.

| Item | Lands with | Line | Conversation Memory |
|---|---|---|---|
| Sweep the drafts for words that read as walking commits | each draft that holds them, found by grep when the drafts are mapped | 93 | — |
| The problem file's next pass: §6 and §8, Failure Case 15, the "project-agnostic" sweep, §2.2's "middle level" | `temp/common-ground/common-ground-problem.md` | 103 | — |
| Whether the rewrite takes the Approaches on Trial and check scripts the CBC Runs wrote | the Backend Kit's parts for birth, checks and release | 190 | — |
| How much a CBC Run records against what it builds | the playbook, `delivery/fills/cbc-run-pure-playbook.md`; the Record Stubs hold little of it (records' Plan Step, 2026-11-27) | 205 | — |
| How a Work Approach and an Output Shape divide an output | the shapes manual, `docs/conventions/shapes/`, decided with the next row | 701 | §2, *How an approach and a shape divide an output* |
| Whether our own forms become Output Shapes, and whether an Output Shape's part can be optional | the shapes manual, and the forms in `.claude/rules/convention-manual.md` and `.claude/rules/exchange-reading.md` | 927 | §3, *Layouts as shapes* |
| Whether the approach-drafting Approach on Trial becomes a convention | `.claude/approaches-on-trial/approach-drafting.md` | 740 | — |
| Whether writing rule 10 reaches unnumbered headings | the writing manual, `docs/conventions/writing/` | 995 | — |
| A Fact Reference from the method's texts to each part of a concept chapter they use | the method's texts, `delivery/method/`, and the chapters, `concept/` | 1092 | §6, *The method's plain rewrite: `cbc-slice`'s opening* |
| Sort `docs/baselines/` by kind, read with care: a wrong move destroys a measurement | `docs/baselines/` | 1164 | — |
| Which ideas here are Idea Models | decided once, with which ideas are Backbone Ideas (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §5, *Open questions*, question 4); decided: §10, QUESTION-7 | 1175 | §29, *Two checks on text kept true* |

## 9. Every text

One line for each file of Living Text at `491e673e`, by `git ls-files`.
History is not mapped: the devlog's entries and the closed ADRs. A
record whose entries are history is mapped by its form. A pair, ours
and the shipped copy, takes one line. **Parts:** what the text holds.
**Layer:** where each part goes
(`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
§3.5, *Where each layer is kept*), or the question that keeps it open;
"in place" when the text already sits at its layer, by its path. A
draft in `temp/` is no layer's: its Layer says what the rewrite reads
it for, and nothing goes before the rewrite decides.
**Needs first:** the texts rewritten before it, or none.

| Text | Parts | Layer | Needs first |
|---|---|---|---|
| `.claude/approaches-on-trial/approach-drafting.md` and `delivery/container/.claude/approaches-on-trial/approach-drafting.md` | trying a new way of working, its idea written only here (§3); the stages | idea: 1 or 2, with §8's approach-drafting row; ours: 4; the CBC Run's copy: 3 | none |
| `.claude/approaches-on-trial/approach-evaluation.md` | trying a new way of working: judging an Approach on Trial and placing its pieces | 4 | `.claude/approaches-on-trial/approach-drafting.md` |
| `.claude/approaches-on-trial/auto-run.md` | a CBC Run on full auto: preparing it and its birth | 4, on trial; TODO's "Evaluate the auto-run Approach on Trial" waits | `delivery/installs/pure-seed.md` |
| `.claude/approaches-on-trial/model-placing.md` | an Idea Model taking what it borrows from a text below it | goes (QUESTION-5): Change's arrow *lesson* does its job | none |
| `.claude/approaches-on-trial/refinement.md` | bringing old text up to a new rule: Refinement Rounds, Finding Kinds, the last read | idea: 1 or 2; the stages: 4 | none |
| `.claude/decisions.md` and `delivery/container/.claude/decisions.md`, its form | the Decisions Log's form; the entries are history | form: 4, open (QUESTION-1) | `docs/conventions/agent-arrangement/` |
| `.claude/rules/convention-manual.md` | the manual's form, as an Agent Rule | QUESTION-4; it goes with the conventions manual (QUESTION-5) | `docs/conventions/conventions/` |
| `.claude/rules/defined-terms.md` | our Defined Terms: the Instruction Text, a Paths Rule | 4, in place | none |
| `.claude/rules/exchange-reading.md` | the CBC Run Reading's form | 4: each part to our change Adapted Case in place that holds it, the rest beside them | `docs/conventions/exchange/` |
| `.claude/rules/foundation-check.md` | the check before a commit | 4 | `docs/conventions/facts-in-sync/` |
| `.claude/rules/one-home.md` and `delivery/container/.claude/rules/one-home.md` | where a fact lives, as an Agent Rule | ours: 4; the CBC Run's copy: 3, its instruction side | `docs/conventions/facts-in-sync/` |
| `.claude/rules/working-a-reading.md` | working a CBC Run Reading's list | 4: each part to our change Adapted Case in place that holds it, the rest beside them; the lessons in §7 of the three CBC Run Readings land here | `docs/conventions/exchange/` |
| `.claude/rules/writing.md` and `delivery/container/.claude/rules/writing.md` | how a text reads, as an Agent Rule | ours: 4; the CBC Run's copy: 3, its instruction side; rule 9: QUESTION-2 | `docs/conventions/writing/` |
| `.claude/skills/commit-messages/SKILL.md` and `delivery/container/.claude/skills/commit-messages/SKILL.md` | writing a commit message | ours: 4; the CBC Run's copy: 3, its instruction side | `docs/conventions/commit-messages/` |
| `.claude/skills/commit-plan/SKILL.md` and `delivery/container/.claude/skills/commit-plan/SKILL.md` | work of more than one commit | ours: 4; the CBC Run's copy: 3, its instruction side | `docs/conventions/commit-plan/` |
| `.claude/skills/deliver-the-kit-update/SKILL.md` | our Deliver the Kit Update: the Instruction Text, an Agent Skill | 4, in place | none |
| `.claude/skills/exchange-deliver/SKILL.md` | delivering to a CBC Run | 4: each part to our change Adapted Case in place that holds it, the rest beside them; a later update to a CBC Run born before names the renames in its Delivery Note, once | `docs/conventions/exchange/` |
| `.claude/skills/exchange-read/SKILL.md` | reading a CBC Run | 4: each part to our change Adapted Case in place that holds it, the rest beside them; the lessons in §7 of the three CBC Run Readings land here | `docs/conventions/exchange/` |
| `.claude/skills/judge-copy-changes/SKILL.md` | our Judge Copy Changes: the Instruction Text, an Agent Skill | 4, in place | none |
| `.claude/skills/read-copy-changes/SKILL.md` | our Read Copy Changes: the Instruction Text, an Agent Skill | 4, in place | none |
| `.claude/skills/visual-comparison/SKILL.md` and `delivery/container/.claude/skills/visual-comparison/SKILL.md` | how a structure is shown | ours: 4; the CBC Run's copy: 3, its instruction side | `docs/conventions/visual-comparison/` |
| `.claude/understanding/defined-terms.md` | our Defined Terms: the Adapted Understanding Text | 4, in place | none |
| `.claude/understanding/deliver-the-kit-update.md` | our Deliver the Kit Update: the Adapted Understanding Text | 4, in place | none |
| `.claude/understanding/judge-copy-changes.md` | our Judge Copy Changes: the Adapted Understanding Text | 4, in place | none |
| `.claude/understanding/read-copy-changes.md` | our Read Copy Changes: the Adapted Understanding Text | 4, in place | none |
| `.editorconfig` and `delivery/container/.editorconfig` | the Hygiene Base's file | ours: 4; the CBC Run's copy: 3, its instruction side | `docs/conventions/repo-hygiene/` |
| `.gitattributes` and `delivery/container/.gitattributes` | the Hygiene Base's file | ours: 4; the CBC Run's copy: 3, its instruction side | `docs/conventions/repo-hygiene/` |
| `.gitignore` and `delivery/container/.gitignore` | the Hygiene Base's file | ours: 4; the CBC Run's copy: 3, its instruction side | `docs/conventions/repo-hygiene/` |
| `ARCHITECTURE.md` | its form; how the repo's parts tie, and the table of CBC Runs | form: 4, open (QUESTION-1); the content: 4, rewritten last | every other text: it says what stands |
| `CHANGELOG.md`, its form | its form, for those who pin a concept version; the entries are history | form: 4, open (QUESTION-1); what is versioned: open (QUESTION-3) | `docs/conventions/project-recording/`; `concept/` |
| `CLAUDE.local.md` | the reviewer's own rules for working here | 4, in place | none |
| `CLAUDE.md` | our Entry File: what this repo is, the records table, the local rules | 4; the records table: QUESTION-1 | `docs/conventions/agent-arrangement/`; `docs/conventions/project-recording/` |
| `PLAN.md` | the legend and the Plan Step Form; the open Plan Step, this repo's work | form: 4, open (QUESTION-1); the Plan Step: 4, in place | `docs/conventions/project-recording/`; the playbook, `delivery/fills/cbc-run-pure-playbook.md` |
| `README.md` | its form; what this repo is, for a reader from outside | form: 4, open (QUESTION-1); the content: 4, rewritten last | every other text: it says what stands |
| `TODO-CONVERSATION-MEMORY.md`, its form | its form, on trial; the sections are history | form: 4, open (QUESTION-1); whether it stays: TODO's "Judge the Conversation Memory trial" | TODO's "Judge the Conversation Memory trial" |
| `TODO.md` | its form, in the header comment; the items, this repo's work | form: 4, open (QUESTION-1); the items: 4, in place | `docs/conventions/project-recording/` |
| `concept/00-cbc.md` | CBC itself: the CBC Inversion, the two components, the shape of the work, how it fails | 1 and 2: CBC design, and CBC design in CBC backend design, by TODO's item that splits the concept, its labels first; the lines that name the concept in the Backend Kit's Record Stubs and its Entry File, kept as they are until then (records' Plan Step, 2026-11-27; the agent-arrangement manual's, 2026-11-27) | none |
| `concept/01-layered-system.md` | the Layered System, its five layers | 1 and 2: CBC design, and CBC design in CBC backend design, by TODO's item that splits the concept, its labels first | none |
| `concept/02-guarantees-and-walls.md` | System Guarantees and Structural Walls, the Falsifiable Promise | 1 and 2: CBC design, and CBC design in CBC backend design, by TODO's item that splits the concept, its labels first | none |
| `concept/03-cbc-framing.md` | CBC Framing: paper first, the derivation order, what it produces | 1 and 2: CBC design, and CBC design in CBC backend design, by TODO's item that splits the concept, its labels first | none |
| `concept/04-cbc-slice.md` | the Invariant Slice: its four phases, the proof standard | 1 and 2: CBC design, and CBC design in CBC backend design, by TODO's item that splits the concept, its labels first | none |
| `delivery/README.md` | a Local Map: how the delivery's groups land in a CBC Run | 4; goes with the delivery it maps | every text under `delivery/` |
| `delivery/container/.claude/CLAUDE.md` | the CBC Run's Entry File | 3, the Backend Kit's | `docs/conventions/agent-arrangement/`; `docs/conventions/project-recording/` |
| `delivery/container/.claude/rules/delivered-copies.md` | taking a delivery; editing a copy | 3: each part to the Backend Kit's change Adapted Case in place that holds it, the rest beside them | `docs/conventions/exchange/` |
| `delivery/container/.claude/rules/shapes-lifecycle.md` | how an Output Shape is born and changed | 3, the Backend Kit's | `docs/conventions/shapes/` |
| `delivery/container/.claude/skills/apply-retrospective/SKILL.md` | applying the look back before Release | 3, the Backend Kit's | `docs/conventions/retrospective/` |
| `delivery/container/.claude/skills/retrospective/SKILL.md` | a CBC Run looking back | 3, the Backend Kit's | `docs/conventions/retrospective/` |
| `delivery/container/ARCHITECTURE.md` | the Record Stub for ARCHITECTURE | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/` |
| `delivery/container/CHANGELOG.md` | the Record Stub for the changelog | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/` |
| `delivery/container/PLAN.md` | the Record Stub for the plan | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/`; the playbook |
| `delivery/container/README.md` | the Record Stub for the README | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/` |
| `delivery/container/TODO.md` | the Record Stub for TODO | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/` |
| `delivery/container/devlog/devlog.md` | the Record Stub for the devlog | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/` |
| `delivery/container/docs/adr/0001-record-architecture-decisions.md` | the first ADR, and the ADR's form | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/` |
| `delivery/container/docs/glossary.md` | the Record Stub for a CBC Run's own glossary | 3, the Backend Kit's record forms; QUESTION-1; QUESTION-2 | `docs/conventions/project-recording/`; `docs/conventions/writing/` |
| `delivery/container/docs/glossary/container.md` | the shared Glossary Names | 3, the Backend Kit's Defined Terms, in place: QUESTION-2 | `docs/conventions/writing/` |
| `delivery/container/temp/README.md` | the Record Stub for `temp/` | 3, the Backend Kit's record forms; QUESTION-1 | `docs/conventions/project-recording/` |
| `delivery/fills/cbc-run-pure-playbook.md` | a CBC Run's Plan Steps from birth to Release, and the Plan Step Form | 3, the Backend Kit's; the Plan Step Form: QUESTION-1; one item waits here (§8); *At the gate* lands here, as an Agent Skill or an item of *At the close*, its why in `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` §2 (the Agent Model's Plan Step, 2026-11-27) | `docs/conventions/project-recording/`; `concept/` |
| `delivery/installs/pure-seed.md` | making a CBC Run Birth: its idea, written only here (§3), and its steps | idea: 1 or 2; the steps: 4 | `docs/conventions/exchange/`; `docs/conventions/repo-hygiene/` |
| `delivery/method/.claude/shapes/evidence-test.md` | the Evidence Test Shape | 3, the Backend Kit's | `docs/conventions/shapes/`; `concept/` |
| `delivery/method/.claude/shapes/kill.md` | the Enemy Collision Kill Shape | 3, the Backend Kit's | `docs/conventions/shapes/`; `concept/` |
| `delivery/method/.claude/shapes/registry-entry.md` | the Invariant Slice Entry Shape | 3, the Backend Kit's | `docs/conventions/shapes/`; `concept/` |
| `delivery/method/.claude/shapes/slice-record.md` | the Invariant Slice Record Shape | 3, the Backend Kit's | `docs/conventions/shapes/`; `concept/` |
| `delivery/method/.claude/skills/cbc-framing/SKILL.md` | the cbc-framing Agent Skill: its stages | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept | `concept/` |
| `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` | the cbc-framing Agent Skill: a reference, cbc-framing-workflow.md | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept | `concept/` |
| `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md` | the cbc-framing Agent Skill: a reference, the-whole-system-in-plain.md | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept | `concept/` |
| `delivery/method/.claude/skills/cbc-framing/references/worked-example.md` | the cbc-framing Agent Skill: a reference, worked-example.md | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept; kept identical with its twin in the other Agent Skill | `concept/` |
| `delivery/method/.claude/skills/cbc-framing/templates/registry.md` | the cbc-framing Agent Skill: an Agent Skill Template, registry.md | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept | `concept/` |
| `delivery/method/.claude/skills/cbc-slice/SKILL.md` | the cbc-slice Agent Skill: its stages | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept | `concept/` |
| `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` | the cbc-slice Agent Skill: a reference, cbc-slice-workflow.md | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept | `concept/` |
| `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md` | the cbc-slice Agent Skill: a reference, system-readiness.md | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept | `concept/` |
| `delivery/method/.claude/skills/cbc-slice/references/worked-example.md` | the cbc-slice Agent Skill: a reference, worked-example.md | 3, the Backend Kit's CBC system design, by TODO's item that splits the concept; kept identical with its twin in the other Agent Skill | `concept/` |
| `delivery/method/docs/glossary/method.md` | the concept's and the method's Glossary Names | 3, the Backend Kit's Defined Terms, in place: QUESTION-2 | `concept/` |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` | the cbc-bootstrap Agent Skill: its stages | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md` | the cbc-bootstrap Agent Skill: a reference, app-structure.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` | the cbc-bootstrap Agent Skill: a reference, spring-boot-walkthrough.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` | the cbc-bootstrap Agent Skill: a reference, spring-harness-reference.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-pom-convention.md` | the cbc-bootstrap Agent Skill: a reference, spring-pom-convention.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/application.yaml` | the cbc-bootstrap Agent Skill: an Agent Skill Template, application.yaml | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/readme-run-test.md` | the cbc-bootstrap Agent Skill: an Agent Skill Template, readme-run-test.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/testcontainers.properties` | the cbc-bootstrap Agent Skill: an Agent Skill Template, testcontainers.properties | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` | the infra-establish Agent Skill: its stages | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` | the infra-establish Agent Skill: a reference, establishment-walk.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md` | the infra-establish Agent Skill: a reference, postgres-role-split.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md` | the infra-establish Agent Skill: a reference, postgres-setup-walkthrough.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/.env.example` | the infra-establish Agent Skill: an Agent Skill Template, .env.example | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/bootstrap.sql` | the infra-establish Agent Skill: an Agent Skill Template, bootstrap.sql | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/compose.yaml` | the infra-establish Agent Skill: an Agent Skill Template, compose.yaml | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/flyway.conf` | the infra-establish Agent Skill: an Agent Skill Template, flyway.conf | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/readme-prerequisites.md` | the infra-establish Agent Skill: an Agent Skill Template, readme-prerequisites.md | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/verify-database-model.sql` | the infra-establish Agent Skill: an Agent Skill Template, verify-database-model.sql | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` | the infra-serve Agent Skill: its stages | 3, by TODO's item that splits the concept, its question whether the stack is only more input to the backend case | `concept/`; the method's Agent Skills |
| `delivery/spring-postgres/docs/glossary/stack.md` | the stack's Glossary Names | 3, the Backend Kit's Defined Terms, in place: QUESTION-2 | `concept/` |
| `devlog/README.md` | the devlog's form; the entries are history | form: 4, open (QUESTION-1) | `docs/conventions/project-recording/` |
| `docs/adr/README.md` | the ADR's form; the ADRs are history | form: 4, open (QUESTION-1) | `docs/conventions/project-recording/` |
| `docs/baselines/cbc-derived-claude-walk1.md` | trial evidence: the first walked birth's derived `CLAUDE.md`, blind | 4, in place; moved only by §8's baselines row; it waits on TODO's "Read the frozen CLAUDE template's stance bullets against a full CBC Run's derived Entry File" | none |
| `docs/baselines/cbc-run-pure-playbook-v2.md` | a held baseline: the playbook frozen at v2, for the per-step reading of the gates experiment; no Living Text names it | 4, in place; moved only by §8's baselines row, which decides whether it stays | none |
| `docs/baselines/cbc-startup-snippet.md` | a held baseline: the startup snippet, its comparison used up on 2026-09-04 (ADR-0014) | 4, in place; moved only by §8's baselines row, which decides whether it stays | none |
| `docs/baselines/claude-md-template-v1.md` | a held baseline: the `CLAUDE.md` template, frozen 2026-09-06, blind | 4, in place; moved only by §8's baselines row; it waits on TODO's "Read the frozen CLAUDE template's stance bullets against a full CBC Run's derived Entry File" | none |
| `docs/baselines/spring-slice-reference.md` | held material: one Invariant Slice's Spring shapes, opened once, at a CBC Run's Release | 3, the Backend Kit's, held: never shipped at birth; moved only by §8's baselines row | `concept/`; the cbc-slice Agent Skill |
| `docs/conventions/README.md` | a Local Map: the order the conventions act in | 4; goes with the manuals it maps | every manual |
| `docs/conventions/agent-arrangement/README.md` | the idea: §1 to §4, an arrangement, the Entry File, `.claude/`; §5, the Claude Code Tool Binding; both seats; the form's sections | idea: 1 or 2 (§8, the Idea Models row); §5: QUESTION-6; the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4 | `docs/models/agent.md` |
| `docs/conventions/commit-messages/README.md` | the idea: §1, §2; §3, our habit; the seats, alike; the form's sections | idea: 1 or 2 (§8, the Idea Models row); §3: 4; the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4 | `docs/conventions/agent-arrangement/`, for §2.3 |
| `docs/conventions/commit-plan/README.md` | the idea: §1, §2; the seats, alike; the form's sections | idea: 1 or 2 (§8, the Idea Models row); the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4 | `docs/conventions/commit-messages/` |
| `docs/conventions/conventions/README.md` | how a Work Approach is written, §1; the manual's form, §2; adding a convention, §3 | goes (QUESTION-5): §1, the new idea of how instructions are written; §2: QUESTION-4; §3: Change | none: the layers, in place |
| `docs/conventions/exchange/README.md` | the idea: §1, §2; down to a CBC Run, §3, §4; editing a copy, §5; up from a CBC Run, §6; the body by seat; the form's sections | §1, §2: 1 or 2 (§8, the Idea Models row); §3 to §6: each to the change text in place that holds it, at layers 2 to 4, the rest beside them; the form's sections: QUESTION-4; the lines that name the exchange in the Backend Kit's Record Stubs, its scratch space's README and its Entry File, kept as they are until then (records' Plan Step, 2026-11-27; the agent-arrangement manual's, 2026-11-27) | `docs/models/tiers.md`; `docs/conventions/facts-in-sync/` |
| `docs/conventions/facts-in-sync/README.md` | the idea: §1 to §5, one home, the Fact Reference, a Canonical Description's rule, a disagreement; both seats; the form's sections | idea: 1 or 2 (§8, the Idea Models row); the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4 | `docs/models/idea-to-output.md`, for §4 |
| `docs/conventions/project-recording/README.md` | the idea of records: §1, §11 to §13; each record, §2 to §8, and its form; the playbook, §9; supporting records, §10; Conversation Memory, §14; both seats; the form's sections | idea: 1 or 2 (§8, the Idea Models row); each record's form: QUESTION-1; §14: 4, on trial; the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4 | none |
| `docs/conventions/repo-hygiene/README.md` | the idea: §1 to §3, the three files, the template layers, the rules; the seats; the form's sections | idea: 1 or 2 (§8, the Idea Models row); the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4 | none |
| `docs/conventions/repo-hygiene/templates/java-spring/editorconfig.part` | the Java and Spring template layer | 3 | `docs/conventions/repo-hygiene/` |
| `docs/conventions/repo-hygiene/templates/java-spring/gitattributes.part` | the Java and Spring template layer | 3 | `docs/conventions/repo-hygiene/` |
| `docs/conventions/repo-hygiene/templates/java-spring/gitignore.part` | the Java and Spring template layer | 3 | `docs/conventions/repo-hygiene/` |
| `docs/conventions/retrospective/README.md` | the idea: §1 to §4, the two Plan Steps, deciding, applying, `RETRO.md`; both seats; the form's sections | idea: 1 or 2 (§8, the Idea Models row); the CBC Run's seat: 3; ours: 4, on trial (TODO's "Run this repo's retrospective, on trial"); the form's sections: QUESTION-4 | `docs/conventions/project-recording/` |
| `docs/conventions/shapes/README.md` | the idea: §1 to §5, what an Output Shape is and is not, where it lives, between repos, using it; both seats; the form's sections | idea: 1 or 2 (§8, the Idea Models row); the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4; two items wait here (§8) | `docs/models/tiers.md`, for §4.1 |
| `docs/conventions/visual-comparison/README.md` | the idea: §1, §2; the seats, alike; the form's sections | idea: 1 or 2 (§8, the Idea Models row); the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4 | none |
| `docs/conventions/writing/README.md` | the idea: §1, §2, what it governs, why each rule; the seats; the form's sections | idea: 1 or 2 (§8, the Idea Models row); rule 9: QUESTION-2; the CBC Run's seat: 3; ours: 4; the form's sections: QUESTION-4; one item waits here (§8) | `docs/conventions/facts-in-sync/`, for §1.1 |
| `docs/glossary.md` | its form; the Glossary Names, each pointing at its home | open (QUESTION-2) | `docs/conventions/writing/`; each text a Name points at |
| `docs/models/agent.md` | how an agent works: §1 to §8, §11, §12; where each convention lands, §9; the Tool Bindings, §10 | §1 to §8, §11, §12: 1 or 2 (§8, the Idea Models row); §9: 4; §10: QUESTION-6 | none |
| `docs/models/idea-to-output.md` | the chain, its kinds and links, the two directions, a convention: §1 to §8 | goes (QUESTION-5): §1, §3.1, §3.2, the layers document; §4, Change; §3.3, the one-home idea; §6.2, the new idea of how instructions are written; the rest by its subject | none: the layers, in place |
| `docs/models/tiers.md` | the tiers, Concept Repos and Run Repos, and the flows between them: §1 to §4 | goes (QUESTION-5): §2, the repos in the layers in keeping knowledge; §3, §4.1, Change; §4.2, the layers document | none: the layers, in place |
| `knowledge/adapted-cases/cbc-backend-design/defined-terms/defined-terms.md` | the Backend Kit's Defined Terms, an Instruction Text alone | 3, in place | none |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/rule.md` | changing a Kit Copy: its Instruction Text, a Paths Rule | 3, in place | none |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/understanding.md` | changing a Kit Copy: its Adapted Understanding Text | 3, in place | none |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/take-the-kit-update/SKILL.md` | taking a Kit Update: its Instruction Text, an Agent Skill | 3, in place | none |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/take-the-kit-update/understanding.md` | taking a Kit Update: its Adapted Understanding Text | 3, in place | none |
| `knowledge/backbone-ideas/change.md` | the Backbone Idea of change | 1, in place | none |
| `knowledge/backbone-ideas/defined-terms.md` | the Backbone Idea of Defined Terms | 1, in place | none |
| `knowledge/backbone-ideas/layers-of-knowledge.md` | the Backbone Idea of the layers | 1, in place | none |
| `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` | change, in CBC backend design | 2, in place | none |
| `knowledge/problem-domain-ideas/cbc-backend-design/defined-terms-in-cbc-backend-design.md` | Defined Terms, in CBC backend design | 2, in place | none |
| `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` | change, in keeping knowledge | 2, in place | none |
| `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` | Defined Terms, in keeping knowledge | 2, in place | none |
| `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` | the layers, in keeping knowledge | 2, in place | none |
| `temp/README.md` | what `temp/` holds: a draft, a kept file | form: 4, open (QUESTION-1) | `docs/conventions/project-recording/` |
| `temp/common-ground/backend-repo-change-flow.md` | a Backend Repo's Copy Change, as a flow: its pictures, and each open decision drawn | none: a source the rewrite reads: the pictures beside the change texts | none |
| `temp/common-ground/backend-repo-change-simulation.md` | a Backend Repo's Copy Change, simulated: each rule's options and why; its *Today* lines | none: a source the rewrite reads: its *Today* lines (ADR-0087, decision 5) | none |
| `temp/common-ground/between-repos-simulation.md` | what passes between the repos, simulated; frozen, in the old names | none: a source the rewrite reads; TODO's "Sort the simulation of what passes between the repos, and drop it" sorts it | none |
| `temp/common-ground/common-ground-problem.md` | the Common Ground Problem; its §1 and §7, the goal of the knowledge work | none: a source the rewrite reads: the rewrite's goal (ADR-0082); one item waits here (§8) | none |
| `temp/exchange-counts.md` | the exchange's texts, counted 2026-11-03 for the ended rebuild | none: kept; no text reads it; the map's §6 holds today's counts | none |
| `temp/model-example/approaches/change-a-home.md` | changing a home, as a Work Approach | none: an earlier try, read for ideas, for the one-home Agent Rule | none |
| `temp/model-example/comparison.md` | today's texts against the earlier try, counted 2026-11-02 | none: an earlier try, read for ideas, for QUESTION-5 | none |
| `temp/model-example/idea-model-problem.md` | the problem of the idea-to-approach model | none: an earlier try, read for ideas, named a first source of the layers in keeping knowledge | none |
| `temp/model-example/idea/commit-set.md` | a set of commits, as an idea bound to no project | none: an earlier try, read for ideas, for the commit-plan manual | none |
| `temp/model-example/idea/one-home.md` | one home per fact, as an idea bound to no project | none: an earlier try, read for ideas, for the facts-in-sync manual | none |
| `temp/model-example/layers.md` | three layers, pictured fresh, tried on one idea | none: an earlier try, read for ideas, named a first source of the layers in keeping knowledge | none |
| `temp/model-example/move-plan.md` | the move: split first, choose a pattern after | none: an earlier try, read for ideas, for the rewrite's order | none |
| `temp/model-example/other-patterns.md` | patterns from shared code and technical writing for texts that rely on each other | none: an earlier try, read for ideas, for QUESTION-4 | none |
| `temp/model-example/sideways-pointers.md` | why today's manuals point sideways at each other, and what replaces each kind | none: an earlier try, read for ideas, for QUESTION-4 and QUESTION-5 | none |
| `temp/model-example/this-repo/committing.md` | committing work, in this repo | none: an earlier try, read for ideas, for the commit-plan and commit-messages manuals | none |
| `temp/model-example/this-repo/one-home.md` | one home per fact, in this repo | none: an earlier try, read for ideas, for the facts-in-sync manual and the one-home Agent Rule | none |
| `temp/model-example/today-problems.md` | three problems of today's design, and the way out | none: an earlier try, read for ideas, for QUESTION-5 | none |
| `temp/reading-run-4-2026-11-26.md` | CBC Run 4's Reading: its findings, pointing at CBC Run 6's items | none: a source the rewrite reads: each taken item lands with its text | none |
| `temp/reading-run-5-2026-11-26.md` | CBC Run 5's Reading: its findings, pointing at CBC Run 6's items | none: a source the rewrite reads: each taken item lands with its text | none |
| `temp/reading-run-6-2026-11-26.md` | CBC Run 6's Reading: the three CBC Runs' decisions and work items, WORK-1 to 18 | none: a source the rewrite reads: each taken item lands with its text | none |
| `temp/rewrite-map.md` | the map: every text, its parts, layers and needs; the items from TODO; the shared questions | none: a source the rewrite reads: its plan | none |
| `temp/run-6-briefing.md` | CBC Run 6's briefing: the checkout it builds | none: kept; no text reads it | none |
| `temp/run-6-handoff/.claude/hooks/keep-going.sh` | the Stop hook that keeps a full-auto CBC Run going | none: an earlier try, read for ideas, for the auto-run Approach on Trial | none |
| `temp/run-6-handoff/.claude/settings.local.json` | the settings that install the Stop hook | none: an earlier try, read for ideas, for the auto-run Approach on Trial | none |
| `temp/run-6-handoff/CLAUDE.local.md` | the reviewer's local rules for a full-auto CBC Run | none: an earlier try, read for ideas, for the auto-run Approach on Trial | none |
| `temp/run-6-handoff/run.md` | how CBC Run 6 runs on full auto | none: an earlier try, read for ideas, for the auto-run Approach on Trial and TODO's "Evaluate the auto-run Approach on Trial" | none |
| `temp/run-6-handoff/start.md` | the prompt that started CBC Run 6 | none: an earlier try, read for ideas, for the auto-run Approach on Trial | none |

## 10. Shared questions

A question many texts share, decided once, here, with the reviewer.
Each text it touches names it in §9.

- **QUESTION-1. Where a record's form goes.** Each record's form says
  what its entries are, adapted for this repo from the project-recording
  manual. In the layers model it may be this repo's own Adapted Case,
  at layer 4, standing on an idea of records at layer 2; or it may
  stand on that idea directly, where it is. Touches every record.
  **Decided 2026-11-26, the reviewer:** each record's form is an
  Adapted Case, ours at layer 4, a Record Stub the Backend Kit's at
  layer 3, copied once at birth. Its parts land by ADR-0087, decision 4:
  - the form, how an entry is written: the record's header, where it
    is, as its Instruction Text, loading when the record is opened;
  - a why several records share: layer 2, an idea of records in
    keeping knowledge, written from the project-recording manual;
  - a why of one record alone: that record's Adapted Understanding
    Text, ours in `.claude/understanding/`; a record with none has
    none, as the Backend Kit's Defined Terms have none.

  Left to practice: the paths of the Backend Kit's Record Stubs, and
  which whys are one record's alone.
- **QUESTION-2. What becomes of the glossary.** It lists the Glossary
  Names of texts outside `knowledge/` and `.claude/understanding/`.
  A text in the layers model keeps its own Defined Terms
  (`.claude/rules/defined-terms.md`), and the glossary does not list
  them (ADR-0085).
  **Answered 2026-11-26, the reviewer:** by
  `.claude/understanding/defined-terms.md` §2, *Two sets of texts*,
  and §3, *Twin names*: the glossary governs the texts outside the
  layers model while the rewrite runs, and the rewrite retires each
  Glossary Name, a twin for its Defined Term, any other as a Defined
  Term at its new home. Added here:
  - the glossary and writing rule 9 go together, when the last text
    outside the layers model is rewritten; the defined-terms Agent
    Rule's rule 6 holds what rule 9 says of a name's form;
  - the delivered Glossary Names, the container's, the method's and
    the stack's, fold into the Backend Kit's Defined Terms, in place;
  - a Glossary Name a rewritten text now defines stays in the glossary,
    pointing at its new home, until no text outside the layers model
    uses it (repo hygiene's Plan Step, 2026-11-26).
- **QUESTION-3. What the changelog versions.** It versions the concept,
  for those who pin a concept version. In the layers model the concept
  is split (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
  §3.3, *The Adapted Case layer*).
  **Decided 2026-11-26, the reviewer:** in the layers model a Backend
  Repo pins a Backend Kit Version, and the Backend Kit Update Note
  says what changed since it, and why, from the commit bodies
  (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`
  §1, *Its Defined Terms*). No repo pins the concept itself. So:
  - our `CHANGELOG.md` goes once the first Kit Update is sent; its
    released entry is history, and its [Unreleased] entries need no
    new home;
  - a Backend Repo's own changelog, its Record Stub, stays, under
    QUESTION-1;
  - TODO's "Release concept v2" no longer fits as it reads; its own
    trigger, the rewrite done, decides what it becomes.
- **QUESTION-4. A manual's own sections.** *What it is for*, *What
  this is made usable as*, *The seats*, *Why it arrives this way*,
  *What this does not cover* and *Where to look* are the manual's form
  (`.claude/rules/convention-manual.md`). In the layers model, a text's
  header says what it is, what it stands on and what stands on it.
  Which of these sections land in the header, which in the text, and
  which go. Touches the 12 manuals.
  **Decided 2026-11-26, the reviewer:** none needs a home of its own;
  each goes where the texts in place already say it, or goes with its
  job:
  - the opening statement: the text's first line;
  - *What it is for*: the Understanding Text's own body;
  - *What this is made usable as*: the header's "What stands on it";
  - *The seats*: goes; each seat is its own Adapted Case, the CBC
    Run's at layer 3, ours at layer 4;
  - *Why it arrives this way*: the Adapted Understanding Text, as
    `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/understanding.md`
    §1, *Why a Paths Rule*;
  - *What this does not cover*: the text's opening, naming its
    neighbours;
  - *Where to look*: goes; a pointer stands where a line relies on it.

  The manual's form, `.claude/rules/convention-manual.md`, goes with
  the conventions manual.
- **QUESTION-5. What the layers model replaces.** The conventions
  manual, the Idea-to-Output Model and the Tiers Model say how ideas,
  texts and repos tie. The layers model says it for its own texts
  (`knowledge/backbone-ideas/layers-of-knowledge.md`). Touches those
  three, and every text with a Foundation Line.
  **Decided 2026-11-26, the reviewer:** the three go once their parts
  have landed, as every text does (ADR-0082, decision 2), and
  model-placing goes with them. Each part lands by its subject, not
  in the nearest text:
  - **held already,** pointing at its place: the chain and a link
    pointing up, the layers document; the two directions, Change;
  - **how knowledge moves:** the five facts on every flow and where a
    lesson lands, Change;
  - **which text may point at which:** the dependency rule, the
    layers document;
  - **keeping linked texts true:** settling a disagreement, the idea
    written from the facts-in-sync manual;
  - **how instructions are written for an agent:** how an Agent Skill
    or Agent Rule is written, what a convention asserts, and the
    Foundation Line, a new idea, written when the rewrite reaches the
    conventions manual. It takes the Agent Model's §9 too: which kind
    of file carries a rule, chosen by the channel table, and no field
    in a file names a channel (the Agent Model's Plan Step,
    2026-11-27).
- **QUESTION-6. Where the Tool Bindings go.** How the Agent Model's
  channels map onto Claude Code: agent-arrangement §5, *The Claude
  Code Tool Binding*, and the Agent Model's §10, *The Tool Bindings*.
  **Decided 2026-11-26, the reviewer:** split as every idea is:
  - what every Tool Binding must say, the Agent Model's §10: layer 1,
    in the Backbone Idea of how an agent works;
  - Claude Code's binding for the Backend Repos, all of which use it:
    a Backend Kit Adapted Case, layer 3;
  - ours, today's agent-arrangement §5: our own Adapted Case, layer 4.

  Written in two parts (2026-11-27, the reviewer): layer 1 with the
  Agent Model's rewrite; layers 3 and 4 with the agent-arrangement
  manual's, since they come from its §5.
- **QUESTION-7. Which ideas are Backbone Ideas.** §8's row on which
  ideas here are Idea Models, decided once with the layers document's
  open question 4, which ideas are Backbone Ideas
  (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
  §5, *Open questions*). In the layers model an Idea Model is a
  Backbone Idea. It settles "1 or 2" in every manual's line of §9.
  **Decided 2026-11-26, the reviewer:** an idea goes to layer 1 when
  both Problem Domains, keeping knowledge and CBC backend design, work
  by it today. One only one works by stays that Problem Domain's idea
  at layer 2, and goes up by Change's arrow *lesson* when a second
  needs it.
  - **Layer 1, in place or planned:** change, Defined Terms, the
    layers, how an agent works, CBC design; agent files, from the
    agent-arrangement manual, which this list did not name (its Plan
    Step, 2026-11-27, decision A).
  - **Layer 1, both work by it:** writing; one home, from the
    facts-in-sync manual, with settling a disagreement; records, from
    the project-recording manual; commit messages; a set of commits,
    from the commit-plan manual; repo hygiene; visual comparison;
    trying a new way of working, from the approach-drafting Approach
    on Trial; how instructions are written for an agent (QUESTION-5).
    Agent files lists the folder of ways of working on trial in plain
    words until the idea of trying a new way of working defines
    Approach on Trial; the line takes the Defined Term then (the
    agent-arrangement manual's Plan Step, 2026-11-27, decision D).
  - **Layer 2, keeping knowledge only:** refinement.
  - **Layer 2, CBC backend design only:** looking back, from the
    retrospective manual, our trial never run; Output Shapes, until
    §8's row on our own forms decides.
  - **No idea of its own:** birth, the Pure Seed's, lands in Change;
    the Tiers Model and the Idea-to-Output Model go (QUESTION-5).
  - **§8's candidates:** one home, Output Shapes and records stand as
    above; the Concept Deliverer and the CBC Run with their seats go,
    the repos already in the layers document and each seat an Adapted
    Case (QUESTION-4); the two checks on text kept true join the
    one-home idea and TODO's "Decide how texts are checked to stay
    true after the rewrite".

  The layers document's question 4 is answered here; its own §5 takes
  the answer when the rewrite reaches it.
