# Writing

**How a text reads: the answer first, short sentences, plain words,
real numbers. One page of rules, loaded in every session, for chat
and records alike. What a text says is never this convention's.**

## What it is for

So that a text can be read once. The failure is lived, in run 3,
never-oversold. It wrote about 150,000 words of Markdown for 768
lines of production code, in long chained sentences, with coined
words never defined. Its reviewer asked "explain simpler" again and
again, and the same request is common here.

Knowing the lesson did not fix it:

- **"Explain plainly" sat in run 3's agent memory from 2026-09-20.**
  Its records still came out in the voice of the skills it read.
- **A polish pass after the fact** cost run 3 a step, and the voice
  was still not fixed.

At its retrospective, on 2026-10-11, run 3 wrote a one-page rule
that loads in every session (its RETRO.md, D2). Its Step 10 then
rewrote its records under the rule, three times. Taken from run 3
on 2026-10-15 (ADR-0053).

## What this is made usable as

- **`delivery/container/.claude/rules/writing.md` — the rule,
  shipped**, held at `.claude/rules/writing.md` with no `paths:`, so
  it loads at the start of every session.
- **`.claude/rules/writing.md` — the deliverer's**, derived from
  this page like the container's, not copied from it, and loaded
  the same way. It differs where the seat does: it covers the
  skills, rules, shapes, manuals, concept chapters and notes the
  deliverer writes, and its examples are this repo's.

This page explains; the rule states. What derives from this page is
that list. A change here walks it; a change forced in it is checked
back against this page.

## The seats

A run writes under the rule from birth: its chat, its records, its
commits. The deliverer writes under its own: its chat and records,
and also what runs read, since an agent copies the voice it reads.
Every new or changed line of a skill, rule, shape, manual, concept
chapter or note follows it. The deliverer also writes this page and
the rule's master.

## 1. What it governs

How a text reads, never what it says. It covers every text written:
chat answers, records, commit messages, code comments.

- **History keeps its words.** A closed devlog entry, an ADR or a
  commit body is not rewritten for its voice. The rule applies to
  every new or changed line.
- **A skill or a rule may be dense.** Its reader follows what it
  says, not how it says it. An agent copies the voice it reads, so
  the rule says outright that it sets the voice.
- **Plain is the default for every kind of text.** A kind of text
  gets another style only when plain has been shown to fall short
  there. The rule then names that kind and its style. None is named
  yet: run 3 left a specification style for its claims to be judged
  on plain text first (its RETRO.md, D14).

## 2. Why each rule

1. **Lead with the answer.** A reader who stops after one line
   still has the point. The reasons are for the reader who asks.
2. **Short sentences, one idea each.** A chained sentence has to be
   held whole before any of it makes sense. Run 3's records were
   full of them (its RETRO.md, D2).
3. **Label the parts.** Dashes and semicolons hide how many parts
   there are. A list shows the count.
4. **Show it with numbers.** A definition asks the reader to
   imagine the case. A worked example shows it, and shows a wrong
   rule as wrong.
5. **Plain words, not metaphor.** A metaphor has to be translated,
   and two readers translate it differently. Run 3's retrospective
   names "costume", "weather" and "stage" as words to drop: the
   stage of a theatre, as in "the stage, not a victim". A skill's
   phase is a stage, a defined word (`ARCHITECTURE.md`, *The
   words*).
6. **Names are labels.** A reference reworded points somewhere
   else. A coined word that is not defined is a word the reader
   cannot check, so each is defined once, in the project's
   glossary. A number local to one record carries its owner outside
   it, because "GUARANTEE-3" means something different in every
   slice record.
7. **Cut what adds nothing.** Every extra sentence is one more
   thing to read before the point.

*Measured in run 3, 2026-10-11 to 10-15: the rule written at the
retrospective, kept at its close, and used for three rewrites of
the records in Step 10.*

## Why it arrives this way

A rule with no `paths:`, loaded in every session
(`docs/conventions/agent-arrangement/` §3.2). Its moment is every
answer and every record written, and nothing else fires at all of
them:

- **A `paths:` list** loads when a file is read, not when one is
  written, and chat has no path. Run 3's first draft loaded on
  Markdown files, and was dropped for this.
- **A skill** fires when the agent notices the moment. The failure
  here is not noticing: the agent writes in the voice it last read.
- **Memory or `CLAUDE.local.md`** held the lesson in run 3 and did
  not act. The local file is also one person's, and reaches no run.

The cost is one page in every session, which is why the rule stays
one page.

## What this does not cover

- **Where a fact lives, and which record owns it** —
  `docs/conventions/project-recording/` §11.
- **The form of a commit message** —
  `docs/conventions/commit-messages/`.
- **The form of a manual** — `docs/conventions/conventions/` §3.3.
- **What a kind of output looks like** —
  `docs/conventions/shapes/`.
- **How a rule reaches an agent** —
  `docs/conventions/agent-arrangement/` §3.2.

## Where to look

- The decision: ADR-0053.
- The rule: `delivery/container/.claude/rules/writing.md`.
