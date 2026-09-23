<!-- A reading: what one pass over run 3 found, and the work it
     implies. Written 2026-09-23, before any of the work.

     This one stays here. temp/'s rule about our vocabulary binds
     what leaves for a run; nothing in this file is going to one,
     so it cites our ADRs and paths freely. What goes to run 3 is
     the note at item W9, written separately.

     It is a scaffold, not a record. The list below is revised as
     items land — settling one can reword or delete others — and
     the file is deleted when the work closes. History keeps it.
     Findings go to TODO, decisions to ADRs, the session to the
     devlog; this file is where they wait until they have a home.

     Its list is not a commit plan. These are things that must be
     done or considered; several will open a commit plan of their
     own, and those are named per item. -->

# Reading: run 3, through `9869798`

## Where we read to

**Run 3 (`never-oversold`, `~/IdeaProjects/cbc-pure-run-3`) read
through `9869798`, 2026-09-23 01:14.** Previous reading stopped at
`adc90f6`, 2026-09-20 14:48 — 45 commits.

That previous point had to be excavated today: our devlog entry of
2026-09-20 named the delivery, and the commit was found by matching
its date against the run's log. This line exists so the next reading
does not repeat that. Where it lives permanently is D7.

## What the run did

**Step 6 — SL-2 closed** (`correction-never-undercuts`). It added
no production code: SL-1's wall and ADR-0011's value-shaped door
already covered it, so the slice is evidence plus two structural
guards. 29 tests to 39. Version 0.2, two of four invariants
evidence-closed. SL-3 is next.

**A writing pass, on its own branch, 19 commits.** It began as "the
records are hard to read" and ended with two artifacts nobody had
asked for: `.claude/shapes/slice-record.md` and
`.claude/rules/shapes-lifecycle.md`. The mechanism it arrived at is
the part that travels: a shape sits where nothing loads it, or
where a `paths:` line loads it while the matching artifact is
written, and **the directory decides whether it is in front of the
writer.**

**Three in-place edits of copies pinned at `4c3ac99`**, the second
firing of the machinery ADR-0034 was written for. Two to
`cbc-slice`, one to `artifact-kinds`. Their reasons are in the
run's decisions log at 2026-09-21 and 2026-09-22.

**Four hand-offs**, one of which asks this repo for a role it does
not have.

## Findings

**F1 — our entry file names a file that no longer exists.**
`CLAUDE.md:25` says `CHANGE-PLAN.md`; the convention renamed it to
`COMMIT-PLAN.md` on 2026-09-19, and `delivery/container/.claude/CLAUDE.md:50`
has it right. Wrong for four days in the one file loaded in full on
every task. **Fourth instance of the class** run 3 has now caught us
on three times — and our own `bundle-update.md:133` uses this exact
rename as the worked example when telling a run to sweep for it.
**Fixed at `6a3eac3` (W1).** The seven other occurrences were read
and none should change: five are append-only history in the devlog
and the decisions log, one is a quotation inside a backlog item,
one is that worked example, and one is a baseline frozen whole on
2026-09-06 — where the old name is what the file said that day,
which is what a baseline is for.

**F2 — stale names and paths in live text.** Widened 2026-09-23
by what W1 turned up; it is no longer about one noun. Two known
targets. `delivery/installs/pure-seed.md:334` reads as live prose
rather than the historical narration its neighbours at lines 18 and
32 are, as does `delivery/fills/cbc-run-pure-playbook.md:26`. And
the *live* header of `docs/baselines/claude-md-template-v1.md`
points the reader at `starter/fills/claude-md-template.md` — a
directory ADR-0029 renamed and a file ADR-0024 retired, so both
halves of that pointer are wrong. The frozen half of the same file
is correct and must not be touched.

**F3 — run 3's last commit deleted five TODO items, and two have
no survivor.** The commit message describes a rewrite of `Now` and
says nothing about deletions; the `## Next (upcoming steps)` header
went, and its children went with it. Checked each:

- the branch-trial gate item — correctly deleted, it became PLAN's
  step-form default gate item
- SL-3's expired-hold mechanism and the `Location` deviation —
  survive in SL-1 §7, the lift condition weaker for it
- **Release: fail fast on a missing secret** — the decision
  survives in their devlog and in `cbc-bootstrap`; the lived
  reproduction is gone (boot at ~2.5s, 500/503 on first request,
  the lazy pool, and the two candidate fixes with what each costs
  the store-free context test)
