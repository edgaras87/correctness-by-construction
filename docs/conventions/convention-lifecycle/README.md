# Convention lifecycle — the kit's protocol

How a set of conventions travels from the repo that delivers it to
the project that receives it, and how the two stay in step
afterwards. The handbook delivers a kit. A concept repo delivers a
bundle. A project receives both the same way.

**What ships:** [`SKILL.md`](SKILL.md), the receiver's procedure,
which a project holds at `.claude/skills/convention-lifecycle/`.
This page explains it; the skill states it.

## The two sides

**The deliverer** keeps one origin for everything it ships. In the
handbook that is `starter/kit/`: the record stubs, the entry file,
the hygiene base, and one skill file per convention. Nothing else
leaves the handbook. The kit is copied whole, as real files, at
the moment of birth.

**The receiver** is a project, and its agent. It holds copies,
never links, because a link into a repo it does not have points at
nothing. It never edits the deliverer. What it learns goes back up
through its own records — a decisions entry, a friction list, a
handoff — which the deliverer reads.

The handbook is a receiver of its own kit as well. Its agent holds
the four skills as copies at a pin and takes a kit change by the
procedure below, so the first seat a shipped sentence is read from
is one with no handbook in reach (ADR-0041).

## How the two stay in step

**The pin.** At birth the project writes one entry in its agent
decisions log, `.claude/decisions.md`: which conventions it was born
with and the deliverer's commit hash at that moment. That entry is
the registry. Every later injection or update appends another
entry with its own hash, and a convention's version in the project
is the hash of the last entry that touched it. There are no version
numbers to bump, and nothing to forget: git mints the hash on every
commit.

**The receipt.** A project may keep a frozen branch holding every
delivered file exactly as it arrived, named by the deliverer's
commit, `kit-<hash>`. It is never edited. At the next update the
new kit lands as one commit on top, `kit-<newhash>`. Then two
ordinary diffs answer the two questions an update has to ask: old
receipt against new receipt is what the deliverer changed, and the
working branch against the old receipt is what the project changed.
No checkout of the deliverer is needed. Run 3 of the CbC seed
invented this and used it through a real update on 2026-09-15; it
worked, with one trap: cut the receipt only after the ignore file
exists, or a wholesale add sweeps build output into it.

**The update.** Position from the registry, evaluate the incoming
skill's `requires`, choose the vehicle by which sides the landing
touches, compare before overwriting, register in one commit, and
edit nothing in the deliverer. The skill states the six steps.

**Editing a copy between two pins.** A project may find a skill
thin mid-step. It may edit its copy, on conditions the skill
states: only from something that happened, only as any project
would want, each edit marked in the copy's header and in the
decisions log, and one TODO line at the step's close asking the
deliverer to evaluate. At the next update the deliverer's version
overwrites the copy whole; a declined edit is gone with it. This is
provisional: run 3 wrote the rule after its first slice, and no
edit has yet gone through a re-pin.

## Why it is shaped this way

- **The registry is entries, not a manifest.** A separate file
  listing versions needs a bump ritual and can lie; an appended
  entry with a hash cannot (ADR-0022, ADR-0034).
- **Compare before overwriting.** The CbC repo's copy of a
  convention was nearly overwritten unread on 2026-09-03; the
  procedure was written from that injection (ADR-0030).
- **Register even an empty update.** A change absorbed through a
  reply without an entry left the pin lying once, on 2026-09-08,
  and the currency check read the lie as truth (ADR-0030).
- **Two commits, one per side, need no change-plan.** The agent
  side and the project side never share a commit (ADR-0019), and a
  plan pays for itself only across a sequence (ADR-0038).
- **An edit goes up, delivery comes down.** An edited copy is not a
  third form of delivery; its diff against the pin is a record the
  deliverer reads (ADR-0038, the tiers model §3).
- **The lifecycle is the kit's, not a topic beside the others.** It
  is the protocol every deliverer and receiver share (ADR-0040).

## Where to look

- The receiver's procedure: [`SKILL.md`](SKILL.md).
- How the handbook builds and ships a convention:
  [`../README.md`](../README.md).
- The kit itself and what each file comes from:
  [`../../starter/README.md`](../../starter/README.md).
- The tiers model, for how deliverers and receivers relate across
  the workspace: [`../../models/tiers.md`](../../models/tiers.md).
