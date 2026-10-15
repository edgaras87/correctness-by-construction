---
foundation: the writing convention
---

# Writing

**Governs:** everything written here: chat answers, records,
commit messages, comments. How it reads, never what it says.

<!-- No paths: line, so this loads at the start of every session:
     its moment is every answer and every record. The why of each
     rule is the deliverer's writing manual. -->

## The rules

1. **Lead with the answer.** The first line says the point. The
   reasons follow.
2. **Write short sentences, one idea each.**
3. **Label the parts.** When an argument has parts, give each its
   own line or label. Don't chain them with dashes and semicolons.
4. **Show it with numbers.** A worked example with real numbers
   beats a definition. "Three submissions with key k-42, two of
   them retries after a timeout: one order exists, and all three
   get its answer" beats "duplicate submissions are idempotent."
5. **Use plain words, not metaphor.** Say what happens. Not
   "KILL-1 to KILL-3 are duplicate delivery in three costumes", but
   "KILL-1 to KILL-3 are the same failure, a second order, caused
   three ways."
6. **Keep names as labels.** Write defined names and references
   exactly: KILL-5, FACT-CALLER-5, SLICE-1, ADR-0014. Define each
   coined word once, in plain words, in the project's glossary,
   where it keeps one. Coin a word only when plain English cannot
   say it. A number local to one record carries its owner outside
   it: "SLICE-1 GUARANTEE-3", never a bare "GUARANTEE-3".
7. **Cut what adds nothing.** If a sentence can go without losing
   meaning, it goes.

## Before and after

Before:

> EVIDENCE-2, the harness can fail: the stored answer this slice
> leans on stands already, so it is made absent on the working
> tree — the lookup bypassed — and the replay seen red there, in
> the build, owed there by name.

After:

> EVIDENCE-2: the test must be able to fail. The stored answer
> already exists, because GUARANTEE-3 built it. So we skip the
> lookup on the working tree, and check that the replay test goes
> red. That red run is owed in the build stage.

Same meaning, same references. It can be read once.

## Where it applies

- **Chat:** every answer.
- **Records:** every new or changed line. History keeps its words.
- **Other texts:** a skill or rule may be written densely. Follow
  what it says, but not how it says it. This rule sets the voice.

## Other styles

Plain is the default for every kind of text. A kind of text gets
another style only when plain has shown it falls short there, and
this rule then names that kind and its style.

---

## Decisions

- CBC ADR-0053 — how a text reads is a convention of its own, and
  its rule loads in every session