- **Release: README names each refusal but not what it costs** —
  gone entirely. Filed 2026-09-20, deleted 2026-09-23. Their
  CHANGELOG already states such a cost plainly for SL-2 while
  README line 36 does not, so the inconsistency is live and no
  longer written down.

Theirs to decide, ours to tell. It matters to us for a second
reason: their TODO is the channel our hand-offs ride on, and a
section-header rewrite that takes its children could take one of
those just as easily. All four hand-offs are intact; the failure
mode is now demonstrated.

**F4 — the inbound direction has no procedure.** Outbound is
`delivery/installs/bundle-update.md`: seven numbered steps, shell
commands, an owner per step, four sections each dated to the firing
that taught it. Inbound is six paragraphs inside
`delivery/README.md`, a document whose job is to describe what a
run copies at birth. Same number of lived firings behind each —
three deliveries against three harvests. The verdict rules, which
are the inbound loop's output, are specified in the outbound
manual.

**F5 — the evidence we said we were watching for did not arrive.**
The held `infra-establish` hand-off watches for a second run
reaching the contract's facility gap, and reads SL-2 leaning on
that paragraph as evidence the first slice needed it. SL-2 does not
mention the facility at all. The item stays held; what changes is
that it has now been checked rather than left looking unexamined.

**F6 — `decide-first` is not returning what it costs, and we ship
it.** Raised 2026-09-23 by the reviewer, after its draft for D1
produced seven ordered questions and no purchase. Three firings are
known. Ours of 2026-09-19, which the devlog records as working —
"its count line did the work", "built and is not a wrapper". Run
3's in the writing pass, whose lesson was that the draft was
covering a pile of queued work rather than one unsettled shape.
And today's, written and discarded. The complaint is not the one
ADR-0030 already records as a review trigger — that one is about
routing nowhere but a comparison skill. It is that writing the
questions costs more than proposing a decision and correcting it
while building, which is what `commit-plan` §4 and §5 already
support with a Proposed ADR and revisions. This is a defect report
against a convention this repo wrote and ships to runs, so it is
not a local preference. Goes to TODO; not this branch's work.

## What the run taught us that we had not thought of

**A tripwire never discharges a kill.** Our skill demanded a red
for every guarantee and said nothing about a test that cannot be
reddened — so such a test was either mislabelled as evidence or
deleted. The run hit it, and the red run is what told the two
apart, not a reading.

**Force can come from placement rather than wording.** Our
conventions get all of theirs from wording, and rely on a person
remembering to read. Worth keeping whatever we decide about shapes.

**One draft per unsettled shape, never per pile of queued work.**
Their `decide-first` draft covered three queued items; two had no
shape question, so the count was sayable for both and the draft was
covering work rather than settling anything.

## Decisions

Preliminary order. D1 gates three of the others, which is why it is
first and why the commit count for this whole reading is not
sayable until it settles.

**Settled 2026-09-23, all in one set: D1, D2, D3, D4 and D5.** D1's
answer was not one of the three it offered — not accept, hold or
decline a role, but *we already do this and have never named it*.
That reframing came from the reviewer reading our own tree, and it
collapsed D2, D3 and D4 into the same set rather than leaving them
behind D1. D6, D7 and D8 remain open; D6 and the consequences of D1
are now in TODO.

- **D1 — do we become the collector?** Run 3 asks this repo to hold
  unexposed shapes from every project, stage them into a run's
  `temp/` with a note when that run reaches a gate ("I hold none" is
  a real delivery), and reconcile afterwards. Today our exchange
  fires when we initiate; this makes it fire on the receiver's
  calendar. It rides with a shipping rule — exposed shapes ship,
  unexposed ones never do — which constrains us immediately and
  could be taken on its own. **Gates D2, D3, and part of D4.**
  Standing recommendation: hold the role with a named trigger (a
  second run reaching a gate with a shape of its own), take the
  shipping rule now. A collector with one contributor is a folder,
  and writing the protocol from one project is what killed ADR-0021.
- **D2 — `cbc-slice` Stage 4 and the `artifact-kinds` shape entry:
  take or decline.** One decision, not two: the shape check is dead
  text for a project with no notion of a shape. Depends on D1.
- **D3 — does `shapes-lifecycle` become a convention?** It would be
  the container's first `.claude/rules/` artifact and the first
  shipped rule presuming a collector. Depends on D1.
