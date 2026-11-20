<!-- The talk behind TODO items, kept beside TODO.md: what was
     asked, what exists, the options weighed, what was said for and
     against, the reviewer's own words. A record that decides
     nothing and tells no story: the item's ADR decides, and the
     devlog tells. Our Convention Seat only, on trial
     (docs/conventions/project-recording/ §14, Conversation Memory; ADR-0060).

     One section per item: a TODO item, or an open question another
     record holds. Numbered as added; a number is never reused.
     Under it the item's words, then one part per talk, headed by
     its date; a part is never rewritten. The item's See, or the
     record holding the question, names the section.

     The reviewer's words are quoted as said, and stay so. Each
     heading that quotes them is followed by two more. First, the
     same words edited: grammar and spelling fixed, the meaning
     kept, under the heading's name with ", edited". Then, where
     the words hold an ask, "What the reviewer asked, as the agent
     would ask it": each ask put in the agent's words, to show its
     reading. Since 2026-11-08, judged with the record's trial.

     The agent asks the reviewer before saving a talk: a new
     section, a part added to one, or nothing, with its
     recommendation. A section is read when its item is worked,
     before its Ideas are weighed, and the devlog says whether it
     changed the work. It goes in the commit that works its item;
     the file stays, empty or not.

     Last touched: 2026-11-20.
     Why the form is as it is: (docs/conventions/project-recording/
     §14, Conversation Memory).
     foundation: the project-recording convention -->

# TODO's Conversation Memory

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

### 2026-10-26

#### What the reviewer asked

Is a form the same as a shape, the one read before the output and
the other after? Should the two share a name, such as a
pre-output shape? Rules and skills already carry no shape: the
shape is checked at the output, and an eval improves it. Then:
what of manuals, models, the concept and the method? And does the
form hold on maintenance, readability, future-proofing and
complexity?

#### Points made

- A form is not only a layout. It also holds rules for the moment
  of writing, such as "add an item the moment it is discovered",
  which a shape cannot hold (`docs/conventions/shapes/` §3). A
  record's form is both, in one place.
- No new name: "pre-output shape" would name a thing this item may
  remove. If layouts become shapes, "form" keeps only the writing
  rules.
- The test for a shape: many of a kind, and a moment to check
  them. Manuals, readings, skills and rules pass. A record's
  entries have no gate of their own, so the record keeps its form.
  Models, three with no shared parts, and the one concept do not.
- The reviewer agreed the record's form stays, and the manual's and
  the reading's forms stay rules until this item decides.
- The four questions, for the record's form:
  - maintenance: one home per rule after the refinement's plan 2
    for layer 2, but two seats each hold a copy, and nothing checks
    they agree;
  - readability: the rule is where the writer looks, and hidden
    from a person reading the page; the header grows;
  - future-proofing: a live run never takes a form's change, since
    records go once, at birth (`docs/conventions/exchange/` §2.4);
  - complexity: no new mechanism, but writing rules and layout
    share one comment.

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

### 2026-10-30

#### What the reviewer asked

With round 3's read committed and 10% of the week's Fable usage
left: "how much this session holds? if i start new model, will i
loose anything? … does we have in session (model) something we
should save as doc that other session and model could catch? is
what we have done, like that big reading is save in sessions
memory? model? how that works? if change model, but work on same
session, does i still be working on same thing?" Then: "maybe we
should have this how sessios, models and memory works writen into
our repo? in agent model maybe?"

#### What exists today

- **The rule, in general:** the Agent Model §6, only what is written
  into the repo survives the session; §5, the context window.
- **The mechanics, lived today:** a model switch inside a session
  keeps the transcript, so the new model sees every word and tool
  result but not the old model's reasoning; the nine readers the
  usage limit stopped kept their transcripts and resumed by
  `SendMessage`; a new session keeps the repo, the devlog's Resume
  line and the user's memory files, which are per user and outside
  the repo.
- **The save point:** a devlog entry with a Resume line, written
  before a switch; today's at `90a70bc`.

#### What the reviewer took

The devlog entry first, then the decisions on the same model, a
devlog entry at about 97% of the week's usage before switching, and
another after the last decision. The mechanics as an idea line under
this item, not a change to the Agent Model mid-refinement: the model
states the rule, the binding would hold the mechanics, both when the
item is worked.

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

## 21. A full read for missing fact references

Item: "Decide whether a standing full read looks for missing fact
references, and for references pointing down".

### 2026-10-27

#### What the reviewer asked

After the fact reference item's seven decisions: "let say we still
miss to add fact-reference somewhere from time to time for some
reason, maybe we miss to consider. i thinking about this reread all
repo and check where we miss fact-reference. now i would should it
go together with a planed sweap or session-end? should it be as
sep? should it be only about fact-reference check or together with
something else that needs full read of repo? but we should be aware
that this should comply with fact-reference checking??? or we
should think on this as some multi agent task where one agent or
group of agent has this fact-reference check task?" Weighed by
maintenance, readability, future-proofing and complexity.

#### What exists today

- **The sweep:** a grep for moved names at a commit plan's close
  (`docs/conventions/commit-plan/` §2.10).
- **Session end:** records only; the devlog entry and its
  missing-context line.
- **The refinement's rounds:** their Dependencies kind reads every
  file for a line missing its fact reference. Round 2's close read
  ran seven agents, one kind and one seat each: 52 findings, 32 of
  them places a round 2 fix had missed.
- **Coming:** the rewrite touches all 329 references; round 3 and
  the refinement's last read cover every file.

#### Options weighed

| | In the sweep | At session end | A separate read, by foundation, by agents |
|---|---|---|---|
| Maintenance | runs too often, finds little | runs too often, finds little | runs when its trigger fires |
| Readability | none | none | one report per foundation |
| Future-proofing | grows heavier with the repo | grows heavier with the repo | a reader per foundation |
| Complexity | mixes a grep with a read | mixes recording with reading | one piece of work, one job |

- A missing reference is the hardest kind to find: the reader must
  know the fact lives elsewhere. So the unit is a foundation, a
  description read beside every file built on it.
- The read needs its rule first: the settled form in facts-in-sync
  §3.1.

#### What the reviewer took

A separate read, by agents and by foundation, with no machinery
built now. It waits on its trigger: a read that finds a missing
fact reference in text written after the per-commit check is in
force.

## 22. Testing fact references and foundations as a whole

Item: "Test fact references and foundations as a whole: name every
scenario a change brings, and check each still holds".

### 2026-10-28

#### What the reviewer asked

While ADR-0070's homes were written, at commit 5 of their plan:
"i thinking to mark todo after we finish refinement or later to go
again through current fact-reference (+foundation) and check if
everything holds after we make change in one-home or when we need
to change in fact-reference side. we should name all scenarios and
look if everything works as expected. So its thing which i want not
to forget to test and look again to see how it is define, how it
works, is nothing is missing and other similar stuff. so its like
diagnostic. because i already see 2 types of keeping everything in
place, where one is used by grep and other needs text eval by
reading and checking if logic is holding. and this one home needs
second one, that logic would hold after we grep pointers to
on-home facts."

#### What exists today

