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

Imaginary commits of the System Repo, oldest first, top to bottom. The left column is main; a step's branch is cut from main and drawn to its right. The middle column marks the commits a Reading reads. The round's parts point at the commit they act on, numbered: 1 a Change, 2 the gate decides, 3 the gate closes, 4 Read, 5 List, 6 Judge, 7 Act, 8 Deliver, 9 the take, 10 the next Plan Step opens. A dotted line is no commit. At a gate's close, main moves to the branch's last commit by fast-forward: a commit named again on main is main moving to it, not a new commit.

#### Picture 1, the take inside its window

```
 main      branches                       read                parts
 ────      ────────                       ────                ─────
 c0 ●  earlier steps' work                ┐ read
    │                                     │ before
 c1 ●  the last stop                      ┘             ◀──── read to: where the last Reading stopped
    │
    ├─ cut ─▶ c2 ●  a Change, its Record  ┐             ◀──── 1. a Change, with its Record, on step 1's branch
    │            │                        │ Reading 1
    │         c3 ●  work                  │ reads
    │            │                        │ c2 to c5
    │         c4 ●  a Change, its Record  │             ◀──── 1. another Change, with its Record
    │            │                        │
    │         c5 ●  the gate closes       ┘             ◀──── 2, 3. the gate decides each Change, and closes
    │            │
 c5 ● ◀──────────┘                                      ◀──── main moves to c5 by fast-forward, no new commit
    │                                                   ◀──── 4 to 6. Read, List, Judge: c2 to c5, the whole span
    │                                                   ◀──── 7. Act: c5 becomes read to
    ┊                                                   ┄┄┄┄┄ 8. Deliver: no commit; the Update waits in temp/
    │
 c6 ●  the take, made on main                           ◀──── 9. Take: main is still c5, so it runs
    │                                                   ◀──── main moves here? Read says only at a gate
    │                                                   ◀┄┄┄┄ open: next Reading after c5, or after c6?
    │
    └─ cut ─▶ c7 ●  step 2's work                       ◀──── 10. step 2 opens on the new Copies
```

| Commit | Where | What happens | Reading |
|---|---|---|---|
| c0 | main | earlier steps' work | read before |
| c1 | main | the last stop | *read to* |
| c2 | step 1's branch | 1. a Change, with its Record | Reading 1 |
| c3 | step 1's branch | work | Reading 1 |
| c4 | step 1's branch | 1. another Change, with its Record | Reading 1 |
| c5 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c5 by fast-forward | Reading 1 stops here |
| no commit | Maintainer Repo | 4 to 6. Read, List, Judge: c2 to c5. 7. Act: c5 becomes *read to*. 8. Deliver: the Update waits in `temp/` | |
| c6 | main | 9. the take: main is still c5, so it runs. Main moves here? Read says only at a gate | open: does the next Reading start after c5, or after c6? |
| c7 | step 2's branch | 10. step 2 opens on the new Copies | |

#### Picture 2, the window missed

Step 2 opened before the take: the human started it before the Update came, or postponed the take (`temp/system-repo-change-simulation.md` §8, step 1, *A postponed take*).

```
 main      branches                       read                parts
 ────      ────────                       ────                ─────
 c0 ●  earlier steps' work                ┐ read
    │                                     │ before
 c1 ●  the last stop                      ┘             ◀──── read to: where the last Reading stopped
    │
    ├─ cut ─▶ c2 ●  a Change, its Record  ┐             ◀──── 1. a Change, with its Record, on step 1's branch
    │            │                        │ Reading 1
    │         c3 ●  work                  │ reads
    │            │                        │ c2 to c5
    │         c4 ●  a Change, its Record  │             ◀──── 1. another Change, with its Record
    │            │                        │
    │         c5 ●  the gate closes       ┘             ◀──── 2, 3. the gate decides each Change, and closes
    │            │
 c5 ● ◀──────────┘                                      ◀──── main moves to c5 by fast-forward, no new commit
    │                                                   ◀──── 4 to 7. Read, List, Judge, Act: c2 to c5;
    │                                                         c5 becomes read to
    │
    └─ cut ─▶ c6 ●  work, old Copies      ┐             ◀──── 10. step 2 opened before the take
                 ┊                        │             ┄┄┄┄┄ 8. Deliver: no commit; the Update waits in temp/
              c7 ●  a Change, its Record  │ read again  ◀──── 1. a Change, with its Record, on step 2's branch
                 │                        │ c6 to c8
              c8 ●  the gate closes       ┘             ◀──── 2, 3. the gate decides each Change, and closes
                 │
 c8 ● ◀──────────┘                                      ◀──── main moves to c8 by fast-forward, no new commit
                                                        ┄┄┄┄┄ 9. Take: main is c8, not c5, so it is refused; no commit
                                                        ┄┄┄┄┄ 4 again. Read: c6 to c8; a new Update replaces the waiting one
```

| Commit | Where | What happens | Reading |
|---|---|---|---|
| c0 | main | earlier steps' work | read before |
| c1 | main | the last stop | *read to* |
| c2 | step 1's branch | 1. a Change, with its Record | Reading 1 |
| c3 | step 1's branch | work | Reading 1 |
| c4 | step 1's branch | 1. another Change, with its Record | Reading 1 |
| c5 | step 1's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c5 by fast-forward | Reading 1 stops here |
| no commit | Maintainer Repo | 4 to 7. Read, List, Judge, Act: c2 to c5; c5 becomes *read to* | |
| c6 | step 2's branch | 10. step 2 opened before the take: work on the old Copies | read again |
| no commit | Maintainer Repo | 8. Deliver: the Update waits in `temp/` | |
| c7 | step 2's branch | 1. a Change, with its Record | read again |
| c8 | step 2's branch, then main | 2, 3. the gate decides each Change, and closes; main moves to c8 by fast-forward | read again stops here |
| no commit | System Repo | 9. the take: main is c8, not c5, so it is refused | |
| no commit | Maintainer Repo | 4 again. Read: c6 to c8; a new Update replaces the waiting one | |
