# 0038. The handbook's decisions become ours, and its coordinates live here

Date: 2026-09-27
Status: Proposed (opened under the commit plan for the handbook
filter; flips at the set's records commit)

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

4. **One ADR adopting the six, holding every coordinate, and the
   text rewritten as ours.** Chosen.

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

2. **The provenance coordinates live here and nowhere else in live
   text.** The bytes came from the handbook (`engineering-handbook`)
   at `ba7eaa4`, and every path we took is identical through their
   `8adb46f`, the last state this repo was aligned with. They landed
   here in three sets: the container at `dc3b7db` and the manuals at
   `9a1637d`, both 2026-09-18; the models at `df9d5ed`, 2026-09-17,
   the last re-copy — the anchor is the last re-copy, not the first
   vendoring, because earlier pins bring their own churn. The
   default playbook, `playbooks/default.md`, came separately from
   their `starter/playbooks/default.md` v2 at `c670fe5`. Paths at
   landing: `delivery/container/` (then `starter/kit/`, renamed by
   ADR-0029), `docs/conventions/`, `docs/models/`. A re-sync diffs
   from the landing commit at the path then current; if a path is
   renamed after this, git's rename detection is what follows it,
   and no live file keeps a command current.

   This amends ADR-0025 decision 2 and ADR-0026 decision 2 in one
   respect: where the coordinates are written. What they are, and
   that they are no obligation, stands.

3. **`HANDBOOK` is retired as a tag in this repo's text.** The
   conventions index's citation rule says shipped files cite
   `CBC ADR-nnnn`; the artifact rule's footer form says the same.
   ADR-0020 stands whole — the reading repo's own decisions are
   bare, another repo's carry its tag, and a run cites us as `CBC`.
   Nothing here decides for a second repo what tag it declares.

4. **The manuals say their why as this repo's text.** Where a manual
   cites a handbook decision it already explains, the citation goes;
   where the citation was the explanation, the reason is written in;
   where the decision is one adopted in decision 1, the citation
   becomes `ADR-0038`. Narrative of the handbook's own history as the
   reason for a rule becomes the reason without the narrative. The
   map from their numbers to what we hold is the table above and
   this record, for whoever has a handbook checkout.

5. **The models' bodies stay as taken.** ADR-0026 decision 4
   governs and nothing lived here contradicts them. Their headers
   say whose they are and point here for where they came from. The
   mentions their bodies keep are attributions of evidence, and the
   open question of whether `docs/models/` still matches reality is
   held in TODO on its own trigger.

6. **What stays as history is not filtered.** The records — ADRs,
   the devlog, TODO, CHANGELOG, the registry, PLAN's closed gates —
   and one dated note in `temp/README.md` recording an event.

## Consequences

Good: a run receives citations it can follow, and the next delivery
carries none it cannot. The manuals explain rather than defer. The
coordinates a re-sync needs are in one record that cannot drift,
where ADR-0025 said the protection lived, instead of in four live
files with a maintenance rule each. The trigger and the cost of a
re-sync are unchanged — ADR-0025 decisions 6 and 7 — and the paths
at landing are written so that the merge stays a one-time diff.

Bad, and accepted: the adopted claims are restatements. A reader
who wants the options the handbook weighed for Conventional Commits
or the detachability split needs its checkout, and this record only
names the numbers. Rewriting five manuals in our voice edits text
that was byte-identical to the fork point, which makes the re-sync
diff larger by exactly the rewrite; ADR-0025 accepted that drift the
day the files became ours.