- **The grep:** the rename grep (`docs/conventions/facts-in-sync/`
  §3.3, *A rename is grepped at its commit*) and the walk's greps
  for a path and a `foundation` value (§4, *The rule for every
  description*, step 3).
- **The read:** the walk's re-read of each retelling with its
  paragraph, the foundation check's read of a derived file against
  its foundation, and the question asked of each new or changed line
  at the commit (ADR-0070).
- No one has walked every scenario through both.

#### What the reviewer took

An item with options, not a choice: on paper, a drill on a
throwaway branch, agents, or a kind in the refinement's last read.
Due when the refinement closes. A diagnostic: what it finds becomes
findings or TODO items, and it changes no rule itself.

## 27. Shared names of conventions and approaches

Item: "Rename the manuals, Agent Skills and Agent Rules that share a
name".

### 2026-10-31

#### What the reviewer asked

At the design's question 8, after the agent recommended renaming
the five manuals: "now i confused and thinking maybe we should leave
that names can be same? we kind of solved by how we refer, by adding
suffix, doent we? what else is wrong if we leave the same names?
could we bring more clarity by having different names? can u show
examples how we could rename both ways … should we bring rules how
we name conventions and how we name approaches, like different
grammar, expression or something like that?" Then: "show me others
too how could look after renaming with those rules".

#### What exists today

- **The kind word, always:** "the commit-plan manual", "the
  commit-plan Agent Skill" (the refinement's DECISION-24 and 27).
  Reading is no longer ambiguous.
- **What stays wrong:** a grep for a shared name finds the manual,
  the Agent Skill, the `foundation:` lines and the paths together;
  history and the CBC Runs' records say the bare name and are never
  reworded.
- **The grammar, tried on every name:** all 12 manuals already fit
  "a subject, a noun", and all 10 Agent Rules fit "what it governs,
  a noun", which cannot part a manual from an Agent Rule. Agent
  Skills follow no one pattern: subject and act (exchange-read,
  infra-establish), act and subject (apply-retrospective), a noun
  (commit-messages). A strict "verb first" renames 11 of 12; a loose
  "has a verb" renames 3 and lets commit-plan through, since it
  reads as a noun or as subject and act.

#### What the reviewer took

The current names stay, the five shared ones too. A rule for new
names: a new name never repeats a manual's, an Agent Skill's or an
Agent Rule's, checked by grep; a new Agent Skill takes a verb. The
renaming, either way the tables show, waits until the CBC Runs built
with the old names have been read: a TODO item, with this talk kept
here.

## 28. Text at the wrong level of the chain

Item: "Read text for its level in the chain, the Levels Finding Kind,
both ways across each boundary".

### 2026-10-31

#### What the reviewer asked

At the design's commit 5, after facts-in-sync §3.4 was written: "do
we have skill or rules for conventions and facts-in-sync? because
what we have write now in them feels as approach. should we mark
those as todo for later to check again and decide if we should have
split into manual and approach?" Then, the item added: "do we also
need to check if vica versa for approaches? what about `model ->
convention` thing, do we need to check both side too? should we have
this defined as approaches which we could use as refinements or
what? like after some times, we do repo check and refinement where
we check how text is writen, and do we need some updates, fixes or
any other change (like the one we noticed on this change)?"

#### What exists today

- **The split, since ADR-0078:** a manual says what, how and why; its
  Work Approaches state the rules and explain nothing.
- **facts-in-sync** has Work Approaches: both one-home Agent Rules and
  the Foundation Check. Its §3.4 first listed rules with almost no
  why; it was rewritten with a reason per point (`96a4d82`).
- **The conventions manual** has the Agent Rule for a manual's form;
  its §1, the rules for writing an Agent Skill or Agent Rule, reaches
  no writer but by reading the manual. TODO's "Write an Agent Rule
  that writes a skill or Agent Rule from its convention" holds it.
- **When a refinement comes again** is open in the refinement's own
  text, judged at its close.

#### What the reviewer took

One item for the whole check: both boundaries of the chain, Idea Model
and manual, manual and Work Approach, each read both ways. It is a
Finding Kind, Levels, for the next refinement, due when this one
closes and decides whether a refinement comes again. This talk kept
here.

## 29. Two checks on text kept true

Item: "Decide which ideas here are Idea Models".

### 2026-10-31

#### What the reviewer asked

At the design's commit 5d, reworded at the reviewer's request: "We
wrote the Idea-to-Output Model so that our texts do not become false
over time. A line written today can stop being true later, when other
texts change. We want the texts never to contradict each other. Each
carries a reference where it needs one, so that when one place
changes, the others are adapted and the whole picture stays true. We
cannot be sure this holds, so we run whole-repo refinements, and what
we just found is one of their results. A refinement checks that the
repo still holds true, and also finds what was missed. When we find a
miss, we can find why it was missed, and improve how we keep the
texts true so that it does not happen again. So a refinement is a
second wall. The first is the rules we follow at each change; when
something slips past them, a full read of the repo catches it. Is
this right? What am I missing, and what could be done better? Will it
hold on maintenance, readability, future-proofing and complexity?
Where, how and when should we define it?" Then: "Should it have an
Idea Model of its own, or be a new section of one we have?"

#### What exists today

- **The first check has four layers:** the Foundation Check and
  one-home rule 6 at each commit; a commit plan's sweep and look back
  at its close; a Plan Step's close items; the reviewer at every
  boundary, whose questions caught four of the day's slips.
- **The second is the refinement,** an Approach on Trial. Its stated
  job is old text meeting a new rule; catching misses is a second job.
  Most of Refinement Round 3's 644 findings are text older than
  writing rules 9 to 11.
- **What was missing:** a finding's cause, so a miss teaches the first
  check; the scripted checks, rebuilt in three sessions and never
  kept; one place that shows the two checks together. A test of the
  first check before it fails is TODO's "Test Fact References and
  foundations as a whole".
- **Weighed on four questions:** maintenance holds once each miss gets
  its cause; readability not yet, the checks spread over five texts
  and three TODO items; future-proofing partly, since full reads grow
  with the repo; complexity low, every piece existing.

#### What the reviewer took

A cause for every finding from Refinement Round 3's close read on, as
the refinement's own change (`fc4efe0`); the two-check view
in the refinement's *Not known yet*, judged at its close with where it
is written. Whether the idea is an Idea Model, a section of the
Idea-to-Output Model or of a one-home model, is this item's, due at
the same close. This talk kept here.

## 30. Reading a CBC Run born before

Item: "Read a CBC Run born before the refinement by its needs, not
its diff".

### 2026-10-31

#### What the reviewer asked

After the method's Names table, the reviewer asked how CBC Runs are
read once the structure changes: "how we gonna read runs after and
decide what to take from them if we now change structuraly? how we
see difference? can we decide what runs done and what new was found,
if we have different structure?"

#### What exists today

- **A read compares the CBC Run with itself:** its copies against its
  own last delivery, its Decisions Log, its Run Asks
  (`.claude/skills/exchange-read/SKILL.md`, step 3). Our renames do
  not touch that diff.
- **Taking an item back lands it in our Master Copy**
  (`.claude/rules/working-a-reading.md`, rule 4). An edit written
  against "slice" or "fence" meets Invariant Slice or Scope
  Exclusion there.
