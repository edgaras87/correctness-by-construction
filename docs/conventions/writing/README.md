# Writing

**How a text reads, never what it says.**

## What it is for

So that a text can be read once. The failure is lived, in CBC Run 3
(its repository, `never-oversold`). It wrote about 150,000 words of Markdown for 768
lines of production code, in long chained sentences, with coined
words never defined. Its reviewer asked "explain simpler" again and
again, and the same request is common here.

Knowing the lesson did not fix it:

- **"Explain plainly" sat in CBC Run 3's agent memory from 2026-09-20.**
  Its records still came out in the voice of the Agent Skills it read.
- **A polish pass after the fact** cost CBC Run 3 a Plan Step, and the voice
  was still not fixed.

At its retrospective, on 2026-10-11, CBC Run 3 wrote a one-page Agent
Rule that loads in every session (its `RETRO.md`, D2). Its Step 10
then rewrote its records under the Agent Rule, three times. Taken from CBC Run 3
on 2026-10-15 (ADR-0053).

## What this is made usable as

- **`delivery/container/.claude/rules/writing.md` — the Agent Rule,
  shipped**, held at `.claude/rules/writing.md` with no `paths:`, so
  it loads at the start of every session.
- **`docs/glossary.md` — the Concept Deliverer's glossary**, the list of
  Glossary Names rule 9 points at; its header comment holds the form of
  an entry. A CBC Run starts its own at the same path, a record that
  holds only the Names it defines.
- **The delivered Glossary Names, shipped as pinned copies,** one file
  per group, updated with every delivery:
  - `delivery/container/docs/glossary/container.md`, the shared Names;
  - `delivery/method/docs/glossary/method.md`, the concept's and the
    method's;
  - `delivery/spring-postgres/docs/glossary/stack.md`, the stack's.

  Each lands under `docs/glossary/` in a CBC Run.
- **`.claude/rules/writing.md` — the Concept Deliverer's**, derived from
  this page like the container's, not copied from it, and loaded
  the same way. It differs where the Convention Seat does: it covers the
  Agent Skills, Agent Rules, Output Shapes, Approaches on Trial, manuals, concept chapters and
  notes the Concept Deliverer writes; and its examples are this repo's.

This page explains; the Agent Rule states. What derives from this page is
that list. A change here runs the Change Walk on it; a change forced in it is checked
back against this page.

## The seats

A CBC Run writes under the Agent Rule from birth: its chat, its records, its
commits. The Concept Deliverer writes under its own: its chat and
records. Its Agent Rule also covers what CBC Runs read, since an agent copies the
voice it reads. So every new or changed line of an Agent Skill, Agent
Rule, Output Shape, Approach on Trial, concept chapter or note follows
it. So do the Concept Deliverer's manuals. The Concept Deliverer also
writes this page and the Agent Rule's Master Copy.

## 1. What it governs

It covers every text written:
chat answers, records, commit messages, code comments.

- **History keeps its words.** A closed devlog entry, an ADR or a
  commit body is not rewritten for its voice. The Agent Rule applies
  to every new or changed line.
- **An Agent Skill or an Agent Rule may be dense.** Its reader follows what it
  says, not how it says it. An agent copies the voice it reads, so
  the Agent Rule says outright that it sets the voice.
- **Plain is the default for every kind of text.** A kind of text
  gets another style only when plain has been shown to fall short
  there. The Agent Rule then names that kind and its style. None is
  named yet: CBC Run 3 put off a specification style until its claims
  had been judged in plain text (its `RETRO.md`, D14).

## 2. Why each rule

1. **Lead with the answer.** A reader who stops after one line
   still has the point. The reasons are for the reader who asks.
2. **Short sentences, one idea each.** A chained sentence has to be
   held whole before any of it makes sense.
3. **Label the parts.** Dashes and semicolons hide how many parts
   there are. A list shows the count.
4. **Show it with numbers.** A definition asks the reader to
   imagine the case. A worked example shows it, and shows a wrong
   rule as wrong.
5. **Plain words, not metaphor.** A metaphor has to be translated,
   and two readers translate it differently. CBC Run 3's retrospective
   names "costume", "weather" and "stage" as words to drop: the
   stage of a theatre, as in "the stage, not a victim". An Agent
   Skill's phase is an Agent Skill Stage (`docs/glossary.md`).
6. **Names are labels.** A reference reworded points somewhere
   else. A coined word that is not defined is a word the reader
   cannot check, so each is defined once, in the project's
   glossary. A number local to one record carries its owner outside
   it, because "GUARANTEE-3" means something different in every
   Invariant Slice Record.
7. **Cut what adds nothing.** Every extra sentence is one more
   thing to read before the point.
