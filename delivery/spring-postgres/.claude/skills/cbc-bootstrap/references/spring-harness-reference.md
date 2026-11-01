# Spring harness reference — the recurring files, as code

The Adversity Harness's five recurring files for the CBC Bootstrap's
end on the Spring line: the two test bases, the Migration Path Test,
and the CBC Bootstrap Probe's two files. **Scoped to one stack, by
name:** Spring Boot on Maven, the Boot 4 line, Testcontainers 2.x,
PostgreSQL. Three CBC Runs built them. The shape below is the latest
CBC Run's, the most corrected.

**It owns nothing.** Three other files do:
- the *outcomes* these files satisfy are
  `.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`'s,
  steps 4 and 5;
- what enters the build, and how each entry is written, is
  `.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`'s;
- the machine setup that makes containers reachable is the project's
  Operator Manual's.

**The CBC Run's CBC Bootstrap Requirements win over all of them.**
Where they forbid something this file shows, the file is wrong for
that CBC Run.

**Why code exists here at all.** This file carries code so that no
CBC Run has to read the last CBC Run's source. The walkthrough
deliberately carries none: two CBC Runs may end with different code
for the same thing. That holds for the application. It does not hold
for these five, which are shaped by the stack and the Adversity
Harness's outcomes, not by the problem. Three CBC Runs produced them
almost identically, and each one's only route was reading the
earlier CBC Run's source. **It is a reference, not an Agent Skill
Template:** imitated, never pasted and filled. Copied without
thought, it will be wrong in the variation points named at the
end.

Placeholders: `<base-package>`, `<project>` (underscored in SQL
identifiers), `<project_db>`, `<project_schema>`, and the Runtime
Ground's major version.

---

## What these files are, in one line each

| File | Scope | The outcome it realizes |
|---|---|---|
| `DatabaseIT` | test | one container per test JVM, a copy of the Runtime Ground set up by the same SQL; migrations on the Adversity Harness's side as `migrator`; the context connects as `runtime` |
| `WebDatabaseIT` | test | the web and database base: an HTTP server on a random port over the same database |
| `MigrationPathIT` | test | the Migration Path Test: the migration path proven, not assumed; the connection identity asserted; the Database Role Split shown by a refused DDL |
| `GroundProbeController` | **main** | the CBC Bootstrap Probe's endpoint: one identity round-trip through the real door; scaffolding, deleted at the first Invariant Slice |
| `ContentionProbeIT` | test | the CBC Bootstrap Probe's test: many requests released at one instant, all asserted |

## 1. The database base

**Outcomes it realizes** (walkthrough, step 4):
1. one PostgreSQL container of the Runtime Ground's major version
   per test JVM, started once and shared. Its lifecycle is explicitly
   the Adversity Harness's own;
2. migration run **on the Adversity Harness's side, right after the
   container starts and before any application context boots.** It
   points at the **one migrations directory on the filesystem,**
   never a classpath copy;
3. the latest CBC Run's correction: **the Database Role Split holds
   in evidence runs.** The container is set up by the SAME
   `bootstrap.sql` the Runtime Ground uses. Migration runs as the
   `migrator` role, and the application context connects as
   `runtime` alone.