- **The Names table maps old words to Names,** but it lives in
  `temp/` and goes at the refinement's close, before CBC Runs 4, 5
  and 6 are read.

The agent proposed giving every Glossary Name its old words in its
entry, so the map outlives the table.

#### What the reviewer said

"when we redo everything with this glossary naming thing, we will
bring better defined full picture. it will not only better frame
definition, but also how everything is put together. so what i think
will happened, is we cant just compare what run have changed. what we
could still do is what how run was going and what it did and consider
if something what is not defined in our new way put together repo is
missing or not, or if something is definded in not right way and we
should change something. i think what could happend after refinement,
is we can find that we frame our delivery in different way and some
run parts is no more relevant. but all this is just a guess."

On the order: stopping the Plan Step to read first "is not best
decision", since the reading "could be still done on old way of
current system we have before refinement", while "i still be working
on old structure which i already see improvement. so yes, i think we
should continue on improvement and reading comes after."

#### What the agent added

- **The diff loses weight; the why keeps it.** A Decisions Log entry
  and a Run Ask say what the CBC Run needed, which survives any
  restructure.
- **"No longer relevant" needs its reason.** A CBC Run that struggled
  with "slice" may have struggled with the idea, which a rename does
  not fix. So each item ends met, still missing, or no longer
  applies, with why the need is gone.
- **Not designed now:** nothing has tried it. The Run Reading of CBC
  Run 4 tests the guess.

#### What the reviewer took

The refinement goes on, and the readings come after it. The way of
reading waits as a TODO item, triggered by CBC Run 4's Run Reading.
Every Glossary Name's entry names its old words, and `exchange-read`
diffs `docs/glossary` too: both added to the design's commit plan.

### 2026-10-31, later

#### What the reviewer asked

When the old words were staged into the concept's entries: "i dont
see this as good idea. it also could mean plain english word. why we
filling those?" Then: "remind we why we need this at all?"

#### What the agent found

- **The line breaks rule 9:** "Older text: "fact"" beside Enemy Fact
  tells a reader a plain "fact" may be the Name.
- **It serves one reading and ships forever:** only CBC Runs 4, 5 and
  6 wrote the old words; every CBC Run born after would carry the
  line in every entry.
- **The need is mostly met already:** most Names hold their old word;
  the Names table maps the rest and stays in git; a reading by needs
  reads a word in its context; a CBC Run born before learns the
  renames from its next Delivery Note.

#### What the reviewer took

No glossary entry names old words, the renamed ones included. A Run
Reading reads them through the Names table at its last commit; a
delivery to a CBC Run born before names the renames in its Delivery
Note. The earlier part's last paragraph is reversed here.

## 32. The agent's memory

Item: "Write the understanding of the agent's memory, and how it is
checked".

### 2026-11-07

#### What the reviewer asked

"there is also rules, that u like write your self to remmeber, like
u adapt by what i correct u or something, but we not store those.
are they in some memory or what? [...] i mean what we loose when we
start new session." Then: "do u read only that sessions memmory?
[...] Should i note that at session ending i should check that
memory for rules that lives only there and decide if i want those to
become pernament". And: "does that means that there is a rule in
chat that does not live in memmory or anywhere else?"

On why it exists: "it does not split into sessions? why it exist
then? why it is there? why not in claude local? do i have to manage
it?" On seeing its changes: "how we see the difference if its not
tracked? is it worth to have snapshots after checks?"

On git inside the memory folder: "i dont see how it will work. you
would be commiting in both repos, one in memory and and one here?"
On the date of the last check: "why we need last check time at all
if we cant see what was touched?"

#### What the agent showed

- **Memory is per project folder, not per session:** every session
  in this folder shares it; the index loads, notes are read when
  relevant; it is not in git and stays on this machine and path.
- **What a new session loses is the chat:** three rules that day
  lived only there, until saved.
- **The repo's Agent Model is wrong about it:** "The repo — the only
  durable memory" (`docs/models/agent.md` §2).
- **A file's time tells which note changed, not what changed in it:**
  nothing old is kept to compare against.

#### What the reviewer said

The reviewer's own form of the check: "each note is sep doc which has
last touch date. we store those as some tags like name and date. if
something we missing that means its new, if something mem is missing
that means its out, if date is diff that means it changed and if note
and date are same it doesnt changed." The agent's form, one date
alone, missed deleted notes.

On where the list lives: "i not sure about devlog, as it could go
aways later and i could loose this rules if i will forget that."

On running it any time: "maybe include also to consider like skill
or rule, where i could run it like /context which gives full check of
that memory and/or chat same way as session end, but maybe with or
without that registry that check?"

#### What the reviewer took

The session-end check, on trial in `CLAUDE.local.md`: the chat's
rules placed or let go; memory compared with the last check's list
of names and dates; both shown as tables; the list written into the
session's devlog entry. Git inside the memory folder dropped. An
understanding text to be written, with all of this, as a TODO item.

## 33. CBC design beyond backends

Items: "Split the concept into general understanding, the System
Kit's backend case and their instructions, losing nothing"; and "Try
CBC design on the finished Common Ground Problem, beside the way
chosen".

### 2026-11-08

#### What the reviewer asked

The agent had said CBC design needs no middle level, since only
System Repos use it, and that the concept is general. The reviewer
asked: "maybe it would be better if we have middle and current one
was mostly middle of system kit? what if cbc design could be not
only for backend (which is now?) but for anything?"

Then of this work: "i already feel we are doing this now on this
repo at this exact moment or we could be doing
"common-ground-problem"? we have this pain description, attacks and
where it could fail, then we may have invariants, guarantees and
test for what we try to do here right now." The draft's purpose was
written as the backend System Kit's is.

"if we could adapt cbc design for "common-ground-problem" in this
maintainer repo we could also maintain it in similar way as in
backend, where if we want introduce something new, we would need to
check if holds our design. we could also decide if it just feature
or invariant. if it is invariant we would need do this analisys. we
could build adapted understanding and instructions how that is
done."

#### What the reviewer asked, edited

The same words, with grammar and spelling fixed, the meaning kept:

- "Maybe it would be better if we had a middle level, and the
  current concept was mostly the System Kit's middle? What if CBC
  design could be not only for backends (which it is now?) but for
  anything?"
- "I already feel we are doing this in this repo at this exact
  moment, or we could be doing it for the Common Ground Problem. We
  have this pain description, attacks and where it could fail; then
  we may have invariants, guarantees and tests for what we are
  trying to do here right now."
- "If we could adapt CBC design for the Common Ground Problem in
  this Maintainer Repo, we could also maintain it in a similar way
  as in the backend: if we want to introduce something new, we would
  need to check that it holds to our design. We could also decide
  whether it is just a feature or an invariant. If it is an
  invariant, we would need to do this analysis. We could build
  adapted understanding, and instructions for how that is done."

#### What the reviewer asked, as the agent would ask it

The questions the reviewer was asking, put by the agent:

1. Is the concept general, fitting any system, with today's
   delivery as its adapted case for backends? If so, does CBC design
   need a middle level after all?
2. Is the Common Ground Problem itself a problem CBC design could
   solve? Its purpose reads like a Falsifiable Promise, and its
   Failure Cases like sources of adversity. Which of CBC's parts
   does it still lack?
