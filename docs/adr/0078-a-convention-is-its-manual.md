# 0078. A convention is its manual, its footers stay here, its Names ship as copies

Date: 2026-10-31
Status: Proposed, the save point before the commit plan for the
refinement's design of DECISION-19, 29 and 32, which opens next.

## Context

Refinement Round 3's read found 644 findings against the writing
rule (`temp/refinement-2026-10-18.md`, *Round 3: how it reads*). Three
of its seventeen decisions change how the repo works, not only what
its text says, so the refinement builds them as a design before the
round's work (`.claude/approaches-on-trial/refinement.md` §2.7,
*Working the findings*):

- **DECISION-19:** the words the concept, the method and the stack
  give a meaning English does not are Glossary Names, as the CBC
  Run's own writing rule 9 already asks. About 100 such words stood
  in the shipped Agent Skills with no Name.
- **DECISION-32,** raised by the reviewer: a convention is its
  manual's level. The Idea-to-Output Model had a convention as two
  texts, its manual and its artifacts
  (`docs/models/idea-to-output.md` §6.1, *The manual's level*), and so spanned
  two levels of its own chain. With it, DECISION-24 and 27: an agent
  part is always named with its kind, "the commit-plan manual", "the
  commit-plan Agent Skill".
- **DECISION-29:** decision numbers are ours. A CBC Run can neither
  open our ADRs nor needs them to change its copies.

Measured at `629ff89`, over living text:

- decision citations: 31 footer lines and 5 in sentences in our Agent
  Skills and Agent Rules; 8 in sentences in our Approaches on Trial;
  33 footer lines in the Container Group's 9 Agent Skills and Agent
  Rules; 20 in sentences in 18 files of the Method Group and the
  Stack Group, which have no footers;
- the concept's words: slice 452 hits in 49 files, framing 174, kill
  162, ground 143, promise 112, wall 101, harness 85, fold 59, census
  35, witness 28;
- "skill": 603 lines in 79 files, 81 of them inside Skill Stage or
  Skill Template; "artifact": 95 uses in 32 files, in two senses;
- five names shared by a manual and an Agent Skill or Agent Rule:
  commit-messages, commit-plan, visual-comparison, retrospective,
  writing.

A record is delivered once and never updated
(`docs/conventions/exchange/` §2.4, *The records' exception*), so a
Name added to a CBC Run's glossary record after its birth never
reaches it, while the Agent Skills that use the Name update at every
delivery.

The reviewer decided each part below as a question, 2026-10-31.

## Options considered

1. **Delivered Names, at birth only,** by a Delivery Fill into the
   CBC Run's glossary. Rejected: a CBC Run's glossary falls behind
   its own Agent Skills. Also rejected: the Delivery Take writing new
   Names into the record, which breaks the records' exception.
2. **The concept's words as one capitalized word,** "a Slice", or
   kept lowercase. Rejected: a capital at a sentence's start or in a
   heading shows nothing, a grep cannot check it, and an exception
   for core words spreads. Lowercase leaves the reader guessing.
3. **Only the troublesome words named,** those that clash or that a
   reader met unexplained. Rejected: the rest stay unjudged, and a
   sweep needs every Name listed.
4. **The Agent Model's words left as its own.** Rejected: the Tiers
   Model's words already have Names.
5. **Every Name written twice,** in our glossary and in the delivered
   file. Rejected for the concept's, method's and stack's Names, which
   read the same for both seats.
6. **"Artifacts" kept on the convention side.** Rejected: the method
   uses the word for framing's three documents, and Work Approach is
   already the Name for these files.
7. **Agent Skill only where a sentence could mislead,** or Skill
   Stage and Skill Template kept as they are. Rejected by the
   reviewer: the kind word is written always.
8. **Renaming one side of the five shared names now,** the manuals by
   their subject or the Agent Skills by their act. Deferred, not
   rejected: CBC Runs 4, 5 and 6 were built with these names and are
   still to be read. A naming grammar alone was weighed and found not
   to prevent clashes: all 12 manuals and all 10 Agent Rules are
   nouns, and a strict "verb first" for Agent Skills would rename 11
   of 12.
9. **Decision footers removed from the Master Copies,** so a copy
   still equals ours byte for byte; this was DECISION-29's first
   ending. Reversed by the reviewer: the footer serves us beside the
   rule it backs, and a strip at delivery keeps that. Also rejected:
   a list of each shipped file's decisions kept apart, a second home.
10. **Three ADRs,** one per part. Rejected: the parts lean on each
    other.
11. **The renames as a pass inside the design.** Rejected: round 3's
    work opens every file anyway, so a file is opened once.

## Decision

**What a convention is**

1. **A convention is the Canonical Description of a way of working,
   its manual.** The Work Approaches made from it, its Agent Skills,
   Agent Rules and Output Forms, sit one level down, as for any
   Canonical Description (`docs/models/idea-to-output.md` §2, *The
   kinds*). The model's §6 states only what makes a convention
   differ from the concept: its manual stays here, only its Work
   Approaches reach a CBC Run, its rules may be broken with a reason
   given, and it has no version. A CBC Run holds no convention, only
   Work Approaches made from ours. "Artifact" leaves our side; the
   conventions manual's §1 is retitled.
2. **An agent part is always named with its kind:** the commit-plan
   manual, the cbc-slice Agent Skill, the one-home Agent Rule, writing
   rule 9 for a numbered line, and a path whenever a sentence points
   at where a fact is written. Agent Skill is a Glossary Name; every
   "skill" that means the file becomes it. Skill Stage becomes Agent
   Skill Stage, and Skill Template Agent Skill Template.
3. **The five shared names stay for now.** A new name never repeats
   a manual's, an Agent Skill's or an Agent Rule's, checked by grep
   before it is given; a new Agent Skill takes a verb. The renaming is
   TODO's "Rename the manuals, Agent Skills and Agent Rules that share
   a name", due when the Run Readings of CBC Runs 4, 5 and 6 have
   closed.

**Decision citations**

4. **One rule for citing a decision, in `docs/conventions/facts-in-sync/`
   §3, *The Fact Reference*,** since a citation points at the home of
   a why. The one-home Agent Rule carries it to both seats, and the
   conventions manual §1.1 points at it:
   1. a manual cites decisions inside its sentences;
   2. a record does the same;
   3. every Work Approach lists the decisions it rests on once, in a
      *Decisions* footer, never inside a sentence;
   4. each seat cites its own decisions as `ADR-nnnn`, a CBC Run its
      own in its own files;
   5. a copy we deliver has its footer stripped at delivery;
   6. a Record Stub and an Agent Skill Template cite nothing.
5. **Our Master Copies keep their footers; every delivery strips
   them.** The strip runs in the Pure Seed and in `exchange-deliver`
   when a delivery is staged, and on our side before `exchange-read`
   compares a CBC Run's copy with ours. It cuts the `---` line and the
   `## Decisions` section below it, and nothing else. A CBC Run's copy
   equals its Master Copy at the Delivery Pin without that footer;
   the exchange manual and the delivered-copies Agent Rule say so. A
   CBC Run never writes a footer on our copy: an edit's reason goes to
   its Decisions Log, as now.
6. **Our own copies of shipped Agent Skills keep their footers,**
   citing `ADR-nnnn`.
7. **A script lists every decision citation** by file, kind of text
   and place, footer or sentence, and shows each that breaks the
   rule. Run once in the design's commit plan, it brings every text in
   line: the 5 in our Agent Skills, the 8 in our Approaches on Trial
   and the 20 shipped go to footers. It then runs as part of the
   sweep.

**The glossary**

8. **Delivered Names are pinned copies,** one file per group, updated
   with every delivery: `docs/glossary/container.md`, the shared
   Names; `docs/glossary/method.md`, the concept's and the method's;
   `docs/glossary/stack.md`, the stack's, swapped with the stack.
   Each lives in its group's folder here. A CBC Run's
   `docs/glossary.md` stays its record and holds only its own Names:
   its problem's words, and its Approaches on Trial's, marked on trial
   and read at each Run Reading, a general one harvested into ours.
   This replaces DECISION-19's Delivery Fill.
9. **Our `docs/glossary.md` keeps its groups.** The Names only we use,
   the Agent Model's among them, and the shared Names have full
   entries there. The concept's, the method's and the stack's Names
   are written once, in the delivered file, and our glossary's group
   points at it. The shared Names exist twice, ours and the CBC Run's
   follower in `container.md`; a script checks that both list the
   same Names.
10. **Every candidate word is judged in one table** before anything
    is renamed: the concept's ten, the method's, the stack's and the
    Agent Model's, with the Names the decisions already gave, Entry
    File, Living Text, Receipt Branch, Hygiene Base and Agent Skill.
    Each row gets a Name of two words, owner or kind first, with a
    one-line reason and its common compounds, or "English", with why.
    The reviewer judges one group at a time. FINDING-507's decline in
    DECISION-20 reverses: the Agent Model's six channel titles become
    their Names.

**The build**

11. **One commit plan, in this order:** this ADR; the model and the
    conventions manual; the citation rule and the strip; the
    glossary's structure; the table. The renames that give old text
    its new Names are done in round 3's work, file by file, with each
    file's findings. This ADR is accepted at the plan's close.

**What changes in part:** ADR-0069's decision 1, where a CBC Run's
copy cited `CBC ADR-nnnn`: a delivered copy now carries no citation.
ADR-0076's decision 2, the glossary as one list: the delivered Names
now live in three pinned files. ADR-0036's copies equal to their
Master Copies: now without the footer. None of the three is edited.

## Consequences

- **A reader always knows what kind of thing is named,** and a CBC
  Run's glossary keeps up with its own Agent Skills.
- **A CBC Run reads no pointer it cannot follow;** we keep ours beside
  the rule it backs.
- **The exchange gains a step,** the strip, in three places; a strip
  forgotten in one shows as false differences in a read.
- **Round 3's work grows:** each file it opens also takes its new
  Names, about 1,350 hits for the concept's words, 520 for Agent
  Skill, 107 for Entry File, each read by hand.
- **The five shared names still meet in a grep** until the renaming
  item is worked.