```java
package <base-package>.testsupport;

import org.flywaydb.core.Flyway;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.postgresql.PostgreSQLContainer;
import org.testcontainers.utility.DockerImageName;
import org.testcontainers.utility.MountableFile;

/**
 * Database-only test base: one real PostgreSQL container per test JVM,
 * started once and shared. The lifecycle is the Adversity Harness's
 * own, deliberately outside any framework-managed teardown.
 *
 * The container is a copy of the Runtime Ground, set up by the same
 * SQL: the same image major as the established Runtime Ground, set up
 * by the SAME bootstrap.sql (one source: infrastructure/postgres/init/).
 * So the Database Role Split and its grants hold in evidence runs
 * exactly as they do on the Runtime Ground. Migrations run on the
 * Adversity Harness's side, right after the container starts and before
 * any application context boots, as the migrator role, from the one
 * migrations directory on the filesystem, never a classpath copy. The
 * application context then connects as the runtime role alone, with
 * the authority it has in production.
 */
@SpringBootTest
public abstract class DatabaseIT {

    private static final String GROUND_BOOTSTRAP_SQL =
            "infrastructure/postgres/init/bootstrap.sql";
    private static final String MIGRATIONS_HOME =
            "filesystem:infrastructure/flyway/migrations";

    private static final PostgreSQLContainer POSTGRES =
            new PostgreSQLContainer(DockerImageName.parse("postgres:17"))
                    .withDatabaseName("<project_db>")
                    .withUsername("postgres")
                    .withPassword("postgres_localdev")
                    .withCopyFileToContainer(
                            MountableFile.forHostPath(GROUND_BOOTSTRAP_SQL),
                            "/docker-entrypoint-initdb.d/bootstrap.sql");

    static {
        POSTGRES.start();
        Flyway.configure()
                .dataSource(POSTGRES.getJdbcUrl(),
                        "<project>_migrator", "<project>_migrator_localdev")
                .schemas("<project_schema>")
                .locations(MIGRATIONS_HOME)
                .load()
                .migrate();
    }

    @DynamicPropertySource
    static void datasourceAsRuntimeIdentity(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", POSTGRES::getJdbcUrl);
        registry.add("spring.datasource.username", () -> "<project>_runtime");
        registry.add("spring.datasource.password", () -> "<project>_runtime_localdev");
    }
}
```

**Bound facts.**

- The **static initializer** is what "the lifecycle is the
  Adversity Harness's own" means concretely: no per-class container
  annotation, no JUnit-managed restart. It runs once per test JVM,
  and the migration runs inside it. So the order the outcome demands,
  migrate *then* boot, is held by structure, not by a convention
  someone must remember.
- **The mounted `bootstrap.sql` is the one source.** The Adversity
  Harness copies the Runtime Ground's own `bootstrap.sql` into
  `docker-entrypoint-initdb.d`, so the copy cannot drift from the
  Runtime Ground's roles. The localdev literals here are the same
  coupling Infrastructure Establishment's `.env.example` documents.
- **The Database Role Split is live in tests:** migrate as
  `<project>_migrator`, connect as `<project>_runtime`. An Adversity
  Harness run as the container's superuser, an earlier CBC Run's
  shape, proves the round-trip but not the authority. DDL attempted
  from application code would succeed in tests and fail on the
  Runtime Ground.
- **Testcontainers 2.x names** are the walkthrough's trap
  (`.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, step 4,
  *The Adversity Harness in the codebase*, *Traps, exact*, item 3).
- The migrate call does here what the `flyway` service in
  `compose.yaml` does on the Runtime Ground, against the throwaway database. Flyway is a **tool of the Adversity Harness, in
  test scope.** At runtime scope it would undo the datasource's claim
  that the application cannot migrate. Which Flyway artifacts it
  needs is the walkthrough's trap
  (`.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, step 4,
  *The Adversity Harness in the codebase*, *Traps, exact*, item 4).
- **The Adversity Harness's Flyway is the build's,** managed by Boot,
  and may be a different major than the Runtime Ground's one-shot
  image. The latest CBC Run ran 12 against the Runtime Ground's 11.
  They never meet: separate databases, separate history tables.
  Noted, accepted.
- **On Boot 4 the engine enters alone, and that is load-bearing.**
  Boot 4 moved Flyway's auto-configuration into its own module. With
  only `flyway-core` and `flyway-database-postgresql` on the test
  classpath, no auto-configuration runs inside the application
  context. So the `static` call above is the only migration path in
  tests. Nothing can migrate from inside a context, at any scope.
  Entering Boot's Flyway module instead would add a second migration
  path.
- **The filesystem location is deliberate:** `filesystem:` and the
  project's one migrations directory, so nothing can drift from a
  classpath copy.

## 2. The web and database base

**Outcome** (step 4): a small, **layered** test-support base, so a
test declares what it needs and inherits the rest. `DatabaseIT` is
above, and `WebDatabaseIT` is over it.

```java
package <base-package>.testsupport;

import org.springframework.boot.resttestclient.autoconfigure.AutoConfigureTestRestTemplate;
import org.springframework.boot.test.context.SpringBootTest;

/**
 * Web and database test base: the full application on a random real
 * port, over the shared PostgreSQL container of this JVM. Evidence that
 * must go through the real door (HTTP → application → store) extends
 * this. The door's client, TestRestTemplate, needs the explicit
 * auto-configure annotation on Boot 4: RANDOM_PORT alone no longer
 * provides the bean.
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureTestRestTemplate
public abstract class WebDatabaseIT extends DatabaseIT {
}
```

