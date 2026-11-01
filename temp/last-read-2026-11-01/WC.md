# Reader WC: Writing, the last read

Finding Kind: Writing, rules 1 to 10. Read at `70404e1`.

Files, each read whole: `docs/conventions/repo-hygiene/README.md` and
its 3 `.part` templates, `docs/conventions/retrospective/README.md`,
`docs/conventions/shapes/README.md`,
`docs/conventions/visual-comparison/README.md`,
`docs/conventions/writing/README.md` (also read as a text under its own
rule), `docs/glossary.md`.

Script hits for these files: none (`hits-wc.txt` is empty).

3 findings: 1 checked, 2 resting on the reader, 0 uncertain.

## Findings

### WC-1

- **Where:** `docs/glossary.md`, group *Kinds of text*, the Idea Model
  entry, lines 121-123.
- **Quote:** `repo writing its own Convention Manual for it. A repo adapts it in a Convention Manual`
- **The rule:** writing rule 7, "Cut what adds nothing. If a sentence
  can go without losing meaning, it goes." (`.claude/rules/writing.md`
  rule 7; `docs/conventions/writing/` §2, *Why each rule*, rule 7).
- **What the text says:** the entry says twice, back to back, that a
  repo adapts an Idea Model in its own Convention Manual. First as a
  clause: "each repo writing its own Convention Manual for it". Then
  as a sentence: "A repo adapts it in a Convention Manual". The second
  adds only the Fact Reference.
