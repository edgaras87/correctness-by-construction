# A System Repo's Change, as a Flow

<!-- A draft for the Plan Step "Find how what we know stays true",
     stage 1. It pictures the whole round of
     temp/system-repo-change-simulation.md. The facts live in the
     simulation, never here. "Now" pictures the simulation as it is.
     "After" pictures one open decision, one drawing per option, each
     named by its option. When the decision is made, the simulation
     changes, the chosen option's drawing becomes "Now", and "After"
     is emptied. B1 and B2 are two forms of one picture, both kept
     until one reads better. It goes when the Plan Step closes, and
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

### B1, two boxes, top to bottom

```mermaid
flowchart TB
  subgraph SR["System Repo"]
    S1["1. Plan Step works:<br/>a Copy changed, with its Record"]
    S2["2. Gate decides each Change"]
    S3["3. Gate closes:<br/>main moves"]
    T1["9. Take, before the next Plan Step opens:<br/>main still the stop?<br/>Copies whole, Changes put back,<br/>the take's commit recorded.<br/>Main moves? Read says only at a gate"]
    S4["10. Next Plan Step opens"]
    S1 --> S2 --> S3
    T1 --> S4
    S4 -- "next round" --> S1
  end
  subgraph MR["Maintainer Repo"]
    M1["4. Read: from read to,<br/>to main, the stop"]
    M2["5. List, nothing judged"]
    M3["6. Judge: a verdict per line"]
    M4["7. Act: System Kit changed;<br/>the stop becomes read to"]
    M5["8. Deliver: the Update made"]
    M1 --> M2 --> M3 --> M4 --> M5
  end
  S3 -. "read only, nothing written" .-> M1
  M5 -- "staged into temp/ only" --> T1
  T1 -. "open: the next Reading<br/>starts here?" .-> M1
```

### B2, two rows, left to right

```mermaid
flowchart LR
  subgraph SR["System Repo"]
    direction LR
    S1["1. Plan Step works:<br/>a Copy changed,<br/>with its Record"] --> S2["2. Gate decides<br/>each Change"] --> S3["3. Gate closes:<br/>main moves"]
    T1["9. Take:<br/>main moves?<br/>Read says only at a gate"] --> S4["10. Next Plan<br/>Step opens"]
  end
  subgraph MR["Maintainer Repo"]
    direction LR
    M1["4. Read:<br/>read to → main"] --> M2["5. List"] --> M3["6. Judge"] --> M4["7. Act:<br/>stop becomes read to"] --> M5["8. Deliver"]
  end
  S3 -. "read only" .-> M1
  M5 -- "into temp/ only" --> T1
  T1 -. "open: next Reading<br/>starts here?" .-> M1
```

## 3. After, item 1

The question: where does the take happen, so that neither the gate nor the next Reading counts the Update as the System Repo's own work? Only the System Repo's side changes; steps 4 to 8 stay as they are.

### Option a, a take of its own

The take is run by its own Adapted Case, an Agent Skill or an Agent Rule, with no Plan Step. Its own check is its gate. Main moves at a gate's close or at a take. The next Reading starts at the take's commit, and reads the take by itself first.

#### B1

```mermaid
flowchart TB
  subgraph SR["System Repo"]
    S1["1. Plan Step works:<br/>a Copy changed, with its Record"]
    S2["2. Gate decides each Change"]
    S3["3. Gate closes:<br/>main moves"]
    T1["9. Take, by its own Adapted Case,<br/>no Plan Step:<br/>main still the stop?<br/>Copies whole, Changes put back,<br/>the take's commit recorded.<br/>Main moves"]
    S4["10. Next Plan Step opens"]
    S1 --> S2 --> S3
    T1 --> S4
    S4 -- "next round" --> S1
  end
  subgraph MR["Maintainer Repo"]
    M1["4. Read: from read to,<br/>to main, the stop"]
    M2["5. List, nothing judged"]
    M3["6. Judge: a verdict per line"]
    M4["7. Act: System Kit changed;<br/>the stop becomes read to"]
    M5["8. Deliver: the Update made"]
    M1 --> M2 --> M3 --> M4 --> M5
  end
  S3 -. "read only, nothing written" .-> M1
  M5 -- "staged into temp/ only" --> T1
  T1 -. "the next Reading starts here,<br/>reading the take first" .-> M1
```

#### B2

```mermaid
flowchart LR
  subgraph SR["System Repo"]
    direction LR
    S1["1. Plan Step works:<br/>a Copy changed,<br/>with its Record"] --> S2["2. Gate decides<br/>each Change"] --> S3["3. Gate closes:<br/>main moves"]
    T1["9. Take, by its<br/>own Adapted Case:<br/>main moves"] --> S4["10. Next Plan<br/>Step opens"]
  end
  subgraph MR["Maintainer Repo"]
    direction LR
    M1["4. Read:<br/>read to → main"] --> M2["5. List"] --> M3["6. Judge"] --> M4["7. Act:<br/>stop becomes read to"] --> M5["8. Deliver"]
  end
  S3 -. "read only" .-> M1
  M5 -- "into temp/ only" --> T1
  T1 -. "next Reading starts here,<br/>take read first" .-> M1
```

