# A System Repo's Change, as a Flow

<!-- A draft for the Plan Step "Find how what we know stays true",
     stage 1. It pictures the System Repo's commits in the round of
     temp/system-repo-change-simulation.md, and the part acting on
     each. The facts live in the
     simulation, never here. "Now" pictures the simulation as it is.
     Each "After" section pictures one open decision, one drawing per
     option, each named by its option. When the decision is made, the
     simulation changes, the chosen option's drawing becomes "Now",
     and that "After" section goes. It goes when the Plan Step closes, and
     git keeps every version. -->

It uses the simulation's short words: Change, Record, Copy, Update, Update Note, Version, Reading, Register (`temp/system-repo-change-simulation.md`, its table at the top).

## 1. What the reader must get

Each drawing is checked against these.

1. **R1, the order:** every step of one round, from a Change to the next Plan Step opening.
2. **R2, the repo:** which repo each step happens in.
3. **R3, what crosses:** a Reading only reads the System Repo, and writes nothing there. An Update is written only into the System Repo's `temp/`.
4. **R4, where main moves:** each place main moves.
5. **R5, where a Reading reads:** where each Reading starts and stops.
6. **R6, what is open:** each part not decided is marked open, and nothing decides it.

## 2. Now

The take moves main, but Read says main moves only at a gate's close (`temp/system-repo-change-simulation.md` §4, step 1, *Where a stretch ends*). That is found item 1 (devlog 2026-11-12).

### The System Repo's commits

#### Picture 1, the take inside its window

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 Reading 1 covers c2 to c6.                   ┌  c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1
 Open: how the take's changes                 │     │                                         ◀──── main moves here? Read says only at a gate
 in c2 are told apart from the                │     ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
 System Repo's own                            │     │            │
                                              │     │         c3 ●  work, no Copy changed
                                              │     │            │
                                              │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 6. Read, List, Judge: c2 to c6       ┐ ─▶  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 7. Act: c6 becomes read to                │        ┊
 8. Deliver: the Update waits in temp/     ┘        ┊
                                                    ┊
                                                    ┊
                                                    │
 The next Reading covers c7.                     c7 ●  the take: Version 2 comes in           ◀──── 9. Take, once it checks: main is still the Reading's stop, c6,
 Open: how the take's changes                       │                                               and the Version is still 1, the one the Update was built from
 are told apart                                     │                                               In order: the Adapted Case for taking first; the files checked
                                                    │                                               against the Update Note; every Copy taken whole, every Record
                                                    │                                               cleared; Changes still needed put back, each with a fresh Record;
                                                    │                                               verdicts acted on; Version 2 recorded; the Update removed from temp/
                                                    │                                         ◀──── main moves here? Read says only at a gate
                                                    │
                                                    └─ cut ──────┐                            ◀──── 10. step 2 opens on Version 2
                                                                 │
                                                              c8 ●  work, on Version 2
