<!-- The talk behind TODO items, kept beside TODO.md: what was
     asked, what exists, the options weighed, what was said for and
     against, the reviewer's own words. A record that decides
     nothing and tells no story: the item's ADR decides, and the
     devlog tells. Our seat only, on trial
     (docs/conventions/project-recording/ §5.5; ADR-0060).

     One section per item: a TODO item, or an open question another
     record holds. Numbered as added; a number is never reused.
     Under it the item's words, then one part per talk, headed by
     its date; a part is never rewritten. The item's See, or the
     record holding the question, names the section.

     The agent asks the reviewer before saving a talk: a new
     section, a part added to one, or nothing, with its
     recommendation. A section is read when its item is worked,
     before its Ideas are weighed, and the devlog says whether it
     changed the work. It goes in the commit that works its item;
     the file stays, empty or not.

     Last touched: 2026-10-25.
     foundation: the project-recording convention -->

# TODO's conversation-memory

## 2. How an approach and a shape divide an output

Item: "Decide how an approach and a shape divide an output".

### 2026-10-20

#### What the reviewer said

It opened with a question: should the shape idea be a model, with
one convention holding both seats, or separate conventions?

A shape is a presumed output, from practice: an output we want to
look the same next time. Why a shape at the gate and not a
template: with a template, or a shape written into the approach,
the agent does the work to it and stops trying other ways. We may
miss a better version, or a case that needs a second shape for the
same approach. We want adaptation. So the shape is kept in
`shapes/`, shown at the gate, and a difference ends one of the
known ways.

So approaches should be written without the output's form: they say
fully what must be done, by their manual, and avoid how the output
looks. Where an approach does not give what a shape needs, the
reviewer listed: the part is optional, and the shape marks it so;
the part was considered and is empty in this case, so it says none;
the part was never considered, by the approach being older than the
shape or touched since, which one home's re-read should make rare.

#### What exists today

- The shapes manual already holds most of the model: written from
  work that exists (§1); "Not a template… Filling a shape in is the
  failure mode it warns about" (§2); read at the gate only, since
  "work written to the shape can only conform" (§3), lived by run 3
  when a shape loaded early (ADR-0052); four endings, decided per
  difference (§5.2). Adaptation is its core: "A shape *wants*
  divergence" (§2); "A shape record that never changes is either
  finished or unread" (§5.2).
- The fourth ending, "the output is a different kind: both stand,
  and a new shape starts", is the reviewer's several shapes for one
  approach.
- §3 holds half of the approach's side: "What must hold while the
  work is written is not a shape. It belongs to the skill… where a
  shape names a part only the work can produce… the skill asks for
  it too." It does not say the other half: a skill carries no form.

#### The live cases

- `cbc-framing` hands over `templates/registry.md`, "Copy-and-fill…
  Fill every slot", for the output the `registry-entry` shape
  governs. Older than shapes (ADR-0008).
- `approach-drafting`'s stage 1 lists what an approach file holds:
  what for, stages, not known, ways rejected, uses. The form of its
  own output, written into the approach.

#### Points made

- The three cases sharpened: a part considered and empty says "none,
  because…", so it reads differently from one left out, as §5.2's "a
  tick with no note is what would be wrong". A part never asked for
  is too late to produce at the gate: a fifth kind of difference,
  whose fix goes upstream to the approach, the output recording the
  gap.
- **The tension:** an approach that asks for a part a shape needs is
  retelling the shape's need, and under ADR-0059 it would carry a
  tag to the shape. A tag invites opening the shape before the gate.
  So the ask is written in the approach's own words, as what to
  capture; the tag serves the walk only; the shape says it is read
  at the gate.

## 3. Layouts as shapes

Item: "Decide whether our own forms become shapes, and whether a
shape's part can be optional", its layout ideas.

### 2026-10-20

#### What the reviewer asked

Is there such a thing as a document layout design, chosen by kind:
one layout for a convention's manual, another for an approach,
another for a shape? Would it help maintenance, readability,
future-proofing, complexity? Then: mark the layout as a shape thing,
a layout shape under the shape model, so layouts adapt, compared at
the gate, with the writing approach carrying none.

#### What exists today

| Kind of document | Its layout | Where | Seen by the writer |
|---|---|---|---|
| a manual | nine sections, in order | `.claude/rules/convention-manual.md` | when a manual is read (a `paths:` rule) |
| a reading | its parts | `.claude/rules/exchange-reading.md` | when a reading is read |
| a skill or rule file | frontmatter, stages, a *Decisions* footer | `docs/conventions/conventions/` §2 | never loaded |
| a record | the form in its header comment | the record | when it is opened |
| an approach on trial | its parts | `approach-drafting`, stage 1 | while drafting |
| a run's outputs | shapes | `.claude/shapes/` | at the gate only |

The writing rule is not one of these: it sets the voice, not where
parts go. Its *Other styles* is where a kind of text would get a
style of its own.

#### Points made

- Under the shape model, a layout is a shape whose output is one of
  our documents: a case of the shapes convention, not a system of
  its own.
- The four questions: one family with one mechanism helps
  maintenance and future-proofing; readability holds either way;
  complexity stays low only if it is shapes extended, not a new
  system beside them.
- **The test is shapes §3's:** what must hold while writing stays a
  rule. A manual's section order may: readers find things in the
  same place across eleven manuals, and a writer who meets the
  sections only at the gate may rework every new manual. How each
  part is written may not.
- A new reading is written without its form in view today, since
  the form loads only when a reading is read (FINDING-4, `162bfb0`).

## 4. What our changelog tracks

