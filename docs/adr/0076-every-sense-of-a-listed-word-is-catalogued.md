# 0076. Every sense of a listed word is catalogued

Date: 2026-10-29
Status: Proposed, opened under the commit plan for round 3's check

## Context

ADR-0074 made writing rule 9: a word with more than one meaning here
carries its subject at every use, bare it means only what plain
English says, and a glossary word with one sense here owns the bare
word and is not used in its plain sense. It listed six words and
left ten candidates to round 3's rule check, to be measured there.

Round 3's rule check tried the rule on the ten, 2026-10-29
(`temp/refinement-2026-10-18.md`, *Round 3: how it reads*). Counted
over the living text outside history:

- "run", 1,382 uses: the repository, 964; the verb, 238.
- "step", 635: PLAN's step, about 420; a numbered step in a text,
  "step 4", 131; a casual phase, "the first step from a convention
  to a model".
- "stage", 401: a skill's stage, 228; an approach on trial's stage;
  the exchange's staging, 37; git's staged and the verb, 52.
- "model", 336: our models, 270, 62 of them named; the Claude model,
  29. In what ships the word already means four other things: the
  world model in the concept, the adversity model in the method, the
  data model and the role model in the stack skills.
- "take", 229: the run's take, 18; the verb, 211.
- "log", 156: the decisions log, 33 named and up to 82 bare; git
  log, 10; the verb, 31; devlog and CHANGELOG as labels.
- "tag", 47: the repo tag CBC, 19; the framing's tags; git's tag.
- "fill", 147: the verb, 115; a noun of ours, a body written into a
  record stub, 7.
- "skill", 605, and "master", 86: one sense each.

Two things the clause for a first-kind word did not foresee. Read
strictly, it forbids "it runs" and "take the diff", 449 verbs that no
reader confuses with "a run" or "the run's take". And it cannot be
checked: a plain use of a first-kind word is the same letters as
ours, so only a reader finds it, which is why shape and form left the
first kind (ADR-0074, decision 7).

The reviewer asked, 2026-10-29, for every variation a listed word is
used in, "plan step" but also a rule's step, and for a rule that says
so; then for a prefix on every word discussed, run among them, so
that a bare word is English and nothing else; and whether the
glossary should define the senses or point at the text each is born
in. The glossary's header already says that where a manual owns the
thing a word names, the entry points at it and does not restate it.

## Options considered

**The clause for a first-kind word:**
1. **As written:** never used in its plain sense. Rejected: it
   forbids every verb that shares letters with a noun of ours, and
   no grep finds a breach.
2. **With a mark:** a plain use carries a mark, "the Claude model".
   Proposed by the agent at the check, with model and then step as
   its case. Rejected: a mark works only for the plain senses known
   in advance, and model's four shipped senses were not; once model
   and step are listed, no first-kind word needs it.
3. **A word of another part of speech is another word.** Taken: "a
   run" is ours and "it runs" is English, and grammar tells them
   apart in every sentence.

**What an entry lists:**
1. **Our senses only,** as ADR-0074 wrote it. Rejected: a reader who
   meets "git log" or "the Claude model" finds nothing under the
   word, and a writer about to coin "role model" does not learn that
   the word is taken four ways already.
2. **Every sense in use, each with its subject, ours and others'
   alike,** the entry pointing at the home that defines each. Taken.
   A use stays bare only where it is casual English and no subject
   would be true of it.

**Which words are listed:**
1. **By the test alone,** more than one noun sense in use: step,
   model, log, tag. Rejected by the reviewer: stage, take and run
   stay bare under it, and a reader must know the test to know that
   bare "run" is ours there and English elsewhere.
2. **Every word discussed,** so a bare word is English and nothing
   else. Taken: step, stage, take, model, log, tag and run. Cost
   accepted: "cbc run" touches 964 lines, 136 of them in what ships.

**The subject of a text's numbered step:**
1. **Its kind,** "rule step 4", "convention step 3". Rejected: it
   still leaves which rule.
2. **Its owner,** "working-a-reading's step 4", "the walk's step 3".
   Taken, as "one-home rule 3" and "the kill shape" already do.

**Where rule 9's old text changes:**
1. **In round 3's read, as findings** (ADR-0074, decision 8).
   Rejected: about 2,600 lines of one kind, each a judgment of
   sense, would bury the round's other findings and be decided twice.
2. **A scripted-and-hand pass by layer before the read,** in one
   commit plan with the retitle of ADR-0075. Taken: a script lists
   every bare use of a listed word, a hand chooses its sense and
   subject, the commit greps for what it changed, and round 3's read
   lists only what the pass missed.

## Decision

1. **A word of another part of speech is another word.** The noun
   "run" is ours; the verb is English. Rule 9 says so.
2. **A listed word's entry catalogues every sense in use,** each
   with the subject it carries, ours and others' alike, and points
   at the home that defines it: the glossary is a contents page, the
   home is the definition, the text is the use. A use stays bare only
   where it is casual English and no subject would be true of it.
   Rule 9 says so, and the glossary's header retells it.
3. **Seven words join the second kind,** with the senses the texts
   use: step, as plan step and a text's step named by its owner;
   stage, as skill stage and approach stage, delivery staging keeping
   its entry; take, as a cbc run's take; model, as idea model, the
   agent, tiers and idea-to-output models by name, and the adversity,
   world, data, role and Claude models as others'; log, as decisions
   log, with git log and the labels as others'; tag, as repo tag,
   with the framing's tags and git's tag as others'; run, as cbc run.
   The entries for rule, shape, form, template and stub gain the
   named senses in use. The noun "fill" is not listed: its 7 uses
   become "composed body".
4. **The exchange's verb "stage" names its object,** "stage a
   delivery", since git's verb is the same word.
5. **Rule 9's old text changes in a pass before round 3 reads,**
   by layer, in one commit plan with the retitle, a TODO item holding
   it until the plan opens.
6. **ADR-0074 changes in part:** its decision 2's clause for a
   first-kind word now reads with decision 1 here; its decision 8's
   "in round 3's Writing read" is now decision 5 here. ADR-0074 is
   not edited.

## Consequences

- The writing manual's rule 9 gains two sentences; both `writing.md`
  follow, each in a commit of its own. The glossary's header says
  what an entry is; seven entries are added and five extended.
- The pass grows to about 2,600 lines: 964 "cbc run", about 400
  "plan step", 130 "skill stage", 208 "idea model", 100 "decisions
  log" and "repo tag", 14 "a cbc run's take", beside the 800 of
  ADR-0074. In what ships, 136 uses of "run" become "cbc run": a
  run reads "a cbc run" of itself, and its own glossary says what
  that is.
- The check at a commit is one grep per listed word for a bare use;
  what it finds is English or a miss.
- Round 3's read meets text already in its words and lists what the
  pass missed; the read's Writing findings are not the pass's.
- The glossary's first kind keeps only words with one sense in use
  and no plain use here: deliverer, newborn, seat, master, staging,
  and the rest of today's entries. A plain use that appears moves
  the word to the second kind, by the move rule of ADR-0074.
- Not decided here: the remaining candidates' entries beyond what the
  texts use today. A new sense gets its line before its first use,
  as before.