- **D4 — does `agent-arrangement` §3 learn about `.claude/shapes/`?**
  A directory whose defining property is that nothing loads it.
  Separable; can be taken without D1.
- **D5 — `cbc-slice` Stage 3, the tripwire rule: take or decline.**
  Rests on nothing. Recommend taking it whole.
- **D6 — do the step form and default gate items fold into
  `cbc-run-pure-playbook`?** Ours. Their branch-per-step trial is
  still open beside it.
- **D7 — the inbound harvest manual: peer to `bundle-update.md` or
  a section of it, and where does it sit?** Recommend a peer.
  `installs/` may be the wrong parent — both files there put files
  into a run, and a harvest puts nothing anywhere.
- **D8 — the standing rule: a branch and a reading for work needing
  more than one commit plan.** On trial, in PLAN above the steps
  with its decision in `.claude/decisions.md`, which is how run 3
  introduced its own branch rule.

## The work

Preliminary order. Items marked **plan** are expected to need a
commit plan of their own; the rest are a commit or two.

- **W1 — fix `CLAUDE.md:25`. Done, `6a3eac3`.** One commit, as
  expected. It also paid for itself twice: reading the other seven
  occurrences established that none of them should change, and it
  is where the second half of W2 was found.
- **W2 — a sweep for stale names and paths in live text. Done,
  `e9baf63`.** Twenty candidates, three defects, all of them
  pointers saying "the live version continues at X" where X had
  moved or gone. The other seventeen are records — dated revision
  notes, a version log, captured evidence, frozen baseline halves,
  the handbook's own paths, and `delivery/README.md`, which carries
  both names on purpose because its `git diff -M` needs the old one
  to resolve the rename. One left on purpose: `docs/models/agent.md`
  names the convention by its old name, and that file belongs to the
  models item in TODO, not here — fixing one noun would make it look
  swept.
- **W3 — the standing rule into PLAN and the decisions log.
  Moved to the end of this branch, 2026-09-23, the reviewer's
  call.** It was second in the order and drafted mid-run; the
  draft was discarded unstaged. **This branch is the rule's first
  run, so the rule is written from what the run taught, not from
  what we expected before it started.** The same reasoning already
  governs W7 and was not applied here until the reviewer applied
  it. **plan**, and the plan opens with a proposal — the whole
  rule text, written once and approved before any of it lands,
  rather than approved a commit at a time. Two commits at least,
  since `.claude/` and PLAN never share one.
- **W4 — settle D1 provisionally, then polish it by building.
  Done, `1a96faa`..`6f51a7b`.** It settled differently from the way
  it was framed. D1 was written as "do we take a new role", and
  reading our own tree answered that we have run the mechanism since
  2026-09-06 in `docs/baselines/` — so the question was never a role
  but a missing name and rule. ADR-0035 accepted; the set took D2,
  D3 and D4 with it, which is why W6 closes here too.
  Reshaped 2026-09-23, the reviewer's call. The `decide-first`
  draft was written and discarded unstaged (F6). In its place: a
  Proposed ADR stating the decision, a commit plan that implements
  it, and the plan's revisions as the place the wording is
  corrected — `commit-plan` §4 and §5, the shape this repo has used
  before. The ADR flips to Accepted in the set's final records
  commit, never in the close. **plan.**
- **W5 — take the tripwire rule into the master. Done, `f2d9477`**,
  as step 4b of W4's set rather than a set of its own: under
  "takes first" it belonged beside the other edit to the same file.
- **W6 — whatever D1 settles. Done inside W4's set**, `4e73d8a`,
  `02d2495`, `9ce2d70`, `16868ea`. D2 and D3 were taken; D4 landed
  as the arrangement manual's `shapes/` entry. The size that was
  "unknown until D1" turned out to be most of a twenty-three-commit
  set.
- **W7 — write the inbound harvest manual** (D7), from the running
  of W4–W6 rather than from memory of the last three harvests.
  **plan**.
- **W8 — record the checked-through mark** at `9869798`. Lands
  wherever D7 puts it, so it follows W7.
- **W3 (out of order, deliberately) — the standing rule**, written
  last from the list below. See its item above for why.
- **W9 — one delivery to run 3**: verdicts on all four hand-offs,
  the three edits answered, and F3 told as a finding with the five
  lines quoted so they can restore what they want. Last, and one
  delivery rather than two — nothing over there is waiting on us.
  **plan**.