Item: "Decide what our CHANGELOG tracks, and how the stub asks it".

### 2026-10-21

#### What the reviewer asked

At the close read's commit 3, which had written `README.md`'s line
"What changed per concept version, for those who pin one": is that
true? Do we have two seats for the changelog? What is a changelog
for, as an idea; what is ours; what is a run's?

Then the reviewer's view, roughly: the changelog a run gets will
serve the system it builds from the delivery, so it could be
prefilled for that. As a stub, it should make the first user decide
what is tracked. That is like the plan and the playbook: a general
plan, and a playbook for the system type we know, which a project
of another kind does without. Our decision to track the concept was
taken long ago; the repo evolved and its responsibilities changed
with no changelog entry. The reviewer asked for every consideration:
update the stub? a playbook analog? how to update ours, what to
track beside the concept, and how not to miss what comes next, such
as the new models in TODO?

#### What exists today

- **The idea** (`docs/conventions/project-recording/` §6): a
  curated record of notable changes per released version, for the
  project's users, answering "what changed between 1.3 and 1.5, and
  will it break me?" without reading commits.
- **The run's seat:** "Its `CHANGELOG.md` logs releases". The stub,
  `delivery/container/CHANGELOG.md`, leaves "what is a version here"
  as a placeholder Framing fills.
- **Ours:** it versions the concept, not a release (ADR-0003). An
  entry is the concept, or an execution derived from or checked
  against it; a convention's or the delivery's change is none
  (ADR-0039, decision 9).
- **The reader it names cannot read it.** ADR-0003, of 2026-08,
  saw runs taking copies pinned to a concept version. Today a run's
  pin is a commit of ours (`ARCHITECTURE.md` §2.5), a run is blind
  to us, and the changelog is never delivered. Its real readers are
  us, and a stranger after a release. `README.md`, `CLAUDE.md`'s
  records table and the changelog's header comment all still name
  the pinners.
- **What was missed:** since v1 (2026-08-28), about 1,350 commits
  added eleven conventions, the container, the models, approaches
  on trial and shapes, and none is logged. Nothing asks again
  whether the changelog still covers what the repo is.

#### Options weighed, with the agent's suggestions

1. **Who reads it:** a stranger who will copy or cite this repo,
   and us. Runs cannot.
2. **What it tracks:** everything that is the product, written as
   what it leaves out: the records, our agent setup, `temp/`. A new
   kind of thing, such as a model, is then tracked from its first
   commit, with no list to update.
3. **What a version is:** the concept version must stay, for
   executions cite it and its bump rule asks whether a derived
   thing could break. A release of the repo is another thing: v2
   carries the concept change and a whole container. Either concept
   versions with the groups logged under them, or a release number
   of the repo's own, each naming the concept version it holds. The
   agent suggested the second; it needs an ADR amending ADR-0003
   and ADR-0039's decision 9.
4. **The gap:** not 1,350 commits rebuilt, which is the "git log
   dump" anti-pattern, but one baseline entry at v2: what each
   group holds now, pointing at the ADRs.
5. **Not missing things again:** a check at each step's close, each
   change outside the left-out paths having an entry or marked
   editorial; and what is tracked read again when the repo grows a
   new kind of thing.
6. **The stub:** it asks only what a version is; our failure shows
   a second question, what is tracked. A `Tracks:` line beside
   `Versioning:`, decided at Framing, with when to revisit it; the
   lesson as a dated italic in project-recording §6.
7. **A playbook analog:** no new file. A fill sets a CbC run's two
   lines at birth, as the playbook fills its plan; we, with no
   playbook, fill ours in place, as §9.4 step 1 already says.
8. **Where each part lives:** the ADR; project-recording §6 and its
   seats; `CLAUDE.md`'s trigger row; the changelog's header; the
   README line.
9. **When:** not inside the close read's plan, being design. A TODO
   item, due when the release item opens, since that item needs a
   changelog entry.

The reviewer said to write the item. Its Ideas are 2 to 7, unweighed;
1, 8 and 9 went into its Context and Trigger.

## 5. Run 4's reading: two moves from layer 6

Item: "Read run 4 against `dac4dd1`, the run 3 commit it was born
from", its two Ideas lines added in `7db58ed`.

### 2026-10-21

The agent proposed, and the reviewer took, moving two of round 1's
layer 6 findings into this item rather than fixing either side:

- **FINDING-77:** the container's `retrospective` skill puts a
  "rules in force now" list on top of the decisions log, which is
  append-only. Run 3 and run 4 both did it. The practice was lived
  twice, so its evidence should decide which side changes: the
  skill, or the log's rule.
- **FINDING-81:** `cbc-framing` writes a status line into the
  run's README, where `docs/conventions/project-recording/` §7.4
  keeps changing status in PLAN. How that line lived in a run
  decides, and run 4 is the next run read.

Nothing more was said of either; the reviewer said "go, write the
plan".

## 6. The method's plain rewrite: `cbc-slice`'s opening

Item: "Rewrite the method's texts plain", its Ideas line on
`cbc-slice`'s opening, added in `7db58ed`.

### 2026-10-21

FINDING-82 found the container's README stub saying an invariant
is "closed by a test", where the concept says the test proves a
wall, and the wall closes it. The stub was fixed in round 1.
`cbc-slice`'s own opening line says the same, stating the
completion test alone; it was moved here, not fixed, because it is
method text, and round 1's rule for the method was to change a line
only where it is untrue. Wording that is true but could be plainer
waits for this rewrite.

## 7. Footers and retellings in shipped files

