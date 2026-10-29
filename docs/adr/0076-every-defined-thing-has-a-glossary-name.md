# 0076. Every defined thing has a Glossary Name

Date: 2026-10-29
Status: Proposed, opened under the commit plan for round 3's check;
rewritten whole at its commit 5c, the same day, before acceptance.
The first text, a catalogue of every sense of seven words, is at
`e43894f`.

## Context

ADR-0074 made writing rule 9: a word with more than one meaning here
carries its subject at every use, bare it means only what plain
English says, and a glossary word with one sense here owns the bare
word. It gave the glossary two kinds of entry, a move rule between
them, and left ten candidate words to round 3's rule check.

Round 3's rule check measured the ten on 2026-10-29
(`temp/refinement-2026-10-18.md`, *Round 3: how it reads*), over the
living text outside history: "run" 1,382 uses, 964 the repository;
"step" 635, about 420 PLAN's; "stage" 401, 228 a skill's, 37 the
exchange's, 52 git's; "model" 336, with world, adversity, data and
role models already in what ships; "take" 229, 18 ours; "log" 156;
"tag" 47; "fill" 147, 7 a noun of ours. Two things the clause for a
first-kind word did not foresee: read strictly it forbids 449 verbs,
"it runs", "take the diff"; and a plain use of such a word is the
same letters as ours, so no grep finds it.

The first text of this ADR answered with more machinery: a word of
another part of speech is another word, an entry catalogues every
sense in use, seven words take a prefix, "cbc run" among them. At
commit 5's boundary the reviewer read "staging" and saw that the
question is not words. This repo defines about thirty things and
had hung each on one English word: rule, shape, form, stub, step,
stage, run, take, model, log, tag. At every use a reader decided
which was meant, and the glossary's two kinds, the clause and the
move rule were a way of deciding that, word by word, forever. The
reviewer asked whether a defined thing should have a bare word at
all, and whether something could mark it as defined so the question
"is this ours?" never arises; and weighed the answers by
maintenance, readability, future-proofing and complexity.

## Options considered

**What a defined thing is called:**
1. **One English word, with the glossary saying it is ours.** Rule 9
   as ADR-0074 wrote it. Rejected: the reader decides at every use,
   a plain use is found only by reading, and every new word reopens
   the question.
2. **A prefix on the words that collide, a catalogue of senses, two
   kinds of entry.** The first text here. Rejected: it decides word by
   word, each by a test the reader must know, and the list grows with
   every collision found.
3. **A Name of two or more words for every defined thing,** owner or
   kind first: CBC Run, Plan Step, Agent Rule, Output Shape, Delivery
   Staging. Taken. Two words say what the thing is and whose, and
   leave the single word to English. The rule is one sentence and has
   no list to keep: a lowercase word is English, always.

**How a Name is told from English:**
1. **Nothing marks it,** as ADR-0074 decided for a prefixed word.
   Rejected: "delivery staging" and "the exchange's staging" read
   alike, and only the glossary says which is defined.
2. **Italic, bold, backticks, quotes or a link.** Rejected, as
   ADR-0074 did: each has a job here, and italic is a title in a Fact
   Reference.
3. **A hyphen, "cbc-run".** Asked for as something a grep can find.
   Rejected: it reads as code, and it fails on a numbered thing,
   "working-a-reading-rule-2".
4. **Each word capitalized.** Taken. A contract's "the Deliverer"
   and Kubernetes' "a Pod" do this: the reader knows the word is
   defined before reading it, and no Markdown mark is spent. A grep
   for a capitalized pair finds every Name, and a grep for a Name's
   last word in lowercase finds the slips.
5. **A one-word Name, "Run".** Rejected: at a sentence's start the
   capital is invisible, and one word says nothing of whose.

**A text's numbered thing, "rule 2", "step 3":**
1. **A Name by kind,** "Rule Step 4". Rejected: it leaves which rule.
2. **Its owner and number,** "working-a-reading rule 2", "the walk's
   step 3", as "one-home rule 3" already reads. Taken. A label inside
   its owner keeps its case, "Step 0" in a plan, "Stage 3" in a
   skill; a path is written as it is.

