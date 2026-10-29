# Commit plan: a section title names its subject

## Summary — the state after all commits

TODO's item "Decide how a section title is written" is decided under
ADR-0075. The writing convention has a tenth rule: a numbered
section's title is a label naming the section's subject, 30
characters at most, in sentence case, one phrase without a gloss,
standing alone without its parent heading; the point goes in the
first sentence. Both seats' `writing.md` carry it. Facts-in-sync
§3.1 keeps its 30-character cut for one case, a numbered rule's bold
lead, and points at the writing rule for titles. The titles
themselves do not change in this set: about 230 of 375 are retitled
and about 270 references rewritten by a commit plan of their own,
by layer, after round 3's rule check and before its read, as the
reference rewrite was; a TODO item holds that work with its
trigger.

## Commits

**1. `docs(agent): add commit plan for section titles`**
This file.

**2. `docs: ADR-0075 a title names its subject`**
Proposed. The seven decisions the reviewer took on 2026-10-29, each
with the ways rejected, and the measurement behind them
(`TODO-CONVERSATION-MEMORY.md` §25, *How a section title is written*).

**3. `docs: writing rule 10, how a title is written`**
The writing manual's §2 gains rule 10 with its why. Facts-in-sync
§3.1's sentence on cutting a title over 30 characters narrows to a
numbered rule's bold lead, and points at rule 10 for a section's
title. One commit: the cut's narrowing stands on titles being 30 or
fewer, so neither reads right without the other.

**4. `chore(agent): our writing.md takes rule 10`**
Our agent rule follows the manual, in a commit of its own
(`docs/conventions/commit-messages/` §2.3, *The agent's files never share…*).

**5. `fix(delivery): shipped writing.md takes rule 10`**
The container's copy follows the manual, with the run's examples.

**6. `docs: the title item closes, ADR-0075 accepted`**
ADR-0075 flips to Accepted. The title item leaves TODO, and a new
item holds the retitle: about 230 titles and 270 references, by
layer, as a commit plan, its trigger round 3's rule check done and
its read not begun. Conversation-memory §25 goes with the decided
item; the retitle item's talk is the same section, read by hash.

**7. `docs(agent): close commit plan for section titles`**
Deletes this file; the body says what diverged.

**8. `docs: devlog for section titles`**
The entry for the set, with the session-end lines.

## Decisions taken inside this plan

- **The rule now, the titles later.** Retitling 230 sections by hand
  and rewriting 270 references is a plan of its own, as the
  reference rewrite was (`053e94f`..`8b9a646`). Round 3's rule check
  comes first, so a doubt about rule 10 is tried on a sample before
  230 titles are written to it.
- **Facts-in-sync changes in the same commit as the writing rule.**
  The cut's narrowing is one change with the cap; the two manuals
  are both descriptions, and each follower of facts-in-sync §3.1 is
  read at that commit.
- **No commit is provisional.** The decision is settled in talk
  (`TODO-CONVERSATION-MEMORY.md` §25, 2026-10-29).
