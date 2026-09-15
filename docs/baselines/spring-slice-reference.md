<!-- BASELINE — held for comparison, blind to newborns (CBC ADR-0021).
     Not in the bundle: no run receives it at birth, and cbc-slice
     never names it. Handed to a run as session input only after
     that run's build is on record — the close commit on the
     step's branch, before the fast-forward to main — so the run's
     shapes are derived clean and compared, never copied. The
     verdict per shape is the run's, in its devlog and decisions
     log; each verdict confirmed at the reading here lands below
     as one dated harvest line naming the run that earned it
     (CBC ADR-0007). A lived best, never a master.
     Checked against concept v1 of correctness-by-construction
     (CBC ADR-0003, ADR-0005 — practice-born), on the harness
     reference's model. Provenance — harvested 2026-09-14 from
     never-oversold (run 3 of the pure seed) Step 5, SL-1 "no
     over-admission under contention", read read-only (CBC ADR-0007):
     its slice record, devlog, and delivered files at the step's
     close. Lived once: every section is a variation point until a
     comparison confirms or replaces it. -->

# Spring slice reference — one slice's build, as code

**Handed, never shipped.** This file reaches a run only after its
own build of a slice is committed on its branch, for a comparison
shape by shape: for each, which is stronger against that run's
guarantees and why, or that they are not comparable. It is not
copied into the run's tree. Opened before the plan is signed it
would become the answer instead of one candidate, and the skill's
seam — what before how, walls by comparison never by lookup — would
be lost; that is why no run has it.

What the *build* stage of one slice looked like on the Spring line,
from the one run that lived it. **Stack-scoped by name**: Spring Boot
on Maven, the Boot 4 line, PostgreSQL through `JdbcClient`, JUnit 5,
ArchUnit. **Problem-scoped by accident**: the words `item`,
`reservation`, `reserve`, `adjust` are never-oversold's, from its
registry; yours are your registry's. The shapes are what this file
carries — the vocabulary is not.

**Masters nothing.** The *outcomes* these artifacts satisfy are the
skill's Stage 2 and Stage 3 gates and `cbc-slice-workflow.md`'s;
the harness they run in is `cbc-bootstrap`'s
`spring-harness-reference.md` (the two bases, the store holder, the
forked instances); what enters the build and how each entry is
written is `spring-pom-convention.md`'s. **The slice's own
specification and plan win over all of it** — where the plan chose a
different wall, the code here is wrong for that slice.

**Why this file exists.** The skill says *zero mechanisms* at Stage 1
and then leaves Stage 3 to implementation judgment, which is right —
and a run on this stack still re-derived six shapes from nothing, one
of them through a dead end. Each shape below states the outcome it
realizes, so a reader can reject the artifact and keep the outcome.
**It is a reference, not a template** (CBC ADR-0008): imitated,
never pasted — copied thoughtlessly it will be wrong in the
variation points at the end. A run on another stack derives its
own shapes; read at its close, they become a sibling baseline
here. The skill is never touched for either.

---

## What these shapes are, in one line each