**Where the old text changes:**
1. **In round 3's read, as findings** (ADR-0074, decision 9).
   Rejected: about 3,000 lines of one kind would bury the round's
   other findings.
2. **A scripted-and-hand pass by Refinement Layer before the read,** in one
   commit plan with the retitle of ADR-0075, one rewritten paragraph
   shown to the reviewer first. Taken.

## Decision

1. **Writing rule 9:** every thing this repo defines has a Glossary
   Name of two or more words, owner or kind first, each word
   capitalized, written exactly. A lowercase word is English and only
   English. No Markdown mark marks a Name. The manual says so; our
   `writing.md` and the container's follow it.
2. **The glossary is the list of Glossary Names,** each pointing at
   the home that defines its thing; the home defines, the entry
   points. The two kinds of entry, the clause for a first-kind word,
   the move rule and the catalogue of senses go. A word whose English
   meaning is ours has no Name and no entry: manual, convention,
   delivery, project. The 32 one-word entries take Names, judged by
   the reviewer one by one; twelve things named only by a phrase
   gain one, Glossary Name itself among them.
3. **A numbered thing is named by its owner and number;** a label
   inside its owner keeps its case; a path is written as it is.
4. **A Name is given at the commit that first uses the thing,** by
   the writer of the line. The test is one question: does the text
   give the word a meaning English does not? If so, its Name and
   glossary entry land in that commit. Rule 9 says so, and nothing
   else finds a missing Name, as one-home rule 6 says of a Fact
   Reference.
5. **The exchange's verb "stage" names its object,** "stage a
   delivery": the verb is English, git's as much as ours.
6. **Rule 10 gains one clause:** a Glossary Name inside a title
   keeps its capitals.
7. **Rule 9's old text changes in a pass before round 3 reads,**
   by Refinement Layer, in one commit plan with the retitle; the TODO item for
   the retitle becomes that plan's.
8. **ADR-0074 changes in part:** its decision 2, the two kinds of
   entry; decision 3, no mark, now the capitals; decision 7's "leave
   the first kind"; decision 8, the list measured, now closed;
   decision 9, the read, now the pass; decision 10, "a prefixed word
   is a name", now a Name. Its words for rule, template, stub,
   overlay, shape and form stand, as Agent Rule, Skill Template,
   Record Stub, Stack Overlay, Output Shape and Output Form.
   ADR-0074 is not edited.

## Consequences

- The writing manual's rule 9 is rewritten and rule 10 gains its
  clause, `ec1f048`; the glossary is 41 Names in six groups. Both
  `writing.md` follow, each in a commit of its own; the glossary
  Skill Template in `cbc-framing` drops the two kinds and takes the
  Name form, so a CBC Run's agent reading rule 9 finds it.
- The pass grows to about 3,000 lines: 964 "run", about 400 "step",
  230 "stage", 208 "model", 150 "rule", 70 "stub", 590 "shape" and
  "form", and the capitals on every phrase already in use, "agent
  rule" to Agent Rule. In what ships, a run reads "a CBC Run" of
  itself, and its own glossary says what that is.
- The check at a commit is two greps: a capitalized pair the
  glossary does not list is a Name to add; a Name's last word in
  lowercase is a slip to read. No check runs at a session's end: it
  would run every session and find little. A sweep at a commit
  plan's close gains the two greps the first time a miss gets past
  rule 9 and round 3's read, not before.
- Round 3's read meets text already in Names and lists what the
  pass missed.
- A shipped Agent Rule changes. CBC Runs hold the older copy until a
  delivery; CBC Run 6's Run Reading is pending.
- The TODO item for the remaining words leaves; the retitle item
  becomes the pass.
- Not decided here: a CBC Run's own Names. The rule ships; the CBC
  Run names its things.
