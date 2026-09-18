# 0028. The procedure gets a picture; the method becomes a playbook

Date: 2026-09-18
Status: Accepted

## Context

`starter/installs/bundle-update.md` is structured — seven numbered
steps, a role marker on each, six bash blocks — and the structure
is invisible. Each step's skeleton sits under 20–50 lines of its
own reasoning, so a reader asking "why the diff in step 7" had to
be told; the answer was mid-paragraph.

The obvious remedy was this repo's own manual-and-rule split, where
`docs/conventions/<name>/README.md` explains what
`starter/kit/.claude/skills/<name>/SKILL.md` states. It was
considered and does not fit, for two reasons. That split exists
because one half *ships* to a run that will never see the other, so
the rule must stand alone; `starter/installs/` ships nowhere
(ADR-0010), and both halves would be read by the same agent in the
same repo. And the reasoning here is load-bearing *at execution
time*, unlike a convention's: strip the story behind "grep every
old identifier, not only the one you are describing" and the next
agent greps for one number again. Split out, the strict half
becomes a checklist that produces the wrong answer confidently.

So what was wanted was an entry point, not a replacement — and the
question of what form it takes is the second format question this
repo has faced in two days. ADR-0027 decision 5 named exactly that
as a trigger.

## Options considered

The comparison ran on ADR-0027's method: six requirements written
down first, four candidates rendered against them, a pass or fail
per line. One was struck in the course of it (decision 3 below),
leaving five, and these are they — written down so a later change
to the shape has something to fail against:

1. **The seven steps in order**, findable by number, so a reader
   mid-procedure can locate where they are and drop back into the
   prose for that step.
2. **Who does each** — three actors, and they are not
   interchangeable.
3. **The repo boundary** — two repos, two `temp/` directories, and
   nobody reaching into anybody. This is the rule the procedure
   exists to keep, so a shape that hides it is worse than none.
4. **The two records written**, one per side: the run's decisions
   entry at step 5, our devlog verdict at step 7.
5. **It must cost less to edit than it costs to read.** A shape
   that goes stale is worse than none, because it will be believed.

The requirements were written as what a reader must *get* rather
than what a picture must *show*, because whether it should be a
picture at all was open — unlike ADR-0027, where that was settled
and only the dialect was in question.

1. **Step index.** Seven lines, numbered, actor in parentheses.
   Cheapest to edit of the four. Rejected: the repo boundary is
   inferable from the actor names and shown nowhere, and that the
   two records are one per side is not visible at all.

2. **Table** — step, who, does, writes. The `writes` column states
   one-record-per-side more plainly than any other candidate, and
   it remains the best answer to that requirement alone. Rejected
   on the boundary: a table implies the handoff and cannot show a
   wall nobody crosses.

3. **Mermaid flowchart with two subgraphs.** Chosen. Rendered and
   confirmed on screen: the two crossing arrows read as carried,
   which was the open question no reasoning could settle.

4. **Mermaid `sequenceDiagram`.** The dialect built for handoffs
   between actors, so it should have been the fit — the same shape
   of expectation `block-beta` disappointed last time. Rejected on
   the render: five of seven steps are an actor working alone and
   draw as self-loops, and step 7 must be drawn as an arrow from us
   into the run, because that is the only way the dialect expresses
   "our agent reads the run." A read is not a call. The picture
   asserts the opposite of the one rule the procedure exists to
   keep, which is worse than having no picture.

## Decision

1. **`bundle-update.md` opens with the flowchart, and the prose is
   untouched.** The picture is additive. Thinning the text a
   picture summarizes is the move that would undo the finding in
   the Context — the reasoning is needed where the work is done.

2. **The operator is modelled as the crossings, not as a place.**
   Two subgraphs force every node into one repo, and steps 3 and 6
   belong to neither; the operator works in both. A third box would
   read as a third repo. The operator is transport, so those two
   steps are the labels on the two arrows that cross the boundary.
   This is a modelling choice, not a layout trick, so ADR-0027
   decision 2 is not fired by it.

3. **Requirement 5 — "show what is conditional" — is struck.** No
   candidate could carry it, which is evidence about the
   requirement rather than about the four. A branch is decidable
   only with its reason attached, and a shape showing the branch
   without the reason invites the wrong call. The conditionals stay
   in the prose. Recorded so the next comparison inherits a spec
   corrected once.

