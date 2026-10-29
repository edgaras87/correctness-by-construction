# Commit plan: a word with more than one meaning here carries its subject

## Summary — the state after all commits

Two TODO items are decided together under ADR-0074: "Decide what
"rule" names" and "Write a rule that a word with more than one
meaning here carries its subject at every use". The writing
convention has a ninth rule: a word with more than one meaning here
carries its subject at every use, and bare means only what plain
English says. Both seats' `writing.md` carry it. The glossary says it
holds two kinds of entry, a word with one sense here and a word with
several, and lists the first two of the second kind: rule, with its
senses agent rule, a numbered line with its owner, invariant, and a
`---` line; and template, with a skill's template and a stack
overlay. The four living lines that used "rule" for an invariant or
a `---` line say what they mean. Round 3's Writing read then has the
words to read old text against; the rewording of about 150 bare uses
of "rule" for a file is its work, not this set's. The remaining
candidate words are measured at round 3's rule check, and the second
item stays in TODO for them, rewritten.

## Commits

**1. `docs(agent): add commit plan for word senses`**
This file.

**2. `docs: ADR-0074 a word's senses carry subjects`**
Proposed. The rule, the glossary's two kinds of entry, no mark on a
prefixed word, the words for "rule" and "template", and when the old
text changes. The options rejected at each.

**3. `docs: writing rule 9 and the glossary's word list`**
The writing manual's §2 gains rule 9 with its why. The glossary's
header names the two kinds of entry, and the entries for rule and
template go in. Project-recording §13's line "one row per rule"
says "one row per invariant", following the glossary. One commit: a
rule without its list, or a list without its rule, is not a
coherent state. Both files stand on the writing convention; the
foundation check reads them together.

**4. `chore(agent): our writing.md takes rule 9`**
Our agent rule follows the manual, in a commit of its own
(`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*).

**5. `fix(delivery): the shipped writing.md takes rule 9`**
The container's copy follows the manual. A run's glossary lists the
run's own words; the rule travels, the list does not.

**6. `fix(delivery): three shipped lines take the words`**
The container's `CLAUDE.md` and `ARCHITECTURE.md` say "one row per
invariant"; the slice-record shape says "a `---` line". After this,
every living use of bare "rule" is the plain sense or the file
sense, which is what round 3 reads for.

**7. `docs: the word items close, ADR-0074 accepted`**
ADR-0074 flips to Accepted. The "rule" item leaves TODO. The word
item is rewritten true for today: the rule is written, two words
listed, the candidates wait for round 3's rule check. Their
conversation-memory sections, §19 and §23, go with them. `PLAN.md`'s
Now line for the refinement says where the step is: between rounds,
at the work due before round 3's rule check.

**8. `docs(agent): close commit plan for word senses`**
Deletes this file; the body says what diverged.

**9. `docs: devlog for the word senses`**
The entry for the set, with the session-end lines.

## Decisions taken inside this plan

- **Two items, one ADR.** The reviewer's test for "rule", a bare
  word means plain English and each sense of ours carries its
  subject, is the second item's rule, and answers how its list is
  kept. Deciding "rule" alone would decide the second item's shape
  without saying so.
- **The list starts with two words, not ten.** The second item
  names eight more candidates. Each needs its uses and senses
  measured, and round 3's Writing read is where every living line is
  read anyway. So the candidates are measured at round 3's rule
  check, which is the moment the Writing kind's rules are confirmed
  (`.claude/approaches-on-trial/refinement.md` §2.3, *Check the rules*),
  and each that collides gets its entry before the read. The item
  stays in TODO for that, rewritten.
- **Four lines change now, the rest in round 3.** The item's
  trigger puts the rewording of old text in round 3's Writing read.
  The four lines that use "rule" for an invariant or a `---` line
  are taken now, so that round 3 meets one question, file or plain,
  not three.
- **`PLAN.md`'s Now line is corrected in the records commit.** It
  still names round 2's close read, which is done. A Now line
  changes when the step enters a new stage; the lesson stories' set
  did not change it.
- **No commit is provisional.** The decision is settled in talk
  (`TODO-CONVERSATION-MEMORY.md` §19 and §23, 2026-10-29).