Item: none in TODO. These are the five of *Met in round 1, for
round 2* in `temp/refinement-2026-10-18.md`, which round 2 reads
first.

### 2026-10-21

#### What the reviewer asked

During layer 6, after `visual-comparison`'s mid-text ADR citations
were cut (FINDING-79): why remove the references, how is the trail
kept now, and why were the ADRs there at all? And of a line in
`commit-messages`, "`CLAUDE.md` and `.claude/` are the working
arrangement…": when agent-arrangement changes, what finds this
line? It carries no tag, so a grep would miss it.

Then: how do we know which place in the text a footer line backs,
now that the ADR no longer sits next to the text? Is it decided
anywhere, and should it be? And: what happens to a footer when a
delivery goes to a run? Is it dropped?

Earlier the same morning the reviewer had asked whether the seed's
playbook version, which lags behind in other places too, should
carry tags, and whether some of it should not live in the seed at
all, taking it that deciding is not round 1's. Items 1 and 2 of the
list came of it.

#### What was answered

- **Why ADRs were cited:** so anyone who doubts a rule can follow
  it to its reason. Conventions §2 moves them to a *Decisions*
  footer, cited once, since mid-sentence citations are noise to an
  agent reading at the moment of use. A grep for an ADR number
  still finds the skill.
- **What the cut lost:** two citations named decisions 2 and 3 of
  ADR-0027, and the footer named the ADR only. Two footer lines
  were added, each naming its decision, then each naming the
  section it backs (§4 and §5 of `visual-comparison`), so either
  side finds the other. ADR-0030's footer line already did this.
- **The `commit-messages` line:** the reviewer was right. The walk
  greps for the changed manual's path; the skill's line retells
  agent-arrangement §1 with no path, and its `foundation` names
  commit-messages, so nothing reaches it. Under ADR-0059 that is a
  second home. It cannot simply be tagged: the skill ships, and a
  run cannot open our paths. That is ADR-0059's run case, left to
  round 2.
- **A look back** found one more of the same kind: `cbc-bootstrap`
  and its walkthrough retell repo-hygiene §2 and §3, with no path.
  Lines that retell the manual their own `foundation` names are
  reached by the `foundation` grep, and are fine.
- **A footer in a run:** its `CBC ADR` lines name ADRs a run can
  never open. Weighed, none decided: keep them as provenance, so a
  run can quote "CBC ADR-0027" when it asks why; drop them at
  delivery, lighter, but no longer byte-identical, which breaks the
  one-diff check; or keep them, with a line in the file saying what
  they are for.

All five went into the round 2 list as written there.

## 8. Run 5's full-auto birth

Item: the step "Birth run 5, on full auto" in `PLAN.md`, opened
from TODO's run 5 birth item.

### 2026-10-21

#### What the reviewer asked

Between the refinement's rounds: can it stop for another step? The
reviewer wants another run on full auto: the agent decides
everything, updates itself where needed, its approaches included,
and writes an approach on trial wherever it finds work with no way
written down, a plan step among them. Run 4's full-auto setup is to
be read again, for what to repeat and what to change. Prepare it,
but not start it; go back to the refinement; start the run before
stopping for the day.

Then: a new problem, its intent reaching "LAYER-5-INTERACTION …
what emerges when areas interact; correctness across them",
moderate in size, "not too small, but also not to blow". Should
preparing an auto run start an approach on trial of its own? And
what might be missed?

#### What was answered

