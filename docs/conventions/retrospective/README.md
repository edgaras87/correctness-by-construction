# Retrospective

**How a CBC Run that has finished building looks back, and what it
changes because of it.**

## What it is for

So that what a CBC Run learned reaches the next CBC Run, written down with
an example and a place to land. The failure is lived, in CBC Run 3
(its repository, `never-oversold`). Its plan ended on a section,
"Retrospective (fill at project end)", with five questions (§2, *How
the look back decides*). CBC Run 3 stopped before Release, the
playbook's last Plan Step, so the section's moment never came. The
retrospective happened only because the reviewer asked for one. It
then did far more than the section asked, and none of that was
written down as a way of working (its `RETRO.md`, D23):

- **It walked the CBC Run part by part,** in the order the CBC Run built
  them, and backed each finding with a quoted line or a count.
- **It decided one thing at a time,** each decision with what was
  rejected and where it lands.
- **It looked and changed nothing.** A Plan Step after it applied the
  lessons to CBC Run 3's own records before Release, and left what CBC Run
  3 had proved alone (its `RETRO.md`, D24).

CBC Run 3 kept the look back and the applying of its lessons as two
Agent Skills, and offered them. Taken on 2026-10-15
(ADR-0054).

## What this is made usable as

- **`delivery/container/.claude/skills/retrospective/SKILL.md` —
  the Agent Skill, shipped**, held at `.claude/skills/retrospective/` and
  opened when the CBC Run has finished building, before Release.
- **`delivery/container/.claude/skills/apply-retrospective/SKILL.md`
  — the Agent Skill, shipped**, held at `.claude/skills/apply-retrospective/`
  and opened when `RETRO.md` is closed, before Release.

The Concept Deliverer holds neither; its Convention Seat is on trial (below). This page
explains; the Agent Skills state. What derives from this page is that
list. A change here runs the Change Walk on it; a change forced in one of them is
checked back against this page.

## The seats

### The CBC Run's seat

Two people work it: the agent and the reviewer. The agent reads,
measures, proposes and writes; the reviewer decides. The Agent
Skills, which stand on this manual, stop at each of the reviewer's
decisions. In summary of them:

- **In the look back, the reviewer decides:**
  - whether small commits are free on the branch;
  - each decision: agree, correct, or drop;
  - each experiment: keep or drop;
  - when the branch lands.

  **The CBC Run gets:**
  - `RETRO.md`, with every decision, its example, what was rejected
    and where it lands;
  - TODO's *To the deliverer* pointing at it;
  - the Plan Step Gate items only the next CBC Run can check, each
    with the Plan Step that judges it.
- **In the apply Plan Step, the reviewer decides:**
  - each triage row: a decision marked applied, partly applied, or
    next CBC Run only;
  - each new decision the triage raises;
  - the commit plan before any change;
  - each planned commit at its boundary;
  - each revision of the plan that changes what lands;
  - when the branch lands.

  **The CBC Run gets** its records improved where the triage said
  so, and `RETRO.md`'s *Applied to* section: what happened to each
  decision.

No guide ships beside the Agent Skills: it would repeat them, and the two
would drift. The choice is reopened if a reviewer works without reading
this repo, or CBC Run 4's CBC Run Reading shows the missing guide cost something.
*Its story: ADR-0054.*

### The Concept Deliverer's seat

On trial. This repo has no project end. Its Plan Steps close on
"lessons written back where they came from: conventions, the
playbook, the concept", a close line its PLAN carries. That names the places but no method.

At the moment TODO's item "Run this repo's retrospective, on trial"
names, it runs both Agent Skills on itself, from `delivery/container/`, in place
of that close line. The parts are its own: the concept, the
conventions, the delivery, the exchange, its records. For this repo,
its next Plan Step plays the part a next CBC Run plays for a CBC Run. The trial's verdict says whether this
repo holds its own copies, and what this Convention Seat is.

## 1. The two Plan Steps