| Shape | Where | The outcome it realizes |
|---|---|---|
| the naive-then-wall split | commits | the evidence seen red with the wall absent, before the wall stands (Stage 3's gate; R5 at the first slice) |
| the witness | test support | the invariant read from the store, from outside every instance, in every readable state |
| the admit as one statement | main | the check and the write are one act; the store's row count is the decision |
| value types at the door | main | nonsense never reaches the decision; the store's constraints as the backstop |
| bodies by path | test support | a field asserted at its path, never by substring |
| absence as bytecode rules | test | a guarantee held by what the code does *not* contain, shown to fire on a plant |

## 1 · The naive-then-wall split, and the red run

**Outcome** (skill, Stage 3): every evidence test was seen red with
its wall absent, recorded from actual output, then green unchanged
once the wall stood. At the first slice this is also R5's answer.

The lived sequence, four commits of the slice's change-plan:

1. **The migration** — the tables, *with* the constraint that is the
   wall. The migration-path test reads the constraint back from the
   catalog (`MigrationPathIT.theWallIsInTheCatalog`): if it is ever
   dropped, this goes red before any storm could pass around it.
2. **The doors, with the admit written the naive way** — read the
   row, check in code, plain update. Fifteen door tests green; the
   storms not yet written.
3. **The red run, never committed.** The storm tests written; on the
   working tree only, the constraint removed from the migration and
   the admit still naive; the storms run:
   `[active sum ≤ on-hand-count] Expecting 22 to be less than or
   equal to 20` in one instance, 23 of 20 across three. The output
   into the devlog; the migration restored from the index;
   `git status` showing only the new test files.
4. **The wall** — the admit as one conditional statement (§3); the
   tests untouched; the same storms green.

**Bound facts.**

- **Red without the constraint AND without the conditional
  statement.** Removing only the code wall leaves the constraint,
  and the storm turns into constraint errors, not an oversell — the
  witness stays true and the red proves the wrong thing. Both walls
  absent is what shows the test is watching the invariant.
- **The red is recorded, not remembered**: the assertion message with
  its numbers, in the devlog, before the wall's commit.
- **The naive commit is honest history**, not a trick: it is the
  door working, which the door tests prove. The wall is then its own
  diff, readable as exactly the thing that turned the storm green.

## 2 · The witness — the invariant read from the store

**Outcome** (workflow, Stage 3): the evidence reads persisted state
showing the invariant, from outside every instance, never computed
from replies; and "in every readable state" is sampled while the
storm runs, not only read after.

```java
package <base-package>.testsupport;

/**
 * The witness: for one item, the on-hand-count, the units held, and
 * the sum of active reservations as the store judges them by its own
 * clock. Reads the invariant; never computes it from replies.
 *
 * Plain JDBC on purpose: no application context, no pool the
 * application shares, so a forked-instance test and an in-process
 * test read the same way.
 */
public final class Witness {

    public record Numbers(int onHandCount, int held, int activeSum, int reservations) {
        public boolean holds() {
            return activeSum <= onHandCount && held <= onHandCount && activeSum <= held;
        }
    }

    public static Numbers read(String item) {
        try (Connection store = connect();
             PreparedStatement statement = store.prepareStatement("""
                     SELECT i.on_hand_count,
                            i.reserved,
                            coalesce((SELECT sum(r.quantity) FROM reservation r
                                      WHERE r.item_id = i.id AND r.expires_at > now()), 0) AS active_sum,
                            (SELECT count(*) FROM reservation r WHERE r.item_id = i.id) AS reservations
                     FROM item i WHERE i.id = ?
                     """)) {
            statement.setString(1, item);
            try (ResultSet row = statement.executeQuery()) {
                if (!row.next()) throw new IllegalStateException("no item " + item);
                return new Numbers(row.getInt(1), row.getInt(2), row.getInt(3), row.getInt(4));
            }
        } catch (SQLException e) {
            throw new IllegalStateException("the witness could not be read", e);
        }
    }

    /** Reads again and again on its own thread until stop is set — every readable state. */
    public static Thread sampleUntil(String item, AtomicBoolean stop, List<Numbers> samples) {
        Thread sampler = new Thread(() -> { while (!stop.get()) samples.add(read(item)); }, "witness-" + item);
        sampler.setDaemon(true);
        sampler.start();
        return sampler;
    }

    public static List<Numbers> violations(List<Numbers> samples) { /* every sample where !holds() */ }

    private static Connection connect() throws SQLException {
        return DriverManager.getConnection(
                ThrowawayStore.jdbcUrl(), ThrowawayStore.RUNTIME_IDENTITY, ThrowawayStore.RUNTIME_PASSWORD);
    }
}
```

**Bound facts.**

- **The witness is the invariant's own sentence in SQL.** `activeSum`
  is its left side, `onHandCount` its right; `held` is the counter
  the entry path keeps, asserted between them so the counter's drift
  (an escape hatch the plan hunted) is seen by every read.
- **It connects as the runtime identity**, the ground's authority
  split held in evidence — what runtime can read is what the
  witness may read.
- **The sampler is a thread, not a schedule**: it reads as fast as
  the store answers, for the storm's whole duration, and the test
  asserts the sample list is non-empty before asserting it is clean
  — an empty list would be a vacuous pass.
- **Plain JDBC, deliberately**, so the same class serves the
  in-process storm and the forked-instance storm: no Spring context
  is needed to read the store.

## 3 · The admit as one statement

**Outcome** (plan, G1): the finding and the recording are one act
against the store's state as it is then, never two acts against a
copy; the store's answer is the decision. Behind it the constraint,
so an over-held row is unwritable by any path.

```java
@Component
class Ledger {                                       // package-private: the one entry path

    Reservation reserve(ItemId item, Quantity quantity, Hold hold) {
        return transaction.execute(status -> {
            int admitted = jdbc.sql("""
                    UPDATE item
                       SET reserved = reserved + :units
                     WHERE id = :id
                       AND reserved + :units <= on_hand_count
                    """)
                    .param("units", quantity.units()).param("id", item.value())
                    .update();                       // one row changed, or none: the decision
            if (admitted == 0) {
                Item current = jdbc.sql("SELECT id, on_hand_count, reserved FROM item WHERE id = :id")
                        .param("id", item.value()).query(Item.class).optional()
                        .orElseThrow(() -> new UnknownItem(item.value()));
                throw new Refused(quantity.units() + " units of " + item.value() + " do not fit: "
                        + current.reserved() + " held of " + current.onHandCount() + " on hand");
            }
            return jdbc.sql("""
                    INSERT INTO reservation (item_id, quantity, expires_at)
                    VALUES (:id, :units, now() + make_interval(secs => :seconds))
                    RETURNING id, item_id AS item, quantity, expires_at
                    """)
                    .param("id", item.value()).param("units", quantity.units()).param("seconds", hold.seconds())
                    .query(Reservation.class).single();
        });
    }

    Item adjust(ItemId item, OnHandCount count) {     // the other writer to the same row
        return transaction.execute(status -> jdbc.sql("""
                        INSERT INTO item (id, on_hand_count)
                        VALUES (:id, :count)
                        ON CONFLICT (id) DO UPDATE SET on_hand_count = EXCLUDED.on_hand_count
                            WHERE item.reserved <= EXCLUDED.on_hand_count
                        RETURNING id, on_hand_count, reserved
                        """)
                .param("id", item.value()).param("count", count.units())
                .query(Item.class).optional()
                .orElseThrow(() -> new Refused("...: more units than that are held by reservations")));
    }
}
```

**Bound facts.**

- **The row count is the decision.** Two racers update one row; the
  store serializes writers to a row under the default isolation, and
  the second re-evaluates the `WHERE` against the first's result. No
  lock is taken by the code, no retry loop exists, and nothing was
  read before the decision.
- **The read after `admitted == 0` decides nothing** — it only tells
  unknown from refused for the reply. The admission was decided by
  the update's answer.
- **The reservation's insert is in the same transaction**, and the
  reply is produced from the committed outcome — the decision *is*
  the commit (G4): death before commit rolls the whole back, and no
  interval exists between deciding and recording to kill.
- **The store's clock, not the JVM's**: `now()` inside the insert,
  the hold carried as seconds; the application never supplies a
  timestamp (§6 makes that structural).
- **Two writers to one row, one shape each.** The adjustment is
  `INSERT … ON CONFLICT DO UPDATE … WHERE`, refused by the same
  constraint whichever order the racers land in (G3). Its refusal is
  the constraint's own answer, no code of the run's.
- **`JdbcClient` and `TransactionTemplate`, no ORM, no repository
  interface**: one store, one writer, the statement visible as one
  SQL sentence. Depth is earned per feature, never stamped.

## 4 · Value types at the door

**Outcome** (plan, G6): only a request naming a known item and a
positive whole quantity within a stated bound reaches the decision;
anything else is answered invalid before any statement runs, and the
numbers do not move. The type system is the wall; the store's
`quantity > 0` and `>= 0` constraints are the backstop for a bypassed
door.

```java
public record Quantity(int units) {

    public static final int BOUND = 1_000_000;

    public Quantity {                                // a value that cannot exist cannot reach the admit
        if (units < 1 || units > BOUND) {
            throw new InvalidRequest("quantity must be a whole number from 1 to " + BOUND);
        }
    }

    public static Quantity of(Integer units) {       // the wire's null, named
        if (units == null) throw new InvalidRequest("quantity is required");
        return new Quantity(units);
    }
}
```

The controller parses each body into these before calling the entry
path — `ledger.reserve(new ItemId(item), Quantity.of(request.quantity()), new Hold(request.hold()))`
— and a `@RestControllerAdvice` maps the three answers besides
success to Problem Details (RFC 9457) with the title in the
definition's words: invalid `400`, unknown `404`, refused `409`. The
unreadable-body case (`HttpMessageNotReadableException`) is mapped
too, so a body that is not the request it should be is `400` with the
same title, not the framework's default.

**Bound facts.**

- **A refusal is not an invalid request**, and the statuses say
  which: the evidence must count refusals to show a storm was real,
  and a client retrying a refusal is doing something different from
  a client fixing a bad request.
- **The compact constructor is the wall**, not a validator called
  somewhere: no path constructs a `Quantity` that is nonsense.
- **Values and answers public in sub-packages; behaviour and writes
  package-private at the feature's root** — a value or an exception
  makes no promise a future feature could abuse; the ledger does. The
  sub-packages must not depend on each other in a cycle.

## 5 · Bodies asserted by path

**Outcome** (harness reference, variation point 9): a field is
asserted at its path, never by substring. The one shape:

```java
public final class Body {
    private final DocumentContext json;
    public static Body of(String raw) { return new Body(JsonPath.parse(raw)); }
    public <T> T at(String path, Class<T> type) { return json.read(path, type); }
    public int intAt(String path) { return at(path, Integer.class); }
    public String stringAt(String path) { return at(path, String.class); }
    public UUID uuidAt(String path) { return UUID.fromString(stringAt(path)); }
    public boolean has(String path) {
        try { return json.read(path) != null; } catch (PathNotFoundException absent) { return false; }
    }
}
```

`json-path` already rides in through the Boot test starter; it is
declared at test scope with its reason so the use is visible and
survives a starter change (pom convention). The storms take the
reservation's id from `$.id`; the door test asserts a field's value,
presence, and absence each as one line.

## 6 · Absence as bytecode rules

**Outcome** (plan, G2 and G5): a guarantee held by what the
application does *not* contain — no process clock consulted, no item
state kept in memory — has no runtime evidence, because an absence
cannot be seen by running anything. Its wall is a rule checked
against the compiled classes on every build, each rule with a
`because` naming its guarantee, each shown to fire on a plant.

```java
class NoInstanceStateOrClockTest {

    private static final JavaClasses APP = new ClassFileImporter()
            .withImportOption(new ImportOption.DoNotIncludeTests())   // never the tests, which may do all of this
            .importPackages("<base-package>");

    @Test
    void theLedgerConsultsNoProcessClock() {
        // accesses, not only calls: a method reference such as Instant::now is an access too
        noClasses().should().accessTargetWhere(target(name("now")).and(target(owner(resideInAPackage("java.time..")))))
                .because("expiry is set and judged by the store's clock, never an instance's (G5)")
                .check(APP);
        noClasses().should().dependOnClassesThat().belongToAnyOf(Clock.class, Date.class)
                .because("a Clock, or a Date, is a process clock by another name (G5)")
                .check(APP);
        noClasses().should().accessTargetWhere(
                        target(name("currentTimeMillis").or(name("nanoTime"))).and(target(owner(type(System.class)))))
                .because("the JVM's time is an instance's own (G5)")
                .check(APP);
    }

    @Test
    void theLedgerKeepsNoStateOutsideTheStore() {
        noFields().should().haveRawType(assignableTo(Map.class)
                        .or(assignableTo(Collection.class))
                        .or(resideInAPackage("java.util.concurrent.atomic")))
                .because("the row is the only state; nothing kept in memory can take part in an admit (G2)")
                .check(APP);
        fields().that().areStatic().should().beFinal()
                .because("a mutable static is shared state an instance holds outside the store (G2)")
                .check(APP);
    }
}
```

**Bound facts.**

- **`accessTargetWhere`, not `callMethodWhere`.** The first draft used
  calls only, and a planted `Instant::now` method reference walked
  through. An access is a call or a reference; the rule must see
  both.
- **Each rule is shown to fire, one plant at a time**: an
  `Instant::now` reference, a `System.nanoTime()` call, a
  `static int`, a `HashMap` field — each caught by its own rule,
  each removed before the commit. A rule never seen red is not known
  to be watching (Stage 3's gate, for structure).
- **DEAD END, lived:** the first version was a regex over the source
  text under `src/main`. It caught a planted `Instant.now()` and
  missed a planted `HashMap` field; re-anchored, it caught both and
  did not look like something developers write. It was not: a text
  rule misses a static import, a method reference, and any
  reformat. Bytecode rules replaced it before anything landed.
- **Only the application's classes are imported.** The tests may
  hold maps, sleep, and read clocks — they are the adversary.
- **A later exception is a narrower rule with its why**, written in
  this file, never a deleted rule.

## 7 · What is not in this file, and why

- **The specification and the plan** — the slice record's, in prose,
  the run's own. This file starts where the plan's owners are chosen.
- **The storms themselves** beyond the witness they read — their
  latch shape is the harness reference's contention probe, grown:
  the same two latches, the pool sized to the request count, the
  replies sorted into admitted and refused, every admitted id
  checked against the store. The forked-instance storm is that
  shape round-robin across the instances the harness started.
- **The pom entries.** Which artifacts realize these capabilities
  and how each comment is written is `spring-pom-convention.md`'s.
  Named here only where a *name* is a trap: `archunit-junit5` is not
  parent-managed, so its version is explicit.
- **The registry, the record, the close** — Stage 4's, in the skill.

## 8 · Variation points — read before copying

1. **The wall is the plan's, not this file's.** The conditional
   update with a constraint behind it was the strongest face for
   *this* guarantee against *this* adversity; a row lock, serializable
   isolation with retry, an advisory lock, or a trigger-maintained
   counter were weighed and rejected in the plan with their costs.
   Another slice's comparison may land elsewhere, and then §3 is the
   wrong code.
2. **The counter over-approximates on the safe side.** `reserved`
   counts an expired hold until an exit ends it — the witness reads
   both the counter and the true active sum and asserts the order
   between them. Whether a later slice moves the counter into a
   trigger is that slice's decision; the plan named it as the first
   option if a second writer to the reservation table ever appears.
3. **The naive commit exists only where the wall is born in this
   slice.** When the wall already stands from an earlier slice, the
   red run is "remove it on the working tree, restore it" — the
   skill's Stage 3 names both.
4. **The witness's query is the invariant's, verbatim.** Another
   invariant has another sentence; what carries over is the shape —
   plain JDBC, the runtime identity, the sampler thread, the
   non-empty check.
5. **The bounds are the door's to state** (`1..1 000 000` units,
   `1 s..7 days` of hold); they are the run's decision at its door's
   conventions, not this file's.
6. **`accessTargetWhere` is ArchUnit 1.5's spelling**; the outcome is
   "calls and references both", whatever the library's next name for
   it.
7. **Sub-packages for vocabulary** were the reader's ask in the
   lived run (a flat feature folder of thirteen files was hard to
   navigate), recorded as a note on the run's structure decision. A
   run whose reader is fine with the flat folder keeps it.
