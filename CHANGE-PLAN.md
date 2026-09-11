# Change-plan: absorb the fifth reply (handbook @ ab916a1)

## Summary — the state after all commits

The handbook's reply of 2026-09-10 is absorbed. This repo's seven
conventions and both models are pinned at `ab916a1`: the four skill
copies and the two models re-copied (compare-first clean — each
identical to the kit at af16eb7 below its header), the three
installed conventions registered at the new hash with the one carry
they bring (README's decisions row). The tag question the reply put
to us is decided: this repo cites its decisions from other repos as
`CBC ADR-nnnn`, declared in README's decisions row; every citation
of this repo's decisions inside the bundle — the text the seed
copies verbatim into a run's `.claude/skills/` — carries the tag,
and nothing that stays here changes form. The fills' kit halves are
re-verified at the pin. TODO's fifth-handoff item closes with the
reply's answers; the material that accrued after the draft went
opens a sixth. PLAN's decision index is caught up (it stopped at
ADR-0013). The two served drafts leave `temp/`, logged in the
devlog.

## Commits

**0. `docs(temp): reply from the handbook, ab916a1`**
The reply file the user staged this morning — delivery, not work,
so it lands before the plan, as the handoff draft did (bdd5fda).
Named here so the set reads whole.

**1. `docs(agent): add change-plan for the fifth reply's absorption`**
This plan.

**2. `chore(agent): update pinned copies to the handbook @ ab916a1`**
Skill delivery, one commit (convention-lifecycle §8 step 5): the
four skill copies overwritten from the kit at ab916a1 — the compare
against af16eb7 ran clean on all four, no local edits — and the two
models re-copied below refreshed headers (both identical to af16eb7
below the header). Registry entry: what moved — every citation in
the copies and models now reads `HANDBOOK ADR-nnnn`; commit-
messages' delivery is `pushed` with no gate; change-plans §6 names
no settings file; convention-lifecycle §6 states the tag rule as the
general case and §8 step 2 gains the born-without sentence;
artifact-kinds' exemplars by role; the agent model's window carries
roles (§5, §8's row, W2); the tiers model's §3 rewritten from our
five, the told channel named, the DRAFT note re-dated. The chain
check (§8 step 2): convention-lifecycle requires agent-arrangement,
held @ af16eb7, updated in commit 7 by its installed path.

**3. `docs(adr): declare the CBC tag, and what stays bare`**
ADR-0020, Proposed. This repo's tag is `CBC`. The bundle's citations
of this repo's decisions carry it, because the seed copies the
bundle verbatim into a run's `.claude/skills/`, where a bare number
is the run's own — lived: run 3's ADR-0003 names its project, and
cbc-framing's header in that same checkout cites our ADR-0003. What
stays bare: the records, the bundle doc, the seed procedure and the
fills' headers — none leaves this repo (the seed inserts a fill's
body and drops its header). The `temp/` rule stays as it is for
told text: a session line cannot follow a citation, tagged or not.
Options rejected inside.

**4. `docs(starter): bundle citations carry the CBC tag`**
The sweep, by script, over `starter/bundle/` only: every
`ADR-nnnn` becomes `CBC ADR-nnnn`; verified by grep before and
after — the distinct numbers listed and each confirmed ours, zero
bare citations left under the bundle, no double tag. The bundle
doc's harvest section gains one sentence saying the citations are
tagged and why. No content changes; no per-file header line (see
the decisions below).

**5. `docs: README's decisions row names the tag`**
The project-recording installed carry: the kit's README stub gained
"cited from other repos as `<TAG> ADR-nnnn`" on its decisions row;
ours reads `CBC ADR-nnnn`. Project-side only.

**6. `docs(starter): the fills re-verified against the kit @ ab916a1`**
`readme-md-template.md`'s kit half follows the stub — the decisions
row gains the citation clause with `<TAG>` literal, the run's to
fill at its naming — and its header's pin line moves to ab916a1.
`claude-md-template.md`: the kit's CLAUDE.md stub is unchanged in
the span; the header records the re-verification. The playbook
fill: default.md changed only in two comments the v4 strip already
removed; Step N's three facts unchanged; nothing to re-vendor, the
header says so.

**7. `chore(agent): register agent-arrangement and project-recording @ ab916a1`**
Two registry entries. agent-arrangement: the kit ships no settings
file (HANDBOOK ADR-0035, decision 1 withdrawn) — never held here,
rejected 2026-09-09, now the kit's own state; §3 describes the file
as one a project adds; nothing installed here changes. project-
recording: the README row carried in commit 5; the other stubs
unchanged in the span. repo-hygiene verified unchanged across the
span, pin left as is (the tiers precedent of 09-09).

**8. `docs: close records for the fifth reply`**
TODO: the fifth-handoff item DONE with the reply's answers in one
paragraph; its post-delivery material (f) moves out as the sixth
handoff's accruing item; the harvest item in Now unchanged. PLAN's
decision index gains ADR-0014 to ADR-0020 — it stopped at 0013, a
catch-up. ADR-0020 flipped to Accepted. Devlog entry for the
absorption, with the resume line.

**9. `docs(temp): delete the served handoff and reply`**
Both drafts have served; history keeps them.

**10. `docs(agent): close change-plan for the fifth reply's absorption`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The tag is `CBC`** — the reply's own example for this repo, short,
  upper-case, and the name the prose already uses.
- **The sweep gets no per-file header line.** ADR-0007 makes each
  execution's header its change log, one dated line per change. A
  citation-form sweep changes no execution's content, and thirty
  header lines saying the same sentence would bury the harvest
  lines they sit beside. The sweep is logged once, in ADR-0020 and
  the bundle doc, and the commit is the diff. Objectionable: the
  rule as written does not carve this out.
- **Nothing under `starter/` outside the bundle is tagged.** The
  bundle doc, the seed procedure and the fills' headers stay in
  this repo; the reply's rule keeps such records bare.
- **The reply lands as commit 0, before the plan**, as the handoff
  draft did: it is the user's delivery into `temp/`, staged by
  them, not this set's work.
- **Order.** Decision-first for the tag (ADR before the sweep and
  the row); the pin update first of all, since every later step
  reads the new copies' text.