3. If the Maintainer Repo adapted CBC design to the Common Ground
   Problem, could the repo be kept the way a backend is? Each new
   change would first be sorted: a feature, or a change that touches
   a System Guarantee. Only the second would get the full analysis.
   Would that need its own adapted understanding and instructions?

#### What the agent showed

- **The concept names no backend:** "A system is what it promises
  about a hostile world" (`concept/00-cbc.md`). The backend sits
  lower, in the Method Group and the `spring-postgres` Stack Group.
  Its examples and words still lean toward software.
- **The draft already holds part of CBC:** §1's purpose as the
  Falsifiable Promise; §4's Failure Cases as sources of adversity;
  §7 as how it could be falsified; §8's "an instruction only when
  work needs one" as feature-thin. Missing: System Guarantees and
  Structural Walls.
- **Today's answer is detection:** sweeps, the Foundation Check, the
  refinement's reads. CBC calls that correctness added afterwards;
  it may explain the cost in the draft's §5.
- **Five risks:** a wall is hard to build in text, so CBC may become
  a checklist; part of the system is a person, so the promise must
  be about texts and sessions; it is circular, the repo judged by
  the concept it keeps; it is an answer, and stage 1 states the
  problem only; making the concept general reaches every CBC Run.
- **It fills a cell:** the draft's §2.1 table gives the Maintainer
  Repo no CBC instructions. With CBC applied to common ground, both
  groups take the same shape, an adapted text on each side of one
  general text.

#### What the reviewer said

On the order: "we continue as we did till now, without cbc design
adapted to our common-ground-problem. we just make change now that
cbc has general understanding and that we have one adapted case for
backends in system kit." The trial comes "after we finish working
with common-ground-problem", applied "to completed
common-ground-problem and see what we can do". The split of the
concept into general understanding, the System Kit's adapted case
and instructions is to be done "without loosing any info and
correctness of cbc concept and methods".

#### What the reviewer said, edited

The same words, with grammar and spelling fixed, the meaning kept:

- "We continue as we did until now, without CBC design adapted to
  our Common Ground Problem. We just make a change now: CBC has a
  general understanding, and we have one adapted case, for backends,
  in the System Kit."
- "After we finish working with the Common Ground Problem", applied
  "to the completed Common Ground Problem, to see what we can do".
- "Without losing any information, or the correctness of the CBC
  concept and methods".

#### What the reviewer asked, as the agent would ask it

The question the reviewer was asking, put by the agent:

1. Should the trial of CBC design on the Common Ground Problem wait
   until the problem is finished? Only the claim that CBC design is
   general, with one backend case, would be written now, and the
   concept's split would be decided in stage 2.

#### What the reviewer took

The draft says now that CBC design is general and the System Kit
holds one adapted case, for backends (`4938344`). Stage 2 sorts the
concept and the Method Group into general and backend, labels only;
the split is a TODO item, after the Plan Step, so the way chosen
shapes it. The trial on the Common Ground Problem is a second item,
after the split: CBC from a clean general text is a fairer test
than from today's mixed one. Why the trial waits: stage 1 stays a
problem; a way chosen without CBC is the baseline to compare
against; CBC needs a settled promise to derive from.

### 2026-11-09

#### What the reviewer asked

On the simulation of what passes between the repos: "just for
curiosity how that is similar what we do in cbc design? (we will do
that later)"

#### What the reviewer asked, edited

The same words, with grammar and spelling fixed, the meaning kept:

- "Just out of curiosity, how is that similar to what we do in CBC
  design? (We will do that later.)"

#### What the reviewer asked, as the agent would ask it

The question the reviewer was asking, put by the agent:

1. Does the simulation's step form match CBC design's parts, so the
   simulation can feed the CBC trial?

#### What the agent showed

- **A step's "what can go wrong"** as a source of adversity.
- **A step's "what is marked"** as a Structural Wall: a pin makes
  "we don't know what was delivered" impossible.
- **Scenarios as checks** as tests that fail when the system drifts
  from its design.
- **A new scenario needed** as a change that touches a System
  Guarantee, so the full analysis runs.

#### What the reviewer took

Kept for the trial: the simulation is its natural input.

## 34. Refining a document

Items: "Design how a document is refined: a broad Adapted Case, an
Output Shape read after the work, and how each corrects the other";
and "Decide where small work is gated when it is too small for a
Plan Step".

### 2026-11-12

#### What the reviewer asked

The agent had run nine checks on the simulation, chosen by itself,
on the reviewer's ask. The reviewer: "what about those checks we
applied to simulation doc, should we note them? i thinking to have
later Adapted Case for refining docs, which i run by my ask for now.
Maybe we should draft one now?"

Then, once the checks were noted: "i thinking to have this idea we
not yet dealt about output shape. i thinking we should have it
applies to doc refinement, where rule has this broader description
of refinement without specific points and telling to find out agent
itself. that, when results comes, we check with the shape. we update
shape if needed by outputs if something new is found. we rerun
refinement checks if something from shape is missing. this kind of
needs plan step or something similar where we put gate. or as some
sep work, which could be done during the plan step, when we feel
that doc needs refinement. if this is not plan step, then we need
work idea with gates at the end, which looks like plan step but it
isnt because it is too small for one. what u think on this and how
we should store this? as multiple todos? with conversation mem?"

#### What the reviewer asked, edited

The same words, with grammar and spelling fixed, the meaning kept:

- "What about the checks we applied to the simulation document:
  should we note them? I am thinking of having, later, an Adapted
  Case for refining documents, which for now I run by asking. Maybe
  we should draft one now?"
- "There is an idea about the Output Shape we have not dealt with
  yet. I think it should apply to refining a document. The rule
  holds a broad description of refinement, with no specific points,
  and tells the agent to find them out itself. Then, when the
  results come, we check them against the shape. We update the shape
  from the outputs when something new is found. We run the
  refinement's checks again when something from the shape is
  missing."
- "This needs a Plan Step, or something like it, where we put a
  gate. Or it is separate work, done during a Plan Step, when we
  feel a document needs refining. If it is not a Plan Step, we need
  a kind of work with gates at its end, which looks like a Plan Step
  but is not one, because it is too small for one."
- "What do you think of this, and how should we store it? As several
  TODO items? With Conversation Memory?"

#### What the reviewer asked, as the agent would ask it

The questions the reviewer was asking, put by the agent:

1. Should the checks run on the simulation be written down, and
   should an Adapted Case for refining a document be drafted from
   them now?
2. Should a refinement work as an Output Shape does? The Adapted
   Case stays broad and names no checks. The Output Shape is read
   against the results. What the results hold and the Output Shape
   lacks goes into it. What the Output Shape holds and the results
   lack is checked again.
3. Where is that Output Shape read? A refinement is too small to be
   a Plan Step, yet it needs a gate at its end.
4. Is this one TODO item or several, and is the talk saved?

#### What the agent showed

- **Draft later, note now:** one run on one document would give a
  case that copies that run. The nine checks went into the devlog
  entry, and a TODO item waits for a second document.
- **Most of the idea exists:** an Output Shape is read at a Plan
  Step Gate only, so it does not steer the work, and a difference
  may end with the Output Shape changing
  (`docs/conventions/shapes/` §2.3, *Not a convention*; §3, *Where an Output Shape lives*).
  The nine checks are a first draft of a refinement's Output Shape.
