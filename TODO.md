# TODO

<!-- Add items the moment they're discovered — that's what empties your head.
     Triage when closing a step. Prune "Later" ruthlessly: deleting an
     idea you'd re-derive anyway costs nothing.
     Rule: an inline TODO:/FIXME: anywhere in the work must reference an
     item here.
     Open work only: a closed item goes, since the devlog, the ADRs
     and git already say what closed. Known issues take the shape
     their heading names. Every other item takes one shape:

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
     extended or declined. The talk that shaped an item may sit in
     TODO-CONVERSATION-MEMORY.md; when See names its section, it is
     read before the Ideas are weighed. When an item changes, rewrite
     it true for today — never stack a dated update on it; the
     change's story is the devlog's.
     foundation: the project-recording convention -->

## Now (due while the open step runs)

- [ ] Decide how this repo's text is divided: by kind, a model, a
      convention or an approach, and by subject (2026-10-20, the
      reviewer).
      Context: the deliverer's role is spread over `ARCHITECTURE.md`
      §2 and §3, `docs/models/tiers.md`, the exchange, eleven seats
      sections and `docs/conventions/project-recording/` §9; staying
      in step over `docs/conventions/project-recording/` §11 and
      `docs/conventions/conventions/` §3.1 to §3.6. Only the agent has
      all three kinds: `docs/models/agent.md`,
      `docs/conventions/agent-arrangement/`, `.claude/`. Round 2's
      Layout fixes will make homes.
      Ideas:
      - a convention per subject with rules and a moment; a model
        for what a thing is; a section for a single rule.
      - a model only where several manuals share an idea, or where
        what it is and what we do got mixed.
      - one manual per subject, a rule per case; a case is often a
        seat.
      - candidate models: one home; what a convention is; the
        deliverer and the run, with seats; a shape, whose
        `docs/conventions/shapes/` §1 and §2 say what one is.
      - the layers themselves as a model: model → description (a
        convention or the concept) → approach → output.
      - a shape is not a layer after the approach: it is written
        from outputs and governs the next at the gate; "governs" is
        named in `9fd905b`, with no upkeep yet.
      - `docs/models/tiers.md` §2.2 already holds two of the
        chain's kinds, the mental layer and its executions; the
        chain as a model of its own, tiers pointing at it.
      - "layer" names three things already: the concept's LAYER-1
        to 5, the refinement's file layers, tiers' two; the chain
        takes another word.
      - the link "reasons from", model to convention, and what keeps
        it up; beside derives, points and governs (`9fd905b`).
      - the agent's chain rechecked against the layers before it is
        the template, so its errors are not copied.
      - `docs/conventions/project-recording/` §9's flow joins the
        deliverer → run relation, beside the exchange and the
        retrospective; `docs/conventions/project-recording/` §1 may be a
        model.
      - folding the agent model into agent-arrangement is the same
        question the other way round (its own item).
      - weigh each split by maintenance, readability,
        future-proofing and complexity.
      Trigger: before round 2 reads, beside its Layout kind.
      See: devlog 2026-10-20, later; 2026-10-19, the redesign's
      ideas; `TODO-CONVERSATION-MEMORY.md` §1.

## Next (each due at its trigger)