```

**Key:**

- **commits:** imaginary commits of the System Repo, oldest first, top to bottom.
- **main, branches:** a step's branch is cut from main, to its right. At its gate's close, main moves to the branch's last commit by fast-forward: a commit named again on main is no new commit.
- **Maintainer Repo:** a bracket marks the commits a Reading covers. A Reading is the Maintainer Repo comparing the System Repo's Copies across them, and it writes nothing there. A bracket closes when the verdicts are acted on, and its last commit becomes *read to*. *Read to* is not a take. The Maintainer Repo's parts stand between the commits, since it makes none.
- **System Repo:** its parts, each pointing at the commit it acts on.
- **┊:** no commit.
- **numbers:** 1 a Change, 2 the gate decides, 3 the gate closes, 4 Read, 5 List, 6 Judge, 7 Act, 8 Deliver, 9 the take, 10 the next Plan Step opens.
- **Versions:** the picture starts in the middle of the work. c0 and c1 were read and acted on, *read to* is c1, and c2 is the last take, which brought Version 1, in the same order as picture 1's take at c7. The Copies stay at Version 1 until a take brings Version 2.

| Commit | Where | System Repo | Maintainer Repo |
|---|---|---|---|
| c0 | main | earlier work, with Changes | read and acted on |
| c1 | main | earlier work, the last stop | read and acted on; *read to* |
| c2 | main | 9. the last take: main was still c1, and Version 1 comes in. Main moves here? Read says only at a gate | covered by Reading 1; open: how the take's changes are told apart from the System Repo's own |
| c3 | step 1's branch | work, no Copy changed | covered by Reading 1 |
| c4 | step 1's branch | 1. a Change: a Copy changed, with its Record | covered by Reading 1 |
| c5 | step 1's branch | 1. another Change: another Copy changed, with its Record | covered by Reading 1 |
| c6 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c6 by fast-forward | covered by Reading 1, its stop |
| no commit | | | 4 to 6. Read, List, Judge: c2 to c6. 7. Act: c6 becomes *read to*. 8. Deliver: the Update waits in `temp/` |
| c7 | main | 9. the take, once it checks: main is still the Reading's stop, c6, and the Version is still 1, the one the Update was built from. Version 2 comes in, in order: the Adapted Case for taking first; the files checked against the Update Note; every Copy taken whole, every Record cleared; Changes still needed put back, each with a fresh Record; verdicts acted on; Version 2 recorded; the Update removed from `temp/` (`temp/system-repo-change-simulation.md` §8, step 1, *At the take, in order*). Main moves here? Read says only at a gate | covered by the next Reading; open: how the take's changes are told apart |
| c8 | step 2's branch | 10. step 2 opens on Version 2 | |

#### Picture 2, the window missed

Step 2 opened before the take: the Update waited in `temp/`, and the human postponed the take (`temp/system-repo-change-simulation.md` §8, step 1, *A postponed take*). When step 2 opens before the Update is made, nothing is refused: no Update is staged while work is under way without the human's word, and it is made when work resumes, at the next opening (§7, step 1; step 2, *Before staging*).

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 Reading 1 covers c2 to c6.                   ┌  c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1
 Open: how the take's changes                 │     │                                         ◀──── main moves here? Read says only at a gate
 in c2 are told apart from the                │     ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
 System Repo's own                            │     │            │
                                              │     │         c3 ●  work, no Copy changed
                                              │     │            │
                                              │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 8. Read, List, Judge, Act,           ┐ ─▶  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 Deliver: c2 to c6; c6 becomes read to;    │        ┊
 the Update waits in temp/                 ┘        ┊
                                                    │
                                                    └─ cut ──────┐                            ◀──── 9. the take postponed, with its why
                                                                 │                            ◀──── 10. step 2 opens on Version 1
                                              ┌               c7 ●  work, on Version 1
 Reading 2 covers                             │                  │
 c7 to c9                                     │               c8 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │                  │
                                              └               c9 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                                 │
                                                 c9 ● ◀──────────┘                            ◀──── main moves to c9 by fast-forward, no new commit
                                                    ┊                                         ┄┄┄┄┄ 9. Take, at step 3's opening, refused: main is c9, not c6; no commit
 4 to 8 again. Read, List, Judge, Act,     ┐        ┊
 Deliver: c7 to c9; c9 becomes read to;    │        ┊
 a new Update replaces the waiting one     ┘        ┊
                                                    │
 The next Reading covers c10.                   c10 ●  the take: Version 2 comes in           ◀──── 9. Take, once it checks: main is still Reading 2's stop, c9,
 Open: how the take's changes                       │                                               and the Version is still 1, the one the Update was built from
 are told apart                                     │                                               In the order of picture 1's c7
                                                    │                                         ◀──── main moves here? Read says only at a gate
                                                    │
                                                    └─ cut ──────┐                            ◀──── 10. step 3 opens on Version 2
                                                                 │
                                                             c11 ●  work, on Version 2
```

Key: as in picture 1.

