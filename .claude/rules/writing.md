---
foundation: the writing convention
---

# Writing

**Governs:** everything written here: chat answers, records, what
we write for runs, commit messages, comments. How it reads, never
what it says.

<!-- No paths: line, so this loads at the start of every session.
     Ours, derived from docs/conventions/writing/ like the
     container's; it differs where the seat does: runs read what we
     write. -->

## The rules

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
   exactly: ADR-0052, F7, W9, `exchange-read`. Define each coined
   word once, in plain words, in `ARCHITECTURE.md`'s *The words*.
   Coin a word only when plain English cannot say it. A number
   local to one document carries its owner outside it: "run 3's
   RETRO D22", never a bare "D22", which the reading numbers too.
7. **Cut what adds nothing.** If a sentence can go without losing
   meaning, it goes.

## Before and after

Before:

> The count undercounts: one item's set can run to twenty commits,
> and an item that edits a skill both seats hold is two commits, the
> agent's own files apart. It is a number of items, never a size.

After:

> The count is of items, not of work. One item can take twenty
> commits. An item that edits a skill both sides hold is two
> commits: the master, then our own copy.

Same meaning. It can be read once.

## Where it applies

- **Chat:** every answer.
- **Records:** every new or changed line. History keeps its words.
- **What runs read:** the skills, rules, shapes, manuals, concept
  chapters and notes we write, every new or changed line. Older
  text is rewritten in work of its own.
- **Reading a dense text:** follow what it says, not how it says
  it. This rule sets the voice.

## Other styles

Plain is the default for every kind of text. A kind of text gets
another style only when plain has shown it falls short there, and
this rule then names that kind and its style.

---

## Decisions

- ADR-0053 — how a text reads is a convention of its own, its rule
  loaded in every session, here as in every run