4. **ADR-0027 decision 5 is answered, not parked: the method
   becomes a skill of this repo's own,
   `.claude/skills/format-comparison/SKILL.md`.** Its *kind* is
   playbook, by artifact-kinds' axes — it *executes* (a step
   sequence with gates) and is a *template* (copied into a fresh
   `temp/` draft each time), and its test, *do you copy it to use
   it*, is yes. Not a convention: "do they owe an explanation if
   they ignore it" is thin here.

   **The kind and the home are different questions**, and answering
   the first does not answer the second. `.claude/skills/` is a
   channel, not a kind — artifact-kinds itself calls a skill copy
   the exemplar of a *reference doc*, a shape that carries any
   force. What decides the home is agent-arrangement §2: a rule
   with a moment goes where the moment is, and it names a skill as
   one of those places. This has a sharp moment — a format is in
   question — so it is not entry-file content, and it is not
   `playbooks/` content either.

   **`playbooks/` was the first answer and was wrong, for a reason
   worth keeping.** That directory has no channel: nothing routes
   an agent to it, and it is read only when a project playbook is
   copied into a PLAN at Framing. A method filed where no moment
   sends anyone is a method that goes stale unread — which is the
   failure this repo names about records generally, arriving here
   as a filing decision.

   **This puts a native skill beside four pinned convention
   copies** in one directory, where before everything there was
   held at a hash. Ours carries no pin header and no manual under
   `docs/conventions/`, which is what distinguishes it; the
   registry stays what it was, a list of conventions, and gains no
   entry for this. `bundle-update.md` step 3 already anticipated
   the mixing when it refused a `cbc-*` glob because it "would also
   catch a skill of the run's own."

   **The objection is recorded rather than dropped.** The
   recommendation was to park this for a third instance, because
   two uses by one author in one week is thin evidence for a rule,
   and the method's own discipline says one instance cannot be
   generalised from. The user's call was that the trigger fired as
   written and a fired trigger is answered. Where this shows, if
   the objection was right, is the skill's warnings list: a
   playbook whose warnings never grow was distilled too early.

5. **It does not ship, and the trigger for revisiting it is
   named.** Two things stand against shipping it today. The kit
   delta stands at five rows against a ceiling of a third of
   sixteen, so a new shipped file spends headroom a run may need
   for something it actually uses. And a method about how we make
   documents is *about* the work rather than part of it, which is
   PLAN Step 9's distinction and Step 9's question to answer.

   **A third argument died when decision 4 moved the home, and it
   is recorded because it was load-bearing an hour ago.** Against a
   `playbooks/` file the objection was that no slot exists — no
   playbook travels as a kit file, the one that ships being a
   *fill* written into the newborn's `PLAN.md`. A skill has an
   obvious slot, `starter/kit/.claude/skills/`, so shipping became
   *easier* at the moment the home got better. Two reasons are not
   three, and saying so is cheaper than letting a retired argument
   keep standing in the record.

   Against the two that remain, a run will meet this question: the
   kit ships `ARCHITECTURE.md` with an ASCII placeholder (ADR-0027
   decision 3), and the method is format-neutral, so shipping it
   would not ship our Mermaid choice. The trigger is therefore the
   first run that actually faces a format question, seen in its own
   records through the harvest loop — the same bar ADR-0007 set
   when it kept the harvest discipline local and gave promotion its
   own trigger.

6. **The Mermaid trial now spans two files.** ADR-0027 decision 3
   contained it to one. Both files never ship, so no run inherits a
   renderer dependency and that containment is unchanged; what
   changes is that decision 2's revert, if it fires, is now two
   reverts rather than one. Stated here rather than discovered at
   the revert.

## Consequences

Good: the procedure's shape is visible without reading 371 lines,
and the picture carries the one thing the prose kept implicit — that
the boundary is crossed only by a human carrying files. The spec
that judged it is written down and has already been corrected once,
so a third comparison starts further along than this one did.

Bad: a second file now depends on a renderer we do not control, and
its diff shows instructions rather than a picture. The same trade
ADR-0027 accepted, taken a second time with the same eyes open.

Also: a playbook distilled from two instances, on a trigger that
fired earlier than the recommendation wanted. Decision 4 names
where that will show if it was premature, which is the most an ADR
can do about a disagreement it records rather than settles.

And one directory now holds two kinds of thing — four convention
copies pinned to a hash, and one skill of our own that is pinned to
nothing. The distinction is real but it is carried by absence: no
pin header, no manual, no registry entry. An absence is a weak
signal, and if a second native skill arrives it will be worth
marking them positively instead.
