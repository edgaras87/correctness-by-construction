# A System Repo's Change, as a Flow

<!-- A draft for the Plan Step "Find how what we know stays true",
     stage 1. It pictures the System Repo's commits in the round of
     temp/system-repo-change-simulation.md, and the part acting on
     each. The facts live in the
     simulation, never here. "Now" pictures the simulation as it is.
     "After" pictures one open decision, one drawing per option, each
     named by its option. When the decision is made, the simulation
     changes, the chosen option's drawing becomes "Now", and "After"
     is emptied. It goes when the Plan Step closes, and
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
 Maintainer Repo                                 main      branches                                 System Repo
 ───────────────                                 ────      ────────                                 ───────────
 
 read and
 acted on.
 read to: where the last Reading stopped  ─▶  ┌  c0 ●  earlier work
                                              │     │
                                              └  c1 ●  take                                   ◀──── the last take, on Version 1
                                                    │
                                              ┌     ├─ cut ─▶ c2 ●  work, no Copy changed
 Reading 1                                    │     │            │
 covers                                       │     │         c3 ●  a Copy changed            ◀──── 1. a Change, with its Record
 c2 to c5                                     │     │            │
                                              │     │         c4 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                              │     │            │
                                              └     │         c5 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                    │            │
                                                 c5 ● ◀──────────┘                            ◀──── main moves to c5 by fast-forward, no new commit
 4 to 6. Read, List, Judge: c2 to c5                ┊
 7. Act: c5 becomes read to                         ┊
 8. Deliver: the Update waits in temp/              ┊
                                                    │
                                                 c6 ●  the take: Version 2 comes in           ◀──── 9. Take: main is still c5, so it runs
                                                    │                                         ◀──── main moves here? Read says only at a gate
                                                    │                                         ◀┄┄┄┄ open: next Reading after c5, or after c6?
                                                    │
                                                    └─ cut ─▶ c7 ●  work, on Version 2        ◀──── 10. step 2 opens on Version 2
```

**Key:**

- **commits:** imaginary commits of the System Repo, oldest first, top to bottom.
- **main, branches:** a step's branch is cut from main, to its right. At its gate's close, main moves to the branch's last commit by fast-forward: a commit named again on main is no new commit.
- **Maintainer Repo:** a bracket marks the commits a Reading covers. A Reading is the Maintainer Repo comparing the System Repo's Copies across them, and it writes nothing there. A bracket closes when the verdicts are acted on, and its last commit becomes *read to*. *Read to* is not a take. The Maintainer Repo's parts stand between the commits, since it makes none.
- **System Repo:** its parts, each pointing at the commit it acts on.
- **┊:** no commit.
- **numbers:** 1 a Change, 2 the gate decides, 3 the gate closes, 4 Read, 5 List, 6 Judge, 7 Act, 8 Deliver, 9 the take, 10 the next Plan Step opens.
- **Versions:** the Copies are at Version 1 until a take brings Version 2. The picture starts at c1: read, judged and acted on, and taken as Version 1, so nothing earlier waits.

| Commit | Where | System Repo | Maintainer Repo |
|---|---|---|---|
| c0 | main | earlier work | read and acted on |
| c1 | main | the last stop, on Version 1 | *read to* |
| c2 | step 1's branch | work, no Copy changed | covered by Reading 1 |
| c3 | step 1's branch | 1. a Change: a Copy changed, with its Record | covered by Reading 1 |
| c4 | step 1's branch | 1. another Change: another Copy changed, with its Record | covered by Reading 1 |
| c5 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c5 by fast-forward | covered by Reading 1, its stop |
| no commit | | | 4 to 6. Read, List, Judge: c2 to c5. 7. Act: c5 becomes *read to*. 8. Deliver: the Update waits in `temp/` |
| c6 | main | 9. the take: main is still c5, so it runs, and Version 2 comes in. Main moves here? Read says only at a gate | open: does the next Reading start after c5, or after c6? |
| c7 | step 2's branch | 10. step 2 opens on Version 2 | |

#### Picture 2, the window missed

Step 2 opened before the take: the human started it before the Update came, or postponed the take (`temp/system-repo-change-simulation.md` §8, step 1, *A postponed take*).

```
 Maintainer Repo                           main      branches                          System Repo
 ───────────────                           ────      ────────                          ───────────
 read and                             ┌  c0 ●  earlier work
 acted on                             │     │
                                      └  c1 ●  the last stop, on Version 1            ◀──── read to: where the last Reading stopped
                                            │
                                      ┌     ├─ cut ─▶ c2 ●  work, no Copy changed
 Reading 1                            │     │            │
 covers                               │     │         c3 ●  a Copy changed            ◀──── 1. a Change, with its Record
 c2 to c5                             │     │            │
                                      │     │         c4 ●  another Copy changed      ◀──── 1. another Change, with its Record
                                      │     │            │
                                      └     │         c5 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                            │            │
                                         c5 ● ◀──────────┘                            ◀──── main moves to c5 by fast-forward, no new commit
 4 to 7. Read, List, Judge, Act:            ┊
 c2 to c5; c5 becomes read to               ┊
                                            │
                                      ┌     └─ cut ─▶ c6 ●  work, on Version 1        ◀──── 10. step 2 opened before the take
 8. Deliver: Update waits in temp/    │                  ┊
 read again                           │               c7 ●  a Copy changed            ◀──── 1. a Change, with its Record
 c6 to c8                             │                  │
                                      └               c8 ●  the gate closes           ◀──── 2, 3. the gate decides each Change, and closes
                                                         │
                                         c8 ● ◀──────────┘                            ◀──── main moves to c8 by fast-forward, no new commit
                                                                                      ┄┄┄┄┄ 9. Take refused: main is c8, not c5; no commit
 4 again. Read: c6 to c8; a new
 Update replaces the waiting one
```

Key: as in picture 1.

| Commit | Where | System Repo | Maintainer Repo |
|---|---|---|---|
| c0 | main | earlier work | read and acted on |
| c1 | main | the last stop, on Version 1 | *read to* |
| c2 | step 1's branch | work, no Copy changed | covered by Reading 1 |
| c3 | step 1's branch | 1. a Change: a Copy changed, with its Record | covered by Reading 1 |
| c4 | step 1's branch | 1. another Change: another Copy changed, with its Record | covered by Reading 1 |
| c5 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c5 by fast-forward | covered by Reading 1, its stop |
| no commit | | | 4 to 7. Read, List, Judge, Act: c2 to c5; c5 becomes *read to* |
| c6 | step 2's branch | 10. step 2 opened before the take: work on Version 1 | covered by the Reading again |
| no commit | | | 8. Deliver: the Update waits in `temp/` |
| c7 | step 2's branch | 1. a Change: a Copy changed, with its Record | covered by the Reading again |
| c8 | step 2's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c8 by fast-forward | covered by the Reading again, its stop |
| no commit | | 9. the take: main is c8, not c5, so it is refused | |
| no commit | | | 4 again. Read: c6 to c8; a new Update replaces the waiting one |