**Bound facts.**

1. The Boot 4 test-client traps, `spring-boot-restclient` at test
   scope and `@AutoConfigureTestRestTemplate`, are the walkthrough's
   (`.claude/skills/cbc-bootstrap/references/spring-boot-walkthrough.md`, step 4,
   *The Adversity Harness in the codebase*, *Traps, exact*, items 1 and 2).
2. The bases stay lean: no shared protected fields. A test autowires
   what it uses (`JdbcClient`, `TestRestTemplate`). So attacking
   through the door, and inspecting persisted state directly, are
   both one line away. The bases grow only what every extending test
   needs. The latest CBC Run added a clock configuration here at a
   later Invariant Slice: growth during Invariant Slice work, not the
   CBC Bootstrap's shape.

## 3. The Migration Path Test

**Outcome** (step 4): the migration path **proven, not assumed.**
With it, two more checks:
- the connection identity is asserted;
- the Database Role Split is shown: the `runtime` role cannot change
  structure in the copy, refused with the Runtime Ground's own
  message.

```java
package <base-package>.store;

import <base-package>.testsupport.DatabaseIT;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.simple.JdbcClient;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

/**
 * Proves the migration path rather than assuming it. Even a run with
 * no migrations creates the history table, so its existence shows the
 * migrator's path on the Adversity Harness's side works end to end. A
 * count of zero is the true state of a Runtime Ground whose migrations
 * are added only when needed. The first real migration turns the count
 * positive, without changing what this proves.
 */
class MigrationPathIT extends DatabaseIT {

    @Autowired
    private JdbcClient jdbc;

    @Test
    void applicationConnectsAsTheRuntimeIdentity() {
        String identity = jdbc.sql("SELECT current_user")
                .query(String.class).single();
        assertThat(identity).isEqualTo("<project>_runtime");
    }

    @Test
    void migrationHistoryExistsWithZeroApplied() {
        Boolean historyTableExists = jdbc.sql("""
                SELECT EXISTS (
                  SELECT 1 FROM information_schema.tables
                  WHERE table_schema = '<project_schema>'
                    AND table_name = 'flyway_schema_history')
                """).query(Boolean.class).single();
        assertThat(historyTableExists).isTrue();

        Integer applied = jdbc.sql(
                        "SELECT count(*) FROM <project_schema>.flyway_schema_history")
                .query(Integer.class).single();
        assertThat(applied).isZero();
    }

    @Test
    void theRuntimeIdentityCannotChangeStructure() {
        // the Runtime Ground's first refusal, held in the copy; the store's
        // message sits at the root of Spring's translated exception
        assertThatThrownBy(() ->
                jdbc.sql("CREATE TABLE <project_schema>.t (i int)").update())
                .rootCause()
                .hasMessageContaining("permission denied for schema <project_schema>");
    }
}
```

**Bound facts.**

- **Zero is the true state at the CBC Bootstrap.** The history table
  is created even by a run with no migrations. So its existence proves
  the path, and zero proves the migrations directory is empty. When
  the first Invariant Slice needs V1, the latest CBC Run changed this
  to "count ≥ 1 and none failed": the count changed, the proof did
  not.
- **The identity assertion is the Database Role Split's cheapest
  check.** `current_user`, seen by SQL from the application context,
  must be the `runtime` role. It costs three lines. It catches an
  Adversity Harness quietly wired as the wrong identity, the exact
  failure the copy exists to prevent.
- **The refused DDL shows the authority, not only the identity.** One
  CBC Run met this: a copy wired as the right name but without the
  Database Role Split, the grants missing and `bootstrap.sql` not
  mounted, passes the identity assertion and fails here, with the
  Runtime Ground's own message. Its trap is in the shape. Spring
  translates the driver's error and wraps it, so the message sits on
  the **root cause,** not the thrown exception. Assert there, or the
  test is red for the wrong reason.

## 4. The CBC Bootstrap Probe

**Outcomes** (step 5):
1. **the endpoint,** in the main source, doing a real round-trip as
   the `runtime` role. It is documented as scaffolding, deleted when
   the first real Invariant Slice lands;
2. **the test:** many requests held at a barrier and released at one
   instant. Each is a full HTTP → application → real-PostgreSQL
   round-trip through the same door a real caller uses, and every
   response is asserted.

