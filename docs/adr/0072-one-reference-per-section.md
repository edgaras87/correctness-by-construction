# 0072. One reference per section of a derived file

Date: 2026-10-28
Status: Accepted (2026-10-28, at the set's records commit; opened
Proposed under the commit plan for the reference rewrite, unchanged
since).

## Context

ADR-0070's decision 7 had a derived file's lines carry fact
references to the parts of its foundation they use, each line its
own. Its consequences named a trigger: "a file where references sit
on most lines and add nothing. One reference per section of the
derived file is then weighed."

The reference rewrite met it, in commit 7. Our `writing.md` holds
eight rules, and every one comes from one part of its manual,
`docs/conventions/writing/` §2, *Why each rule*. A reference on each
line would repeat one address eight times in a 79-line file. Our
`exchange-reading.md` and the two exchange skills read the same
way: a section of the file follows one part of the manual.

## Options considered

1. **One reference per line,** as decision 7 had it. Rejected: the
   same address on most lines tells the reader nothing new, and
   that was the trigger.
2. **None to the file's own foundation,** the `foundation` line
   covering it. Rejected on 2026-10-27, in ADR-0070: in a large
   foundation a line's fact is not found without its section.

## Decision

A derived file carries a fact reference to its foundation's part
once per section, where the section's lines all use that one part.
Where the lines of a section use different parts, each line carries
its own. A line that relies on any other text carries its reference,
as before. This changes ADR-0070's decision 7.

## Consequences

- Facts-in-sync §4 step 2 says so.
- `writing.md`, `exchange-reading.md`, `exchange-deliver` and
  `exchange-read` carry one reference per section (`ed96ed0`).
- The walk still finds the file by its `foundation` line, and a
  reader still lands on the part the section follows.
