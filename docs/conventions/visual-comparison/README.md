# Visual comparison

How a structure is shown — a picture, a table, a plain list — is
settled by building every candidate and rendering it, judged
against what the reader must get. The unit is the thing being
shown.

**What ships:** [`SKILL.md`](SKILL.md), which a project holds at
`.claude/skills/visual-comparison/` and an agent opens when a
structure is hard to see and more than one way of showing it could
work. This page explains it; the skill states it.

## What it is

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

## Why it is shaped this way

- **The candidate set must hold at least one thing that is not a
  picture.** Otherwise a picture wins by construction and the
  method cannot return *no picture*, which is a real result. This
  is the rule the naming mistake would have broken, written down so
  the mistake is not available again.

- **The render decides, not the reasoning about the render.** Both
  Mermaid failures were dialects built for the job in hand.
  `block-beta` is meant for stacked blocks and lost the arrow
  labels; `sequenceDiagram` is meant for handoffs and had to draw a
  read-only reading as an arrow into the other repo, asserting the
  opposite of the rule the procedure existed to keep. Neither was
  predictable from the documentation.

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

## An open question

Settled 2026-09-24, the other way round. CBC ADR-0030 decision 10
asked whether this earned a second artifact: if its findings never
gained an entry from a comparison whose winner was not a picture,
the split was decoration and the two should merge back. The trigger
never fired, and the general half was discarded rather than merged
into — it had run once, in the set that created it. This is the
method now, not a specialisation of one.

A narrower one: this repo's Mermaid trial is provisional (CBC
ADR-0027 decision 3) and does not travel. A project deciding its
own notations may reach a different answer, and nothing here says
it may not.

## Where to look

- The rule: [`SKILL.md`](SKILL.md).
- The decisions: CBC ADR-0027, CBC ADR-0028, CBC ADR-0030.
