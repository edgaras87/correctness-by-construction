# Visual comparison

**How a structure is shown — a picture, a table, a plain list — is
settled by building every candidate and rendering it, judged
against what the reader must get. The unit is the thing being
shown.**

## What it is for

So that the way a structure is shown is chosen by what a reader
gets from it, and not by what the writer expected a notation to
do. The failure is lived, twice, on 2026-09-18: two Mermaid
dialects, each built for the job in hand, failed only when
rendered — `block-beta` lost its arrow labels, and
`sequenceDiagram` had to draw a read-only reading as an arrow into
the other repo, asserting the opposite of the rule the procedure
existed to keep (CBC ADR-0027, CBC ADR-0028). And the answer that
won one requirement that day was a table, which a method named for
diagrams would have left out of the set. Written as a method the
same day, made a convention on 2026-09-19 (CBC ADR-0031).

## What this is made usable as

- **`delivery/container/.claude/skills/visual-comparison/SKILL.md`
  — the skill, shipped**, held at `.claude/skills/visual-comparison/`
  and opened when a structure is hard to see and more than one way
  of showing it could work.
- **`.claude/skills/visual-comparison/SKILL.md` — the deliverer's
  copy**, downstream of the container's, changed by being copied
  anew.

This page explains; the skill states. What derives from this page
is that list. A change here walks it; a change forced in one of
them is checked back against this page.

## The seats

A run runs it on its own pictures. The deliverer runs it the same
way on its own.

## 1. What it is

The general method, plus the one failure mode only a picture has: a
notation that asserts something you did not mean. A table can be
unhelpful; a diagram can be *wrong* in a way the reader will
believe, because a drawing makes a claim by its shape before anyone
reads a label.

Its name went through four candidates before this one, and the
reason the others failed is the same reason this page exists.
`diagram-comparison` named the winning candidate rather than the
question — and would have excluded the table and the numbered list
from the set, which is where CBC ADR-0028's best answer to one
requirement came from. The question is *how is this shown*, and
"not a picture" is one of its answers.

## 2. Why it is shaped this way

- **The candidate set must hold at least one thing that is not a
  picture.** Otherwise a picture wins by construction and the
  method cannot return *no picture*, which is a real result. This
  is the rule the naming mistake would have broken, written down so
  the mistake is not available again.

- **The render decides, not the reasoning about the render.** Both
  Mermaid failures were dialects built for the job in hand, and
  neither was predictable from the documentation.

- **Fighting a notation is losing.** Invisible links, spacer nodes,
  nodes declared out of meaning order — a candidate needing them
  has already failed, because the next person to edit it will not
  know which parts are load-bearing.

- **The buildable notations are few, and the constraint is not
  aesthetic.** Plain text, rendering on GitHub and in the IDE with
  no build step, leaves Mermaid and Unicode box drawing. PlantUML,
  Graphviz and D2 need a render step or a plugin; a committed SVG
  renders but is not text anyone can read in a diff. A diagram
  nobody can read in review is a binary blob with extra steps.

*Settled 2026-09-24, the other way round from how it was asked. CBC
ADR-0030 decision 10 asked whether this earned an artifact of its
own beside a general comparison method: if its findings never
gained an entry from a comparison whose winner was not a picture,
the split was decoration and the two should merge back. The
trigger never fired, and the general half was discarded rather
than merged into — it had run once, in the set that created it.
This is the method now, not a specialisation of one.*

## What this does not cover

- **Which notations a project uses** — the project's own. The
  deliverer's Mermaid trial is provisional and does not travel (CBC
  ADR-0027 decision 3); a project deciding its own may reach a
  different answer.
- **A choice that is not about how something is shown** — no
  convention: it is decided while building, and corrected at a
  boundary, `docs/conventions/commit-plan/`.
- **Whether a picture may carry a fact the prose does not** — the
  manual that holds the picture decides;
  `docs/conventions/shapes/` states its own rule for itself.

## Where to look

- The decisions: CBC ADR-0027, CBC ADR-0028, CBC ADR-0030, CBC
  ADR-0031.
