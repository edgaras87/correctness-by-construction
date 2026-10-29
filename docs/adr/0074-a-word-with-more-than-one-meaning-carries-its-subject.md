# 0074. A word with more than one meaning here carries its subject

Date: 2026-10-29
Status: Proposed, opened under the commit plan for word senses

## Context

Some plain words carry senses of our own here, and a reader cannot
tell which is meant from the word alone. Counted 2026-10-25 and
2026-10-29 over the living text:

- **"rule"**, about 970 uses, in five senses: a file under
  `.claude/rules/` that loads into the agent (the path 115 times,
  "skills and rules" 25); a numbered line inside one, "one-home
  rule 3" (41, each with its owner); what a text says must be done,
  "the bump rule"; what a built system keeps, "one row per rule"
  (3 lines, beside 120 uses of the method's word, invariant); and
  once, in the slice-record shape, the `---` line between blocks, a
  typesetter's word.
- **"template"**, 135 uses, in three senses and the plain one: the
  files under a skill's `templates/` that a run copies and fills
  (`delivery/container/.claude/rules/delivered-copies.md`, rule 8);
  repo-hygiene's stack overlay, three `.part` files under its
  `templates/`; and the plain sense, a text copied and filled in.
  A record's stub is called "stub", 125 times.

The glossary defines none of these senses. Every entry it holds is a
word with one sense here, written bare: run, master, take, step,
stage. Writing rule 6 coins a word only when plain English cannot
say it and defines each once. Writing rule 8 says what a word is
before its first use, and that covers a first use only: since
ADR-0070 a fact reference lands a reader on one section, past it.
The conventions manual's §1.1, *How a rule is written*, is about
the files, and its first line, "A rule is one sentence in the
imperative", means a line.

Round 3 of the refinement reads how every living text reads, and
its rule check confirms the Writing kind's rules before it reads
(`.claude/approaches-on-trial/refinement.md` §2.3, *Check the rules*).
The words must be settled before it, so one read finds every
misuse.

The reviewer asked, 2026-10-25, what "rule" means in an item's
title, and proposed "agent rule" for the file
(`TODO-CONVERSATION-MEMORY.md` §19, *What "rule" names*). On
2026-10-28 the reviewer asked whether "template" should always carry
its subject, and whether every such word should
(`TODO-CONVERSATION-MEMORY.md` §23, *A word with more than one meaning here*).
On 2026-10-29 the reviewer set the test: a bare word means plain
English only; each sense of ours carries its subject; a new sense
is listed before it is used, or a bare use is caught.

Every mark Markdown has already has a job here: italic for a section
title in a fact reference and for the "*Its story:*" lines; bold
for a lead; backticks for a path or a command; quotes for a word
spoken of, not used. Our glossary does not ship; a run starts its
own from framing's template.

## Options considered

**Which uses carry the subject:**
1. **The first use in a file,** writing rule 8 as it stands.
   Rejected: a fact reference lands a reader past it.
2. **Every use, judged by the writer.** Rejected: applied unevenly,
   and no grep can find a miss.
3. **Every use, for the words a list names.** Taken: one rule, one
   list, and a grep for a listed word without its subject finds the
   misses.

**Where the list lives:**
1. **One glossary entry per word,** the bare sense first, each
   sense of ours beneath it with its subject. Taken: the glossary
   is where a word is already defined once, and a reader who meets
   a prefixed word looks under the bare one.
2. **The writing rule holds the list.** Rejected: a rule that ships
   to both seats would carry a list that is ours; the run's words
   are its own.
3. **The rule defines the term, and a glossary group lists the
   words, each pointing at the rule.** Rejected: the group is the
   list in all but name, and the pointer says what the glossary's
   header can say once.

**How the file sense of "rule" is named:**
1. **"agent rule".** Taken: two plain words, not a coined one; says
   who reads it; holds in both seats; a grep tells it from bare
   "rule". The path `.claude/rules/` stays, since a path is a name.
2. **"rules file".** Rejected: says where it sits, not who reads it.
3. **Bare "rule", read from context.** Rejected by the test above.

**The other senses of "rule":**
- A numbered line carries its owner already: "one-home rule 3",
  "writing rule 6". Nothing new is coined for it.
- What a built system keeps has the method's word, invariant. A
  prefix, "system rule", was rejected: a second term for a thing
  that has one.
- The `---` line says what the reader types, "a `---` line".
- Bare "rule" means what a text says must be done, the plain sense.

**A mark on a prefixed word,** italic, bold, backticks, quotes or a
link to the glossary. All rejected. The subject explains itself in
plain words, with or without the glossary. Each mark would take a
second meaning, and quotes in prose read as doubt. A run cannot
follow a mark to our glossary. And marking the prefixed words while
coined words stay bare, 154 uses of run, seat, deliverer and newborn
in the exchange manual alone, would single out the easier kind.

**Which words are listed now:**
1. **Every candidate the item names,** ten words, each measured
   first. Rejected: round 3's Writing read is where every living
   line is read, and that read is the measure.
2. **"rule" and "template",** both measured already; the rest at
   round 3's rule check, each that collides listed before the read.
   Taken.

**Renaming `convention-manual.md`,** since it reads as a manual.
Rejected: every agent rule of ours is named by what it governs,
`one-home.md`, `working-a-reading.md`, `foundation-check.md`; with
"agent rule" the word, "the agent rule `convention-manual.md`" reads
clearly.

**When the old text changes:**
1. **Now, in this set.** Rejected: about 150 bare uses of "rule"
   for a file, and the read that finds them is round 3's.
2. **In round 3's Writing read,** as the items' trigger says. Taken,
   with one exception: the four lines that use "rule" for an
   invariant or a `---` line change now, so round 3 meets one
   question, file or plain, not three.

## Decision

1. **Writing rule 9:** a word with more than one meaning here
   carries its subject at every use. Bare, it means only what plain
   English says. The glossary lists the words and each sense's
   subject. Both seats' `writing.md` carry it; a run's glossary
   lists the run's own words.
2. **The glossary holds two kinds of entry,** and its header says
   so. A word with one sense here is defined bare, as every entry is
   today. A word with more than one sense here has one entry: the
   word, its plain sense, then each sense of ours beneath it with
   the subject it carries. A sense that has a word of its own names
   that word. A new sense gets its line before its first use.
3. **No mark around a prefixed word:** no italic, bold, backticks,
   quotes or link. Quotes keep their one job, a word spoken of.
4. **The words for "rule":** agent rule, for a file under
   `.claude/rules/`; a numbered line carries its owner; bare "rule"
   is what a text says must be done; what a built system keeps is
   an invariant, never a rule; the line between blocks is a `---`
   line.
5. **The words for "template":** a skill's template, for the files
   under a skill's `templates/` that a run copies and fills; a stack
   overlay, for repo-hygiene's `.part` files; bare "template" is a
   text copied and filled in. A record's stub stays "stub".
6. **The rest of the list** is measured at round 3's rule check:
   stage, step, fill, master, take, tag, skill, log, model and run,
   and any word the check meets. Each that collides is listed before
   round 3 reads.
7. **Old text is reworded in round 3's Writing read,** against the
   list. Four lines change now: project-recording §13's and the
   container's two "one row per rule", and the slice-record shape's
   "separated by a rule".

## Consequences

- The writing manual's §2 gains rule 9 and its why
  (`docs/conventions/writing/` §2, *Why each rule*). Both `writing.md`
  follow it, each in a commit of its own.
- The glossary's header changes, and gains its first two entries of
  the second kind. It stands on the writing convention, so the
  foundation check reads the two together.
- Round 3's Writing read has words to read against: about 150 bare
  uses of "rule" for a file become "agent rule", "skills and rules"
  among them; and the conventions manual's §1.1 reads as an agent
  rule's lines. That is round 3's work.
- A shipped agent rule changes. Runs hold the older copy until a
  delivery; run 6's reading is pending.
- Every new line asks one more question at the commit: is its word
  listed, and does it carry its subject. A grep for a listed word
  without one finds the misses.
- The "rule" item leaves TODO. The word item stays for the
  remaining candidates, rewritten, due at round 3's rule check.
- Not decided here: a run's own collisions, such as "fact" against
  its `FACT-` tags. The rule ships; the run lists its words.
