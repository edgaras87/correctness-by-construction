# Commit plan: round 3's rule check

## Summary — the state after all commits

Round 3's rule check is written in the refinement's file and ended.
Its one rule, `writing.md` on the writing manual, was read whole with
what changed since round 2's check; three doubts were tried on
samples and the reviewer decided each on 2026-10-29. Rule 9 gains
two sentences: a word of another part of speech is another word, and
a listed word's entry names every sense in use with its subject, ours
and others' alike, a use staying bare only where it is casual
English. The glossary lists seven more words of the second kind:
plan step, skill stage, a cbc run's take, idea model, decisions log,
repo tag and cbc run; each entry is a contents page, one line per
sense and the address of its home, and the entries already listed
gain the named senses in use. Rule 11
says an edit changes the lines its change needs and no others, and
Markdown has no line width. Both `writing.md` carry rules 9 and 11
as the manual states them. Two TODO items are closed, and the
retitle item becomes the plan for the words-and-titles pass, which
runs before round 3 reads: about 800 lines take their subject and
about 230 titles become labels, by layer. ADR-0076 and ADR-0077 are
Accepted; ADR-0074's decisions 2 and 8 are changed in part by the
first, with no accepted ADR edited.

## Commits

**1. `docs(agent): add commit plan for round 3's check`**
This file.

**2. `docs(temp): round 3's rule check written`**
The refinement's file gains *Round 3: how it reads* with the check:
what changed, the six items, the three doubts with their trials and
the reviewer's decisions, and the files by layer. The Writing row in
*Kinds and rounds* widens to all living text.

**3. `docs: ADR-0076 rule 9 refined, the pass first`**
Proposed. The two refinements to rule 9: a word of another part of
speech is another word, and an entry catalogues every sense in use.
Seven words listed: step, stage, take, model, log, tag and run, each
with the senses the texts use; the noun "fill" gone; the words pass
before round 3's read. Names what it changes in ADR-0074.

**4. `docs: ADR-0077 an edit changes only its lines`**
Proposed. Rule 11 and the ways rejected: a width as a guide, a
change about as long as what it replaces.

**5. `docs: rule 9 refined, log and tag join the list`**
The writing manual's rule 9 gains its two sentences. The glossary's
header says an entry is a contents page: the home defines, the entry
points. Entries of the second kind for step, stage, take, model, log,
tag and run, each sense with its subject and its home's address; the
entries for rule, shape, form, template and stub gain the named
senses in use. One commit: the sentences and the entries are one
rule as it now reads.

**6. `docs: writing rule 11, an edit changes its lines`**
The writing manual's §2 gains rule 11 with its why.

**7. `chore(agent): our writing.md takes rules 9 and 11`**
Our agent rule follows the manual, in a commit of its own
(`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*).

**8. `fix(delivery): shipped writing.md takes 9 and 11`**
The container's copy follows the manual, with the run's examples.

**9. `docs: the check's items close, two ADRs accepted`**
ADR-0076 and ADR-0077 flip to Accepted. TODO: the remaining-words
item and the edit-shape item leave; the retitle item is rewritten
as the words-and-titles pass, a commit plan due before round 3
reads, with the thirteen labels as its sample. `PLAN.md`'s Now line
says where the refinement is: before round 3's read, at the pass.

**10. `docs(temp): round 3's rule check, how each ended`**
The check's endings, one per doubt, with the commits that hold
them, as round 2's check wrote its own.

**11. `docs(agent): close commit plan for round 3's check`**
Deletes this file; the body says what diverged.

**12. `docs: devlog for round 3's rule check`**
The entry for the set, with the session-end lines.

## Decisions taken inside this plan

- **The thirteen labels wait for the pass.** They were the trial for
  rule 10 and read right; writing them now would start the retitle
  by hand, outside the plan that does it by script and hand together.
- **Two ADRs, not one.** Rule 9's refinements and rule 11 are two
  decisions with different reasons and different rejected options.
- **The check is written before its fixes land, and its endings
  after,** in two `docs(temp)` commits, as round 2's check was.
- **Every sense in use is catalogued** (revision of 2026-10-29,
  before commit 2). The reviewer asked for every variation a listed
  word is used in, "plan step" but also a rule's step, and for a
  rule that says so. The entry lists each sense with its subject and
  points at the home that defines it; a casual use, where no subject
  would be true, stays bare. The mark sentence first proposed for
  rule 9 goes: no first-kind word needs it once step and model are
  listed.
- **Step, stage, take and run are listed too** (the same revision).
  Step has three noun senses in use and its plain sense keeps
  coming; stage has a skill's and an approach's; take and run have
  one noun sense each, but the reviewer chose a prefix for every word
  discussed, so that a bare word is English and nothing else: "a
  cbc run's take", "cbc run", 964 lines. A text's numbered step is
  named by its owner, "the walk's step 3", not by a kind.
- **Model is listed, not marked** (revision of 2026-10-29, before
  commit 2). The plan first kept "model" bare and marked Claude's 29
  uses. The reviewer asked why; the shipped text already says world
  model, adversity model, data model and role model, so a bare
  "model" tells a reader nothing, and the rule's own test says second
  kind. About 208 generic uses become "idea model" in the pass.
- **No commit is provisional.** The four decisions are the
  reviewer's, taken one by one on 2026-10-29.
