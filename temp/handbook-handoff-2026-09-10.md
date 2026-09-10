# Handoff from correctness-by-construction — 2026-09-10

<!-- Staging copy, tracked in temp/ while it is shaped; deleted
     once the handbook's reply is absorbed. Substance is on record
     in this repo's TODO (fifth-handoff item, (a)–(e); the
     gates-experiment item's 2026-09-10 note), .claude/decisions.md
     (the 2026-09-09 entries), and the devlog (2026-09-09, 09-10). -->

From the concepts tier (correctness-by-construction). Context
first: run 3 of the pure seed took the kit update to af16eb7 on a
receipt branch, then ran Framing through its close — 44 commits,
merged to main. That is the first full step lived under the three
pieces your reply left on trial (the entry file under .claude/,
the operator's local file, the settings-file gate), so their
report is in. Two asks, one report, three FYIs. What we need back
is at the end. Nothing here blocks us; our pins hold at af16eb7.

## 1. Report: run 3 through Step 1 — the three trials

**The kit update, by receipt branch.** The kit at af16eb7 was
delivered as one commit on a branch cut from the seed commit that
carries the c670fe5 pin, so the branch's one commit against its
parent is the kit at the two pins. The agent ran §8 under a
change-plan, seven commits, project side first so the registry
entry named an existing commit. What the branch gave the compare,
in the run's words: the whole kit diff at the two pins in one
place, and compare-first became one `git diff` per file against
the seed commit — every copy identical, every overwrite clean.
Where it fell short: the four placeholder reversions (the seed's
fills reverting to the kit's placeholders) are noise to read past;
the receipt cannot say which convention a stub change belongs to
(the starter README's table is not a kit file); the why is not in
it either (ADRs and convention text are not kit files) — and the
agent went to a handbook checkout for both, since its own §8
names "a checkout on disk" as the handbook. The entry-file stub
diff was carried into the living file by hand, comment only.

**The settings file: rejected, not deferred.** The agent read
ADR-0035's withdrawal at the checkout and the pace already held by
the operator's file plus the commit-messages sentence, and refused
the kit's born default in its plan before running under it once.
The receipt branch keeps the file so the compare stays honest.
The hygiene comment's "(if any)" was kept as a recorded local edit
for the same reason. So run 3 lives the case your reply named as
deciding whether the local copy is dead weight or a band-aid:
sentence plus local file, no gate. Through Framing it held: every
verdict the reviewer's, the plan revised on the reviewer's
questions, and the local file's text entered no record.

**The entry file under .claude/** — your decision 5 waited on
this. The move was a pure rename, content untouched, one decisions
entry; the harness read it at the new address from the next
session (the run's Step 1 change-plan targets `.claude/CLAUDE.md`
by path, and the pre-framing guard the file held governed the
session). Nothing else changed: records name the file, none its
path. The report is: the address is a layout preference,
mechanically identical either way. Our own reading of your 09-09
note — root for a repo about the arrangement, .claude/ for one
that builds an app — is what we act on: this repo moved back to
root, and our seed now writes the entry file to .claude/ for every
born run.

**The branch per step** (ours, a playbook rule — FYI): cut from
main before the step's first commit, fast-forwarded on the word,
no question the rule made the agent ask. Two gaps it showed, ours
to fix: the branch gate item can only be ticked in anticipation,
since the merge follows the close commit; and the rule says
nothing about a merged branch.

## 2. Ask: text that does not survive the copy

Read at the af16eb7 update, §8 friction, three forms.

- **Bare ADR numbers in skill copies and models.** Every citation
  in the kit's skill copies and in the two models is the
  handbook's, bare; the ones below 0020 collide with this repo's
  own ADR sequence on other subjects, and a run that reads
  "ADR-0035" in its copy has nothing to resolve it against. Your
  stub rule (no handbook citations in a stub) stops one step short
  of the skill copies. A self-qualifying citation at the master —
  "handbook ADR-nnnn" — survives verbatim copying and can never
  collide.
- **Exemplars from the handbook's seat.** artifact-kinds' exemplars
  name `conventions/…` paths and "this repo"; the playbook one
  reads "the handbook's starter/playbooks/default.md — or the one
  a concept repo keeps beside its own manual", which a born
  project has never heard of and which points nowhere for either
  reader (a born project holds no playbook copy; ours is a fill).
  Exemplars by role survive the copy: "the playbook your PLAN's
  Steps-from line names".
- **The requires chain naming a convention a project was born
  without.** convention-lifecycle @ af16eb7 requires
  agent-arrangement, and a repo born before it existed has no
  registry position for it — §8 step 2 reads as "check the copy",
  and there is none. We ran it as a first injection by the
  installed path. Worth one sentence in §8.

Related, FYI-shaped and older: default.md v2's Step 0 comment
ships "(ADR-0031)" into every born PLAN, where it reads as the
newborn's own number. Your line to draw; we dropped the citation
from our own shipped Step 0 comment on 2026-09-05.

## 3. Ask: the tiers model's §3, from five lived runs

models/tiers.md @ 4fe8083, unchanged at af16eb7. Its shape holds —
three tiers, copies down, records up, one tier per repo, the
garden paragraph exact — but §3 was written from zero runs and
five have now lived it. Five refinements, each with evidence:

- **Delivery has two forms.** The pinned copy, and the fill the run
  owns from the seed commit on — steps written into PLAN, the two
  entry files — folded back by name at the retrospective, never
  re-copied. "Always a copy, always pinned" describes the first.
- **Up is a reading, not a sending.** The tier above reads the
  run's records read-only, at step boundaries during the run; the
  run sends nothing and keeps working. Your checkout-system review
  is the same flow one tier up, splitting the yield by ownership.
  "Rides the promotion queue or a friction list back" describes
  the run as the mover; in practice the reader moves.
- **One downward channel is deliberately not a copy.** Our gates
  experiment hands a missing paid-for warning to the run as
  session input, after the run's own derivation is on record —
  told, unpinned, by design. "Down is delivery, always a copy"
  would call it a violation; it is the experiment's instrument.
- **Tiers talk in documents because no tier's agent reads another
  tier's repo.** A run reads only its own; a concept repo opens a
  handbook checkout only for the lifecycle update. And the pin
  must follow the talk: our registry lay for two days after a
  reply was absorbed through TODO with no entry — §8's own warning,
  lived.
- **Vocabulary.** The "startup snippet" was withdrawn 2026-09-02;
  "pinned at a concept version" is a concept-repo commit, each
  execution naming its concept version; and the DRAFT note's
  revise trigger names the garden — a second concept — which has
  not fired, where "no runs yet" is what actually changed.

Ask: revise §3 and the DRAFT note; we re-vendor at the new pin.

## 4. FYI: two change-plans lessons from run 3's close

From the run's own close body, not asked for. **Name a
touch-ups-on-reading step from the start**: three review-driven
wording fixes to committed exports each cost a plan revision
before a provisional "touch-ups" step named them, then one landed
under it. And **a step run as a commit series** — a draft, one
revision per reviewer question that changed something, the
verdict — so a question's effect is a diff between commits; it
held for seven steps. Whether the series shape wants naming in
change-plans, or stays a project's practice, is yours.

## 5. FYI: the three-voices problem, third time

An agent weighs its harness wiring over the firing prompt over
repo files, and skills are files. Run 1 of the pure seed saw
change-plans §6 and justified skipping the stop by an instruction
the prompt never gave. Run 3 read a handbook checkout during its
kit update because "stay inside this repository" sat in a
briefing section that had not fired yet, while its own §8 named
a checkout on disk. Same lesson each time: a told rule exists only
in the session it is told to; a rule resting on a session fact (a
reviewer is present, a repo is out of bounds) cannot live in a
file alone. Your agent model's §8 table already carries the
diagnostic row; what it does not say is the order the voices win
in, which is what decides a brake's home. Our side: every prompt
to a run now carries its session rules whole.

## What we need back

- On §1: whether decision 5 closes on this report, and if the
  stub moves, the new kit pin.
- On §2: the citation form for skill copies and models, and
  whether §8 gains the born-without sentence.
- On §3: the revised §3 and DRAFT note, at a pin.
- §4 and §5 need nothing back.
