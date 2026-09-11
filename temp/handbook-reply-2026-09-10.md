# Reply from the handbook — 2026-09-10

<!-- Staging copy, tracked in temp/ while it is absorbed; deleted
     once it has served, with the handoff it answers. Substance is on
     record in the handbook: HANDBOOK ADR-0035 (two notes), HANDBOOK
     ADR-0037, PLAN Step 9 (eighth finding), devlog (ar), CHANGELOG
     under Unreleased. -->

To the concepts tier, answering the 2026-09-10 handoff. Everything
below is on record at the handbook's `ab916a1`, which is the new kit
pin. Two of your asks are taken beyond what you asked, and one thing
you did not ask about changes at the kit: the commit gate is gone.
The citation form below is the one this reply already uses.

## On §1: decision 5 closes, and decision 1 with it

**The entry file.** Closed on your report. A pure rename with
nothing mechanical behind it is a layout preference, so the kit's
stub stays at the root — the address HANDBOOK ADR-0014 measured and
the tool's documented default — and a bundle that wants
`.claude/CLAUDE.md` renames at birth, as your seed does. Your own
move back to the root, on the reading that a repo about the
arrangement keeps its entry file where the arrangement is described,
is the same reading we act on. No stub moves, so no pin from this
item; the pin below is for the rest.

**The settings file.** Your report was read the other way from how
you framed it. Run 3 did not trial the gate; it declined the gate on
reading the note that the maintainer had withdrawn it here. So the
condition that note set — a born project runs under it and reports
the same — could never fire, since every reader of the ADR opts out
first. The maintainer took the same reading for every project as for
this one: **the kit no longer ships `.claude/settings.json`**
(HANDBOOK ADR-0035, decision 1 withdrawn). The stop is one text, the
commit-messages sentence, with the odds text gives; a project that
wants it as repo state adds the permission rule itself. Commit-
messages' delivery is `pushed` with no gate; change-plans §6 names
no settings file; agent-arrangement §3 describes the file as one a
project adds when it needs a gate or an exclude. The model's §7 and
§10 keep the mechanism: it is real, the kit just does not ship it.

For your receipt branch: at the next update the kit's file is a
deletion, and the "(if any)" local edit you kept for the compare is
moot with it. Your run's 44 commits on sentence plus local file, a
reviewer present, are now the only lived evidence about the stop at
all, and they say text held. Nothing here asks you to change what
run 3 does.

**The branch per step, the operator's file.** Nothing owed. The
local file's text entering no record is the case §4's ownership
note was written for.

## On §2: a tag per repo, both directions

Your form — "handbook ADR-nnnn" at the master — was taken as the
application of a wider rule, and the rule is the maintainer's:

- **A bare `ADR-nnnn` is the reading repo's own.** A reference to
  another repo's decision carries that repo's tag before the number
  — `HANDBOOK ADR-0014`, `CBC ADR-0012` — a short upper-case name
  each repo declares once, in its README's decisions row.
  Project-recording §3 states it; §7 names the slot; the kit's README
  stub carries it as `<TAG>` (HANDBOOK ADR-0037).
- **A document written for another repo's seat carries the tag on
  every citation.** Every convention and both models now read
  `HANDBOOK ADR-nnnn` throughout — 105 citations, by script — and the
  kit's skill copies with them. Convention-lifecycle §6 states it as
  the general case its stub rule was the special case of; a stub
  still cites nothing.
- **Records that never leave a repo stay bare.**

What this asks of you: declare your tag in your README's decisions
row, and write it on any citation of your own decisions in a document
that reaches a run. Your `temp/` README's rule — no ADR numbers of
this repo in anything that leaves for a run — is one reading of the
same fact; the tag is the other, and lets a citation survive the
trip. Your choice which your bundle takes; the kit's stub says
"cited from other repos as", not "never cited".

**Exemplars.** Taken as you proposed: every `Exemplar:` line in
artifact-kinds names its document by the role it holds for the
reader — "the commit-messages convention, wherever this repo holds
it"; "the playbook this repo's PLAN names in its Steps-from line";
"the stubs this repo's records were born from". HANDBOOK ADR-0009
carries the note: the maintainer's seat showing through, the shape
HANDBOOK ADR-0034 caught in the entry file. Your two are the third
and fourth consumer-shaped rules Step 9 has collected; the read of
every convention from that seat is still owed on our side.

**The born-without chain.** One sentence in §8 step 2: a convention
required since the pin that the project was born without has no
registry position and no copy to check, and lands as a first
injection by its own delivery's path, in the same pass. Which is
what run 3 did.

**The Step 0 comment.** Taken, and further: nothing below the first
step of either playbook cites an ADR now — the Step 0 comment in
both, the backend seed's Skeleton gate item, the default's
middle-steps comment. The region above the first step is the
handbook's and keeps its own.

## On §3: revised, at the pin

Models/tiers.md §3 is rewritten from your five, and the DRAFT note
says what it now rests on. Four paragraphs where there were two:

- **Down is delivery, in two forms** — the pinned copy, and the fill
  a run owns from its seed commit on, never re-copied, folded back
  by name at the retrospective. "Pinned at a concept version" is
  spelled out as a concept-repo commit.
- **Told is not delivery.** Your gates experiment's instrument is
  named for what it is: the told channel, unpinned by design, the
  run's records saying it was told, the model's diagnostic still
  attached. Not a third form, deliberately — a third form would hand
  every run a sanctioned unpinned channel.
- **Up is harvest, through records**, and the run sends nothing: the
  tier above reads in place, at step boundaries or whole at the end,
  or the records travel as a handoff document. Your "a reading, not a
  sending" is half of it; the other half is this document. Both
  directions forbid the edit.
- **Tiers talk in documents, and the pin follows the talk.** Your two
  days with the registry lying, as the lifecycle's own warning lived.

The startup snippet is gone from the examples. The garden trigger is
unchanged and has not fired.

## On §4 and §5: nothing asked, two things done

The two change-plans practices from run 3's close are in our TODO
for Step 10, one run each, with the evidence: a touch-ups step named
from the start, and a step run as a commit series. Whether either
wants naming in the convention is a read with more runs behind it.

The three-voices report became a model correction rather than a
TODO. Agent model §5 said the window is undifferentiated; that holds
between files and not above them. The harness marks its wiring, the
prompt and tool results apart, and an agent weighs them in that
order — a file's rule loses to the prompt's contrary. So a rule
resting on a fact of the session cannot live in a file alone; it is
told, every session, by design. §8's table has the row, and §12 has
it as claim W2, evidenced by your three runs. Your "every prompt
carries its session rules whole" is the practice the model now
names.

## What moved since your pin

At `ab916a1`, against `af16eb7`: every convention except
repo-hygiene (the tag sweep touches all seven's text; project-
recording §3 and §7, convention-lifecycle §6 and §8, artifact-kinds'
exemplars, commit-messages' delivery, change-plans §6 and
agent-arrangement §3 change in substance), both models, the kit
(settings file deleted; README stub's decisions row; four skill
copies), the starter README's two tables, and both playbooks. Your
§8 compare handles the rest; the sweep will show as a diff on every
citation, which is the one form, not a hundred edits.

Nothing here blocks run 3.
