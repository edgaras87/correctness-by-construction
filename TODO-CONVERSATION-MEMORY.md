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

     Last touched: 2026-10-21.
     foundation: the project-recording convention -->

# TODO's conversation-memory

## 1. How this repo's text is divided

Item: "Decide how this repo's text is divided: by kind, a model, a
convention or an approach, and by subject".

### 2026-10-20

#### What the reviewer asked

- This repo maintains the delivery: the container, the method, the
  stack practice. Is that an idea of its own, a convention? Where is
  it defined? Do we need one?
- We share conventions with runs, split by seats, and we have a
  convention about conventions. Do seats need a convention of their
  own? Or should all of this be one convention with sections, or
  separate conventions pointing at each other, kept in step by one
  home?
- Which holds best for maintenance, readability, future-proofing
  and complexity? Is it round 2's?

Then a proposal, in the reviewer's words, roughly: describe ideas
such as seats, the deliverer and the run, and one home as
**models**, freely, binding nothing. Then **conventions** describe
a specific case: one home could have a case in project-recording,
in the conventions manual, in a run's tagging of its invariants and
kills. Then **approaches** — skills, rules, shapes, the agent's
bundle — come from those conventions. Is this good or bad?

And: the agent's chain, model → agent-arrangement → `.claude/`, was
written before this way of thinking, and may have errors; recheck
it before copying its shape. Describe `model → convention →
approach` as a model itself. Maybe the whole repo is chains of
dependencies.

#### What exists today

| Idea | Where it is written | Kind of text |
|---|---|---|
| this repo maintains the delivery | `ARCHITECTURE.md` §2 and §3; "deliverer" in *The words* | a description |
| why the repos are shaped so, and the planned move of the delivery to a repo of its own | `docs/models/tiers.md`: the method layer "held by the concept repo… until three repos have lived (ADR-0038)" | a model, binding nothing |
| what passes between deliverer and run | `docs/conventions/exchange/` | a convention |
| the playbook's steps flowing down, lessons flowing up | `docs/conventions/project-recording/` §9 | inside the records' convention |
| seats | `docs/conventions/conventions/` §3.4, one rule; a seats section in eleven manuals | a rule, applied eleven times |
| one home, followers, tags, the walk | project-recording §11; conventions §3.1, §3.2, §3.5, §3.6 | split over two manuals |
| what the records are | project-recording §1, "The model at a glance" | a model inside a manual |
| the agent | `docs/models/agent.md` → `docs/conventions/agent-arrangement/` → `.claude/` | the only full chain of three kinds |

#### Options weighed

| Question | One big convention | A convention per idea | The rule of thumb |
|---|---|---|---|
| Maintenance | one file, many subjects to keep apart | each change in one manual; more pointers | changes in one place, no empty manuals |
| Readability | the opening cannot name one subject | each opening names one subject | as per idea, where rules exist |
| Future-proofing | hard to move part of it when the delivery leaves | each piece moves alone | each piece moves alone |
| Complexity | low overhead, much mixing | each convention costs its form: manual, seats, index, counts, an ADR | pays the form only where there are rules |

**The rule of thumb proposed:** a convention for each subject that
has rules of its own and a moment they act; a description or a
model for what a thing is; a section for a single rule. By it:
maintaining the delivery stays a description and a model, with no
rules beyond the exchange's; seats stay one rule; one home is a
convention of its own.

#### The layers, as discussed

```
model → description → approach → output
        (convention       (skills,     ▲
         or concept)       rules)      │ governs, read at the gate
                                     shape ← written from earlier outputs
```

- **Good:** each layer changes for its own reason; it fits one home
  (one model, a rule per case); it undoes a mix lived on 2026-10-19,
  "what a concept is" against "how one is written"; the conventions
  manual mixes what a convention is (§1) with how to write one and
  how everything stays in step (§3).
- **Risks:** "binds nothing" cuts both ways: if nothing makes a
  manual follow its model, the model drifts into decoration; if
  something does, it is a description. The agent model sits between:
  agent-arrangement "reasons from" it, a link with no named upkeep.
  Three layers for every idea means three walks for every change.
  A case is usually a seat, so one manual per subject with a rule
  per case, not a manual per case.