### Option b, the next Plan Step's first commit

The take is the first commit of the next Plan Step, on its branch. Main moves only at a gate's close, so the take reaches main with that step's work. Its gate, and the next Reading, compare from the take's commit, not from where the step began or from *read to*.

#### B1

```mermaid
flowchart TB
  subgraph SR["System Repo"]
    T1["9. Next Plan Step opens;<br/>its first commit is the take:<br/>main still the stop?<br/>Copies whole, Changes put back.<br/>Main does not move"]
    S1["1. Plan Step works:<br/>a Copy changed, with its Record"]
    S2["2. Gate decides each Change,<br/>compared from the take's commit"]
    S3["3. Gate closes:<br/>main moves, the take with it"]
    T1 --> S1 --> S2 --> S3
  end
  subgraph MR["Maintainer Repo"]
    M1["4. Read: from the take's commit,<br/>to main, the stop"]
    M2["5. List, nothing judged"]
    M3["6. Judge: a verdict per line"]
    M4["7. Act: System Kit changed;<br/>the stop becomes read to"]
    M5["8. Deliver: the Update made"]
    M1 --> M2 --> M3 --> M4 --> M5
  end
  S3 -. "read only, nothing written" .-> M1
  M5 -- "staged into temp/ only" --> T1
```

#### B2

```mermaid
flowchart LR
  subgraph SR["System Repo"]
    direction LR
    T1["9. Next Plan Step<br/>opens with the take"] --> S1["1. Plan Step works"] --> S2["2. Gate decides,<br/>from the take's commit"] --> S3["3. Gate closes:<br/>main moves"]
  end
  subgraph MR["Maintainer Repo"]
    direction LR
    M1["4. Read: from<br/>the take's commit"] --> M2["5. List"] --> M3["6. Judge"] --> M4["7. Act:<br/>stop becomes read to"] --> M5["8. Deliver"]
  end
  S3 -. "read only" .-> M1
  M5 -- "into temp/ only" --> T1
```

### Option c, a Plan Step of its own

The take is a Plan Step, "Take the Update", with a full gate. Main moves only at a gate's close. Its gate compares from the take's commit, or it would count the whole Update as Changes. Whether the next Reading reads that Plan Step as work, or starts after it, stays open.

#### B1

```mermaid
flowchart TB
  subgraph SR["System Repo"]
    S1["1. Plan Step works:<br/>a Copy changed, with its Record"]
    S2["2. Gate decides each Change"]
    S3["3. Gate closes:<br/>main moves"]
    T1["9. Plan Step 'Take the Update':<br/>main still the stop?<br/>Copies whole, Changes put back"]
    T2["9b. Its gate, compared<br/>from the take's commit:<br/>main moves"]
    S4["10. Next Plan Step opens"]
    S1 --> S2 --> S3
    T1 --> T2 --> S4
    S4 -- "next round" --> S1
  end
  subgraph MR["Maintainer Repo"]
    M1["4. Read: from read to,<br/>to main, the stop"]
    M2["5. List, nothing judged"]
    M3["6. Judge: a verdict per line"]
    M4["7. Act: System Kit changed;<br/>the stop becomes read to"]
    M5["8. Deliver: the Update made"]
    M1 --> M2 --> M3 --> M4 --> M5
  end
  S3 -. "read only, nothing written" .-> M1
  M5 -- "staged into temp/ only" --> T1
  T2 -. "open: the next Reading reads<br/>this step, or starts after it?" .-> M1
```

#### B2

```mermaid
flowchart LR
  subgraph SR["System Repo"]
    direction LR
    S1["1. Plan Step works:<br/>a Copy changed,<br/>with its Record"] --> S2["2. Gate decides<br/>each Change"] --> S3["3. Gate closes:<br/>main moves"]
    T1["9. Plan Step<br/>'Take the Update'"] --> T2["9b. Its gate:<br/>main moves"] --> S4["10. Next Plan<br/>Step opens"]
  end
  subgraph MR["Maintainer Repo"]
    direction LR
    M1["4. Read:<br/>read to → main"] --> M2["5. List"] --> M3["6. Judge"] --> M4["7. Act:<br/>stop becomes read to"] --> M5["8. Deliver"]
  end
  S3 -. "read only" .-> M1
  M5 -- "into temp/ only" --> T1
  T2 -. "open: read this step,<br/>or start after it?" .-> M1
```