- **What the run showed:** the walk of one case through every part
  found the contradiction and the gaps. The scripts found none.
- **One caution:** an agent that reads the Output Shape before it
  works follows it as a list, and stops looking past it.
- **The new part is the gate,** and it is wider than refinement:
  any small work that needs a check at its end has it. A commit
  plan's close is one candidate. The agent would not design the
  small work now.

#### What the reviewer took

Two TODO items and this section: the refinement's item rewritten to
hold the Adapted Case, the Output Shape and how each corrects the
other; a second item for where small work is gated. The Adapted Case
is not drafted yet.

## 35. The layers of knowledge

Item: "Model the layers of knowledge in a draft of its own, then
write the model into `temp/common-ground/common-ground-problem.md` §3, *The
Knowledge Axes*".

### 2026-11-14

#### What the reviewer said

While the simulation's opening was made plain, on its "step by
step": "also these step by step sounds not nice, but i think this
must first be changed in common-ground-problem. we should define
there this from change to take there as one thing of what this is."

Then the model: "we should refine our "common-ground-problem". I
think we should start from "## 3. The Knowledge Axes". we should
define 3 layer model of knowledge similar we had idea model if i
remmeber right, when we had sep repo open for it. So basical we
define model where to top layer is project agnostic, second layer is
adapted case, and 3rd is repo using adapted case. now we have this
simulation where change in this adapted case use, which we: read,
judge , act, deliver, take. so what i thinking is to start from
defining that model to see what part we simulating. we can then
refer better and describe better. i thinking to do that first in sep
doc from "common-ground-problem" to write it first as sep and then
put that back. what u think?"

And at the session's end: "lets start from that model thing first.
then we decide what to with all this. lets finish this session with
task for next, for modeling in sep doc how we see those layers. then
we continue from there."

#### What the reviewer said, edited

"Also, this 'step by step' doesn't sound nice, but I think it must
first be changed in the Common Ground Problem. We should define
there what runs from the change to the take, as one thing."

"We should refine the Common Ground Problem, starting from §3, *The
Knowledge Axes*. We should define a three-layer model of knowledge,
like the idea model we had, if I remember right, when we had a
separate repo for it. The top layer is project-agnostic, the second
is the Adapted Case, and the third is a repo using the Adapted Case.
The simulation follows a change made where an Adapted Case is used:
read, judge, act, deliver, take. I want to define the model first,
to see which part we are simulating. Then we can refer to it and
describe it better. I want to write it first in a document separate
from the Common Ground Problem, then put it back. What do you think?"

"Let's start with the model first. Then we decide what to do with
all this. Let's end this session with the task for next time:
modeling, in a separate document, how we see those layers. Then we
continue from there."

#### What the reviewer asked, as the agent would ask it

1. Should what happens from a System Kit Copy Change to the take of the next System Kit Update be defined as one thing in the problem file, so the simulation can name it instead of saying "step by step"?
2. Should the problem file's §3 hold a model of three layers: project-agnostic text, the Adapted Case, and a repo using the Adapted Case?
3. Does the simulation then show which part of that model it covers?
4. Should the model be drafted in a separate document first, and then written back into the problem file?

#### What the agent added

- **The simulation is a Change moving between the layers:** it starts at the third, in a System Repo's Copy; Read and Judge carry it up; Deliver and Take bring the result down. The depths a to f may be how high a lesson goes: a stays at the third layer, b reaches the second, c to e reach the first.
- **Most pieces exist apart:** the two levels of understanding (§3.3, *The kind of text*); a System Repo's copy that "may adapt it further" (*Defined Terms*, Adapted Understanding Text); and the idea model (`temp/idea-model-problem.md` §1, *The model we try to build*), whose third level is the instructions, not a repo. In the reviewer's model, the kind of text stays an axis of its own, and each layer holds both kinds.
- **Two questions for the model:** whether the Maintainer Repo is a repo of the third layer, for its own Adapted Cases; and whether the model joins §3.3 and §3.4, or stands beside them.
- **A separate draft** carries a header saying it is a draft for the problem file's §3 and goes once written back, so it is never a second home.

#### What the reviewer took

The model is drafted in a document of its own, first in the next session, before `temp/`'s old files are decided. The TODO item holds it.

### 2026-11-14, later, and 2026-11-15

#### What the reviewer said

On drafting the model: "lets go and start modeling and leave all those question for answering after we draft that model. lets use that info we have not as final but as source to use to draft model. model could diff from what we though before. would it be better if model together with picturing that model. so we draw picture which is refered what we write? also if we change something in picture we check if what we write corresponds of how we picture?"

On the top layer: "when we say: "Project-agnostic ideas bound to no project: understanding", i think i wanted to say not project agnostic but domain agnostis. ... So i thinking i should have idea writen not related to domain. then that idea could be adapted to domain and then adapted domain idea is used to write adated case."

On how the layers fill: "can we say that this model layers are filled from lower level to upper? one of the case when new ideas is comming is from work we do, where find new things and change what we know. ... but this is not necessary how it will work and that it is final. it could happen that we may change that model or edit based what practice will show. this is now to orientate how we are planning to handle understanding."

On what the model is for: "i think we should build this model till that point where we could go back and rewrite our todays maintainer repo into that model. then using this model maintain understanding in relevance and correctnes."

On a Maintainer Kit: "now question is should we write such kit from which maintainer could be born? ... should we mark this when we will be designing or we should decide that now?" Then: "maybe in todo with refering that we have question here in model section of open questions?"

On the model's home: "question 7 could be answered now as this is idea undertanding text of layer 2 of maintainer domain. we will refer to it as one-home."

On a general model: "do we need domain agnostic layer model, that this repo could refere and explain that it is maintainer how maintains instance of that model?" Then, on the rule that blocked it: "i think it should reduce boundary, to "when a second domain needs it, or when we need to write domain agnostice description that it would not land in domain " or something similar , better formulated."

On a variant: "in my head we write this another variant for domain idea becuase of controling how we understand some complex idea, where that complex idea can have variants. ... i see it full and i not dependable when i make change to default case, so as when i touch default case i do not have to consider Slice variant of it."

On the next work: "i was thinking to go manualy each doc especialy common ground problem and check what ideas could be moved here, not necessary in exact text they write there. So basicaly i dont want to loose thinking we did before that fits this model we writing now."

#### What the reviewer said, edited

"Let's start modeling, and leave the questions until the model is drafted. Let's use what we have as sources, not as final; the model may differ from what we thought before. Would it be better to model and picture it together, so the text refers to the picture? And when the picture changes, we check that the text still matches it?"

"Where we say 'project-agnostic ideas, bound to no project', I meant domain-agnostic. An idea should be written with no domain in it. Then it is adapted to a domain, and the domain's idea is used to write an Adapted Case."

"Can we say the layers are filled from below? New ideas mostly come from the work we do, where we find new things and change what we know. This is not necessarily how it will work, nor final: practice may change the model. It is for now, to orient how we plan to handle understanding."

"We should build the model until we can rewrite today's Maintainer Repo into it, then use it to keep our understanding relevant and correct."

