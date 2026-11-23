# 0085. Defined Terms at their homes

Date: 2026-11-23
Status: Proposed, opened under the commit plan for knowledge/

## Context

The layers model leaves `temp/` for `knowledge/` (ADR-0084). Leaving `temp/` makes a text Living Text, and writing rule 9 then lists each defined thing's Name in `docs/glossary.md`. The two layers documents define 22. About 20 of the model's Defined Terms name what a Glossary Name already names: System Repo and CBC Run, Maintainer Repo and Concept Deliverer (`temp/common-ground/common-ground-problem.md` §2.2, *Today and what to check*, the table of today's names).

The glossary item was due. "Decide which names go in the glossary, and how a name one text uses alone is kept apart" waited for the problem file's Defined Terms to land in the rewrite (ADR-0082). Its risk: two texts with one name for two things, merged by the agent.

The glossary today: 309 lines, about 70 Names, a header of rules, 21 lines. Most entries retell a home's definition; a few are the only home.

## Options considered

- **Every new Name in the glossary, beside today's.** Rejected: about 20 things with two Names in one list; every term written twice, its home and its entry, which drift; and the glossary cannot say who uses a term.
- **Only the Names without a twin, or none until the rewrite.** Rejected: each breaks rule 9.
- **A file of terms per group,** as today's delivered glossaries. Rejected for this repo: two places per term again. Kept as the first guess for the System Kit, whose readers cannot open layers 1 and 2.
- **An index made by script from the definitions.** Not taken now: a grep finds a bold definition as fast. Its trigger: a reader who cannot find a Defined Term's home.
- **An index of exact lines.** Rejected: every edit moves the lines. The bold definition and the borrow table's Fact Reference are the anchors.
- **One scoped sentence in writing rule 9, holding the new rules.** Rejected: the rules would live in today's writing convention, and change again when it is rewritten into the layers model.

`cbc-concept/ideas/names.md` was a possible source of the Backbone Idea. The reviewer read it on 2026-11-23 and found nothing to take; the later check of `cbc-concept` (ADR-0082, decision 3) skips it.

## Decision

1. **Defined Terms is an idea of its own, at three layers:** a Backbone Idea, since CBC backend design needs it too; a Problem Domain Idea of keeping knowledge; and the Maintainer Repo's own Adapted Case, whose Instruction Text is a Paths Rule on `knowledge/**`. The problem file's rules for its Defined Terms are a source, taken where they still hold.
2. **Under `knowledge/`, and in the texts decision 3 names with it, a Defined Term is defined at its home and borrowed by table, never listed in the glossary.** How, and how the agent finds one, is the Defined Terms texts'.
3. **`docs/glossary.md` stays for today's texts** until the rewrite retires them. Writing rule 9 points `knowledge/` at the Defined Terms idea, and with it `.claude/understanding/` and an Agent Skill or Agent Rule whose understanding sits there: this repo's own Adapted Cases are kept whole in `.claude/` (ADR-0084), and must use Defined Terms. The copy delivered to CBC Runs is not changed: a CBC Run has no `knowledge/`.
4. **The System Kit's Defined Terms are open.** First guess: one terms text in the System Kit, each Defined Term adapted from its home. It is decided when the first System Repo Adapted Case is written.

## Consequences

- Two lists of Names stand for a while: the glossary for today's texts, the Defined Terms homes under `knowledge/`.
- Without one list, a collision is found only by grepping before a new Defined Term is defined. The Defined Terms texts make that a rule.
- An agent reads a Defined Term's definition, not its whole home, only if the Paths Rule tells it to.
