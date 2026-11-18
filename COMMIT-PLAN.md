# Commit plan: Adapted Cases used where they are kept sit in layer 4

## Summary — the state after all commits

An Adapted Case that is used only where it is kept, and copied nowhere, is written straight into layer 4. Layer 3 holds only Adapted Cases kept apart from their work, for copies. The general document says so as a rule, and its arrows and picture show it.

In the Maintainer document, the Maintainer Repo's own Adapted Cases sit in layer 4, as "its own work, by its own Adapted Cases". The picture's right column runs from layer 2 straight to layer 4. The box for its own layer 3 and the double line *used in place* are gone. Layer 3 holds the System Kit alone and is no longer split by Work Domain. Only layer 2 is split. Knowledge on Trial, in either repo, is written in layer 4 where its work is done.

What it gives: each layer-3 box means one thing, what is delivered, and the picture draws no layer-3 Maintainer Kit ahead of a second Maintainer Repo.

## Commits

**1. `docs: temp's general layers let work hold its case`**
`temp/common-ground/knowledge-layers-general.md`:
- **§2.4:** a rule: an Adapted Case used only where it is kept, and copied nowhere, is written in layer 4.
- **§3.2:** the arrows *adapt*, *lesson*, *set apart* and *change* join layer 2 and layer 4 for such a case. *change* writes a case on trial in layer 4.
- **The picture:** shows the arrows between layer 2 and layer 4.

It comes first because the Maintainer document adapts this one and never departs from it. The wording is drafted at this commit's boundary.

**2. `docs: temp's Maintainer cases sit in layer 4`**
`temp/common-ground/knowledge-layers.md`, the Maintainer Repo's own Adapted Cases:
- **The picture and its key:** the right column's layer-3 box goes, its arrows run from layer 2 to layer 4, and the double line *used in place* goes, with its key sentence.
- **§2.3:** the paragraph on the split by Work Domain goes. §2.3.1 goes, and §2.3.2's text becomes §2.3's own, with no subsections.
- **§2.4:** the bullet on the Maintainer Repo's own work holds what §2.3.1 held, with the Maintainer Kit sentence.
- **§3.1:** the arrow *used in place* goes. The arrows *adapt*, *lesson* and *set apart* name the right column's run from layer 2 to layer 4.
- **§3.3:** a lesson changes the Adapted Case in layer 4, not layer 3.
- **§4:** question 1 points at §2.4. Question 13 says the Maintainer Repo's own change is made in its Adapted Case at once.

The picture and the text are one commit, since the header checks them against each other at every change. A rename grep for §2.3.1 and §2.3.2 runs in this commit.

**3. `docs: temp's Knowledge on Trial sits in layer 4`**
`temp/common-ground/knowledge-layers.md`: §2.3's paragraph on Knowledge on Trial moves to §2.4. A System Repo's own is kept in the System Repo and copied nowhere, so it is layer 4 by commit 1's rule, as the Maintainer Repo's own is. §4 question 14's pointer follows.

It is a commit of its own because it reaches the System Repos' side, not only the Maintainer's.

## Decisions taken inside this plan

- **The rule goes into the general document,** not only into the Maintainer document. The Maintainer document adapts the general one and never departs from it, and the general arrows name layer 3 only.
- **Knowledge on Trial in a System Repo is layer 4 too.** This follows from the rule: it is kept where its work is done and copied nowhere. It was not discussed. Commit 3 drops out if you say otherwise.
- **Three work commits, not the four first proposed.** The picture, §2.3, §2.4 and the pointers are one change in one file. Split, each part reverted alone would leave the picture and text disagreeing, which the header forbids.
- **The 2026-11-16 decision that layer 3 splits by Work Domain is reversed** by commit 2. Layer 2 still splits.
- **No records commit.** The TODO item on the concept's split (line 197) puts the System Kit's cases in layer 3, which stays true. No new Glossary Name. The devlog entry comes at the session's end, outside this plan.