- [ ] Write `exchange-birth` while a birth runs (2026-09-26, the
      reviewer).
      Context: written from the exchange's manual, as `exchange-read`
      and `exchange-deliver` were, keeping the seed's intent — it
      delivers everything and decides nothing. Then *What this does
      not do* in `.claude/skills/exchange-deliver/SKILL.md` points at
      it, `pure-seed.md` goes, and ADR-0016's procedure of record
      moves. Run 5 is born by the seed, to keep its birth small.
      Ideas: first-time work on our seat, so an approach on trial
             drafted by `approach-drafting` (ADR-0058).
      Trigger: the birth after run 5's.
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
      §9.

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
      §10.

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
        (`docs/conventions/agent-arrangement/` §3.7: settings,
        never rules).
      - or that section splits in two: the approaches, and what
        reaches the agent's setup.
      - `CLAUDE.local.md` repeats two rules: commit on the word
        (`commit-messages`) and a stop at each boundary
        (`commit-plan`). Yet `docs/conventions/agent-arrangement/`
        §3.7 counts how often the agent stops as a setting.
      - "never rewrite main across 35edd3f" lives only in the
        agent's memory, unseen by any reader of the repo. Its
        failure is not noticing the moment, a rebase: a local rule
        for our `CLAUDE.md` (`docs/conventions/agent-arrangement/`
        §2.4)?
      Trigger: run 5's reading, with the lines gathered by then.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §11; `.claude/decisions.md`, 2026-10-22, the account skills.

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
      without it can show it wrong (`docs/conventions/shapes/` §3).
      A skill that carries the output's form undoes that.
      `cbc-framing` hands over `templates/registry.md` to fill in,
      for the output the `registry-entry` shape governs.
      `approach-drafting`'s stage 1 lists the parts an approach
      file holds, the form of its own output.
      Ideas:
      - a shape adapts: divergence is how it learns
        (`docs/conventions/shapes/` §2), and a shape that never
        changes is finished or unread (`docs/conventions/shapes/`
        §5.2).
      - an approach is written without the output's form; a part a
        shape needs is asked for as content, in the approach's own
        words.
      - such an ask is tagged to the shape only for the walk; the
        shape says it is read at the gate.
      - a part may be optional, and the shape marks it so.
      - a part considered and empty says "none, because…", so it
        reads differently from one left out.
      - a part never asked for is a fifth kind of difference at the
        gate: the fix goes to the approach, and the output records
        the gap.
      Trigger: `approach-drafting`'s first evaluation, at the
               refinement's close.
      See: devlog 2026-10-20, later; `TODO-CONVERSATION-MEMORY.md` §2.

- [ ] Choose whether a manual is called a concept (2026-10-19, the
      reviewer).
      Context: one idea should have one word. The reviewer saw a
      manual as a concept: an idea written down, with sub-ideas,
      and its rules and skills as the convention. "Concept" already
      names the CbC concept and the tiers model's concepts tier.
      `docs/conventions/conventions/` §3.5 calls both a description.
      Ideas:
      - a manual is a concept; its rules and skills, the convention.
      - "description" stays the general word, as
        `docs/conventions/conventions/` §3.5 has it.
      Trigger: the item on what a thing is, decided.
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
      Trigger: the refinement's close, once round 2 has swept one
               home and shown what a sweep finds.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §11, the `claude-md-management` part.

- [ ] Define the fact reference, and stop calling it a tag
      (2026-10-24, the reviewer).
      Context: a line that relies on a fact written elsewhere carries
      the address of its home, today called a tag (`one-home` rule 2,
      project-recording §11), defined nowhere in *The words*. "Tag"
      also names git tags, image tags and the repo prefix "CBC
      ADR-0053" (ADR-0020). Like a Java object reference: one fact,
      many lines pointing at it. Unlike one, a retelling holds a
      copy, so the walk re-reads it when the home changes.
      Ideas:
      - *The words*: "fact reference", with "home" defined as the
        fact's single source of truth.
      - written `(<path>, §<number>, <title>)`, no prefix word, no
        ids; a long title may be cut to its first words. The 137
        numbered titles average 13 characters, and 13 are over 30.
      - when a section is touched, every fact reference to its path,
        number or title is grepped and updated in the same commit,
        widening `docs/conventions/conventions/` §3.2's grep for a
        moved section.
      - the repo prefix keeps its own name.
      - a fact reference that jumps a level, an approach citing a
        model, may mean a convention, or a part of one, is missing
        between them; or none is needed, since the walk finds the
        jump when the model changes. Noted, not solved, until a case
        forces it. One today: `auto-run.md` → the agent model's
        §10.4. When a piece is placed (`approach-evaluation` stage
        5), or a run's approach rewritten here (stage 6), its
        references move to their new homes; nothing says so yet.
      - a missing fact reference is found by nothing: the walk sees
        only lines that carry one. At each commit, each new or
        changed line is asked whether it relies on a fact written
        elsewhere and, if so, whether it says where. Lived: the 11
        manuals' channel sections reasoned from the agent model
        untagged until 2026-10-24.
      Trigger: round 2's staying-in-step convention.
      See: devlog 2026-10-24, the text-division item;
      `TODO-CONVERSATION-MEMORY.md` §13.

