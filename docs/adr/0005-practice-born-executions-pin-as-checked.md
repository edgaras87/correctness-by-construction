# 0005. Practice-born executions pin as checked-against

Date: 2026-08-28
Status: Accepted

## Context

ADR-0003 has executions cite the concept version they derive from,
and ARCHITECTURE holds the invariant that no execution lands without
stating its concept version. The practice executions
(infra-establish, infra-serve, cbc-bootstrap, and their agent
definitions) break the assumption behind that wording: they were not
derived from the chapters. They grew from lived runs — distilled
from real establishment and bootstrap work — and were then aligned
with the concept's pipeline. Their headers have to say something,
and "derives from concept v1" would be a false claim about lineage.

## Options considered

1. Claim "derives from concept v1" anyway — uniform headers, false
   provenance. The whole point of the header is that it can be
   believed.
2. Leave them unpinned — honest about lineage, but it breaks the
   pinning invariant and, worse, exempts them from the versioning
   machinery: a concept bump would name no reason to re-review them.
3. Pin as **checked against** concept v1 — chosen.

## Decision

A practice-born execution's pin line reads "checked against concept
v1" instead of "derives from concept v1". The versioning function is
identical — the pin names the concept state the execution is known
to be consistent with, and a version bump that could invalidate it
triggers re-review exactly as ADR-0003 provides. Only the lineage
claim differs: derived-from means the chapters produced it;
checked-against means practice produced it and the concept was the
test it passed.

The two phrasings are the complete vocabulary: every execution
carries exactly one of them. Which one a future execution gets is a
fact about its history, not a choice.

## Consequences

Good: headers stay believable; the pinning invariant holds
unchanged; the distinction itself is information — it marks which
executions are upstream candidates for harvest (practice-born ones
carry lived knowledge the chapters may not state yet).
Bad: two phrasings where ADR-0003 assumed one — accepted; a reader
meeting "checked against" learns something true instead of
something tidy.
