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
| How much a CBC Run records against what it builds | the Record Stubs, `delivery/container/`, and the playbook, `delivery/fills/cbc-run-pure-playbook.md` | 205 | — |
| How a Work Approach and an Output Shape divide an output | the shapes manual, `docs/conventions/shapes/`, decided with the next row | 701 | §2, *How an approach and a shape divide an output* |
| Whether our own forms become Output Shapes, and whether an Output Shape's part can be optional | the shapes manual, and the forms in `.claude/rules/convention-manual.md` and `.claude/rules/exchange-reading.md` | 927 | §3, *Layouts as shapes* |
| Whether the approach-drafting Approach on Trial becomes a convention | `.claude/approaches-on-trial/approach-drafting.md` | 740 | — |
| Whether writing rule 10 reaches unnumbered headings | the writing manual, `docs/conventions/writing/` | 995 | — |
| A Fact Reference from the method's texts to each part of a concept chapter they use | the method's texts, `delivery/method/`, and the chapters, `concept/` | 1092 | §6, *The method's plain rewrite: `cbc-slice`'s opening* |
| Sort `docs/baselines/` by kind, read with care: a wrong move destroys a measurement | `docs/baselines/` | 1164 | — |
| Which ideas here are Idea Models | decided once, with which ideas are Backbone Ideas (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §5, *Open questions*, question 4) | 1175 | §29, *Two checks on text kept true* |

## 9. Every text

One line for each file of Living Text at `491e673e`, by `git ls-files`.
History is not mapped: the devlog's entries and the closed ADRs. A
record whose entries are history is mapped by its form. A pair, ours
and the shipped copy, takes one line. **Parts:** what the text holds.
**Layer:** where each part goes
(`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`
§3.5, *Where each layer is kept*), or the question that keeps it open.
**Needs first:** the texts rewritten before it, or none.