- [ ] Decide how an item names the items it waits on, and what
      happens when one closes (2026-10-24, the reviewer).
      Context: TODO sorts by horizon and trigger; within a horizon,
      by when added. Some triggers name another item in free prose.
      One names an item that does not exist ("the item on what a
      thing is"), and two wait on the text-division item, with
      nothing to find them when it closes. Order mattered twice in
      the text-division item's own work. Now holds 1 item, Next 24,
      Later 33.
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
      Context: a session's end is spread out. project-recording
      §4 asks for a devlog entry and a Resume line. Two habits
      live only in the agent's own memory: a line per
      delegation, and, from 2026-10-22, one missing-context
      finding. A reader of the repo sees neither.
      Ideas:
      - a convention of its own, by its moment; the sweep its
        twin for work that has landed.
      - a section of project-recording §4, since most of it is
        devlog writes.
      - an approach on trial first (ADR-0058).
      - a rule loaded every session, naming each duty and its
        home.
      - its twin, a session's start: what is read first.
      - a session's end runs the sweep first, then writes its
        devlog entry. Weigh against the missing-context findings,
        which a sweep was to decide in a batch.
      Trigger: the text-division item, which decides how such a
               subject is placed.
      See: devlog 2026-10-22, later; `TODO-CONVERSATION-MEMORY.md`
      §12.

- [ ] Decide how commits cited by hash can still be regrouped
      (2026-10-19, the reviewer).
      Context: `.claude/skills/commit-plan/SKILL.md` §4 regroups a
      set's commits before its
      close, and a regroup gives them new hashes. This repo cites
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
      Trigger: the refinement of this repo closes; its rounds read
               `commit-plan` and `docs/conventions/conventions/` §3.2.
      See: devlog 2026-10-19, regrouping.

- [ ] Make the conventions index a full local map (2026-09-30, the
      reviewer).
      Context: its chain shows only the conventions that act in
      sequence during a piece of work. The other eight relate by what
      they govern, read or describe, stated as about thirty pointers
      across the manuals' *What this does not cover*, and seen
      together nowhere. The local-map rule now exists
      (`docs/conventions/project-recording/` §8.6, ADR-0045).
      Ideas:
      - all eleven and how each touches the others, derived from
        those pointers, built by `visual-comparison`.
      - three links, each with its upkeep: derives
        (`docs/conventions/conventions/` §3.5, the foundation
        check), points (one home, the grep at a commit that moves a
        section, a step's close), governs
        (none: a change to a rule that governs other text could
        sweep that text or file the sweep, a rule beside
        `docs/conventions/conventions/` §3.5).
      - scenarios as entries into one procedure, the foundation
        check: a manual, a skill or rule, a run's finding. Two
        exits it lacks: the governs sweep, and what must run again
        after.
      Trigger: due — the pair it waited on was made on 2026-09-30.
      See: devlog 2026-09-30, local maps.

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
        `docs/conventions/project-recording/` §7.4 keeps changing
        status in PLAN: how that line lived in run 4.
      Trigger: the refinement of this repo closes; in a new session.
      See: `f097695`, the kickoff and the message it took;
      `TODO-CONVERSATION-MEMORY.md` §5.

- [ ] Decide whether our own forms become shapes, and whether a
      shape's part can be optional (2026-10-17, the reviewer).
      Context: a shape is read at a step's gate only, so the work
      is not shaped by it (`docs/conventions/shapes/` §1). Our own
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
        (`docs/conventions/shapes/` §3): a
        manual's section order may; how each part is written may not.
      - `.claude/rules/convention-manual.md` is the manual's form. It
        stands on the conventions convention until this item
        decides; as a shape, it would stand on the shapes convention.
      - a record's form, in its header comment, stays
        project-recording's: it is read when the record is opened,
        while an entry is written, which shapes §3 keeps for rules.
        Only `.claude/decisions.md` holds one under another
        convention, agent-arrangement. The open forms are those in
        rules: a manual's, a reading's.
      Trigger: run 4's reading, which reads how run 4 lived run 3's
               shapes.
      See: devlog 2026-10-17, our forms as shapes; 2026-10-20,
      later, layouts; `TODO-CONVERSATION-MEMORY.md` §3.

- [ ] Try a readability pass, the reviewer marking where text is
      hard to read (2026-10-18, the reviewer).
      Context: a refinement's finding names a broken rule, so text
      that meets the rules stays, even when it could read better
      (`.claude/approaches-on-trial/refinement.md` §2.4). Polish
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
      Context: `docs/conventions/conventions/` §2 says how a skill
      or rule is written, and nothing puts it in front of the
      writer: a manual has `convention-manual.md`, a skill or rule
      has no such rule. An approach on trial writes freely, and its
      pieces are input: what the work needed. When an evaluation
      places one, the lasting form comes from
      `docs/conventions/conventions/`: the manual by §3, each skill
      or rule from it by §2.
      Ideas:
      - a rule derived from `docs/conventions/conventions/` §2, as
        `convention-manual.md` is from §3, on `.claude/skills/`,
        `.claude/rules/` and `delivery/`.
      - a `paths:` rule loads only on a Read; the commit is the
        other moment (`.claude/decisions.md`, 2026-10-17).
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
      Trigger: the refinement of this repo closes. Its writing kind
               reads these texts; what round 3 did leaves this
               item, and what is left stays or goes.
      See: devlog 2026-10-17, later, the plain method;
      `TODO-CONVERSATION-MEMORY.md` §6.

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
      run's. Two checks in `docs/conventions/exchange/` miss it:
      §3.4 checks only that no path is claimed by two of our groups;
      the take's diff, §4, sees that a file differs, not whose it is.
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
        at Framing, with when to revisit it; the lesson goes in
        `docs/conventions/project-recording/` §6.
      - a fill sets a CbC run's two lines at birth, as the playbook
        fills its plan; we fill ours in place
        (`docs/conventions/project-recording/` §9.4, step 1).
      Trigger: the release item above opens; its CHANGELOG entry
               needs the answer.
      See: devlog 2026-10-21; `TODO-CONVERSATION-MEMORY.md` §4.

- [ ] Decide whether a check compares the worked example's two
      copies (2026-10-15, the commit plan for writing rules).
      Context: one-home's rule 5 asks a check where two copies
      cannot be avoided (ADR-0053). The worked example sits in
      `cbc-framing` and `cbc-slice` and must stay identical; it is
      compared by hand at each edit, and was identical on
      2026-10-15.
      Ideas: a diff of the two in `exchange-deliver`'s gates, since
             a delivery is when the copies leave.
      Trigger: the two found different, or the worked example's
               next edit.

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
      (`docs/conventions/conventions/` §3.2 numbers by form).
      Trigger: the first pointer that needs a section of a chapter.
      See: devlog 2026-09-30, numbered parts.

- [ ] Does the playbook need a convention of its own? (2026-09-29,
      the reviewer)
      Context: `docs/conventions/project-recording/` §9 describes
      it, and one playbook exists, the CbC run's. It is not a
      shape: `docs/conventions/shapes/` §1–2 say a shape is form,
      never content, and a filled-in template is not one; a
      playbook is content, copied and filled at birth.
      Ideas: a convention of its own, split from
             `docs/conventions/project-recording/` §9.
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
      by `docs/models/tiers.md` §2.2 the garden stays a plain folder
      until a second concept repo exists. Until then it lives here,
      beside the agent model; `docs/models/` stays.
      Trigger: a second concept repo.
      See: devlog 2026-09-30, the tiers model.

- [ ] Fold the agent model into agent-arrangement? (2026-09-29,
      the reviewer)
      Context: agent-arrangement reasons from `docs/models/agent.md`
      and states a few of its facts itself, each beside a pointer.
      A fold would more than double the manual; keeping them apart
      costs a second file to open. On 2026-09-30 neither had drifted
      from the other.
      Ideas: the model as the manual's theory section, its binding
             and claims with it.
      Trigger: a change to the arrangement that has to edit both
      files for one fact. Met 2026-10-24: when a path rule loads
      changed in the model's §10.6 and in agent-arrangement §3.2
      (`36eb0c1`).
      See: devlog 2026-09-29, the agent model.

- [ ] Move the records table into a rule of its own, so every file
      has one `foundation`? (2026-10-24, the reviewer)
      Context: both entry files carry two `foundation` lines, the
      only files that do: the records table's comment names
      project-recording, the guard agent-arrangement. A skill
      points at another convention with `requires`; the table
      cannot point, since it must be present every session. A rule
      with no `paths:` loads every session too.
      Ideas:
      - `.claude/rules/records.md`, standing on project-recording;
        costs agent-arrangement §2.4, project-recording §13 and the
        container, and a reader of `CLAUDE.md` no longer sees where
        the records are.
      - at our seat the table is most of the entry file, which would
        keep three lines: the seats differ, or ours first gains what
        it lacks.
      Trigger: a third file that needs two `foundation` lines, or
      the entry file's next redesign.
      See: devlog 2026-10-24, the text-division item.

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
      Context: the `.part` files under `docs/conventions/`
      `repo-hygiene/templates/java-spring/` are pointed at by
      nothing, and three runs derived `.gitignore` by hand. They
      are spring-postgres (ADR-0029 decision 7) and move with the
      answer; until then they sit against decision 5's beside-it
      rule, an exception the ADR records. The walk named the wider
      gap: nothing ships a stack overlay, and a blind run cannot
      fetch one.
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
      Trigger: the next revision of `docs/conventions/exchange/`.

- [ ] Decide whether an overtaken reading still owes the run a note
      (2026-09-30, the reading of run 3).
      Context: the reading of 2026-09-24 was overtaken on 09-26 and
      deleted without one, so what run 3 had addressed to us since
      its pin had no verdict until the reading of 2026-09-30 read it
      again — three edits to copies, ten asks and offers.
      `docs/conventions/exchange/` §6.4 closes an overtaken reading
      "the same way", one pass over its items, and is silent on the
      note `docs/conventions/exchange/` §6.6 says every read ends
      with. Once so far.
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
      Trigger: the next change to `docs/conventions/agent-arrangement/`.
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

- [ ] Deduplicate the worked example (2026-09-17).
      Context: one document shipped twice, byte-identical in both
      skills' `references/`. Merging would make
      cbc-slice uninstallable without cbc-framing; diff polices
      the copies.
      Trigger: a reason to install one skill without the other.
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
      copy (`docs/conventions/exchange/` §2.3). Run 3's copy lacked
      `4de6ba2`'s shapes; no files went, so it never acted.
      Ideas: the note's "why it matters" names a change to the rule
             first, so the run takes it knowingly.
      Trigger: the first files delivered to a run still building,
               with `delivered-copies.md` changed since its pin.
      See: devlog 2026-10-18.

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)

- The postgres image tag floats (2026-08-28). The ground template
  and the harness reference both say `postgres:17`, so they can
  pull different minors at different times. Accepted: the shared
  major is a deliberate coupling, and no run has hit drift.
  Revisit: a run's first minor-drift surprise — then pin both
  tighter, to a full version or a digest.
