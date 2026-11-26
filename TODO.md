# TODO

<!-- Add items the moment they're discovered, so nothing has to be held in memory.
     Triage when closing a Plan Step. Delete from "Later" freely: deleting an
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
     added, and See points at it. An item that is its story's only
     home keeps it and has no See. Ideas are noted as they come and
     weighed only when the item is due. Each is then taken, extended
     or declined, and the verdict goes with the work. The talk that shaped an item may sit in
     TODO-CONVERSATION-MEMORY.md. When See names its section, it is
     read before the Ideas are weighed (TODO-CONVERSATION-MEMORY.md,
     its header comment). When an item changes, rewrite
     it true for today. Never stack a dated update on it: the
     change's story is the devlog's.
     Why the form is as it is: (docs/conventions/project-recording/
     §5.4, How an item is written).
     foundation: the project-recording convention -->

## Now (due while the open Plan Step runs)

## Next (each due at its trigger)

- [ ] Bring the model of the layers of knowledge to what is enough
      to work by; then finish the change work by it; then bring
      today's Maintainer Repo into it; and keep it true from practice
      (2026-11-14, the reviewer).
      Context: the draft is two documents, placed by layer in
      `knowledge/` (ADR-0084): the layers in any Problem Domain, `knowledge/backbone-ideas/layers-of-knowledge.md`, and
      the Maintainer Repo's Problem Domain Idea of them,
      `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`. It is the minimum
      written where how to keep knowledge is not yet known, a trial:
      practice changes it, and the ideas around it, such as Change.
      Each document's §5 holds its open questions. Change, in keeping knowledge,
      §3, holds the open points of how a change travels,
      each beside its part's rules, with its trigger.
      Ideas:
      - the change work: its rules in Change, in keeping knowledge, §3,
        how each was chosen in the simulation; depth c at its trigger
        (its item);
      - a piece of work modeled at each layer, in a document of its
        own, starting from `cbc-concept/ideas/`, to see how ideas are
        kept at each layer;
      - today's Maintainer Repo brought in: its ideas, manuals and
        Agent Skills, each to its layer; a text goes once everything
        it holds has landed, or has been judged not needed (ADR-0082).
      Trigger: due now.
      See: `TODO-CONVERSATION-MEMORY.md` §35, *The layers of knowledge*.

