# 0059. A retelling may stand, tagged to its source

Date: 2026-10-20
Status: Proposed (under the commit plan for tagged retelling,
inside the refinement's round 1).

## Context

One home per fact allows a pointer only: "Elsewhere, link; don't
retell" (`.claude/rules/one-home.md`, rule 2). Its manual,
project-recording §11, allows a second copy only "when two copies
cannot be avoided", one the owner, the other its follower, with a
check that compares them.

A pointer alone can leave the reader without the picture at the
moment of use. On 2026-10-20, writing `approach-drafting`, a line
that retold the step form was cut to a pointer: "what its Notes and
gate take from the approach is `PLAN.md`'s step form's". The
reviewer asked whether a retelling could stand if it named its
source, and a change to the source re-read it.

Part of this already exists. A pointer is a path with a section
(`docs/conventions/conventions/` §3.2), so one grep finds it. A
change to a description greps for its path (§3.5, step 3), and the
foundation check makes this repo do that before every commit since
2026-10-17. What is missing is the permission, and the re-read.

The cost was measured. A change to one section re-reads few places:
eight pointers name the exchange's §3.2, the most for any one
section. But 19 pointers name the exchange manual with no section,
and would make every change re-read them all.

Round 1 found retellings that drifted, tag and all: FINDING-40 and
FINDING-41, both in `ARCHITECTURE.md` §5. Both were written on
2026-09-30, before the foundation check existed.

The reviewer judged three cases from round 1, each written both
ways, and found the retellings read better. Round 1's DECISION-3,
and its findings on retellings, rest on the rule.

## Options considered

- **Keep rule 2 as it is.** Rejected: the sample showed the gain,
  and a glossary entry cannot be a bare pointer at all.
- **Allow a retelling anywhere, if tagged.** Rejected: every walk
  would judge more text, for lines no reader acts on in place.
- **Give staying in step its own convention now.** Rejected for
  now: moving text between manuals is round 2's kind of fix, made
  on text round 1 has made true. Round 2's Layout finding names it.
- **Move the whole subject into project-recording, or into the
  conventions manual.** Rejected: each would hold a subject wider
  than its own.
- **Widen a run's rule now.** Rejected: a run's case, which ids
  are tags and when they are re-read, is designed once, with round
  2's convention, so a shipped rule changes once. No run is born
  before then.

## Decision

1. **A fact may be retold beside its pointer where the reader acts
   on it in place.** Elsewhere: point, don't retell. A summary that
   nobody acts on stays as rule 3 has it.
2. **A retelling carries a tag:** a label grep finds, defined at the
   fact's home. Without the tag it is a second home, and a defect.
3. **When the fact changes at its home, every tagged retelling is
   found and re-read,** with the paragraph around it. A retelling
   whose host is itself a source walks on.
4. **Each case applies the rule with its own tag and its own
   moment.** Ours, now: a manual's path and section
   (`docs/conventions/conventions/` §3.2), re-read by the walk at
   every commit (§3.5). A run's: its invariants, kills and slices,
   tagged by id, designed with round 2's convention.
5. **The rule is written where its pieces live today:**
   project-recording §11 leads, conventions §3.1, §3.2 and §3.5 and
   the manual form follow. Where the subject should live is round
   2's Layout finding.

## Consequences

- `.claude/rules/one-home.md` allows a tagged retelling; the
  container's does not change yet.
- Conventions §3.1's "stated twice" and the manual form's "never a
  restatement" carry the exception.
- DECISION-3 narrows: a retelling's pointer carries its path and
  section; whether every plain pointer must is still its question.
- Round 2's One home and Dependencies kinds no longer list a tagged
  retelling the reader acts on in place.