"Should we write a kit a Maintainer Repo could be born from? Should that be marked for when we design it, or decided now?" Then: "Maybe in TODO, pointing at the question in the model's open questions?"

"Question 7 can be answered now: this is the understanding text of layer 2, in the Maintainer domain. We refer to it as its one home."

"Do we need a domain-agnostic layer model, which this repo refers to, saying the Maintainer Repo maintains one instance of it?" Then: "The rule should be widened: when a second domain needs it, or when a domain-agnostic description would otherwise land in a domain. Something like that, better worded."

"I write a variant of a Domain Idea to control how a complex idea is understood, where that idea can have variants. I see the variant whole, and I don't depend on it when I change the default; when I change the default, I don't have to consider the slicing variant."

"I want to go through each document by hand, the Common Ground Problem first, and see which ideas can move here, not necessarily in their words. I don't want to lose the thinking we did before that fits this model."

#### What the reviewer asked, as the agent would ask it

1. Should the model be drafted with a picture, the text checked against the picture at every change?
2. Is the top layer domain-agnostic rather than project-agnostic, with a domain layer between it and the Adapted Cases?
3. Are the layers filled from below, by work, the model itself only an orientation that practice may change?
4. Is the model built only until today's Maintainer Repo can be rewritten into it?
5. Should a Maintainer Kit be decided now, or marked with its trigger; and can the question sit in the model while TODO holds its trigger?
6. Is this draft the model's one home, as the Maintainer domain's layer-2 text?
7. Should a domain-agnostic model be written apart, this draft its Maintainer instance; and should the fill rule allow a general text before a second domain needs it?
8. Is a Domain Idea Variant written whole, to understand a complex idea in one situation, each version changed alone?
9. Should the earlier drafts be gone through together, their fitting ideas moved into the model?

#### What the agent added

- **Today's drafts already hold layers 1 and 2 as text levels** (the problem file's §2.1 and §3.3), and the idea model's third level is instructions, not a repo; the reviewer's layer of a repo using an Adapted Case was new.
- **The simulation is one Change's movement through the layers,** and its depths a to f read as how high a Change goes; depth f had no layer until the domain layer gave it part of one.
- **The System Kit is not a layer** but what is copied to System Repos, drawn as a frame.
- **The Tiers Model and ADR-0038** argue against building a Maintainer Kit ahead of a second Maintainer Repo; `cbc-concept` is close to one.
- **`cbc-concept/ideas/`** already holds ten domain-agnostic ideas, among them the parts of a piece of work.
- **A variant's name carries Domain Idea whole,** by writing rule 9.

#### What the reviewer took

The model is drawn and written in `temp/common-ground/knowledge-layers.md`, its own home, and its general part in `temp/common-ground/knowledge-layers-general.md`, on trial; the fill rule is widened. A Domain Idea Variant is written whole. The Maintainer Kit stays an open question, with a TODO item for its trigger. The earlier drafts are gone through together, the problem file first, before `temp/`'s old files are decided.

### 2026-11-15, later

#### What the reviewer said

On a domain: "but i actualy think it is sort of work. when we have some work, like maintainer, we use domain agnostic idea to adapt to maintainer repo. when we have cbc backend design kit, we use those domain agnostic ideas to adapt to that domain. where is the problem to define what domain means?" Then, on its name: "craft sound weird. how else we could call, what maintainer repo work and system repo is doing? it seems that it is kind of Work Domain or what?"

On layer 1: "layer 1 not only about sharing. it is also information layer. this doc we write now is one of examples. we write general understanding here which we will not put in layer 2. also it could be used in another work domain which will need to write its work domain idea based on this but it is not only one reason or condition"

On how knowledge enters: "when we have idea in mind which needs to test, it could go first in understanding, like work domain or even Bound to no Work Domain . then based on that we write approahes. ... knowledge could enter at any place. if we already in some work domain, it could come idea for layer 1. during the writing we notice that we have some backbone of idea which we want o distinct and put in layer 1. it does nothing to do with reuse. so maybe layer 1 should be define not as share between work domains, but as backbone if idea in layer 2. it could happen that it will be writen only for one or even non of layer 2. i may want to put idea for understanding of something that no current work domain needs it, but we as context would use."

On a variant: "we should say that there could be idea's from layer 1 variants, so same idea from layer 1 could have multiple adaptations. maybe we should drop saying a  default. ... it is al theory, maybe we should sorten most of it and move to open questions"

On examples: "i dont want specific example, so it should sound not specific to any or remove at all."

On the picture: "should we place idea boxes in layer 1? should we put multiple with tags numers, that we could also refer those from layer 2? we could then domonstrat same idea 2 times , one 1 time or non (not included)." Then: "i want same picture. lets have a rows that picture would fit. lets make max 2 boxes in the row, with 2 rows"

#### What the reviewer said, edited

"I think a domain is a sort of work. Maintainer work adapts the domain-agnostic ideas to the Maintainer Repo; a CBC backend design kit adapts them to its own domain. Where is the problem in defining what a domain means?" Then: "'Craft' sounds odd. What do we call what the Maintainer Repo and a System Repo do? A kind of Work Domain?"

"Layer 1 is not only about sharing. It holds understanding too, and this document is an example: general understanding we will not put in layer 2. Another Work Domain may write its Work Domain Idea from it, but that is not the only reason or condition."

"An idea to test may go first into understanding, in a Work Domain or even bound to no Work Domain; then the approaches are written from it. Knowledge can enter anywhere. Inside a Work Domain, an idea for layer 1 may come up: while writing, we see a backbone we want to set apart in layer 1. That has nothing to do with reuse. So layer 1 is the backbone of an idea in layer 2, not what Work Domains share. It may be written for one Work Domain Idea, or for none: I may write an idea no current Work Domain needs, as context we use."

"One layer-1 idea can have several adaptations. Maybe drop the default. It is all theory: shorten most of it and move it to the open questions."

"No specific example: make it general, or remove it."

"Put idea boxes in layer 1, numbered, so layer 2 can refer to them, and show one idea adapted twice, one once, one not at all." Then: "Keep one picture. Fit it in rows of at most two boxes, two rows."

#### What the reviewer asked, as the agent would ask it

1. Is a domain a sort of work, so open question 1 is answered, and is its Name Work Domain?
2. Is layer 1 an idea's backbone, written for one Work Domain Idea, several or none, rather than what Work Domains share?
3. Can knowledge enter at any layer, a backbone set apart while a lower text is written?
4. Is a layer-1 idea adapted more than once in one Work Domain, with no default, the rest of the variant theory moved to the open questions?
5. Should the general document name no specific example?
6. Should the one picture show numbered layer-1 ideas, adapted twice, once and not at all, in rows of two?

#### What the agent added

- **"Domain" means a system's business in the backend Agent Skills** ("a domain class", "domain state" in `cbc-bootstrap`). Application Domain is the same meaning; Repo Domain names the repo, not the work, and many repos share one.
- **The fill rule stood three times,** in two words: "shares" in §3.1 and §3.2, "needs" or "true for every text below" in §3.1.
- **Setting a backbone apart is not a lesson from work,** so the picture had no arrow for it.
- **Understanding Idea does not tell layer 1 from layer 2:** a Work Domain Idea is understanding too.