| Commit | Where | System Repo | Maintainer Repo |
|---|---|---|---|
| c0 | main | earlier work, with Changes | read and acted on |
| c1 | main | earlier work, the last stop | read and acted on; *read to* |
| c2 | main | 9. the last take: main was still c1, and Version 1 comes in. Main moves here? Read says only at a gate | covered by Reading 1; open: how the take's changes are told apart from the System Repo's own |
| c3 | step 1's branch | work, no Copy changed | covered by Reading 1 |
| c4 | step 1's branch | 1. a Change: a Copy changed, with its Record | covered by Reading 1 |
| c5 | step 1's branch | 1. another Change: another Copy changed, with its Record | covered by Reading 1 |
| c6 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c6 by fast-forward | covered by Reading 1, its stop |
| no commit | | | 4 to 8. Read, List, Judge, Act, Deliver: c2 to c6; c6 becomes *read to*; the Update waits in `temp/` |
| open | | 9. the take postponed, with its why: where the why is written, and so whether it is a commit, is open | |
| c7 | step 2's branch | 10. step 2 opens: work on Version 1 | covered by Reading 2 |
| c8 | step 2's branch | 1. a Change: a Copy changed, with its Record | covered by Reading 2 |
| c9 | step 2's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c9 by fast-forward | covered by Reading 2, its stop |
| no commit | | 9. the take, at step 3's opening: main is c9, not c6, so it is refused | |
| no commit | | | 4 to 8 again. Read, List, Judge, Act, Deliver: c7 to c9; c9 becomes *read to*; a new Update replaces the waiting one, and carries its verdicts not yet sent (`temp/system-repo-change-simulation.md` §8, step 1, *Before the take*) |
| c10 | main | 9. the take, once it checks: main is still Reading 2's stop, c9, and the Version is still 1, the one the Update was built from. Version 2 comes in, in the order of picture 1's c7. Main moves here? Read says only at a gate | covered by the next Reading; open: how the take's changes are told apart |
| c11 | step 3's branch | 10. step 3 opens on Version 2 | |

## 3. After, item 1a

The question: where does the take happen, and must main move only at a close? Option a changes only the end of picture 1; the rest stays as in Now. Options b and c of item 1a, the next Plan Step's first commit and a Plan Step of its own, were drawn once and dropped; they can be drawn again.

### Option a, a take of its own, on a branch

The take is run by its own Adapted Case, with no Plan Step. It cuts a branch from main at c6, makes one commit per part of the take's order, and moves main by fast-forward at its gate's close (`temp/system-repo-change-simulation.md` §8, step 1, *At the take, in order*). The take is run by the Adapted Case for taking an Update; the first thing it takes is the Update's own new version of itself, so the rest is taken by the new one (Failure Case 10). Its checks come first: main is still the Reading's stop, and the files match the Update Note. Its gate comes last, c14. It does for the Changes put back and the verdicts acted on what a Plan Step's gate does for its Changes (`temp/system-repo-change-simulation.md` §3, step 2): the Copies compared against c9, each Change shown with its fresh Record and decided, Changes with one reason linked, and the misfit question asked against Version 2. Step 2 is cut from c14 as c15. c7 commits the Update as it arrived, in `temp/` and not yet in force: a record of what came, before the take changes anything. It may go later. c10 and c11 stand for one commit each per Change put back and per verdict acted on, zero or more.

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 Reading 1 covers c2 to c6.                   ┌  c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1
 Open: how the take's changes                 │     │                                         ◀──── main moves here? Read says only at a gate
 in c2 are told apart from the                │     ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
 System Repo's own                            │     │            │
                                              │     │         c3 ●  work, no Copy changed
                                              │     │            │
                                              │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 6. Read, List, Judge: c2 to c6       ┐ ─▶  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 7. Act: c6 becomes read to                │        ┊
 8. Deliver: the Update waits in temp/     ┘        ┊
                                                    ┊
                                                    ┊
                                                    │
                                                    ├─ cut ──────┐                            ◀──── 9. Take, once it checks: main is still the Reading's stop, c6,
                                                    │            │                                  and the Version is still 1, the one the Update was built from
 The next Reading covers                      │     │         c7 ●  the Update, as it arrived ◀──── committed in temp/, not yet in force: a record
 c7 to c14. Open: how the                     │     │            │                                  of what came, before the take changes anything
 take's changes are told apart                │     │            │
                                              │     │         c8 ●  the new Adapted Case      ◀──── for taking, at Version 2, put in first; it runs the rest of the take
                                              │     │            ┊                            ┄┄┄┄┄ the files checked against the Update Note; no commit
                                              │     │         c9 ●  every Copy at Version 2   ◀──── Copies taken whole; every Record cleared
                                              │     │            │
                                              │     │        c10 ●  a Change put back         ◀──── one per Change, each with a fresh Record
                                              │     │            │
                                              │     │        c11 ●  a verdict acted on        ◀──── zero or more: unsound reversed or kept, a question answered
                                              │     │            │
                                              │     │        c12 ●  Version 2 recorded        ◀──── with the commit that holds it, c9
                                              │     │            │
                                              │     │        c13 ●  the Update removed        ◀──── the Update and the Update Note leave temp/
                                              │     │            │
                                              └     │        c14 ●  the gate closes           ◀──── the gate decides each Change put back, and closes
                                                    │            │
                                                c14 ● ◀──────────┘                            ◀──── main moves to c14 by fast-forward, at the gate's close
                                                    │
                                                    └─ cut ──────┐                            ◀──── 10. step 2 opens on Version 2
                                                                 │
                                                             c15 ●  work, on Version 2
