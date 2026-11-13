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

### The System Repo's commits

#### Picture 1, the take inside its window

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 Reading 1 compares the last take's           ┌  c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1; its branch is not drawn
 clean copy, on c2's branch, with             │     │                                         ◀──── main moved to c2 when the take's gate closed, as at c14
 c6, its stop. The commits between            │     ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
 are history                                  │     │            │
                                              │     │         c3 ●  work, no Copy changed
                                              │     │            │
                                              │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 6. Read, List, Judge                 ┐ ─▶  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 7. Act: c6 becomes read to                │        ┊
 8. Deliver: the Update waits in temp/     ┘        ┊
                                                    ┊
                                                    ┊
                                                    │
                                                    ├─ cut ──────┐                            ◀──── 9. Take, once it checks: main is still the Reading's stop, c6,
                                                    │            │                                  and the Version is still 1, the one the Update was built from
                                                    │         c7 ●  the Update, as it arrived ◀──── committed in temp/, not yet in force: a record
                                                    │            │                                  of what came, before the take changes anything
                                                    │            │
                                                    │         c8 ●  the new Adapted Case      ◀──── for taking, at Version 2, put in first; it runs the rest of the take
                                                    │            ┊                            ┄┄┄┄┄ the files checked against the Update Note; no commit
 The next Reading compares c9, the            ┌     │         c9 ●  every Copy at Version 2   ◀──── Copies taken whole; every Record cleared
 clean copy, checked against Version          │     │            │
 2, with main's latest snapshot               │     │        c10 ●  a Change put back         ◀──── one per Change, each with a fresh Record
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

**Key:**

- **commits:** imaginary commits of the System Repo, oldest first, top to bottom.
- **main, branches:** a step's or a take's branch is cut from main, to its right. At its gate's close, main moves to the branch's last commit by fast-forward: a commit named again on main is no new commit.
- **Maintainer Repo:** a bracket joins the two snapshots a Reading compares: its top is the older, *read to* or, after a take, the clean copy, and its bottom is the stop. The commits between are history, opened only to understand something deeper. A Reading writes nothing in the System Repo. A bracket closes when the verdicts are acted on, and its stop becomes *read to*. *Read to* is not a take. The Maintainer Repo's parts stand between the commits, since it makes none.
- **System Repo:** its parts, each pointing at the commit it acts on.
- **┊:** no commit.
- **numbers:** 1 a Change, 2 the gate decides, 3 the gate closes, 4 Read, 5 List, 6 Judge, 7 Act, 8 Deliver, 9 the take, 10 the next Plan Step opens.
- **Versions:** the picture starts in the middle of the work. c0 and c1 were read and acted on, *read to* is c1, and c2 is the last take, which brought Version 1 by the same parts as picture 1's take from c7 to c14. Its branch is not drawn. The Copies stay at Version 1 until a take brings Version 2.

| Commit | Where | System Repo | Maintainer Repo |
|---|---|---|---|
| c0 | main | earlier work, with Changes | read and acted on |
| c1 | main | earlier work, the last stop | read and acted on; *read to* |
| c2 | main | 9. the last take: main was still c1, and Version 1 comes in. Its branch is not drawn; main moved to c2 when its gate closed | Reading 1's older snapshot is this take's clean copy, on its branch |
| c3 | step 1's branch | work, no Copy changed | history between Reading 1's snapshots |
| c4 | step 1's branch | 1. a Change: a Copy changed, with its Record | history between Reading 1's snapshots |
| c5 | step 1's branch | 1. another Change: another Copy changed, with its Record | history between Reading 1's snapshots |
| c6 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c6 by fast-forward | Reading 1's stop |
| no commit | | | 4 to 6. Read, List, Judge: the last take's clean copy compared with c6. 7. Act: c6 becomes *read to*. 8. Deliver: the Update waits in `temp/` |
| no commit | main | 9. the take checks, case 1: main is still the Reading's stop, c6, and the Version is still 1, the one the Update was built from (`temp/system-repo-change-simulation.md` §8, step 1, *Before the take*). Its branch is cut from c6 | |
| c7 | the take's branch | the Update, as it arrived, committed in `temp/`, not yet in force | |
| c8 | the take's branch | the new Adapted Case for taking, at Version 2, put in first; then the files are checked against the Update Note, with no commit | |
| c9 | the take's branch | every Copy taken whole, at Version 2; every Record cleared | the clean copy: the next Reading's older snapshot, checked first against Version 2 |
| c10 | the take's branch | a Change put back, with a fresh Record; one commit per Change | history between the next Reading's snapshots |
| c11 | the take's branch | a verdict acted on; zero or more | history between the next Reading's snapshots |
| c12 | the take's branch | Version 2 recorded, with the commit that holds it, c9 | history between the next Reading's snapshots |
| c13 | the take's branch | the Update and its Update Note removed from `temp/` | history between the next Reading's snapshots |
| c14 | the take's branch, then main | the take's gate decides each Change put back, and closes; main moves to c14 by fast-forward (`temp/system-repo-change-simulation.md` §8, step 1, *At the take, in order*) | main's latest snapshot, until step 2's work reaches main |
| c15 | step 2's branch | 10. step 2 opens on Version 2 | |