Looking and changing are kept apart on purpose. A retrospective that
may fix what it finds starts fixing the first thing, and stops
looking. But if the look changes nothing, the CBC Run is released with
records it has already shown could read better. So a second Plan Step applies
the lessons, before Release.

*Its story: devlog 2026-10-15; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## 2. How the look back decides

- **Every finding has an example from the CBC Run:** a quoted line, a
  file and line number, a count. No example, no finding.
- **Every decision says where it lands,** and the place is one the
  next CBC Run starts from: an Agent Skill, an Agent Rule, the playbook, an Agent Skill Template,
  the reviewer's local file. "Remember to" is not a place, and a
  lesson that lands nowhere is repeated.
- **No decision without something that went wrong.** A rule drafted
  with nothing to fix is dropped.
- **Choices are shown on real text:** the variants of a name applied
  to real lines, not argued in the abstract.
- **The reviewer's corrections are kept.** The agent's first
  version goes under "Considered and rejected", with the reason.
- **The old questions still ask.** They are prompts, asked while the
  CBC Run is read part by part:
  - which Plan Steps took longer or shorter;
  - what needed to happen earlier;
  - what was tried and dropped;
  - what had no home;
  - which Plan Step Gate items caught nothing;
  - and the Entry File read top to bottom, its only re-reading
    (`docs/conventions/agent-arrangement/` §2.6, *The Entry File's size*).

*Its story: devlog 2026-10-29, the lessons' own stories: six places.*

## 3. How the lessons are applied

- **Apply what improves what the CBC Run hands over, without changing
  what it proved:** a plainer sentence, a fact kept once and linked.
- **What changes how a Plan Step runs waits for the next CBC Run.** The
  CBC Run's Plan Steps are closed.
- **History is never touched.** A record that later Plan Steps were
  built on changes only by a dated revision entry.
- **New proof is not this Plan Step's.** A test written now was never
  seen to fail, so it proves nothing yet.
  A gap found here is listed, and the reviewer decides whether it
  earns a Plan Step of its own.
- **The order of the commits follows influence.** Removing repeats
  goes before rewriting, so no text is polished and then deleted.
  Owners go before the records that summarize them, README last of
  these. The plain-words rewrite comes after all of them.
- **A fresh reader checks each rewrite** against the old text. The
  writer reads what they meant, not what is on the page.
- **Tests are counted from this CBC Run's reports only.** A report
  folder can keep files from earlier CBC Runs.
- **A tool that edits text is checked on what it must not touch,**
  not only on what it changed.

*Its story: devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## 4. `RETRO.md`

The look back's record, at the CBC Run's root, one per CBC Run. It holds
every decision, the experiments, what was set aside for later, and,
after the
apply Plan Step, a row per decision saying what happened to it. The
records table names its moment. It is history once the CBC Run is
released: the next CBC Run starts from where its decisions landed, not
from `RETRO.md`.

## Why it arrives this way

Two Agent Skills, because each Plan Step is bound to a moment the agent would
otherwise have to notice: the CBC Run finishing its building, and
`RETRO.md` closing. A Plan Step opens each, and names the Agent Skill: where a pointer
is placed decides whether it fires (`docs/models/agent.md` §12.2, *Claims on the Pulled Channel*).

A section in the plan did not work. Its moment was the project's
end, which a CBC Run that stops early never reaches. And a section
can hold questions but not a way of working. Two Agent Skills, not
one, because the two Plan Steps are kept apart (§1, *The two Plan
Steps*).

## What this does not cover

- **The records a CBC Run keeps, and when each is opened** —
  `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md`.
- **How the apply Plan Step's commits are planned** —
  `docs/conventions/commit-plan/`.
- **What an Output Shape is, and how a Plan Step Gate reads it** —
  `docs/conventions/shapes/`.
- **How a CBC Run edits a delivered copy, and hands it back** —
  `docs/conventions/exchange/` §5, *Editing a copy*.
- **How a text reads** — `docs/conventions/writing/`.

## Where to look

- The decision: ADR-0054.
- CBC Run 3's record of both Plan Steps: its `RETRO.md`, D23 and D24.
