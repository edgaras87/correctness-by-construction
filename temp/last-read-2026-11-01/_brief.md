# Brief for every reader of the last read

You are one reader in the last read of a refinement of the repository
at /home/edge/PycharmProjects/engineering/concept-garden/correctness-by-construction
(branch `refinement-2026-10-18`, at commit `70404e1`). The repo holds
documents only: manuals, Agent Rules, Agent Skills, records, and what
ships to other repos under `delivery/`. A refinement reads all Living
Text against the repo's own rules, lists what breaks them, and only
then fixes anything.

You read for ONE Finding Kind, in the files your assignment names.
Look for nothing else. Something of another kind that you cannot
help noticing goes in a short "Met in passing" list at the end, one
line each; do not dig for it.

## Rules of the read

1. **Read-only.** Never edit, create or delete a file in the repo.
   Never run a git command that changes state. You may read files,
   grep, and run `git log`/`git show`/`git blame`.
2. **Read before you judge:**
   - your Finding Kind's row in `temp/refinement-2026-10-18.md`,
     section `## The last read`, `### The rules' check (§2.3)`, and
     the rule's home it names, read whole;
   - `.claude/approaches-on-trial/refinement.md` §2.4 *Reading the
     Finding Kinds* and §2.5 *List the findings*.
3. **A finding names the rule the text breaks.** Text that meets its
   rule stays, even if it could be said better. Taste is not a
   finding. A reader asked to look always finds something; resist it.
4. **Settled questions are not findings.** Before listing, check the
   decisions in `temp/refinement-2026-10-18.md`: every `### Decisions`
   section (DECISION-1 to DECISION-40) and the two lists that begin
   "The agent's calls". Also `docs/adr/0079-the-rules-say-what-the-refinement-decided.md`.
   A line a decision or call settled is not a finding.
5. **Already listed, not again.** The leftovers in
   `temp/refinement-2026-10-18.md`, `### Before the readers`, and the
   item list in
   /tmp/claude-1000/-home-edge-PycharmProjects-engineering-concept-garden-correctness-by-construction/810efcbc-3ec8-4fef-8241-1f29baac5035/scratchpad/leftovers.md
   (the lines marked "stands") are already findings. Do not list them
   again. If you find one that is wrong (already fixed, or worse than
   it says), note it under "Met in passing".
6. **History is not read as Living Text:** the devlog months,
   closed ADRs, commit bodies, the entries of `.claude/decisions.md`,
   the parts of `TODO-CONVERSATION-MEMORY.md`, and `CHANGELOG.md`'s
   released entries (`[v1]` and below). Read those two files by
   their header comment only. Their header comments are Living Text.
7. **Read each assigned file whole** unless your assignment says
   otherwise. Do not skim. If your context runs short before you
   finish, stop, write what you have, and name the files you did not
   read; do not guess at them.

## The form of a finding

Number your findings R-1, R-2, … (your reader label in front, e.g.
SL1-3). Each:

- **Where:** path, section title, line number at `70404e1`.
- **Quote:** the text, copied exactly from one line (it is checked by
  script; copy, never paraphrase).
- **The rule:** what it says, with its home (path and section).
- **What the text says,** and why it breaks the rule, in one or two
  sentences.
- **Stands:** checked (you verified it in the tree), resting on the
  reader (your judgement), or uncertain.
- **Why it was missed:** older than the rule; missed at a change
  (name the commit if `git log -L` or blame shows it, and the check
  that should have caught it); or the rule is unclear.
- **Proposed:** "fix:" with the replacement text, or "question:" with
  what the reviewer must decide.

Then **Found true, so not listed:** what you checked and found
holding, a few lines. Then **Met in passing.** Then **Not read**, if
any file was not read whole.

## Output

Write your full report to
/tmp/claude-1000/-home-edge-PycharmProjects-engineering-concept-garden-correctness-by-construction/810efcbc-3ec8-4fef-8241-1f29baac5035/scratchpad/findings/<your label>.md
(the scratchpad is outside the repo; writing there is allowed).
Your final reply is only: the file's path, the number of findings,
how many checked / resting on the reader / uncertain, and the files
not read, if any. Nothing else.

Write plainly: short sentences, one idea each.