```

### Option d, the rule narrowed

Read's rule is narrowed to its reason: a Plan Step's work reaches main only at its gate's close, by fast-forward, so a Reading never reads Changes a gate may still edit or reverse (`temp/system-repo-change-simulation.md` §4, step 1, *Chosen*). Today's playbook says the same: a Plan Step reaches main by fast-forward from its branch (`delivery/fills/cbc-run-pure-playbook.md`, *At the close*). Main then moves in two ways only: at a gate's close, and at a take. A take is not a Change (§3, step 1), and what it puts back is decided by the human at the take (§8, step 1), so nothing on main waits for a gate. The take stays one commit on main, as in Now; only the marks at c2 and c7 change.

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 Reading 1 covers c2 to c6.                   ┌  c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1
 Open: how the take's changes                 │     │                                         ◀──── main moves to c2 by the take, which the rule allows
 in c2 are told apart from the                │     ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
 System Repo's own                            │     │            │
                                              │     │         c3 ●  work, no Copy changed
                                              │     │            │
                                              │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 6. Read, List, Judge: c2 to c6       ┐ ─▶  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 7. Act: c6 becomes read to                │        ┊
 8. Deliver: the Update waits in temp/     ┘        ┊
                                                    ┊
                                                    ┊
                                                    │
 The next Reading covers c7.                     c7 ●  the take: Version 2 comes in           ◀──── 9. Take, once it checks: main is still the Reading's stop, c6,
 Open: how the take's changes                       │                                               and the Version is still 1, the one the Update was built from
 are told apart                                     │                                               In order: the Adapted Case for taking first; the files checked
                                                    │                                               against the Update Note; every Copy taken whole, every Record
                                                    │                                               cleared; Changes still needed put back, each with a fresh Record;
                                                    │                                               verdicts acted on; Version 2 recorded; the Update removed from temp/
                                                    │                                         ◀──── main moves to c7 by the take, which the rule allows
                                                    │
                                                    └─ cut ──────┐                            ◀──── 10. step 2 opens on Version 2
                                                                 │
                                                              c8 ●  work, on Version 2
```

## 4. After, item 1b

The question: after a take, where does the next Reading start (`temp/system-repo-change-simulation.md` §4, step 3, *Open*)? *Read to* is c1, and the take at c2 lies inside Reading 1's span. Only the start of picture 1 changes; the rest stays as in Now.

### Option a, read the take

