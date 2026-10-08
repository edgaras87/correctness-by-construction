# Commit plan: run 3's edits, into the masters

## Summary — the state after all commits

What run 3 learned at SL-3 and the review after it is in the masters,
and the reading of 2026-10-08 has every decision ended (its W2 and W4).
D2 is already in, at `6389120`.

- **The slice skill hunts against the trust list** and carries the
  rest of run 3's five edits: a cost says its size, a red counts only
  on the witness, a race's pause stays on the red tree, a wall's own
  check is a third kind of test. The worked example's slice half says
  the same (D1, D10).
- **The PostgreSQL hand-off asks** which identity people inspect with
  (D3).
- **A take clears only its staging**: the exchange manual says so,
  the shipped `delivered-copies.md` with it, and our `exchange-deliver`
  no longer stops on a run's own drafts in `temp/` (D5).
- **Commit-plan counts its subjects when the plan is written, and
  plans agent files as their own step**: the manual's reasons and the
  container's master first, then ours (D6).
- **The walls chapter says what run 3 found**, under a new ADR, with
  the version question answered in it (D4).
- **What is held has its line in TODO**: the evidence-test shape, a
  rule on trial, a glossary (D7–D9).

## Commits

**1. `docs(agent): add commit plan for run 3's edits`**
This plan.

**2. `docs(temp): the reading settles its decisions`**
D1–D10 marked in place as this plan settles them, D2 with
`6389120`. Decision-first: settled in conversation, the plan's
approval being the word.

**3. `fix(delivery): the slice skill's five lessons`**
Run 3's `cbc-slice` edits taken whole, SKILL.md and the workflow,
and the worked example's slice half in the same commit, both copies
one text: the escape-hatch hunt read against the trust line, the
build gate's red on the witness (D1, D10).

**4. `fix(delivery): the inspection identity is asked`**
The PostgreSQL walkthrough's hand-off, run 3's edit taken whole
(D3).

**5. `docs: a take clears only its staging`**
`docs/conventions/exchange/` §4 step 5 and the run's-side paragraph
of §5, where `temp/` is "emptied at the take", say the take removes
its staging and nothing else; `delivered-copies.md` rule 5 takes run
3's edit whole, derived from them (D5).

**6. `chore(agent): deliver looks for our staging only`**
Our `exchange-deliver`: its quiet-tree check leaves the run's
`temp/` out of `git status` and looks there only for a staging or
note of ours, where it said "must be empty"; its closing line and
gates drop the same claim. No decisions entry: the log's header
counts a fix that brings a skill to its manual as no decision. Run
3's `temp/` holds a draft today and shows in its `git status`, so W3
would stop on either old check.

**7. `docs: commit-plan learns two habits`**
The commit-plan manual gains the reason for each — subjects counted
where they are first written; agent files apart from records — and
the container's master takes run 3's two edits (D6).

**8. `chore(agent): commit-plan follows the container`**
Our copy follows, byte-identical. No decisions entry, as at step 6:
the manual moved at step 7, and this brings our skill to it.

**9. `docs(adr): 0048, who may write, and the walls`** — *provisional*
Proposed. Run 3's walls lessons: the single-entry-path rung holds
only while a trust line names that path the only writer; a right
withheld in the store's grants is a wall. Its options and the
version question (ADR-0003) are written when the chapter's text is
in front of us. Material-first: the shape is decided there.

**10. `docs: the store's refusal tops the walls`**
ADR-0048 decisions 1, 2 and 4, as one change: in
`concept/02-guarantees-and-walls.md` the top rung renamed and the
paragraph after the ranking; and the three skill files that state
the ranking renamed with it — `cbc-slice`'s SKILL.md and workflow,
`cbc-framing`'s `the-whole-system-in-plain.md`. One commit: the
chapter alone would leave every derivation naming a rung that is
gone. L1 is untouched; the ADR found no sentence owed there. The
chapter's header stays as it is: a shipped file carries no history
(ADR-0022), and the change lives in ADR-0048 and CHANGELOG.

**11. `fix(concept): the chapters carry no header`**
All five chapters lose their provenance comment. Read per line, as
ADR-0022's test asks of a shipped file, every line is history —
the archive pin, the import, chapter 03's dated line of 2026-09-06,
"verbatim below this header", false of 03 since then and of 02
since step 10 — but one, "a run's copy is pinned, never edited",
which the run's `delivered-copies.md` says where it loads on
`docs/concept/**`. The history is CHANGELOG's `[v1]`, ADR-0003 and
git. No body changes.

**12. `docs: records carry run 3's edits`**
ADR-0048 Accepted. CHANGELOG's Changed, for the chapter, naming v2
(ADR-0048 decision 3), and its line on the chapters' headers made
true for step 11. TODO: lines for D7–D9, and for the skills'
`foundation: concept v1`, which becomes v2 at the release; "Decide
our own side of shapes", "Ship `temp/`…" and "Split a shipped
file's header…" made true for what run 3 and step 11 showed. The
reading marks D1–D10 and W2, W4 done. The devlog.

**13. `docs(agent): close commit plan for run 3's edits`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

The reading's verdicts, settled by this plan's approval:

- **D1, D3, D5, D6 — taken whole.** Each asks a question any project
  meets and carries no answer of run 3's.
- **D10 — taken with D1, in its commit.** The example would
  otherwise show the hunt and the red the skill now forbids.
- **D4 — taken, under an ADR.** The walls half is the concept's to
  say; the framing half (who else writes, size) is already the L1
  line on accepted trust, and the runtime ground lives in the skill.
- **D7 — held.** One run's tests, and the slice-record shape is held
  on the same ground. Trigger: the next birth's first slice, its
  evidence tests read against the skeleton — the measurement a
  hidden shape exists for. D1 already takes two of its lessons.
- **D8 — held**, with D7: a rule on trial is a question only once
  there is a rule we would deliver that way.
- **D9 — held.** Trigger: Release's README gate, where a stranger
  first needs the words.

And of the plan itself:

- **Each master is checked against what it derives from.** The
  container's files derive from the manuals (ADR-0042), the method
  from the chapters. Two manuals move with their masters, in the
  same commit and unscoped, as `89b4815` was; the chapters move
  only for D4 — D1's details refine 04's "the demonstration that
  the wall exists" and contradict nothing, and D2 and D3 sit inside
  L1's accepted trust.
- **The two Later items commit-plan fires** — grep the unwrapped
  text, one meaning for "step" — are not worked here. They become
  due, beside TODO's three due commit decisions (series, mood, the
  50-character limit), as the next set. This one stays run 3's.
- **No CHANGELOG line for the skills.** [Unreleased] already says
  the method was added; these edits reshape nothing that entry says.
- **The reading is marked twice**, settled at step 2 and done at
  step 12, not at every boundary.
- **The note to run 3 is not in this set.** `exchange-deliver`
  follows the close, as W3.