```java
package <base-package>.probe;

import java.util.Map;

import org.springframework.jdbc.core.simple.JdbcClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * SCAFFOLDING — deleted when the first real Invariant Slice lands.
 *
 * One real round-trip to the database as the runtime role, so the CBC
 * Bootstrap's Adversity Harness has a full HTTP → application → store
 * path to attack. It carries no business meaning, and must never grow
 * any: the first Invariant Slice replaces it with its own door.
 */
@RestController
class GroundProbeController {

    private final JdbcClient jdbc;

    GroundProbeController(JdbcClient jdbc) {
        this.jdbc = jdbc;
    }

    @GetMapping("/probe/ground")
    Map<String, String> groundRoundTrip() {
        String identity = jdbc.sql("SELECT current_user")
                .query(String.class).single();
        return Map.of("identity", identity);
    }
}
```

```java
package <base-package>.adversity;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import <base-package>.testsupport.WebDatabaseIT;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.resttestclient.TestRestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * Proves the Adversity Harness can CREATE contention, the Adversity
 * Class the first Invariant Slice needs, end to end through the real
 * door: many requests held at a barrier, released at one instant, each
 * a full HTTP → application → real-PostgreSQL round-trip, every
 * response asserted.
 * The release-at-one-instant pattern is the shape later race evidence
 * takes; here it is aimed at nothing yet.
 */
class ContentionProbeIT extends WebDatabaseIT {

    private static final int CONCURRENT_REQUESTS = 100;

    @Autowired
    private TestRestTemplate http;

    @Test
    void oneHundredSimultaneousRoundTripsAllSucceed() throws Exception {
        ExecutorService pool = Executors.newFixedThreadPool(CONCURRENT_REQUESTS);
        CountDownLatch ready = new CountDownLatch(CONCURRENT_REQUESTS);
        CountDownLatch release = new CountDownLatch(1);
        try {
            List<Future<ResponseEntity<String>>> responses = new ArrayList<>();
            for (int i = 0; i < CONCURRENT_REQUESTS; i++) {
                responses.add(pool.submit(() -> {
                    ready.countDown();
                    release.await();
                    return http.getForEntity("/probe/ground", String.class);
                }));
            }
            ready.await();
            release.countDown();     // the one instant

            for (Future<ResponseEntity<String>> response : responses) {
                ResponseEntity<String> entity = response.get();
                assertThat(entity.getStatusCode()).isEqualTo(HttpStatus.OK);
                // a substring is enough here: the body IS the identity
                // string, not a shape. A real body is asserted by path
                // (spring-harness-reference.md, variation point 9), never by substring.
                assertThat(entity.getBody()).contains("<project>_runtime");
            }
        } finally {
            pool.shutdownNow();
        }
    }
}
```

**Bound facts.**

- **The two latches are the pattern**, not decoration: one counts
  every worker to the line, one releases them together. Submitting a
  hundred tasks without the barrier tests the thread pool's ramp-up,
  not simultaneity.
- **The CBC Bootstrap Probe round-trips the identity,** not
  `select 1`. Every asserted response then shows both the door and
  the authority: a hundred simultaneous confirmations that the
  application speaks as `runtime`.
- **The pool is sized to the request count,** so every worker can
  block at the barrier at once. That is the requirement here. A fixed
  pool of that size (the latest CBC Run) and virtual threads (an
  earlier one) both satisfy it. Any pool smaller than the count weakens
  the burst.
- **Both files are scaffolding, and both are deleted together** at the first
  Invariant Slice. The endpoint must never grow business meaning: the
  real surface is created from its invariant, not extended out of the
  CBC Bootstrap Probe. Say this in the code, not only in an ADR: the
  javadoc is what the person deleting it will read.
- **What this proves, and what it does not.** It proves the
  Adversity Harness can *drive* simultaneity end to end. It does
  **not** assert that the requests overlapped in the database, and
  would pass on serialized execution. That is correct for a proof of
  the machinery, and must be stated. The first real Invariant Slice's
  evidence has to assert the State Witness, persisted state
  showing the violation, not a count of successful responses.

## 5. What is not in this file

- **The application's own code.** It is the CBC Run's, always. Only
  the CBC Bootstrap Probe crosses into `main/`, because the method
  demands it, and the method deletes it.
