# Commit plan: direction, and placing into the tiers model

## Summary — the state after all commits

The three decisions of 2026-10-28 on which way a fact reference may
point (`TODO.md`, "Write down which way a fact reference may point,
then lift what the models borrow from below";
`TODO-CONVERSATION-MEMORY.md` §16) stand in an ADR and their homes,
and the tiers model no longer leans on a manual.

- **The ADR:** ADR-0071, the three decisions and what each rejected;
  it reverses ADR-0063's "kept" for `requires`.
- **Direction, at its home:** idea-to-output §3 says a line that
  relies on a fact points at its own level or above, and a line that
  only names or lists may name any level. Its links are four.
- **Its followers:** facts-in-sync §3.1; conventions §1.2; the
  glossary's *link*; our `convention-manual.md` item 5.
- **`requires` goes** from our `commit-plan` skill and three shipped
  skills.
- **The placing:** the tiers model's §3 states the general flows,
  learned from the exchange: a run is blind, nothing arrives by
  itself, copies below and masters above, a copy edited when it
  fails, nothing up as files, the pin. The exchange stands on the
  tiers model and keeps what is this repo's.
- **This repo's place:** which tier it is and what it holds today
  leave the tiers model for `README.md`. The agent model's `PLAN.md`
  example is marked as one.
- **The placing is written down as it runs:** an approach on trial,
  `.claude/approaches-on-trial/model-placing.md`, drafted at its start,
  corrected as the work teaches, and handed to TODO's "Decide how a
  text finds its foundation" at its close.

## Commits

**0. `docs(agent): add plan for direction and placing`**
Opens the set.

### Direction

**1. `docs: ADR-0071 which way a fact reference points`**
Proposed.

**2. `docs: idea-to-output says relying points up`**
§3.1 loses `requires`, and its links are four; §3.2 tells relying
from naming.

**3. `docs: direction's followers in the manuals`**
Facts-in-sync §3.1, conventions §1.2, the glossary's *link*.

**4. `chore(agent): our rules follow the direction`**
Our `commit-plan` skill loses `requires`; `convention-manual.md`
item 5 says fact references at its level or above.

**5. `fix(delivery): requires leaves the shipped skills`**
`retrospective`, `apply-retrospective` and `commit-plan` in the
container.

### The placing

**6. `chore(agent): draft model placing on trial`**
`.claude/approaches-on-trial/model-placing.md`, written for this work
as `approach-drafting.md` stage 1 asks: what it is for, its stages,
what is not known, the ways rejected, uses empty.

**7. `docs: the tiers model states the flows`**
§3 gains the general facts, in general words, with where they were
learned. Its four pointers down become general lines, or marked
examples. Its "today" facts and ADRs leave.

**8. `docs: the exchange stands on the tiers model`**
`foundation: the tiers model`; §1 points up for the general facts
and keeps what is this repo's. The walk reaches what stands on the
exchange.

**9. `docs: README holds this repo's place in the tiers`**
Which tier this repo is, the top tier empty, and what it holds
today, from the tiers model.

**10. `docs: the agent model marks its example`**
"Here, for example": the `PLAN.md` line.

**11. `chore(agent): model placing notes its use`**
The approach's use note, and its hand-over to TODO's foundation
item.

### Records and close

**12. `docs: ADR-0071 is accepted, TODO's item is worked`**
The direction item leaves TODO.

**13. `docs(agent): close plan for direction and placing`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts, and the
approach's corrections.** A commit that changes a description walks
what stands on it; a derived file that then disagrees gets a
lettered commit after it. When the placing shows the approach wrong,
the approach changes first, as a lettered commit of its own
(`.claude/approaches-on-trial/approach-drafting.md`, *Work*).

## Decisions for you to object to

- **Direction first, the placing after,** so the placing is written
  to a rule already in its home.
- **The approach's name, `model-placing.md`:** "placing" is the
  act `approach-evaluation.md` already names for writing a piece into
  a higher home; one verb for the step to a convention and the step
  to a model.
- **The exchange's foundation becomes the tiers model,** in
  frontmatter of its own, as conventions §1.3 gives a manual whose
  idea a model states. Three manuals already do.
- **Idea-to-output §2's "Here" column stays.** Its heading marks it
  as this repo's, and it only names.
- **No reference rewrite here.** Lines this plan writes take the
  settled form; the rest wait for the rewrite, which follows this
  plan.
