# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step. Prune "Later" ruthlessly: deleting an
     idea you'd re-derive anyway costs nothing.
     Rule: an inline TODO:/FIXME: anywhere in the work must reference an
     item here.
     Open work only: a closed item goes, since the devlog, the ADRs
     and git already say what closed. Known issues take the form
     their heading names. Every other item takes one form:

     - [ ] <What to do or decide.> (<date>, <who raised it>)
           Context: <why it holds, true today — eight lines at most>.
           Ideas: <optional — how it might be handled, a line each>.
           Trigger: <the moment it is due>.
           See: <the devlog entry, ADR or commit with its story;
                its section in TODO-CONVERSATION-MEMORY.md, if any>.

     The story goes in that session's devlog entry when the item is
     added, and See points at it; an item that is its story's only
     home keeps it and has no See. Ideas are noted as they come and
     weighed only when the item is due — each is then taken,
     extended or declined, and the verdict goes with the work. The talk that shaped an item may sit in
     TODO-CONVERSATION-MEMORY.md; when See names its section, it is
     read before the Ideas are weighed. When an item changes, rewrite
     it true for today — never stack a dated update on it; the
     change's story is the devlog's.
     Why the form is as it is: (docs/conventions/project-recording/
     §5.4, How).
     foundation: the project-recording convention -->

## Now (due while the open step runs)

## Next (each due at its trigger)

- [ ] Read run 6, `checkout`, by `exchange-read` (2026-10-29, the
      reviewer).
      Context: run 6 ran on full auto through its Release, Step 14,
      and closed a Step 15 after it: 254 commits, 7 slices, tag
      `v0.1.0`. Its birth step stopped before its close, so its
      reading waits.
      Trigger: the refinement's close, or the reviewer's word.
      See: devlog 2026-10-29, morning.

- [ ] Unlock the folders locked for run 6 (2026-10-29, the
      reviewer).
      Context: run 6 must not read another repository, and a
      `Read` deny rule does not stop a shell. So, before its birth,
      twelve entries in `~/IdeaProjects` were made unreadable,
      `chmod 000`: `archive`, `cbc-pure-run`, `cbc-pure-run-2`,
      `cbc-pure-run-3`, `cbc-pure-run-4`, `cbc-pure-run-5`,
      `checkout-system`, `idempotent-orders`, `order-placement`,
      `safe-reservations-v1`, each 755 before; and
      `checkout-system-first-prompt.md`,
      `safe-reservation-briefing.md`, each 644 before.
      Trigger: the reviewer's word, or before run 5's lessons step
               resumes, since it reads run 5. Run 6's Release,
               the first trigger, has passed; the reviewer kept
               the lock for now.
      See: devlog 2026-10-29, night.

- [ ] Write `exchange-birth` while a birth runs (2026-09-26, the
      reviewer).
      Context: written from the exchange's manual, as `exchange-read`
      and `exchange-deliver` were, keeping the seed's intent — it
      delivers everything and decides nothing. Then *What this does
      not do* in `.claude/skills/exchange-deliver/SKILL.md` points at
      it, `pure-seed.md` goes, and ADR-0016's procedure of record
      moves. Runs 5 and 6 are born by the seed, to keep their births
      small.
      Ideas: first-time work on our seat, so an approach on trial
             drafted by `approach-drafting` (ADR-0058).
      Trigger: the birth after run 6's.
      See: devlog 2026-09-26, evening; and 2026-09-30, night,
      later, where `pure-seed.md` was brought up to date for it.

- [ ] Decide whether a commit plan's look-back also asks if the
      work could have been done better (2026-10-21, the reviewer).
      Context: before its close, `commit-plan` looks back at the
      landed commits for their grouping only. Work shows what a plan
      missed; the reviewer would have the look-back ask whether the
      work itself could be meaningfully better, and if so try that
      way and compare it with the first try before keeping one. Run
      4 tried each Real question's options on `try/` branches: 14
      of them, and 2 changed the answer. Run 5 tries it first, from
      its hand-off.
      Ideas:
      - a bar for "meaningful": it changes a wall, a test's
        adversity, or removes a part; rewording is not enough.
      - the better way on a `try/` branch, compared, the loser kept.
      - a cap on its cost, so no plan doubles by habit.
      Trigger: run 5's reading.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §9, *A commit plan's look-back…*.

- [ ] Decide whether the concept, the conventions and the
      approaches keep examples (2026-10-21, the reviewer).
      Context: run 4 read run 3's real kills in the shapes' examples
      at birth, and its framing copied them in places (ADR-0061).
      The method's worked example, 271 lines in both `cbc-framing`
      and `cbc-slice`, is an order service that weighs "Orders are
      never lost AND payment always completes"; the concept's
      chapters, the slice workflow, the playbook, `writing.md` and
      the stack's references hold smaller ones. Run 5, event
      tickets, is born with all of them.
      Ideas:
      - examples stripped to a description of what must be done.
      - examples kept, drawn from a domain no run will build.
      - examples kept where a reader learns, gone where a run acts.
      Trigger: run 5's reading.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §10, *Examples in the concept…*.

