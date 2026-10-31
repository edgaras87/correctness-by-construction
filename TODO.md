# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a Plan Step. Prune "Later" ruthlessly: deleting an
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
     §5.4, How an item is written).
     foundation: the project-recording convention -->

## Now (due while the open Plan Step runs)

## Next (each due at its trigger)

- [ ] Read CBC Run 6, `checkout`, by `exchange-read` (2026-10-29, the
      reviewer).
      Context: CBC Run 6 ran on full auto through its Release, Step 14,
      and closed a Step 15 after it: 254 commits, 7 slices, tag
      `v0.1.0`. Its birth Plan Step stopped before its close, so its
      Run Reading waits.
      Trigger: the refinement's close, or the reviewer's word.
      See: devlog 2026-10-29, morning.

- [ ] Unlock the folders locked for CBC Run 6 (2026-10-29, the
      reviewer).
      Context: CBC Run 6 must not read another repository, and a
      `Read` deny rule does not stop a shell. So, before its birth,
      twelve entries in `~/IdeaProjects` were made unreadable,
      `chmod 000`: `archive`, `cbc-pure-run`, `cbc-pure-run-2`,
      `cbc-pure-run-3`, `cbc-pure-run-4`, `cbc-pure-run-5`,
      `checkout-system`, `idempotent-orders`, `order-placement`,
      `safe-reservations-v1`, each 755 before; and
      `checkout-system-first-prompt.md`,
      `safe-reservation-briefing.md`, each 644 before.
      Trigger: the reviewer's word, or before CBC Run 5's lessons Plan Step
               resumes, since it reads CBC Run 5. CBC Run 6's Release,
               the first trigger, has passed; the reviewer kept
               the lock for now.
      See: devlog 2026-10-29, night.

- [ ] Write `exchange-birth` while a birth runs (2026-09-26, the
      reviewer).
      Context: written from the exchange manual, as `exchange-read`
      and `exchange-deliver` were, keeping the Pure Seed's intent — it
      delivers everything and decides nothing. Then *What this does
      not do* in `.claude/skills/exchange-deliver/SKILL.md` points at
      it, `pure-seed.md` goes, and ADR-0016's procedure of record
      moves. CBC Runs 5 and 6 are born by the Pure Seed, to keep their births
      small.
      Ideas: first-time work on our Convention Seat, so an Approach on Trial
             drafted by `approach-drafting` (ADR-0058).
      Trigger: the birth after CBC Run 6's.
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
      of them, and 2 changed the answer. CBC Run 5 tries it first, from
      its Run Hand-off.
      Ideas:
      - a bar for "meaningful": it changes a wall, a test's
        adversity, or removes a part; rewording is not enough.
      - the better way on a `try/` branch, compared, the loser kept.
      - a cap on its cost, so no plan doubles by habit.
      Trigger: CBC Run 5's Run Reading.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §9, *A commit plan's look-back…*.

- [ ] Decide whether the concept, the conventions and the
      Approaches on Trial keep examples (2026-10-21, the reviewer).
      Context: CBC Run 4 read CBC Run 3's real kills in the Output Shapes' examples
      at birth, and its framing copied them in places (ADR-0061).
      The method's worked example, 271 lines in both `cbc-framing`
      and `cbc-slice`, is an order service that weighs "Orders are
      never lost AND payment always completes"; the concept's
      chapters, the slice workflow, the playbook, `writing.md` and
      the stack's references hold smaller ones. CBC Run 5, event
      tickets, is born with all of them.
      Ideas:
      - examples stripped to a description of what must be done.
      - examples kept, drawn from a domain no CBC Run will build.
      - examples kept where a reader learns, gone where a CBC Run acts.
      Trigger: CBC Run 5's Run Reading.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §10, *Examples in the concept…*.

- [ ] Decide how work is run by agents: delegation, model and
      effort by kind of work, forks or fresh agents, new challenges
      and look-backs; and what the agent's setup holds, and where
      that is recorded (2026-10-22, the reviewer).
      Context: nothing here says when a lead agent hands work to
      others, with which model and effort, or whether a fork or a
      fresh agent takes it. On 2026-10-21 the agent sent 3 readers
      to CBC Run 4 and 8 to the close read on its own judgement; CBC Run 4
      changed model mid-run with no record of why. `/doctor`,
      2026-10-22: 69 general-purpose agents in 29 days, none given
      a model, so all on Opus: 11% of a week's usage. New challenges
      have `approach-drafting`; looking back has a trial in CBC Run 5.
      Ideas:
      - low effort to read and collect; the highest to find the
        options; medium or high to implement and summarise.
      - a lead agent fans out readers and keeps the decisions.
      - each delegation leaves one line: the kind of work, the
        Idea Model, the effort, whether it paid.
      - an Approach on Trial before any convention (ADR-0058); a
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
        `CLAUDE.local.md`, the agent's memory, or an Agent Rule. On
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
        setting (`docs/conventions/agent-arrangement/` §3.7, *`CLAUDE.local.md`*). Refinement Round
        2's FINDING-194 found it again.
      - "never rewrite main across 35edd3f" lives only in the
        agent's memory, unseen by any reader of the repo. Its
        failure is not noticing the moment, a rebase: a Local Rule
        for our `CLAUDE.md` (`docs/conventions/agent-arrangement/`
        §2.4, *How the entry file is written*)?
      - what survives what, lived 2026-10-30: a model switch inside a
        session keeps the transcript; an agent the usage limit stopped
        keeps its transcript and resumes by `SendMessage`; a new
        session keeps the repo, the devlog's Resume line and the
        user's memory files only. The Agent Model §6 states the rule;
        the binding, agent-arrangement §5, would hold the mechanics.
      Trigger: CBC Run 5's Run Reading, with the lines gathered by then.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §11, *How work is run by agents*; `.claude/decisions.md`, 2026-10-22, the account skills.

- [ ] Evaluate `auto-run`, the Approach on Trial for preparing a
      full-auto CBC Run (2026-10-22, the Plan Step that birthed CBC Run 5).
      Context: drafted and used once, for CBC Run 5
      (`.claude/approaches-on-trial/auto-run.md`, its use note). Its
      open questions are CBC Run 5's Run Reading's to answer: what in the
      Run Hand-off is general enough for the Container Group, and whether the
      light read of the last CBC Run cost CBC Run 5 anything. Evaluated
      before that, every piece would end on trial and be judged
      again.
      Trigger: CBC Run 5's Run Reading, with its lessons in hand.
      See: devlog 2026-10-22.