8. **Start from what the reader holds.** A label the reader does
   not hold stops them, however plain the sentence around it. Rule
   6 keeps a label exact; this rule makes sure it is understood.
   So a label, a section number or a coined word the reader may not
   know is said first in plain words.
9. **A defined thing has a Glossary Name of two or more words.**
   Owner or kind first, then the word, each word capitalized, written
   exactly: CBC Run, Plan Step, Agent Rule, Delivery Staging. A
   lowercase word is English and only English. A thing named by one
   English word makes the reader decide at every use which is meant,
   "staging" the exchange's or git's. Two words say what the thing is
   and whose. The capitals say it is defined before the words are
   read, as a contract's "the Deliverer" or Kubernetes' "a Pod" do.
   A Name built on another Name carries it whole: Agent Skill
   Template, never Skill Template, since a short form leaves its word
   for the reader to decide again. This holds however long the Name
   gets. A Name of more than 4 words, every word counted, is a trigger
   to look for a shorter true Name before it is accepted; when none is
   found, the long Name stands. The trigger is a count, so a script
   can find it. A
   hyphenated word counts as one, here and in the two words a Name
   needs: "never-event" is one word.
   Every Markdown mark already has a job here, so none marks a Name.
   Three things are written otherwise:
   - a numbered thing, by its owner and number: "working-a-reading
     rule 2", "the walk's step 3";
   - a label inside its owner, keeping its case: "Step 0" in a plan,
     "Stage 3" in an Agent Skill;
   - a path, as it is.

   A thing is defined when a text gives it a meaning
   English does not. Its Name goes into the glossary in the commit
   that first uses it, pointing at the home that defines it. A word
   whose English meaning is ours has no Name (rule 6).
10. **A section's title names its subject.** A title is read in every
    Fact Reference to its section, where the sentence already says
    the point. A title that states the point says it twice, and it
    changes when the rule does. A subject is short, so a title of 30
    characters or fewer is carried whole, never cut. It stands alone,
    since a reference shows no parent: *How a plan is written*, never
    *How*. A title is:
    - one phrase;
    - in sentence case, a Glossary Name inside it keeping its
      capitals;
    - with no gloss after a dash or colon: the gloss opens the body.

    This holds for numbered sections and parts in both Convention
    Seats. Three are not titles under it: the manual form's fixed
    headings, an Agent Skill Stage heading, and a numbered rule's bold
    lead.
11. **An edit changes the lines its change needs.** The reviewer
    reads a diff at every commit boundary, for its change; a line
    rewrapped beside it hides the change among lines that did not
    need to move. Markdown has no line width here. A reader meets the
    text rendered, or in an editor that wraps. 985 lines in 83 of the
    99 living files already run past 72. The 72 is
    the commit-messages manual's rule for a body and nothing else
    (`docs/conventions/commit-messages/` §2.1, *Conventional Commits*).
    A scripted pass is held to the same rule: it counts headings,
    references and code fences before and after, and changes nothing
    on a second run.

*Its story: devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model; devlog 2026-10-19; ADR-0074 to ADR-0077, rules 9 to 11; devlog 2026-10-29, the lessons' own stories: six places.*

## Why it arrives this way

An Agent Rule with no `paths:`, loaded in every session
(`docs/conventions/agent-arrangement/` §3.9, *An Agent Rule always loaded*). Its moment is every
answer and every record written, and nothing else fires at all of
them (`docs/models/agent.md` §8, *Choosing a channel*):

- **A Paths Rule** loads when a file is touched, after a new one's
  first draft is written. Chat has no path
  (`docs/conventions/agent-arrangement/` §5.6, *Rules files*). CBC Run 3's first
  draft loaded on Markdown files, and was dropped for this.
- **An Agent Skill** fires when the agent notices the moment. The failure
  here is not noticing: the agent writes in the voice it last read.
- **Memory or `CLAUDE.local.md`** held the lesson in CBC Run 3 and did
  not act. The local file is also one person's, and reaches no CBC Run.

The cost is one page in every session, which is why the Agent Rule
stays one page.

## What this does not cover

- **Where a fact lives** — `docs/conventions/facts-in-sync/` §1, *One home*.
- **Which record owns which kind of fact** —
  `docs/conventions/project-recording/` §13, *The records table*.
- **The form of a commit message** —
  `docs/conventions/commit-messages/`.
- **The form of a manual** — `docs/conventions/conventions/` §2, *The Convention Manual*.
- **What a kind of output looks like** —
  `docs/conventions/shapes/`.
- **How an Agent Rule reaches an agent** —
  `docs/conventions/agent-arrangement/` §5.6, *Rules files*.

## Where to look

- The decision: ADR-0053.
- The Agent Rule: `delivery/container/.claude/rules/writing.md`.
