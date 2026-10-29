# 0077. An edit changes only the lines it needs

Date: 2026-10-29
Status: Proposed, opened under the commit plan for round 3's check

## Context

Nothing said how an edit keeps or changes the shape of the text it
touches. The 72-character width is written for one thing, a commit
body (`.claude/skills/commit-messages/SKILL.md`). The agent applied
it to Markdown and rewrapped whole paragraphs to fit: diffs grew past
their change, and a scripted rewrap broke structure twice, once
joining a shipped skill's frontmatter to its body. The reviewer
raised it on 2026-10-25 as TODO's "Decide how an edit or a new text
is shaped, line width included", due at round 3's rule check, which
reads the writing rules.

Measured 2026-10-29 over the 99 living Markdown files: 985 lines run
past 72 characters in 83 of them, tables aside. A reader meets the
text rendered, or in an editor that wraps. The reviewer reads a diff
at every commit boundary, and reads it for its change.

## Options considered

1. **A line width for Markdown,** 72 or another number, applied by
   an edit. Rejected: it would rewrap 83 of 99 files for a reader
   who never sees the line breaks, and every later edit would carry
   rewrapped lines that hide its change.
2. **A width shown as a guide in `.editorconfig`,** not enforced.
   Rejected: a guide invites the rewrap it does not require, and the
   agent followed one before.
3. **A change about as long as what it replaces.** Rejected: it
   cannot be checked, and a right change is sometimes longer.
4. **An edit changes the lines its change needs and leaves the rest
   as they stand; Markdown has no line width.** Taken. The rule is
   checked by reading the diff: a line the change did not need is a
   breach.

**The home:**
1. **The writing convention, as rule 11,** both `writing.md`
   following. Taken: the moment is every edit, and that rule loads
   in every session; how an edit lands is part of how a text reads
   to its reviewer.
2. **Repo-hygiene's `.editorconfig`.** Rejected: that file sets what
   an editor does to a file, not what an edit does to a text.
3. **A convention of its own for editing.** Rejected: one rule does
   not earn a manual.

## Decision

1. **Writing rule 11:** an edit changes the lines its change needs
   and leaves the rest as they stand. Markdown has no line width
   here, and nothing is rewrapped to one. The 72 stays
   commit-messages' rule for a body.
2. **A scripted pass is held to the same rule:** it counts headings,
   references and code fences before and after, and changes nothing
   on a second run.

## Consequences

- The writing manual's §2 gains rule 11 and its why; both
  `writing.md` follow, each in a commit of its own.
- TODO's item on how an edit is shaped closes.
- The 985 long lines stay as they are. A line is rewritten when its
  words change, not for its length.
- A diff at a boundary shows its change and nothing else, so the
  reviewer reads what changed, not what moved.
- Not decided here: how a new text is laid out beyond its lines.
  Writing rule 3 labels its parts, rule 10 titles its sections, and
  the records' forms and the output shapes say the rest.