Reading 1 starts after *read to*, c1, and covers the take. Its first part reads c2 alone: it compares the Copies at c2 with Version 1, and what differs is what the System Repo put back at the take. Then the rest is read as usual. This is the answer to try already written into Read step 3's two Opens.

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 Reading 1 covers c2 to c6.                   ┌  c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1
 First part, c2 alone: its Copies             │     │                                         ◀──── main moves here? Read says only at a gate
 against Version 1; what differs              │     ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
 was put back at the take                     │     │            │
                                              │     │         c3 ●  work, no Copy changed
                                              │     │            │
                                              │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 6. Read, List, Judge: c2 to c6       ┐ ─▶  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 7. Act: c6 becomes read to                │        ┊
 8. Deliver: the Update waits in temp/     ┘        ┊
```

### Option b, skip the take

Reading 1 starts after the commit the take recorded, c2, not after *read to*, so it covers c3 to c6 (`temp/system-repo-change-simulation.md` §8, step 1, item 6). A Change the System Repo put back inside the take's commit is never read; it is read only if it is made in a commit after c2.

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 skipped: Reading 1 starts after c2 ─▶           c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1
                                                    │                                         ◀──── main moves here? Read says only at a gate
                                                    ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
                                                    │            │
                                              ┌     │         c3 ●  work, no Copy changed
 Reading 1                                    │     │            │
 covers                                       │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
 c3 to c6                                     │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 6. Read, List, Judge: c3 to c6       ┐ ─▶  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 7. Act: c6 becomes read to                │        ┊
 8. Deliver: the Update waits in temp/     ┘        ┊
```

### Option c, start at the commit holding the Version

Drawn on item 1a's take, where each part of the take is its own commit. A Reading compares each Copy at two points, its start and its stop, and the Records in the Copies say the why (`temp/system-repo-change-simulation.md` §4, step 3, option a). After a take, the start is the later of *read to* and the commit the take recorded as holding the new Version, c9 here: from there, everything that differs is the System Repo's own. The take's System Kit part, c7 to c9, is skipped; what it put back, c10, and the verdicts it acted on, c11, are read, with the step's new work. A Change put back carries a fresh Record saying so, so it is told apart from a new one; where the take ended, c13, could mark the split as well, but is not needed for it.

```
 Maintainer Repo                                   main      branches                              System Repo
 ───────────────                                   ────      ────────                              ───────────
 read to: Reading 1's stop ─▶                    c6 ●  step 1's gate closed
                                                    │
                                                    ├─ cut ──────┐                            ◀──── 9. Take, once it checks: main is still c6, Version still 1
                                                    │            │
 skipped: the System Kit's part                     │         c7 ●  the Update, as it arrived
                                                    │            │
                                                    │         c8 ●  the new Adapted Case
                                                    │            │
 Reading 2 starts after c9 ─▶                       │         c9 ●  every Copy at Version 2   ◀──── the commit that holds Version 2
                                                    │            │
 Reading 2 covers                             ┌     │        c10 ●  a Change put back         ◀──── with its fresh Record, saying so
 c10 to c16:                                  │     │            │
 the System Repo's                            │     │        c11 ●  a verdict acted on
 own part only                                │     │            │
                                              │     │        c12 ●  Version 2 recorded        ◀──── with the commit that holds it, c9
                                              │     │            │
                                              │     │        c13 ●  the Update removed
                                              │     │            │
                                              │ c13 ● ◀──────────┘                            ◀──── main moves to c13 by fast-forward
                                              │     │
                                              │     └─ cut ──────┐                            ◀──── 10. step 2 opens on Version 2
                                              │                  │
                                              │              c14 ●  work, no Copy changed
                                              │                  │
                                              │              c15 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │                  │
                                              └              c16 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                                 │
 4 to 7. Read, List, Judge, Act:              ┐ c16 ● ◀──────────┘                            ◀──── main moves to c16 by fast-forward
 c10 to c16; c16 becomes read to              ┘     ┊
```