- **A step can stop for another** (`PLAN.md`'s step form): marked
  `[!]`, its stage kept; main takes its branch by fast-forward; the
  next step is cut from main. Done at `e849b6a`. Run 5's pin then
  sits on main.
- **The birth:** `delivery/installs/pure-seed.md` exists and has
  born every run; it copies this repo's tree, pinned at `HEAD`, so
  run 5 gets the latest delivery, round 1's fixes in, rounds 2 and 3
  not. The tree must be clean when it runs. `exchange-birth`, the
  birth as the exchange's third act, does not exist yet; drafting
  it during this birth would close half a TODO item for about an
  extra hour. The reviewer chose the seed alone.
- **An approach on trial, yes, for preparing a full-auto run:** it
  was done once, inside run 3, never on our seat (ADR-0058). It
  is `auto-run`.
- **Run 4: a light read,** not its full reading, which waits for
  the refinement's close: run 3's hand-off (`temp/RUN-4.md`), run
  4's decisions log and `RETRO.md`, for how full auto went. The
  reviewer added: what run 4 skipped for want of a way, since those
  are the gaps run 5's approaches on trial may fill. The cost: run
  4's method lessons and its edited copies do not reach run 5.
- **The problem:** LAYER-5 is empty by construction with one area,
  so at least two areas, each owning its facts, whose meeting can
  go wrong. Weighed: event tickets (seat holds, payments, orders: a
  hold expiring as its payment succeeds); equipment rental
  (reservations, check-out and return, deposits); a shared wallet
  (accounts, transfers, limits: two transfers each passing a limit
  check, together breaking it), which may prove one area under
  concurrency, too small. The reviewer chose event tickets, the
  intent theirs to write. The container's rule holds: nothing
  before the briefing names the problem, and this repo hands over
  the hand-back line only, never an opening prompt.
- **What might be missed:** the two TODO items due before a birth
  (shapes read at birth; shipping `temp/`); the run's own settings,
  as run 4's hand-off had them; when the run stops and how the
  reviewer checks on it; its directory,
  `~/IdeaProjects/cbc-pure-run-5`, and its row in
  `ARCHITECTURE.md` §2.5; that a full-auto run takes hours.
- **The order:** first staged as a step that only prepares, the
  birth waiting in TODO while the refinement resumed. The reviewer
  then chose to birth right away and stop for the day, so the step
  takes the birth, and the refinement resumes the next day. The
  retrospective item's trigger, "the close of the step that runs
  run 5's birth", holds again.

### 2026-10-22

#### The briefing

The reviewer asked for help writing run 5's intent, which framing
commits unchanged as its briefing. The agent drafted it on the five
headings runs 3 and 4 used; the reviewer chose each open point.

- **One event, not several.** Several events add bookkeeping,
  keeping each show's seats apart, and almost no new trouble;
  concurrency, many buyers on one seat at once, is there with one.
- **Refunds out.** Weighed as a third area, refunds, beside holds
  and orders: new meeting points (never refund someone who got a
  ticket, never refund twice, a refund racing a late second
  confirmation), about a third more work, perhaps 6–7 slices
  against 4–5. Bounded, it would read: "In: asking the provider to
  return a payment when its confirmation arrives for a seat no
  longer held, and only then. Out: any other refund — a buyer
  cancelling, part of a payment, a ticket already issued." Left
  out to keep the run moderate; a good next run, the same system
  and one more area. The service records who is owed, so a paid,
  unheld seat is still the run's question.
- **The two complaints kept,** though they point at the two
  promises: an owner would say them, and the open decision still
  leaves the promise to framing.

#### The stack, the name, the remote

The reviewer asked whether the bootstrap repeats run 3's stack,
whether the run names itself after framing, whether it might
create a remote, and whether run 4 had trouble with any of it.

- **The stack** is delivered: the seed copies the `spring-postgres`
  group, so the ground is PostgreSQL in podman with the migrator
  and runtime roles, and the skeleton Spring Boot 4, Java 21 and
  Maven, in our edited versions no run has used. Nothing said the
  stack is given; the hand-off now does.
- **The name:** the playbook's Step 2 decides it after framing, but
  the ground's database and roles are named from it. The seed
  expects the briefing to bring the name, so the briefing names the
  service `event-tickets`, and Step 2 keeps it. The folder stays
  `cbc-pure-run-5`.
- **The remote:** Step 2's title says "remote", and on full auto
  nothing stopped a `gh repo create`. Banned; the remote is the
  reviewer's after Release. Run 4, its name settled in advance, had
  a one-line Identity step, no remote and no push, as the light
  read found; it could not be read again, being locked.
- **Podman:** every container and volume on the machine is visible
  to any process, among them run 3's and run 4's databases; a lock
  on folders does not reach them. Weighed: a rule and trust, or
  exporting and removing other projects' containers and volumes
  until run 5 is done. The reviewer chose the rule: run 5 uses only
  what it creates.

## 9. A commit plan's look-back at the way

Item: "Decide whether a commit plan's look-back also asks if the
work could have been done better".

### 2026-10-21

#### What the reviewer asked

While run 4 was read for run 5's birth: did run 4 use
`commit-plan`, with provisional ADRs? When it planned meaningful
work, did each step it did change how it had planned? Things look
one way before the work, and a step or two in, something shows that
was not seen. Then a proposal: before a commit plan closes, look
back and check whether the work could have been done better; only
for a real, meaningful change, try that way and compare it with the
agent's first try before deciding which to keep. Should that be
marked to check?

#### What exists today

- **Run 4 used `commit-plan` twice,** both for its retrospective
  (`58ce0a1` to `cf221b3`, `95e9091` to `74a4445`). Its framing,
  skeleton and four slices were steps, each with its gate written
  first, and small commits; none was a commit plan. Its one
  recorded divergence: commit 5 of the apply plan split when a
  script missed an anchor, and a commit was added outside the plan.
- **Provisional ADRs, some:** ADR-0007 and ADR-0011 opened
  Proposed and were accepted later; all 13 are Accepted.
- **`commit-plan`'s look-back** checks the landed commits for their
  grouping only: "two that are one change, or one that is two".
  Divergence already lets a plan change when a commit needs
  something else (`commit-plan` §5).
- **Run 4's `try/` branches:** each Real question's options tried
  before the decision, 14 branches, 2 tries changing the answer.

#### Points made

- The idea looks back at the way, not the grouping, and is close to
  what worked on run 4's `try/` branches.
- It needs a bar for "meaningful", or every plan doubles its cost:
  the better way changes a wall, a test's adversity, or removes a
  part.
- It is tried first in run 5's hand-off, since run 5 runs on auto
  and its log will show whether it paid. Shipped in the convention
  now, it would decide for every run before one has tried it. The
  reviewer agreed to mark it.

## 10. Examples in the concept, the conventions and the approaches

Item: "Decide whether the concept, the conventions and the
approaches keep examples".

### 2026-10-21

#### What the reviewer asked

After the light read showed run 4 copying run 3's kills from the
shapes' examples: the examples reach further than the shapes, into
the concept's method too. Could run 5 be born with the delivery as
it is, and its copies then changed, before any commit, so that
every example or clue becomes a plain description of what must be
done, with nothing to follow? Checked several times, so nothing is
missed and nothing contradicts. Then, seeing the size: too much
work; "it is for consider that later if we should be keeping
examples in concepts, conventions and approaches". The shapes stay,
read at the gates only.

#### What exists today

Where examples live, counted that day:

| Where | What it holds |
|---|---|
| `cbc-framing` and `cbc-slice`, `references/worked-example.md` | 271 lines each, a whole order service with payments; it weighs "Orders are never lost AND payment always completes" |
| `concept/`, five chapters | 24 lines naming orders, bookings, inventory, payments and the like |
| the slice workflow, `cbc-framing`'s SKILL, the playbook | smaller examples |
| the container's `writing.md` | "Three submissions with key k-42 … one order exists" |
| the stack | `cbc-bootstrap` and the establishment walk |
| the method's four shapes | a tiny order service, its tags and its numbers |

#### Points made

- **Where to strip, had it been done:** not in the newborn's copies
  after the seed. Its pin would claim copies equal to a commit they
  do not equal, and every stripped line would read later as an
  edit the run made and never logged. The honest way was a branch
  here with the stripped delivery, seeded from, kept forever, never
  merged.
- **The cost:** a few hours, with several checks, which would have
  moved the birth to the next day.
- **The concept:** stripping its examples changes what `concept v1`
  says, even in one run's copy; each such edit would have needed a
  mark that the concept had not changed.
- **What stands instead:** the shapes are read at the gates only
  (ADR-0061), and run 5's hand-off asks its analysis to show: each
  probe committed before its verdict.

## 11. How work is run by agents

Item: "Decide how work is run by agents: delegation, model and
effort by kind of work, forks or fresh agents, new challenges and
look-backs; and what the agent's setup holds, and where that is
recorded".

### 2026-10-22

#### What the reviewer asked

With run 5 already started, so nothing in it changes: should there
be a convention on how to use models and efforts, and on how work
is managed, mostly on full auto but in ordinary work too? Say a main
agent hands readers something to read and collect, at low effort;
when a problem needs deciding, finding the options takes the
highest effort, in one agent; once the options are found, several
agents at medium or high effort implement and report back as a
summary. None of this, efforts, forks, delegation, is defined
anywhere. Nor how new challenges are met, or looking back, as just
decided for run 5.

#### What exists today

- **Delegation by judgement:** on 2026-10-21 the agent sent 3
  readers to run 4 and 8 to round 1's close read, each a fresh
  agent with a written brief, at the default effort.
- **No record of models:** run 4 changed from Fable 5.1 to Opus 5.5
  mid-run, and only the reviewer's own memory says why.
- **New challenges:** `approach-drafting`, shipped.
- **Looking back:** a commit plan's look-back, on trial in run 5,
  with a brake.
- **The agent's own tool** sets another agent's effort only when the
  reviewer has asked for a level; otherwise the default holds.

#### Points made

- A real gap, but a convention now would be rules nobody has lived,
  the fault the light read found in run 4's hand-off. New work
  starts as an approach on trial (ADR-0058).
- Where it lives is the text-division item's question:
  agent-arrangement says what an agent holds; how an agent works
  may be a convention of its own or a section of that one.
- Evidence first: from the next session, each delegation leaves one
  devlog line, its kind of work, model, effort and whether it paid;
  run 5's reading adds how a run on full auto delegated by itself.

### 2026-10-22, at `/doctor`

#### What the reviewer asked

`/doctor` offered to run every general-purpose agent on Sonnet. The
reviewer kept them as they are, and held the question for this
item: model and effort by kind of work, not one default. Then:

- Why was so much never used? Not found, not asked for, or else?
  Could any of it help our work?
- What is Claude Docs? Is it what `one-home` tried for in Markdown?
- Which skills come from Claude, are there more, and is there a
  skill that finds skills before one is built?
- Is leaving the account skills on better or worse, if a convention
  may later record what is on or off?
- Grade the 13 account skills by chance of need, in a table: the
  grade, what each does, where it could apply in our work.
- Is what was turned off, and what was left, recorded with its why?
  Where? Is moving it elsewhere an open question, once we decide how
  skills that are not ours are maintained?

#### What exists today

- **Subagents:** 69 general-purpose agents in 29 days, none given a
  model, so all on Opus; `/usage` puts them at 11% of a week's
  usage. The 11 Explore agents ran on Sonnet, set by their own
  definition.
- **Account skills:** 15 synced from claude.ai. None of the 13 still
  on was used since install; together about 2.3k est. tokens in
  every session.
- **The marketplace:** Claude Code holds the official catalog, 315
  plugins, none installed. `/plugin` browses it; no skill searches
  it.
- **Claude Docs:** a claude.ai editor with comments, sharing, charts
  and export. Its connector loads in every session; no call in 29
  days.
- **A record exists:** the records table sends agent setup changes
  to `.claude/decisions.md`. Its 2026-10-22 entries hold every
  switch-off so far, user-wide ones among them.

#### Points made

- Unused because the work never called for them: Office files,
  browsers, Google files. Nothing was missed, and no ask left them
  out.
- Claude Docs is a place; `one-home` is a rule about places. Records
  belong in git: history, reviewed commits, runs that read the repo.
  Docs fits a page for a reader outside git.
- Chance of need is a guess no one can measure. The grades went by
  evidence instead: can't run here, no trigger, named trigger,
  regular work. Each middle grade carries its trigger.
- By that table 12 were turned off and `skill-creator` kept; the
  table is in `.claude/decisions.md`, 2026-10-22.
- A skill to find skills would be building ahead. The trigger is a
  habit: search before a new skill is proposed.
- `session-report` would show what each delegation cost. `/usage`
  first; the plugin only if it falls short.
- User-wide switches act in every project, yet only this repo's log
  records them. Where they belong is open.
- Skills that are not ours arrive and change without us: claude.ai
  syncs new ones, plugins update. When the table is graded again is
  not yet asked by the item.

### 2026-10-22, `claude-md-management`

#### What the reviewer asked

- How does `claude-md-management` work? Do we use it when we touch
  `CLAUDE.md`? Should we, how often, and should it keep that file?
  What else are we missing?
- Should its end-of-session question be an idea, checked against
  how we already keep the entry file? Should the pass over the
  nearest plugins go in TODO too?
- Does that idea mean rechecking the convention? Should it come
  next, after this TODO work?

#### What exists today

- **The plugin:** Anthropic's, not installed. A skill scores each
  CLAUDE.md from A to F on commands, architecture, gotchas, length,
  currency and actionability, then adds what it finds. A command,
  `/revise-claude-md`, asks at a session's end what context was
  missing, and adds one-line learnings to CLAUDE.md.
- **Our way:** agent-arrangement §2 says what the entry file may
  hold; the foundation check runs at every commit that touches it;
  `.claude/decisions.md` keeps the why.

#### Points made

- It assumes a code repo. It would score our records table low and
  ask for commands and a directory map, which `/doctor` cuts as
  derivable.
- It writes learnings into CLAUDE.md. Here a learning goes to the
  record that owns it (`one-home` rule 1).
- It looks for `.claude.local.md`; Claude Code reads
  `CLAUDE.local.md`, so ours would never be found.
- Graded no trigger. Worth taking: its end-of-session question,
  with each answer routed through our own path.
- "What else are we missing" is answered by search, then grading:
  the pass over `session-report`, `hookify`, `claude-code-setup`,
  `superpowers` and `mattpocock-skills`.
- The idea uses the convention as it stands; it does not recheck
  it. A recheck would follow only if answers keep landing where the
  convention has no rule.
- Not next: the open step takes the text-division item first, and
  that item decides where how agents work is written.

## 12. A session's end

Item: "Decide whether a session's end has a home of its own, and
what it holds".

### 2026-10-22

#### What the reviewer asked

- Should the session-end question be used as findings, and decided
  only once they are gathered? Should we then change what
  `CLAUDE.md` holds, or improve something else?
- Does all this belong in the sweep idea, parked for look-backs and
  regrouping, with this question added to it?
- Should a session's end be a convention of its own, put in TODO
  with its options recorded as they come? Is there such an item
  already?
- Is it true we may want two conventions, one for sweeps and one
  for session ends, to control better what each does? What else is
  there?
- Should the missing-context question be an option in the
  session-end item too?

#### What exists today

- **A session's end:** project-recording §4.4 asks for a devlog
  entry and a Resume line; the records table names the moment. Two
  habits live only in the agent's private memory: a line per
  delegation, and from 2026-10-22 one missing-context finding.
- **The sweep:** a TODO item, its parts one home and regrouping,
  now a missing-context part too.
- **Look-backs:** a commit plan's, inside the plan; `retrospective`,
  a run's at its end, shipped to runs; our seat has none of its own.

#### Points made

- The asking and the deciding split. Asking needs the session's
  memory, so it stays at the session's end, one devlog line. The
  deciding needs many findings, so it goes to the sweep. One gap
  may be a one-off; a batch shows which repeat.
- A finding's ending is wider than `CLAUDE.md`: the entry file, a
  rule, a skill, a record, or nothing.
- A convention here is tied to a moment. A session's end and a
  sweep are different moments, read different things and write
  different things, so each may want its own home.
- The form, convention, section, approach on trial or rule, is the
  text-division item's to decide; the item's title stays neutral
  so as not to assume it.
- Four look-back moments: inside a commit plan, a session's end,
  after work lands, a run's end. One subject or four is a
  text-division question.
- Two session-end habits are invisible in the repo, and runs never
  get them: a reason to give them a written home soon.
- A session's start is the twin: what is read first.
- The missing-context question is already in the item, as a habit
  it must place; an idea for it would be a second home.


## 13. What the reference to a fact's home is called

Item: "Define the fact reference, and stop calling it a tag".

### 2026-10-24

Met while the text-division item's close was planned: one
`foundation` per file, the root, and a tag on every line that uses
a part of any document, the root included.

#### What the reviewer asked

- Channels, pointers and tags: how is each defined, and does what
  was just decided need them fixed? Should "tag" go back to
  "pointer"? What do Claude Code and the community call it?
- Ids beside each section, or the section's number and title? Ids
  would demand an id near each section. When a section is touched,
  every reference is checked and updated.
- The form "(<path>, §<number>, <title>)": is the title worth the
  length, for knowing what a section is without opening it?
- "Citation" may be the text quoted, not the label. In Java one
  object has many references pointing at it: is this the same?
- Is the label just how a reference looks? Keep "tag" as its
  synonym, or write `reference(...)` or `refer(...)`?
- "Source of truth" instead, used in descriptions and talk, since
  "reference" will mean other things later and needs saying whose
  it is? Should one-home itself become "source of truth"?
- Then "fact reference"?

#### What exists today

- **channel:** defined, `docs/models/agent.md` §4: how text reaches
  the agent.
- **pointer:** only used, in the agent model's claims P1 and P2:
  text that sends the agent to a file it may not open.
- **tag:** only used, `one-home` rule 2 and project-recording §11:
  a path and section on a line, for the walk's grep. Also the repo
  prefix "CBC ADR-0053" (ADR-0020); git tags and image tags beside.
- **Near words:** home, master, canonical, follower (`one-home`
  rule 5), retelling.
- **Measured:** 137 numbered section titles in the manuals and
  models, a mean of 13 characters, the longest 56, 13 over 30;
  about 115 references in the form `path §n`.
- **Outside:** traceability calls the link a trace link, and tools
  mark it suspect when its source changes; Anthropic's skill docs
  call a pointer to files loaded when needed progressive
  disclosure; docs-as-code says single source and cross-reference.
  None calls it a tag.

#### Options weighed, and what the reviewer took

| Name | For | Against | Taken |
|---|---|---|---|
| pointer | already in the model | names whether an agent follows it, P1 and P2 | no |
| tag | in use | git, image and repo-prefix tags; defined nowhere | no |
| citation | plain; "the tag a citation carries" half in use | names the quoting, not the label | no |
| reference | the Java word; plain | too general once used for other things | no |
| home reference | says where it points | names the address, not what is relied on | no |
| source of truth | the industry's word | names the home, not the link | as the definition of home |
| fact reference | named after its target, as Java's object reference | what is written is the home's address | yes |

- **One-home stays one-home.** "Source of truth" names a place, not
  the rule; "truth" is busy here ("project truth", canonical); a
  fourth word beside home, master and canonical; a rename in both
  seats and a note to runs.
- **No ids:** the number says where, the title what, and either
  finds the section if the other changes; nothing new beside each
  section. The title is taken, cut to its first words when long.
- **No prefix word:** the walk finds a reference by its path, and
  `reference(...)` reads as code in prose.
- **The Java parallel, and where it breaks:** one fact, many lines
  pointing at it; but a retelling holds a copy, so the walk re-reads
  it when the home changes.

The reviewer's draft for *The words*, kept as said:

> **fact reference** — what a line carries when it relies on a
> fact written elsewhere: the address of the fact's home, written
> `(<path>, §<number>, <title>)`. The home is the one place the
> fact is written, its single source of truth (`one-home`). When
> the home changes, the walk greps for every fact reference to it.

## 14. A sweep, and what looking back is

Item: "Decide whether a sweep checks one home after work lands, and
when".

### 2026-10-25

#### What the reviewer asked

- facts-in-sync was to say that a description states what is true
  today. Should other texts be checked for history sentences: now,
  in round 2, or later; in the sweep, or at a session's end?
- In their words: "i may want convention and model (or part like
  section or what of model) for sweap and session end checks. It is
  idea that has to have definition, which sounds something like: we
  look back and check agains rules, source of truths, correctness
  and something like that to find what is out of date or no more
  incorrect or has a conflict, disagrement or any possible
  incorrectness. it should be define in as one-home and reference
  where needed."