#### What the reviewer took

Work Domain, a sort of work, its own paragraph in §2. Layer 1 holds Backbone Ideas, each standing under several Work Domain Ideas, one, or none; reuse is not why it is written. Knowledge enters at any layer; the arrow *set apart* joins *lesson* at both gaps going up; "on trial" and "writing from the top is rare" go. Layer 2 holds one kind, the Work Domain Idea, a Backbone Idea adapted once or more; the variant's theory moves to the open questions. The picture numbers three ideas, in rows of two. No example names a case.

### 2026-11-18, the Change idea

#### What the reviewer said

On where Change sits: "maybe lets try to have as section to see how it goes and if we want to have as sep doc"

On the order: "i think we should wait with maintainer change behavior. we now should relocate this change thing into knowledge layer. after we go to recheck change flow in system repo. then move that final version in knowldege layer. then we check and update "read to take" part and maybe draw too. after one side will be finished we would look at other. what u think?" Then: "is it true that we should first finish change flow and simulation before we do this Change section?"

On the pointers: "current simulation is pointing to those parts. will those pointers move now into knowledge layer?" Then: "does current simulation and change-flow needs updates accordingly knowledge layers?"

On the old word: "why we not renaming it? doesnt we now have layers?" Then: "is that true that we should update judge and act? because before we did not considered this layer stuff?"

On the next session: "i am thinking to stop this commit plan and write for next session: start from updating simulation by new layers we have defined. After update and finish chnage flow. then decide where we put change. then update everything where each has one-home and we do not repeat one thing everythere. what u think?"

#### What the reviewer said, edited

"Let's try it as a section first, to see how it goes, and whether we want it as a separate document."

"I think we should wait with the Maintainer Repo's own changes. First move the Change rules into the layers document. Then recheck the change flow in the System Repo, and move the final version into the layers document. Then check and update Read to Take, and maybe draw it. Once one side is finished, we look at the other. What do you think?" Then: "Is it true that we should first finish the change flow and the simulation before we write this Change section?"

"The simulation points at those parts. Will its pointers now move to the layers document?" Then: "Do the simulation and the change flow need updates for the layers model?"

"Why aren't we renaming it? Don't we have layers now?" Then: "Is it true that Judge and Act need updating, because they were written before the layers?"

"I'm thinking of stopping this commit plan and writing down for next session: start by updating the simulation to the layers we defined; then finish the change flow; then decide where Change goes; then update everything so each fact has one home and nothing is repeated everywhere. What do you think?"

#### What the reviewer asked, as the agent would ask it

1. Should the Change idea start as a section of the layers document, on trial, and become a document of its own only if practice shows it should?
2. Should the Maintainer Repo's own changes wait until the System Repo's side is finished?
3. Must the rules be finished and checked before they move to their home, or can they move first?
4. Do the simulation's pointers follow the rules when they move?
5. Do the simulation and the flow drawing need updates for the layers model?
6. Why keep the old word "project-agnostic" when the layers model replaced it?
7. Do Judge and Act need rework, since they were written before the layers?
8. Should the commit plan stop, and the next session work in four steps: the simulation brought up to the layers, the change flow finished, where Change goes decided, then one home for each fact?

#### What the agent added

- **The general document's §2.2 rule** says each adaptation is "written whole, read alone, and changed alone". A Change idea in a document of its own would stand on the layers document's repo terms. So the rule would first have to be narrowed to variants, the case it came from.
- **Nothing forces the move to wait,** and nothing is fixed twice: a fix moves with its text. But the rules are checked against one case only. Moving them once, finished, keeps unchecked rules out of the layers document.
- **The simulation's 15 pointers** at the problem file's §2.1 all aim at parts that move. The flow drawing has none.
- **Four kinds of update** in the simulation: the old word on 14 lines, depth f, the on-trial row that is not a Change, and Judge and Act knowing one level above an Adapted Case.
- **"Project-agnostic lesson" names a verdict,** on 6 lines across two files. Its home is a bold lead, which the agent first called a title. With two layers above, the verdict may split in two, so renaming it before the rework would change those lines twice.
- **The TODO item's claim was wrong:** it said the simulation's §7 sends only the changes. §7 sends every Copy whole.

#### What the reviewer took

The Change idea adapts "The layers of knowledge", in keeping knowledge. Its subject is a change crossing between the repos, written from one source so far. Where it goes was drafted as a section of the layers document, then held until the rules are finished. The commit plan for the simulation was dropped before its first commit. The next session works in four steps: the simulation brought up to the layers model, Judge and Act included; the change flow finished, Change to Take; where Change goes decided; one home for each fact across the drafts.

### 2026-11-19, step 1 and the three places

#### What the reviewer said

On the guesses: "yes, 4a then 4b, but we should keep in mind that this is just a guess and real practice should show how to correct those guesses later. so should we now define that or would it be better if we leave that as open questions? or maybe we could have both, define some how simpler and general and have as guesses open questions, that practice was not influanced by guess?"

On the three places: "yes, commit it, then explain. Do we have today in multile places a Change? i see it repeating in knowledge layers, common ground problem and simulation. am i missing something? should we move everything in one place and just refer that one place from others? for example move to simulation till we finish with that and relocate in final (no simulation place) or change simulation into final place of change? should we first finish this commit plan and do that as next?"

On the order: "yes, stage commit 5 with the new order"

The other decisions, each on the agent's recommendation: "yes, depths are layers, c split in two"; "yes, apply that split, next question"; "yes, agree with that split, next question", three times; "yes, agree with these names, next question"; "yes, agree with this scope, next question"; "yes, commit the revision, keep the label".

#### What the reviewer said, edited

"Yes, 4a then 4b. But we should keep in mind that this is just a guess, and real practice should show how to correct those guesses later. So should we define it now, or would it be better to leave it as open questions? Or could we have both: define something simpler and general, and keep the guesses as open questions, so that practice is not influenced by a guess?"

"Yes, commit it, then explain. Do we have Change in several places today? I see it repeating in the layers document, the Common Ground Problem and the simulation. Am I missing something? Should we move everything into one place and just point at that place from the others? For example, move it into the simulation until we finish it, then relocate it to its final place, with no simulation left; or turn the simulation into Change's final place? Should we first finish this commit plan and do that next?"

"Yes, stage commit 5 with the new order."

The other decisions keep their words; each is a "yes" to the agent's recommendation.

#### What the reviewer asked, as the agent would ask it

1. Should a guess, such as the order of 4a and 4b, be written as a rule, left as an open question, or both: a simple, general rule, and the guess open, so practice is not steered by it?
2. Is Change written in more than one place: the layers document, the problem file and the simulation?
3. Should it move to one place, the others pointing there: into the simulation until it is done, then to the final home; or should the simulation become the final home?
4. Should this commit plan finish first, and the move come next?

#### What the agent added

