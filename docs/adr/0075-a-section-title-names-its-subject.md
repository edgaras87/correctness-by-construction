# 0075. A section title names its subject

Date: 2026-10-29
Status: Proposed, opened under the commit plan for section titles

## Context

Since ADR-0070 a fact reference carries the title of the section it
names, so a title is read wherever a line points at it, not only at
its section. Facts-in-sync says what the title is for there: it
says what is there without opening it, and a number and title that
no longer match show a stale reference; the sentence says its point
in words, and the reference gives only the address
(`docs/conventions/facts-in-sync/` §3.1, *What it is*). A title over
30 characters is cut at a word boundary and ends in "…". Nothing
says how a title is written.

Measured 2026-10-29 over 96 living files outside history:

- 375 numbered titles; the median is 16 characters, 71 run past 30.
  Of 562 references that carry a title, 112 carry a cut one:
  "*The records table…*" 15 times, "*The agent's files never
  share…*" 11 times.
- 121 titles are statements or imperatives, *A rename is grepped at
  its commit*, *Material-first is a first-class mode, not a
  failure*; 35 of them run past 30. The rest are labels, *The
  artifact*, *The seats*, or one word.
- 106 titles are one word. 56 of them are *What*, *Why*, *Where*,
  *How*, *When* and *Anti-patterns*: the record sections of
  project-recording, §2 to §9 and §14, and agent-arrangement §2. 27
  references name one of these, "(… §2.4, How)", 9 of them in the
  container's record stubs. Read in a reference, *How* says nothing
  without its parent.
- 40 titles carry a gloss after a dash, colon or middle dot:
  *PLAN.md — the spine*, *The method — `delivery/method/`*, and the
  stack references' "§1 · Decide the Execution Environment — demands
  first, against the lived default", 77 characters.
- Since 2026-09-20, 24 titles changed their words under the same
  number. Labels changed as often as statements: *The rounds* became
  *The stages*, *The five links* became *The four links*.

Conventions §2.5 says each numbered section holds one subject, and
writing rule 1 puts the point in the first line. The one-word
channel names in the agent model, *ambient*, *pulled*, *pushed*, are
the model's own words and name their subject.

## Options considered

**What a title is:**
1. **A label naming the section's subject,** a noun phrase: *The
   records table*, *The stop at every boundary*, *Renames*. Taken.
   The section holds one subject, and the title names it; the point
   is the first sentence's. Around a reference the sentence already
   says the point, so a statement title says it twice: "never share
   a commit (… §2.3, *The agent's files never share…*)". A statement
   is a retelling of the rule that changes with it, and every
   reference is re-grepped when it does. A subject is short, so no
   reference cuts it.
2. **A statement of the point.** Rejected: 35 of 108 statement
   titles already run past 30 characters, and a rule pressed into 30
   characters is a slogan.
3. **Either, capped at 30.** Rejected: cheaper now, about 140
   titles against 230, but no check can say which kind a new title
   should be, and the mix the item noticed stays.

**Length:**
1. **At most 30 characters,** the reference's cut, so a title is
   carried whole. Taken; checkable by script.
2. **No cap, the reference cuts,** as today. Rejected: 112
   references carry a title that says less than its section does.
3. **A higher cap, 40.** Rejected: a subject fits 30, and 36 titles
   run past 40 anyway.

**The one-word record titles:**
1. **Retitled to stand alone:** *How a plan is written*, *What a
   plan is*, *A plan's anti-patterns*. Taken: the pattern stays
   visible across the records, and a reference says something.
2. **Exempt, as a repeated pattern.** Rejected: the pattern is
   written nowhere, and 27 references would keep saying *How*.

**The gloss:**
1. **Moved into the first sentence,** the path included; the title
   is one phrase. Taken.
2. **Kept as the title's second part.** Rejected: the gloss is what
   runs the title past 30, and writing rule 3 keeps parts apart.

**Scope:**
1. **Numbered sections and parts, in both seats.** Taken. The manual
   form's fixed headings, *What it is for*, *Decisions*, are the
   manual form's (`docs/conventions/conventions/` §2, *The manual*);
   a stage heading is the stages' (`docs/conventions/conventions/`
   §1.4, *Stages*); a numbered rule's bold lead is a rule, a
   sentence, and its reference is cut as today.
2. **Every heading.** Rejected: the fixed headings are the manual form's,
   chosen once, and a stage heading names a stage by its skill.

**The home:**
1. **The writing convention,** a tenth rule, both `writing.md`
   following. Taken: how a title reads is how a text reads.
2. **Facts-in-sync §3.1,** beside the cut. Rejected: that section is
   the reference's; a title is written before anything points at it.
3. **The conventions manual's body rule, §2.5.** Rejected: it would
   cover manuals only, and 170 of the 375 titles are elsewhere.

**When the titles change:**
1. **In round 3's read, as findings.** Rejected: 230 findings of one
   kind, each needing a title chosen by hand, would bury the round's
   other kinds.
2. **As a commit plan of their own,** by layer, after round 3's rule
   check and before its read, as the reference rewrite was. Taken.
   The rule check tries a doubt on a sample before 230 titles are
   written to the rule; round 3's read catches what the pass missed.

## Decision

1. **Writing rule 10:** a numbered section's title is a label naming
   the section's subject, a noun phrase of at most 30 characters.
   The point goes in the first sentence under it.
2. **A title stands alone.** It says its subject without its parent
   heading: *How a plan is written*, never *How*.
3. **A title is one phrase in sentence case,** with no gloss after a
   dash, colon or middle dot; a gloss, a path among them, opens the
   body instead. A path may be the title when it is the subject.
4. **Scope:** numbered sections and parts, `## N.` and `### N.M`, in
   both seats. The manual form's fixed headings, stage headings and
   a numbered rule's bold lead are not titles under this rule.
5. **Facts-in-sync §3.1 keeps its cut for a numbered rule's bold
   lead,** and points at rule 10 for a section's title. ADR-0070's
   decision 1, "a long title is cut to its first words", now holds
   for that case alone.
6. **The rule now, the retitles as their own commit plan,** by
   layer, after round 3's rule check and before its read. Each title
   is chosen by hand; its references are rewritten by script and
   grepped at the commit (`docs/conventions/facts-in-sync/` §3.3,
   *A rename is grepped…*).

## Consequences

- The writing manual's §2 gains rule 10 and its why; both
  `writing.md` follow, each in a commit of its own.
- Facts-in-sync §3.1 changes one sentence. The walk from it finds no
  follower that restates the cut.
- About 230 of 375 titles change, and about 270 references with
  them, in the retitle plan: the 71 long ones, the 60 one-word
  record titles, the 40 glossed ones, and the statements under 30.
  Among them, ARCHITECTURE.md's six area titles lose their paths to
  the body, project-recording's nine record sections lose their
  glosses, and the stack references' middle-dot numbering goes. Nine
  lines in the container's record stubs follow, so runs hold the
  older copy until a delivery.
- The 112 cut references become whole titles.
- Every new section asks one question at the commit: is the title a
  subject, 30 characters or fewer? A script can count the second.
- The one-word titles that are words of the model's own, *ambient*,
  *pulled*, stay: each names its subject.
- Not decided here: how a conversation-memory section is titled
  beyond this rule. Its sections are numbered and named after their
  items, and seven run past 30; the retitle plan treats them as any
  numbered section.