#### What exists today

- Five acts read a text against what it rests on: the foundation
  check, at each commit; `commit-plan`'s sweep, at a plan's close;
  a refinement round; an exchange reading; and the missing-context
  finding, at a session's end.
- facts-in-sync §4 holds the walk, and §5 a disagreement. Nothing
  names the act they share, or lists when it runs.

#### Points made

- History sentences: round 2's One home kind finds them once
  facts-in-sync says it, since such a sentence retells its ADR. The
  sweep greps for names a plan moved, and a history sentence has no
  fixed word to grep for. A check every session for something
  written rarely costs more than it finds.
- What a check is fits the idea-to-output model, beside §3's links,
  where either side may be wrong. When each check runs stays in its
  own convention, pointing at the model.
- Not built now: round 2 does not need it. Its moment is this
  item's trigger, the refinement's close, when the refinement's
  approach is judged: the largest check this repo runs.

## 15. Each seat's copy, written for its seat

Item: "Decide whether each seat's copy is written for its seat".

### 2026-10-25

#### What the reviewer asked

It began with commit 2's fact reference to the sweep, which named
only the container's skill: does our commit-plan sweep too? It
does, since the two skills are the same file today. In their words:
"i dont like that thing "byte-identical to the shipped one"
anymore. because it should be all as "byte-identical to the shipped
one" or non. now i need to track which are and which not. it would
be simple to repeat things and alter each part according to seat."

