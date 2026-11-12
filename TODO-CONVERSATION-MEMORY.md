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

     Last touched: 2026-11-12.
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

## 31. Keeping what we know true

Item: "Write the problem of keeping what we know true, in the reviewer's words".

### 2026-11-05

#### What the reviewer said

Asked whether to build approaches on the one-change drawing, the
reviewer stepped back: "i actualy thinking if we not overengineered
our model of that layer system. i am thinking, maybe i should try to
start over." Then the problem, in full, for the first time:

"main purpose is to find how to maintain what we learned and know.
by we i mean what i know and u are on same page. you know everything
and i learn something, write something. now that i dont have to
retell you in new session u read that from what i know, so we are on
same page and continue improving from there."

Two problems: "when we have skill writen, idea behind is missing.
the bigger problem is when we work we keep moving forward. everything
what was writen before is out of date, so they most likely incorrect,
contradictional, missing something or anyway different."

On one home per fact: "it became to costly to maintain. maybe it is
still good way of maintain, but needs improvememtn." A refresh is one
agent running through the whole repo. In the best case, one spot is
fixed and the whole is true again. In the worse cases, a change in a
referring part forces the home to change; then every other reference
is checked; if they disagree, back to the home, and so on: "this
becomes not one iteration problem where decition needs to be taken
based different spots." And when references start to disagree with
each other, "that multiplies".

On the rebuild: "we started from top layer, which is most general as
idea and its graph. that part is not asociated to any project, so we
try to find general idea again without real world. so what i think
is we should start from real world and then go up. actualy we should
find if we need that at all." Layering v1 and v2 were a good find,
not to be dropped; "whats really help to understand is
visualization."

The way: freeze `cbc-concept`, come back here, and state the
problem anew. "if that our repo knowledge and approaches effects and
influance too much on answers we should create new fresh repo and
start over, but differently this time from buttom to up".

#### What exists today

- `temp/idea-model-problem.md`, 2026-11-02, holds most of it: the
  loop between a home and its references (§5), with this repo's
  numbers, 398 section references pointing at 129 sections; the
  Agent Skill without its why (§2); 9 musts, each with a check (§3).
- What it lacks: the purpose, the two sides on the same page; the
  bottom-up direction, since it takes the three levels as given; and
  references disagreeing with each other, not only with the home.
- ADR-0081 had set the rebuild to stand on its own first, and to take
  a rule only when its work needs it (its decisions 3 and 4). The
  rebuild wrote 10 ideas and 1 Work Approach in 3 days.

#### What the agent added

- **The real world is on record:** 18 "What context was missing"
  lines in the devlog since October, and the refinement's findings,
  485 in round 3's close read and 385 in its last read. A sample
  sorted by cause shows where staleness comes from.
- **Not everything must stay true:** history cannot go stale; what
  the agent acts on must be true now. The smaller that set, the less
  to keep.
- **Check at use, not by sweep:** the loop comes from a sweep; a
  text checked when it is about to be used bounds each fix to the
  work in hand. An option, not weighed.
- **The bias, named in advance:** this repo loads one home and the
  Foundation Check in every session. Signs a fresh repo is needed:
  the problem cannot be stated without this repo's Glossary Names,
  or every option is a variant of one home. Not yet agreed.

#### What the reviewer took

The playback was right. `cbc-concept` frozen, its README telling
what it was, when it was born, what was done and where it stopped.
The rebuild's Plan Step closes. Then, in order, each deleted once
done: write the problem, read the real-world record, take the first
real case. "we change that order when needed, that is when something
changes."

### 2026-11-05, later

#### What the reviewer said

On closing the rebuild: "maybe we should stop instead of drop till
we see if we dont want to go back? i think after we work on next
step we will see if there i a reason to go back again?"

On the signs of bias the agent proposed: "Again explain simple what
we are doing here? because i think we are not on same page." Then:
"we now gonna describe problem before we try to find solution. our
repo using one approach which is build without full consideration
"one-home" and "references". it may be incorrect or not complete."

On the problem's first line: "this "You learn something and write it
down" in "## 1. The purpose" is actually a knowledge. Knowledge is
what i know and how i understand something. Knowledge is stored/put
in texts."

On the same page: "those text is interface between my mind and u."
"Knowledge text for u and me means little different things. for me
is to put some ideas how i see something, how i understand that,
where i am [...] this does not mean that it is correct. also idea
knowledge could be at different understanding levels [...] Also i
use it something as to recall." For the agent: "it does not mean
what u know. it means u know at what understanding level i am. you
know more about it. [...] u use that text to help me to work on that
idea. by work we mean multiple things: use that idea for
application, learn more about that idea, maintain that idea and any
other thing we can do about it."

On names: ""you" and "me" words can become misleading, because in
text at some point each could me both." On the two uses: "These
sound as bounded list. should we make it open for extension?"

On time: "knowledge can also be: what we knew before, what we know
now, and what we have in mind to learn later. Also it can be said
as: what I thought before, what i think it is now and what i think
we should check about it later." Agent Skills and rules wait: "this
is another axis to problem we facing and it is something we should
talk separatly later."

On the draft so far: "it seems that this text is too lean. do we
capture all this thinking we do now? does this text delivers same
knowldege what we have in this session now, if someone would read it
in new session?"

#### What the agent added

- **The same page was wrong as first written:** the agent knows more
  of the subject than the text; what must match is its picture of
  the human's understanding, and its level.
- **Nine cases where the interface breaks,** from thinking it
  through; two seen that day: the rebuild's purpose written nowhere
  for 3 days, and the agent's dense answers.
- **One drift, three places:** text holding less than the knowledge,
  or older than it; lost at writing, in time, or at reading.
- **Stale is a wrong time:** a text still reading as now after the
  knowledge moved on. History cannot go stale this way.
- **The moves between times lose knowledge;** before keeps why it
  changed; now has degrees of certainty.
- **The draft was its own case 9:** it held the what, not the why,
  until the missing points went in.
- **The signs of bias set in advance** were a check built ahead.

#### What the reviewer took

The rebuild stopped, not closed, and "Find how what we know stays
true" opened with three stages; stage 3 kept. No signs of bias set
in advance: either side says so when it is felt. The problem is
drafted in `temp/knowledge-problem.md` and polished one insight at a
time, each a commit, so the diffs show what changed: knowledge and
text; the text as the interface; the human and the agent, named and
defined; the two uses as open lists; the time axis; each axis a
section; and the agent's five missing points.

### 2026-11-06 and 2026-11-07

#### What the reviewer said

On words with two meanings: "i also noticed that we vary commonly
overload words. should we mark this as todo later for writing rule
to consider and pay attention?" On local names, the agent's reading
of them across documents: "what happens when agent will read more
then one doc with such rule, where in one doc it list its words and
in other theirs. now will agent dont mix that in his context?"

On the middle level: "this middle level, or as i just though as
understandings lower lever which is part of understanding and
adapted to project needs [...] brings as extra understanding
maintanace. complexity grow [...] Now how that helps. we can have
some understand writen without dependency on any specific project
[...] so maybe while i try to put everything what i understand i
find reason why middle level is required and not optional?"

On definitions at the start: "we should have definitions of those
words in the beggining. maybe we should mark them or have label or
note as this is defined in begining. [...] in books we have this
start '*' i think and footer". Later: "i wanted, that when it appears
first time in doc, we would mark it something like '*' [...] but
term list i would like to be order alphabeticaly".

On the intent against today: "we write more like we pretending if
it is done this intendent way, where in reallity it may need to
make changes. So maybe here we should also write our own naming and
talk about cbc runs as what we think they are, where after we gonna
clarify if they really are." And: "maybe we could start by naming
our current `deliver` in better way."

On the CBC part, held for later: "now i think i understood why u were
suggesting before to include CBC in name for our repo [...] Just
keep in mind that i have idea why this is true which i will describe
later as another insight."

