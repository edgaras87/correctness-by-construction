# Change-plan: the handbook delivery @ ba7eaa4

## Summary — the state after all commits

The four pinned skill copies and both vendored models are the
handbook's files at `ba7eaa4`, and the registry says so for all
seven conventions. The copies are the rewritten kit: rules only,
roughly two thirds of the text gone, each skill's explanation left
behind in a handbook page that never ships. Their sections are
renumbered — what we hold as §1–§8 in convention-lifecycle is §1–§3
there, step numbers inside the update unchanged.

What that buys: the update procedure we hold can run again. At our
pin it names three things that no longer exist — the directory it
diffs, the frontmatter field it reads, the master it copies from —
so this delivery is taken under the note's three corrections and is
the last one that needs them. It also brings HANDBOOK ADR-0038, "a
project may edit its copy between two pins", which is the shape run
3 is asking us to rule on for the bundle's five method skills. That
answer is the next change set, not this one.

## Commits

**1. `docs(agent): add change-plan for the handbook delivery @ ba7eaa4`**
This file, agreed before any of it lands.

**2. `docs(temp): the note from the handbook, and run 3's handoff`**
Two documents arrived untracked. temp/ is tracked here so a draft's
shaping and its arrival are visible as diffs; these two are read-only
arrivals and land as they came. The note is deleted at commit 6, once
spent; the handoff stays until the bundle answers it.

**3. `chore(agent): update pinned copies to the handbook @ ba7eaa4`**
The four skill copies from `starter/kit/.claude/skills/<name>/SKILL.md`
and both models from `models/`, plus one registry entry naming
`ba7eaa4`. Copy and registry together is step 5's rule, and the
2026-09-11 update landed the same way. Compare-first has already run
and is recorded in the plan's decisions below.

**4. `chore(agent): register the installed three @ ba7eaa4`**
agent-arrangement's one changed stub line — the decisions-log header's
cross-reference follows the renumbering, `convention-lifecycle §7` to
`§2` — carried into our own header, with its registry entry.
project-recording and repo-hygiene verified unchanged across the span
and registered at the new pin. Agent-side throughout: `.claude/` only,
so no project-side half and no split.

**5. `docs: records for the handbook delivery`**
The devlog entry for the session, and two TODO Later lines the note
opens: the handbook's invitation to say what we had to invent when we
authored our own parts (its two drafts, `repo-shapes-model-draft.md`
and `repo-shapes-gap-list.md`, are ours for the asking and bind
nothing), and its caution if we restructure — our parts are not called
conventions, and the concept stays beside the executions rather than
inside them.

**6. `docs(temp): delete the spent note`**
The note says to delete it once used, and anything worth keeping is in
the records by commit 5. Run 3's handoff is untouched.

**7. `docs(agent): close change-plan for the handbook delivery @ ba7eaa4`**
Deletes this file; the body carries what diverged.

## Decisions taken inside this plan

**The delivery goes first, before run 3's ask is answered.** Run 3's
handoff asks whether a run may edit its copy of a bundle skill between
two pins. The handbook answered that same question for its own four
conventions at kit `9e28143` — HANDBOOK ADR-0038 — and the text is
inside this delivery, at convention-lifecycle §3 step 4. Answering
CBC ADR-0007 before we hold it would be writing blind to a shape
already settled one tier up. The ask does not block run 3: its Step 6
opens on the copies as they stand.

**Compare-first is already run, and clean.** All four skill copies are
byte-identical to the kit at our pin `ab916a1`; both models are
identical to `models/` at `ab916a1` below their vendoring headers. No
copy carries a local edit, so every overwrite is silent-safe and
nothing is re-applied, dropped or promoted. Commit 3's registry entry
states this rather than leaving it to be re-derived.

**The old file compared against is reached at the pin, not at HEAD.**
`git show ab916a1:conventions/<name>/CONVENTION.md` resolves although
`CONVENTION.md` is gone everywhere at HEAD. The layout change broke
the fetch, not the comparison — narrower than it first reads.

**The models ride with the skills, not in their own commit.** They are
a different vendoring — ADR-0002, not the convention registry — but
they move as one delivery from one hash, and reverting half of it
would leave the repo citing section numbers across a renumbering.
The 2026-09-11 update is the precedent, one commit and one entry.

**The handbook is at `da93a88`, one commit past the note's `ba7eaa4`.**
That commit touches nothing under `starter/kit/` or `models/` — it is
the handbook recording what this case taught it about being a sender.
So `ba7eaa4` is the hash this delivery pins, and the checkout is left
on `main` while the work runs: the procedure diffs against whatever is
checked out.

**No ADR in this set.** Nothing here is our decision — the corrections
are the handbook's and we apply them, and vendoring is already
ADR-0002. The registry entries carry the reasoning, as they did on
09-11 and 09-09.

**This set runs on a branch, `handbook-delivery-ba7eaa4`.** First time
in this repo; `main` holds no other work, so the close is a
fast-forward. Not named `kit-<hash>`: that spelling means a receipt
branch in the procedure we are taking, a branch holding every
delivered file as it arrived and never edited, and we hold none. The
practice is on trial for this set only — if it holds, the devlog says
so and it goes to the retrospective, not to a rule.

**`temp/questions.md` stays untracked.** It is a personal scratch list,
not a draft on its way to another repo, so temp/'s rule does not
reach it.