#### What exists today

- ADR-0042: both seats derive from the manuals, neither copied from
  the other; a file identical in both is an outcome, not a
  dependency. It rejected diverging the identical files as "a
  change nobody needs".
- Five lines say which are the same: commit-plan, commit-messages
  and visual-comparison, each "identical to it today";
  agent-arrangement's "Three skills are identical files"; and the
  conventions manual's rule that a file of ours byte-identical to
  its shipped master keeps `CBC ADR-nnnn`, so one diff checks the
  pair.
- The commit-plan manual names the sweep only in §2, "The sweep
  reads the text unwrapped". Only the skills say it runs before a
  close.

#### Points made

- Stating an outcome makes each manual keep it true by hand: the
  tracking the reviewer would drop.
- Each seat written for itself leaves nothing to track, and each
  copy reads for its own reader. It reverses ADR-0042's rejected
  option, so it needs a new ADR, and the one-diff check goes.
- Not the facts-in-sync plan's: its commit 2b points at the
  commit-plan manual instead of the container's file.

## 16. Which way a fact reference points

Item: "Decide which way a fact reference may point: up, sideways,
across chains".

### 2026-10-25

#### What the reviewer asked

It began at facts-in-sync §3's line "The agent may follow it to
read the fact whole, with no guarantee that it will
(`docs/models/agent.md` §4.2, claim P1)". In their words: "it may
be that this fact now lives only in model. but what if that fact
also was in convention, then which we should refer? model or
convention? why? do we need to define that choose how to choose?
how much combination there could be and how much we should
bother?" And: "should we refer to convention because it is more
specific to what we are on, as model is more general case of that
fact?" And: "the more deeper levels in idea-to-output chain is the
more specific it is … and when we need reference, it is more
specific the more deeper we refer to. and also it hold idea that
top levels does not refer to lower levels. also it kind of suggest
that if we refer to fact we always look for our level of that fact
reference and check upwords to top level first. we should never
check in reverse". Does the same apply to approaches? What is
missing?