- **The gate proposed:** a model only where several manuals share an
  idea, or where what it is and what we do were mixed in practice.
  Candidates: one home; what a convention is; the deliverer and the
  run, with seats; a shape; the layers themselves.
- **A shape is not a layer after the approach.** It is written from
  outputs and governs the next output at the gate; written from the
  approach, it would describe intent, a template. "Governs" is one
  of the local map's three links (`9fd905b`: derives, points,
  governs), the one with no upkeep yet; "reasons from" would be a
  fourth.
- **The agent's chain first:** recheck it against the layers before
  it serves as the template, so its errors are not copied.

#### Related, already placed

- Round 2's Layout finding names staying in step as a convention of
  its own, with a rule for each case: ours, manuals by path and
  section, re-read by the walk before every commit; a run's, its
  invariants, kills and slices tagged by id; records linking
  records (the refinement's file; ADR-0059).
- Folding the agent model into agent-arrangement is the same
  question the other way round (its own TODO item).

#### Other threads met in this talk

Each has its home, named in it.

- **Does a manual still go on trial,** now that unproven work stays
  in approaches? `.claude/approaches-on-trial/approach-evaluation.md`,
  *Not known yet*.
- **Does "stages from earlier work" retire** from the step form's
  opening item? `.claude/approaches-on-trial/approach-drafting.md`,
  *Not known yet*.
- **What catches a small TODO item outside a step,** now that
  first-time-work's skill and its description are gone? The same.
- **What a run does with a piece left its own:** keeps it as an
  approach, or writes a skill or rule of its own?
  `approach-evaluation`, *Not known yet*.
- **`approach-drafting`'s footer:** it was left without one to dodge
  the tag problem; DECISION-6's line in conventions §2 now lets an
  identical copy cite `CBC ADR-0058`. For its first evaluation.
- **An exchange §3.2 line runs past 72 characters** (`cfbe031`):
  round 3's to see.
- **Is generalizing work of its own?** The reviewer asked whether an
  approach for generalizing is needed. Not now: it is step 6 of
  `approach-evaluation`, and both are the deliverer's alone, so no
  seat splits them; if its first use shows it is work of its own,
  that evaluation splits it. `approach-evaluation`, *Not known yet*.
- **How a run's offered approach reaches the evaluation.** Weighed:
  a skill opening at a second moment, when a reading meets the offer
  line; `working-a-reading.md` pointing at the evaluation; nothing,
  the reading working it by hand. Left open when the evaluation
  itself went on trial; today only its own *When it opens* says it.
  `approach-evaluation`, *Not known yet*.
- **Whether the in-place design change moves to every step form.**
  First drafted into both step forms, then kept to the refinement,
  since only the refinement had lived it (`8c9aadf`). The
  refinement's evaluation at its close decides.
  `.claude/approaches-on-trial/refinement.md` §3, *Not known yet*.

#### The candidate models, one by one

Each is a model that the gate proposed above would allow: an idea
several manuals share, or one where what it is and what we do were
mixed. For each: what it would say, the cases that would be its
conventions or rules, where its pieces sit today, and what stayed
open.

##### One home

- **What it would say:** each fact has one home; elsewhere a
  pointer; a copy is a follower, tagged by a label grep finds,
  defined at the fact's home; a change at the home finds and
  re-reads every follower, with its paragraph, and a host that is
  itself a source walks on; history is not a second home.
- **Its cases:** ours, manuals and rules, tagged by path and
  section, re-read by the walk before every commit; a run's, its
  invariants, kills and slices, tagged by id, re-read when the run
  changes the fact, not designed yet; records linking records.
- **Where it sits today:** project-recording §11; conventions §3.1,
  §3.2, §3.5 and §3.6; `.claude/rules/one-home.md` and the
  container's; ADR-0053 and ADR-0059.
- **Open:** round 2's Layout finding names it a convention of its
  own; the run's case is designed with it.

##### A shape

- **What it would say:** a presumed output, written from outputs
  that exist; read only at the gate, so the work can show it wrong;
  it adapts, and a shape that never changes is finished or unread; a
  difference ends one of four ways, and a part never asked for is a
  fifth, fixed upstream; the approach that makes the output carries
  no form.
- **Its cases:** a run's outputs, the method's shapes; our own
  documents' layouts, a manual's, an approach's, a reading's, a
  record's.
- **Where it sits today:** the shapes manual, its §1 and §2 a model,
  §3 to §5 rules;
  `delivery/container/.claude/rules/shapes-lifecycle.md`; the
  method's four shapes; our form rules, `convention-manual.md`
  and `exchange-reading.md`.
- **Open:** the reviewer's question, one convention with both seats
  or separate conventions; whether our forms become shapes (TODO);
  how an approach and a shape divide an output (§2).

##### The deliverer and the run

- **What it would say:** a deliverer holds the masters and makes the
  delivery; a run builds blind, from pinned copies; files go down
  whole, what the run learned comes back as a reading, a verdict
  returns; each side holds only the half it can run; every
  convention has the two sides as its seats.
- **Its cases:** the exchange, what passes between them; the
  playbook's flow, steps down at birth and lessons up after a run,
  project-recording §9; the retrospective, how lessons are found;
  the seats rule, conventions §3.4, and eleven seats sections.
- **Where it sits today:** `ARCHITECTURE.md` §2 and §3;
  `docs/models/tiers.md`; *The words*: deliverer, run, seats.
- **Open:** the tiers model plans the delivery's move to a repo of
  its own; this model would move with it.

##### What a convention is

- **What it would say:** a way of working written down once, in a
  manual, and made into the rules and skills a project acts on; a
  rule, not a method, that the work may ignore with a reason it can
  give.
- **Its cases:** the conventions manual's form for a manual, §3.3;
  its artifacts, §2; how one is added, §4.
- **Where it sits today:** the conventions manual, §1 holding the
  model, §2 to §4 the rules, and §3.1 to §3.6 also holding staying
  in step, which belongs to *One home* above.
- **Open:** whether a manual still goes on trial now that approaches
  exist.

##### The layers

- **What it would say:** model → description (a convention or the
  concept) → approach → output, with a shape governing the output
  from beside it; each link has its kind and its upkeep: reasons
  from, derives, points, governs.
- **Its cases:** the agent, the only full chain today; the concept
  and the method; each model above, once written.
- **Where it sits today:** nowhere as a whole. The local map's three
  links are in `9fd905b`; "reasons from" has no home.
- **Open:** the reviewer's guess that the whole repo is chains of
  dependencies; the agent's chain to be rechecked first.

### 2026-10-21

#### What the reviewer asked

Between layer 3's commits: is it true that the tiers model will
most likely be updated, and that the chain discussed the day
before, `model (idea) -> idea description for specific case
(convention or concept) -> approach -> output -> shape`, "most
likely should live here with changes"?

#### What was answered

- **The tiers model will change, yes,** whatever is decided.
  `docs/models/tiers.md` §2.2 already holds a small version of the
  chain: a concept repo holds "the **mental** layer" and "the
  **executions** derived from it", which is description, then
  approach, for concepts only. Its §1 and §2.1 list what "how you
  work" holds; approaches and shapes would join that list.
- **The chain living in tiers: no, a model of its own,** which
  tiers points at. Tiers answers *which repo* a thing belongs to;
  the chain answers *what kind of text* a thing is and how it links
  to the others. Every repo holds several kinds, so the two cross,
  and one model holding both would be the very mix this item is
  about.
- **"Layer" is taken three times already:** the concept's
  LAYER-1-ENVIRONMENT to LAYER-5-INTERACTION, the refinement's
  file layers 1 to 6, and tiers' mental and executions layers. A
  "layers model" would be a fourth meaning; the chain needs another
  name, such as "the chain of kinds".

Two Ideas lines came of it, held while layer 3's plan was open and
added in `abae9c4`.

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