- **W10 — records catch up**: the ADRs each decision earns, the
  devlog, TODO.

## What the first run of the rule has taught

Kept as it happens, because W3 writes the rule from this list and
nothing else. Each line is something the rule did not say and
should.

- **Items keep their numbers when they close.** Marked done in
  place, never deleted or renumbered — this file cites its own
  items by number, and so does a TODO entry outside it. Found at
  the W1 revision.
- **Revise at the item's close, not when it next occurs to
  anyone.** Found when the reviewer noticed W2 had closed and the
  file still listed it as pending while W3 was already underway.
- **A reading is written before the branch and counts it.** Lived
  rather than assumed: ten items, four wanting plans, which is
  what made this branch work rather than a single commit plan.
- **The order is preliminary and the reviewer reorders it.** W3
  moved from second to last mid-run, because the branch turned out
  to be the rule's own first firing.
- **An item's own set can close other items.** W6 did not run; it
  closed inside W4's set, because settling D1 meant taking what D2,
  D3 and D4 asked. The list's items are not independent, and a
  reading that assumes they are will over-count what is left.
- **A decision can be answered by a question the list never asked.**
  D1 offered accept, hold or decline. The answer was none of them —
  the reviewer read our own tree and found the mechanism already
  running, unnamed. The three options were all about a role, and the
  thing that mattered was not a role.

## Notes

- Ten work items, five done — W1, W2, W4, W5 and W6. At least four of the rest want a
  commit plan of their own, so by D8's test this stays branch work.
- Revised after W1, and again after W2. What each revision taught
  is in the section above, which is the one W3 reads.
- W9 is deliberately last. A delivery costs the receiver a take,
  and run 3 has three branches of its own queued before SL-3.
- Nothing here is staged into run 3's `temp/` yet. Its tree is
  clean as of `9869798`, so the 2026-09-20 mistake — staging while
  its agent was mid-work — is not in play, but the staging is the
  operator's step either way.
- This file is itself on trial. If it turns out to be TODO's "Now"
  written earlier, one firing will show it and we drop it.

## Why this file has this shape

Written down because it lives nowhere else. The shape was settled
in conversation on 2026-09-23, and W7 will be written from this
file rather than from that conversation.

**The branch is `reading-run-3-2026-09-23`**, cut from main at
`93b7f1a`. Named for the artifact, because the artifact is what
decided the branch exists. Recorded here because this repo has made
no merge commit in its history — every branch is fast-forwarded, so
nothing in main will say a branch existed or what it was called.

**The list is not a commit plan, and could not be.** That
convention rules it out twice over: it plans the commits and not
the change, so what is being changed is settled *before* it opens —
and half the list here is not settled. And it forbids status, where
this list must carry it, because settling one item reshapes or
deletes others.

**The kind is `plan`, by `artifact-kinds`' own test.** *Does it lie
if not kept current?* Yes. Narrowed from "one per project" to one
per undertaking, which that convention permits — contexts may
specialise, not contradict. Its top half is findings, which
describes; a hybrid, named by its dominant force.

**The reading comes before the branch, not after.** The branch test
is whether the work needs more than one commit plan, and only the
list can answer that. So the reading is written first, on main, and
the branch is cut from what it counts.

### What was rejected

- **TODO's "Now" section as the home.** It is the nearest fit and
  the real competitor: an ordered worklist for what is being done
  now, where the last two harvests went. Rejected because TODO
  accretes — completed entries stay as history, which is its job —
  and this list is edited down as it is worked. A record whose
  value is that nothing leaves it cannot hold a list whose value is
  that things do.
- **A branch per step, run 3's standing rule.** Rejected because
  their steps are gated: the gate closes, then the branch
  fast-forwards, so the branch is the unit the gate certifies. A
  reading has no gate. Taking their rule because we happened to be
  reading their repo is the wrong way for a convention to arrive.
- **A `.claude/rules/` file with a `paths:` list.** Rejected on
  mechanism: a rules file loads when a matching path is touched,
  and a reading begins with no file open. The trigger could never
  fire.
- **Making it a convention now.** Rejected as generalising from one
  firing — the thing that withdrew ADR-0021, and what run 3's own
  `shapes-lifecycle` §1 rules out. It goes in as a standing rule on
  trial (D8) and earns promotion or dies.

### What is deliberately not being done yet

The manual, an `installs/` file, or a convention. That is D7 and
W7, and it should be written from two firings. Noting the reasoning
is not promoting it.