#### What exists today

- `docs/models/idea-to-output.md` §3: every link points up; a line
  may point at a fact's home in any document; an approach stands on
  a description, never on a model directly.
- 11 of 12 manuals point at the agent model without standing on
  it, mostly in *Why it arrives this way*, as the manual form asks.
  Each manual's *What this does not cover* points at its
  neighbours, sideways.
- No approach points at a model today. `auto-run.md` did, at the
  agent model's §10.4, until that section moved to
  agent-arrangement §5.4.

#### Points made

- No choice between levels: a fact has one home, so a reference
  has one target, the home of the fact its line relies on. The same
  fact in a model and a convention is a second home, a One home
  finding.
- What looks like one fact at two levels is usually two: the
  general one in the model (an agent may not follow a pointer, P1),
  the specific one in the convention (so we retell where the reader
  acts, facts-in-sync §1). The line relies on one of them.
- "Deeper is more specific" describes the chain, but choosing by it
  goes wrong both ways: a convention pointed at for a model's claim
  costs the reader two hops; a model pointed at for a convention's
  choice loses the repo's decision.
- Looking at one's own level first, then up, is a way to find the
  home; the rule stays the fact relied on.
- The real gap is direction: what "up" means between two texts of
  one level, or of two chains. The model's "every link points up"
  is stated more strongly than practice, which points sideways in
  every manual.