#### Picture 2, the window missed

Step 2 opened before the take: the Update waited in `temp/`, and the human postponed the take (`temp/system-repo-change-simulation.md` §8, step 1, *A postponed take*). When step 2 opens before the Update is made, nothing is refused: no Update is staged while work is under way without the human's word, and it is made when work resumes, at the next opening (§7, step 1; step 2, *Before staging*).

```
 Maintainer Repo                                   main      branches                               System Repo
 ───────────────                                   ────      ────────                               ───────────
 read and acted on                            ┌  c0 ●  earlier work, with Changes
                                              │     │
 read to: the last Reading's stop ─▶          └  c1 ●  earlier work, the last stop
                                                    │
 Reading 1 compares the last take's           ┌  c2 ●  the last take: Version 1 comes in      ◀──── 9. the last take: main was still c1; its branch is not drawn
 clean copy, on c2's branch, with             │     │                                         ◀──── main moved to c2 when the take's gate closed, as at c17
 c6, its stop. The commits between            │     ├─ cut ──────┐                            ◀──── 10. step 1 opens on Version 1
 are history                                  │     │            │
                                              │     │         c3 ●  work, no Copy changed
                                              │     │            │
                                              │     │         c4 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │     │            │
                                              │     │         c5 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c6 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
 4 to 8. Read, List, Judge, Act,           ┐  ┌  c6 ● ◀──────────┘                            ◀──── main moves to c6 by fast-forward, no new commit
 Deliver; c6 becomes read to;              │  │     ┊
 the Update waits in temp/                 ┘  │     ┊
                                              │     │
                                              │     └─ cut ──────┐                            ◀──── 9. the take postponed, with its why
                                              │                  │                            ◀──── 10. step 2 opens on Version 1
 Reading 2 compares c6, read to,              │               c7 ●  work, on Version 1
 with c9, its stop. The commits               │                  │
 between are history                          │               c8 ●  a Copy changed            ◀──── 1. a Change, with its Record
                                              │                  │
                                              └               c9 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                                 │
                                                 c9 ● ◀──────────┘                            ◀──── main moves to c9 by fast-forward, no new commit
                                                    ┊                                         ┄┄┄┄┄ 9. Take, at step 3's opening: case 2, main is c9, not c6, so no take; no commit
 4 to 8 again. Read, List, Judge, Act,     ┐        ┊
 Deliver; c9 becomes read to;              │        ┊
 a new Update replaces the waiting one     ┘        ┊
                                                    │
                                                    ├─ cut ──────┐                            ◀──── 9. Take, once it checks: main is still Reading 2's stop, c9,
                                                    │            │                                  and the Version is still 1, the one the Update was built from
                                                    │        c10 ●  the Update, as it arrived ◀──── committed in temp/, not yet in force: a record
                                                    │            │                                  of what came, before the take changes anything
                                                    │            │
                                                    │        c11 ●  the new Adapted Case      ◀──── for taking, at Version 2, put in first; it runs the rest of the take
                                                    │            ┊                            ┄┄┄┄┄ the files checked against the Update Note; no commit
 The next Reading compares c12, the           ┌     │        c12 ●  every Copy at Version 2   ◀──── Copies taken whole; every Record cleared
 clean copy, checked against Version          │     │            │
 2, with main's latest snapshot               │     │        c13 ●  a Change put back         ◀──── one per Change, each with a fresh Record
                                              │     │            │
                                              │     │        c14 ●  a verdict acted on        ◀──── zero or more: unsound reversed or kept, a question answered
                                              │     │            │
                                              │     │        c15 ●  Version 2 recorded        ◀──── with the commit that holds it, c12
                                              │     │            │
                                              │     │        c16 ●  the Update removed        ◀──── the Update and the Update Note leave temp/
                                              │     │            │
                                              └     │        c17 ●  the gate closes           ◀──── the gate decides each Change put back, and closes
                                                    │            │
                                                c17 ● ◀──────────┘                            ◀──── main moves to c17 by fast-forward, at the gate's close
                                                    │
                                                    └─ cut ──────┐                            ◀──── 10. step 3 opens on Version 2
                                                                 │
                                                             c18 ●  work, on Version 2
```