- **The pom entries.** Which artifacts realize these capabilities,
  when they enter, and how each comment is written is
  `.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`'s. This file names artifacts only where
  a *name* is a trap (`testcontainers-postgresql`,
  `spring-boot-restclient`, `flyway-database-postgresql`).
- **The machine setup.** The container-runtime socket, the properties
  file that binds only from `$HOME`, Ryuk under rootless podman: the
  walkthrough's step 4, and the project's Operator Manual.
- **The test-command wiring.** Widening the build's test includes to
  cover the integration naming is a build decision, stated as an
  outcome in the walkthrough.

## 6. The variation points

1. **The image version follows the Runtime Ground's major
   version.** `postgres:17` here, because the Runtime Grounds CBC Runs
   built were 17. This is the one line that is wrong by default in any
   project whose Runtime Ground differs.
2. **The migrations directory's path** is the project's one
   migrations directory, as its own records name it. The
   `filesystem:` prefix is fixed; the path is not.
3. **How credentials are handled decides the wiring.** The localdev literals
   here are Infrastructure Establishment's coupling (`bootstrap.sql` ↔
   `.env.example`) carried into the Adversity Harness. They keep the
   suite self-contained: no environment set, no Runtime Ground up. A
   CBC Run whose CBC Bootstrap Requirements forbid committed test
   credentials leaves this reference at exactly this point. Derive
   its wiring, and record the deviation. Expect it to come back as a
   change to this file.
4. **A missing migrations directory is caught somewhere,
   deliberately.** Git carries no empty directory. So a fresh clone
   can lack the migrations directory, while Flyway's default skips a
   missing location with a warning. An earlier CBC Run caught it in
   Flyway config (`failOnMissingLocations(true)`). The latest relied on
   the Migration Path Test, plus a tracked directory. Either works.
   Catching it nowhere leaves the suite green on a clone that cannot
   migrate.
5. **How data is accessed** follows the CBC Run's CBC Bootstrap
   Requirements, not this file: `JdbcClient` appears because plain
   SQL access was required.
6. **The request count** can be set; it is not a requirement. A
   hundred is what the CBC Runs used. What matters is that they are
   released together.
7. **Package layout** (`testsupport/`, `probe/`) is the CBC Run's.
   The layering is the outcome; the names are not. The test packages
   by kind are `.claude/skills/cbc-bootstrap/references/app-structure.md`'s.
8. **More than one instance, when the System Definition names
   them.** The shape above creates the race inside one test process.
   If CBC Framing's Runtime Ground says the system runs as more than
   one instance, the proof of the machinery must cross the process
   boundary (walkthrough, step 5). A pass in a single process proves
   a shape nobody runs, and a lock inside the process could make it
   pass. One CBC Run built it, and it is carried here as prose until
   a second CBC Run builds it:
   - **a store holder:** the container and the migration lifted out
     of `DatabaseIT` into a holder of their own, so a test with no
     application context shares the store. The base keeps only the
     datasource override, and the layering is the two bases plus the
     holder;
   - **a process helper:** it starts one instance of the build's own
     output on a free port against the holder's store, waits for its
     door to answer UP with the store's component UP, and stops it on
     close;
   - **the CBC Bootstrap Probe answering its process id** beside the
     identity, so the race asserts the process ids served are exactly
     the instances started;
   - **the race test running no Spring context of its own:** the
     requests released at one instant, round-robin across the
     instances, and the State Witness read from the store as the
     `runtime` role while the instances are still up.

   The burst inside one process stays beside it, as the cheap first
   check.
9. **A body is asserted by path, never by substring.** This file
   once left the rule unsaid, so each CBC Run decided by habit.
   One CBC Run met why: a substring cannot tell `3` from `30`, cannot
   say a field exists, and cannot say one is absent. The rule,
   decided before the first Invariant Slice and held after:
   - **by path for a shape:** a small test-support reader parses a
     body once and answers a path, `$.id`, `$.onHandCount`. So a
     field's value, presence and absence are each one assertion;
   - **by type when a shared API contract exists:** a client type
     both sides compile against. None exists in a system built from
     its invariant, so path is the default;
   - **never by substring,** even for a word. An error title is a
     path too.

   The CBC Bootstrap Probe above is the one exception, and its comment
   says why: its body is the identity string itself, not a shape.