- **Nine decisions, one at a time:** the on-trial row out; depths are layers, c split in two; question 4 as 4a and 4b; the split of defined and Open; the survey, depth d and depth e by that split; names by layer; the scope, three files.
- **The split's test:** what follows from a rule already written, in the general document, is defined, by pointer; a choice of how is an Open item with its trigger. Depths are layers stays defined, since it rests on "a lesson goes as high as it is true".
- **Depth f, found while reading:** a Work Domain Idea stands above every Adapted Case of its Work Domain, so "all of one Work Domain" is depth c, at layer 2. Two cases are left with no home.
- **Decision 8's list named f's column phrase as its label.** The label was kept, and the phrase went to its column.
- **The three places are three roles, overlapping:** the simulation's workings, the problem file's rules, the layers document's summary. Four kinds of fact stand in two places each: the depth table, the six parts, the rules, the movements between repos. One change of meaning took three commits.
- **A third way:** the rules moved once, now, to the final home drafted on 2026-11-18, on trial, the simulation pointing there. The simulation as the final home would keep its options and its *Today* lines, which are workings.
- **The order:** the change flow edits every part again, so where Change goes is decided before it.

#### What the reviewer took

Depths are layers, c split in two; question 4 as 4a and 4b. What follows from a rule already written is defined, by pointer; each choice of how is an Open item with its trigger, so practice is not steered by a guess. The survey, depth d and depth e follow that split; verdicts are named by layer; the work reaches three files. Depth f keeps its label. This commit plan finishes first. Where Change goes is decided next, before the change flow; which of the three ways is open.

## 36. Guesses set aside for practice

Item: "Set aside a project's own Changes and Attention Notes in
`temp/common-ground/system-repo-change-simulation.md`, until practice
meets them".

### 2026-11-20

#### What the reviewer said

While case D2 was drawn, and the Take's putting back needed a new
rule: "what u think if we now make this put back changes that is project related back  and just draw all cases where we take only Chnage thats pure. because now it feels overwhelming to think all at once?"

Then, on case D1: "can we do now same thing with Attention Note as we did with personal chages? put them in todo for later to reconcider ?"

Then, told the simulation still held both: "i think we should set aside those in simulatio and here is why. first it just a guess and we already strugle to define what could happen. i think i need facing that in practice not guess. we should mark that as we aware that could happen. now taking everything into account just make this too complex and we cant finish. also we i think in simulation, that case we took should have those, doesnt it? so we wrote rules upfront simulation it self, doesnt it?"

#### What the reviewer said, edited

"What do you think if we now put back the changes that are project-related, and just draw all the cases where we take only Changes that are pure? Right now it feels overwhelming to think about everything at once."

"Can we now do the same with Attention Notes as we did with personal Changes, and put them in TODO to reconsider later?"

"I think we should set those aside in the simulation too, and here is why. First, it is just a guess, and we already struggle to define what could happen. I need to face that in practice, not guess. We should mark that we are aware it could happen. Taking everything into account just makes this too complex, and we can't finish. Also, in the simulation, the case we took should have those, shouldn't it? So we wrote rules up front in the simulation itself, didn't we?"

#### What the reviewer asked, as the agent would ask it

1. Should the pictures draw only pure Changes, those taken into the System Kit, and leave a project's own Changes for later?
2. Should Attention Notes wait in TODO the same way?
3. Should the simulation set both aside too, as guesses to meet in practice, with a mark that they can happen?
4. Is a project's own Change the simulated case itself, and were rules written ahead of what happened?

#### What the agent added

- **Pure, defined:** every Change is taken into the System Kit, so nothing stays in the System Repo's Copies and nothing is put back at the Take.
- **Case D1 has no pure example:** with pure Changes only, every Reading ends with something to send, a new Version or a verdict that goes down, so it is D2.
- **The simulated case is depth a,** a project's own Change: §5 to §8 are written for it. The Attention Notes came from outside the case, in §3, to carry what no Change carries: rules written ahead of anything that happened.
- **The size:** most of §3 to §8, about 35 places by a rough count, so a commit plan, next session.

#### What the reviewer took

Both are set aside in the simulation, not only in the pictures, until practice meets them. The simulated case becomes depth b, the Change taken into the System Kit; their rules leave §3 to §8, and git keeps them; §2 keeps a short list of what is known and not ruled, each with its trigger. The work waits for the next session, a commit plan first.

### 2026-11-20, later

#### What the reviewer said

Before the decisions: "so before we continue, can u tell me back again what currently those attention notes and specific changes solves and where? are they connected or are sep things? how much complexity we drop if remove them now? would it be better to leave them and draw pictures from them separatly and have those other pictures when take case is pure?"

Then: "set them aside as planned. what we need to decide now?"

On the look past main: "wait a second, doesnt we read only main? where this comes from?"

On the Take's gate: "yes, take a and keep branch thing too"

#### What the reviewer said, edited

"Before we continue, can you tell me again what those Attention Notes and specific Changes currently solve, and where? Are they connected, or separate things? How much complexity do we drop if we remove them now? Would it be better to leave them, draw pictures of them separately, and have the other pictures for when the Take's case is pure?"

"Set them aside as planned. What do we need to decide now?"

"Wait a second, don't we read only main? Where does this come from?"

"Yes, take a, and keep the branch thing too."

#### What the reviewer asked, as the agent would ask it

1. What does each solve, and where in the simulation?
2. Are they one thing or two?
3. How much does setting them aside remove?
4. Would keeping them, drawn apart from the pure pictures, be better?
5. What must be decided before the work?
6. A Reading reads only main: where does a look past main come from?

#### What the agent showed

- **Attention Notes** carry what no Change carries: a misfit worked around, a doubt about a line, a lack, a Copy no longer used. 24 lines, in §2, §3, §4, §7 and §8.
- **A project's own Change** lets a System Repo keep a Change that fits only it, which today forbids. About 36 lines, by grep, of the simulation's 527 non-empty: the simulated case, question 2, and the Take's putting back and its gate.
- **Two things,** meeting in one line, §8's item 5.
- **What setting them aside drops:** the Take's putting back, the gate's main job, and judging a put-back Change again at each Take. **What it costs:** §5 to §8 re-simulated for depth b.
- **Three ways:** set aside as planned; keep them and draw them apart; keep them, each marked set aside where it stands. Kept, the next step, which checks the rules by drawing them, meets them again.
- **The look past main** came in `5dd275c`, 2026-11-11, in the same paragraph as the rule that a Reading reads only main, as an exception. Nothing that happened asked for it.

#### Options weighed, with the agent's suggestions

1. **A Change the System Kit does not take:** judged its own, unsound, misread or held. With nothing put back, the Take's whole Copies replace it. Suggested: Judge keeps every verdict; the simulation follows only Changes the System Kit takes; §2's list names this one with its trigger, the first such verdict; the Take's rules say nothing of putting back.
2. **The look past main:** first suggested as set aside, with a list entry. Once the reviewer asked where it came from: removed outright, since it is a tool someone might want, not something that can happen.
3. **The Take's gate,** with nothing put back to decide: a, keep the branch and the gate, the gate checking that the Take finished; b, drop both, the Take on main, Read's rule given an exception. Suggested: a; whether the Take still needs its branch noted, not acted on.
4. **Pictures 1 and 2,** due to go by their own item: a, remove them first, in this work; b, fix them, then remove them. Suggested: a.

#### What the reviewer took

Set aside as planned, and all four as suggested: the look past main removed outright; for the gate, a, and the branch question kept, as an open point in the simulation's §8.