Key: as in picture 1.

| Commit | Where | System Repo | Maintainer Repo |
|---|---|---|---|
| c0 | main | earlier work, with Changes | read and acted on |
| c1 | main | earlier work, the last stop | read and acted on; *read to* |
| c2 | main | 9. the last take: main was still c1, and Version 1 comes in. Its branch is not drawn; main moved to c2 when its gate closed | Reading 1's older snapshot is this take's clean copy, on its branch |
| c3 | step 1's branch | work, no Copy changed | history between Reading 1's snapshots |
| c4 | step 1's branch | 1. a Change: a Copy changed, with its Record | history between Reading 1's snapshots |
| c5 | step 1's branch | 1. another Change: another Copy changed, with its Record | history between Reading 1's snapshots |
| c6 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c6 by fast-forward | Reading 1's stop; then *read to*, Reading 2's older snapshot |
| no commit | | | 4 to 8. Read, List, Judge, Act, Deliver: the last take's clean copy compared with c6; c6 becomes *read to*; the Update waits in `temp/` |
| open | | 9. the take postponed, with its why: where the why is written, and so whether it is a commit, is open | |
| c7 | step 2's branch | 10. step 2 opens: work on Version 1 | history between Reading 2's snapshots |
| c8 | step 2's branch | 1. a Change: a Copy changed, with its Record | history between Reading 2's snapshots |
| c9 | step 2's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c9 by fast-forward | Reading 2's stop |
| no commit | | 9. the take checks at step 3's opening, case 2: main is c9, not c6, so there is no take, and the System Repo says so (`temp/system-repo-change-simulation.md` §8, step 1, *Before the take*) | |
| no commit | | | 4 to 8 again. Read, List, Judge, Act, Deliver: c6 compared with c9; c9 becomes *read to*; a new Update replaces the waiting one, and carries its verdicts not yet sent (`temp/system-repo-change-simulation.md` §8, step 1, *Before the take*) |
| no commit | main | 9. the take checks, case 1: main is still Reading 2's stop, c9, and the Version is still 1, the one the Update was built from. Its branch is cut from c9 | |
| c10 | the take's branch | the Update, as it arrived, committed in `temp/`, not yet in force | |
| c11 | the take's branch | the new Adapted Case for taking, at Version 2, put in first; then the files are checked against the Update Note, with no commit | |
| c12 | the take's branch | every Copy taken whole, at Version 2; every Record cleared | the clean copy: the next Reading's older snapshot, checked first against Version 2 |
| c13 | the take's branch | a Change put back, with a fresh Record; one commit per Change | history between the next Reading's snapshots |
| c14 | the take's branch | a verdict acted on; zero or more | history between the next Reading's snapshots |
| c15 | the take's branch | Version 2 recorded, with the commit that holds it, c12 | history between the next Reading's snapshots |
| c16 | the take's branch | the Update and its Update Note removed from `temp/` | history between the next Reading's snapshots |
| c17 | the take's branch, then main | the take's gate decides each Change put back, and closes; main moves to c17 by fast-forward | main's latest snapshot, until step 3's work reaches main |
| c18 | step 3's branch | 10. step 3 opens on Version 2 | |
