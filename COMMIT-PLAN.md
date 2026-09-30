# Commit plan: agent-arrangement and the model, read whole

## Summary — the state after all commits

agent-arrangement and `docs/models/agent.md` say nothing false, and
each fact they share has one home. The 98-line measurement, which
the manual credited to the model's M1 although M1 never held it,
lives in M1's evidence, credited to the handbook, and the manual
points at it once. The manual's §2 and §3 are true for both seats.
Its skills are derived at the deliverer, not copied. Its entry file
is revisited at the re-reading its own Size paragraph names. And
its Where paragraph says each thing once. The model says what names
a channel, and G1 carries this repo's evidence.

This branch already holds two commits, `812271c` and `935c88d`. They
were made as a single small change before the whole manual was
read. This plan covers what that reading found.

## Commits

**1. `docs(agent): add commit plan for the arrangement`**
This plan.

**2. `docs: the 98-line measurement moves to M1`**
agent-arrangement states it twice, on lines 16 and 160, citing the
model's M1. M1's evidence is a different case, the lost "no
period". Git shows the origin: on 2026-09-27 (`426b39c`),
"HANDBOOK ADR-0014 records the measured case" became "model claim
M1, measured once: 98 lines". The measurement goes into M1's
evidence, credited to the handbook's entry file. The manual keeps
its reason and points at M1. It is one commit across both files,
because one fact changes home.

**3. `docs(conventions): agent-arrangement's §2 and §3`**
- §3's `skills/` says "the copy verbatim". That is a run's case; the
  deliverer's skills are derived from their manuals (CBC ADR-0042).
- §2's When says "not otherwise", against the Size paragraph's
  re-reading, which can remove lines.
- §2's Where says "every agent-side path sits in one directory"
  twice, and has the fragment "Whatever the tool looks for
  otherwise."
- Beside these: a double blank line in §1, a broken wrap in *why it
  arrives this way*, and "the decisions log's promotion queue",
  which only a run's log has.

**4. `docs(models): §9's channel and G1's evidence`**
§9's "nothing names a channel" means no field in a skill names one.
It says so beside §8's pointer to each manual's *why it arrives this
way*. G1 gains this repo's evidence: A1's count, with no gate on
subject length.

**5. `docs: devlog carries the arrangement`**
The session's entry for this branch. It covers the fold weighed and
kept apart with its own trigger, the two small commits, and this
reading. It also records that the first answer of the reading, "that
is it", was given before the manual had been read whole.

**6. `docs(agent): close commit plan for the arrangement`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **The measurement's home is the model.** It is evidence for a
  claim, and the model is where claims keep their evidence. The
  manual keeps the reason it needs, and the number stays in one
  place.
- **No ADR.** These are corrections under ADR-0042 and ADR-0043.
- **The same branch.** The two commits before this plan and this
  set are one tidy-up of one manual and its model, and land
  together.
