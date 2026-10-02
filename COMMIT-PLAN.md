# Commit plan: the eval's group 5, the front door and records

## Summary — the state after all commits

What a stranger reads first, and the records this repo keeps, say
what is true today.

- **The CHANGELOG's Unreleased is the net change since v1**: one
  heading per kind, every line true now, nothing that came and went
  before a release; and its header says so, so it does not drift
  again (F48, D9).
- **This repo cites its own decisions bare** in everything that
  stays here — the manuals, ARCHITECTURE, our own rules and exchange
  skills. The tag stays where a file ships, where text describes the
  shipped form, and in our three convention skills, which are
  identical to the container's (F54, F68, D10).
- **The front door, the plan and the map are true**: the README's
  harvest criterion met and its history gone; PLAN's Release gate
  without a dead pointer; ARCHITECTURE's container list naming all
  seventeen files, and its words pointing at the exchange for the
  pin and the read-through (F49–F53).
- **TODO is true**: what is due sits in Now, a trigger that fires at
  every commit is replaced, an item the stub cannot hold goes, a
  count that moved goes; and two items it lacked — the devlog's own
  split, due, and a decisions entry's length (F55–F57).
- **`.gitignore` points at `temp/README.md`** (F59).

Nothing here ships.

## Commits

**1. `docs(agent): add commit plan for the eval's group 5`**
This plan.

**2. `docs: the CHANGELOG says what changed since v1`**
*Provisional in its wording*: the rewrite is decided in the
material, the draft shown before it lands. *Unreleased* rebuilt as
the net change since v1 under Added, Changed, Removed, Fixed — each
line checked against today's tree; the header comment gains the
rule. v1's own entry is untouched.

**3. `docs: this repo cites its decisions bare`**
`CBC ADR-` becomes `ADR-` in the manuals and ARCHITECTURE. Kept: the
two passages that describe the shipped form (exchange §3.7's, the
conventions manual §2's), and every file under `delivery/`.

**4. `chore(agent): our own files cite bare`**
The same in `.claude/rules/exchange-reading.md` and the two exchange
skills' footers; `exchange-deliver`'s sentence on the shipped form
keeps its tag. Our three convention skills keep theirs: identical to
the container's, by CBC ADR-0042.

**5. `docs: the front door, the plan and the map are true`**
README: the harvest criterion as met, with the commit, and "Since
2026-09-18" gone (F50, F51). PLAN: the Release gate without "(TODO,
Next)" (F49). ARCHITECTURE §2.3: the README and ADR-0001 stubs in
the list (F52); *The words*: pin and read-through point at exchange
§2.2, and the line above them says what it now is (F53).

**6. `docs: TODO is true`**
The three due items move to Now; the 50-character item's trigger
becomes the mood decision's (F55); the overlay-marker item goes, the
playbook being ours to change (F56); the worked example's line count
goes (F57). Two new lines: split the devlog by month, due — its own
header's trigger, 5,350 lines; decide a decisions entry's length —
the header says three lines, the median is eighteen.

**7. `chore: .gitignore points at temp/README.md`**
The dated comment that restated the old list becomes a pointer
(F59).

**8. `docs: records carry the eval's group 5`**
The eval marks F48 to F57, F59 and F68 fixed with their commits.

**9. `docs(agent): close commit plan for the eval's group 5`**
Deletes this file. The body records what diverged.

## Decisions taken inside this plan

- **Two commits for D10**, by seat: the manuals and ARCHITECTURE are
  docs, our rules and skills are the agent's files.
- **Where the tag stays.** A passage describing the shipped form is
  about the tag, not a citation; our three convention skills are
  byte-identical to the container's and stay so; `delivery/` ships.
- **The CHANGELOG step is material-first.** What changed since v1 is
  read from the tree, not from the entries it replaces, and shown
  before it lands.
- **The two new TODO lines are capture, not decision**: the devlog
  split is mechanical and due; the entry length is weighed when its
  trigger fires.
