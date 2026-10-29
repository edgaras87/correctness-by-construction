# 0074. A word with more than one meaning here carries its subject

Date: 2026-10-29
Status: Accepted (2026-10-29, at the set's records commit; opened
Proposed under the commit plan for word senses, revised three times
while Proposed: an entry lists only the senses that keep the word,
with stub and overlay listed; the bare word is left to English and a
first-kind word owns the bare word; shape and form moved to the
second kind)

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
- **"template"**, 135 uses: the files under a skill's `templates/`
  that a run copies and fills
  (`delivery/container/.claude/rules/delivered-copies.md`, rule 8);
  and the plain sense, a text copied and filled in, which covers
  repo-hygiene's `.part` files too. A record's stub is called
  "stub", 125 times, and "template" for it is a slip.
- **"stub"**, about 70 uses in living text outside history, all for
  a record as it is born. One sense here; but a run writes tests,
  where a stub is a stand-in for a real part, and a run's agent
  reads what ships. Shipped text already says "record stub" twice.
- **"overlay"**, 11 uses, all but one "stack overlay", repo-hygiene's
  `.part` files for one stack; once a verb, in `exchange-deliver`.
- **"shape"**, 437 uses, and **"form"**, 214: ours in all but about
  26, which are the verb, "shaped by a talk", and idioms, "takes one
  form". Both were glossary words of the first kind.

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
(`d3ebdff:TODO-CONVERSATION-MEMORY.md` §19, *What "rule" names*). On
2026-10-28 the reviewer asked whether "template" should always carry
its subject, and whether every such word should
(`d3ebdff:TODO-CONVERSATION-MEMORY.md` §23, *A word with more than one meaning here*).
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

**What a glossary entry lists:**
1. **Every sense met,** a thing with a word of its own named under
   the word it is not called: "never a rule, an invariant". Taken at
   first, as a catch at writing time. Dropped when the reviewer
   read the entries: the rule catches it already, since a bare use
   that is not the plain sense must be listed, and an unlisted one
   sends the writer to the right word. Two of the four such lines
   were wrong besides: repo-hygiene's `.part` files are templates in
   the plain sense, and a stub needs no line saying what it is not.
2. **Only the senses that keep the word,** each with its subject.
   Taken.

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

**Stub and overlay:**
1. **Bare,** as words with one sense here. Rejected for stub: the
   reader of shipped text is a run, and in its tests the word has a
   second meaning. Rejected for overlay: the word is used only with
   its subject, "stack overlay", and the entry should say so.
2. **Prefixed, as entries of the second kind:** record stub, stack
   overlay. Taken. "Repo-hygiene stack" was weighed for the second
   and rejected: a stack is the technology, not the convention, and
   the word that carries the sense is "overlay".

**What an entry says of the bare word:**
1. **Its plain sense,** "what a text says must be done". Taken at
   first. Dropped when the reviewer asked whether it harms us: it
   narrows a plain English word to one of its senses, so "as a rule"
   would break the entry, and the glossary would own what is not
   ours.
2. **Only that it is plain English,** read as any word is, with
   nothing of ours in it. Taken. Rule 9 already said "what plain
   English says".

**Shape and form,** which the reviewer proposed as second-kind words:
1. **First kind, with the clause the rule was missing,** since the
   two are ours in all but 26 of 651 uses. Taken first, on the
   one-time cost, 26 lines against 650. Reversed the same day: a
   plain use of a first-kind word is found only by reading, and the
   agent broke the clause five times in one afternoon, in text about
   the clause. The cost that repeats, every new line by every
   writer, is the one that counts, and round 3 reads the 650 lines
   anyway.
2. **A prefix at every use,** checked by grep. Taken. "Record form"
   was rejected as the prefix: it does not cover a manual's or a
   reading's form. So form's subject is its owner, "a record's
   form", "the manual's form", and "output form" names the kind.
   Shape's is "output shape", and a particular one is named by its
   output, "the kill shape", as 62 lines already write by rule 8.
   The convention's name and the paths stay labels: `shapes`,
   `shapes-lifecycle.md`.

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
   today; it owns the bare word, so that word is not used in its
   plain sense here. A word with more than one sense here has one entry:
   the word, a line saying that bare it is plain English, read as
   any word is, then each sense of ours beneath it with the subject
   it carries. The entry defines nothing of the bare word. A thing
   with a word of its own is not a sense and is not listed. A new
   sense gets its line before its first use; a first-kind word that
   needs a second sense, ours or the plain one, becomes a
   second-kind entry, and its bare uses take their subject in the
   same change.
3. **No mark around a prefixed word:** no italic, bold, backticks,
   quotes or link. Quotes keep their one job, a word spoken of.
4. **The words for "rule":** agent rule, for a file under
   `.claude/rules/`; a numbered line carries its owner; bare, it is
   plain English. What a built system keeps is an invariant, and the
   line between blocks is a `---` line: words of their own, not
   senses of "rule".
5. **The words for "template":** a skill's template, for the files
   under a skill's `templates/` that a run copies and fills; bare,
   it is plain English, and repo-hygiene's `.part` files are
   templates in that sense. A record's stub is a stub.
6. **The words for "stub" and "overlay":** record stub, for the
   shipped file with its header and headings that a project fills;
   stack overlay, for repo-hygiene's `.part` files for one stack.
   Bare, each is plain English.
7. **The words for "shape" and "form":** output shape, a presumed
   output read at the gate, a particular one named by its output;
   output form, how an output is written, a particular one named by
   its owner. Bare, each is plain English. Both leave the first kind:
   the first words the glossary's move rule applies to.
8. **The rest of the list** is measured at round 3's rule check:
   stage, step, fill, master, take, tag, skill, log, model and run,
   and any word the check meets, the glossary's own first-kind
   entries read first. Each that collides is listed before round 3
   reads.
9. **Old text is reworded in round 3's Writing read,** against the
   list. Four lines change now: project-recording §13's and the
   container's two "one row per rule", and the slice-record shape's
   "separated by a rule".
10. **A prefixed word is a name,** written exactly as its entry
   writes it: "agent rule", never "the agent's rule file". Writing
   rule 6 already says so of a defined name; the glossary's header
   says it of these.

## Consequences

- The writing manual's §2 gains rule 9 and its why
  (`docs/conventions/writing/` §2, *Why each rule*). Both `writing.md`
  follow it, each in a commit of its own.
- The glossary's header changes, and gains its first two entries of
  the second kind. It stands on the writing convention, so the
  foundation check reads the two together.
- Round 3's Writing read has words to read against: about 150 bare
  uses of "rule" for a file become "agent rule", "skills and rules"
  among them; about 70 bare "stub" become "record stub"; about 590
  bare uses of "shape" and "form" take "output" or their owner, the
  26 plain ones staying as they are; and the
  conventions manual's §1.1 reads as an agent rule's lines. That is
  round 3's work.
- The run's glossary template, `cbc-framing`'s, takes the second
  kind of entry in its header, so a run's agent reading rule 9 finds
  the form. The list is the run's own.
- The glossary's groups stay by what a word names. A second-kind
  entry is told apart by its layout; a grep for "bare, plain English"
  lists them. A second grouping would be a second home for the list.
- A shipped agent rule changes. Runs hold the older copy until a
  delivery; run 6's reading is pending.
- Every new line asks one more question at the commit: is its word
  listed, and does it carry its subject. A grep for a listed word
  without one finds the misses.
- The "rule" item leaves TODO. The word item stays for the
  remaining candidates, rewritten, due at round 3's rule check.
- Not decided here: a run's own collisions, such as "fact" against
  its `FACT-` tags. The rule ships; the run lists its words.