- [ ] Simulate depth c, then bring the Change idea to it
      (2026-11-22, the reviewer).
      Context: depth c is a lesson that changes the idea above: a
      Problem Domain Idea at layer 2, or a Backbone Idea at layer 1.
      The survey of Change, in keeping knowledge, §3.4 holds a first
      guess: each text built on the idea is asked whether it still
      fits. It was never walked through Deliver the Kit Update and
      Take the Kit Update, nor drawn. Until it is, the first guess is
      worked by, and the judge-copy-changes Agent Skill stops at depth
      c and asks the human.
      Ideas:
      - layer 2 first, then layer 1, each walked against depth b as
        the simulation's §2 says, writing only what differs; its
        pictures by a visual comparison in the flow file;
      - then the Maintainer Repo's own new idea, a source the
        simulation's §2 leaves for later: only its start may differ;
      - questions likely met: whether other Backend Repos fall behind
        too; what the Update Note's why says; at layer 1, how far
        down the survey reaches (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`
        §3.4, *Act on the verdicts*, its *Open*);
      - the Adapted Cases the split writes follow what depth c
        changes, both halves (2026-11-24, the reviewer);
      - depth c is the first change that starts at an idea and must
        reach every text built on it. It answers the Backbone Idea
        Change's open question on such a change, first a guess: carried
        to all layers together (2026-11-24, the reviewer).
      Trigger: the first lesson judged at depth c, in a Backend Repo's
      reading.
      See: devlog 2026-11-22, the depth c item.

- [ ] Sweep the drafts for words that read as walking commits, where
      Read Copy Changes compares two snapshots (2026-11-13, the
      reviewer).
      Context: Read Copy Changes compares two snapshots and never
      walks commits (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.2,
      *Read Copy Changes*). "Runs from … to main" and "across that span"
      read as a walk in the problem file's rules on reading, cut on
      2026-11-19; the same words may stand in other drafts.
      Trigger: the map reaches the drafts that hold these words.

- [ ] Do the problem file's next pass: §6 and §8, Failure Case 15,
      the rest of the "project-agnostic" sweep, and §2.2's "middle
      level" (2026-11-22, the reviewer).
      Context: found on 2026-11-18, and written since only in the
      devlog. The Change idea's move rewrote the problem file's §2.1
      and its Defined Terms first, so each line changes once. Each
      fault is checked again now it is due.
      Ideas:
      - the problem file's answers that belong in the layers
        document move there: §2.1's table of the two groups of
        understanding; the lines of the Repo Responsibility lists
        that retell the layers document; §8's middle-level option,
        which the layers model answers.
      Trigger: the map reaches the problem file.
      See: devlog 2026-11-18, later, *Found, not fixed*, item 5.

- [ ] Confirm the Common Ground Problem in the reviewer's words
      (2026-11-05, the reviewer; an item since 2026-11-19).
      Context: the problem is drafted in
      `temp/common-ground/common-ground-problem.md`, purpose first,
      and polished one insight at a time. The reviewer has not yet
      said it is right. Its §1 and §7 hold the goal of the whole
      knowledge work (ADR-0082).
      Ideas:
      - the problem as an idea of its own, which the layers model
        answers, the layers documents pointing up to it in one line
        as their purpose. A first guess, looked at again when due:
        how the idea looks, what goes, what stays, what changes and
        what is new. One shape met so far: its general part, the
        purpose, the five Knowledge Axes and most Failure Cases, a
        Backbone Idea; the Maintainer Repo's part, the Repo
        Responsibility, §2.2 and the Failure Cases between repos,
        its adaptation.
      Trigger: the rewrite of today's repo done, on the reviewer's
      word.
      See: ADR-0082; `TODO-CONVERSATION-MEMORY.md` §31, *Keeping what
      we know true*, in git at `60f692d`.

- [ ] Sort where common ground was lost, by cause, with counts
      (2026-11-05, the reviewer; an item since 2026-11-19).
      Context: two parts. First, the repo set against what the
      problem file says it is meant to keep, its §2.1: what it does,
      and what it does not; its descriptions of itself, such as
      `CLAUDE.md` and `ARCHITECTURE.md`, checked for intent written as
      if it were now (Failure Case 17). Then where common ground was
      lost: the devlog's "What context was missing" lines, the
      refinement's findings and the agent's memory notes.
      Ideas:
      - a sample sorted by the problem file's Failure Cases, so each
        gets its count; a failure none fits is a new Failure Case;
      - the sources as the closing Plan Step counted them: 18 devlog
        lines since October, 485 findings in round 3's close read,
        385 in the last read.
      Trigger: the Common Ground Problem confirmed.
      See: ADR-0082; `TODO-CONVERSATION-MEMORY.md` §31, *Keeping what
      we know true*, in git at `60f692d`.

- [ ] Draw two real cases side by side, and decide whether one fits
      both (2026-11-05, the reviewer; an item since 2026-11-19).
      Context: one case drawn and defined, as `cbc-concept`'s step
      drawings did one change; a second beside it, from outside this
      repo, such as a CBC Run, since the problem holds wherever a
      human works with an agent. Then it is decided whether one fits
      both, the two stay apart, or one general one is drawn. The
      layers model already answers part of it.
      Ideas:
      - the simulation's case, a Backend Repo's change, may be the
        first; the judged findings of CBC Runs 4, 5 and 6 may give
        the second.
      Trigger: where common ground was lost, sorted.
      See: ADR-0082; `TODO-CONVERSATION-MEMORY.md` §31, *Keeping what
      we know true*, in git at `60f692d`.

- [ ] Choose the way to keep what we know true, set against one home
      per fact (2026-11-05, the reviewer; an item since 2026-11-19).
      Context: the way is written with what it keeps true, what it
      lets go stale, and what one change costs. It answers the
      problem file's §7, *What would show it's solved*.
      Ideas:
      - not everything must stay true, since history cannot go stale;
      - check a text when it is about to be used, not by a sweep;
      - if this repo's rules steer the answers, the reviewer or the
        agent says so when it is felt, and the reviewer decides then.
      Trigger: two real cases drawn side by side.
      See: ADR-0082; `TODO-CONVERSATION-MEMORY.md` §31, *Keeping what
      we know true*, in git at `60f692d`.

- [ ] Map today's Maintainer Repo for the rewrite: each text, the
      parts it holds, the layer each part goes to, and which text
      needs another first (2026-11-23, the reviewer).
      Context: the rewrite brings today's texts into the layers model
      part by part, and a text goes once all it holds has landed or
      been judged not needed (ADR-0082, decision 2). A question many
      texts share is decided once, on the map, not text by text.
      `temp/rebuild-inventory.md` lists 28 Work Approaches and the 16
      ideas behind them, counted on 2026-11-03 for the rebuild in
      `cbc-concept`.
      Ideas:
      - first, the 14 items whose trigger was the refinement's close,
        on 2026-11-02: each goes into the map, is done before the
        rewrite, or is dropped, since most are about texts the rewrite
        replaces;
      - the inventory brought up to date, not started again;
      - which of today's ideas are Backbone Ideas, open question 4 of
        the keeping-knowledge layers document;
      - how much is rewritten, decided here by what the map shows,
        with the aim of getting back to the projects soon
        (2026-11-26, the reviewer);
      - a later update to a CBC Run born before names the renames in
        its Delivery Note, once (from the Plan Step that reads and
        judges CBC Runs 4, 5 and 6);
      - the lessons in §7 of the three CBC Run Readings, for
        working-a-reading and the exchange-read Agent Skill (from the
        Plan Step that reads and judges CBC Runs 4, 5 and 6).
      Trigger: CBC Runs 4, 5 and 6 judged.
      See: devlog 2026-11-23, the order before the rewrite.

- [ ] Decide whether the rewrite takes the Approaches on Trial and
      check scripts the CBC Runs wrote (2026-11-26, the judging of
      CBC Runs 4, 5 and 6).
      Context: four Approaches on Trial were offered: birth (CBC Runs
      5 and 6), checks and identity (CBC Run 5), release (CBC Runs 5
      and 6). The CBC Runs wrote their own check scripts, such as a
      fresh-clone check, a commit guard and a close tool. CBC Run 6's
      records check could not fail for four steps: a check is seen
      failing before it is trusted. Held, not evaluated: the rewrite
      may replace the texts they would change (ADR-0089).
      Trigger: the map decides whether the rewrite's kit ships
      Approaches on Trial and check scripts.
      See: `temp/reading-run-6-2026-11-26.md` §5, *Decisions*; devlog
      2026-11-26.

- [ ] Decide how much a CBC Run records against what it builds
      (2026-11-26, the judging of CBC Runs 4, 5 and 6).
      Context: CBC Run 6 wrote 58,266 words of record against 17,594
      of code and tests, about 3 to 1; its 7 slice records alone hold
      16,329. CBC Run 4 wrote 39,162 words against 457 lines of main
      Java, about 85 words a line. The slice records' line limits are
      another item's, taken for the slice-record shape.
      Trigger: the map decides which records the rewrite keeps.
      See: `temp/reading-run-6-2026-11-26.md` §6, *The work*.

- [ ] Decide what becomes of the branch `experiment-simulation-auto`
      (2026-11-19, the reviewer).
      Context: 9 commits on the simulation, of 2026-11-12, kept, not
      merged. 8 were taken onto `knowledge-2026-11-05`, now in main.
      The one left, `401e68b`, puts an "Its rules:" line under each
      part heading, pointing at the problem file's rules, which were
      cut on 2026-11-19 (`71dfe16`).
      Trigger: the reviewer's word.
      See: devlog 2026-11-12, the simulation made plain.

- [ ] Decide whether a Maintainer Kit should exist, for a new
      Maintainer Repo to be born from (2026-11-14, the reviewer).
      Context: one Maintainer Repo exists, so a kit would be written
      from one example and no repo would be born from it yet. The
      question and its facts are the draft's.
      Trigger: a second Concept Repo.
      See: `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §5, *Open questions*,
      "A kit for new Maintainer Repos".

- [ ] Decide how a second kit reuses the Backend Kit's group for
      keeping knowledge: a copy of its own, or one group both kits
      share (2026-11-24, the reviewer).
      Context: the steps a Backend Repo takes to change a Kit Copy and
      to take a Kit Update name nothing of backends; the simulation
      used nothing of them. Each Problem Domain has its own set at
      layer 3, never shared (ADR-0084, decision 5;
      `knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The
      Problem Domain layer*, its **Rules**), so a copy is the way
      today. One shared group changes that rule.
      Trigger: the second Problem Domain that needs a kit.

- [ ] Design how a document is refined: a broad Adapted Case, an
      Output Shape read after the work, and how each corrects the
      other (2026-11-12, the reviewer).
      Context: the reviewer asks for a refinement by hand today, and
      the agent chooses the checks each time. On 2026-11-12 nine
      checks were run on `temp/common-ground/backend-repo-change-simulation.md`. An
      Output Shape is read after the work, and changes when an output
      differs from it (`docs/conventions/shapes/` §2.3, *Not a convention*;
      §3, *Where an Output Shape lives*). One run on one document is
      not yet a form to derive from.
      Ideas:
      - the Adapted Case describes a refinement broadly, names no
        checks, and tells the agent to find them itself;
      - an Output Shape says what a refinement's report holds; the
        nine checks are its first draft;
      - the output holds what the Output Shape lacks: the Output
        Shape gains it;
      - the Output Shape holds what the output lacks: that check is
        run again;
      - the agent does not read the Output Shape before it works, or
        it becomes a list to tick;
      - the walk of one case through every part comes before the
        wording, since it changes what the text says;
      - which checks a script runs and which need a read by eye;
      - where the Output Shape is read is the item "Decide where
        small work is gated when it is too small for a Plan Step";
      - our own Output Shapes are the item "Decide whether our own
        forms become Output Shapes".
      Trigger: a second document is refined by the reviewer's ask.
      See: devlog 2026-11-12, the checks run on the simulation;
      `TODO-CONVERSATION-MEMORY.md` §34, *Refining a document*.

- [ ] Decide where small work is gated when it is too small for a
      Plan Step (2026-11-12, the reviewer).
      Context: an Output Shape is read at a Plan Step Gate, when the
      Plan Step closes (`docs/conventions/shapes/` §3, *Where an Output Shape lives*).
      A document is refined inside a Plan Step, when it needs it, and
      that work is too small to be a Plan Step. So nothing reads its
      Output Shape. Any small work that needs a check at its end has
      the same gap.
      Ideas:
      - a Plan Step of its own;
      - separate work inside a Plan Step, with gates at its end: it
        looks like a Plan Step and is not one;
      - a commit plan's close, which already says what diverged.
      Trigger: the item "Design how a document is refined" is worked,
               or other small work needs a check at its end.
      See: devlog 2026-11-12, a refinement's Output Shape;
      `TODO-CONVERSATION-MEMORY.md` §34, *Refining a document*.

- [ ] Sort the simulation of what passes between the repos, and drop
      it: `temp/common-ground/between-repos-simulation.md` (2026-11-10,
      the reviewer; sort and drop, 2026-11-23).
      Context: the simulation grew into designing the whole exchange,
      and was frozen after scenario 3: scenarios 0 to 3 written, 4 to
      8 not. The Common Ground Problem took one case instead: a
      Backend Repo changes a Backend Kit Copy. That case grew into the
      Change simulation and Change, in keeping knowledge, §3, which hold the
      draft's §5.2, steps 2 and 3, and §5.3. Three parts live only in
      the draft:
      - birth, §5.1: choosing the kit, the delivery and its separate
        check, the start, the first session's prompt, the cleanup.
        Change, in keeping knowledge, §3.2, points at it for the start;
      - an idea's repo, §5.0: the brief worked in a repo of its own,
        on a branch, main made from its cleaned history;
      - 18 *Changed from today* findings, which the sorting of where
        common ground was lost needs, and two Failure Cases it noted
        that the problem file's §4 lacks: context from the Maintainer
        Repo written into a brief, and an agent reading the Maintainer
        Repo on disk.
      The draft goes once each part has landed, or is judged not
      needed (ADR-0082).
      Ideas:
      - its names for a repo and a kit of any kind of system, kept
        from before ADR-0086, as its header says: settled first;
      - birth as a case of its own, as the Copy Change became; Change,
        in keeping knowledge, §3.2 asks it for the delivery check
        writing the Backend Repo's register row, with the *settled
        snapshot* set to the start;
      - each *Open* field, with its trigger, lands with its part;
      - scenarios as checks: how the alert fires was to be decided
        once the simulation was done (2026-11-09, the reviewer);
      - the birth's branch: one option was chosen, a branch cut from
        main; the other, going on in the same branch, still needs a
        trigger to check and confirm it (2026-11-10, the reviewer).
      Trigger: the Common Ground Problem is finished.
      See: devlog 2026-11-10, the simulation frozen;
      `TODO-CONVERSATION-MEMORY.md` §31, in git at `60f692d`.

- [ ] Split the concept into general understanding, the Backend
      Kit's backend case and their instructions, losing nothing
      (2026-11-08, the reviewer).
      Context: CBC design fits any system, not only software. The
      Backend Kit holds one Adapted Case of it so far, for backends.
      Today `concept/` holds both in one text, its examples and words
      leaning toward software, and the Method Group's Agent Skills
      stand on it. `concept/` and the Method Group are first labelled
      general or backend, labels only, nothing rewritten. The split
      waits for the way chosen, so that way shapes it. No fact or
      step of the concept or the
      methods may be lost.
      Ideas:
      - the three parts as layers (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md`):
        CBC design as a Backbone Idea in layer 1; its Problem Domain Idea
        for backends in layer 2; framing, slicing and the like as
        Adapted Cases in layer 3, worked by in layer 4 (2026-11-16,
        the reviewer);
      - the labels as the split's input;
      - the concept's software examples may go with the backend case,
        which meets the item on whether the concept keeps examples;
      - concept v2's release may carry it, since every CBC Run pins a
        concept version;
      - the Backend Kit's description of CBC system design, for a
        Backend Repo's readers, is decided with it: its form, such as
        a README paragraph, a longer text or a playbook part, and
        whether a Backend Repo may change it (the layers document,
        §3, the Backend Kit's item 5);
      - whether infra, the stack, is only a bigger set of input to
        the backend case, not a complexity of its own (2026-11-07,
        the reviewer's question, not yet answered).
      Trigger: the way to keep what we know true chosen (the item
      that chooses it).
      See: devlog 2026-11-08, CBC design beyond backends;
      `TODO-CONVERSATION-MEMORY.md` §33, *CBC design beyond backends*.

- [ ] Rewrite the Agent Model into the layers of knowledge: how an
      agent works as a Backbone Idea, a Problem Domain Idea of it in
      each Problem Domain, and Adapted Cases written from each
      (2026-11-16, the reviewer).
      Context: the layers model plans how an agent works as a
      Backbone Idea, rewritten from the Agent Model
      (`docs/models/agent.md`). It holds what one piece of agent
      work is: what the agent does, when, where and how
      (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.1, *The Backbone
      Idea layer*). Each Problem Domain holds its own Problem Domain Idea
      of it (§2.2 there).
      Ideas:
      - the same shape as the concept's split, the item above;
      - the two Problem Domain Ideas of it are written apart, each its
        Problem Domain's own; what both hold goes up to the Backbone
        Idea (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2,
        *The Problem Domain layer*);
      - the piece of work, split off as a Backbone Idea of its own if
        a second Backbone Idea uses it; both then point at it
        (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.1, *The
        Backbone Idea layer*);
      - `CLAUDE.md` comes in whole then, its Local Rule among its
        lines: no understanding text for one line before the rest
        (2026-11-23, the reviewer);
      - the Backend Kit's *At the gate*, the gate's part of closing
        one of the Backend Repo's Plan Steps, is written with how a
        Backend Repo closes a Plan Step, in how an agent works, in
        CBC backend design. Its form, an Agent Skill or a step of
        the close, is decided then. Its why stands in
        `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md`
        §2, *Changing a Kit Copy*; its steps in the simulation's §3,
        step 2 (2026-11-25, the reviewer).
      Trigger: with the concept's split.
      See: devlog 2026-11-16 and 2026-11-18, layers 3 and 4 read back.

- [ ] Check `cbc-concept` for ideas not yet taken in here, then drop
      it (2026-11-19, the reviewer).
      Context: the rebuild in `cbc-concept` ended (ADR-0082). The
      reviewer will not go back to it, but it holds ideas to consider
      once, among them ten in `cbc-concept/ideas/`, such as plan,
      gate, change and one home. The repo is kept only until this
      check.
      Ideas:
      - the reviewer reads it manually first; then the agent checks it
        for ideas not yet taken in here; then it is dropped.
      Trigger: the Agent Model's rewrite reaches the piece of work as a
      Backbone Idea (the item above).
      See: ADR-0082; ADR-0081.

- [ ] Try CBC design on the finished Common Ground Problem, beside
      the way chosen (2026-11-08, the reviewer).
      Context: the Common Ground Problem draft already reads in part
      as a CBC design: its purpose as a Falsifiable Promise, its
      Failure Cases as sources of adversity, its checks of being
      solved as how it could be falsified. It lacks System Guarantees
      and Structural Walls. Today's answer to stale text is detection:
      sweeps, and checks at each commit. The trial waits for the
      concept's split, and for a way chosen without CBC to compare.
      Ideas:
      - each change sorted first: a feature, or a change that touches
        a System Guarantee; only the second gets the full analysis;
      - if it holds, the Maintainer Repo's own Adapted Case of CBC
        design, with its instructions;
      - the risks seen: a Structural Wall is hard to build in text;
        part of the system is a person; the repo is judged by the
        concept it keeps.
      Trigger: the concept's split is done.
      See: devlog 2026-11-08, CBC design beyond backends;
      `TODO-CONVERSATION-MEMORY.md` §33, *CBC design beyond backends*.

- [ ] Land two facts from the agent's memory in the exchange
      convention (2026-11-08, the reviewer).
      Context: two facts lived only in the agent's memory until the
      first session-end check moved them here. Main's history is never
      rewritten: a CBC Run's Delivery Pin names a commit on main, and
      CBC Run 4 was born from `35edd3f`. And this repo never drafts a
      CBC Run's next opening prompt: at a step's end it gives one
      hand-back line, and the run decides how it continues.
      Ideas:
      - their home: the Exchange Convention, which owns pins and
        readings, and `.claude/rules/working-a-reading.md`; or an ADR
        for the first.
      Trigger: the Exchange Convention is next changed, in the rewrite
      or before.

- [ ] Write the understanding of the agent's memory, and how it is
      checked (2026-11-07, the reviewer).
      Context: the agent keeps notes outside the repo, one folder for
      each project folder, its index loaded every session, each note
      read when it seems relevant. They are not in git, and the
      reviewer rarely reads them; the repo's Agent Model says the repo
      is the only durable memory (`docs/models/agent.md` §2, §6). A
      session-end check of them is on trial in `CLAUDE.local.md`.
      Ideas:
      - the kinds of note and where each belongs: the reviewer's
        working rules to `CLAUDE.local.md`, a fact of the repo to its
        records, a lesson about the agent itself to its memory;
      - the check compares names and dates with the last check's
        list: new, deleted, changed, unchanged; the first check sees
        every note as new; what changed inside a note shows only in
        the agent's own report, with nothing to compare against;
      - where the list lives: the devlog on trial, safe if lost, since
        every note then counts as new; or a home of its own;
      - a command to run the check at any moment, on memory, the chat
        or both, with or without the list: a full check without it;
        not named /context or /memory, which Claude Code already has;
      - git inside the memory folder, dropped: a second repo and
        commit rhythm against a risk not yet met.
      - the check by name and date finds only notes the agent edited;
        a note made stale by a change in the repo around it shows only
        in a full review, as on 2026-11-07, or when where common
        ground was lost is sorted.
      - names in the agent's memory: a Defined Term or a narrowed
        word in a note sits outside the repo, where no Borrow Table
        or collision search reaches it. From the glossary item,
        closed 2026-11-23.
      Trigger: the session-end item is decided, or the Agent Model is
      reworked, whichever comes first.
      See: `TODO-CONVERSATION-MEMORY.md` §32, *The agent's memory*.

- [ ] Try a multi-agent refinement of the Common Ground Problem
      (2026-11-07, the reviewer).
      Context: one agent edits a document from a snapshot: a fix in one
      place can break another unseen, as "level" did and as renames
      missed uses until a grep. A core agent, the only one that edits,
      would take reports from checker agents, ask the reviewer where a
      choice is theirs, apply, and re-check what each change touched,
      until a pass finds nothing new. Tried on one document first.
      Ideas:
      - split by rule, not by idea: one home, locked words, Defined
        Terms written whole, references, contradictions need the whole
        document; plain writing can be split by part;
      - a mistake is a breach of the document's own rules: its Defined
        Terms lead, the writing rules found, intent kept from today;
      - measure it against the three fresh reads: what it found, what
        it cost, whether it converged; one fresh read was about 40,000
        tokens, a run could reach half a million;
      - it may be one answer to the problem itself, a Knowledge Drift
        Repair by agents, close to layering v2's agent for each chain;
      - only then decide whether it becomes a rule, an Agent Skill or
        nothing; at milestones, not on every change.
      Trigger: the draft's renames done, in place of its fourth fresh
      read.
      See: `TODO-CONVERSATION-MEMORY.md` §31, *Keeping what we know
      true*, its part of 2026-11-06 and 2026-11-07, in git at `60f692d`.

- [ ] Land the writing rules found in the problem draft (2026-11-06,
      the reviewer).
      Context: writing `temp/common-ground/common-ground-problem.md` found rules the
      writing rule lacks, each in force there on trial: a plain word
      keeps one meaning in a text ("time", "place", "seat", "case",
      "kind", "level" each carried two); an exact meaning gets a Name,
      capitalized, defined at the start of a text that alone uses it;
      a definition names what it builds on by its Name, not its place;
      a Name is never shortened by sharing words with another, as in
      "Task and Session". Writing rule 9 covers defined Names only.
      Ideas:
      - a check at the commit: does any word in this text mean two
        things?
      - a fifth rule found: a numbered thing is in parentheses when it
        is a pointer, "(Failure Case 15)", bare when it is the subject
        of its sentence, "In Failure Case 11 the text matches".
      Trigger: this repo's writing rule is reworked, once the repo is
      fixed.

- [ ] Move this repo's own lines out of the Defined Terms Problem
      Domain Idea, into this repo's Adapted Case for Defined Terms
      (2026-11-23, the agent, on the reviewer's question).
      Context: two lines of
      `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md`,
      at layer 2, hold for this repo alone: §4's rule that a name
      from a text not yet in the layers model, such as a Glossary
      Name, is borrowed the same way, needed only while the rewrite
      runs; and §6's question 1, which names writing rule 9 and
      `knowledge/`. A text is written in the layer it belongs to:
      theirs is layer 4, `.claude/understanding/defined-terms.md`.
      Trigger: the next change to the Defined Terms Problem Domain
      Idea, or the rewrite's end, whichever comes first.
      See: devlog 2026-11-23, the `knowledge/` plan's Defined Terms
      commits.

- [ ] Write the exchange-birth Agent Skill while a CBC Run Birth runs (2026-09-26, the
      reviewer).
      Context: written from the exchange manual, as the exchange-read Agent Skill
      and the exchange-deliver Agent Skill were, keeping the Pure Seed's intent — it
      delivers everything and decides nothing. Then *What this does
      not do* in `.claude/skills/exchange-deliver/SKILL.md` points at
      it, `pure-seed.md` goes, and ADR-0016's procedure of record
      moves. CBC Runs 5 and 6 are born by the Pure Seed, to keep their CBC
      Run Births small.
      Ideas: first-time work on our Convention Seat, so an Approach on Trial
             drafted by the approach-drafting Approach on Trial (ADR-0058).
      Trigger: the CBC Run Birth after CBC Run 6's.
      See: devlog 2026-09-26, evening; and 2026-09-30, night,
      later, where `pure-seed.md` was brought up to date for it.

- [ ] Decide whether a commit plan's look-back also asks if the
      work could have been done better (2026-10-21, the reviewer).
      Context: before its close, the commit-plan Agent Skill looks back at the
      landed commits for their grouping only. Work shows what a plan
      missed; the reviewer would have the look-back ask whether the
      work itself could be meaningfully better, and if so try that
      way and compare it with the first try before keeping one. CBC
      Run 4 tried the options of each question it must not decide
      alone on `try/` branches: 14 of them, and 2 changed the answer. CBC Run 5 tried it from
      its CBC Run Hand-off: 13 look-back lines, 0 tries (its CBC Run Reading of 2026-10-22, FINDING-9). CBC Run 6's found nothing 12 times, and it struck the look-back (its RETRO's D9).
      Ideas:
      - a bar for "meaningful": it changes a Structural Wall, a test's
        adversity, or removes a part; rewording is not enough.
      - the better way on a `try/` branch, compared, and the try not
        chosen kept on its branch.
      - a cap on its cost, so no plan doubles by habit.
      Trigger: the commit-plan Agent Skill is rewritten.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §9, *A commit plan's look-back at the way*.

- [ ] Decide whether the concept, the conventions and the
      Approaches on Trial keep examples (2026-10-21, the reviewer).
      Context: CBC Run 4 read CBC Run 3's real Enemy Collision Kills in the Output Shapes' examples
      at birth, and its CBC Framing copied them in places (ADR-0061).
      The method's worked example, 328 lines in both the cbc-framing
      and the cbc-slice Agent Skills, is an order service that weighs "Orders are
      never lost AND payment always completes"; the concept's
      chapters, the cbc-slice workflow, the playbook, `writing.md` and
      the stack's references hold smaller ones. CBC Run 5,
      `event-tickets`, was born with all of them.
      Ideas:
      - examples stripped to a description of what must be done.
      - examples kept, drawn from a domain no CBC Run will build.
      - examples kept where a reader learns, gone where a CBC Run acts.
      - a second worked example on another kind of problem, keeping
        this one: CBC Run 5 framed two Responsibility Areas and a
        LAYER-5 not empty (its CBC Run Reading of 2026-10-22, §4, *What run 5 teaches
        the worked example*).
      - the worked example shows that one claim may hold two halves:
        CBC Run 6 framed one claim for both halves of its briefing,
        which the example rejects as overloaded, and it held through
        seven slices (its CBC Run Reading of 2026-11-26, TAUGHT-4).
      Trigger: the cbc-framing Agent Skill is rewritten.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §10, *Examples in the concept, the conventions and the approaches*.

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
      have the approach-drafting Approach on Trial; looking back was tried in CBC Run 5. CBC Run 5 delegated nothing.
      Ideas:
      - low effort to read and collect; the highest to find the
        options; medium or high to implement and summarise.
      - a lead agent fans out readers and keeps the decisions.
      - each delegation leaves one line: the kind of work, the
        model, the effort, whether it paid.
      - an Approach on Trial before any convention (ADR-0058); a
        convention of its own, or a section of agent-arrangement.
      - one default model for every subagent, offered by `/doctor`
        and held for this item.
      - before a new Agent Skill is proposed, search what exists: the
        plugin marketplace (`/plugin`, 315 plugins) and the account
        Agent Skills.
      - setup records stay in `.claude/decisions.md`, or user-wide
        switches (`~/.claude/settings.json`, every project) go
        elsewhere.
      - a table of what is on or off, each graded by its evidence
        (can't run here, no trigger, named trigger, regular work),
        what it does, where it applies; the first is in
        `.claude/decisions.md`, 2026-10-22, the account Agent Skills.
      - Agent Skills not ours (account, built-in, plugins) arrive and
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
      - `CLAUDE.local.md` repeats two rules, both the commit-messages manual's:
        commit on the word, and a stop at each boundary
        (`docs/conventions/commit-messages/` §2.4, *Commit on the word*). Yet agent-arrangement counts how often the agent stops as a
        setting (`docs/conventions/agent-arrangement/` §3.7, *`CLAUDE.local.md`*). Refinement Round
        2's FINDING-194 found it again.
      - "never rewrite main across 35edd3f" lives only in the
        agent's memory, unseen by any reader of the repo. Its
        failure is not noticing the moment, a rebase: a Local Rule
        for our `CLAUDE.md` (`docs/conventions/agent-arrangement/`
        §2.4, *How the Entry File is written*)?
      - what survives what, lived 2026-10-30: a model switch inside a
        session keeps the transcript; an agent the usage limit stopped
        keeps its transcript and resumes by `SendMessage`; a new
        session keeps the repo, the devlog's Resume line and the
        user's memory files only. The Agent Model §6 states the rule;
        the Tool Binding (`docs/conventions/agent-arrangement/` §5,
        *The Claude Code Tool Binding*) would hold the mechanics.
      Trigger: the Agent Model is rewritten.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §11, *How work is run by agents*; `.claude/decisions.md`, 2026-10-22, the account Agent Skills.

- [ ] Evaluate the auto-run Approach on Trial, for preparing a
      full-auto CBC Run (2026-10-22, the Plan Step that birthed CBC Run 5).
      Context: drafted for CBC Run 5 and used twice, for CBC Runs 5
      and 6 (`.claude/approaches-on-trial/auto-run.md`, its use note;
      CBC Run 6's note written at its CBC Run Birth's close, `e5bb8ca`). Its
      open questions: what in the CBC Run Hand-off is general enough for
      the Container Group, and whether the light read of the last CBC
      Run cost anything. The judging of CBC Runs 4, 5 and 6 gathered its
      evidence: full auto held in all three; the reviewer's message
      mid-run; the run file against the delivered forms; CBC Run 5's
      nine lessons for the next CBC Run; decision logs nobody read.
      Trigger: the next full-auto CBC Run's hand-off is prepared.
      See: devlog 2026-10-22; `temp/reading-run-6-2026-11-26.md` §6,
      *The work*.

- [ ] Decide how a Work Approach and an Output Shape divide an output: the
      Work Approach says what is done, the Output Shape how its output looks
      (2026-10-20, the reviewer).
      Context: an Output Shape is read at a Plan Step Gate only, so work written
      without it can show it wrong (`docs/conventions/shapes/` §3, *Where an Output Shape lives*).
      An Agent Skill that carries the output's form undoes that.
      the cbc-framing Agent Skill hands over `templates/registry.md` to fill in,
      for the output the Invariant Slice Entry Shape governs.
      the approach-drafting Approach on Trial's Stage 1 lists the parts a Work Approach
      file holds, the form of its own output.
      Ideas:
      - an Output Shape adapts: divergence is how it learns
        (`docs/conventions/shapes/` §2, *What an Output Shape is not*), and an Output Shape that never
        changes is finished or unread (`docs/conventions/shapes/`
        §5.2, *Ticks and differences*).
      - a Work Approach is written without the output's form; a part an
        Output Shape needs is asked for as content, in the Work Approach's own
        words.
      - such an ask carries a Fact Reference to the Output Shape only for
        the Change Walk; the
        Output Shape says it is read at a Plan Step Gate.
      - a part may be optional, and the Output Shape marks it so.
      - a part considered and empty says "none, because…", so it
        reads differently from one left out.
      - a part never asked for is a fifth kind of difference, beside
        the four a Plan Step Gate ends one in
        (`docs/conventions/shapes/` §5.2, *Ticks and differences*):
        the fix goes to the Work Approach, and the output records
        the gap.
      - Refinement Round 2's FINDING-211: one form told in an Agent Skill, an Output Shape
        and an Agent Skill Template: the Invariant Slice Record's outline, the
        Structural Wall Backstop at the Red Run, a cost's size, the Invariant Slice Entry's fields, a
        body asserted by path.
      - a document's refinement is a case of it: the item "Design how
        a document is refined".
      Trigger: the approach-drafting Approach on Trial's first evaluation, at the
               refinement's close.
      See: devlog 2026-10-20, later; `TODO-CONVERSATION-MEMORY.md` §2, *How an approach and a shape divide an output*.

- [ ] Decide whether the approach-drafting Approach on Trial becomes a convention
      (2026-10-27, the reviewer).
      Context: `approach-drafting.md` is on trial (ADR-0058), held
      word for word in both Convention Seats until its evaluation (ADR-0069,
      decision 2). No manual lists it.
      Ideas:
      - one convention for Approaches on Trial, its Work Approaches
        the approach-drafting Approach on Trial in both Convention Seats and the approach-evaluation one
        in ours.
      Trigger: the approach-drafting Approach on Trial's evaluation at the
               refinement's close, at the approach-evaluation Approach on Trial's Stage 5.

- [ ] Choose whether a manual is called a concept (2026-10-19, the
      reviewer).
      Context: one idea should have one word. The reviewer saw a
      manual as a concept: an idea written down, with sub-ideas,
      and its rules and Agent Skills as the convention. "Concept" already
      names this repo's concept and the Tiers Model's concepts tier.
      Facts-in-sync calls both a Canonical Description
      (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).
      Ideas:
      - a manual is a concept; its rules and Agent Skills, the convention.
      - "description" stays the general word, as facts-in-sync has it
        (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*).
      Trigger: a second Concept Repo, when what a concept is gets
               decided (`docs/models/idea-to-output.md` §5, *An Idea Model and a concept*).
      See: devlog 2026-10-19, the redesign's ideas.

- [ ] Decide whether a sweep checks one home after work lands, and
      when (2026-10-22, the reviewer).
      Context: the Foundation Check walks what derives from a
      changed Canonical Description at each commit, and the commit-plan Agent Skill's close
      sweeps for names a Change Set moved. Nothing looks back over finished
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
        reads the findings since the last one and ends each: Entry
        File, Agent Rule, Agent Skill, record, or nothing.
      - how the sweep stands to the retrospective Agent Skill, a CBC Run's look-back
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
        the commit-plan Agent Skill's sweep, a Refinement Round, a CBC Run Reading
        and the missing-context finding. What a check is
        in the Idea-to-Output Model; when each runs, in its own
        convention.
      Trigger: the refinement's close.
      See: devlog 2026-10-21, evening; `TODO-CONVERSATION-MEMORY.md`
      §11, *How work is run by agents*, the `claude-md-management` part, and §14, *A sweep, and what looking back is*.

- [ ] Decide how an item names the items it waits on, and what
      happens when one closes (2026-10-24, the reviewer).
      Context: TODO sorts by section, Now, Next and Later, then by trigger; within a section,
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
        dropped. The moment is worth a Plan Step Gate item; lighter forms to weigh:
        only the items in the decision's area, a fresh agent, or only
        at a big piece of work's close.
      - a check of the chat, on trial in `CLAUDE.local.md` since
        2026-11-07: each correction or rule said only in the chat is
        placed or let go, and the agent's memory notes written or
        changed are shown to the reviewer. Three such rules were found
        at that session's end that lived nowhere else.
      - the agent's memory is not in git, so its changes leave no
        history, and the repo's Agent Model says the repo is the only
        durable memory (`docs/models/agent.md` §2, §6): add both to
        the problem draft (§3.1, and §2.2 as a gap seen); check
        what `/memory` covers; at each check, ask per note
        whether it stays, moves into the repo, or goes.
      Trigger: with "Decide whether a sweep checks one home after
               work lands", its twin; ADR-0063's kinds of text now
               say where either belongs.
      See: devlog 2026-10-22, later; `TODO-CONVERSATION-MEMORY.md`
      §12, *A session's end*.

- [ ] Decide how commits cited by hash can still be regrouped
      (2026-10-19, the reviewer).
      Context: our `commit-plan` Agent Skill regroups a Change Set's commits before
      its close (`docs/conventions/commit-plan/` §2.12, *The look back*), and a regroup gives them new hashes. This repo cites
      hashes in Living Text: the refinement's file, TODO, other
      commit bodies. So the refinement's commits up to `ccce6af`
      were not regrouped, and the history keeps every small fix,
      each reviewed as it landed.
      Ideas:
      - cite records, not commits: Living Text points at a devlog
        entry or a section; hashes only in history.
      - cite at the close: while a Change Set is open nothing durable
        cites its hashes; the close cites the final ones.
      - rewrite the citations with the regroup: a map of old hash
        to new, grepped and replaced in the same rewrite.
      - regroup only on the branch, before main takes it.
      Trigger: the refinement of this repo closes; its Refinement Rounds read the commit-plan manual and the Fact Reference's form
        (`docs/conventions/facts-in-sync/` §3, *The Fact Reference*).
      See: devlog 2026-10-19, regrouping.

- [ ] Make the conventions index a full Local Map (2026-09-30, the
      reviewer).
      Context: its order shows only the conventions that act in
      sequence during a piece of work. The other nine relate by what
      they govern, read or describe, stated as about thirty Fact References across the manuals' *What this does not cover*, and seen
      together nowhere. Project-recording's Local Map part now exists
      (`docs/conventions/project-recording/` §8.6, *Local Maps*, ADR-0045).
      Ideas:
      - all twelve and how each touches the others, derived from those references, built by the visual-comparison Agent Skill.
      - the four Chain Links (`docs/models/idea-to-output.md` §3.1, *The four Chain Links*),
        each with its upkeep: stands on
        (`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, the Foundation
        Check), points (one home, the grep at a commit that moves a
        section, a Plan Step's close), governs
        (none: a change to a rule that governs other text could
        sweep that text or file the sweep, a rule beside
        `docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*),
        written from (none named yet).
      - scenarios as entries into one procedure, the Foundation
        Check: a manual, an Agent Skill or Agent Rule, a CBC Run's finding. Two
        exits it lacks: the governs sweep, and what must run again
        after.
      - rename "The chain": the Idea-to-Output Model's chain is
        another thing. Not "hand-off", which names the full-auto
        CBC Run Hand-off and a CBC Run Ask.
      Trigger: due — the pair it waited on was made on 2026-09-30.
      See: devlog 2026-09-30, Local Maps; `cb41ade`.

- [ ] Decide whether our own forms become Output Shapes, and whether an
      Output Shape's part can be optional (2026-10-17, the reviewer).
      Context: an Output Shape is read at a Plan Step Gate only, so the work
      is not shaped by it (`docs/conventions/shapes/` §3, *Where an Output Shape lives*). Our own
      forms, a CBC Run Reading's and a manual's, are Agent Rules that load when
      such a file is read. They kept that place because this repo
      had no Plan Steps; since ADR-0057 it has. CBC Run 6 read its
      Output Shapes at the gate only: one rework per kind of output, at
      its first close, each finding a real miss, and nothing after (its
      CBC Run Reading of 2026-11-26, TAUGHT-2). CBC Run 4, holding them from birth, cut late at SLICE-1 too (its FINDING-39).
      Ideas:
      - the work's rules keep what must hold while working, such as
        numbers never changed; the forms become Output Shapes.
      - a part an Output Shape names may be optional, where the work does
        not always produce it.
      - Known already as questions, an Agent Skill's Gates and the
        playbook's lists, answered in a Plan Step's own words.
      - our documents' layouts are Output Shapes too, a case of the shapes
        convention: a manual's, a Work Approach's, a CBC Run Reading's, a
        record's. Five mechanisms hold them today.
      - read at a Plan Step Gate and adaptable like any Output Shape; the Work Approach
        or Agent Rule that writes the document carries no layout.
      - what must hold while writing stays an Agent Rule
        (`docs/conventions/shapes/` §3, *Where an Output Shape lives*): a
        manual's section order may; how each part is written may not.
      - `.claude/rules/convention-manual.md` is the manual's form. It
        stands on the conventions convention until this item
        decides; as an Output Shape, it would stand on the shapes convention.
      - a record's form, in its header comment, stays
        project-recording's: it is read when the record is opened,
        while an entry is written, which the shapes manual keeps for Agent Rules
        (`docs/conventions/shapes/` §3, *Where an Output Shape lives*).
        Only `.claude/decisions.md` and `docs/glossary.md` hold one
        under another convention: agent-arrangement and writing. The
        open forms are those in Agent Rules: a manual's, a CBC Run Reading's.
      - a text gets an Output Shape when there are many of its kind and a
        moment to check them: manuals, CBC Run Readings, Agent Skills and Agent Rules
        may; a record's entries are checked only as they are written.
      - Idea Models and the concept get none while nothing of their kind
        recurs: three Idea Models share no parts yet, and the concept has
        one form and one home (`docs/models/idea-to-output.md` §5, *An Idea Model and a concept*).
      - a refinement's report may be the first: the item "Design how
        a document is refined".
      Trigger: the map.
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
        `.claude/rules/writing.md`, so a refinement's Writing Finding Kind
        catches it after.
      - what is read most first: the README, our Agent Skills and
        Agent Rules, what ships.
      - the agent polishing alone, only where a rewrite cuts words;
        the reviewer checks each one for drift in meaning.
      Trigger: the refinement of this repo closes.
      See: devlog 2026-10-18, readability.

- [ ] Decide whether writing rule 10 reaches unnumbered headings
      (2026-10-30, the reviewer).
      Context: rule 10 binds a numbered section's title; its reason,
      that a title is read in every Fact Reference to it, reaches an
      unnumbered heading too. Refinement Round 3 found references
      cutting an Agent Skill's or a reference file's heading short, and 27
      unnumbered headings in the Method Group with a gloss after a
      dash or colon. The round read against the rule as written.
      Trigger: the refinement of this repo closes.
      See: `55e2bd0^:temp/refinement-2026-10-18.md`, DECISION-20 (`1aa928c`).

- [ ] Rename the manuals, Agent Skills and Agent Rules that share a
      name (2026-10-31, the reviewer).
      Context: five names are shared: commit-messages, commit-plan,
      visual-comparison and retrospective, each a manual and an Agent
      Skill; writing, a manual and an Agent Rule. Writing the kind
      word always keeps them apart in reading (the refinement's
      DECISION-24 and DECISION-27), but a grep still finds both. It waits for
      two reasons: which side is renamed, and to what, is a choice
      that how CBC Runs 4, 5 and 6 used these parts can inform; and
      all five names ship, so a rename moves every CBC Run's
      folders and commands, the paths a read compares by. Their
      records keep the old names either way, since a record is never
      updated. New names follow the naming rule of the
      refinement's design, ADR-0078.
      Ideas:
      - rename the manual, by its subject: commit-message-form,
        change-sets, diagram-choice, looking-back, plain-writing.
      - or rename the Agent Skill or Agent Rule, by its act:
        write-commit-message, plan-commits, compare-diagrams,
        hold-retrospective, write-plainly; all five ship, so every CBC
        Run gets new folders and commands.
      - a strict "verb first" grammar would rename 11 of the 12
        Agent Skills; a loose one 3, and lets commit-plan through.
      - no grammar parts a manual from an Agent Rule: both are nouns.
      Trigger: CBC Runs 4, 5 and 6 judged. A
               CBC Run born before then is built with the old names
               and joins them.
      See: `TODO-CONVERSATION-MEMORY.md` §27, *Shared names of
      conventions and approaches*.

- [ ] Write an Agent Rule that writes an Agent Skill or Agent Rule from its convention
      (2026-10-17, the reviewer).
      Context: the conventions manual says how an Agent Skill or Agent Rule is
      written (`docs/conventions/conventions/` §1, *A convention's Work Approaches*), and nothing puts it in front of the
      writer: a manual has `convention-manual.md`, an Agent Skill or Agent Rule
      has no such rule. An Approach on Trial writes freely, and its
      pieces are input: what the work needed. When an evaluation
      places one, the lasting form comes from the conventions manual: the manual by
      (`docs/conventions/conventions/` §2, *The Convention Manual*), each Agent Skill or
      Agent Rule from it by (`docs/conventions/conventions/` §1, *A convention's Work Approaches*).
      Ideas:
      - an Agent Rule derived from the conventions manual's Work Approaches part
        (`docs/conventions/conventions/` §1, *A convention's Work Approaches*), as
        `convention-manual.md` is from its manual part
        (`docs/conventions/conventions/` §2, *The Convention Manual*), on `.claude/skills/`,
        `.claude/rules/` and `delivery/`.
      - a Paths Rule loads only when a file is touched, and the
        commit is the other moment
        (`docs/conventions/agent-arrangement/` §5.6, *Rules files*).
      - the approach-evaluation Approach on Trial's placing hands each piece to the
        rule, for a Work Approach of ours and of a CBC Run's alike.
      Trigger: the first evaluation that places a piece as an Agent Skill
               or Agent Rule, at Stage 5 of
               `.claude/approaches-on-trial/approach-evaluation.md`.
      See: devlog 2026-10-17, later, the Agent Skill rewrite.

- [ ] Read text for its level in the chain, the Levels Finding Kind,
      both ways across each boundary (2026-10-31, the reviewer).
      Context: each level has its own job. An Idea Model states an
      idea any repo adapts; a manual says what a way of working is, how
      and why; the Work Approaches made from it state the rules, one
      sentence each, and explain nothing (`docs/models/idea-to-output.md`
      §6.1, *The manual's level*, ADR-0078). Text at the wrong level
      breaks that. Found at commit 5 of ADR-0078's commit plan: facts-in-sync §3.4
      first listed its six rules with almost no why; the conventions
      manual §1 holds the rules for writing an Agent Skill or Agent
      Rule, and no Work Approach carries them to the writer.
      Ideas:
      - the four cells: an Idea Model holding this repo's own rules; a
        manual retelling its model's idea; a manual stating rules
        with no why; an Agent Skill or Agent Rule explaining why.
      - per passage: which level it belongs to, and whether the level
        it belongs to already holds it.
      - the conventions manual §1 is the item above, "Write an Agent Rule that
        writes an Agent Skill or Agent Rule from its convention".
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
      Context: Refinement Round 3 rewrote the method's and the stack's
      texts, the concept chapters and System Readiness against the
      writing rule. FINDING-206 and 224 were gone by then, and the
      refinement's last read fixed 223, 227 and 228. What is
      left: the method's texts use parts of the concept chapters and
      never say which, so a change to a chapter finds no line here
      (the refinement's DECISION-43 and FINDING-1665).
      Ideas:
      - one Fact Reference per section that uses a chapter part
        (ADR-0072), such as (`docs/concept/03-cbc-framing.md`, *The
        derivation order*); the first one fires "Number the concept
        chapters' sections".
      - the chapters, one Canonical Description copied whole, need none
        between themselves.
      Trigger: the refinement of this repo closes.
      See: devlog 2026-10-17, later, the plain method;
      `TODO-CONVERSATION-MEMORY.md` §6, *The method's plain rewrite: `cbc-slice`'s opening*.

- [ ] Run this repo's retrospective, on trial (2026-10-17, from the
      Plan Step Gate of PLAN's Step 10).
      Context: `docs/conventions/retrospective/`, the Concept Deliverer's
      seat, says what it is: both retrospective Agent Skills run on this repo, from
      `delivery/container/`, and a verdict on whether we hold them.
      The Plan Step Gate of PLAN's Step 10 held it until ADR-0057.
      Trigger: the close of the refinement Plan Step.
      See: ADR-0057, decision 4.

- [ ] Judge the Conversation Memory trial (2026-11-01, the
      refinement's last read).
      Context: project-recording put `TODO-CONVERSATION-MEMORY.md` on
      trial (`docs/conventions/project-recording/` §14,
      *Conversation Memory*). The trial runs on as it is, three
      forms included, and is judged later, on the reviewer's word.
      If it holds, it reaches CBC Runs through the Container Group;
      if not, it goes.
      Trigger: the rewrite of today's repo into the layers model
      (ADR-0082) reaches the records.
      See: devlog 2026-11-01, the last read's work.

- [ ] Decide whether a delivery checks its paths against the CBC Run's
      own files (2026-09-30, the CBC Run Reading of CBC Run 3).
      Context: our shipped `.claude/rules/shapes-lifecycle.md` sat
      at CBC Run 3's own rule's path, so the Delivery Take landed ours over the
      CBC Run's. Two checks in the Exchange Convention miss it: one checks only that no path
      is claimed by two of our groups (`docs/conventions/exchange/` §3.4, *One group per file*);
      the Delivery Take's diff sees that a file differs, not whose it is
      (`docs/conventions/exchange/` §4, *The Delivery Take*).
      Once so far; checked by hand at `e6538f6`: no staged path was new.
      The Method Group's four Output Shapes sit at CBC Run 3's own `.claude/shapes/`
      paths (ADR-0052); they first landed at CBC Run 5's CBC Run Birth.
      Ideas: in the exchange-deliver Agent Skill, the staged paths against the
             CBC Run's files that are not at its Delivery Pin.
      Trigger: the next delivery that ships a path new to the CBC Run.
      See: devlog 2026-09-30, the delivery to CBC Run 3.

- [ ] Read the frozen CLAUDE template's stance bullets against a
      full CBC Run's derived Entry File (2026-09-06, the reviewer).
      Context: the template's method half, from the method's first
      walk, is frozen at `docs/baselines/claude-md-template-v1.md`.
      No CBC Run Birth can judge the stance bullets, the template's lines on
      how to work: only a CBC Run that has framed and built. Three
      texts to compare: the CBC Run's `CLAUDE.md`, frozen v1, and
      `cbc-derived-claude-walk1.md`; a Record Harvest re-enters the template
      only from that CBC Run Reading, each line traced to the CBC Run. CBC Run 3
      has had no Release; CBC Run 4 released the same project, so its
      Entry File is read, CBC Run 3's beside it.
      Trigger: the Agent Model is rewritten, where `CLAUDE.md` comes in
      whole.
      See: devlog 2026-09-06 (the template re-cut).

- [ ] Sort `docs/baselines/` by kind (2026-09-23, ADR-0035
      decision 6).
      Context: trial evidence is withheld so a later derivation
      measures independence; an Output Shape is withheld only until a
      Plan Step Gate. A wrong move destroys a measurement that cannot be
      remade, so this is a piece of work of its own, read with care,
      not a tidy-up. The Spring Invariant Slice reference opens once, at a CBC Run's Release
      (ADR-0033); CBC Run 3 has had no Release, and CBC Run 4 had one.
      Trigger: the map.
      See: devlog 2026-09-24.

- [ ] Decide which ideas here are Idea Models (2026-10-24, the
      reviewer).
      Context: three Idea Models exist: the Agent Model, the Tiers Model
      and the Idea-to-Output Model. An
      Idea Model comes from a convention whose idea is general enough to
      be used elsewhere (`docs/models/idea-to-output.md` §4.2, *The upward direction*). The
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
        project-recording's list of the records shows (the refinement's DECISION-12). Weighed against the Idea-to-Output Model, which holds part of
        it (`docs/models/idea-to-output.md` §2, *The kinds*).
      - the two checks on text kept true: the checks at each change,
        a refinement after, and a finding's cause the way back. A
        section of the Idea-to-Output Model, with its Chain Links and
        its way up, or with the one-home idea if that becomes a model.
      Trigger: the refinement's close.
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
      Trigger: a CBC Run's CBC Run Reading finds a convention misread for want
               of the Idea Model behind it.
      See: ADR-0063.

- [ ] Decide whether an Idea Model may be written for one convention
      (2026-10-23, the reviewer).
      Context: the text-division item had an Idea Model only where several
      manuals share an idea. The reviewer asked to weaken that: an
      Idea Model for one convention, "to see general idea behind that
      convention". The Idea-to-Output Model has an Idea Model come from a convention whose idea is
      general enough (`docs/models/idea-to-output.md` §4.2, *The upward direction*).
      Trigger: a convention whose idea another repo could use, with
               no second manual sharing it.
      See: ADR-0063; `30eb42e:TODO-CONVERSATION-MEMORY.md` §1.

- [ ] Decide whether a standing full read looks for missing Fact
      References, and for references pointing down (2026-10-27, the
      reviewer).
      Context: a line that relies on a fact written elsewhere and
      carries no Fact Reference is found by no grep and no Change Walk. The
      check of ADR-0070 asks it of each new or changed
      line at the commit. Only the refinement's Refinement Rounds read the whole
      repo for it today: their Dependencies Finding Kind, which two of Refinement
      Round 2's seven close-read agents ran, with 19 findings. The last
      read found it missed in text written after the check: FINDING-1625
      (`9435842`, 2026-10-30) and FINDING-1626 (`683febc`, 2026-11-01).
      Ideas:
      - its own piece of work: not the sweep, a grep at a plan's
        close, and not session end, which only records.
      - read by foundation: one agent reads a Canonical Description beside
        every file built on it, and asks of each line whether it
        relies on a fact and says where.
      - one Finding Kind per agent; other Finding Kinds may share the read, each
        with its own agent.
      - it reads against the reference's form
        (`docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is*).
      - a second Finding Kind for the same read: direction (ADR-0071). A
        line in an Idea Model or a manual that relies on a lower text is
        found by no grep either: telling relying from naming takes
        a read. Done by hand on 2026-10-28: the three Idea Models and 67
        manual paragraphs, 6 found, 3 of them references left at a
        fact's old home when it moved (`b7c17ae`).
      Trigger: the refinement's close.
      See: devlog 2026-10-28; `TODO-CONVERSATION-MEMORY.md` §21, *A full read for missing fact references*.

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
      - the scenarios:
        - a fact changed at its home;
        - a section renamed, renumbered or retitled;
        - a file renamed;
        - a fact moved to a new home, a placed Approach on Trial among
          them;
        - a foundation changed;
        - a derived file changed against its foundation;
        - a retelling whose host is itself a Canonical Description;
        - a CBC Run's id whose home changes;
        - a shipped line that retells a manual, when our manual changes;
        - a fact stated only in history;
        - a line with no Fact Reference;
        - a reference inside a living sentence about the past, after
          its section is retitled: it takes the new title, since only
          history keeps an old one (2026-10-31, ADR-0078's Context).
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
        writing rule 9's question at the commit, and a refinement's Writing
        read. The sweep scripts live in a session's scratchpad today.
      Trigger: the refinement closes.
      See: devlog 2026-10-28; ADR-0070;
      `TODO-CONVERSATION-MEMORY.md` §22, *Testing fact references and foundations as a whole*.

- [ ] Look again at where a CBC Run learns how to treat an Agent Skill
      Template (2026-10-28, the reviewer).
      Context: four shipped files told the off-template rule in
      their own words, and drifted: deviate from an Agent Skill Template,
      derive from what it implements, log it, expect a Record Harvest,
      never bend a decided constraint to fit it. On 2026-10-28 it went to the Exchange Convention
      (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*) and the CBC Run's `delivered-copies.md`, chosen on
      one CBC Run Reading, with no CBC Run having lived it.
      Ideas:
      - (a) one Agent Skill states it; the others point.
      - (b) delivered copies: the Exchange Convention
        (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*) and the CBC Run's
        `delivered-copies.md`; today's choice.
      - (c) each Agent Skill Template states it in its own header,
        where a CBC Run meets the choice.
      - (d) an Output Shape for Agent Skill Templates.
      - weigh each by maintenance, readability, future-proofing and
        complexity.
      - check that every manual and shipped text that speaks of an
        Agent Skill's templates agrees with the Exchange Convention (`docs/conventions/exchange/` §5.8, *Agent Skill Templates*) and
        `delivered-copies.md`,
        and that `delivery/README.md` and ADR-0008 still match.
      - check that each use says whose template it is: an Agent Skill's,
        repo-hygiene's, or a Record Stub. Of 97 uses in Living Text,
        only some say.
      Trigger: a CBC Run Reading that shows a CBC Run deviating from an
               Agent Skill Template, or a second stack's Stack Overlays arriving,
               whichever comes first.
      See: devlog 2026-10-28; ADR-0070.

- [ ] Decide whether a single commit's subject is counted by script
      when it is written (2026-11-19, the reviewer).
      Context: the writer aims at 50 characters, and the checks, at a
      Plan Step's close and a session's end, pass a subject up to 70
      (ADR-0083). Nothing counts a single commit's subject when it is
      written; a commit plan still counts its own. Each subject past
      70 a check finds counts here, fixed or kept. Found so far: 0.
      Ideas:
      - found fast: the commit-messages Agent Skill counts each
        subject when it is written;
      - not sure yet: 5 more finds before deciding;
      - rare, and a reword cheaper than counting: drop the question.
      Trigger: the 5th subject past 70 found by a check.
      See: ADR-0083; devlog 2026-11-19, the subject's aim and its line.

## Later / someday

- [ ] Release concept v2 (2026-10-17, from PLAN's Step N).
      Context: so a stranger, or future-you, can read, cite and copy
      from this repo without the archive. Four items of its own:
      - a CHANGELOG entry for the release;
      - README true for a stranger, who meets the method's words in the chapters (`delivery/method/docs/glossary/method.md` lists them);
      - `docs/models/` checked against the repo, since `CLAUDE.md`
        sends a stranger there;
      - known issues filed here.
      PLAN held it until ADR-0057.
      Trigger: the reviewer names it, after the refinement's close.
      See: ADR-0057, decision 4.

- [ ] Decide what our CHANGELOG tracks, and how the Record Stub asks it
      (2026-10-21, the reviewer).
      Context: ADR-0003 (2026-08) made it the concept's log, for
      CBC Runs pinning a version; ADR-0039 decision 9 kept conventions
      out. Since v1 (2026-08-28), about 1,800 commits on main, counted
      2026-11-02, added the
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
        at the CBC Framing Plan Step, with when to revisit it; the lesson goes in project-recording's changelog part
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
      Context: one document, byte-identical in the cbc-framing Agent Skill's and
      the cbc-slice Agent Skill's `references/`. `.claude/rules/one-home.md` rule 5
      asks a check where two copies cannot be avoided (ADR-0053);
      today they are compared by hand at each edit, and were
      identical on 2026-10-15. Made one, the cbc-slice Agent Skill could not be
      installed without the cbc-framing Agent Skill.
      Ideas:
      - a diff of the two in the exchange-deliver Agent Skill's gates, since a
        delivery is when the copies leave.
      - one document, once one Agent Skill is wanted without the other.
      Trigger: the two found different, the worked example's next
               edit, or a reason to install one Agent Skill without the
               other.
      See: devlog 2026-09-17, later.

- [ ] Decide whether the Infrastructure Contract carries a paragraph
      on the store's facility (2026-09-17, CBC Run 3).
      Context: CBC Run 3 wrote one at Step 3 — the ways its store makes
      two writers disagree — because the Agent Skill is silent on it. We
      held it rather than declined: one instance is not an Output Shape.
      CBC Run 3 says SL-2 did not lean on it; SL-2 faces no race.
      CBC Run 4 rebuilt CBC Run 3's problem from CBC Run 3's copies, so it
      cannot be the second CBC Run. CBC Run 5's CBC Run Reading of
      2026-10-22 has nothing on it.
      Trigger: a CBC Run Reading finds a CBC Run writing it unprompted.
      See: devlog 2026-09-17, later still.

- [ ] Move the Agent Skills' `foundation` to concept v2 at the release
      (2026-10-08, ADR-0048).
      Context: the Method Group's Agent Skills say `foundation: concept v1`.
      ADR-0048 makes the next release v2, and the cbc-slice and
      cbc-framing Agent Skills already state its ranking.
      Trigger: the release that names v2.

- [ ] Decide whether an Agent Rule can be delivered on trial, as an Output Shape
      can (2026-10-08, CBC Run 3).
      Context: an Output Shape reaches a CBC Run but binds nothing until a
      Plan Step Gate reads it (ADR-0052); an Agent Rule learned in one CBC Run is in
      force in the next from its first Plan Step. CBC Run 3 asked after
      offering its Evidence Test Shape as an Agent Rule. Held: the question
      is real only once there is an Agent Rule we would deliver that way.
      CBC Run 3's RETRO D4 says a trial names the close that judges it,
      and the Plan Step Form says so since `0cdc50c`.
      Ideas:
      - ship it as an Approach on Trial: in force only when a Plan Step
        takes it as its Work Approach, and each use comes back as a note
        (ADR-0058).
      Trigger: an Agent Rule we would ship that one CBC Run alone has lived.
      See: devlog 2026-10-08.

- [ ] Number the concept chapters' sections (2026-09-30).
      Context: their `##` headings are unnumbered, and nothing points
      into a chapter's section today. The chapters are the canonical
      text every CBC Run holds a copy of, so numbering them would change
      every copy for no reader yet
      (`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).
      Trigger: the first Fact Reference that needs a section of a
               chapter.
      See: devlog 2026-09-30, numbered parts.

- [ ] Does the playbook need a convention of its own? (2026-09-29,
      the reviewer)
      Context: project-recording describes it
      (`docs/conventions/project-recording/` §9, *The playbook*), and one playbook exists, the CBC Run's. It is not an Output Shape: an Output Shape is form, never content
      (`docs/conventions/shapes/` §1.1, *What an Output Shape says*, and §2, *What an
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
      maintainer's Container Group does either.
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

- [ ] Name the discipline "lived is evidence, not text to copy"
      (2026-09-04, the reviewer).
      Context: the records table says what goes in a README, the
      Entry File and the internal records, and it slipped twice in
      one session the same way. Text a Newborn CBC Run had lived was
      taken because of where it came from, without checking it
      against the target record's rule.
      Trigger: a third slip — then the rule gets its guard.
      See: devlog 2026-09-04.

- [ ] Decide whether a receiver needs a rule for claims it cannot
      check (2026-09-18).
      Context: the sending half is in force — a Delivery Note says when it
      claims what the receiver cannot check. Two receivers, the
      handbook, the repo that held the working arrangement before this
      one, and CBC Run 3, took such claims as attributed
      rather than checked, unprompted; a rule now would tell them
      to keep doing what they do.
      Trigger: the first receiver that acts on an unmarked
      uncheckable claim as fact.
      See: devlog 2026-09-18, later still.

- [ ] Decide whether the cbc-bootstrap Agent Skill points at the Spring
      Stack Overlay, or "grow, never overwrite" stands (2026-09-18).
      Context: the `.part` files under
      `docs/conventions/repo-hygiene/templates/java-spring/` are pointed at by
      nothing, and six CBC Runs derived `.gitignore` by hand, the last CBC Runs 4, 5 and 6. They
      belong to the Stack Group (ADR-0029 decision 7) and move with the
      answer. Until then they break ADR-0029 decision 5, that what is
      about a group sits beside it, an exception the ADR records. The Change Walk named the wider
      gap: nothing ships a Stack Overlay, and a blind CBC Run cannot
      fetch one.
      Ideas:
      - Refinement Round 2's FINDING-203: the cbc-bootstrap Agent Skill and its
        walkthrough both tell a CBC Run to add a Stack Overlay below
        each hygiene file's marker, and no file ships one. The
        Agent Skill could point at the walkthrough's step 2 instead.
      Trigger: the cbc-bootstrap Agent Skill's hygiene step is rewritten.
      See: devlog 2026-09-18; `temp/reading-run-6-2026-11-26.md` §6,
      *The work*.

- [ ] Weigh three candidate rules for what makes a Delivery Note land
      (2026-09-17, the reply of the handbook).
      Context: the only outside reading of our Delivery Notes. The
      three candidates:
      - an opening ordered by weight let them plan their commit split
        from four lines;
      - "we are not asking you to write the convention" removed a
        pressure we did not have to name;
      - all four additions were usable with no follow-up question. None
      of the three is in the exchange manual.
      Trigger: the Delivery Note that answers CBC Run 5's CBC Run Reading, before it is
               written.

- [ ] Decide whether an overtaken CBC Run Reading still owes the CBC Run a Delivery Note
      (2026-09-30, the CBC Run Reading of CBC Run 3).
      Context: the CBC Run Reading of 2026-09-24 was overtaken on 09-26 and
      deleted without one, so what CBC Run 3 had addressed to us since
      its Delivery Pin had no verdict until the CBC Run Reading of 2026-09-30 read it
      again — three edits to copies, ten CBC Run Asks.
      The Exchange Convention closes an overtaken CBC Run Reading
      (`docs/conventions/exchange/` §6.4, *How a CBC Run Reading closes*)
      "the same way", one pass over its items, and is silent on the Delivery Note every read ends with
      (`docs/conventions/exchange/` §6.6, *The Delivery Note after a read*). Once so far.
      Ideas:
      - the overtaken CBC Run Reading sends a Delivery Note: read, asks
        open.
      - the next read goes back to the last Delivery Note's
        Read-Through Commit.
      Trigger: the next CBC Run Reading overtaken.
      See: devlog 2026-09-30, the delivery to CBC Run 3.

- [ ] Name when a CBC Run is read (2026-10-01, from the draft of
      working a reading, now gone).
      Context: a CBC Run Reading happens when the reviewer says. A CBC Run Ask
      arriving, a Plan Step closing at the CBC Run, a calendar — none is
      named, so a CBC Run Reading happens when someone remembers, and both
      sides drift further from the Delivery Pin while it waits. CBC Run 3's RETRO
      D24 names one moment: after a CBC Run's apply-retrospective Plan Step, so its
      decisions arrive tried. CBC Run 3's next Plan Step waited on our Delivery Note:
      recording the Read-Through Commit was on its path (2026-10-18).
      Trigger: a CBC Run Ask found waiting for a CBC Run Reading nobody called.
      See: devlog 2026-10-01.

- [ ] Decide how CBC Run Readings work with more than one live CBC Run
      (2026-10-01, from the draft of working a reading, now gone).
      Context: the rules for reading and working a CBC Run Reading are
      written for one CBC Run. Two live CBC Runs mean two CBC Run Readings, and
      their items may be the same finding twice.
      Trigger: a second live CBC Run.
      See: devlog 2026-10-01.

- [ ] Say once that a CBC Run Reading's decisions are the reviewer's
      (2026-10-01, from the draft of working a reading, now gone).
      Context: the agent proposes and builds, the reviewer settles —
      every CBC Run Reading has gone so, and nothing says it. Probably
      agent-arrangement's to say, not the CBC Run Reading's.
      Trigger: an agent found settling what was the reviewer's.
      See: devlog 2026-10-01.

- [ ] Could a project need its own variant of a shipped Agent Skill?
      (2026-09-17, the reviewer)
      Context: an Agent Skill is the same for every project; what one
      project needs goes in its own records, never the copy. The
      gap: an edit the project needs in the Agent Skill's behaviour,
      declined.
      Ideas: an overlay file per Agent Skill beside the copy — CBC Run 3's,
             which it declined to build.
      Trigger: declined-but-needed becoming a pattern.
      See: devlog 2026-09-17, later.

- [ ] Add a level for System Guarantees held by absence to the enforcement
      hierarchy (2026-09-14, CBC Run 3's SL-1).
      Context: no process clock, no state outside the store — nothing
      to observe at runtime; its Structural Wall is a rule on the compiled
      classes. CBC Run 3 asks for a level between "single checked entry
      path" and "code review". It met it again in SL-2 and SL-4, and
      CBC Run 4 rebuilt the same problem from CBC Run 3's copies, so neither
      is a second CBC Run, and CBC Run 5's CBC Run Reading of 2026-10-22 has nothing on it. The hierarchy lives in
      `concept/02-guarantees-and-walls.md` and both of the cbc-slice Agent Skill's files: a
      concept change, with an ADR and the version question (ADR-0003).
      Trigger: a CBC Run Reading finds another CBC Run meeting a System
               Guarantee held by absence.
      See: devlog 2026-09-15; and 2026-10-10.

- [ ] Decide whether the worked example shows an Invariant Slice that
      inherits its Structural Wall (2026-10-10, the CBC Run Reading of CBC Run 3).
      Context: CBC Run 3's SL-4 built no Structural Wall — SL-3's one statement
      already held its invariant — and owed proof only, against its
      own instance killed mid-write and an outcome its caller cannot
      know. The worked example has no such Invariant Slice and no such
      adversity. One CBC Run's Invariant Slice, so held.
      Trigger: a second CBC Run whose Invariant Slice inherits its Structural Wall.
      See: devlog 2026-10-10.

- [ ] Decide whether the cbc-slice Agent Skill says a Red Run removes the Structural Wall Backstop too
      (2026-10-10, the CBC Run Reading of CBC Run 3).
      Context: the Agent Skill says a Structural Wall that already stands is removed on
      the working tree for its Red Run. SL-4's Red Run as signed stayed green:
      the store's check on the units held caught both orders, and the
      evidence went red only with the one transaction and that check
      both gone. CBC Run 3 revised its plan for it and proposed no edit.
      Since `2674c03` the Agent Skill asks the Red Run to note whether each
      Structural Wall Backstop was seen or is unproven; removing it is not asked.
      Trigger: a second Invariant Slice whose Red Run a Structural Wall Backstop holds green.
      See: devlog 2026-10-10.

- [ ] Decide whether a second service family earns its own
      walkthrough (2026-08-28).
      Context: beside `postgres-setup-walkthrough.md`; the test is
      long, sequenced, likely to recur.
      Trigger: a CBC Run first standing up a non-PostgreSQL service.

- [ ] Revisit "backend" in the Agent Skills' description lines
      (2026-09-06).
      Context: kept — it names the real scope of the Agent Skills, and
      every CBC Run so far is one. The Stack Group's Agent Skills' bodies
      (compose, Flyway, Spring Boot) are backend-born too.
      Ideas: start with the description lines.
      Trigger: the first non-backend CBC Run.
      See: devlog 2026-09-07.

- [ ] Tune the Stack Group's Agent Skills' trigger descriptions (2026-08-28).
      Context: unoptimized since import (archive STATUS).
      Trigger: an Agent Skill under- or over-firing in a CBC Run.

- [ ] Consider a held-insight kind in the Record Harvest discipline
      (2026-08-29, safe-reservations' close).
      Context: safe-reservations sent its lessons back in two kinds:
      sure adoptions, landed in the Master Copies, and insights held
      as evidence, each with a named way to be promoted later. ADR-0007 has only the first kind; adding
      one is an amendment, decided deliberately.
      Trigger: a CBC Run Reading holds an insight it cannot land yet and
      has nowhere to put it.
      See: devlog 2026-08-29 (framing shape decided).

- [ ] Harvest how public docs beyond the README live, when a CBC Run
      lives it (2026-08-30).
      Context: public docs beyond the README, written once there is
      something to say, saying only what is already true, and
      refreshed at each Invariant Slice Close. Seen in the
      safe-reservations repo, never lived by a CBC Run of ours.
      Trigger: a CBC Run first writing public docs beyond its README.
      See: devlog 2026-08-30 (doc projection checked).

- [ ] Decide how a CBC Run learns that the rule for taking deliveries
      changed (2026-10-18, the reviewer).
      Context: a CBC Run takes a delivery under the `delivered-copies.md`
      it holds, so a delivery that changes that rule is taken under
      the old one. The rule cannot be delivered alone: one Delivery Pin covers every
      copy (`docs/conventions/exchange/` §2.2, *The CBC Run*). CBC Run 3's copy lacked
      `4de6ba2`'s Output Shapes; no files went, so it never acted.
      Ideas: the Delivery Note's "why it matters" names a change to the rule
             first, so the CBC Run takes it knowingly.
      Trigger: the first files delivered to a CBC Run still building,
               with `delivered-copies.md` changed since its Delivery Pin.
      See: devlog 2026-10-18.

## Known issues (deferred deliberately — each entry: what, why accepted, when to revisit)

- The postgres image tag floats (2026-08-28). The infra-establish Agent
  Skill's Agent Skill Template `templates/compose.yaml` and the Adversity Harness reference both say `postgres:17`, so they can
  pull different minors at different times. Accepted: the shared
  major is a deliberate coupling, and no CBC Run has hit drift.
  Revisit: a CBC Run's first minor-drift surprise — then pin both
  tighter, to a full version or a digest.