- [ ] Decide how work is run by agents: delegation, model and
      effort by kind of work, forks or fresh agents, new challenges
      and look-backs; and what the agent's setup holds, and where
      that is recorded (2026-10-22, the reviewer).
      Context: nothing here says when a lead agent hands work to
      others, with which model and effort, or whether a fork or a
      fresh agent takes it. On 2026-10-21 the agent sent 3 readers
      to run 4 and 8 to the close read on its own judgement; run 4
      changed model mid-run with no record of why. `/doctor`,
      2026-10-22: 69 general-purpose agents in 29 days, none given
      a model, so all on Opus: 11% of a week's usage. New challenges
      have `approach-drafting`; looking back has a trial in run 5.
      Ideas:
      - low effort to read and collect; the highest to find the
        options; medium or high to implement and summarise.
      - a lead agent fans out readers and keeps the decisions.
      - each delegation leaves one line: the kind of work, the
        model, the effort, whether it paid.
      - an approach on trial before any convention (ADR-0058); a
        convention of its own, or a section of agent-arrangement.
      - one default model for every subagent, offered by `/doctor`
        and held for this item.
      - before a new skill is proposed, search what exists: the
        plugin marketplace (`/plugin`, 315 plugins) and the account
        skills.
      - setup records stay in `.claude/decisions.md`, or user-wide
        switches (`~/.claude/settings.json`, every project) go
        elsewhere.
      - a table of what is on or off, each graded by its evidence
        (can't run here, no trigger, named trigger, regular work),
        what it does, where it applies; the first is in
        `.claude/decisions.md`, 2026-10-22, the account skills.
      - skills not ours (account, built-in, plugins) arrive and
        change without us: when the table is graded again, and by
        whom.
      - read and grade into the table the plugins nearest this
        work: `session-report`, `hookify`, `claude-code-setup`,
        `superpowers`, `mattpocock-skills`.
      - the `session-report` plugin, for what each delegation cost,
        only if `/usage` cannot answer it; not run, known from its
        catalog listing.
      - where a habit of working with the reviewer lives:
        `CLAUDE.local.md`, the agent's memory, or a rule. On
        2026-10-23, staging a TODO line at once went to
        `CLAUDE.local.md`; memory loads only when recalled.
      - a manual's "What this is made usable as" also names any
        `CLAUDE.md` line and the settings it leaves to the operator,
        so `CLAUDE.local.md` holds only those
        (`docs/conventions/agent-arrangement/` §3.7, *`CLAUDE.local.md`*: settings,
        never rules).
      - or that section splits in two: the approaches, and what
        reaches the agent's setup.
      - `CLAUDE.local.md` repeats two rules, both commit-messages':
        commit on the word, and a stop at each boundary
        (`docs/conventions/commit-messages/` §2.4, *Commit on the word*). Yet agent-arrangement counts how often the agent stops as a
        setting (`docs/conventions/agent-arrangement/` §3.7, *`CLAUDE.local.md`*). Round
        2's FINDING-194 found it again.
      - "never rewrite main across 35edd3f" lives only in the
        agent's memory, unseen by any reader of the repo. Its
        failure is not noticing the moment, a rebase: a local rule
        for our `CLAUDE.md` (`docs/conventions/agent-arrangement/`
        §2.4, *How*)?
      Trigger: run 5's reading, with the lines gathered by then.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §11, *How work is run by agents*; `.claude/decisions.md`, 2026-10-22, the account skills.

- [ ] Evaluate `auto-run`, the approach on trial for preparing a
      full-auto run (2026-10-22, the step that birthed run 5).
      Context: drafted and used once, for run 5
      (`.claude/approaches-on-trial/auto-run.md`, its use note). Its
      open questions are run 5's reading's to answer: what in the
      hand-off is general enough for the container, and whether the
      light read of the last run cost run 5 anything. Evaluated
      before that, every piece would end on trial and be judged
      again.
      Trigger: run 5's reading, with its lessons in hand.
      See: devlog 2026-10-22.

- [ ] Decide how an approach and a shape divide an output: the
      approach says what is done, the shape how its output looks
      (2026-10-20, the reviewer).
      Context: a shape is read at the gate only, so work written
      without it can show it wrong (`docs/conventions/shapes/` §3, *One place, read at the gate*).
      A skill that carries the output's form undoes that.
      `cbc-framing` hands over `templates/registry.md` to fill in,
      for the output the `registry-entry` shape governs.
      `approach-drafting`'s stage 1 lists the parts an approach
      file holds, the form of its own output.
      Ideas:
      - a shape adapts: divergence is how it learns
        (`docs/conventions/shapes/` §2, *What a shape is not*), and a shape that never
        changes is finished or unread (`docs/conventions/shapes/`
        §5.2, *A tick, and a difference*).
      - an approach is written without the output's form; a part a
        shape needs is asked for as content, in the approach's own
        words.
      - such an ask carries a fact reference to the shape only for
        the walk; the
        shape says it is read at the gate.
      - a part may be optional, and the shape marks it so.
      - a part considered and empty says "none, because…", so it
        reads differently from one left out.
      - a part never asked for is a fifth kind of difference at the
        gate: the fix goes to the approach, and the output records
        the gap.
      - round 2's FINDING-211: one form told in a skill, a shape
        and a template: the slice record's outline, the backstop at
        the red run, a cost's size, the registry entry's fields, a
        body asserted by path.
      Trigger: `approach-drafting`'s first evaluation, at the
               refinement's close.
      See: devlog 2026-10-20, later; `TODO-CONVERSATION-MEMORY.md` §2, *How an approach and a shape…*.

- [ ] Decide whether approach drafting becomes a convention
      (2026-10-27, the reviewer).
      Context: `approach-drafting.md` is on trial (ADR-0058), held
      word for word in both seats until its evaluation (ADR-0069,
      decision 2). No manual lists it.
      Ideas:
      - one convention for approaches on trial, its artifacts
        `approach-drafting` in both seats and `approach-evaluation`
        in ours.
      Trigger: `approach-drafting`'s evaluation at the refinement's
               close, at its stage 5.

- [ ] Choose whether a manual is called a concept (2026-10-19, the
      reviewer).
      Context: one idea should have one word. The reviewer saw a
      manual as a concept: an idea written down, with sub-ideas,
      and its rules and skills as the convention. "Concept" already
      names the CbC concept and the tiers model's concepts tier.
      Facts-in-sync calls both a description
      (`docs/conventions/facts-in-sync/` §4, *The rule for every description*).
      Ideas:
      - a manual is a concept; its rules and skills, the convention.
      - "description" stays the general word, as facts-in-sync has it
        (`docs/conventions/facts-in-sync/` §4, *The rule for every description*).
      Trigger: a second concept repo, when what a concept is gets
               decided (`docs/models/idea-to-output.md` §5, *A model and a concept*).
      See: devlog 2026-10-19, the redesign's ideas.

- [ ] Decide whether a sweep checks one home after work lands, and
      when (2026-10-22, the reviewer).
      Context: the foundation check walks what derives from a
      changed description at each commit, and `commit-plan`'s close
      sweeps for names a set moved. Nothing looks back over finished
      work to see whether its facts still have one home. Round 2's
      One home kind does it once, for the refinement.
      Ideas:
      - a one-home sweep of its own, or one part of a sweep
        defined as a convention or an approach.
      - other parts such a sweep might hold: regrouping commits,
        if a way is found that breaks no reference (its own item,
        on commits cited by hash).
      - when: after a branch is fast-forwarded; when a branch is
        cut; at a commit plan's close.
      - a missing-context part: each session ends by asking "what
        context was missing that would have helped?", as
        `claude-md-management` does; the answer is one finding in
        that session's devlog entry, from 2026-10-22. The sweep
        reads the findings since the last one and ends each: entry
        file, rule, skill, record, or nothing.
      - how the sweep stands to `retrospective`, a run's look-back
        at its end.
      - `.claude/rules/foundation-check.md`, weighed with this item:
        what is checked at each commit, and what is left to the
        sweep.
      - compare `CLAUDE.local.md` with the settings the manuals
        leave to the operator. A missing setting is not wrong, so a
        sweep reports it; nothing checks it at a session's start.
      - a reference sweep, two kinds: missing, a line relying on a
        fact elsewhere with no reference, found only by reading;
        broken, a reference whose path, number or title no longer
        matches, which a script can check in the form `(<path>,
        §<number>, <title>)`.
      - looking back, defined once: reading a text against what it
        rests on, to find what is out of date, wrong or in
        disagreement. Five acts do it today: the foundation check,
        `commit-plan`'s sweep, a refinement round, an exchange
        reading and the missing-context finding. What a check is
        in the idea-to-output model; when each runs, in its own
        convention.
      Trigger: the refinement's close, once round 2 has swept one
               home and shown what a sweep finds.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §11, *How work is run by agents*, the `claude-md-management` part, and §14.

- [ ] Decide how an item names the items it waits on, and what
      happens when one closes (2026-10-24, the reviewer).
      Context: TODO sorts by horizon and trigger; within a horizon,
      by when added. Some triggers name another item in free prose.
      One named an item that did not exist ("the item on what a
      thing is"), and two waited on the text-division item, with
      nothing to find them when it closed on 2026-10-24. Order
      mattered twice in that item's own work. That day Now held 1
      item, Next 24, Later 33.
      Ideas:
      - a trigger names each item it waits on by quoting its first
        words, a fact reference; several are allowed.
      - at an item's close, grep TODO for its first words; an item
        whose waits are all closed moves up in the same commit.
      - at step-close triage, Next is ordered: ready items first,
        and among them those others wait on; a cycle is split,
        merged or decided provisionally.
      - no re-sort when an item is added.
      Trigger: the next step's close, at its triage.
      See: devlog 2026-10-24, the text-division item.

- [ ] Decide whether a session's end has a home of its own, and
      what it holds (2026-10-22, the reviewer).
      Context: a session's end is spread out.
      Project-recording asks for a devlog entry and a Resume line
      (`docs/conventions/project-recording/` §4, *Devlog — the engineering…*). Two habits
      live only in the agent's own memory: a line per
      delegation, and, from 2026-10-22, one missing-context
      finding. A reader of the repo sees neither.
      Ideas:
      - a convention of its own, by its moment; the sweep its
        twin for work that has landed.
      - a section of project-recording's devlog part
        (`docs/conventions/project-recording/` §4, *Devlog — the engineering…*), since most of it is devlog writes.
      - an approach on trial first (ADR-0058).
      - a rule loaded every session, naming each duty and its
        home.
      - its twin, a session's start: what is read first.
      - a session's end runs the sweep first, then writes its
        devlog entry. Weigh against the missing-context findings,
        which a sweep was to decide in a batch.
      - when the devlog entry closes a piece of work, look back at
        what the new thing touches. Tried once by hand, 2026-10-28:
        all 67 TODO items read against ADR-0070 and ADR-0071, 17
        touched, two of them real gaps (`e219401`, `8d5212d`), the
        rest reminders; too heavy to run after every decision, and
        dropped. The moment is worth a gate; lighter forms to weigh:
        only the items in the decision's area, a fresh agent, or only
        at a big piece of work's close.
      Trigger: with "Decide whether a sweep checks one home after
               work lands", its twin; ADR-0063's kinds now place
               either.
      See: devlog 2026-10-22, later; `TODO-CONVERSATION-MEMORY.md`
      §12, *A session's end*.

- [ ] Decide how commits cited by hash can still be regrouped
      (2026-10-19, the reviewer).
      Context: our `commit-plan` skill regroups a set's commits before
      its close (`.claude/skills/commit-plan/SKILL.md` §4, *Lifecycle*), and a regroup gives them new hashes. This repo cites
      hashes in living text: the refinement's file, TODO, other
      commit bodies. So the refinement's commits up to `ccce6af`
      were not regrouped, and the history keeps every small fix,
      each reviewed as it landed.
      Ideas:
      - cite records, not commits: living text points at a devlog
        entry or a section; hashes only in history.
      - cite at the close: while a set is open nothing durable
        cites its hashes; the close cites the final ones.
      - rewrite the citations with the regroup: a map of old hash
        to new, grepped and replaced in the same rewrite.
      - regroup only on the branch, before main takes it.
      Trigger: the refinement of this repo closes; its rounds read `commit-plan` and the fact reference's form
        (`docs/conventions/facts-in-sync/` §3, *The fact reference*).
      See: devlog 2026-10-19, regrouping.

- [ ] Make the conventions index a full local map (2026-09-30, the
      reviewer).
      Context: its chain shows only the conventions that act in
      sequence during a piece of work. The other nine relate by what
      they govern, read or describe, stated as about thirty fact references across the manuals' *What this does not cover*, and seen
      together nowhere. The local-map rule now exists
      (`docs/conventions/project-recording/` §8.6, *Local maps*, ADR-0045).
      Ideas:
      - all twelve and how each touches the others, derived from those references, built by `visual-comparison`.
      - three links, each with its upkeep: derives
        (`docs/conventions/facts-in-sync/` §4, *The rule for every description*, the foundation
        check), points (one home, the grep at a commit that moves a
        section, a step's close), governs
        (none: a change to a rule that governs other text could
        sweep that text or file the sweep, a rule beside
        `docs/conventions/facts-in-sync/` §4, *The rule for every description*).
      - scenarios as entries into one procedure, the foundation
        check: a manual, a skill or rule, a run's finding. Two
        exits it lacks: the governs sweep, and what must run again
        after.
      - rename "The chain": the idea-to-output model's chain is
        another thing. Not "hand-off", which names the full-auto
        hand-off and a run's hand-off of edited copies.
      Trigger: due — the pair it waited on was made on 2026-09-30.
      See: devlog 2026-09-30, local maps; `cb41ade`.

- [ ] Read run 4 against `dac4dd1`, the run 3 commit it was born
      from (2026-10-15, the reviewer).
      Context: run 4, safe-reservation-2, was born 2026-10-15 by
      hand from run 3's skills, rules and shapes at `dac4dd1` and
      our container at `35edd3f`, and ran on full auto through
      Release. Reading it shows what it changed on top of
      `dac4dd1`, what of run 3's asks it answered, what still has
      to be checked, and what is new. It left twelve lines under
      To the deliverer.
      Ideas:
      - run 3's and run 4's `RETRO.md` read against the
        retrospective skill's form, for a shape (ADR-0054).
      - `temp/RUN-4.md`, run 3's hand-off that started run 4, never
        committed there: what run 4 was told, read for lessons, and
        deleted once read.
      - how run 4 closed its step branches (`run4/step-9` to 11):
        the playbook still ticks "reached main by fast-forward" in
        the gate, which ours dropped (`49d06e6`).
      - whether run 4's birth fired three triggers: "before the next
        birth", shipping `temp/`; "the next birth's Step 3 close",
        the ground-must-be-up rule; "a fourth run deriving
        `.gitignore` by hand", cbc-bootstrap's hygiene.
      - the retrospective puts a "rules in force now" list on top of
        a decisions log kept append-only; run 3 and run 4 both did:
        which side changes.
      - `cbc-framing` writes a status line into the README, where
        the README's form, its header comment, keeps changing status
        in PLAN: how that line lived in run 4.
      - whether run 4 confirmed its plan's steps once framed, as project-recording says a run does
        (`docs/conventions/project-recording/` §9.4, *How*),
        though no skill or step asks it: if not, whether the playbook's
        Framing step should.
      Trigger: the refinement of this repo closes; in a new session.
      See: `f097695`, the kickoff and the message it took;
      `TODO-CONVERSATION-MEMORY.md` §5, *Run 4's reading: two moves…*.

- [ ] Decide whether our own forms become shapes, and whether a
      shape's part can be optional (2026-10-17, the reviewer).
      Context: a shape is read at a step's gate only, so the work
      is not shaped by it (`docs/conventions/shapes/` §3, *One place, read at the gate*). Our own
      forms, a reading's and a manual's, are rules that load when
      such a file is read. They kept that place because this repo
      had no steps; since ADR-0057 it has.
      Ideas:
      - the work's rules keep what must hold while working, such as
        numbers never changed; the forms become shapes.
      - a part a shape names may be optional, where the work does
        not always produce it.
      - Known already as questions, a skill's Gates and the
        playbook's lists, answered in a step's own words.
      - our documents' layouts are shapes too, a case of the shapes
        convention: a manual's, an approach's, a reading's, a
        record's. Five mechanisms hold them today.
      - read at the gate and adaptable like any shape; the approach
        or rule that writes the document carries no layout.
      - what must hold while writing stays a rule
        (`docs/conventions/shapes/` §3, *One place, read at the gate*): a
        manual's section order may; how each part is written may not.
      - `.claude/rules/convention-manual.md` is the manual's form. It
        stands on the conventions convention until this item
        decides; as a shape, it would stand on the shapes convention.
      - a record's form, in its header comment, stays
        project-recording's: it is read when the record is opened,
        while an entry is written, which the shapes manual keeps for rules
        (`docs/conventions/shapes/` §3, *One place, read at the gate*).
        Only `.claude/decisions.md` holds one under another
        convention, agent-arrangement. The open forms are those in
        rules: a manual's, a reading's.
      - a text gets a shape when there are many of its kind and a
        moment to check them: manuals, readings, skills and rules
        may; a record's entries are checked only as they are written.
      - models and the concept get none while nothing of their kind
        recurs: three models share no parts yet, and the concept has
        one form and one home (`docs/models/idea-to-output.md` §5, *A model and a concept*).
      Trigger: run 4's reading, which reads how run 4 lived run 3's
               shapes.
      See: devlog 2026-10-17, our forms as shapes; 2026-10-20,
      later, layouts; `TODO-CONVERSATION-MEMORY.md` §3, *Layouts as shapes*.

- [ ] Try a readability pass, the reviewer marking where text is
      hard to read (2026-10-18, the reviewer).
      Context: a refinement's finding names a broken rule, so text
      that meets the rules stays, even when it could read better
      (`.claude/approaches-on-trial/refinement.md` §2.4, *Read*). Polish
      with no rule has no end: a reader asked to look always finds
      something. The reviewer is the reader the text fails, and asks
      "explain simpler" after most answers with parts.
      Ideas:
      - each mark is a finding; a file is done when the reviewer
        reads it without a stumble.
      - a pattern in the marks becomes a rule in
        `.claude/rules/writing.md`, so a refinement's writing kind
        catches it after.
      - what is read most first: the front door, our skills and
        rules, what ships.
      - the agent polishing alone, only where a rewrite cuts words;
        the reviewer checks each one for drift in meaning.
      Trigger: the refinement of this repo closes.
      See: devlog 2026-10-18, readability.

- [ ] Write a rule that writes a skill or rule from its convention
      (2026-10-17, the reviewer).
      Context: the conventions manual says how a skill or rule is
      written (`docs/conventions/conventions/` §1, *The artifact*), and nothing puts it in front of the
      writer: a manual has `convention-manual.md`, a skill or rule
      has no such rule. An approach on trial writes freely, and its
      pieces are input: what the work needed. When an evaluation
      places one, the lasting form comes from the conventions manual: the manual by
      (`docs/conventions/conventions/` §2, *The manual*), each skill or
      rule from it by (`docs/conventions/conventions/` §1, *The artifact*).
      Ideas:
      - a rule derived from the conventions manual's artifact part
        (`docs/conventions/conventions/` §1, *The artifact*), as
        `convention-manual.md` is from its manual part
        (`docs/conventions/conventions/` §2, *The manual*), on `.claude/skills/`,
        `.claude/rules/` and `delivery/`.
      - a `paths:` rule loads only when a file is touched, and the
        commit is the other moment
        (`docs/conventions/agent-arrangement/` §5.6, *Rules files*).
      - `approach-evaluation`'s placing hands each piece to the
        rule, for an approach of ours and of a run's alike.
      Trigger: the first evaluation that places a piece as a skill
               or rule, at stage 5 of
               `.claude/approaches-on-trial/approach-evaluation.md`.
      See: devlog 2026-10-17, later, the skill rewrite.

- [ ] Rewrite the method's texts plain (2026-10-17, run 3's RETRO
      D2).
      Context: the agent copies the voice it reads. Run 3's records
      came out in the skills' voice, though "explain plainly" was in
      its memory. Plain already: the rules, the shapes, `cbc-slice`'s
      skill and workflow (`2674c03`). Not yet, about 26,000 words:
      `cbc-framing` (8,500), the stack skills (13,800), the concept
      chapters (3,400), readiness (600). A chapter reworded is a
      concept change, editorial unless a meaning moves.
      Ideas:
      - one commit per file; the worked example's two copies as one.
      - the fenced collisions as "nothing dies" kills, as the kill
        shape asks; the example's kill count and reconciliation move.
      - "invariant-shaped", "contract-shaped": "shape" is a defined
        word now.
      - chapter 02's "scope creep wearing a safety costume".
      - `cbc-slice`'s opening states the completion test alone;
        `concept/04-cbc-slice.md` says the test proves a wall, and
        the wall closes the slice.
      - round 2's lessons and layout in these texts, left here by
        the refinement's DECISION-7 and 8: FINDING-223, the harness
        reference's "passes"; 224, the "lived" markers; 227,
        `cbc-framing`'s export section, `infra-establish`'s manuals
        told three times, the worked example's two layouts; 228,
        the walkthrough's parts in its fourth section
        (`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §4, *Stand up the evidence harness*); and 206, the playbook's 12
        citations of run 3's RETRO.
      Trigger: the refinement of this repo closes. Its writing kind
               reads these texts; what round 3 did leaves this
               item, and what is left stays or goes.
      See: devlog 2026-10-17, later, the plain method;
      `TODO-CONVERSATION-MEMORY.md` §6, *The method's plain rewrite…*.

- [ ] Run this repo's retrospective, on trial (2026-10-17, from
      Step 10's gate).
      Context: `docs/conventions/retrospective/`, the deliverer's
      seat, says what it is: both skills run on this repo, from
      `delivery/container/`, and a verdict on whether we hold them.
      Step 10's gate held it until ADR-0057.
      Trigger: the close of the step that runs run 5's birth.
      See: ADR-0057, decision 4.

- [ ] Decide whether a delivery checks its paths against the run's
      own files (2026-09-30, the reading of run 3).
      Context: our shipped `.claude/rules/shapes-lifecycle.md` sat
      at run 3's own rule's path, so the take landed ours over the
      run's. Two checks in the exchange miss it: one checks only that no path
      is claimed by two of our groups (`docs/conventions/exchange/` §3.4, *Every shipped file is…*);
      the take's diff sees that a file differs, not whose it is
      (`docs/conventions/exchange/` §4, *The take*).
      Once so far; checked by hand at `e6538f6`: no staged path was new.
      The method's four shapes sit at run 3's own `.claude/shapes/`
      paths (ADR-0052); the next birth is where they first land.
      Ideas: in `exchange-deliver`, the staged paths against the
             run's files that are not at its pin.
      Trigger: the next delivery that ships a path new to the run.
      See: devlog 2026-09-30, the delivery to run 3.

- [ ] Read the frozen CLAUDE template's stance bullets against a
      full run's derived entry file (2026-09-06, the user).
      Context: the template's walk-1-era method half is frozen at
      `docs/baselines/claude-md-template-v1.md`. No birth can judge
      the stance bullets — only a run that has framed and built.
      Three ways: the run's `CLAUDE.md`, frozen v1, and
      `cbc-derived-claude-walk1.md`; harvest re-enters the template
      only from that reading, each line traced to the run. Run 3
      has had no Release; run 4 released the same project, so its
      entry file is read, run 3's beside it.
      Trigger: run 4's reading.
      See: devlog 2026-09-06 (the template re-cut).

- [ ] Sort `docs/baselines/` by kind (2026-09-23, ADR-0035
      decision 6).
      Context: trial evidence is withheld so a later derivation
      measures independence; a shape is withheld only until a
      gate. A wrong move destroys a measurement that cannot be
      remade, so this is its own reading, not a tidy-up. The
      Spring slice reference opens once, at a run's Release
      (ADR-0033); run 3 has had no Release, and run 4 had one.
      Trigger: run 4's reading, where the Spring slice reference
               opens.
      See: devlog 2026-09-24.

- [ ] Read what run 5's first slice gate found against the
      evidence-test shape (2026-10-08, the reading of run 3).
      Context: the shape ships with the method since ADR-0052, read
      only at the gate. A newborn writes its first tests without it,
      and its first slice's close reads them against it: the
      differences are the measurement. Run 4 held run 3's shape from
      birth, so run 5 is the first clean one, unless it reads the
      shapes at birth (the item on `.claude/shapes/`). `cbc-slice`
      holds most of its lessons, so tests from the skill alone may
      meet it.
      Trigger: run 5's first slice closing.
      See: devlog 2026-10-08; and 2026-10-10.

- [ ] Watch whether the next newborn adds the ground-must-be-up
      rule to its entry file unasked (2026-09-04, ADR-0013's scope
      boundary).
      Context: the entry-file stub teaches this fill and no skill
      prompts it. Run 3 answered the bootstrap half — its entry
      file now states only what never changes. At establish it
      added no local rule, at no visible cost; a costly miss would
      be evidence for a skill line.
      Trigger: the next birth's Step 3 close.
      See: devlog 2026-09-12, later.

- [ ] Decide which ideas here are models (2026-10-24, the
      reviewer).
      Context: three models exist: agent, tiers, idea-to-output. A
      model comes from a convention whose idea is general enough to
      be used elsewhere (`docs/models/idea-to-output.md` §4.2, *Up, work to an idea*). The
      text-division item held candidates, left open by ADR-0063.
      Ideas:
      - one home: facts, their home, fact references, and how a
        disagreement between linked texts is settled.
      - the deliverer and the run, with seats.
      - a shape: the shapes manual says what one is
        (`docs/conventions/shapes/` §1.1, *What it says*, and §2, *What
        a shape is not*).
      - records: what a record is, a form and its entries; what a
        set of records answers; how each seat adapts it, as the
        refinement's DECISION-12 map shows. Weighed against the idea-to-output model, which holds part of
        it (`docs/models/idea-to-output.md` §2, *The kinds*).
      Trigger: the refinement's close, once facts-in-sync, whose
               subject is the first idea, has lived through round 2.
      See: ADR-0063; `30eb42e:TODO-CONVERSATION-MEMORY.md` §1.

- [ ] Decide whether a model ships to a run (2026-10-24, the
      reviewer).
      Context: no manual and no model ships
      (`docs/conventions/exchange/` §3.2, *What goes*). A manual may now stand on
      a model, as agent-arrangement does; a run gets the files made
      from it, never the reasoning above them.
      Ideas:
      - the tiers model's method layer holds the models in the
        concept repo "until three repos have lived".
      Trigger: a run's reading finds a convention misread for want
               of the model behind it.
      See: ADR-0063.

- [ ] Decide whether a model may be written for one convention
      (2026-10-23, the reviewer).
      Context: the text-division item had a model only where several
      manuals share an idea. The reviewer asked to weaken that: a
      model for one convention, "to see general idea behind that
      convention". Idea-to-output has a model come from a convention whose idea is
      general enough (`docs/models/idea-to-output.md` §4.2, *Up, work to
      an idea*).
      Trigger: a convention whose idea another repo could use, with
               no second manual sharing it.
      See: ADR-0063; `30eb42e:TODO-CONVERSATION-MEMORY.md` §1.

- [ ] Decide what "rule" names, and give the agent's rule files a
      name of their own (2026-10-25, the reviewer).
      Context: "rule" has four senses in 779 uses across living
      text. A file under `.claude/rules/` that loads into the agent:
      91 mentions of the path, 54 of "skills and rules". A numbered
      line inside one, "one-home rule 3": 17. What a text says must
      be done, "the bump rule". In a run, a rule the built system
      keeps, "one row per rule": 5. `docs/glossary.md` defines none.
      The conventions manual's artifact part is about the files
      (`docs/conventions/conventions/` §1, *The artifact*), yet its
      "A rule is one sentence in the imperative" means a line.
      Ideas:
      - "agent rule" for the file, plain "rule" for what must be
        done; an agent rule holds rules, numbered.
      - the run's sense says "invariant", the method's own word.
      - the same check for other words with several senses: "model"
        (ours, and the Claude model a delegation names), "step"
        (PLAN's, and a numbered step inside a section), "run" (the
        repository, and the verb round 3 already lists).
      - `.claude/rules/convention-manual.md` reads as a convention's
        manual; it is the rule for a manual's form. About 5 living
        references would move.
      Trigger: round 3's rule check, so its Writing kind reads
               against the chosen words.
      See: devlog 2026-10-25, evening; `TODO-CONVERSATION-MEMORY.md`
      §19, *What "rule" names*; `163767f`.

- [ ] Decide whether a standing full read looks for missing fact
      references, and for references pointing down (2026-10-27, the
      reviewer).
      Context: a line that relies on a fact written elsewhere and
      carries no fact reference is found by no grep and no walk. The
      check of ADR-0070 asks it of each new or changed
      line at the commit. Only the refinement's rounds read the whole
      repo for it today: their Dependencies kind, which round 2's
      close read ran with seven agents and 52 findings.
      Ideas:
      - its own piece of work: not the sweep, a grep at a plan's
        close, and not session end, which only records.
      - read by foundation: one agent reads a description beside
        every file built on it, and asks of each line whether it
        relies on a fact and says where.
      - one kind per agent; other kinds may share the read, each
        with its own agent.
      - it reads against the reference's form
        (`docs/conventions/facts-in-sync/` §3.1, *What it is*) once the settled form is
        written there.
      - a second kind for the same read: direction (ADR-0071). A
        line in a model or a manual that relies on a lower text is
        found by no grep either: telling relying from naming takes
        a read. Done by hand on 2026-10-28: the three models and 67
        manual paragraphs, 6 found, 3 of them references left at a
        fact's old home when it moved (`b7c17ae`).
      Trigger: a read finds a missing fact reference in text written
               after the per-commit check is in force, or a reference
               pointing down in text written after ADR-0071.
      See: devlog 2026-10-28; `TODO-CONVERSATION-MEMORY.md` §21, *A full read for missing fact…*.

- [ ] Test fact references and foundations as a whole: name every
      scenario a change brings, and check each still holds
      (2026-10-28, the reviewer).
      Context: two means keep facts in place. A grep finds every line
      that names a path, number, title or id. Only a read tells
      whether that line, its paragraph or its whole file still holds
      after the change. One home rests on both: the grep finds the
      line, the read keeps its logic. ADR-0070 changed the reference
      and the rename grep, and no one has walked every scenario
      through both, end to end.
      Ideas:
      - the scenarios: a fact changed at its home; a section renamed,
        renumbered or retitled; a file renamed; a fact moved to a new
        home, a placed approach among them; a foundation changed; a
        derived file changed against its foundation; a retelling
        whose host is itself a source; a run's id whose home changes;
        a shipped CBC line when our manual changes; a fact stated
        only in history; a line with no fact reference.
      - for each: what finds it, a grep or a read; which rule says
        so, by fact reference; what is re-read, the line, its
        paragraph or the whole file; what could still slip.
      - (a) on paper: a table of the scenarios against the rules.
      - (b) a drill on a throwaway branch: each scenario made for
        real, the check run, and what it found compared with a full
        read.
      - (c) agents: one per scenario, or one trying to make a change
        slip past the check.
      - (d) a kind of its own in the refinement's last read.
      - what a scenario finds missing becomes a finding or a TODO
        item; the test changes no rule itself.
      Trigger: the refinement closes.
      See: devlog 2026-10-28; ADR-0070;
      `TODO-CONVERSATION-MEMORY.md` §22, *Testing fact references…*.

- [ ] Look again at where a run learns how to treat a skill's
      template (2026-10-28, the reviewer).
      Context: four shipped files told the off-template rule in
      their own words, and drifted: deviate from a skill's template,
      derive from what it implements, log it, expect a harvest,
      never bend a decided constraint to fit it. On 2026-10-28 it went to the exchange
      (`docs/conventions/exchange/` §5.8, *A skill's template is filled…*) and the run's `delivered-copies.md`, chosen on
      one reading, with no run having lived it.
      Ideas:
      - (a) one skill states it; the others point.
      - (b) delivered copies: the exchange
        (`docs/conventions/exchange/` §5.8, *A skill's template is filled…*) and the run's
        `delivered-copies.md`; today's choice.
      - (c) each skill's template states it in its own header,
        where a run meets the choice.
      - (d) a shape for a skill's templates.
      - weigh each by maintenance, readability, future-proofing and
        complexity.
      - check that every manual and shipped text that speaks of a
        skill's templates agrees with the exchange (`docs/conventions/exchange/` §5.8, *A skill's template is filled…*) and
        `delivered-copies.md`,
        and that `delivery/README.md` and ADR-0008 still match.
      - check that each use says whose template it is: a skill's,
        repo-hygiene's, or a record stub. Of 97 uses in living text,
        only some say.
      Trigger: a run reading that shows a run deviating from a
               template, or a second stack's templates arriving,
               whichever comes first.
      See: devlog 2026-10-28; ADR-0070.

- [ ] Write a rule that a word with more than one meaning here
      carries its subject at every use, and list those words
      (2026-10-28, the reviewer).
      Context: "template" names a skill's template, repo-hygiene's
      templates, a record stub and the plain sense, in 97 uses that
      only sometimes say whose. Verbs collide too: "fill", "take",
      "stage". Writing rule 8 covers a word's first use; a fact
      reference lands a reader mid-file, past it. Taken in talk: a
      rule for every use, for the words a list names, so a grep for
      a listed word without its subject finds the misses.
      Ideas:
      - how the list is built, still open:
        - (a) one glossary entry per word, its bare sense first,
          then a sense per subject beneath it;
        - (b) the writing rule defines "a word with more than one
          meaning here" and holds the list itself;
        - (c) the rule defines the term, and a glossary group lists
          the words, each pointing at the rule.
      - candidates: template, stage, step, fill, master, rule, take,
        tag, skill, log; measure each word's uses and senses before
        the list is written. "Log" in what ships means the decisions
        log, git's log, "the run's log" with no record named, and a
        verb.
      - "a skill's template" reads as one a skill uses as much as one
        it holds; the other name that fits all 11 is "copy-and-fill
        template", as shipped text says "copy-and-fill master".
      - collisions with git and Claude Code count: stage, master,
        tag, skill.
      - "Decide what 'rule' names" may become one entry in the list.
      - the run's seat: a run's own collisions, such as "fact"
        against the `FACT-` tags, and whether the shipped
        `writing.md` takes the rule.
      Trigger: round 3's rule check, so its Writing kind reads
               against the rule.
      See: devlog 2026-10-28; `TODO-CONVERSATION-MEMORY.md` §23, *A word with more than one…*.

- [ ] Decide how a section title is written (2026-10-28, the
      reviewer).
      Context: since ADR-0070 a fact reference carries its section's
      title, so a title is read wherever a line points at it, not
      only at its section. Nothing says how one is written. Of 253
      numbered titles, some state a point (*A rename is grepped at
      its commit*), some are labels (*The entry file*), some a lone
      word (*What*, *Why*); 32 run past the 30 characters a
      reference keeps, and are cut.
      Ideas:
      - its home: the writing convention, how a text reads, with
        both `writing.md` following.
      - a statement or a label: a statement says the point and
        changes with it; a label is stable and says less.
      - 30 characters at most, so no reference is cut.
      - a title names its subject, as the rule for a word with more
        than one meaning asks; a lone *What* tells a reference
        nothing.
      - the manual form's fixed headings, such as *What it is for*,
        stay the form's.
      - a retitle after the reference rewrite is a scripted replace, since a rename's grep covers titles
        (`docs/conventions/facts-in-sync/` §3.3, *A rename is grepped…*).
      Trigger: round 3's rule check, so its Writing kind reads the
               titles against it.
      See: devlog 2026-10-28; ADR-0070.

## Later / someday

- [ ] Release concept v2 (2026-10-17, from PLAN's Step N).
      Context: so a stranger, or future-you, can read, cite and copy
      from this repo without the archive. Four items of its own:
      a CHANGELOG entry for the release; README true for a
      stranger; `docs/models/` checked against the repo, since
      `CLAUDE.md` sends a stranger there; known issues filed here.
      PLAN held it until ADR-0057.
      Trigger: the reviewer names it, after the step that runs run
               5's birth closes.
      See: ADR-0057, decision 4.

- [ ] Decide what our CHANGELOG tracks, and how the stub asks it
      (2026-10-21, the reviewer).
      Context: ADR-0003 (2026-08) made it the concept's log, for
      runs pinning a version; ADR-0039 decision 9 kept conventions
      out. Since v1 (2026-08-28), about 1,350 commits added the
      conventions, the container, the models and approaches on
      trial, and none is logged. A run pins a commit and cannot read
      our changelog: its readers are us and a stranger after a
      release. `README.md`, `CLAUDE.md`'s records table and the
      changelog's header comment still name the pinners.
      Ideas:
      - track by exclusion: all but the records, our agent setup and
        `temp/`, so a new kind of thing is tracked from its first
        commit.
      - the concept version stays, for citation; the repo gets a
        release number of its own, each naming the concept version
        it holds (amends ADR-0003 and ADR-0039 decision 9).
      - one baseline entry at v2: what each group holds now, pointing
        at the ADRs, not rebuilt from commits.
      - a check at each step's close: every change outside the
        excluded paths has an entry, or is marked editorial.
      - what is tracked is read again when the repo grows a new kind
        of thing.
      - the stub gains a `Tracks:` line beside `Versioning:`, decided
        at Framing, with when to revisit it; the lesson goes in project-recording's changelog part
        (`docs/conventions/project-recording/` §6, *CHANGELOG.md*).
      - a fill sets a CbC run's two lines at birth, as the playbook
        fills its plan; we fill ours in place
        (`docs/conventions/project-recording/` §9.4, *How*, step 1).
      Trigger: the release item above opens; its CHANGELOG entry
               needs the answer.
      See: devlog 2026-10-21; `TODO-CONVERSATION-MEMORY.md` §4, *What our changelog tracks*.

- [ ] Decide how the worked example's two copies are kept: checked
      by a diff, or made one (2026-09-17, and 2026-10-15 for the
      check).
      Context: one document, byte-identical in `cbc-framing`'s and
      `cbc-slice`'s `references/`. `.claude/rules/one-home.md` rule 5
      asks a check where two copies cannot be avoided (ADR-0053);
      today they are compared by hand at each edit, and were
      identical on 2026-10-15. Made one, `cbc-slice` could not be
      installed without `cbc-framing`.
      Ideas:
      - a diff of the two in `exchange-deliver`'s gates, since a
        delivery is when the copies leave.
      - one document, once one skill is wanted without the other.
      Trigger: the two found different, the worked example's next
               edit, or a reason to install one skill without the
               other.
      See: devlog 2026-09-17, later.

- [ ] Decide whether `infra-establish`'s contract carries a paragraph
      on the store's facility (2026-09-17, never-oversold).
      Context: run 3 wrote one at Step 3 — the ways its store makes
      two writers disagree — because the skill is silent on it. We
      held it rather than declined: one instance is not a shape.
      Run 3 says SL-2 did not lean on it; SL-2 faces no race.
      Run 4 rebuilt run 3's problem from run 3's copies, so it
      cannot be the second run.
      Trigger: run 5 reaching the same gap unprompted.
      See: devlog 2026-09-17, later still.

- [ ] Move the skills' `foundation` to concept v2 at the release
      (2026-10-08, ADR-0048).
      Context: the method's skills say `foundation: concept v1`.
      ADR-0048 makes the next release v2, and `cbc-slice` and
      `cbc-framing` already state its ranking.
      Trigger: the release that names v2.

- [ ] Decide whether a rule can be delivered on trial, as a shape
      can (2026-10-08, never-oversold).
      Context: a shape reaches a run but binds nothing until a
      gate reads it (ADR-0052); a rule learned in one run is in
      force in the next from its first step. Run 3 asked after
      offering its evidence-test shape as a rule. Held: the question
      is real only once there is a rule we would deliver that way.
      Run 3's RETRO D4 says a trial names the close that judges it,
      and the step form says so since `0cdc50c`.
      Ideas:
      - ship it as an approach on trial: in force only when a step
        takes it as its approach, and each use comes back as a note
        (ADR-0058).
      Trigger: a rule we would ship that one run alone has lived.
      See: devlog 2026-10-08.

- [ ] Give the method a glossary (2026-10-08, never-oversold).
      Context: its words are defined where each is first used;
      tripwire, witness, fold, fence and possession appear only in
      the skills, never in the chapters a reader starts from, and
      the wall's own check joins them. Whether a list beside the
      chapters, or a chapter's, is open. Since `fbd1c5e` each run
      starts its own glossary at framing; the method has none.
      Trigger: Release's README item, where a stranger first needs
      the words.

- [ ] Number the concept chapters' sections (2026-09-30).
      Context: their `##` headings are unnumbered, and nothing points
      into a chapter's section today. The chapters are the canonical
      text every run holds a copy of, so numbering them would change
      every copy for no reader yet
      (`docs/conventions/facts-in-sync/` §3.2, *A section's parts are numbered* numbers by form).
      Trigger: the first fact reference that needs a section of a
               chapter.
      See: devlog 2026-09-30, numbered parts.

- [ ] Does the playbook need a convention of its own? (2026-09-29,
      the reviewer)
      Context: project-recording describes it
      (`docs/conventions/project-recording/` §9, *Playbook — the cross-project…*), and one playbook exists, the CbC run's. It is not a shape: a shape is form, never content
      (`docs/conventions/shapes/` §1.1, *What it says*, and §2, *What a
      shape is not*), and a filled-in template is not one; a
      playbook is content, copied and filled at birth.
      Ideas: a convention of its own, split from project-recording's playbook part
        (`docs/conventions/project-recording/` §9, *Playbook — the cross-project…*).
      Trigger: a second typed playbook.
      See: devlog 2026-09-29, the PLAN pass.

- [ ] Filter a maintainer's container out of this repo, when one is
      needed (2026-09-29, the reviewer).
      Context: `delivery/container/` is the run's derivation of the
      conventions, and this repo's own files are the deliverer's
      (ADR-0042). No second maintainer repo exists, so no
      maintainer's container does either.
      Ideas: filter this repo — keep the functionality and layout,
             drop this concept's own content.
      Trigger: a second maintainer repo.
      See: devlog 2026-09-29, the split.

- [ ] Move the tiers model to the garden (2026-09-30).
      Context: it maps the workspace, and the workspace has no home:
      the garden stays a plain folder until a second concept repo
      exists (`docs/models/tiers.md` §2.2, *Concepts*). Until then it lives here,
      beside the agent model; `docs/models/` stays.
      Trigger: a second concept repo.
      See: devlog 2026-09-30, the tiers model.

- [ ] Name the discipline "lived is evidence, not master text"
      (2026-09-04, the user).
      Context: the records table says what goes in a README, the
      entry file and the internal records, and it slipped twice in
      one session the same way — lived newborn text adopted on
      provenance, unaudited against the target record's rule.
      Trigger: a third slip — then the rule gets its guard.
      See: devlog 2026-09-04.

- [ ] Decide whether a receiver needs a rule for claims it cannot
      check (2026-09-18).
      Context: the sending half is in force — a note says when it
      claims what the receiver cannot check. Two receivers, the
      handbook and never-oversold, took such claims as attributed
      rather than checked, unprompted; a rule now would tell them
      to keep doing what they do.
      Trigger: the first receiver that acts on an unmarked
      uncheckable claim as fact.
      See: devlog 2026-09-18, later still.

- [ ] Decide whether cbc-bootstrap points at the Spring hygiene
      parts, or "grow, never overwrite" stands (2026-09-18).
      Context: the `.part` files under
      `docs/conventions/repo-hygiene/templates/java-spring/` are pointed at by
      nothing, and three runs derived `.gitignore` by hand. They
      are spring-postgres (ADR-0029 decision 7) and move with the
      answer; until then they sit against decision 5's beside-it
      rule, an exception the ADR records. The walk named the wider
      gap: nothing ships a stack overlay, and a blind run cannot
      fetch one.
      Ideas:
      - round 2's FINDING-203: `cbc-bootstrap`'s skill and its
        walkthrough both tell a run to add a stack overlay below
        each hygiene file's marker, and no file ships one. The
        skill could point at the walkthrough's step 2 instead.
      Trigger: cbc-bootstrap's hygiene step next opened, or a
      fourth run deriving `.gitignore` by hand.
      See: devlog 2026-09-18.

- [ ] Weigh three candidate rules for what makes a note land
      (2026-09-17, the handbook's reply).
      Context: the only outside reading of our note-writing. An
      opening ordered by weight let them plan their commit split
      from four lines; "we are not asking you to write the
      convention" removed a pressure we did not have to name; all
      four additions were usable with no follow-up question. None
      of the three is in the exchange manual.
      Trigger: the note that answers run 5's reading, before it is
               written.

- [ ] Decide whether an overtaken reading still owes the run a note
      (2026-09-30, the reading of run 3).
      Context: the reading of 2026-09-24 was overtaken on 09-26 and
      deleted without one, so what run 3 had addressed to us since
      its pin had no verdict until the reading of 2026-09-30 read it
      again — three edits to copies, ten asks and offers.
      The exchange closes an overtaken reading
      (`docs/conventions/exchange/` §6.4, *A reading closes two ways*)
      "the same way", one pass over its items, and is silent on the note every read ends with
      (`docs/conventions/exchange/` §6.6, *Every read ends with a note*). Once so far.
      Ideas: the overtaken reading sends a note: read, asks open.
             the next read goes back to the last note's read-through.
      Trigger: the next reading overtaken.
      See: devlog 2026-09-30, the delivery to run 3.

- [ ] Name when a run is read (2026-10-01, the working draft).
      Context: a reading happens when the reviewer says. A hand-off
      arriving, a step closing at the run, a calendar — none is
      named, so a reading happens when someone remembers, and both
      sides drift further from the pin while it waits. Run 3's RETRO
      D24 names one moment: after a run's apply step, so its
      decisions arrive tried. Run 3's next step waited on our note:
      recording the read-through was on its path (2026-10-18).
      Trigger: a hand-off found waiting for a reading nobody called.
      See: devlog 2026-10-01.

- [ ] Decide how readings work with more than one live run
      (2026-10-01, the working draft).
      Context: the rules for reading and working a reading are
      written for one run. Two live runs mean two readings, and
      their items may be the same finding twice.
      Trigger: a second live run.
      See: devlog 2026-10-01.

- [ ] Say once that a reading's decisions are the reviewer's
      (2026-10-01, the working draft).
      Context: the agent proposes and builds, the reviewer settles —
      every reading has gone so, and nothing says it. Probably the
      arrangement's to say, not the reading's.
      Trigger: an agent found settling what was the reviewer's.
      See: devlog 2026-10-01.

- [ ] Watch whether the worked example anchors a run's framing
      (2026-09-17, the user).
      Context: an invented order service with an idempotency slice
      could steer a run toward that shape. No evidence in three
      runs; one weak signal — the example and run 3 both land on
      one area.
      Ideas: a second example on another shape, keeping this one.
      Trigger: the next framing read on a differently shaped
      problem.
      See: devlog 2026-09-17, later.

- [ ] Could a project need its own mould of a shipped skill?
      (2026-09-17, the user)
      Context: a skill is the same for every project; what one
      project needs goes in its own records, never the copy. The
      gap: an edit the project needs in the skill's behaviour,
      declined.
      Ideas: an overlay file per skill beside the copy — run 3's,
             which it declined to build.
      Trigger: declined-but-needed becoming a pattern.
      See: devlog 2026-09-17, later.

- [ ] Add a rung for guarantees held by absence to the enforcement
      hierarchy (2026-09-14, run 3's SL-1).
      Context: no process clock, no state outside the store — nothing
      to observe at runtime; its wall is a rule on the compiled
      classes. Run 3 asks for a rung between "single validated entry
      path" and "code review". It met it again in SL-2 and SL-4, and
      run 4 rebuilt the same problem from run 3's copies, so neither
      is a second run. The hierarchy lives in
      `concept/02-guarantees-and-walls.md` and both cbc-slice files: a
      concept change, with an ADR and the version question (ADR-0003).
      Trigger: run 5 meeting an absence guarantee.
      See: devlog 2026-09-15; and 2026-10-10.

- [ ] Decide whether the worked example shows a slice that
      inherits its wall (2026-10-10, the reading of run 3).
      Context: run 3's SL-4 built no wall — SL-3's one statement
      already held its invariant — and owed proof only, against its
      own instance killed mid-write and an outcome its caller cannot
      know. The worked example has no such slice and no such
      adversity. One run's slice, so held.
      Trigger: a second run whose slice inherits its wall.
      See: devlog 2026-10-10.

- [ ] Decide whether `cbc-slice` says a red removes the backstop too
      (2026-10-10, the reading of run 3).
      Context: the skill says a wall that already stands is removed on
      the working tree for its red. SL-4's red as signed stayed green:
      the store's check on the units held caught both orders, and the
      evidence went red only with the one transaction and that check
      both gone. Run 3 revised its plan for it and proposed no edit.
      Since `2674c03` the skill asks the red run to note whether each
      backstop was seen or is unproven; removing it is not asked.
      Trigger: a second slice whose red a backstop holds green.
      See: devlog 2026-10-10.

- [ ] Decide whether a second service family earns its own
      walkthrough (2026-08-28).
      Context: beside `postgres-setup-walkthrough.md`; the test is
      long, sequenced, likely to recur.
      Trigger: a run first standing up a non-PostgreSQL service.

- [ ] Revisit "backend" in the skills' description lines
      (2026-09-06).
      Context: kept — it names the toolkit's honest scope, and
      every run so far is one. The practice skills' bodies
      (compose, Flyway, Spring Boot) are backend-born too.
      Ideas: start with the description lines.
      Trigger: the first non-backend run.
      See: devlog 2026-09-07.

- [ ] Tune the practice skills' trigger descriptions (2026-08-28).
      Context: unoptimized since import (archive STATUS).
      Trigger: a skill under- or over-firing in a run.

- [ ] Consider a held-insight tier in the harvest discipline
      (2026-08-29, safe-reservations' close).
      Context: its flow-back split sure adoptions, landed in the
      masters, from insights held as evidence with a named
      promotion path. ADR-0007 has only the first tier; adding
      one is an amendment, decided deliberately.
      Trigger: a reading holds an insight it cannot land yet and
      has nowhere to put it.
      See: devlog 2026-08-29 (framing shape decided).

- [ ] Harvest the projection law's deeper lifecycle when a run
      lives it (2026-08-30).
      Context: public docs beyond the README, earned by substance
      and refreshed at slice closes — seen in the safe-reservations
      node's projection model, never lived by a run of ours.
      Trigger: a run first reaching the milestone that fires it.
      See: devlog 2026-08-30 (doc projection checked).

- [ ] Decide how a run learns that the rule for taking deliveries
      changed (2026-10-18, the reviewer).
      Context: a run takes a delivery under the `delivered-copies.md`
      it holds, so a delivery that changes that rule is taken under
      the old one. The rule cannot travel alone: one pin covers every
      copy (`docs/conventions/exchange/` §2.2, *The run*). Run 3's copy lacked
      `4de6ba2`'s shapes; no files went, so it never acted.
      Ideas: the note's "why it matters" names a change to the rule
             first, so the run takes it knowingly.
      Trigger: the first files delivered to a run still building,
               with `delivered-copies.md` changed since its pin.
      See: devlog 2026-10-18.

- [ ] Decide how an edit or a new text is shaped, line width
      included (2026-10-25, the reviewer).
      Context: 72 characters is written only for a commit body
      (`.claude/skills/commit-messages/SKILL.md`). The agent applied it to Markdown, and
      rewrapped paragraphs to fit: diffs grew, and a scripted rewrap
      broke structure twice. 685 lines in 70 of the 171 Markdown
      files run past 72, tables aside. Nothing says how an edit
      keeps or changes the shape of the text it touches.
      Ideas:
      - an edit keeps the logic of the part it changes, and improves
        it where a better logic exists.
      - no width at all; a width for `*.md` in `.editorconfig`,
        shown as a guide; or a change about as long as what it
        replaces. A limit only if nothing better is found.
      - a home: the writing convention, if shape is how a text
        reads; repo-hygiene's `.editorconfig`, if it is a width; or
        a convention of its own for editing.
      Trigger: a diff the reviewer finds bigger than its change, or
               round 3's rule check, which reads the writing rules.
      See: devlog 2026-10-25, the agent binding.

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)

- The postgres image tag floats (2026-08-28). The ground template
  and the harness reference both say `postgres:17`, so they can
  pull different minors at different times. Accepted: the shared
  major is a deliberate coupling, and no run has hit drift.
  Revisit: a run's first minor-drift surprise — then pin both
  tighter, to a full version or a digest.
