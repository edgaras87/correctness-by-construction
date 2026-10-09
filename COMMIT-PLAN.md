# Commit plan: the commit rules, settled

## Summary — the state after all commits

The five questions TODO held about how commits are written and
planned are settled, under one ADR:

- **A commit plan counts commits.** "Step" is `PLAN.md`'s word
  alone; inside a commit plan, the unit is a commit — commit 3 of 5,
  the records commit, a provisional commit. One word, one meaning.
- **A PLAN step done in many commits needs no name of its own**:
  it is a step with a commit plan. Run 3's question was the double
  meaning, and the first answer removes it.
- **The sweep before a close reads the unwrapped text**, so a
  phrase the file breaks across two lines is found.
- **The 50-character limit stays.** Counted when the plan is
  written, no subject has run over since; the limit was unchecked,
  not mis-set.
- **A subject may take either mood.** It says what the commit
  changes and makes sense alone in `git log --oneline`; a code change
  reads as a command, a record as what became true, and nobody
  sorts a commit first.

Each change lands in its manual and the container's master
together, and our two copies follow.

## Commits

**1. `docs(agent): add commit plan for commit rules`**
This plan.

**2. `docs(adr): 0049, the unit, the mood, the limit`**
Proposed. The five questions, the options each weighed, and the
answers above. Decision-first: settled in conversation.

**3. `docs: a commit plan counts commits`**
The commit-plan manual and the container's `commit-plan` skill:
"step", where it means one commit of a plan, becomes "commit" —
the per-commit note, the records commit, a provisional commit,
the lifecycle table. "Step" stays wherever it means a `PLAN.md`
step. The reviewer's `CLAUDE.local.md` takes the word at the same
boundary.

**4. `docs: the sweep reads the unwrapped text`**
The skill's §4 sweep gains the line — join the text before
grepping it — and the manual its reason, the four misses that
taught it.

**5. `docs: a subject may take either mood`**
The commit-messages manual gains the reason, and the container's
`commit-messages` skill drops "imperative" from the subject's
line, keeping what the subject must do.

**6. `chore(agent): our commit skills follow suit`**
Our `commit-plan` and `commit-messages`, byte-identical to the
container's. No decisions entry: each change brings a skill to its
manual.

**7. `docs: records carry the commit rules`**
ADR-0049 Accepted, its decision 5 gaining "present tense", as
commit 5 landed it on the reviewer's word. TODO: the five items
close; the provisional watch item made true in the new word. The
devlog.

**8. `docs(agent): close commit plan for commit rules`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **One ADR for the five.** They are one subject — how a commit is
  written and planned — and three of them weighed options.
- **"Step" changes only in the commit-plan convention**, and in the
  reviewer's local file, at the reviewer's request: its "stop at
  every step's boundary" reads "commit's" from commit 3, shown in
  the console — the file is ignored by git, so no commit carries
  it.
- **Run 3 hears it at the next delivery.** Its line under *To the
  deliverer* — framing steps as commit series, and the imperative
  test — is answered in that note; no delivery for this alone.
- **No CHANGELOG line.** Nothing here is the concept or an
  execution.