On refining a document with many agents: "can we have such thing
like document refinement, where we start it by one agent and giving
him rule where it can start his agents, where each agent is
responsible about one idea in that doc. [...] when one agent does,
that it kind of feels that it reasons on snapshot of document. i
want that it was check according what document is stating. so there
could be multiple ideas and snapshot can take change for one place
but break other."

#### What the agent added

- **Local names bleed** between documents the agent reads together;
  narrowed lowercase words most, unique capitalized Terms least.
- **The middle level pays by demand,** only for an idea two projects
  with different needs share; the trade-off kept as an option.
- **The repo already has words for some of it:** Concept Deliverer,
  Glossary Name, Canonical Description, the last with two scopes.
- **A third sort of instruction,** an Agent Rule loaded by path.
- **First-use marks** weighed: a mark goes stale when an earlier use
  is added, and breaks plain searches.
- **For many agents,** one core agent edits; checkers report, split
  by rule rather than by idea, until a pass finds nothing new.

#### What the reviewer took

Words with two meanings swept, and the writing rules found gathered
in one TODO item, to land once the repo is fixed. The middle level
kept, with its two failures and its trade-off as an option. Defined
Terms at the start, sorted alphabetically, with no mark at first use
and no opening line about capitals. The intent in the draft's own
Terms, today in the repo's names, in §2.2 and its table: Maintainer
Repo, System Repo, System Kit, System Kit Copy, Task, Session and
File Instruction Text, Knowledge on Trial. Neutral Terms kept until
the CBC insight is written. The document named the Common Ground
Problem. The multi-agent refinement noted in TODO, to try in place
of the draft's fourth fresh read.

### 2026-11-08 and 2026-11-09

#### What the reviewer said

- **Our own adapted level:** "Now that means that each repo has its
  adapted need understanding, so ours should too as maintainer repo.
  That means we need to write adapted understing to us too which we
  not even mention and i think were awere." Then: "so then that
  means we should have `maintainer repo adapted understanding <-
  general understanding -> system kit understanfing`". And: "we need
  to decide if these adapted understandings could/should be
  delivered together with instructions. maybe we should do exact as
  we do with cbc understanding where we are judge? or maybe it is
  redudntant text for system repo?"
- **The picture:** "system-repo responsibility is: - maintain
  understanding of target problem which is in cbc system design
  domain - maintain adapted understanding and its instructions
  (agent work + cbc design + infra)". On infra: "what i think that
  it is just bigger set of input and not complexity, what u think?"
- **What the general text answers to:** "or we think about
  differently as general understanding should be project agnostic.
  so no matter if something in any adapted understand is no more
  true. it only if we think it has to be as general understanding
  lesson, like new thing or change of old one." And: "we could have
  as option to run survey in adapted understanding about this new
  formulated lesson where each tells its insigh in somekind of way.
  so i would have more info for decition."
- **Updates:** "now when i have few system repos, i could check all
  and send updated notes. what happens if there is alot? [...] i
  will be working on one project at one time. maybe i could request
  updates while i am on project only?" And: "i think here we will
  need that starter kit could be different by bytes from starter
  kit copy." And: "should we mark that each repo that has to have
  adapted understandig with instrcutions on how it will be taking
  updates?"
- **The word general:** "should we have some like shared-system-kit
  and shared-understanding instead of general? did i used general
  incorrectly?" And: "would u understand me if i sometime will say
  general by mistake?"
- **Lessons:** "should we have this as "Project-Agnostic Lesson"
  term"; "isnt this lesson for System kit?"; "so maybe we have Repo
  Lesson, which gives Project-Agnostic Understanding Lesson and
  Adaptive Understanding Lesson?" Then: "Judged Lesson would fit
  better if we need direct. Understanding Lesson could mean any
  direction as shared/general leson for any case direction, in and
  out and any future needs maybe?"
- **Instructions and their understanding:** "my guess was that we
  not aware that instrcutions are tight to adapted understanding and
  when we touch adapted understanding we should do that together
  with instrcutions. or not?"
- **Blindness, and a simulation:** "system repo can and have clues
  in his records what have change and what to check, but system repo
  has not address for maintainer. it has to stay blind from it. now
  this is decided. maybe we should decide how updated goes back,
  before we start making scenarios on how we read lessons?" Then:
  "i think it should be like simulation, where we start from step
  one, consider whats happening, then include parts we see is needed
  to mark and go to next step." On the example: "is there difference
  if change in system repo is done on copy we have delivered vs
  changes as new things by knowledge was introduces vs
  knowledge-on-trail as provisional was delivered and some changes
  was do to it?" On checks: "should we have those scenarios as
  checks, when something is done later not by scenario will be alert
  that we need to change or introduce scenario and recheck this
  maintanace system if that still holds?"

#### What the reviewer said, edited

The same words, with grammar and spelling fixed, the meaning kept:

