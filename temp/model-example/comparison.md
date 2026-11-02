# Today's texts against the new model

<!-- A draft: the two ideas tried in temp/model-example/, set against
     how this repo holds the same two today. Counts taken 2026-11-02.
     The checks and criteria are temp/idea-model-problem.md §3. -->

## In short

Today the repo has three layers too: Idea Model, convention manual,
Agent Skill or Agent Rule. They are cut differently. A manual is not
the idea free of projects: it is the idea already adapted, holding
both projects' versions, their history, and many pointers sideways
to other manuals. Steps live in more than one text, and the why is
spread over four kinds of text.

The new model is about a third of the size for the same two ideas.
That is not yet a fair count: today's texts carry lessons from many
CBC Runs, and the new ones are a day old.

## 1. The texts

| | Today | Lines | New | Lines |
|---|---|---|---|---|
| One home per fact | facts-in-sync manual | 414 | the idea | 75 |
| | our one-home Agent Rule | 78 | this repo's project text | 49 |
| | the Foundation Check Agent Rule | 88 | Change a home | 37 |
| | the shipped one-home Agent Rule | 60 | | |
| A commit set | commit-plan manual | 194 | the idea | 71 |
| | our commit-plan Agent Skill | 206 | this repo's project text | 60 |
| | the shipped commit-plan Agent Skill | 206 | 3 Work Approaches, not drafted | about 105 |
| **Both** | 7 files | **1,246** | 7 files | **about 397** |

## 2. What each layer holds

| | Today | New |
|---|---|---|
| **The idea, free of projects** | None. The manual opens with this repo's history and the CBC Runs' cases | The idea text: no project, path or tool |
| **Each project's choices** | Both projects in one manual, under *The seats*, and spread through its body: the pointer form, section numbering, where the plan file lives | One project text per project; a change for one leaves the other alone |
| **Steps** | In the manual's body, the Agent Rules and the Agent Skill: the Change Walk is in facts-in-sync §4 and again in the Foundation Check | The Work Approach only |
| **Why** | The manual, the ADRs it cites (18 in facts-in-sync, 13 in commit-plan), each Agent Skill's and Agent Rule's *Decisions* footer, and the devlog by *Its story* lines (7 and 11) | The idea's *Why*; dated *Changes* at its end |
| **Shipped copy** | A second Agent Skill or Agent Rule, derived from the manual on its own, kept in step by hand | Not drafted. The project text names the need: a shipped copy's pointers do not resolve in the other repo |

## 3. Pointers

| | Today | New |
|---|---|---|
| **Sideways, idea to idea** | facts-in-sync points at 7 other manuals and 2 Idea Models; commit-plan at 3 manuals and 1 Idea Model | None. Each idea states its needs; the project text wires them |
| **Out of one text** | facts-in-sync: 37 paths and 18 ADRs; one-home Agent Rule: 14 and 6 | Idea: 0. Project text: up to the ideas it draws on. Work Approach: 1 |
| **Into one section** | facts-in-sync §4: 22 places | Not yet measured |
| **Address form** | Path, section number and title. A new section shifts numbers, and every shift is a rename grep | Path and heading. Adding a section moves no pointer |

## 4. Against the checks

| | Check | Today | New |
|---|---|---|---|
| 1 | Both kinds of idea in one shape | Partly: the concept has chapters, a way of working a manual, two shapes | Yes, on two ideas of one kind; the concept not tried |
| 2 | An idea names no project | No: the manuals name CBC Runs, this repo, its records | Yes |
| 3 | A second project writes only what differs | No: a second repo would extract the idea from the manual | Not tried |
| 4 | Several Work Approaches from one idea | Yes: our Agent Rule and the Foundation Check from one manual | Yes in shape; one drafted |
| 5 | A contradiction shows before it lands | Partly: the Foundation Check, between an Agent Rule and its manual | Where ideas meet, in the project text; one case shown |
| 6 | A project's ideas read in one place | No | Read from the project texts; not built |
| 7 | Each lesson leaves a trace | Yes, spread: CHANGELOG, ADRs, devlog | The idea's *Changes*; not tried |
| 8 | One step each way | Partly: each Agent Skill names its manual; a manual lists what derives from it | Yes, upward links only |
| 9 | A change stays local | No: 22 places at one section, and sideways pointers | Untested |

## 5. Against the criteria

| Criterion | Today | New |
|---|---|---|
| Maintenance | High: a change runs the Change Walk across manuals, Agent Rules and both copies | Lower on paper: no sideways pointers, no section numbers. Untested |
| Readability, agent | An Agent Skill reads alone, but carries "Why it is so" lines into the manual | A Work Approach reads alone, with no why |
| Readability, reviewer | A manual mixes idea, two projects, history and pointers | Each text holds one kind of thing |
| Future-proofing | A new idea adds a manual that points at others | A new idea touches no other idea |
| Complexity | 7 files and 4 kinds of why for two ideas | 7 files, one place for why |
| Cost of use | Agent Rules loaded in every session: 363 lines | Not measured |
| Cost of switching | None | Porting 13 manuals and their Agent Skills and Agent Rules, and the lived lessons in them |

## 6. Not yet fair

- **Lived detail.** The commit-plan manual's §2 holds 13 lessons: small
  commits, counting subjects, the agent's files, and more. The new
  model would put most in the project text's *Local needs*, and a few
  in the idea. Ported in full, how big is it?
- **Shipping.** Today ships a copy of each Agent Skill and Agent Rule
  to every CBC Run. The new model has not said how.
- **Only two ideas,** both ways of working. The concept, CBC, is not
  tried.

## 7. What would settle it

1. **Port one idea in full:** the commit-plan manual and both Agent
   Skills, every lesson kept, into the three layers. Compare the size,
   and what was lost.
2. **Change one fact both ways:** the same change, made in today's
   texts and in the new ones. Count the texts touched, the lines read,
   and the time.
