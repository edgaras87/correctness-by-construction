# Visual comparison

**How the way a structure is shown is chosen: a picture, a table,
or a plain list.**

## What it is for

So that the way a structure is shown is chosen by what a reader
gets from it, and not by what the writer expected a notation to
do. The failure is lived, twice, on 2026-09-18: two Mermaid
dialects, each built for the job in hand, failed only when
rendered — `block-beta` lost its arrow labels, and
`sequenceDiagram` had to draw a read-only Run Reading as an arrow into
the other repo, asserting the opposite of the rule the procedure
existed to keep (ADR-0027, ADR-0028). And the answer that
won one requirement that day was a table, which a method named for
diagrams would have left out of the set. Written as a method the
same day, made a convention on 2026-09-19 (ADR-0031).

## What this is made usable as

- **`delivery/container/.claude/skills/visual-comparison/SKILL.md`
  — the skill, shipped**, held at `.claude/skills/visual-comparison/`
  and opened when a structure is hard to see and more than one way
  of showing it could work.
- **`.claude/skills/visual-comparison/SKILL.md` — the Concept Deliverer's**,
  derived from this page like the container's, neither copied from
  the other, and written for this Convention Seat (ADR-0042, ADR-0069).

This page explains; the skill states. What derives from this page
is that list. A change here walks it; a change forced in one of
them is checked back against this page.

## The seats

A CBC Run runs it on its own pictures. The Concept Deliverer runs it the same
way on its own.

## 1. What a comparison is

Every candidate is built and rendered, and judged against what the
reader must get. The unit is the thing being shown.

The general method, plus the one failure mode only a picture has: a
notation that asserts something you did not mean. A table can be
unhelpful; a diagram can be *wrong* in a way the reader will
believe, because a drawing makes a claim by how it is drawn before
anyone reads a label.

Its name is the question, not a candidate: *how is this shown*,
and "not a picture" is one of its answers. A name that named a
picture would have kept the table and the numbered list out of the
set, which is where ADR-0028's best answer to one requirement
came from.

## 2. Why it is shaped this way

*Its story: ADR-0030; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.1 A non-picture in the set

The candidate set holds at least one thing that is not a picture. Otherwise a picture wins by construction and the
method cannot return *no picture*, which is a real result. This
is the rule the naming mistake would have broken, written down so
the mistake is not available again.

### 2.2 Deciding by the render

The render decides, not the reasoning about the render. What
a notation drops, or asserts by accident, shows only once it is
drawn; its documentation does not say it ahead. *Its story: devlog 2026-09-18; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.3 Fighting a notation

Fighting a notation is losing. Invisible links, spacer nodes,
nodes declared out of meaning order — a candidate needing them
has already failed, because the next person to edit it will not
know which parts are load-bearing.

### 2.4 The buildable notations

The buildable notations are few, and the constraint is not aesthetic. Plain text, rendering on GitHub and in the IDE with
no build step, leaves Mermaid and Unicode box drawing. PlantUML,
Graphviz and D2 need a render step or a plugin; a committed SVG
renders but is not text anyone can read in a diff. A diagram
nobody can read in review is a binary blob with extra steps.

## Why it arrives this way

A skill, opened when a structure is hard to see and more than one way
of showing it could work (`docs/models/agent.md` §4.2, *pulled*). The agent
recognises the moment by the question it is facing; no path is touched
that a rule could load on, and nothing in a record would bring the
method up then.

## What this does not cover

- **Which notations a project uses** — the project's own. The
  Concept Deliverer's Mermaid trial is provisional and does not travel
  (ADR-0027 decision 3); a project deciding its own may reach a
  different answer.
- **A choice that is not about how something is shown** — no
  convention: it is decided while building, and corrected at a
  boundary, `docs/conventions/commit-plan/`.
- **Whether a picture may carry a fact the prose does not** — the
  manual that holds the picture decides.

## Where to look

- The decisions: ADR-0027, ADR-0028, ADR-0030,
  ADR-0031.