- **Stands:** checked. The two lines are in the tree as quoted.
- **Why it was missed:** missed at the change. `b379c2d` ("the
  glossary meets the rule again", Round 3's close read) replaced the
  figure "like an interface" with the clause, beside a sentence that
  already said it. The rule 7 read at that commit's review should have
  caught it.
- **Proposed:** fix: "an idea any repo can adapt, its rules varying by
  repo. Each repo adapts it in a Convention Manual of its own
  (`docs/models/idea-to-output.md` §2, *The kinds*, and §5, *An Idea
  Model and a concept*)."

### WC-2

- **Where:** `docs/glossary.md`, group *Kinds of text*, the Canonical
  Description entry, lines 113-120.
- **Quote:** `reference, not that it is correct. It is today's understanding,`
- **The rule:** writing rule 7, "Cut what adds nothing"
  (`.claude/rules/writing.md` rule 7).
- **What the text says:** the entry's first lines say a Canonical
  Description is "how we understand a thing today" and "may be wrong
  or incomplete". Its last lines say both again: "'Canonical' means
  the reference, not that it is correct. It is today's
  understanding". Only "changed only for a reason that is recorded"
  is new.
- **Stands:** resting on the reader. The repeat is in the tree. Whether
  the sentence on the word "Canonical" adds meaning is judgement.
- **Why it was missed:** missed at the change. `a575fb5` split the
  entry's first sentence into "It may be wrong or incomplete. It is
  the one that counts regardless."; `b379c2d` reworded the closing
  sentence in plain words. Neither weighed the two against each other
  under rule 7.
- **Proposed:** fix: lines 118-120 become "they differ at the edges
  (ADR-0039). It changes only for a reason that is recorded."

### WC-3

- **Where:** `docs/conventions/shapes/README.md`, *What it is for*
  line 13; §2, *What an Output Shape is not*, lines 134-138; *What
  this does not cover*, line 333.
- **Quote:** `hidden for opposite reasons. Trial evidence is withheld **so that it`
- **The rule:** writing rule 9: "A thing is defined when a text gives
  a word a meaning English does not: its Name goes into the glossary"
  (`.claude/rules/writing.md` rule 9; `docs/conventions/writing/` §2,
  rule 9). Writing rule 8: a word the reader may not hold is said
  first in plain words.
- **What the text says:** "trial evidence" has a meaning of this
  repo's own: material in `docs/baselines/` withheld from every CBC
  Run, so that a later derivation can be measured for independence
  (ADR-0035 decision 6, ADR-0033). The manual uses it at line 13
  before saying what it is, and §2 gives the meaning only by contrast
  with an Output Shape. It has no Glossary Name, and it sits beside
  two Names it could be taken for: Approach on Trial, and the method's
  Evidence Test. "A derivation" (line 137) is not said either.
- **Stands:** resting on the reader. The uses are in the tree, and no
  glossary lists it; whether its meaning is English is the judgement.
  Not raised in any of Round 3's decisions (searched for "trial
  evidence" and "baseline").
- **Why it was missed:** the rule is unclear on a phrase made of two
  English words whose sum is ours. DECISION-23 settled such phrases
  one by one ("living text", "receipt branch"); this one was not met.
  Older than ADR-0076's rule 9.
- **Proposed:** question: (a) a Glossary Name, such as Trial Evidence,
  with shapes §2 or a Local Map in `docs/baselines/` as its home; its
  other living uses, `ARCHITECTURE.md` line 248 and `TODO.md` line
  717, follow; or (b) English, said once in plain words at shapes line
  13: "material kept in `docs/baselines/` and never shown to a CBC
  Run, so its work can be measured blind".

## Found true, so not listed

- Every numbered title in the five manuals is 30 characters or fewer,
  one phrase, with no gloss; the longest is shapes §4, 29.
- No Glossary Name is written in lowercase or in the wrong case in the
  nine files (each of the 173 Names searched, case-folded). "*Local
  rules* slot" (glossary 172) is a heading, written as it is.
- Bold Names: each is at its home or opens a list item (Hygiene Base
  and Stack Overlay in repo-hygiene §2, Output Shape in shapes §1.1).
  Shapes' bold phrases ("**so that it stays**", "**only until the
  Plan Step Gate**", "**finding**") mark emphasis, not a Name.
- Local numbers carry their owner: "its `RETRO.md`, D2", D14, D23,
  D24; "its `aa9b3ec`", "its `5336563`"; "ADR-0027 decision 3".
- A convention is never named by its bare word; "the exchange" in
  writing rule 5's and rule 9's examples is the English process.
- "Release" (retrospective 12, 23, 34, 37, 102) is the playbook's step
  label, given its owner at first use.
- "The Plan Step that makes the stack true" with its plain gloss
  (repo-hygiene 17-18) is the agent's call on FINDING-1026.
- *Why it is shaped this way* (visual-comparison §2), "fighting a
  notation", "load-bearing", "day zero": settled by DECISION-20 and
  DECISION-26.
- The `.part` templates' comments: short, plain, and the markers name
  the Stack Overlay; the marker mismatch is leftover C9.
- The leftovers for these files still stand where step 1 put them: C1
  (writing 67), C4 (writing 175), C5 (writing 167), C6
  (visual-comparison 55), C7 (shapes 305), C9 (editorconfig.part 3),
  C10, C11 (glossary 44-45, retrospective 89). Not listed again.

## Met in passing

- `docs/glossary.md` 168-171, the Agent Rule entry: "The kinds in use:
  a Local Rule; a Paths Rule; and Claude Code's permission and deny
  rules". A Local Rule is a line in the Entry File, and the permission
  rules sit in `.claude/settings.json`. Neither is a file under
  `.claude/rules/`, which is what the entry says an Agent Rule is.
- `docs/conventions/writing/README.md` §1 line 70: "An Agent Skill or
  an Agent Rule may be dense." *The seats* (lines 56-59) says every
  new or changed line of an Agent Skill or Agent Rule follows the
  Agent Rule. The bullet's body is about reading a dense text, as our
  `writing.md` *Where it applies* puts it.
- `docs/conventions/shapes/README.md` §4.1 lines 192-196: the italic
  paragraph tells the case (ADR-0037's fetch, CBC Run 3's two closes)
  instead of pointing at its story, as leftover B5 found in
  commit-plan.
- Leftover W1 (the writing manual's *What this is made usable as*
  lacks `delivery/container/docs/glossary.md`) is a little weaker than
  stated: line 32-33 says "A CBC Run starts its own at the same path",
  so the Record Stub is named in words, though not by its path.