- [ ] Decide how a Work Approach and an Output Shape divide an output: the
      Work Approach says what is done, the Output Shape how its output looks
      (2026-10-20, the reviewer).
      Context: an Output Shape is read at the gate only, so work written
      without it can show it wrong (`docs/conventions/shapes/` §3, *One place, read at the gate*).
      A skill that carries the output's form undoes that.
      `cbc-framing` hands over `templates/registry.md` to fill in,
      for the output the Registry-Entry Shape governs.
      `approach-drafting`'s stage 1 lists the parts a Work Approach
      file holds, the form of its own output.
      Ideas:
      - an Output Shape adapts: divergence is how it learns
        (`docs/conventions/shapes/` §2, *What an Output Shape is not*), and an Output Shape that never
        changes is finished or unread (`docs/conventions/shapes/`
        §5.2, *A tick, and a difference*).
      - a Work Approach is written without the output's form; a part an
        Output Shape needs is asked for as content, in the Work Approach's own
        words.
      - such an ask carries a Fact Reference to the Output Shape only for
        the Change Walk; the
        Output Shape says it is read at the gate.
      - a part may be optional, and the Output Shape marks it so.
      - a part considered and empty says "none, because…", so it
        reads differently from one left out.
      - a part never asked for is a fifth kind of difference at the
        gate: the fix goes to the Work Approach, and the output records
        the gap.
      - Refinement Round 2's FINDING-211: one form told in a skill, an Output Shape
        and a template: the slice record's outline, the backstop at
        the red run, a cost's size, the registry entry's fields, a
        body asserted by path.
      Trigger: `approach-drafting`'s first evaluation, at the
               refinement's close.
      See: devlog 2026-10-20, later; `TODO-CONVERSATION-MEMORY.md` §2, *How an approach and a shape…*.

- [ ] Decide whether approach drafting becomes a convention
      (2026-10-27, the reviewer).
      Context: `approach-drafting.md` is on trial (ADR-0058), held
      word for word in both Convention Seats until its evaluation (ADR-0069,
      decision 2). No manual lists it.
      Ideas:
      - one convention for Approaches on Trial, its artifacts
        `approach-drafting` in both Convention Seats and `approach-evaluation`
        in ours.
      Trigger: `approach-drafting`'s evaluation at the refinement's
               close, at its stage 5.

- [ ] Choose whether a manual is called a concept (2026-10-19, the
      reviewer).
      Context: one idea should have one word. The reviewer saw a
      manual as a concept: an idea written down, with sub-ideas,
      and its rules and skills as the convention. "Concept" already
      names the CbC concept and the Tiers Model's concepts tier.
      Facts-in-sync calls both a Canonical Description
      (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).
      Ideas:
      - a manual is a concept; its rules and skills, the convention.
      - "description" stays the general word, as facts-in-sync has it
        (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).
      Trigger: a second Concept Repo, when what a concept is gets
               decided (`docs/models/idea-to-output.md` §5, *An Idea Model and a concept*).
      See: devlog 2026-10-19, the redesign's ideas.

- [ ] Decide whether a sweep checks one home after work lands, and
      when (2026-10-22, the reviewer).
      Context: the Foundation Check walks what derives from a
      changed Canonical Description at each commit, and `commit-plan`'s close
      sweeps for names a set moved. Nothing looks back over finished
      work to see whether its facts still have one home. Refinement Round 2's
      One home Finding Kind does it once, for the refinement.
      Ideas:
      - a one-home sweep of its own, or one part of a sweep
        defined as a convention or a Work Approach.
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
      - how the sweep stands to `retrospective`, a CBC Run's look-back
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
        disagreement. Five acts do it today: the Foundation Check,
        `commit-plan`'s sweep, a Refinement Round, a Run Reading
        and the missing-context finding. What a check is
        in the Idea-to-Output Model; when each runs, in its own
        convention.
      Trigger: the refinement's close, once Refinement Round 2 has swept one
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
        words, a Fact Reference; several are allowed.
      - at an item's close, grep TODO for its first words; an item
        whose waits are all closed moves up in the same commit.
      - at a Plan Step's close triage, Next is ordered: ready items first,
        and among them those others wait on; a cycle is split,
        merged or decided provisionally.
      - no re-sort when an item is added.
      Trigger: the next Plan Step's close, at its triage.
      See: devlog 2026-10-24, the text-division item.

- [ ] Decide whether a session's end has a home of its own, and
      what it holds (2026-10-22, the reviewer).
      Context: a session's end is spread out.
      Project-recording asks for a devlog entry and a Resume line
      (`docs/conventions/project-recording/` §4, *The devlog*). Two habits
      live only in the agent's own memory: a line per
      delegation, and, from 2026-10-22, one missing-context
      finding. A reader of the repo sees neither.
      Ideas:
      - a convention of its own, by its moment; the sweep its
        twin for work that has landed.
      - a section of project-recording's devlog part
        (`docs/conventions/project-recording/` §4, *The devlog*), since most of it is devlog writes.
      - an Approach on Trial first (ADR-0058).
      - an Agent Rule loaded every session, naming each duty and its
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
      its close (`.claude/skills/commit-plan/SKILL.md` §4, *The lifecycle*), and a regroup gives them new hashes. This repo cites
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
      Trigger: the refinement of this repo closes; its rounds read `commit-plan` and the Fact Reference's form
        (`docs/conventions/facts-in-sync/` §3, *The Fact Reference*).
      See: devlog 2026-10-19, regrouping.

