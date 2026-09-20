# 0034. An edited copy carries no header line; the record is elsewhere

Date: 2026-09-20
Status: Proposed

## Context

`convention-lifecycle` §3 step 4 lets a project edit a convention
copy between two pins, and asks for three records of that edit:

> Give each edit a dated line in the copy's header comment, saying
> what changed and which step found it, and one entry in the
> decisions log. At the step's close, add one TODO line per edited
> copy asking the deliverer to evaluate since the pin.

A fourth record exists whether or not anyone writes it: the diff of
the copy against the delivery commit, which §3 step 4 elsewhere
names as the compare and which no edit can hide.

The rule was written provisionally — "until one such edit has gone
through an update" — and on 2026-09-20 the machinery ran for the
first time. never-oversold took the delivery at `6f2be1d`, found
five lines in four delivered convention files still saying
"change-plan" after the rename, and fixed them in its copies: its
first in-place edit of a pinned copy, five words, one exact hunk per
file. It wrote the decisions entry and the TODO line. It did not
write the header lines. It wrote them, looked at them, removed them
unstaged, dropped the same clause from its own rules file in a step
of its own, and asked us to drop it from both.

Its argument: a comment in an artifact says how to use the artifact
or what a part of it is — never what changed. What changed is
history, and history here has two homes already. A third copy inside
the file is the explanation-in-the-artifact that both repos have
been stripping out since 2026-09-17.

## Options considered

1. **Keep the clause.** The three other records all require knowing
   to look; a header line does not. An agent that opens the skill
   mid-step to follow a rule consults no registry first, and
   `agent-arrangement`'s own test — a line with a moment goes where
   the moment is — reads as an argument for the line. Rejected on
   what the reader would *do*: nothing. The rule in front of them is
   the one the project deliberately decided it should say, and
   following it is the intended outcome. The reader who genuinely
   needs to know an edit exists is whoever runs the next re-pin, and
   that reader is already ordered to diff and already handed the
   TODO line.
2. **Drop it for typo and noun fixes, keep it for rule changes.**
   Rejected: the reader must classify the edit before knowing which
   rule applies. That is the same weakness this repo's standing TODO
   holds against a mood exception in `commit-messages` — a
   convention nobody can apply without first sorting the case is a
   convention that will be applied inconsistently.
3. **Drop it.** Chosen.

## Decision

1. **The clause goes.** `convention-lifecycle` §3 step 4 no longer
   asks for a dated line in the copy's header comment. The three
   records that remain are the decisions entry, the TODO line, and
   the diff against the delivery commit — and the rule says so
   positively rather than leaving a hole where the clause was, so a
   reader is not left wondering where the record went.

2. **The principle is stated once, where it applies to everything:**
   a comment in a shipped artifact carries how to use it and what a
   part is; what changed is history and lives in the records. This
   is ADR-0022's reasoning — a shipped file carries instruction only
   — reaching the one place ADR-0022 did not: the receiver's copy
   rather than the sender's master.

3. **The provisional clause is discharged, not merely edited.** "A
   project may edit its copy between two pins, provisionally until
   one such edit has gone through an update" survives as written.
   What ran here is the first *edit*, not the first edit through an
   update; that still fires at never-oversold's next re-pin, and its
   report to the handbook carries this finding with it.

4. **We answer for our copy of the convention, and the handbook
   answers for its own.** ADR-0025 made these files ours, so the
   change needs nobody's permission. But HANDBOOK ADR-0038 is
   provisional on exactly this report, and it has not made its
   decision. **The two texts may diverge, and that is allowed** —
   what would not be allowed is our changing the rule and letting a
   run believe both sources agree. never-oversold's own hand-off to
   the handbook is the other half of the report and is not ours to
   send.

## Consequences

Good: one edit now has three records instead of four, and the one
removed was the only one that had to be written by hand into the
artifact it describes. The rule loses a clause that its first live
firing found wrong, which is what a provisional clause is for — the
machinery worked exactly as designed, and the design's own test was
the first thing it failed.

Bad: **a reader of an edited copy now has no in-file signal that it
is edited.** Opening the file tells you what to do and nothing about
where it came from. The mitigation is that the reader who needs that
fact — the one running the next re-pin — is ordered to diff, and the
diff cannot be wrong. A reader who needs it for any other reason has
the registry. If a project is ever surprised by an edit it could have
seen, this decision is the reason and option 1 is what it should
become.

Also: this is the first rule of ours changed on a run's argument
rather than on our own reading, and the run's argument was against
the rule it was running under, written the same day it first ran it.
Worth naming, because the arrangement is built to produce exactly
that and this is the first time it has.
