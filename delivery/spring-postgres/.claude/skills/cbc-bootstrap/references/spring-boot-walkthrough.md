# Spring Boot walkthrough — outcomes and traps met

The stack line:

- **Spring Boot 4.x · Java 21 · Maven;**
- an established PostgreSQL Runtime Ground;
- under the Database Role Split (`<project>_migrator` /
  `<project>_runtime`);
- the migrations directory `infrastructure/flyway/migrations/`,
  empty;
- rootless podman as the container runtime.

Boot 4's renamed modules are load-bearing throughout. On Boot 3 the
names differ.

This doc carries **required outcomes**, what must be true, the how
being yours, and **traps met**, exact facts about this stack and
environment. It carries no code to copy. Its config files, though,
are Agent Skill Templates in `templates/` beside this Agent Skill's
`references/`, and they implement the stack line above. If the CBC
Run's decided stack differs, you are off-template. Derive from the
outcomes here, and record the deviation as delivered-copies rule 8
says (`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill Template is copied and filled, never edited in place*).
**The project's CBC Bootstrap Requirements win over this doc on any
conflict.** The principle in the Runtime Ground and in the Adversity
Harness alike: *something outside the app migrates; the app runs.*

## 1. Record the stack decision

Before any code, an ADR carries:

- the stack;
- the application structure, decided against the Stack Default.
  `.claude/skills/cbc-bootstrap/references/app-structure.md`, beside
  this walkthrough, holds the choice. Departing from its default is a
  logged decision, off-default;
- Flyway staying outside the app: no `migrator` credentials in any
  profile;
- the migrations directory confirmed.

**Trap: the standard recipe reverses the Runtime Ground's
constraint.** The usual Spring path, in-app Flyway with two sets of
credentials and JPA with `ddl-auto: validate`, hands the running app
control over database structure. No JPA, no in-app Flyway, no
`-data-` starters.

## 2. Stand the skeleton in the live repo

- Generate the skeleton with Spring Initializr from the Build
  Coordinates, and **extract it into the existing repo root,** beside
  the infrastructure directories. Never overwrite. Each hygiene file
  takes its Stack Overlay below the marked line it carries:
  - `.gitignore`: the build output, IDE, OS and log sets;
  - `.gitattributes`: the wrapper line endings, the shell wrapper LF
    and the cmd wrapper CRLF;
  - `.editorconfig`.

  `README.md` is kept.
- Capabilities at this step, and no more: an HTTP surface and
  operational health.
- Generated files not needed are removed: help files, empty static
  and template directories. The properties file is replaced by a YAML
  carrying the application name only. The pom's empty metadata blocks
  are deleted, and its description filled from the CBC Framing
  Intent.
- The pom is written by the POM convention,
  `.claude/skills/cbc-bootstrap/references/spring-pom-convention.md`.

**Verified:**
- the context test green, with no database;
- the app starts and announces **Java 21**. If not, align the IDE's
  and the terminal's JDK;
- health UP.

**Traps:**
- Boot 4 renames the web starter to the web-MVC name, and pairs
  runtime starters with `-test` companions. State the pairing rule
  once, as a pom comment. Initializr on Boot 4 already emits both, so
  the trap is met when a pom is written or translated by hand, not
  when it is generated.
- A `4.x.y.RELEASE`-style coordinate does not resolve on this line.
  The version is plain `4.x.y`.

## 3. Wire the runtime datasource

The config skeleton is an Agent Skill Template,
`.claude/skills/cbc-bootstrap/templates/application.yaml`. The
absences below are in it as comments. The CBC Run's business config
grows under its own key, never in the Agent Skill Template.

- Connect **as the `runtime` role only,** with the connection facts
  the CBC Bootstrap Requirements carry. The details are in the
  Operator Manual.
- **Three deliberate absences, each commented in the config with its
  why:**
  1. no schema pinning in the app: the Runtime Ground pins the search
     path on the server;
  2. no `migrator` credentials in any profile;
  3. no test profile: the Adversity Harness overrides the datasource
     itself.
- Access by capability: a plain SQL client (`JdbcClient`), not an
  ORM. The driver is at runtime scope.
- The password comes from the environment. **Environment facts are
  written in no tool's notation, in any doc you write.** Compose's
  `${VAR:-default}` syntax pasted into `application.yaml` does not
  error. It silently resolves to a literal like `-5432`.

**Verified:** with the Runtime Ground up, the app runs, and health is
UP **with the db component UP.** A fact: the test run stays green
with the Runtime Ground down, because the pool connects lazily.
Degradation shows only in health. That is correct, not a gap.

**Trap: a missing secret does not stop the app.** The same fact,
seen the other way, met in a CBC Run:
1. started with nothing exported, the app *starts*;
2. Boot's configuration binding leaves an unresolvable `${VAR}` as
   the literal string, so the literal becomes the password;
3. the store logs `password authentication failed`, and health
   answers DOWN with the db component DOWN. Nothing else says so.

What follows from it:
- the plain context test needs no environment and no test property.
  A property added "so the placeholder resolves" is dead: verify by
  removing it;
- the README's Run section names the symptom.

Whether the app should refuse to start without its secret is a
*what*, not a wiring detail. It is decided at the cbc-bootstrap Agent Skill's Stage 1 by name. One
CBC Run decided it at release, not at the CBC Bootstrap. It is never
absorbed here.

## 4. The Adversity Harness

### The test runtime (once per machine; the Operator Manual's)

Testcontainers needs a reachable container-runtime socket. With
rootless podman: enable the user socket unit, and point the library
at it.

**Traps, exact:**
1. `~/.testcontainers.properties` binds **only from `$HOME`,** never
   from the project root. A CBC Run lost a long search to the "no
   valid Docker environment" error here. Agent Skill Template:
   `.claude/skills/cbc-bootstrap/templates/testcontainers.properties`.
2. Ryuk, the library's reaper:
   - it runs fine under rootless podman on the Testcontainers 2.x
     line. A CBC Run saw it on podman 5.8 and Testcontainers 2.0.5:
     both throwaways reaped within seconds of the JVM's exit. Keep it
     on;
   - older guidance disables it with a `ryuk.disabled=true` line in
     the properties file. 2.x does not read that key, so the line has
     no effect;
   - if Ryuk fails on a host, the switch is
     `TESTCONTAINERS_RYUK_DISABLED=true` in the environment, never a
     properties line. A test JVM killed hard can then leave a
     throwaway running. `podman ps` shows it by image:
     `postgres:<major>` with a random name, and `testcontainers/ryuk`.
     Remove those, and only those, with `podman rm -f <name>`.
3. The socket unit can report *active (listening)* with the socket
   file missing. Active is not enough: stop the socket and service
   user units, start the socket again, and confirm the file exists.
4. This setup belongs in the project's Operator Manual, not the code.

### The Adversity Harness in the codebase

- **Capabilities in test scope only:**
  1. drive a real PostgreSQL container from tests;
  2. integrate with the Spring test context;
  3. run migrations **on the Adversity Harness's side.**

  Flyway is a tool of the Adversity Harness. At runtime scope it
  would undo step 3's claim. On Boot 4 the engine enters, not Boot's
  Flyway module. The engine alone runs no auto-configuration, so the
  Adversity Harness's own call is the only migration path
  (`.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`
  §1, *The database base*).
- **One container per test JVM,** of the Runtime Ground's major
  version, started once and shared. Its lifecycle is explicitly the
  Adversity Harness's own.
- **Migration runs right after the container starts, before any app
  context boots.** It points at **the one migrations directory on the
  filesystem** (`filesystem:infrastructure/flyway/migrations`), never
  a classpath copy.
- **The Database Role Split holds in evidence runs:**
  - the container is initialized by the same
    `infrastructure/bootstrap.sql` the Runtime Ground uses;
  - migration runs as the `migrator` role;
  - the application context connects as the `runtime` role alone.
- **A small layered test-support base:** `DatabaseIT`, for the
  database only, and `WebDatabaseIT`, for the web and the database,
  extending it.
- **Integration tests run under the one standard test command.**
  Widen Surefire's includes to cover `*IT`: no second command, no test
  that quietly never runs.
- **The migration path proven, not assumed:** the Migration Path
  Test asserts the history table exists with **zero applied
  migrations.** The table is created even by a run with no
  migrations. Zero is correct for a Runtime Ground whose migrations
  are added only when needed. The first real migration turns the
  count positive, without changing what the test proves.

The files these outcomes keep producing, the two bases and the
Migration Path Test, are kept as confirmed code in
`.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`,
beside this walkthrough: **imitated, never pasted.** Read its
variation points before writing a line.

**Traps, exact:**
1. `spring-boot-restclient` must be present **at test scope** on
   Boot 4, or the web test context fails with
   `NoClassDefFoundError: RestTemplateBuilder`. The failure names
   something else.
2. Boot 4 moved the test REST client:
   - it is now in `org.springframework.boot.resttestclient.*`;
   - `RANDOM_PORT` alone **no longer provides the `TestRestTemplate`
     bean.** The test, or its base, needs
     `@AutoConfigureTestRestTemplate` from
     `org.springframework.boot.resttestclient.autoconfigure`, or the
     autowire fails with "No qualifying bean". A CBC Run met it on
     Boot 4.1.1.
3. Testcontainers 2.x renamed artifacts and packages:
   `testcontainers-postgresql`, `org.testcontainers.postgresql`. The
   1.x names fail as a missing class, not a helpful message.
4. `flyway-core` alone is not enough on Flyway ≥ 10:
   `flyway-database-postgresql` is required for PostgreSQL.
5. **No dummy baseline migration.** Keep the migrations directory
   empty until a migration is needed. Git cannot track an empty
   directory; a keep-file is the Runtime Ground's own decision, not
   the app's.

**Verified:** the standard test command green, the image pulled,
all passing.

## 5. The adversity created

- **The CBC Bootstrap Probe's endpoint,** in main source: one real
  round-trip to the database as the `runtime` role. Its own javadoc
  documents it as **scaffolding, deleted when the first real
  Invariant Slice lands.** It never grows business meaning.
- **The CBC Bootstrap Probe's test:** many requests (one CBC Run used
  a hundred) held at a barrier and **released at one instant.** Each
  is a full HTTP → application → real-PostgreSQL round-trip through
  the real door, and every response is asserted. Releasing them at
  one instant *is* the shape later race evidence takes, aimed at
  nothing yet.
- The CBC Bootstrap Probe as code, the endpoint, the barrier test and
  the javadoc that schedules its deletion, is in
  `.claude/skills/cbc-bootstrap/references/spring-harness-reference.md`,
  under the same rule: imitate, never paste.
- **When the System Definition's Runtime Ground names more than one
  instance,** the burst inside one process is the cheap first check,
  and does not close the proof. A lock inside the process would make
  it pass while two real instances still oversell, so it proves a
  shape nobody runs. The proof is then **N ≥ 2 instances of the
  system as separate processes:**
  1. against one store;
  2. each addressed through its own door;
  3. requests released at one instant across all of them;
  4. every response asserted;
  5. the State Witness read from the store from outside, never
     through an instance.

  Only a mechanism in the store, or a protocol every process honours,
  can pass it. The harness reference carries the shape, as its
  variation point 8.

**As one CBC Run built it:**
- **What is started:** the instances are **started from the build's
  own output:** `target/classes`, plus exactly the runtime classpath,
  which the dependency plugin writes to a file at
  `process-test-classes`. The system ships as a plain process, and
  the evidence starts it in the form it ships. That this needs no
  second command (the test phase runs before packaging) is a gain,
  not the reason. Were an image to ship, the evidence would start the
  image. No test-scope code runs inside an instance. Verify it: the
  written classpath carries no flyway, testcontainers, junit or
  `-test` artifact.
- **What each instance gets:** the three environment facts a real
  instance gets, the store's port, the runtime password and its own
  listen port, and nothing else from the Adversity Harness. Its
  output goes to a log file under `target/`.
- **How "up" is read:** free ports come from a socket bound and
  released. The up signal is health UP, with the store's component
  UP, through the instance's own door.
- **Who owns the lifecycle:** the Adversity Harness. Instances are
  started before the race and closed in `finally`, destroyed and then
  forcibly, none left running on a failed test.
- **What the CBC Bootstrap Probe answers:** its process id beside the
  identity, so the race asserts the process ids served are exactly
  the instances started.
- **Traps met:** none. Three instances, 120 requests at one instant,
  no port collision across runs.

**Verified:** the standard test command green.

## The exit

The project's records grown: the stack, the run and test commands,
the Operator Manual linked, "no business behavior yet" said
outright, the CBC Bootstrap Probe's deletion scheduled at the first
Invariant Slice.

## Recall list — the traps compressed

1. Boot 4 renames: web starter → web-MVC name; `-test` companions per
   starter; test REST client in `org.springframework.boot.resttestclient.*`.
2. `spring-boot-restclient` at test scope or the web test context fails on
   `RestTemplateBuilder`; `@AutoConfigureTestRestTemplate` required —
   `RANDOM_PORT` alone provides no `TestRestTemplate` bean.
3. Testcontainers 2.x: `testcontainers-postgresql`,
   `org.testcontainers.postgresql`.
4. `~/.testcontainers.properties` binds only from `$HOME`.
5. Podman socket can be *active* with the file missing — restart user
   units, confirm the file.
6. Ryuk stays on under rootless podman on 2.x; `ryuk.disabled` in the
   properties file has no effect — if it fails, the environment variable.
7. No dummy baseline migration; the history table is created by a
   run with no migrations.
8. Flyway is the Adversity Harness's only; at runtime scope it undoes
   the Runtime Ground's constraint. On Flyway ≥ 10 it needs
   `flyway-database-postgresql`.
9. Boot version coordinate plain `4.x.y` — the `.RELEASE` suffix does not
   resolve.
10. Environment facts in no tool's notation — never compose placeholder
    syntax in application config or in requirement text you write.
11. A missing secret does not stop the app — the unresolved placeholder
    binds as the literal; only health (`db` DOWN) tells. Fail-fast is a
    *what*, decided by name.
