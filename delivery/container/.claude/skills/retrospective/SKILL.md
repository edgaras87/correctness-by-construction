---
name: retrospective
description: Walk a finished CBC Run part by part and decide what the next CBC Run does differently. Use when the CBC Run has finished building, before Release, or when the reviewer asks for a retrospective, a look back, or "what would we do differently". Do NOT use to fix this CBC Run's records; that is the apply-retrospective Agent Skill, after this.
foundation: the retrospective convention
---

# Retrospective

The CBC Run stays as it is. Its lessons go to the next CBC Run, through what
the next CBC Run starts from: the Agent Skills, the Agent Rules, the
playbook the Plan Steps came from, the Agent Skill Templates, the
reviewer's `CLAUDE.local.md`. A lesson that lands nowhere is
repeated.

The reviewer decides everything. The agent reads, measures, finds,
proposes and writes.

## Stage 0 — open

1. **Cut a branch,** `retrospective`, from main. Main is not touched
   until the retrospective lands. Ask the reviewer whether small commits are
   free on it.
2. **Write the note,** `RETRO.md` at the root, with these sections:
   - **Goal:** the CBC Run stays as it is; lessons go to the next CBC Run.
   - **Rules:** the branch, the `try/` branches, how commits work,
     one decision at a time.
   - **Parts:** a table of the CBC Run's parts, in the order the CBC Run
     built them, each with its files and a status: not started, in
     progress, done (date).
   - **Do differently:** one block per part.
   - **Delivering the retrospective:** what reaches the next CBC Run, and how.
   - **Experiments:** one line per `try/` branch.
   - **Parked:** questions raised in one part that belong to
     another, each naming that part.
3. **Explain the CBC Run to the reviewer first:** how work is done, what
   is read when, what you think is good and what is costly. Use
   numbers: words of records against lines of code, commits by kind.
   The first candidates for decisions come from this.

## Stage 1 — walk each part, in order

1. **Read the part's files in full.** Then measure: sizes, counts,
   how often a thing appears, where one fact is written twice.
2. **Find what went wrong or cost too much.** Ask of the part:
   - Which Plan Steps took much longer or shorter than planned, and why?
   - What needed to happen earlier?
   - Which ways of working were tried and dropped?
   - What work had no home in the plan?
   - Which Plan Step Gate items caught nothing?

   Each finding needs a real example from the CBC Run: a quoted line
   with its file and line number, or a count. A finding without an
   example is dropped.
3. **Say what worked.** "Kept as it is", with the reason, is a valid
   result for a part.
4. **Group the findings into a few decisions.** Then go to Stage 2.
5. **Mark the part done** in the table when its last decision is in.

## Stage 2 — one decision at a time

1. **Show the reviewer one decision:**
   - the problem, with its example;
   - the change;
   - where it lands;
   - a recommendation.

   Where there is a choice, show the variants applied to real text
   from the CBC Run, side by side, before asking.
2. **When the reviewer asks for a simpler explanation,** give one,
   with an example, before changing anything.
3. **On agreement, write the decision into the note and stage it.**
   Commit on the reviewer's word. Then show the next one.
4. **A decision block holds, in order:**
   - **D<n>. The decision as a sentence.** (date)
   - What happened in the CBC Run, with the example.
   - The change, as bullets.
   - **Considered and rejected:** each option that was on the table,
     with its reason. Only when there was one.
   - **Lands in:** the named places.
5. **When the reviewer corrects you,** the corrected version is the
   decision, and your first version goes under "Considered and
   rejected", with the reviewer's reason.

## Rules for a decision

- **"Lands in" names a place the next CBC Run starts from.** "Remember
  to" is not a place.
- **Stay inside the question asked.** A new question goes to Parked,
  with the part that owns it.
- **No decision without something that went wrong.** A good idea
  with no failure behind it is dropped.
- **Judge on real text, never before it exists.** A question that
  needs text the CBC Run has not written yet waits for the moment it
  will exist, listed under *Parked*.
- **Do not fix the CBC Run's records.** The one exception is Stage 4,
  item 3: the CBC Run's own CBC Run Asks.

## Stage 3 — try a change on a branch

A change worth testing during the retrospective, such as a new rule,
goes on `try/<what>`, cut from `retrospective`, and is used for the
rest of the retrospective. At the close the reviewer keeps it or
drops it. Kept: `retrospective` fast-forwards to it. Dropped: the
branch is deleted, and the commits to `RETRO.md` made on it are copied back to `retrospective`. The note's Experiments line records which.

## Stage 4 — close

1. **Every part is done,** and every Parked item is judged or still
   names its part.
2. **The Entry File is read top to bottom.** Every line still passes
   the three tests in the comment above its *Local rules*, or leaves.
3. **The CBC Run's own CBC Run Asks close into the note.** Each CBC Run Ask
   in TODO's "To the deliverer" that a decision answers becomes one
   line naming that decision. The Decisions Log gets a "rules in
   force now" list on top, with what each rule replaced.
4. **What only the next CBC Run can check becomes its Plan Step Gate items.** List
   them in the note, each with the Plan Step that judges it. The
   Concept Deliverer writes each into the playbook the next CBC Run is
   born with, at that Plan Step, with one line of reason, naming the
   decision.
5. **One TODO line asks the Concept Deliverer to apply the note's
   decisions.**
6. **A devlog entry,** ending with a "Resume:" line, and TODO's Now
   updated.
7. **Land it.** The closing look at the landed commits, and the
   `-detail` branch that keeps what was tried, are the commit-plan Agent Skill's
   (`.claude/skills/commit-plan/SKILL.md` §4, *The lifecycle*, and §6.2, *Small commits*). The branch,
   `retrospective`, reaches main by fast-forward, on the reviewer's
   word (`PLAN.md`, *The Plan Step Form*, *At the close*).
8. **Then apply it to this CBC Run,** before Release:
   `.claude/skills/apply-retrospective/`.

## Between sessions

PLAN's "Now:" line and the devlog's last "Resume:" line say where
the retrospective stands. The note holds every decision, so a new session
reads those two, then the note.

---

## Decisions

- ADR-0054 — the retrospective is a convention, its look and
  its apply step two Agent Skills, taken from CBC Run 3's
