---
foundation: the writing convention
---

# Writing

**Governs:** everything written here: chat answers, records, what
we write for CBC Runs, commit messages, comments. How it reads, never
what it says.

<!-- No paths: line, so this loads at the start of every session.
     Ours is derived from docs/conventions/writing/, as the
     container's is. That manual's *What this is made usable as*
     lists how the two differ. -->

## The rules

Why each rule is so: (`docs/conventions/writing/` §2, *Why each rule*).

1. **Lead with the answer.** The first line says the point. The
   reasons follow.
2. **Write short sentences, one idea each.**
3. **Label the parts.** When an argument has parts, give each its
   own line or label. Don't chain them with dashes and semicolons.
4. **Show it with numbers.** "42 commits, 7 copies edited, 4 of
   them untried" beats "a long span with several edits."
5. **Use plain words, not metaphor.** Say what happens. Not "a third
   act of the exchange", but "a third step of the exchange."
6. **Keep names as labels.** Write defined names and references
   exactly: ADR-0052, FINDING-7, WORK-9, `exchange-read`. Define each
   Glossary Name once, in plain words, in `docs/glossary.md`. Coin a
   word only when plain English cannot say it. A number
   local to one document carries its owner outside it: "CBC Run 3's RETRO
   D22", never a bare "D22": every CBC Run's RETRO has one.
7. **Cut what adds nothing.** If a sentence can go without losing
   meaning, it goes.
8. **Start from what the reader holds.** Before a label, a section
   number or a Glossary Name, ask whether this reader knows it. If
   not, say first, in plain words, what it is. Not "Stale lines has
   a weak rule", but "Stale lines, the kind that finds lines no
   longer true, has a weak rule".
9. **Write a defined thing by its Glossary Name,** two or more
   words, owner or kind first, each word capitalized, exactly as
   `docs/glossary.md` lists it, or the file it points at for the
   concept's, the method's and the stack's: CBC Run, Plan Step, Agent Rule,
   Output Shape, Delivery Staging. A Name built on another Name
   carries it whole, however long it gets: Agent Skill Template, never
   Skill Template. Past 4 words, every word counted, look for a
   shorter true Name before taking it; when none is found, the long
   Name stands. A hyphenated word counts as one, toward the two and the 4:
   "never-event" is one word. A lowercase word is English and
   only English. No Markdown mark marks a Name, but bold once, at
   the line that defines it. A list item's bold lead may begin with
   a Name. Written otherwise:
   - a numbered thing carries its owner and number,
     "working-a-reading rule 2", "the walk's step 3";
   - a label inside its owner keeps its case, "Step 0";
   - a path is written as it is;
   - a Foundation Line's value is written as the conventions manual
     gives it, `the exchange convention`.

   A thing is defined when a text gives
   a word a meaning English does not: its Name goes into the glossary
   in the commit that first uses it, pointing at the home that
   defines it.
10. **Title a numbered section with its subject.** A title is:
    - a label, a noun phrase of 30 characters or fewer;
    - in sentence case, a Glossary Name inside it keeping its
      capitals;
    - one phrase, with no gloss after a dash or colon, joined by a
      comma, or in parentheses;
    - standing alone without its parent heading: *How a plan is
      written*, never *How*.

    The point goes in the first sentence. The manual form's fixed
    headings, an Agent Skill Stage or Approach on Trial Stage heading, and a numbered rule's bold lead are not
    titles under this rule.
11. **Change only the lines the change needs.** The rest stand as
    they are. Markdown has no line width here; 72 is a commit body's
    rule and nothing else. A script that rewrites text counts
    headings, references and code fences before and after, and
    changes nothing on a second run.

## Before and after

Before:

> The count undercounts: one item's set can run to twenty commits,
> and an item that edits a skill both seats hold is two commits, the
> agent's own files apart. It is a number of items, never a size.

After:

> The count is of items, not of work. One item can take twenty
> commits. An item that edits an Agent Skill both sides hold is two
> commits: the Master Copy, then our own copy.

Same meaning. It can be read once.

## Where it applies

What the rules govern: (`docs/conventions/writing/` §1, *What it governs*).

- **Chat:** every answer.
- **Records:** every new or changed line. History keeps its words.
- **What CBC Runs read:** the Agent Skills, Agent Rules, Output Shapes, Approaches on Trial,
  concept chapters and notes we write, and the manuals they come
  from, every new or changed line. Older text is rewritten in work
  of its own.
- **Reading a dense text:** follow what it says, not how it says
  it. This rule sets the voice.

## Other styles

Plain is the default for every kind of text. A kind of text gets
another style only when plain has shown it falls short there, and
this rule then names that kind and its style
(`docs/conventions/writing/` §1, *What it governs*).

---

## Decisions

- ADR-0053 — how a text reads is a convention of its own, its rule
  loaded in every session, here as in every CBC Run
- ADR-0074 — rule 9's first form: a word with more than one meaning
  here carried its subject; the words for rule, template, stub,
  overlay, shape and form
- ADR-0075 — rule 10: a numbered section's title names its subject,
  30 characters at most, standing alone
- ADR-0076 — rule 9: every defined thing has a Glossary Name of two
  or more words, capitalized; the glossary is the list of Names
- ADR-0077 — rule 11: an edit changes only the lines its change
  needs; Markdown has no line width
- ADR-0078 — rule 9: a Name built on another Name carries it whole;
  past 4 words, a trigger to look for a shorter one
- ADR-0079 — rule 9: bold once at a Name's home, a list item's bold
  lead, a Foundation Line's value; rule 10: a comma or a parenthesis
  is a gloss
