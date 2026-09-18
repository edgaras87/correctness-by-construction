# 0024. The kit is taken here, verbatim but for a stated delta

Date: 2026-09-17
Status: Accepted (2026-09-18, at the set's final records commit;
opened Proposed per change-plans §4 and rewritten twice at
boundaries — decision 3 lost `PLAN.md` when the user chose to keep
the playbook a document, and decision 5 gained its second half when
the manuals were actually brought. The take is in place:
`starter/kit/` at `ba7eaa4`, fourteen files verbatim, the delta
list in `starter/README.md`, and a birth that no longer runs
another repo's bash in our shell)

## Context

A run has two parents. It holds a kit hash from the handbook and a
bundle hash from here, in one decisions log, updated by two
procedures on two schedules, and nobody owns the pair. When the
handbook's kit restructured at `ba7eaa4`, the break was absorbed
here — and will have to be absorbed again in every run, separately,
because each run took the kit itself.

Our independence from the handbook is already a fiction, and worse
than a pointer. `pure-seed.md` step 2 defers to their `pure.md` *by
pointer, no step restated*, and its blocks use the same
`handbook_dir` / `new_project_dir` variables in the same terminal
session. That is two documents in two repositories sharing shell
state, at whatever commit their checkout happens to be on, with no
pin between them. Rename a variable there and our birth breaks
here, silently, at the next birth rather than at the change.

Four more surfaces ride on kit shapes holding still: `PLAN.md`'s
`STEPS-BEGIN`/`STEPS-END` markers matched by `sed`, its playbook
version placeholder matched as a literal string, the kit shipping
`CLAUDE.md` at the root — which the seed's step 4 then undoes,
moving it to `.claude/` with a note that this half "goes the day
the kit ships it there" — and the kit's entry-file text carried
verbatim in the fills. The adaptation layer is not a proposal. It
exists, as a `sed` command with a wish attached.

The handbook has already written this role down. Its TODO, since
their ADR-0041: "every maintainer repo is both sides — the handbook
receives its own kit and sends to CbC, CbC receives and sends to its
runs. Only a run is receiver-only." That is this decision in their
words, and the kit half is the part that was never made true.

The objection that stood in the way — two masters, so the compare
dies — is answered by ADR-0023: a compare is a reading over two
diffs, and the diff that survives two masters is our copy against
our own pin.

What remained was the size of the adaptation, and it has now been
measured rather than guessed. The kit at `ba7eaa4` is 16 files and
926 lines:

- **Thirteen come over untouched**, about 800 lines: the four
  convention skills (verified byte-identical to the copies this
  repo already holds), the three hygiene dotfiles, and every record
  stub but one — `TODO.md`, `devlog/devlog.md`, `CHANGELOG.md`,
  `ARCHITECTURE.md`, `docs/adr/0001`, `.claude/decisions.md`.
- **Three are flavoured**, and they are exactly the three files
  `starter/fills/` already holds: `CLAUDE.md`, `README.md`,
  `PLAN.md`. Plus one line in `.claude/decisions.md`, whose birth
  entry names one upstream and must name two.

So this is finishing something half-built. `starter/fills/` is the
bundle's kit, started and never named as such — two of its files
already carry the kit's own text verbatim with a re-verify duty
attached, which is vendoring, already, for two files.

Two findings from the measurement bear on the shape.

`ARCHITECTURE.md` comes over **verbatim**, and that settles a
question by measurement. Its Invariants section — "what must NEVER
happen to the data / system, and where each rule is enforced" — is
this concept's vocabulary in a generic kit, which makes it a defect
at the maintainer tier and exactly right at the run tier. The same
file is wrong above and correct below. That is the evidence for two
degrees of completeness, one per tier: a skeleton for a maintainer
to flavour, a complete artifact for a receiver who has nobody to
flavour it.

And the kit is more neutral than we assumed. Our complaint of
2026-08-28 — the CHANGELOG stub "had to be replaced, not filled,
app-repo assumptions" — is already fixed upstream: the stub now
reads "an app releases SemVer; a concept repo versions its
concepts; Framing decides." They absorbed it without being asked
again. Their `.gitignore` goes further and already implements the
shape this repo wants generally: a base layer declared for "any
repo, from day zero (records-only repos included)", with stack
overlays appended below a line at app bootstrap. One artifact of
sixteen has the answer in it already.

## Options considered

1. **Leave the two upstreams.** Cheapest, and the handbook keeps
   its only field data about its kit outside its own repo.
   Rejected: it keeps the unpinned shell coupling, keeps four
   surfaces the kit must hold still, and makes every kit break a
   thing each run absorbs separately, for ever.

2. **Vendor the install procedure only** — restate their `pure.md`
   here so our birth stops running another repo's bash in our
   shell, and let kit updates keep flowing to runs directly.
   Rejected: it removes the sharpest harm and none of the others.
   The four assumed surfaces remain, and a run still holds two
   pins, which was the problem.

3. **Fork the kit — take it and own it outright, no pin.**
   Rejected: ADR-0023's compare needs a pin to diff against, and a
   fork throws away improvements that arrive unasked. The CHANGELOG
   fix landed upstream while we were not looking; a fork would still
   be carrying our complaint.

4. **Take it at a pin, verbatim but for a stated delta.** Chosen.
   The delta is measured, small, and consists of surgery the seed
   already performs.

## Decision

1. **`starter/kit/` holds this repo's copy of the handbook's kit at
   a pin**, at their path name, so the mechanical half of a compare
   is a directory diff and nothing has to be mapped.

2. **Verbatim is the default and the delta is stated.** At the take,
   thirteen of sixteen files are byte-identical to the master.
   Every departure is one line in the delta list with its reason,
   and at each re-pin the delta is re-applied to the new master, not
   merged into the old copy.

3. **The delta at the take is two files and a birth entry.**
   `CLAUDE.md` and `README.md` are the composed entry files this
   repo already holds — ADR-0015's whole-delivery rule, now true of
   the kit and not only of one file. `CLAUDE.md` sits at
   `.claude/CLAUDE.md`, which is the seed's step-4 surgery
   relocated from a `sed` into the artifact. And the birth entry in
   `.claude/decisions.md`, with the comment above it, names both
   upstreams.

   *Revised at the set's second boundary.* This decision listed
   `PLAN.md` as a third flavoured file, arriving with the
   playbook's steps already between its markers. The user chose
   otherwise: the playbook stays a document and the seed goes on
   inserting its steps at birth, so `PLAN.md` comes over verbatim
   and the take is fourteen files untouched rather than thirteen.
   What that buys is ADR-0011 untouched and playbooks kept as a
   menu, against a marked-region insert surviving as the birth's
   one genuine merge. The forward reason is PLAN Step 9's: a CbC
   project that is not Spring and Postgres wants a different
   sequence, and a menu makes that a choice rather than a rewrite.

4. **`starter/fills/` is absorbed and the category retires.** A fill
   was text written into a file the kit had already put there; once
   this repo ships the file, there is nothing to write into. ADR-0017's
   three-way split becomes `kit/` and `bundle/` landing as files,
   `installs/` staying home. ADR-0019's semi-pure step dissolves
   with it — not switched off, unnecessary.

5. **The manuals are vendored read-only, and what we flavour is
   ours to explain.** `conventions/` — seven manuals, never
   shipped — comes here at the kit's own pin under ADR-0002's rule,
   as reference, and is never re-flavoured. The rules live in
   artifacts we may flavour; the *why* keeps one master, or the
   explanation forks too and nothing anchors either copy.

   The second half, added when the manuals were brought: their
   manuals explain *their* artifacts, and anything this repo
   flavours needs an explanation they cannot give, because they do
   not know it happened. That explanation is ours. Today it is the
   delta list in `starter/README.md` — a table, because the
   departures are stub-level and one sentence each. When it
   outgrows a table it graduates into manuals here, beside theirs,
   and that graduation is the signal the flavour has become
   rule-level rather than shape-level.

   What came: eleven files. Sixteen further entries under their
   `conventions/` are symlinks into `starter/kit/`, which we hold,
   so the links are not reproduced and a manual's pointer to its
   artifact resolves here into `starter/kit/` instead. One does not
   resolve — `agent-arrangement/stubs/CLAUDE.md` names
   `starter/kit/CLAUDE.md`, which delta row 1 moved.

6. **A ceiling, so the take can be found wrong.** If more than a
   third of the kit's files carry a delta, or if any delta cannot be
   stated in one sentence with its reason, the take was the wrong
   shape and this decision is revisited rather than extended. Today
   the figure is three of sixteen.

7. **A run receives one delivery and one pin, and the pin names both
   hashes.** Composed here, tested together before a run sees it.
   Per ADR-0023 decision 8 the registry entry states what the pin
   claims: derived from the kit at that hash, with this delta list,
   last read on this date. One pin that hides which kit is inside it
   would be a pin that lies.

8. **No back door.** The chain runs one way in each direction and
   has no special case: a run does not contact the handbook
   directly, and the handbook does not reach a run except through
   here. A back door that exists is used, and then there are two
   chains *plus* a rule about which applies, which is worse than the
   two chains this decision exists to end. What a run needs from the
   handbook comes through here — slower, and traceable. What the
   handbook needs from a run is section 4's cost, paid in reports we
   owe rather than in a channel we keep open.

9. **The assumed-surface contract ends**, and with it ADR-0009's
   two-copy birth. There is no contract to hold when the shapes are
   ours: `starter/README.md`'s three assumptions — the STEPS region,
   the step/gate idiom, the playbook vendor base — stop being things
   the handbook must hold still and become things we hold. ADR-0009's
   record-layering half stands unchanged: the kit owns the record
   system, CbC owns method content. ADR-0016 stands; `pure-seed.md`
   loses its step 2 and shrinks.

10. **Three things go up after the take, in one letter**, as
    observation and not request. Not before: the handbook asked for
    exactly one thing, whenever it happens — that `bundle-update.md`
    having run for real, we say what it taught or that it taught
    nothing — and the take running is what produces that message.
    Sending the case first and the report later is two letters where
    one will do, which is the paper they had just declined to write.
    The timing risk is accepted with open eyes: their repo-shapes
    model's §4 states two upstreams as fact and may reach us folded
    into `models/tiers.md`, which we vendor pinned. If it arrives
    first we take it whole and send our evidence after, which is the
    rule we handed a run three days ago and which binds us the same
    way. The constraint: whatever their pure kit becomes,
    ours should be derivable from it — not "change for us", but "here
    is the shape that exists; pure should be able to produce it".
    The cost they are about to pay: runs are their only field data
    about the kit outside their own repo, their ADR-0035 gate was
    withdrawn on a run's report and their ADR-0038 came from a run's
    hand-off, and interposing this repo removes that channel; we owe
    them kit-level findings explicitly in its place, and whether that
    is as good is genuinely unknown. And the finding: `ARCHITECTURE.md`
    is right below and wrong above, which is a defect report about
    one stub, not a preference about who owns method.

## Consequences

Good: a run has one upstream, one pin and one procedure, and
`bundle-update.md` becomes a whole manual instead of half of one.
The birth stops running another repo's bash in our shell at an
unpinned commit. Four surfaces the kit had to hold still stop being
a contract. The adaptation that already existed gets a home and a
name instead of living in a `sed` command. And the handbook is free
to purify without breaking us, which makes that work fundable
rather than blocking.

Bad, and accepted: we own the kit's correctness in runs — the
handbook fixes something and runs wait for us to pass it on, where
today they could take it directly. The handbook loses its only
field data about its kit outside its own repo, and the replacement
is our word. Every handbook update is now evaluated twice, once for
this repo's agent and once for the kit we hold; that is a transition
cost with an end only if their purification actually happens and our
copy stays derivable from it, and neither is guaranteed. Run 3 holds
two pins today and migrating it is real work with a one-off
procedure. And their repo-shapes model states two upstreams as fact
in its §4, with a recommendation to fold it into `models/tiers.md`,
which we vendor pinned — if that arrives we take it whole and argue
afterwards, by the rule we handed a run three days ago.

Not settled here: how the bundle's contents group once the kit is
one of them — the work-kit, the concept and its skills, and the
stack-shaped practice executions look like three things and get
their own decision. Nor how run 3 migrates from two pins to one, nor
what `pure-seed.md` looks like once its step 2 is gone.