| Text | Parts | Layer | Needs first |
|---|---|---|---|
| `.claude/approaches-on-trial/approach-drafting.md` and `delivery/container/.claude/approaches-on-trial/approach-drafting.md` | | | |
| `.claude/approaches-on-trial/approach-evaluation.md` | | | |
| `.claude/approaches-on-trial/auto-run.md` | | | |
| `.claude/approaches-on-trial/model-placing.md` | | | |
| `.claude/approaches-on-trial/refinement.md` | | | |
| `.claude/decisions.md` and `delivery/container/.claude/decisions.md`, its form | | | |
| `.claude/rules/convention-manual.md` | | | |
| `.claude/rules/defined-terms.md` | | | |
| `.claude/rules/exchange-reading.md` | | | |
| `.claude/rules/foundation-check.md` | | | |
| `.claude/rules/one-home.md` and `delivery/container/.claude/rules/one-home.md` | | | |
| `.claude/rules/working-a-reading.md` | | | |
| `.claude/rules/writing.md` and `delivery/container/.claude/rules/writing.md` | | | |
| `.claude/skills/commit-messages/SKILL.md` and `delivery/container/.claude/skills/commit-messages/SKILL.md` | | | |
| `.claude/skills/commit-plan/SKILL.md` and `delivery/container/.claude/skills/commit-plan/SKILL.md` | | | |
| `.claude/skills/deliver-the-kit-update/SKILL.md` | | | |
| `.claude/skills/exchange-deliver/SKILL.md` | | | |
| `.claude/skills/exchange-read/SKILL.md` | | | |
| `.claude/skills/judge-copy-changes/SKILL.md` | | | |
| `.claude/skills/read-copy-changes/SKILL.md` | | | |
| `.claude/skills/visual-comparison/SKILL.md` and `delivery/container/.claude/skills/visual-comparison/SKILL.md` | | | |
| `.claude/understanding/defined-terms.md` | | | |
| `.claude/understanding/deliver-the-kit-update.md` | | | |
| `.claude/understanding/judge-copy-changes.md` | | | |
| `.claude/understanding/read-copy-changes.md` | | | |
| `.editorconfig` and `delivery/container/.editorconfig` | | | |
| `.gitattributes` and `delivery/container/.gitattributes` | | | |
| `.gitignore` and `delivery/container/.gitignore` | | | |
| `ARCHITECTURE.md` | | | |
| `CHANGELOG.md`, its form | | | |
| `CLAUDE.local.md` | | | |
| `CLAUDE.md` | | | |
| `PLAN.md` | | | |
| `README.md` | | | |
| `TODO-CONVERSATION-MEMORY.md`, its form | | | |
| `TODO.md` | | | |
| `concept/00-cbc.md` | | | |
| `concept/01-layered-system.md` | | | |
| `concept/02-guarantees-and-walls.md` | | | |
| `concept/03-cbc-framing.md` | | | |
| `concept/04-cbc-slice.md` | | | |
| `delivery/README.md` | | | |
| `delivery/container/.claude/CLAUDE.md` | | | |
| `delivery/container/.claude/rules/delivered-copies.md` | | | |
| `delivery/container/.claude/rules/shapes-lifecycle.md` | | | |
| `delivery/container/.claude/skills/apply-retrospective/SKILL.md` | | | |
| `delivery/container/.claude/skills/retrospective/SKILL.md` | | | |
| `delivery/container/ARCHITECTURE.md` | | | |
| `delivery/container/CHANGELOG.md` | | | |
| `delivery/container/PLAN.md` | | | |
| `delivery/container/README.md` | | | |
| `delivery/container/TODO.md` | | | |
| `delivery/container/devlog/devlog.md` | | | |
| `delivery/container/docs/adr/0001-record-architecture-decisions.md` | | | |
| `delivery/container/docs/glossary.md` | | | |
| `delivery/container/docs/glossary/container.md` | | | |
| `delivery/container/temp/README.md` | | | |
| `delivery/fills/cbc-run-pure-playbook.md` | | | |
| `delivery/installs/pure-seed.md` | | | |
| `delivery/method/.claude/shapes/evidence-test.md` | | | |
| `delivery/method/.claude/shapes/kill.md` | | | |
| `delivery/method/.claude/shapes/registry-entry.md` | | | |
| `delivery/method/.claude/shapes/slice-record.md` | | | |
| `delivery/method/.claude/skills/cbc-framing/SKILL.md` | | | |
| `delivery/method/.claude/skills/cbc-framing/references/cbc-framing-workflow.md` | | | |
| `delivery/method/.claude/skills/cbc-framing/references/the-whole-system-in-plain.md` | | | |
| `delivery/method/.claude/skills/cbc-framing/references/worked-example.md` | | | |
| `delivery/method/.claude/skills/cbc-framing/templates/registry.md` | | | |
| `delivery/method/.claude/skills/cbc-slice/SKILL.md` | | | |
| `delivery/method/.claude/skills/cbc-slice/references/cbc-slice-workflow.md` | | | |
| `delivery/method/.claude/skills/cbc-slice/references/system-readiness.md` | | | |
| `delivery/method/.claude/skills/cbc-slice/references/worked-example.md` | | | |
| `delivery/method/docs/glossary/method.md` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/SKILL.md` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/app-structure.md` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-harness-reference.md` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-pom-convention.md` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/application.yaml` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/readme-run-test.md` | | | |
| `delivery/spring-postgres/.claude/skills/cbc-bootstrap/templates/testcontainers.properties` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/SKILL.md` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/references/establishment-walk.md` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-role-split.md` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/references/postgres-setup-walkthrough.md` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/.env.example` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/bootstrap.sql` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/compose.yaml` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/flyway.conf` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/readme-prerequisites.md` | | | |
| `delivery/spring-postgres/.claude/skills/infra-establish/templates/verify-database-model.sql` | | | |
| `delivery/spring-postgres/.claude/skills/infra-serve/SKILL.md` | | | |
| `delivery/spring-postgres/docs/glossary/stack.md` | | | |
| `devlog/README.md` | | | |
| `docs/adr/README.md` | | | |
| `docs/baselines/cbc-derived-claude-walk1.md` | | | |
| `docs/baselines/cbc-run-pure-playbook-v2.md` | | | |
| `docs/baselines/cbc-startup-snippet.md` | | | |
| `docs/baselines/claude-md-template-v1.md` | | | |
| `docs/baselines/spring-slice-reference.md` | | | |
| `docs/conventions/README.md` | | | |
| `docs/conventions/agent-arrangement/README.md` | | | |
| `docs/conventions/commit-messages/README.md` | | | |
| `docs/conventions/commit-plan/README.md` | | | |
| `docs/conventions/conventions/README.md` | | | |
| `docs/conventions/exchange/README.md` | | | |
| `docs/conventions/facts-in-sync/README.md` | | | |
| `docs/conventions/project-recording/README.md` | | | |
| `docs/conventions/repo-hygiene/README.md` | | | |
| `docs/conventions/repo-hygiene/templates/java-spring/editorconfig.part` | | | |
| `docs/conventions/repo-hygiene/templates/java-spring/gitattributes.part` | | | |
| `docs/conventions/repo-hygiene/templates/java-spring/gitignore.part` | | | |
| `docs/conventions/retrospective/README.md` | | | |
| `docs/conventions/shapes/README.md` | | | |
| `docs/conventions/visual-comparison/README.md` | | | |
| `docs/conventions/writing/README.md` | | | |
| `docs/glossary.md` | | | |
| `docs/models/agent.md` | | | |
| `docs/models/idea-to-output.md` | | | |
| `docs/models/tiers.md` | | | |
| `knowledge/adapted-cases/cbc-backend-design/defined-terms/defined-terms.md` | | | |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/rule.md` | | | |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/change-a-kit-copy/understanding.md` | | | |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/take-the-kit-update/SKILL.md` | | | |
| `knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/take-the-kit-update/understanding.md` | | | |
| `knowledge/backbone-ideas/change.md` | | | |
| `knowledge/backbone-ideas/defined-terms.md` | | | |
| `knowledge/backbone-ideas/layers-of-knowledge.md` | | | |
| `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` | | | |
| `knowledge/problem-domain-ideas/cbc-backend-design/defined-terms-in-cbc-backend-design.md` | | | |
| `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` | | | |
| `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` | | | |
| `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` | | | |
| `temp/README.md` | | | |
| `temp/common-ground/backend-repo-change-flow.md` | | | |
| `temp/common-ground/backend-repo-change-simulation.md` | | | |
| `temp/common-ground/between-repos-simulation.md` | | | |
| `temp/common-ground/common-ground-problem.md` | | | |
| `temp/exchange-counts.md` | | | |
| `temp/model-example/approaches/change-a-home.md` | | | |
| `temp/model-example/comparison.md` | | | |
| `temp/model-example/idea-model-problem.md` | | | |
| `temp/model-example/idea/commit-set.md` | | | |
| `temp/model-example/idea/one-home.md` | | | |
| `temp/model-example/layers.md` | | | |
| `temp/model-example/move-plan.md` | | | |
| `temp/model-example/other-patterns.md` | | | |
| `temp/model-example/sideways-pointers.md` | | | |
| `temp/model-example/this-repo/committing.md` | | | |
| `temp/model-example/this-repo/one-home.md` | | | |
| `temp/model-example/today-problems.md` | | | |
| `temp/reading-run-4-2026-11-26.md` | | | |
| `temp/reading-run-5-2026-11-26.md` | | | |
| `temp/reading-run-6-2026-11-26.md` | | | |
| `temp/rewrite-map.md` | | | |
| `temp/run-6-briefing.md` | | | |
| `temp/run-6-handoff/.claude/hooks/keep-going.sh` | | | |
| `temp/run-6-handoff/.claude/settings.local.json` | | | |
| `temp/run-6-handoff/CLAUDE.local.md` | | | |
| `temp/run-6-handoff/run.md` | | | |
| `temp/run-6-handoff/start.md` | | | |