- **Our own adapted level:** "That means each repo has its own
  adapted understanding, so ours should too, as the Maintainer Repo.
  We need to write an adapted understanding for ourselves too, which
  we don't even mention, and I think we weren't aware of it." Then:
  "So we should have `Maintainer Repo adapted understanding ←
  general understanding → System Kit understanding`." And: "We need
  to decide whether these adapted understandings could or should be
  delivered together with the instructions. Maybe we should do
  exactly as we do with the CBC understanding, where we are the
  judge? Or is it redundant text for a System Repo?"
- **The picture:** "A System Repo's responsibility is to maintain
  the understanding of its target problem, which is in the CBC
  system design domain, and to maintain the adapted understanding
  and its instructions (agent work, CBC design and infra)." On
  infra: "I think it is just a bigger set of input, not more
  complexity. What do you think?"
- **What the general text answers to:** "Or we think of it
  differently: general understanding should be project-agnostic. So
  it doesn't matter whether something in an adapted understanding is
  no longer true. It changes only if we think the lesson belongs in
  the general understanding, as something new or a change to
  something old." And: "We could have, as an option, a survey of the
  adapted understandings about the newly worded lesson, where each
  gives its view in some way. Then I would have more to decide on."
- **Updates:** "Now that I have a few System Repos, I could check
  them all and send update notes. What happens if there are many?
  [...] I will be working on one project at a time. Maybe I could
  request updates only while I am on a project?" And: "I think we
  will need the System Kit to be able to differ, byte for byte, from
  a System Kit Copy." And: "Should we say that each repo needs an
  adapted understanding, with instructions, for how it takes
  updates?"
- **The word general:** "Should we have something like a shared
  System Kit and shared understanding instead of general? Did I use
  general incorrectly?" And: "Would you understand me if I sometimes
  said general by mistake?"
- **Lessons:** "Should this be a Term, Project-Agnostic Lesson?";
  "Isn't this a lesson for the System Kit?"; "So maybe we have a
  Repo Lesson, which gives a Project-Agnostic Understanding Lesson
  and an Adapted Understanding Lesson?" Then: "Judged Lesson would
  fit better if we need a direction. Understanding Lesson could mean
  any direction, a lesson for any case, in and out, and maybe any
  future needs?"
- **Instructions and their understanding:** "My guess was that we
  weren't aware that instructions are tied to their adapted
  understanding, and that when we touch the adapted understanding,
  we should touch the instructions with it. Or not?"
- **Blindness, and a simulation:** "A System Repo can have, and has,
  clues in its records about what changed and what to check, but it
  has no address for the Maintainer Repo. It has to stay blind to
  it. This is decided. Maybe we should decide how updates go back
  before we start making scenarios for how we read lessons?" Then:
  "I think it should be like a simulation: we start from step one,
  consider what happens, add the parts we see need marking, and go
  to the next step." On the example: "Is there a difference between
  a System Repo changing a copy we delivered, adding new things as
  new knowledge, and changing Knowledge on Trial we delivered as
  provisional?" On checks: "Should the scenarios be checks, so that
  when something is later done outside any scenario, an alert says
  we need to change or add a scenario and recheck that this
  maintenance system still holds?"

#### What the reviewer asked, as the agent would ask it

The questions the reviewer was asking, put by the agent:

1. Does the Maintainer Repo need its own adapted understanding of
   agent work, and should the System Kit's adapted understanding go
   to System Repos with the instructions, judged by us when they
   change it?
2. Is a new group of understanding, such as infra, only more of the
   same shape, or does it add complexity?
3. Is the general understanding what all adapted cases agree on, or
   is it bound to no project, with each adapted case's view only
   input to the decision?
4. How do updates reach System Repos when there are many, and must
   each System Repo have its own instructions for taking them?
5. Is "general" the right word, or is "shared" what was meant?
6. Should a lesson have a Defined Term, named by where it lands, and
   should that name carry a direction?
7. When an adapted understanding changes, must its instructions
   change with it?
8. Should the update direction be settled before the reading
   direction is simulated, and should the simulation's scenarios
   become checks that fire when work falls outside them?

#### What the agent added

- **The draft had a hole:** our instructions built straight from
  the understanding of agent work, the middle skipped.
- **Judging has outcomes on two questions:** how far a change
  reaches, and what it says about the general text. Four questions
  in order, cheapest first, and a misreading among the outcomes.
- **Reading back before updating:** an update first could erase a
  System Repo's unread changes; an update merges, never overwrites.
- **The update instructions update themselves:** taken first, or an
  update is taken by instructions older than it (Failure Case 10).
- **General and shared differ:** the System Kit's adapted case is
  shared, not general; a general idea may be used by no repo yet.
  "Shared" for the general text would bring view 1 back.
- **What arrives is not a lesson yet:** two of the four questions
  end with none. "Judged" carries no direction, since both
  directions are judged; direction belongs to the movement.
- **An instruction and its adapted case are checked together,** not
  always changed together; a change to either can end in an
  Understanding Lesson.
- **Today's exchange already answers most of the update:** blind, a
  Delivery Take that re-applies held edits, a Delivery Pin. Two
  differences from the intent: who judges an update, and when one
  happens.
- **For the simulation:** birth first; a second pass of the cycle;
  the reviewer as an actor; what must be written before a session
  ends; the agent marks what it borrows from today's exchange.

#### What the reviewer took

Decisions 1 to 5, in the draft (`917b05d`): view 2, the general
text bound to no project and a survey as input, never a veto; a
lesson reworded to name no project, its first wording kept; the
survey's three answers; the four questions; updates when work
resumes, open in their how. Each sort of repo takes a change by its
own adapted case. "General" renamed Project-Agnostic Understanding
Text (`ecd311e`); the System Kit defined as shared (`5a9b22a`).
Understanding Lesson as the Term, with no direction, not yet
written. Today's blindness stands. Next, a simulation of what passes
between the repos, in eight scenarios: birth, work in a System
Repo, reading it, judging, the flow down, updating it, a lesson
from our own work, new knowledge from the reviewer. One main
example, a delivered copy edited, with the other kinds of change as
variants. Scenarios as checks: how the alert fires is decided once
the simulation is done.

### 2026-11-09 and 2026-11-10

#### What the reviewer said

- **The carrying:** "should we say "The human carries the files
  across" or "human ask agent to carry" or "we have instruction how
  to carry out, which is followed by human or agent by human
  premision" or something?"
- **The understanding goes:** "yes, adapted understanding goes with
  its instructions".
- **A change from today:** "should we note a requared change next
  to it?" And: "what this means "Today the explanation stays home."
  in "**Decides:**"?"
- **Copies stay their own, and a Name:** "should we mention or even
  decide now, that we thinking that adapted understanding +
  instruction can diff from system kit even after reading and
  update, because in maintainer we keep shared one and in system
  repo we have edited/adapted to problem needs? also i see the need
  to have term for adapted understanding + instruction, what u
  think? we had in current system use approach, we could also use
  that, but we different term from todays maintainer. what could u
  suggest?"
- **Work Approach:** "we use "Work Approach" for skill intruction?
  it is already Agent Skill, doesnt it? where it is defined?" Then:
  "do we need a word in intent for "Work Approach"? does it really
  mean something like "Instruction Kind"? do u see better name?"
- **The sweep:** "so we go with "Adapted Case"? also should we
  update "common-ground-problem" and change to "Adapted Case" where
  we are saying instruction text with its adapted understandig?"
- **The concept in the System Kit:** "We will need only concept as
  project documentation for description. So maybe just paragraph in
  README is enough or maybe we want more detailed description? then
  should that description like in System Kit already to deliver and
  reused? both? is this what this word means? should we have a term
  that descirbes all this?" And: "should we have in one place listed
  what system kit consists for better maintenance and refer where we
  need that as one-home rule?"
- **Adapted, twice over:** "i mean we use project-agnostic
  understanding to write adapted case, but when we say "2. CBC
  system design, adapted to one kind of system:" it feels strange,
  doesnt it? am i missing something?" Then: "also should we use word
  norrowed instead of adapted?"
- **Retelling:** "doesnt this retell too much? should we just refer
  what kit contains when its delivered? also why not make *What the
  System Kit holds* as section?" And: "wait a minute. shoulding we
  refernce what system kit holds instead?"
- **A birth:** "should we have here adapted case for birth? and in
  that adapted case instruction or as sep script which human alone
  could use?"

#### What the reviewer said, edited

The same words, with grammar and spelling fixed, the meaning kept:

- **The carrying:** "Should we say "The human carries the files
  across", or "the human asks the agent to carry them", or "we have
  instructions for how to carry them, followed by the human, or by
  the agent with the human's permission", or something else?"
- **The understanding goes:** "Yes, the adapted understanding goes
  with its instructions."
- **A change from today:** "Should we note the required change
  next to it?" And: "What does "Today the explanation stays home."
  mean in "Decides"?"
- **Copies stay their own, and a Name:** "Should we mention, or even
  decide now, that an adapted understanding with its instructions
  can differ from the System Kit even after reading back and an
  update, because the Maintainer Repo keeps the shared one and the
  System Repo keeps one edited to its problem's needs? I also see
  the need for a term for an adapted understanding with its
  instructions; what do you think? Today we use "approach", and we
  could use that too, but we use different terms from today's
  Maintainer Repo. What would you suggest?"
- **Work Approach:** "Do we use "Work Approach" for an Agent
  Skill's instructions? Isn't that already an Agent Skill? Where is
  it defined?" Then: "Do we need a word in the intent for "Work
  Approach"? Does it really mean something like "Instruction Kind"?
  Do you see a better name?"
- **The sweep:** "So we go with "Adapted Case"? And should we update
  the Common Ground Problem to say "Adapted Case" where it says an
  Instruction Text with its adapted understanding?"
- **The concept in the System Kit:** "We need the concept only as
  project documentation, a description. Is a paragraph in a README
  enough, or do we want a more detailed description? Should that
  description already be in the System Kit, delivered and reused?
  Both? Is that what this word means? Should we have a term for all
  this?" And: "Should the System Kit's contents be listed in one
  place, for easier upkeep, and referred to wherever they are needed,
  by the one-home rule?"
- **Adapted, twice over:** "We use the project-agnostic
  understanding to write an Adapted Case, but "2. CBC system design,
  adapted to one kind of system" feels strange, doesn't it? Am I
  missing something?" Then: "Should we use the word "narrowed"
  instead of "adapted"?"
- **Retelling:** "Doesn't this retell too much? Should we just refer
  to what the System Kit holds when it is delivered? And why not make
  *What the System Kit holds* a section?" And: "Wait a minute.
  Shouldn't we refer to *What the System Kit holds* instead?"
- **A birth:** "Should a birth have its own Adapted Case here? And in
  that Adapted Case, should the steps be an instruction, or a
  separate script the human could run alone?"

#### What the reviewer asked, as the agent would ask it

The questions the reviewer was asking, put by the agent:

1. What must hold when files cross between the repos: who carries
   them, or that nothing crosses without the human's word?
2. Where does a step say how it differs from today's exchange, so
   that today's facts are not read as the intent's?
3. Does a System Repo's copy stay its own after reading back and an
   update, for both halves alike?
4. What one Name fits an adapted understanding with the Instruction
   Texts built on it, without taking a word today uses for something
   else?
5. Does the intent need its own word for today's Work Approach, or
   does it have one already?
6. What does a System Repo need of the concept beyond its Adapted
   Cases, in what form, and where is it decided?
7. Should the System Kit's contents have one home, that every other
   mention points at?
8. Does "adapted" mean one thing, when it covers a sort of repo, a
   kind of system and one project, and is "narrowed" the more exact
   word?
9. Is a birth an Adapted Case of the Maintainer Repo's, and may its
   mechanical steps be something a human runs without the agent?

#### What the agent added

- **Adapted Case, not Approach:** today's Work Approach is the
  instructions alone, so "Approach" for both halves would give one
  word two scopes (Failure Case 8). Work Approach is today's name
  for what the intent calls Instruction Text, sorted by form, not by
  when it loads.
- **A field, Changed from today:** a "today" sentence in Decides
  reads as now (Failure Case 13). Each difference goes to the
  Common Ground Problem's §2.2.
- **A judged difference stays:** so something must mark it, or
  reading back judges the same edit again; the simulation's second
  pass is where the need shows.
- **"The concept" in the System Kit meant three things:** the
  project-agnostic text, which stays home; CBC for backends, already
  an Adapted Case; and a description for readers, the one left open.
- **Adapting does two things:** it narrows an idea and adds what the
  need has, such as HTTP for backends or a 50-character subject cap.
  What was added has nothing above it to be checked against; judging
  question 3 checks only the narrowed part.
- **A count in the wording decides what is open:** "one Adapted
  Case" where the split is open.
- **Today's Pure Seed is already half of a birth's Adapted Case:**
  shell commands inside a document, deciding nothing, since the repo
  holds no code. Instruction Text, what the agent acts on, does not
  cover steps a human runs alone.
- **Step 1's branch clashed with "stay home":** it sent the
  project-agnostic texts to a System Repo no System Kit fits.

#### What the reviewer took

The adapted understanding goes with its instructions; the
project-agnostic texts stay home, at birth and at an update, and an
update sends only the System Kit's changes, each with its why
(`eb841a4`, `51e975a`). A System Repo's copies stay its own after
reading back and an update, both halves alike (`b8ad5a1`). Adapted
Case, defined and swept through both drafts (`46d636e`, `83c8196`,
`e2e2916`); the mapping table's Instruction Text row (`7d15a60`).
*What the System Kit holds*, one list in its own section, the rest
pointing at it (`cad1f1c`, `28763b8`, `7af28da`). An Adapted
Understanding Text narrows to a sort of need and adds what that need
has (`8d1e229`, `83d7fb7`). Nothing crosses without the human's word
(`7392be1`); a birth is the Maintainer Repo's Adapted Case, its
mechanical part's form open (`e9cb979`); steps a human runs alone
have no Defined Term yet (`a2ecef2`). The moment of the System Kit is
marked at birth (`706ee8a`). A System Repo no System Kit fits starts
from a first Adapted Case the Maintainer Repo writes, on trial
(`40fa928`). The description of CBC system design waits for the
concept's split (`dde07a0`). Next, scenario 1, step 3.

### 2026-11-10, later

#### What the reviewer said

- **The start:** "which one we should keep and why: [the agent's
  line on committing the received files unchanged first] ? should we
  include that we deliver problem brief and first promp to start?
  maybe we should not commit from maintainer? do we include hash
  which should be included in records from maintainer in that promp?
  what else i may be missing? i think we have sep branck for that
  preparation in the runs, at least we had i think in run 3? do we
  need to mention that?"
- **A birth Adapted Case on the System Repo's side:** "so we prepare
  in maintainer not only problem brief but also prompt. also i want
  to have some Adapted Case for System Repo , which would know what
  it has to do in the beggining. If we say that we make first commit
  from Maintainer with System Kit Copy in new Repo, then in System
  Repo should be Adapted Case, that knows that it receives promp and
  has to cut new branch and do stuff. now, if we commit System Kit
  Copy most likely we have create local git repo and commited
  hygiene already? so this part shoud be clear what do what. does
  first job of agent is to read prompt and prepare everything? how
  much maintainer tells what shoud be prepared and how much system
  repo agent has to figure out itself?"
- **The prompt and the brief:** "we say that promp is the same for
  all birth, right? so it should live together with maintainer's
  part of birth Adapted case? as sep doc to use and not in
  instructions? instructions will refer to it? should we consider or
  left open if that prompt should be also touch durring delivery by
  problem brief?" And: "Also we should decide how that problem brief
  is started and when it reach new repo? do we start problem brief
  in maintainer repo temp/ and when we know which system kit we use
  we deliver it in new repo, so basicaly when we finish on problem
  brief? or we could have like default new repo each time we start
  on problem brief."
- **A repo for an idea:** "i thinking to have brief in sep repo. I
  think i dont want to polute maintainer of extend with another
  resposibility of problem intents. also System Repo could have its
  history, which we may want to edit maybe." And: "That repo may die
  not started a project. That repo does all briefing stuff not on
  main branch. when we decided to work on that problem briefing, we
  edit git history on that branch before we merge to main, so we
  keep history of problem but in controled way." And: "i still want
  marks for prompt here. if it standart for system kit, we could
  deliver together with the kit. but i want to leave open question
  if there should prompt we posible edits by problem briefing, which
  real world experience may demand." And: "also  that way maintainer
  would need to reg those and edit by how we work on them, like did
  it stated and what system kit is used, does it still on briefing,
  or did we droped. also i could open new session and work on ideas
  from fresh context, but have ability to bring required context
  what maintainer had access, like project-agnostic ideas or prev or
  now running projects."
- **Merge first, or go on:** "now should we merge to main and then
  again new branch cutted or we continue on say it should be open
  question and checked by real application, but for now i think we
  should choose one and mark second as trigger to check and confirm.
  what u think?"
- **An empty main and a messy branch:** "cant we work on briefing
  branch with empty main branch?" And: "we have this messy branch
  where we commiting how we need. then before we fast-forward, we
  copy that branch, clean up  there and fast forward to main. clean
  up branch can be deleted as it is on main now, messy is kept for
  history and local only, no remote push ever if we need hide messy
  part of briefing." And: "so basicaly we could repeat same thing
  for system birth scenario, where in the end branch is copied,
  cleaned, fast forward and deleted by keeping messy one for history
  and decliend for remote push."
- **Copy or clean in place:** "do we really need to copy branch
  before deleting, or that cleanup should go in same branch and we
  rebase on main only cleaned part?"
- **The step's fields:** "we have who acts, read, decides...do we
  need options here? also maybe we have section for Adapted Case as
  sep, which describes which is used and responsibility in this
  step? Why now it feels that it need steps inside step, like cut
  branch, copy system-kit, ...? why are those not sep steps? are
  they to small? should we have sep steps in each step?"
- **The check:** "Can we have agent Adapted case that checks that?
  should it be next to copy of system kit, where one delivers and
  other check the deliver?" Then: "why we have check on system repo
  side? i was thinking only about from maintainer?"

#### What the reviewer said, edited

The same words, with grammar and spelling fixed, the meaning kept:

- **The start:** "Which one should we keep, and why? Should we
  include that we deliver the problem brief and the first prompt to
  start? Maybe the Maintainer Repo should not commit? Do we put the
  hash that the Maintainer Repo's records must hold in that prompt?
  What else may I be missing? I think we had a separate branch for
  that preparation in the runs, at least in run 3; do we need to
  mention that?"
- **A birth Adapted Case on the System Repo's side:** "So the
  Maintainer Repo prepares not only the problem brief but also the
  prompt. I also want an Adapted Case for the System Repo that knows
  what it has to do at the beginning. If the Maintainer Repo makes
  the first commit with the System Kit Copies in the new repo, then
  the System Repo should have an Adapted Case that knows it receives
  a prompt, has to cut a new branch, and so on. If we commit the
  System Kit Copies, we have most likely created the local git repo
  and committed the hygiene files already? So it should be clear who
  does what. Is the agent's first job to read the prompt and prepare
  everything? How much does the Maintainer Repo say about what is
  prepared, and how much does the System Repo's agent work out
  itself?"
- **The prompt and the brief:** "We say the prompt is the same for
  every birth, right? So should it live with the Maintainer Repo's
  part of the birth Adapted Case, as a separate document to use, not
  inside the instructions, with the instructions referring to it?
  Should we consider, or leave open, whether the problem brief also
  changes that prompt during delivery?" And: "We should also decide
  how the problem brief is started and when it reaches the new repo.
  Do we start it in the Maintainer Repo's temp/ and deliver it to
  the new repo once we know which System Kit we use, so when the
  brief is finished? Or do we open a default new repo each time we
  start a problem brief?"
- **A repo for an idea:** "I am thinking of keeping the brief in a
  separate repo. I don't want to burden the Maintainer Repo, or
  extend it, with another responsibility: problem intents. Also, the
  System Repo could have its own history, which we may want to
  edit." And: "That repo may die without a project starting. It does
  all the briefing off the main branch. When we decide to go ahead
  with the brief, we edit the git history on that branch before we
  merge to main, so the problem's history is kept, in a controlled
  way." And: "I still want the prompt marked here. If it is standard
  for a System Kit, we could deliver it with the System Kit. But I
  want to leave open whether the problem brief may edit the prompt,
  which real-world experience may demand." And: "That way the
  Maintainer Repo would need to register these repos and update each
  by how the work on it goes: whether it started and which System
  Kit it uses, whether it is still briefing, or whether we dropped
  it. I could also open a new session and work on ideas from a fresh
  context, but be able to bring in the context the Maintainer Repo
  had access to, such as project-agnostic ideas, or earlier or
  running projects."
- **Merge first, or go on:** "Should we merge to main and then cut a
  new branch, or continue on the same one? We could say it is an
  open question, to be checked by real use. But for now I think we
  should choose one, and mark the other with a trigger to check and
  confirm it. What do you think?"
- **An empty main and a messy branch:** "Can't we work on the
  briefing branch with main empty?" And: "We have this messy branch
  where we commit however we need. Then, before we fast-forward, we
  copy that branch, clean it up there, and fast-forward main to it.
  The cleaned branch can be deleted, since it is on main now. The
  messy one is kept for history, local only, never pushed to a
  remote, if we need to hide the messy part of the briefing." And:
  "So we could repeat the same thing in the birth scenario: at the
  end the branch is copied, cleaned, fast-forwarded and deleted,
  keeping the messy one for history and never pushing it."
- **Copy or clean in place:** "Do we really need to copy the branch
  before deleting it, or should the cleanup happen on the same
  branch, with only the cleaned part rebased onto main?"
- **The step's fields:** "We have Who acts, Reads, Decides. Do we
  need options here? And maybe a section of its own for the Adapted
  Case, describing which one is used and its responsibility in this
  step? Why does it now feel as if steps need steps inside them,
  like cutting a branch or copying the System Kit? Why are those not
  separate steps? Are they too small? Should each step have separate
  steps?"
- **The check:** "Can an agent's Adapted Case do that check? Should
  it sit next to the one that copies the System Kit, so that one
  delivers and the other checks the delivery?" Then: "Why is there a
  check on the System Repo's side? I was thinking only of the
  Maintainer Repo's."

#### What the reviewer asked, as the agent would ask it

The questions the reviewer was asking, put by the agent:

1. Who fixes where a System Repo's own history starts, the birth
   before the agent acts or the agent's first commit, and what of
   today's birth, its Receipt Branch among it, does that borrow?
2. Does the birth deliver the brief and the first prompt, and does
   the System Kit's moment travel in the prompt or in the files?
3. What does the Maintainer Repo prepare at a birth, and what does
   the System Repo's agent work out itself, by an Adapted Case of
   its own?
4. Where does the fixed prompt live, and may a brief change it?
5. Where is a brief drafted, and when does it reach the repo that
   will be born?
6. Can a brief live in a repo of its own from the first idea, made
   and registered by the Maintainer Repo, which may die or later be
   born into a System Repo?
7. After a brief's history is cleaned, does main take it before
   birth, or does birth go on from the same branch?
8. Can main stay empty until the brief is finished, and can the
   messy branch be kept, local, while only a cleaned branch reaches
   main, at the brief and at birth alike?
9. Must the clean history be built on a branch apart, or can it be
   cleaned in place?
10. Does a step need fields for what it leaves open and for the
    Adapted Case it runs by, and where does one step end and the
    next begin?
11. Who checks a delivery, and by which Adapted Case?

#### What the agent added

- **Today's texts disagree on the start:** the Pure Seed writes the
  Read-Through Commit as *none* at birth; the exchange's cycle has
  the CBC Run write its birth commit b.
- **The moment goes in the files, never the prompt:** a prompt lives
  in one session, and Run 3 showed a rule told only in a session is
  lost there.
- **A prompt fixed per System Kit keeps births comparable;** a brief
  retold in the prompt would be a second home for the problem.
- **Blindness is only told today:** Run 3's agent read a checkout on
  disk of the repo it took copies from. No Failure Case covers it.
- **Keeping the messy branch off the remote does not hide it from
  the agent** in the same repo: `git log --all` shows it. Hence the
  open question of moving it out.
- **The cleanup can delete what reading back needs:** lessons are
  written before it, and a record citing a messy commit points at
  nothing on main.
- **The start must survive the birth's cleanup whole:** the clean
  branch is built on the start itself, and the start's commit is
  checked the same on both branches.
- **A clean branch apart keeps two rules:** the messy branch is
  never rewritten, and main moves once, after the human approves.
  Cleaning in place breaks the first; cleaning on main, the second.
- **An empty main works:** tried in a scratch repo, the first commit
  goes on the briefing branch, and main is made later at the clean
  tip.
- **Steps inside a step are its Adapted Case's order.** A step is
  one actor, in one repo, doing one kind of work, ending in
  something a later step reads.
- **A misreading:** the agent first put the delivery's check on the
  System Repo's side, with a file list. A blind repo cannot compare
  with the System Kit; the reviewer had meant a second Adapted Case
  beside the one that delivers.

#### What the reviewer took

The start is the delivery as it arrived, made by the birth before
the agent acts, and today's way kept over the agent's first draft; a
birth Adapted Case on the System Repo's side gives the outcomes and
the order, never the arrangement (`e95b73b`). A brief lives in a
repo of its own, scenario 0: made and registered by the Maintainer
Repo, worked on a briefing branch kept local, cleaned onto a branch
apart, main made once; whether the briefing branch stays in the repo
is open (`6cd4cfa`). Birth happens in that repo, main growing from
the start; the prompt goes with the System Kit, whether a brief may
edit it open (`d49478d`). Each step names its Adapted Case and what
it leaves open (`3652e69`). The birth's cleanup is a step of its own
(`3c42a4e`). A second Adapted Case of the Maintainer Repo's checks
the delivery (`1cc6f0e`). Next, scenario 2.

### 2026-11-10 and 2026-11-11

#### What the reviewer said

- **Freezing the scenarios:** "i think this can increase complexity of already complex enough problem, where we build common-ground-problem solution together with current repo update to intent repo. so i think what we can do is to freeze those scenarios for later, after we finish with this problem." And: "So what i think we should take one obviuos scenario and just describe intent of it. this scenarios should be system repo system kit copy change. so if we define this one case we and we write boundary that there is others, but we intentionaly not dealing now with those, we could continue on common-ground-problem."
- **The hows, for one case first:** "also i think we need also to write: how change is recorded, how we read, how we decide, and how we write update. right?" And: "should we split in possible scenarios, select only one now to define first version for hows. after check each if that holds?"
- **Narrowing, never shrinking:** "it coud happend, that project agnostic understanding does not need any records, as it hold that change already and we need only to change adapted cases." And: "should we not shrink ever and in adapted case just mark that this specific part is excluded here with reason why?"
- **Simulating to write rules:** "go step by step and consider what must happen. for example we take change as sep step and cosider for specific case what could we do and what we finaly choose. when we see all steps togther we write rules. then we check with out scenario all steps and how rules holds." And: "lets sep for change in system-repo, where we put as all simulations needed till we can continue on the common-ground-problem with derived rules."
- **A scope, not an example:** "why we need that example at all? why we can just have define scope with example?"
- **Checking at the gate:** "each step has its ending. current system repo uses such plan and has gates. it think this structure will not change. so i think this is the place to check and this is one gate to include: to check if we have any changes for Adated Cases we  have used." And: "or should we have like note create , when we first time dissagree what Adapte Case is saying and check that note in the end?"
- **Entries in a footer:** "or we should have changes and records why that happened as footer in Adapted Case understanding, because it does not load for work and those change notes does not bothers." And: "if we write notes of change whys and whats, we can change any time we like and reverse or edit those changes. gates and session end just checkpoints and we should decide how they could be useful."
- **A proposal, checked twice:** "Should we go with double check, where system repo gives this as proposal from his point of view and maintainer checks change and gives his oppinion on that proposal, where it could find that suggestion was incorrect?"
- **Worth its upkeep:** "Now tell me how usefull or redundant this is? do we loose alot without it? what it actualy helps us? how much of maintanance that brings and is it worth it?" And: "yes, drop step 2, but should we keep a record, like what we have droped?"
- **Notes:** "i think i still may use this practice, where i will note something that maintainer should look or check, when something is poping in my minds. so if this funtionality is available, is there point to list about these changes? is it a noise and/or breaks one-home rule"
- **One System Repo by default:** "Can i still in some case ask to read some steps in the middle of work if needed or to check only specific repo only and not check all when needed?"
- **"Read to" in the register:** "you mean all readings are kept just to have from where to read? i not see this as good idea. i think if we have register, we could store there where we left, like hash of commit or something." And: "now if reading was never done, should we have default "none", "null" or what? is this not this step responsibility?"
- **Knowledge on Trial:** "also about that folder, we also have sep folder in system kit for them, as we have in today's."
- **The questions:** "do we ask those questions for each finding? are those questions good? should i be asking more? are they fit everything?" And: "if change that is comming is actually needed, but it is writen not quite good, like it is too specific to problem, not shared enough manner. will we still drop it even if change is needed only writen better?"
- **Who a verdict is for:** "for whome we write verdic? do i understand correct, that we write those for ourself to prepare changes on system kit and when needed project-agnostic understanding with everything related to them."
- **An update in the middle of a step:** "now i have updated which is for the part that is before step started. if i brough that and update in the middle of step it is a place of possible failure, because update was conidered on old info and if we process update we can u loose new info because work moved forward."
- **What is delivered:** "we also need to deliver updated system kit as copy, doesnt it? because how system repo will know how it looks after reading is taken? do we need to deliver everything or only whats touched?"
- **Who checks the fit:** "who should check this fitting thing? should system repo do that as it knows better its needs, or maintainer during the update when it writes that update."
- **Delivery, a step:** "we will have adapted case for deliver: "The human carries it into the System Repo, since nothing arrives by itself". so is it step we missing? deliver updates?"
- **Entries at the take:** "shouldnt we delete entries and write new ones? also we could write what has not fit and what we changed during implementation of update."
- **A boundary at the opening:** "can we solve this we just writing boundary that today, system repo can not move forward while update is not finished."
- **Bounding out:** "now i really thinking , maybe i should bound out this and wait till i face this. because this is too much complexity for now."
- **A gate that reworked entries:** "it could happend that at gate of step, new entries togther with old ones was merged, wired or connected into new findingd. so how would that work? is it simpler to just drop update and redo or atleast redo and in the end just compare somehow?" And: "so we kind of need to readings or/and reading evalutations? am i missing something?"
- **"Read to" once acted on:** "so after we judge, "read to" still not moves till we not locked those changes we found in this maintainer repo. after changes was landed, that means there is no more to read and judge and "read to" is safe to move, no matter if repo reached updates." And: "is it true that we could split those basicaly in 2 cases, where first one is when updated that is comming, was prepared on same system kit version from which reading of that updated was done and if that system repo we sending update nowhere moved."
- **Six parts:** "should it be like `change(system repo) -> read(maintainer) -> judge(maintainer) -> update(maintainer) -> deliver(maintainer) -> take updates(system repo)`?" And: "why we need that split into 2 half? those half gives us what? what not remove that split and then split in those six parts?"

#### What the reviewer said, edited

The same words, with grammar and spelling fixed, the meaning kept:

- **Freezing the scenarios:** "I think this can add complexity to a problem already complex enough, where we build the Common Ground Problem's solution together with turning today's repo into the intended one. So I think we can freeze those scenarios for later, after we finish this problem." And: "So I think we should take one obvious scenario and just describe its intent. This scenario should be a System Repo changing its System Kit Copy. If we define this one case, and write a boundary saying there are others that we are not dealing with now on purpose, we can continue on the Common Ground Problem."
- **The hows, for one case first:** "I think we also need to write how a change is recorded, how we read it, how we decide, and how we write the update. Right?" And: "Should we split it into possible scenarios, select only one now to define a first version of the hows, and afterwards check whether each holds?"
- **Narrowing, never shrinking:** "It could happen that the project-agnostic understanding needs no record, since it already holds that change, and we only need to change Adapted Cases." And: "Should we never shrink it, and in the Adapted Case just mark that this specific part is excluded here, with the reason why?"
- **Simulating to write rules:** "Go step by step and consider what must happen. For example, take a change as a separate step and consider, for a specific case, what we could do and what we finally choose. When we see all the steps together, we write the rules. Then we check all the steps against our scenario, and how the rules hold." And: "Let's separate the System Repo's change into its own file, where we put all the simulation needed until we can continue on the Common Ground Problem with the rules derived."
- **A scope, not an example:** "Why do we need that example at all? Why can't we just define the scope?"
- **Checking at the gate:** "Each step has its end. Today's System Repo works by such a plan and has gates. I don't think this structure will change. So I think this is the place to check, and this is one gate to include: checking whether we have any changes for the Adapted Cases we have used." And: "Or should we create a note the first time we disagree with what an Adapted Case says, and check that note at the end?"
- **Entries in a footer:** "Or we should keep the changes, and records of why they happened, as a footer in the Adapted Understanding Text, because it is not loaded for work, so those change notes don't get in the way." And: "If we write notes of each change's why and what, we can change anything at any time, and reverse or edit those changes. Gates and session ends are just checkpoints, and we should decide how they could be useful."
- **A proposal, checked twice:** "Should we check twice, where the System Repo gives this as a proposal from its point of view, and the Maintainer Repo checks the change and gives its opinion on that proposal, so it could find that the suggestion was incorrect?"
- **Worth its upkeep:** "Now tell me how useful or redundant this is. Do we lose much without it? What does it actually help us with? How much upkeep does it bring, and is it worth it?" And: "Yes, drop step 2. But should we keep a record of what we dropped?"
- **Notes:** "I think I may still use this practice, where I note something the Maintainer Repo should look at or check, when something pops into my mind. So if this is available, is there any point in listing these changes? Is it noise, does it break the one-home rule, or both?"
- **One System Repo by default:** "Can I still, in some cases, ask to read some steps in the middle of work if needed, or check only one specific repo and not all of them?"
- **"Read to" in the register:** "You mean all readings are kept just so we know where to read from? I don't think that's a good idea. If we have a register, we could store there where we left off, like a commit hash." And: "If a reading was never done, should we have a default, "none", "null", or what? Isn't this this step's responsibility?"
- **Knowledge on Trial:** "Also, about that folder: the System Kit has a separate folder for them too, as today's does."
- **The questions:** "Do we ask those questions for each finding? Are they good questions? Should I be asking more? Do they fit everything?" And: "If an incoming change is actually needed, but it is not written well, too specific to the problem, not written in a shared way, do we still drop it, even though the change is needed and only needs writing better?"
- **Who a verdict is for:** "Who do we write the verdict for? Do I understand correctly that we write it for ourselves, to prepare changes to the System Kit and, when needed, to the project-agnostic understanding, with everything related to them?"
- **An update in the middle of a step:** "Now I have an update for the part before the step started. If I bring that update in the middle of the step, it is a place where things can fail, because the update was built on old information, and if we process it we can lose new information, since work moved forward."
- **What is delivered:** "We also need to deliver the updated System Kit as a copy, don't we? Otherwise how will the System Repo know how it looks after the reading is taken? Do we need to deliver everything, or only what was touched?"
- **Who checks the fit:** "Who should check this fit? Should the System Repo, since it knows its needs better, or the Maintainer Repo, when it writes the update?"
- **Delivery, a step:** "We will have an Adapted Case for delivering: "The human carries it into the System Repo, since nothing arrives by itself". So is it a step we are missing, delivering updates?"
- **Entries at the take:** "Shouldn't we delete the entries and write new ones? We could also write what did not fit, and what we changed while putting the update in place."
- **A boundary at the opening:** "Can we solve this just by writing a boundary that, for now, a System Repo cannot move forward while an update is not finished?"
- **Bounding out:** "Now I am really thinking I should bound this out and wait until I face it, because it is too much complexity for now."
- **A gate that reworked entries:** "It could happen that, at a step's gate, new entries together with old ones were merged, wired or connected into new findings. How would that work? Is it simpler to drop the update and redo it, or at least redo it and just compare at the end somehow?" And: "So do we need two readings, or two reading evaluations? Am I missing something?"
- **"Read to" once acted on:** "So after we judge, "read to" still does not move until we have locked in the changes we found, in this Maintainer Repo. Once the changes have landed, there is nothing more to read and judge, and "read to" is safe to move, whether or not the update has reached the repo." And: "Is it true that we could split them into two cases, the first where the incoming update was prepared on the same System Kit version the reading was done from, and the System Repo we are sending it to has not moved?"
- **Six parts:** "Should it be change (System Repo), read (Maintainer Repo), judge (Maintainer Repo), update (Maintainer Repo), deliver (Maintainer Repo), take the update (System Repo)?" And: "Why do we need that split into two halves? What do the halves give us? Why not remove that split and split into those six parts instead?"

#### What the reviewer asked, as the agent would ask it

The questions the reviewer was asking, put by the agent:

1. Can the scenarios be frozen, and one case, a System Repo changing its copy, followed until the Common Ground Problem has rules, the others bounded out on purpose?
2. Does the case need the four hows, recorded, read, decided and updated, and should one case be worked first and the rest checked against it?
3. When the project-agnostic text already holds a lesson, or holds what fits not every Adapted Case, does it change, or does the Adapted Case mark what it leaves out?
4. Should the rules be found by simulating each step in a file of its own, options weighed and one chosen, and written only once a half's steps are seen together?
5. Does a fixed example bound the case, where a scope would not?
6. Where is a copy's change caught: a Plan Step's gate, a note at the first disagreement, a check at a session's end, or an entry written with the change?
7. Who decides whether a change is the System Repo's own or any repo's?
8. Is each check worth its upkeep, and is a dropped one recorded?
9. Do the reviewer's own notes to the Maintainer Repo repeat the entries?
10. Is one System Repo read by default, and can a reading be asked for at any time?
11. Where is a reading's stop kept, and what does it start as?
12. How is new Knowledge on Trial found?
13. Are the judging questions enough, and is a needed change that is badly worded dropped?
14. Who reads a verdict?
15. What happens to an update made from a reading the work has since moved past?
16. What does an update carry, and who checks that it fits?
17. Is delivery a step of its own, by an Adapted Case?
18. Do entries survive a take?
19. When the System Repo moved on, is the update redone or continued, and does a repo on an older System Kit moment need a reading of its own?
20. When does "read to" move?
21. Are the six parts the real structure, and what do the two halves still give?

#### What the agent added

- **Today's stop needs a delivery to travel:** the Read-Through Commit reaches the CBC Run only in a Delivery Note. Once a reading may have no update after it, the stop must live in the Maintainer Repo.
- **Only a Plan Step's gate survives sessions;** a session's end is not a checkpoint the work can rely on. The session-end check was weighed with the reviewer and dropped, its trigger kept.
- **An entry written with the change, in the same commit,** is caught by a commit check; nothing else needs remembering.
- **Judging reads what a change does, never its wording:** the System Repo writes in its own words, and rewording is the Maintainer Repo's, after judging. Question 0, is the change sound, comes first, since an unsound change spreads nowhere.
- **Entries describe a difference from one System Kit moment.** After a take, none says how a copy differs from the new one, so all are cleared and the needed ones rewritten.
- **A check before delivery can be stale by the take;** a check at the take is not. The update's note names its base and the reading's stop, so even an older Adapted Case for taking runs the check.
- **"Covered":** a change the System Kit has since made the same way, so a lesson is not made twice.
- **"Halves" names two things:** the two halves of the case, and the two texts of an Adapted Case.
- **Misreadings:** the agent wrote the verdict for the System Repo; wrote that the human carries the update, where an Adapted Case delivers; and wrote that birth's delivery was the only time the Maintainer Repo writes into a System Repo. The agent's redo-and-compare, for a System Repo that moved on, was replaced by the reviewer's "read to" once acted on.

#### What the reviewer took

The scenarios are frozen, and one case, "A System Repo's change", is followed in two halves, recorded and read, then decided and updated (`d9cd5ca`, `fc15327`, `61f8770`). A Project-Agnostic Understanding Text narrows and never shrinks (`9f6cc48`). The case is simulated step by step in `temp/system-repo-change-simulation.md`, by a scope rather than an example, with its cases table (`75808bd`, `698878d`, `98929f7`). A copy changes with its entry in the Adapted Understanding Text's footer, checked at the commit; each step names its Adapted Case (`5226a0e`, `22d9624`, `c15c23f`). The gate keeps, edits or reverses each change, and a note carries only what has no change (`a357418`, `eb94bc9`). "Read to" lives in the register, set by birth (`3ea48da`, `22b803c`). The first half's rules are written from the steps (`8412f15`). Judging gains question 0 and reads substance; the verdict is the Maintainer Repo's (`4bf6aa9`, `0af84ad`, `f037caa`). The update carries the whole System Kit and the verdicts that can be acted on, is delivered in a step, and is taken at a Plan Step's opening, entries cleared (`a3a597e` to `05050ed`). "Read to" moves once the verdicts are acted on; the take checks its own base, case 1 or case 2 (`b2f458c`, `d124fd7`). The six parts are mapped (`0b24556`). Next: the halves give way to the six parts when the rules are written from both.

### 2026-11-11 and 2026-11-12

#### What the reviewer said

- **Six parts, not halves:** "what about droping the split and making it into six parts which table we have in "## 1. How it is worked" of "system-repo-change-simulation"?"
- **Alike cases:** "i think we could drop or merge something. for example having different cases where "both halves of one Adapted Case" and "an Instruction Text only" as sep is no point anymore, doesnt it? it does not matter if we have change entries in Adaped Case , right?" And: "it quit big change, maybe we should write down how we gonna do this? where we start and what order?"
- **The rule headings:** "why we keeping in "##### Recording and reading" and "##### Deciding and updating" in common-ground-problem? should we split in same way as in simulation? why?"
- **Always read first:** "if update is delivered to repo,where we dont need to read, that means that repo dont have repo specifics? or i missing something. lets consider the case, when we deliver update to repo, which we not read. so that repo should be with same system kit moment the change was done and also work was not moved on. can that case be without any change entries? should i comepletle ignore that case and always read, especialy when i return on prev repo which was paused?"
- **Specifics written back:** "we get reading in which there is finding which are project specific. in judge we confirm those and write those back. system repo itself writes those back to system copy when it takes updates and write entries again. that means we have updated and we can continue working." And: "maybe only one case where after we took update and rewrote specific to project changes with entries and nothing have change we dont do reading and judging as nothing really have changes even though system kit copy if different. but that we may want to leave as open question for practice to test and not overcomplicate here"
- **No memory of verdicts:** "lets go b. it is same thing we just talked. in this modeling lets leave just normal read without memory of what was done before"
- **New Defined Terms:** "Do we need these new terms: moment ..., change ..., entry ...? what could they be?"
- **Version, change and record:** ""System Kit Version" i think is good, but should it be more correct if we say "System Kit Copy Version", or "System Kit Version" works too?" And: "Now "Change Entry" is does not say alot, doesnt it? also definition is not quite right too. we write entry in Adapted Case understanding text. System Kit does not has footer. But then hat means all parts has to have Adapted Understanding Text, not only instructions. this could be true, but we not know that now. maybe in definition tell that." And: "About change, maybe we should have Adapted Case Change where it is only about changes of those which came wih System Kit copy? current version?"
- **The two notes:** ""System Kit Note" is actualy a "System Kit Change Note" as todo, doesnt it? And "System Kit Update Note" is what maintainer write as note when we deliver update to take." And: "should we say, then attention note or what?"
- **Whose register:** "what about "Maintainer's System Repo Register"?"
- **Long names:** "Is it because of long name? how that could be solved? we cant use just Change, doesnt we? because if we later will need again new Change it will be ambiguas?" And: "i dont see here anything better actually. we still need to distinct kit from copy, copy from change, record from change... so i think those stays. also does this more clear for agent and it will not mixed up things?"
- **The steps again:** "i think we will go each step again to confirm or fix each again after this commit plan."

#### What the reviewer said, edited

The same words, with grammar and spelling fixed, the meaning kept:

- **Six parts, not halves:** "What about dropping the split and making it into the six parts, from the table in "## 1. How it is worked" of the simulation?"
- **Alike cases:** "I think we could drop or merge something. For example, having "both halves of one Adapted Case" and "an Instruction Text only" as separate cases has no point any more, does it? It does not matter where in the Adapted Case the change entries are, right?" And: "It is quite a big change. Maybe we should write down how we are going to do it: where we start, and in what order?"
- **The rule headings:** "Why are we keeping "Recording and reading" and "Deciding and updating" in the problem file? Should we split them the same way as the simulation? Why?"
- **Always read first:** "If an update is delivered to a repo we did not need to read, does that mean the repo has no specifics of its own, or am I missing something? Consider delivering an update to a repo we have not read: it would still be on the System Kit version the change was made from, and its work would not have moved on. Can that case have no change entries at all? Should I ignore that case completely and always read, especially when I return to a repo that was paused?"
- **Specifics written back:** "We get a reading with findings that are project-specific. In judging, we confirm those, and they are written back: the System Repo itself writes them back into its System Kit Copy when it takes the update, and writes their entries again. Then the update is done, and we can continue working." And: "Maybe there is one case: after we took the update and rewrote the project-specific changes with their entries, and nothing else changed, we don't read and judge, since nothing has really changed, even though the System Kit Copy differs. But we may want to leave that as an open question for practice to test, and not overcomplicate it here."
- **No memory of verdicts:** "Let's go with b. It is the same thing we just talked about. In this model, let's keep a normal reading, with no memory of what was done before."
- **New Defined Terms:** "Do we need these new terms: moment, change, entry? What could they be?"
- **Version, change and record:** ""System Kit Version" is good, I think. But would "System Kit Copy Version" be more correct, or does "System Kit Version" work too?" And: ""Change Entry" doesn't say much, does it? The definition isn't quite right either: we write the entry in the Adapted Case's Adapted Understanding Text, and the System Kit has no footer. That would mean every part has to have an Adapted Understanding Text, not only the instructions. That could be true, but we don't know it yet; maybe the definition should say so." And: "About change: maybe we should have Adapted Case Change, only for changes to what came with a System Kit Copy, its current version?"
- **The two notes:** ""System Kit Note" is actually a "System Kit Change Note", like a TODO, isn't it? And "System Kit Update Note" is what the Maintainer Repo writes as a note when we deliver an update to take." And: "Should we call it an attention note, then, or what?"
- **Whose register:** "What about "Maintainer's System Repo Register"?"
- **Long names:** "Is it because of the long names? How could that be solved? We can't use just Change, can we? Because if we later need another Change, it will be ambiguous." And: "I don't actually see anything better here. We still need to tell kit from copy, copy from change, and record from change, so I think those stay. Also, is this clearer for the agent, so it won't mix things up?"
- **The steps again:** "I think we will go through each step again, to confirm or fix it, after this commit plan."

#### What the reviewer asked, as the agent would ask it

The questions the reviewer was asking, put by the agent:

1. Should the simulation drop its two halves and run in the six parts its own table maps?
2. Do cases that differ only in which text of an Adapted Case changed still need rows of their own, given the entry sits in one place?
3. Should a change this size be planned commit by commit before it starts?
4. Should the problem file's rules be grouped by the same six parts, and why were the two groups kept?
5. Is there ever an update without a reading, or is every update preceded by one, even for a paused repo?
6. Who puts a System Repo's own changes back after a take, and does the next reading need to know they were judged before?
7. Do "moment", "change" and "entry" need Defined Terms, and what are they?
8. Whose version is it, the System Kit's or the copy's; where does a record sit for a copy outside any Adapted Case; and how narrow is the change?
9. What should the System Repo's note and the update's note each be called?
10. Should the register's name say whose it is?
11. Can the long names be made shorter without becoming ambiguous, and are they clearer for the agent?

#### What the agent added

- **"Half" named two things:** a part of the case, and one text of an Adapted Case. The six parts removed both.
- **Every update already follows a reading:** the Deliver step makes one only after the System Repo is read and judged, so no case of an update without a reading exists.
- **The agent proposed that the Maintainer Repo build each update with the System Repo's own changes in it,** so the take is a plain install. The reviewer kept the System Repo putting them back itself, as Take step 4 says.
- **Step 7 decided nothing** once the reading kept no memory of verdicts, so its questions became Opens in Read, step 3.
- **"Note" meant two things in the same steps:** what a System Repo writes, and what goes with an update.
- **"System Kit Copy Version" would name one copy's version,** which changes with every edit; the version is the whole System Kit's.
- **"Adapted Case Change" would leave out the Defined Terms and the description,** which the System Kit holds too.
- **A name built on another carries it whole,** so "Maintainer's" became Maintainer Repo Register, and shorter names such as Local Change were weighed against the long ones.
- **Misreadings:** the agent first kept the problem file's two rule groups as work done twice; counted the cases table by eye, "10 or 11", where 12 was right; and offered a step 7 that the simulation's own Take step had already contradicted.

#### What the reviewer took

The simulation runs in six parts, its alike cases merged, under a commit plan (`d875239` to `5af546f`); the problem file's rules sit under the same parts (`0266d9d`). Every update follows a System Repo Reading, the System Repo puts its own changes back at the take, and a reading keeps no memory of earlier verdicts; step 7 became two Opens left to practice (`63de51b`). Eight Defined Terms and a label are defined: System Kit Version, System Kit Copy Change, System Kit Copy Change Record, System Kit Attention Note, System Kit Update, System Kit Update Note, Maintainer Repo Register with *read to*, and System Repo Reading (`514b706` to `e738413`), and the two files use them (`15e7b32` to `8b96309`). The long names stay, since they keep kit, copy, change and record apart. Next: each step gone through again, then depth c, then the rules rewritten from the steps.

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