- The one-target sentence follows from one home and goes in
  facts-in-sync §3, in the plan's commit 2b. The direction waits for
  round 2's Dependencies kind, which reads every pointer.

### 2026-10-25, later

#### What the reviewer asked

On `.claude/rules/convention-manual.md` item 5, "Pointers to other
conventions as paths from the repo root": "should here be pointers
as references and conventions as levels of chain, where in this
case models and conventions? is this fix for later when we have
this idea which we just include in todo about reference level
references and where and what it should refere?"

#### Points made

- The line is wrong twice. "Pointers" names the written address,
  which facts-in-sync §3 calls a fact reference. "Other
  conventions" is narrower than practice: 11 of 12 manuals point at
  the agent model, as item 7 of the same file asks.
- Both wait on this item. What replaces "other conventions" is the
  direction it decides. Retiring "pointer" as a noun is a decision
  ADR-0065 did not take; it retired only "tag".

## 17. What kind of text our ARCHITECTURE is

Item: "Decide what kind of text our ARCHITECTURE is, and its size".

### 2026-10-25

#### What the reviewer asked

After commit 5 of the facts-in-sync plan edited it: do we have both
seats of it, what is each, and how do they differ? How does it
differ from a model? Does it hold redundancy, or miss something?
Should anything move out of it, or into it as its home? Is it part
of the idea-to-output chain? Does it hold on maintenance,
readability, future-proofing and complexity? Then: how would it be
useful if done correctly; what does project-recording say it is
for; how useful is it in runs; should we keep it at all, and should
it be a run's thing only?

#### What exists today

- project-recording §8 holds both seats. A run's maps a built
  system in one or two pages: a diagram, components, an invariants
  table, a `src/` codemap. Ours maps documents and the delivery:
  3,608 words, with *The words* and a known-wrong list inside. A
  run's glossary is its own file, `docs/glossary.md`.
- §8.2: ADRs are a history of choices; ARCHITECTURE is the
  synthesized present, read second, after the README. §8.1: what a
  later slice may rely on.
- In a run it is load-bearing. `cbc-bootstrap` writes what a slice
  may rely on; `cbc-slice` adds one Invariants row per rule at a
  slice's close, and its gate checks the rows against the build;
  the entry file sends "asking what a slice may rely on" there. Run
  3's RETRO D10 made it that home, after certified history was read
  as current; D16 cut its 2,031 words to the table.
- In ours no skill writes or reads it. Writing rule 6 makes *The
  words* the home of each coined word.
- Three texts name its kind differently: facts-in-sync §4 a
  description; idea-to-output §2 lists only manuals and the concept
  as descriptions; project-recording a record. It carries no list
  of what derives from it, which a description must.

#### Points made

- A model is an idea any repo can adapt; ARCHITECTURE maps one repo
  today. Not a model.
- §2.3 says which convention owns each of the 23 container files;
  each file's `foundation` already does, and the walk greps it.
  Commit 5 edited that sentence for one convention, as every new one
  will.
- §2.5, §3 and §4 may retell exchange, facts-in-sync and
  agent-arrangement: round 2's One home kind reads them.
- §1 says "two bodies of writing" and leaves out the models.
- Counts ("twelve manuals", "twenty-three files") go stale with
  every addition; a pointer does not. "Three movements… the
  material, the motion, the actor" is metaphor.
- Maintenance, future-proofing and complexity do not hold;
  readability is weak.
- Done right, ours would answer in one or two pages what nothing
  else does: how the stated and the made usable pair, where each
  thing goes, and where each local map is. The foundation lines
  and the walk now record what depends on what, file by file, so
  the map need not.
- The run's is plainly worth keeping: the method writes and checks
  it. Ours has thin evidence of being read; its live use is *The
  words*. Kept short, it is the newcomer's forest and what a
  maintainer's container would be filtered from (ADR-0042). Made
  run-only, our map would move into the README and *The words* to a
  file of its own.
- Not in the facts-in-sync plan: round 2 reads layer 4 next, and
  what falls outside its kinds is this item.
