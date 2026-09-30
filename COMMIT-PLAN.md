# Commit plan: the tiers model, read

## Summary — the state after all commits

`docs/models/tiers.md` says nothing false, and says each thing once.
Its header and draft line no longer carry the handbook-era posture
and revision history. It names the container where it said "kit",
and says the concept repo's records derive from the manuals
(ADR-0042), not from a kit. Its pointers to the exchange are root
paths.

Its §3 flows keep what is true between tiers and point to the
master and the exchange for the mechanics they already hold. It
does not tell the same flows a second time.

It stays where it is. It maps the workspace, and the workspace has
no home of its own: by the model's own §2, the garden stays a plain
folder until a second concept repo exists. That second repo is also
the trigger for the model to move. The TODO item "Check
`docs/models/tiers.md`, and decide whether `docs/models/` stays" is
answered and goes. Both models stay, each with its own trigger for
leaving, and my idea of a workspace README, which does not exist,
goes with the item.

## Commits

**1. `docs(agent): add commit plan for the tiers model`**
This plan.

**2. `docs(models): the tiers model says what is true`**
- The header's "the body is otherwise as taken" (ADR-0043).
- The draft line's revision history.
- §2's "kit-born" and "a kit copy".
- §3's "the update procedure", whose file is gone.
- "(the exchange, §5)" and "(the exchange, §6)", rewritten in the
  root-path form of `docs/conventions/conventions/` §3.2.

**3. `docs(models): the tiers flows point home`**
*Provisional in its cut.* §3 retells the master's "Down — delivery"
and "Up — harvest" and parts of the exchange. With one concept repo,
these are one fact in two homes. It keeps what holds between tiers:
that delivery is copies and fills, that told is not delivery, that
learning moves only through records, and that the pin follows the
talk. It points to the master and the exchange for the rest. If §3's
bold-led parts hold as parts after the cut, they are numbered by
form (§3.2).

**4. `docs: devlog carries the tiers model`**
The session's entry. The TODO item on `docs/models/` closes: both
models stay. The agent model folds when one fact needs both files
edited; that trigger is in TODO already. The tiers model moves to
the garden when a second concept repo exists; that trigger is added
beside it.

**5. `docs(agent): close commit plan for the tiers model`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **Not into the master.** The master maps this repo, and the tiers
  model maps the workspace. Folded in, it would have to come back
  out when the garden gets a home.
- **Not to the garden now.** The model's own rule keeps the garden
  a plain folder until a second concept repo. Moving the model
  there first would break the rule it states.
- **No ADR.** These are edits under ADR-0043.