- [ ] Make the conventions index a full Local Map (2026-09-30, the
      reviewer).
      Context: its chain shows only the conventions that act in
      sequence during a piece of work. The other nine relate by what
      they govern, read or describe, stated as about thirty Fact References across the manuals' *What this does not cover*, and seen
      together nowhere. The local-map rule now exists
      (`docs/conventions/project-recording/` §8.6, *Local Maps*, ADR-0045).
      Ideas:
      - all twelve and how each touches the others, derived from those references, built by `visual-comparison`.
      - three links, each with its upkeep: derives
        (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, the Foundation
        Check), points (one home, the grep at a commit that moves a
        section, a Plan Step's close), governs
        (none: a change to a rule that governs other text could
        sweep that text or file the sweep, a rule beside
        `docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).
      - scenarios as entries into one procedure, the Foundation
        Check: a manual, a skill or rule, a CBC Run's finding. Two
        exits it lacks: the governs sweep, and what must run again
        after.
      - rename "The chain": the Idea-to-Output Model's chain is
        another thing. Not "hand-off", which names the full-auto
        Run Hand-off and a Run Ask.
      Trigger: due — the pair it waited on was made on 2026-09-30.
      See: devlog 2026-09-30, Local Maps; `cb41ade`.

- [ ] Read CBC Run 4 against `dac4dd1`, the CBC Run 3 commit it was born
      from (2026-10-15, the reviewer).
      Context: CBC Run 4, safe-reservation-2, was born 2026-10-15 by
      hand from CBC Run 3's skills, Agent Rules and Output Shapes at `dac4dd1` and
      our Container Group at `35edd3f`, and ran on full auto through
      Release. Reading it shows what it changed on top of
      `dac4dd1`, what of CBC Run 3's asks it answered, what still has
      to be checked, and what is new. It left twelve lines under
      To the Concept Deliverer.
      Ideas:
      - CBC Run 3's and CBC Run 4's `RETRO.md` read against the
        retrospective skill's form, for an Output Shape (ADR-0054).
      - `temp/RUN-4.md`, CBC Run 3's Run Hand-off that started CBC Run 4, never
        committed there: what CBC Run 4 was told, read for lessons, and
        deleted once read.
      - how CBC Run 4 closed its step branches (`run4/step-9` to 11):
        the playbook still ticks "reached main by fast-forward" in
        the gate, which ours dropped (`49d06e6`).
      - whether CBC Run 4's birth fired three triggers: "before the next
        birth", shipping `temp/`; "the next birth's Step 3 close",
        the ground-must-be-up rule; "a fourth run deriving
        `.gitignore` by hand", cbc-bootstrap's hygiene.
      - the retrospective puts a "rules in force now" list on top of
        a Decisions Log kept append-only; CBC Run 3 and CBC Run 4 both did:
        which side changes.
      - `cbc-framing` writes a status line into the README, where
        the README's form, its header comment, keeps changing status
        in PLAN: how that line lived in CBC Run 4.
      - whether CBC Run 4 confirmed its plan's Plan Steps once framed, as project-recording says a CBC Run does
        (`docs/conventions/project-recording/` §9.4, *How a playbook is written*),
        though no skill or Plan Step asks it: if not, whether the playbook's
        Framing Plan Step should.
      Trigger: the refinement of this repo closes; in a new session.
      See: `f097695`, the kickoff and the message it took;
      `TODO-CONVERSATION-MEMORY.md` §5, *Run 4's reading: two moves…*.

- [ ] Decide whether our own forms become Output Shapes, and whether an
      Output Shape's part can be optional (2026-10-17, the reviewer).
      Context: an Output Shape is read at a Plan Step's gate only, so the work
      is not shaped by it (`docs/conventions/shapes/` §3, *One place, read at the gate*). Our own
      forms, a Run Reading's and a manual's, are Agent Rules that load when
      such a file is read. They kept that place because this repo
      had no Plan Steps; since ADR-0057 it has.
      Ideas:
      - the work's rules keep what must hold while working, such as
        numbers never changed; the forms become Output Shapes.
      - a part an Output Shape names may be optional, where the work does
        not always produce it.
      - Known already as questions, a skill's Gates and the
        playbook's lists, answered in a Plan Step's own words.
      - our documents' layouts are Output Shapes too, a case of the shapes
        convention: a manual's, a Work Approach's, a Run Reading's, a
        record's. Five mechanisms hold them today.
      - read at the gate and adaptable like any Output Shape; the Work Approach
        or rule that writes the document carries no layout.
      - what must hold while writing stays an Agent Rule
        (`docs/conventions/shapes/` §3, *One place, read at the gate*): a
        manual's section order may; how each part is written may not.
      - `.claude/rules/convention-manual.md` is the manual's form. It
        stands on the conventions convention until this item
        decides; as an Output Shape, it would stand on the shapes convention.
      - a record's form, in its header comment, stays
        project-recording's: it is read when the record is opened,
        while an entry is written, which the shapes manual keeps for Agent Rules
        (`docs/conventions/shapes/` §3, *One place, read at the gate*).
        Only `.claude/decisions.md` holds one under another
        convention, agent-arrangement. The open forms are those in
        rules: a manual's, a Run Reading's.
      - a text gets an Output Shape when there are many of its kind and a
        moment to check them: manuals, Run Readings, skills and Agent Rules
        may; a record's entries are checked only as they are written.
      - Idea Models and the concept get none while nothing of their kind
        recurs: three Idea Models share no parts yet, and the concept has
        one form and one home (`docs/models/idea-to-output.md` §5, *An Idea Model and a concept*).
      Trigger: CBC Run 4's Run Reading, which reads how CBC Run 4 lived CBC Run 3's
               Output Shapes.
      See: devlog 2026-10-17, our forms as shapes; 2026-10-20,
      later, layouts; `TODO-CONVERSATION-MEMORY.md` §3, *Layouts as shapes*.

- [ ] Try a readability pass, the reviewer marking where text is
      hard to read (2026-10-18, the reviewer).
      Context: a refinement's finding names a broken rule, so text
      that meets the rules stays, even when it could read better
      (`.claude/approaches-on-trial/refinement.md` §2.4, *Reading the Finding Kinds*). Polish
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

- [ ] Decide whether writing rule 10 reaches unnumbered headings
      (2026-10-30, the reviewer).
      Context: rule 10 binds a numbered section's title; its reason,
      that a title is read in every Fact Reference to it, reaches an
      unnumbered heading too. Refinement Round 3 found references
      cutting a skill's or a reference file's heading short, and 27
      unnumbered headings in the Method Group with a gloss after a
      dash or colon. The round read against the rule as written.
      Trigger: the refinement of this repo closes.
      See: `temp/refinement-2026-10-18.md`, DECISION-20 (`1aa928c`).

- [ ] Rename the manuals, Agent Skills and Agent Rules that share a
      name (2026-10-31, the reviewer).
      Context: five names are shared: commit-messages, commit-plan,
      visual-comparison and retrospective, each a manual and an Agent
      Skill; writing, a manual and an Agent Rule. Writing the kind
      word always keeps them apart in reading (the refinement's
      DECISION-24 and 27), but a grep still finds both. It waits for
      two reasons: which side is renamed, and to what, is a choice
      that how CBC Runs 4, 5 and 6 used these parts can inform; and
      four of the names ship, so a rename moves every CBC Run's
      folders and commands, the paths a read compares by. Their
      records keep the old names either way, since a record is never
      updated. New names follow the naming rule of the
      refinement's design, ADR-0078 when written.
      Ideas:
      - rename the manual, by its subject: commit-message-form,
        change-sets, diagram-choice, looking-back, plain-writing.
      - or rename the Agent Skill or Agent Rule, by its act:
        write-commit-message, plan-commits, compare-diagrams,
        hold-retrospective, write-plainly; four ship, so every CBC
        Run gets new folders and commands.
      - a strict "verb first" grammar would rename 11 of the 12
        Agent Skills; a loose one 3, and lets commit-plan through.
      - no grammar parts a manual from an Agent Rule: both are nouns.
      Trigger: the Run Readings of CBC Runs 4, 5 and 6 have closed. A
               CBC Run born before then is built with the old names
               and joins them.
      See: `TODO-CONVERSATION-MEMORY.md` §27, *Shared names of
      conventions and approaches*.

- [ ] Read a CBC Run born before the refinement by its needs, not its
      diff (2026-10-31, the reviewer).
      Context: a Run Reading takes three things from a CBC Run: the
      diff of its copies, its Decisions Log and its Run Asks
      (`.claude/skills/exchange-read/SKILL.md`, step 3). The
      refinement renames the delivered text to Glossary Names and may
      change how the parts are put together, so a diff by CBC Runs
      4, 5 and 6 shows edits to text we no longer hold, and cannot be
      taken as it stands. Their Decisions Log entries and Run Asks
      still say what each needed and what went wrong without it. The
      readings come after the refinement, not before: read now, every
      item taken would land in text round 3 rewrites.
      Ideas:
      - read how the CBC Run went and what it did, and ask whether
        the new structure meets each need, defines it wrongly, or
        misses it.
      - each item ends one of three ways: met, naming where; still
        missing or wrong, becoming work; no longer applies, saying
        why the need is gone, not only the text it touched.
      - the old words a CBC Run wrote are read through each Glossary
        Name's entry, which names them.
      Trigger: the Run Reading of CBC Run 4 opens. If its diff proves
               still usable as it stands, the item closes with nothing
               changed.
      See: `TODO-CONVERSATION-MEMORY.md` §30, *Reading a CBC Run
      born before*.

- [ ] Write an Agent Rule that writes a skill or Agent Rule from its convention
      (2026-10-17, the reviewer).
      Context: the conventions manual says how a skill or rule is
      written (`docs/conventions/conventions/` §1, *A convention's Work Approaches*), and nothing puts it in front of the
      writer: a manual has `convention-manual.md`, a skill or rule
      has no such rule. An Approach on Trial writes freely, and its
      pieces are input: what the work needed. When an evaluation
      places one, the lasting form comes from the conventions manual: the manual by
      (`docs/conventions/conventions/` §2, *The Convention Manual*), each skill or
      rule from it by (`docs/conventions/conventions/` §1, *A convention's Work Approaches*).
      Ideas:
      - an Agent Rule derived from the conventions manual's artifact part
        (`docs/conventions/conventions/` §1, *A convention's Work Approaches*), as
        `convention-manual.md` is from its manual part
        (`docs/conventions/conventions/` §2, *The Convention Manual*), on `.claude/skills/`,
        `.claude/rules/` and `delivery/`.
      - a `paths:` rule loads only when a file is touched, and the
        commit is the other moment
        (`docs/conventions/agent-arrangement/` §5.6, *Rules files*).
      - `approach-evaluation`'s placing hands each piece to the
        rule, for a Work Approach of ours and of a CBC Run's alike.
      Trigger: the first evaluation that places a piece as a skill
               or rule, at stage 5 of
               `.claude/approaches-on-trial/approach-evaluation.md`.
      See: devlog 2026-10-17, later, the skill rewrite.

- [ ] Read text for its level in the chain, the Levels Finding Kind,
      both ways across each boundary (2026-10-31, the reviewer).
      Context: each level has its own job. An Idea Model states an
      idea any repo adapts; a manual says what a way of working is, how
      and why; the Work Approaches made from it state the rules, one
      sentence each, and explain nothing (`docs/models/idea-to-output.md`
      §6.1, *The manual's level*, ADR-0078). Text at the wrong level
      breaks that. Found at the design's commit 5: facts-in-sync §3.4
      first listed its six rules with almost no why; the conventions
      manual §1 holds the rules for writing an Agent Skill or Agent
      Rule, and no Work Approach carries them to the writer.
      Ideas:
      - the four cells: a model holding this repo's own rules; a
        manual retelling its model's idea; a manual stating rules
        with no why; an Agent Skill or Agent Rule explaining why.
      - per passage: which level it belongs to, and whether the level
        it belongs to already holds it.
      - conventions §1 is the item above, "Write an Agent Rule that
        writes a skill or Agent Rule from its convention".
      - a passage with no Work Approach: an Agent Rule is made, or the
        passage stays as the manual's reason for a rule held
        elsewhere.
      - a Finding Kind of the next refinement, if one comes again
        (`.claude/approaches-on-trial/refinement.md` §3, *Not known
        yet*); ADR-0078 is the new rule that makes it due.
      Trigger: the refinement of this repo closes, when whether a
               refinement comes again is decided.
      See: ADR-0078; `TODO-CONVERSATION-MEMORY.md` §28, *Text at the
      wrong level of the chain*.

- [ ] Rewrite the method's texts plain (2026-10-17, CBC Run 3's RETRO
      D2).
      Context: the agent copies the voice it reads. CBC Run 3's records
      came out in the skills' voice, though "explain plainly" was in
      its memory. Plain already: the Agent Rules, the Output Shapes, `cbc-slice`'s
      skill and workflow (`2674c03`). Not yet, about 26,000 words:
      `cbc-framing` (8,500), the stack skills (13,800), the concept
      chapters (3,400), readiness (600). A chapter reworded is a
      concept change, editorial unless a meaning moves.
      Ideas:
      - one commit per file; the worked example's two copies as one.
      - the fenced collisions as "nothing dies" kills, as the Kill
        Shape asks; the example's kill count and reconciliation move.
      - "invariant-shaped", "contract-shaped": "shape" now reads as the
        Output Shape.
      - chapter 02's "scope creep wearing a safety costume".
      - `cbc-slice`'s opening states the completion test alone;
        `concept/04-cbc-slice.md` says the test proves a wall, and
        the wall closes the slice.
      - Refinement Round 2's lessons and layout in these texts, left here by
        the refinement's DECISION-7 and 8: FINDING-223, the harness
        reference's "passes"; 224, the "lived" markers; 227,
        `cbc-framing`'s export section, `infra-establish`'s manuals
        told three times, the worked example's two layouts; 228,
        the walkthrough's parts in its fourth section
        (`delivery/spring-postgres/.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md` §4, *Stand up the evidence harness*); and 206, the playbook's 12
        citations of CBC Run 3's RETRO.
      Trigger: the refinement of this repo closes. Its Writing Finding Kind
               reads these texts; what Refinement Round 3 did leaves this
               item, and what is left stays or goes.
      See: devlog 2026-10-17, later, the plain method;
      `TODO-CONVERSATION-MEMORY.md` §6, *The method's plain rewrite…*.

- [ ] Run this repo's retrospective, on trial (2026-10-17, from
      Step 10's gate).
      Context: `docs/conventions/retrospective/`, the Concept Deliverer's
      seat, says what it is: both skills run on this repo, from
      `delivery/container/`, and a verdict on whether we hold them.
      Step 10's gate held it until ADR-0057.
      Trigger: the close of the Plan Step that runs CBC Run 5's birth.
      See: ADR-0057, decision 4.

- [ ] Decide whether a delivery checks its paths against the CBC Run's
      own files (2026-09-30, the Run Reading of CBC Run 3).
      Context: our shipped `.claude/rules/shapes-lifecycle.md` sat
      at CBC Run 3's own rule's path, so the Delivery Take landed ours over the
      CBC Run's. Two checks in the Exchange Convention miss it: one checks only that no path
      is claimed by two of our groups (`docs/conventions/exchange/` §3.4, *One group per file*);
      the Delivery Take's diff sees that a file differs, not whose it is
      (`docs/conventions/exchange/` §4, *The Delivery Take*).
      Once so far; checked by hand at `e6538f6`: no staged path was new.
      The Method Group's four Output Shapes sit at CBC Run 3's own `.claude/shapes/`
      paths (ADR-0052); the next birth is where they first land.
      Ideas: in `exchange-deliver`, the staged paths against the
             CBC Run's files that are not at its Delivery Pin.
      Trigger: the next delivery that ships a path new to the CBC Run.
      See: devlog 2026-09-30, the delivery to CBC Run 3.

- [ ] Read the frozen CLAUDE template's stance bullets against a
      full CBC Run's derived entry file (2026-09-06, the user).
      Context: the template's walk-1-era method half is frozen at
      `docs/baselines/claude-md-template-v1.md`. No birth can judge
      the stance bullets — only a CBC Run that has framed and built.
      Three ways: the CBC Run's `CLAUDE.md`, frozen v1, and
      `cbc-derived-claude-walk1.md`; harvest re-enters the template
      only from that Run Reading, each line traced to the CBC Run. CBC Run 3
      has had no Release; CBC Run 4 released the same project, so its
      entry file is read, CBC Run 3's beside it.
      Trigger: CBC Run 4's Run Reading.
      See: devlog 2026-09-06 (the template re-cut).

- [ ] Sort `docs/baselines/` by kind (2026-09-23, ADR-0035
      decision 6).
      Context: trial evidence is withheld so a later derivation
      measures independence; an Output Shape is withheld only until a
      gate. A wrong move destroys a measurement that cannot be
      remade, so this is its own Run Reading, not a tidy-up. The
      Spring slice reference opens once, at a CBC Run's Release
      (ADR-0033); CBC Run 3 has had no Release, and CBC Run 4 had one.
      Trigger: CBC Run 4's Run Reading, where the Spring slice reference
               opens.
      See: devlog 2026-09-24.

- [ ] Read what CBC Run 5's first slice gate found against the
      Evidence-Test Shape (2026-10-08, the Run Reading of CBC Run 3).
      Context: the Output Shape ships with the method since ADR-0052, read
      only at the gate. A Newborn Run writes its first tests without it,
      and its first slice's close reads them against it: the
      differences are the measurement. CBC Run 4 held CBC Run 3's Output Shape from
      birth, so CBC Run 5 is the first clean one, unless it reads the
      Output Shapes at birth (the item on `.claude/shapes/`). `cbc-slice`
      holds most of its lessons, so tests from the skill alone may
      meet it.
      Trigger: CBC Run 5's first slice closing.
      See: devlog 2026-10-08; and 2026-10-10.

- [ ] Watch whether the next newborn adds the ground-must-be-up
      rule to its entry file unasked (2026-09-04, ADR-0013's scope
      boundary).
      Context: the shipped entry file teaches this fill and no skill
      prompts it. CBC Run 3 answered the bootstrap half — its entry
      file now states only what never changes. At establish it
      added no Local Rule, at no visible cost; a costly miss would
      be evidence for a skill line.
      Trigger: the next birth's Step 3 close.
      See: devlog 2026-09-12, later.

- [ ] Decide which ideas here are Idea Models (2026-10-24, the
      reviewer).
      Context: three Idea Models exist: agent, tiers, idea-to-output. An
      Idea Model comes from a convention whose idea is general enough to
      be used elsewhere (`docs/models/idea-to-output.md` §4.2, *Up, work to an idea*). The
      text-division item held candidates, left open by ADR-0063.
      Ideas:
      - one home: facts, their home, Fact References, and how a
        disagreement between linked texts is settled.
      - the Concept Deliverer and the CBC Run, with Convention Seats.
      - an Output Shape: the shapes manual says what one is
        (`docs/conventions/shapes/` §1.1, *What an Output Shape says*, and §2, *What
        an Output Shape is not*).
      - records: what a record is, a form and its entries; what a
        set of records answers; how each Convention Seat adapts it, as the
        refinement's DECISION-12 map shows. Weighed against the Idea-to-Output Model, which holds part of
        it (`docs/models/idea-to-output.md` §2, *The kinds*).
      - the two checks on text kept true: the checks at each change,
        a refinement after, and a finding's cause the way back. A
        section of the Idea-to-Output Model, with its Chain Links and
        its way up, or with the one-home idea if that becomes a model.
      Trigger: the refinement's close, once facts-in-sync, whose
               subject is the first idea, has lived through Refinement Round 2.
      See: ADR-0063; `30eb42e:TODO-CONVERSATION-MEMORY.md` §1;
      `TODO-CONVERSATION-MEMORY.md` §29, *Two checks on text kept
      true*.

- [ ] Decide whether an Idea Model ships to a CBC Run (2026-10-24, the
      reviewer).
      Context: no manual and no Idea Model ships
      (`docs/conventions/exchange/` §3.2, *What goes*). A manual may now stand on
      an Idea Model, as agent-arrangement does; a CBC Run gets the files made
      from it, never the reasoning above them.
      Ideas:
      - the Tiers Model's top tier holds the Idea Models in the
        Concept Repo "until three repos have lived".
      Trigger: a CBC Run's Run Reading finds a convention misread for want
               of the Idea Model behind it.
      See: ADR-0063.

- [ ] Decide whether an Idea Model may be written for one convention
      (2026-10-23, the reviewer).
      Context: the text-division item had an Idea Model only where several
      manuals share an idea. The reviewer asked to weaken that: an
      Idea Model for one convention, "to see general idea behind that
      convention". Idea-to-output has an Idea Model come from a convention whose idea is
      general enough (`docs/models/idea-to-output.md` §4.2, *Up, work to
      an idea*).
      Trigger: a convention whose idea another repo could use, with
               no second manual sharing it.
      See: ADR-0063; `30eb42e:TODO-CONVERSATION-MEMORY.md` §1.

- [ ] Decide whether a standing full read looks for missing Fact
      References, and for references pointing down (2026-10-27, the
      reviewer).
      Context: a line that relies on a fact written elsewhere and
      carries no Fact Reference is found by no grep and no Change Walk. The
      check of ADR-0070 asks it of each new or changed
      line at the commit. Only the refinement's rounds read the whole
      repo for it today: their Dependencies Finding Kind, which Refinement Round 2's
      close read ran with seven agents and 52 findings.
      Ideas:
      - its own piece of work: not the sweep, a grep at a plan's
        close, and not session end, which only records.
      - read by foundation: one agent reads a Canonical Description beside
        every file built on it, and asks of each line whether it
        relies on a fact and says where.
      - one Finding Kind per agent; other Finding Kinds may share the read, each
        with its own agent.
      - it reads against the reference's form
        (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*) once the settled form is
        written there.
      - a second Finding Kind for the same read: direction (ADR-0071). A
        line in an Idea Model or a manual that relies on a lower text is
        found by no grep either: telling relying from naming takes
        a read. Done by hand on 2026-10-28: the three Idea Models and 67
        manual paragraphs, 6 found, 3 of them references left at a
        fact's old home when it moved (`b7c17ae`).
      Trigger: a read finds a missing Fact Reference in text written
               after the per-commit check is in force, or a reference
               pointing down in text written after ADR-0071.
      See: devlog 2026-10-28; `TODO-CONVERSATION-MEMORY.md` §21, *A full read for missing fact…*.

- [ ] Test Fact References and foundations as a whole: name every
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
        home, a placed Approach on Trial among them; a foundation changed; a
        derived file changed against its foundation; a retelling
        whose host is itself a source; a CBC Run's id whose home changes;
        a shipped CBC line when our manual changes; a fact stated
        only in history; a line with no Fact Reference; a reference
        inside a living sentence about the past, after its section is
        retitled: it takes the new title, since only history keeps an
        old one (2026-10-31, ADR-0078's Context).
      - for each: what finds it, a grep or a read; which rule says
        so, by Fact Reference; what is re-read, the line, its
        paragraph or the whole file; what could still slip.
      - (a) on paper: a table of the scenarios against the rules.
      - (b) a drill on a throwaway branch: each scenario made for
        real, the check run, and what it found compared with a full
        read.
      - (c) agents: one per scenario, or one trying to make a change
        slip past the check.
      - (d) a Finding Kind of its own in the refinement's last read.
      - what a scenario finds missing becomes a finding or a TODO
        item; the test changes no rule itself.
      - the same two means for Glossary Names, 2026-10-30. A script
        can check every bold capitalized phrase against the glossary,
        every entry's pointer against the file where its Name is bold
        once (DECISION-22 of the refinement), and every Name spelled
        in lowercase. Only a read finds a word a text gives a new
        meaning with no mark, and decides a Name or plain words:
        rule 9's question at the commit, and a refinement's Writing
        read. The sweep scripts live in a session's scratchpad today.
      Trigger: the refinement closes.
      See: devlog 2026-10-28; ADR-0070;
      `TODO-CONVERSATION-MEMORY.md` §22, *Testing fact references…*.

- [ ] Look again at where a CBC Run learns how to treat a Skill
      Template (2026-10-28, the reviewer).
      Context: four shipped files told the off-template rule in
      their own words, and drifted: deviate from a Skill Template,
      derive from what it implements, log it, expect a harvest,
      never bend a decided constraint to fit it. On 2026-10-28 it went to the Exchange Convention
      (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*) and the CBC Run's `delivered-copies.md`, chosen on
      one Run Reading, with no CBC Run having lived it.
      Ideas:
      - (a) one skill states it; the others point.
      - (b) delivered copies: the Exchange Convention
        (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*) and the CBC Run's
        `delivered-copies.md`; today's choice.
      - (c) each Skill Template states it in its own header,
        where a CBC Run meets the choice.
      - (d) an Output Shape for a Skill Templates.
      - weigh each by maintenance, readability, future-proofing and
        complexity.
      - check that every manual and shipped text that speaks of a
        skill's templates agrees with the Exchange Convention (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*) and
        `delivered-copies.md`,
        and that `delivery/README.md` and ADR-0008 still match.
      - check that each use says whose template it is: a skill's,
        repo-hygiene's, or a Record Stub. Of 97 uses in living text,
        only some say.
      Trigger: a Run Reading that shows a CBC Run deviating from a
               Skill Template, or a second stack's Stack Overlays arriving,
               whichever comes first.
      See: devlog 2026-10-28; ADR-0070.

## Later / someday

- [ ] Release concept v2 (2026-10-17, from PLAN's Step N).
      Context: so a stranger, or future-you, can read, cite and copy
      from this repo without the archive. Four items of its own:
      a CHANGELOG entry for the release; README true for a
      stranger; `docs/models/` checked against the repo, since
      `CLAUDE.md` sends a stranger there; known issues filed here.
      PLAN held it until ADR-0057.
      Trigger: the reviewer names it, after the Plan Step that runs run
               5's birth closes.
      See: ADR-0057, decision 4.

- [ ] Decide what our CHANGELOG tracks, and how the Record Stub asks it
      (2026-10-21, the reviewer).
      Context: ADR-0003 (2026-08) made it the concept's log, for
      runs pinning a version; ADR-0039 decision 9 kept conventions
      out. Since v1 (2026-08-28), about 1,350 commits added the
      conventions, the Container Group, the Idea Models and Approaches on
      Trial, and none is logged. A CBC Run pins a commit and cannot read
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
      - a check at each Plan Step's close: every change outside the
        excluded paths has an entry, or is marked editorial.
      - what is tracked is read again when the repo grows a new kind
        of thing.
      - the Record Stub gains a `Tracks:` line beside `Versioning:`, decided
        at Framing, with when to revisit it; the lesson goes in project-recording's changelog part
        (`docs/conventions/project-recording/` §6, *CHANGELOG.md*).
      - a Delivery Fill sets a CBC Run's two lines at birth, as the playbook
        fills its plan; we fill ours in place
        (`docs/conventions/project-recording/` §9.4, *How a playbook is written*, step 1).
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
      Context: CBC Run 3 wrote one at Step 3 — the ways its store makes
      two writers disagree — because the skill is silent on it. We
      held it rather than declined: one instance is not an Output Shape.
      CBC Run 3 says SL-2 did not lean on it; SL-2 faces no race.
      CBC Run 4 rebuilt CBC Run 3's problem from CBC Run 3's copies, so it
      cannot be the second CBC Run.
      Trigger: CBC Run 5 reaching the same gap unprompted.
      See: devlog 2026-09-17, later still.

- [ ] Move the skills' `foundation` to concept v2 at the release
      (2026-10-08, ADR-0048).
      Context: the Method Group's skills say `foundation: concept v1`.
      ADR-0048 makes the next release v2, and `cbc-slice` and
      `cbc-framing` already state its ranking.
      Trigger: the release that names v2.

- [ ] Decide whether an Agent Rule can be delivered on trial, as an Output Shape
      can (2026-10-08, never-oversold).
      Context: an Output Shape reaches a CBC Run but binds nothing until a
      gate reads it (ADR-0052); an Agent Rule learned in one CBC Run is in
      force in the next from its first Plan Step. CBC Run 3 asked after
      offering its Evidence-Test Shape as an Agent Rule. Held: the question
      is real only once there is an Agent Rule we would deliver that way.
      CBC Run 3's RETRO D4 says a trial names the close that judges it,
      and the Plan Step Form says so since `0cdc50c`.
      Ideas:
      - ship it as an Approach on Trial: in force only when a Plan Step
        takes it as its Work Approach, and each use comes back as a note
        (ADR-0058).
      Trigger: an Agent Rule we would ship that one CBC Run alone has lived.
      See: devlog 2026-10-08.

- [ ] Give the method a glossary (2026-10-08, never-oversold).
      Context: its words are defined where each is first used;
      tripwire, witness, fold, fence and possession appear only in
      the skills, never in the chapters a reader starts from, and
      the wall's own check joins them. Whether a list beside the
      chapters, or a chapter's, is open. Since `fbd1c5e` each CBC Run
      starts its own glossary at framing; the method has none.
      Trigger: Release's README item, where a stranger first needs
      the words.

- [ ] Number the concept chapters' sections (2026-09-30).
      Context: their `##` headings are unnumbered, and nothing points
      into a chapter's section today. The chapters are the canonical
      text every CBC Run holds a copy of, so numbering them would change
      every copy for no reader yet
      (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts* numbers by form).
      Trigger: the first Fact Reference that needs a section of a
               chapter.
      See: devlog 2026-09-30, numbered parts.

- [ ] Does the playbook need a convention of its own? (2026-09-29,
      the reviewer)
      Context: project-recording describes it
      (`docs/conventions/project-recording/` §9, *The playbook*), and one playbook exists, the CBC Run's. It is not an Output Shape: an Output Shape is form, never content
      (`docs/conventions/shapes/` §1.1, *What an Output Shape says*, and §2, *What a
      Output Shape is not*), and a filled-in template is not one; a
      playbook is content, copied and filled at birth.
      Ideas: a convention of its own, split from project-recording's playbook part
        (`docs/conventions/project-recording/` §9, *The playbook*).
      Trigger: a second typed playbook.
      See: devlog 2026-09-29, the PLAN pass.

- [ ] Filter a maintainer's Container Group out of this repo, when one is
      needed (2026-09-29, the reviewer).
      Context: `delivery/container/` is the CBC Run's derivation of the
      conventions, and this repo's own files are the Concept Deliverer's
      (ADR-0042). No second maintainer repo exists, so no
      maintainer's container does either.
      Ideas: filter this repo — keep the functionality and layout,
             drop this concept's own content.
      Trigger: a second maintainer repo.
      See: devlog 2026-09-29, the split.

- [ ] Move the Tiers Model to the Concept Garden (2026-09-30).
      Context: it maps the workspace, and the workspace has no home:
      the Concept Garden stays a plain folder until a second Concept Repo
      exists (`docs/models/tiers.md` §2.2, *Concept Repos*). Until then it lives here,
      beside the Agent Model; `docs/models/` stays.
      Trigger: a second Concept Repo.
      See: devlog 2026-09-30, the Tiers Model.

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
      Context: the sending half is in force — a Delivery Note says when it
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
      nothing, and three CBC Runs derived `.gitignore` by hand. They
      are spring-postgres (ADR-0029 decision 7) and move with the
      answer; until then they sit against decision 5's beside-it
      rule, an exception the ADR records. The Change Walk named the wider
      gap: nothing ships a Stack Overlay, and a blind CBC Run cannot
      fetch one.
      Ideas:
      - Refinement Round 2's FINDING-203: `cbc-bootstrap`'s skill and its
        walkthrough both tell a CBC Run to add a Stack Overlay below
        each hygiene file's marker, and no file ships one. The
        skill could point at the walkthrough's step 2 instead.
      Trigger: cbc-bootstrap's hygiene step next opened, or a
      fourth CBC Run deriving `.gitignore` by hand.
      See: devlog 2026-09-18.

- [ ] Weigh three candidate rules for what makes a note land
      (2026-09-17, the handbook's reply).
      Context: the only outside reading of our Delivery Notes. An
      opening ordered by weight let them plan their commit split
      from four lines; "we are not asking you to write the
      convention" removed a pressure we did not have to name; all
      four additions were usable with no follow-up question. None
      of the three is in the exchange manual.
      Trigger: the Delivery Note that answers CBC Run 5's Run Reading, before it is
               written.

- [ ] Decide whether an overtaken Run Reading still owes the CBC Run a Delivery Note
      (2026-09-30, the Run Reading of CBC Run 3).
      Context: the Run Reading of 2026-09-24 was overtaken on 09-26 and
      deleted without one, so what CBC Run 3 had addressed to us since
      its Delivery Pin had no verdict until the Run Reading of 2026-09-30 read it
      again — three edits to copies, ten asks and offers.
      The Exchange Convention closes an overtaken Run Reading
      (`docs/conventions/exchange/` §6.4, *How a Run Reading closes*)
      "the same way", one pass over its items, and is silent on the Delivery Note every read ends with
      (`docs/conventions/exchange/` §6.6, *The Delivery Note after a read*). Once so far.
      Ideas: the overtaken Run Reading sends a Delivery Note: read, asks open.
             the next read goes back to the last Delivery Note's Read-Through Commit.
      Trigger: the next Run Reading overtaken.
      See: devlog 2026-09-30, the delivery to CBC Run 3.

- [ ] Name when a CBC Run is read (2026-10-01, the working draft).
      Context: a Run Reading happens when the reviewer says. A Run Ask
      arriving, a Plan Step closing at the CBC Run, a calendar — none is
      named, so a Run Reading happens when someone remembers, and both
      sides drift further from the Delivery Pin while it waits. CBC Run 3's RETRO
      D24 names one moment: after a CBC Run's apply Plan Step, so its
      decisions arrive tried. CBC Run 3's next Plan Step waited on our Delivery Note:
      recording the Read-Through Commit was on its path (2026-10-18).
      Trigger: a Run Ask found waiting for a Run Reading nobody called.
      See: devlog 2026-10-01.

- [ ] Decide how Run Readings work with more than one live CBC Run
      (2026-10-01, the working draft).
      Context: the rules for reading and working a Run Reading are
      written for one CBC Run. Two live CBC Runs mean two Run Readings, and
      their items may be the same finding twice.
      Trigger: a second live CBC Run.
      See: devlog 2026-10-01.

- [ ] Say once that a Run Reading's decisions are the reviewer's
      (2026-10-01, the working draft).
      Context: the agent proposes and builds, the reviewer settles —
      every Run Reading has gone so, and nothing says it. Probably the
      arrangement's to say, not the Run Reading's.
      Trigger: an agent found settling what was the reviewer's.
      See: devlog 2026-10-01.

- [ ] Watch whether the worked example anchors a CBC Run's framing
      (2026-09-17, the user).
      Context: an invented order service with an idempotency slice
      could steer a CBC Run toward that shape. No evidence in three
      CBC Runs; one weak signal — the example and CBC Run 3 both land on
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
      Ideas: an overlay file per skill beside the copy — CBC Run 3's,
             which it declined to build.
      Trigger: declined-but-needed becoming a pattern.
      See: devlog 2026-09-17, later.

- [ ] Add a rung for guarantees held by absence to the enforcement
      hierarchy (2026-09-14, CBC Run 3's SL-1).
      Context: no process clock, no state outside the store — nothing
      to observe at runtime; its wall is a rule on the compiled
      classes. CBC Run 3 asks for a rung between "single validated entry
      path" and "code review". It met it again in SL-2 and SL-4, and
      CBC Run 4 rebuilt the same problem from CBC Run 3's copies, so neither
      is a second CBC Run. The hierarchy lives in
      `concept/02-guarantees-and-walls.md` and both cbc-slice files: a
      concept change, with an ADR and the version question (ADR-0003).
      Trigger: CBC Run 5 meeting an absence guarantee.
      See: devlog 2026-09-15; and 2026-10-10.

- [ ] Decide whether the worked example shows a slice that
      inherits its wall (2026-10-10, the Run Reading of CBC Run 3).
      Context: CBC Run 3's SL-4 built no wall — SL-3's one statement
      already held its invariant — and owed proof only, against its
      own instance killed mid-write and an outcome its caller cannot
      know. The worked example has no such slice and no such
      adversity. One CBC Run's slice, so held.
      Trigger: a second CBC Run whose slice inherits its wall.
      See: devlog 2026-10-10.

- [ ] Decide whether `cbc-slice` says a red removes the backstop too
      (2026-10-10, the Run Reading of CBC Run 3).
      Context: the skill says a wall that already stands is removed on
      the working tree for its red. SL-4's red as signed stayed green:
      the store's check on the units held caught both orders, and the
      evidence went red only with the one transaction and that check
      both gone. CBC Run 3 revised its plan for it and proposed no edit.
      Since `2674c03` the skill asks the red run to note whether each
      backstop was seen or is unproven; removing it is not asked.
      Trigger: a second slice whose red a backstop holds green.
      See: devlog 2026-10-10.

- [ ] Decide whether a second service family earns its own
      walkthrough (2026-08-28).
      Context: beside `postgres-setup-walkthrough.md`; the test is
      long, sequenced, likely to recur.
      Trigger: a CBC Run first standing up a non-PostgreSQL service.

- [ ] Revisit "backend" in the skills' description lines
      (2026-09-06).
      Context: kept — it names the toolkit's honest scope, and
      every CBC Run so far is one. The practice skills' bodies
      (compose, Flyway, Spring Boot) are backend-born too.
      Ideas: start with the description lines.
      Trigger: the first non-backend CBC Run.
      See: devlog 2026-09-07.

- [ ] Tune the practice skills' trigger descriptions (2026-08-28).
      Context: unoptimized since import (archive STATUS).
      Trigger: a skill under- or over-firing in a CBC Run.

- [ ] Consider a held-insight tier in the harvest discipline
      (2026-08-29, safe-reservations' close).
      Context: its flow-back split sure adoptions, landed in the
      masters, from insights held as evidence with a named
      promotion path. ADR-0007 has only the first tier; adding
      one is an amendment, decided deliberately.
      Trigger: a Run Reading holds an insight it cannot land yet and
      has nowhere to put it.
      See: devlog 2026-08-29 (framing shape decided).

- [ ] Harvest the projection law's deeper lifecycle when a CBC Run
      lives it (2026-08-30).
      Context: public docs beyond the README, earned by substance
      and refreshed at slice closes — seen in the safe-reservations
      node's projection model, never lived by a CBC Run of ours.
      Trigger: a CBC Run first reaching the milestone that fires it.
      See: devlog 2026-08-30 (doc projection checked).

- [ ] Decide how a CBC Run learns that the rule for taking deliveries
      changed (2026-10-18, the reviewer).
      Context: a CBC Run takes a delivery under the `delivered-copies.md`
      it holds, so a delivery that changes that rule is taken under
      the old one. The rule cannot travel alone: one Delivery Pin covers every
      copy (`docs/conventions/exchange/` §2.2, *The CBC Run*). CBC Run 3's copy lacked
      `4de6ba2`'s Output Shapes; no files went, so it never acted.
      Ideas: the Delivery Note's "why it matters" names a change to the rule
             first, so the CBC Run takes it knowingly.
      Trigger: the first files delivered to a CBC Run still building,
               with `delivered-copies.md` changed since its Delivery Pin.
      See: devlog 2026-10-18.

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)

- The postgres image tag floats (2026-08-28). The ground template
  and the harness reference both say `postgres:17`, so they can
  pull different minors at different times. Accepted: the shared
  major is a deliberate coupling, and no CBC Run has hit drift.
  Revisit: a CBC Run's first minor-drift surprise — then pin both
  tighter, to a full version or a digest.
