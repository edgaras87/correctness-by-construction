# 0038. The handbook is history: its decisions become ours, and no re-sync is kept

Date: 2026-09-27
Status: Proposed (opened under the commit plan for the handbook
filter; revised once at step 5's boundary, when the reviewer
rejected the re-sync premise the first draft kept; flips at the
set's records commit)

## Context

ADR-0025 made the container and the conventions' manuals this
repo's, and ADR-0026 did the same for the two models. Both kept the
handbook in live text on purpose: the two hashes a re-sync would
start from, written in `delivery/README.md`, the conventions index
and each model's header, with a diff command beside them and a rule
that a rename adds the old path to that command in the same commit.
That was the whole of our protection against the day the fork is
merged.

Nine days on, the reviewer measured what the fork left behind:
about two hundred mentions of the handbook across twenty-two live
files, of three kinds.

**The provenance passages.** Four copies of the same two hashes,
three landing hashes, three diff commands, and a re-verify duty that
ADR-0025 decision 3 removed and `delivery/README.md` still names.
Coordinates for a re-sync that ADR-0025 says may never happen are a
fact, and a fact wants recording once. Kept in four live files, they
are a standing obligation in everything but name — the rename rule
proves it.

**The manuals and the models.** Five manuals explain their rules by
citing `HANDBOOK ADR-nnnn` mid-sentence, forty-odd times, and narrate
the handbook's own history — its field test, its entry file, its
commit subjects — as the reason a rule is what it is. A manual is
the why (`docs/master.md` §1; the conventions index says a rule is
the instruction and its why is the manual's). A why that points past
the manual at a record the reader cannot open is not a why. The
models are a different case, decided already: ADR-0026 decision 4
takes their bodies verbatim and edits them only when something lived
here contradicts them. Their evidence *is* the handbook's history,
and naming the source of evidence is attribution.

**Seven citations in two shipped skills.** `commit-messages` and
`commit-plan` list the decisions they rest on in a footer, as
`HANDBOOK ADR-0005`, `0010`, `0019`, `0025`, `0027` and `0035`. A
run holds no handbook and never will (ADR-0025 decision 7 makes a
second consumer the trigger for any sharing relationship, and none
exists). So the footers point a blind reader at six decisions it
cannot read, and the conventions index's citation rule licenses it:
"`HANDBOOK ADR-nnnn` for a decision inherited from the handbook".
ADR-0020 adopted the tag rule the handbook wrote — a bare number is
the reading repo's own, another repo's decision carries that repo's
tag — and that rule is right; what is wrong is shipping a tag whose
repo the reader does not have.

The delivery to run 3 is next. Its note carries the shorter shapes
rule and the `foundation` field on nine files, and would carry the
seven citations once more.

**The premise under all of it, read at step 5's boundary.** The
first draft of this record kept every coordinate *for a re-sync*:
it moved the protection ADR-0025 built into one place and called
that the fix. The reviewer's reading, when the delta table's
purpose came up: the handbook was built ahead of its evidence — a
repo responsible for the manuals and the container of every other
repo, designed before a second repo existed. That is the
prediction without proof this repo refuses everywhere else. The
rule that replaces it is the one this repo already applies to
conventions and playbooks: derive nothing general from one
instance. A second repo that needs what this one holds copies
parts of it. A third does the same. Only after three is anything
handbook-like worth considering, from what the three lived. Under
that rule a re-sync has no reader, and the coordinates are a fact
of history, not a protection.

## Options considered

1. **Leave it.** The tag is honest: those decisions were the
   handbook's. Rejected. Honest about authorship and useless to the
   reader, which for a shipped file is the wrong trade; and the
   provenance passages are obligations ADR-0025 said it removed.

2. **Six ADRs, one per adopted decision.** Rejected. We did not
   weigh their options; we inherited their conclusions and have
   lived under them. Six records would read as six decisions taken
   here, and the numbers would be spent on nothing this repo
   decided.

3. **Keep the `HANDBOOK` citations in the manuals, drop them from
   shipped files only.** Rejected. The manuals are ours since
   ADR-0025 and are what a maintainer reads to learn why; a manual
   that cites a decision the maintainer cannot open has the same
   defect as a shipped skill that does, with a smaller audience.
   Where a manual already gives the reason the citation is
   redundant; where it does not, the reason is what belongs there.

4. **One ADR adopting the six, holding every coordinate for a
   re-sync, and the text rewritten as ours.** The first draft.
   Rejected at step 5's boundary: it kept the re-sync as a future
   to protect, in one file instead of four, and the future is not
   planned.

5. **One ADR adopting the six, recording where the bytes came from
   as history, and ending the re-sync.** Chosen.

## Decision

1. **The six decisions the shipped skills rest on are this repo's,
   by adoption.** Each is stated here with the claim it made, so a
   footer citing this ADR is citing something a maintainer here can
   read, and a run's skill cites one decision of ours.

   | Theirs | Adopted as | The claim |
   |---|---|---|
   | 0005 | 1a | Conventional Commits on top of 50/72: the type prefix makes history machine-readable and maps to SemVer, at seconds per commit. |
   | 0010 | 1b | A change set is its own convention, its plan committed then deleted: an in-flight set is visible from a clean clone, git history is the status, steps split by change with revert as the test, and a single commit gets no plan. |
   | 0019 | 1c | Records split by detachability: the agent side is a closed path list, and the discipline binds at the commit — a commit touching those paths is scoped `agent` and touches nothing else, so the arrangement can be filtered out of the history and the project stays whole. |
   | 0025 | 1d | Projection follows truth: a README never claims what is not yet true, and a step whose gate makes something projectable true includes updating its projection — a gate item where relevant, never a standing checklist line. |
   | 0027 | 1e | Change sets distill upward: an in-set ADR opens Proposed and flips at the final records commit; the commit list rolls, near steps firm and the tail provisional; step order follows where the decision lives — decision-first when settled in conversation, material-first when only seeable in the material. |
   | 0035 | 1f | The stop at every boundary — stage, show the diff, commit on the reviewer's word — is one sentence in commit-messages, at the commit moment, gated by no tool. The one project that could have used a permission gate declined it and held forty-four commits on the sentence alone. |

   Shipped files cite these as `CBC ADR-0038`. Whether a later
   decision here revises one of them is that decision's, taken
   against the claim as stated above and not against the handbook's
   text.

2. **The handbook is history, and where the bytes came from is a
   fact recorded here once.** The container, the conventions'
   manuals, the two models and the default playbook came from the
   handbook (`engineering-handbook`): the first four at `ba7eaa4`,
   identical through their `8adb46f`, landing here at `dc3b7db`,
   `9a1637d` and `df9d5ed`; the playbook from their
   `starter/playbooks/default.md` v2 at `c670fe5`. That is the whole
   of it. No re-sync is planned, protected or prepared for: no live
   file repeats a hash, keeps a diff command current, lists what
   differs from what was taken, or names the handbook as a tier
   above this repo.

   This supersedes ADR-0025 decisions 2, 4 and 7 and ADR-0026
   decisions 2 and 5. In their place, the reviewer's rule: a second
   repo that needs what this one holds copies parts of it, and so
   does a third; anything handbook-like is considered only after
   three repos have lived, from what they lived. ADR-0025's
   decisions 1, 3, 5, 6 and 8 and ADR-0026's 1, 3 and 4 stand.

3. **`HANDBOOK` is retired as a tag in this repo's text.** The
   conventions index's citation rule says shipped files cite
   `CBC ADR-nnnn`; the artifact rule's footer form says the same.
   ADR-0020 stands whole — the reading repo's own decisions are
   bare, another repo's carry its tag, and a run cites us as `CBC`.
   Nothing here decides what tag a second repo declares.

4. **The manuals say their why as this repo's text.** Where a manual
   cites a handbook decision it already explains, the citation goes;
   where the citation was the explanation, the reason is written in;
   where the decision is one adopted in decision 1, the citation
   becomes `ADR-0038`. Narrative of the handbook's own history as the
   reason for a rule becomes the reason without the narrative. The
   map from their numbers to what we hold is the table above and
   this record, for whoever has a handbook checkout.

5. **The tiers model says what is true; the agent model keeps its
   evidence.** ADR-0026 decision 4 lets a model's body change when
   something lived here contradicts it, and decision 2 above is
   that contradiction for the tiers model's first tier: no repo
   owns method above this one. Its shape shows the top row empty,
   with the rule of three as what fills it, and its upward channels
   name the tier above, which today is nobody. The agent model's
   evidence is the handbook's own history and says so; that is
   attribution, nothing contradicts it, and it stays. Its subject
   sentence names the conventions a project was born with. Both
   headers say whose the file is and point here for where it came
   from. Whether `docs/models/` matches reality beyond this is the
   open TODO item, on its own trigger.

6. **What stays as history is not filtered.** The records — ADRs,
   the devlog, TODO, CHANGELOG, the registry, PLAN's closed gates —
   and one dated note in `temp/README.md` recording an event. Three
   TODO items waited on the handbook being opened again; two are
   dropped, since it is not, and the third keeps its own trigger
   without the handbook's name.

## Consequences

Good: a run receives citations it can follow, and the next delivery
carries none it cannot. The manuals explain rather than defer. Four
live files stop carrying coordinates with a maintenance rule each,
and the rename rule that made those coordinates an obligation goes
with them. The tiers model stops describing a tier that governs
nothing. And the question of what this repo's container becomes,
which ADR-0025 left open between "close to the handbook's, so a
re-sync stays cheap" and "what CbC runs need", is answered: the
second, because the first had no reader.

Bad, and accepted: the adopted claims are restatements. A reader
who wants the options the handbook weighed for Conventional Commits
or the detachability split needs its checkout, and this record only
names the numbers. If a fourth repo ever wants a general form, it
starts from what this repo holds then, and from what the second and
third copied and changed, not from a fork point; the merge ADR-0025
kept cheap is given up because nothing plans to make it. And the
handbook's own improvements, which ADR-0025 decision 6 already
said would stop arriving, now also stop being looked for.
