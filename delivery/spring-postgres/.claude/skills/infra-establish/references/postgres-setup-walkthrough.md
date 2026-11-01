# PostgreSQL setup walkthrough — from nothing to a governed, verified Runtime Ground

What to do, end to end, for one Infrastructure Service, as two
CBC Runs did it.

**It owns nothing.** The shape of the authority, the roles, the
grants and the why, has its home in
`.claude/skills/infra-establish/references/postgres-role-split.md`.
On any conflict, the Database Role Split wins.

The context it assumes, noted where it binds:

- the Execution Environment is **podman local containers,** driven
  by a compose file;
- **Flyway** runs as a compose one-shot, as the only DDL path.

Placeholders: `<project>`, with an underscore in SQL identifiers
(`<project>_migrator`), and with a hyphen where project naming allows
it (the compose project name).

The files themselves are Agent Skill Templates in `templates/`,
beside this Agent Skill's `references/`. This walkthrough carries the whys
and the order. The Agent Skill Templates carry the bodies, and their
comments for recall. Fill one, and the filled file is the CBC Run's
own. The Agent Skill Templates implement the assumptions above. If
the CBC Run's decided constraints differ, you are off-template.
Derive from the Database Role Split
(`.claude/skills/infra-establish/references/postgres-role-split.md`),
and record the deviation as delivered-copies rule 8 says
(`.claude/rules/delivered-copies.md`, rule 8, *An Agent Skill Template is…*).

## 0. Preconditions

- podman installed, and a compose provider present. `podman compose
  config` runs clean. The canonical command is `podman compose`,
  whatever provider stands behind it.
- The decisions already made and logged: PostgreSQL is a required
  Infrastructure Service, and its Infrastructure Service Constraints
  are named: DDL by migrations only, and authority by the Database
  Role Split. This walkthrough *implements* those decisions. It does
  not make them.

## 1. Declare the service

`compose.yaml`: a `postgres` service and the Flyway one-shot. The
one-shot sits behind a profile: it is the only DDL path, hidden from
plain `up`. Agent Skill Template:
`.claude/skills/infra-establish/templates/compose.yaml`.

Podman notes:
- the `:Z` mount flag matters on SELinux hosts;
- volume and network names get the compose project prefix
  automatically. Never write it by hand;
- the `name:` pin is a correction a CBC Run made. Without it, the
  volume's identity depends on the directory the file happens to run
  from.

## 2. Split out credentials

`.env`, git-ignored, and a committed `.env.example`. Agent Skill
Template: `.claude/skills/infra-establish/templates/.env.example`.
The keys:

1. the Database Setup Identity's password;
2. the `migrator` password, which **must equal** the literal in
   `bootstrap.sql`;
3. `POSTGRES_PORT`, optional;
4. the `runtime` application password, which **must equal** the
   `runtime` literal in `bootstrap.sql`. The app reads it from the
   environment at the CBC Bootstrap.

The rule: secrets and what varies per machine are variables.
**Decided identities (the database, schema and role names) stay
literal** in the files that use them. Changing one is a committed
decision, not configuration.

## 3. Write `bootstrap.sql`

`infrastructure/postgres/init/bootstrap.sql` runs **once,**
automatically, at the container's first start against an empty
volume. It runs as the Database Setup Identity, **connected to
`POSTGRES_DB`.** Agent Skill Template:
`.claude/skills/infra-establish/templates/bootstrap.sql`. Its
comments are there for recall, carried in full. The load-bearing
lines are the default privileges. Every table and sequence a future
migration creates arrives already granted to `runtime`. So the split
needs no discipline per migration, and cannot stop holding.

Who creates the database: **the container,** from `POSTGRES_DB`. It
is owned by the Database Setup Identity, and `migrator` owns only the
schema. There is no `CREATE DATABASE` in the script.

## 4. Land the Catalog Check

`infrastructure/postgres/verify-database-model.sql` sits beside
`init/`, **not in it:** it runs on demand, never at container start.
Agent Skill Template:
`.claude/skills/infra-establish/templates/verify-database-model.sql`.
It queries the catalog against the Database Role Split's claims:

1. the roles and their capabilities;
2. who owns the database and the schema;
3. the schema's privileges;
4. the default privileges: the Database Role Split's load-bearing mechanism, which
   `\dn+` does not show.

The expected results are comments beside each query, so the reader
needs no other doc open.

## 5. Wire Flyway

`infrastructure/flyway/conf/flyway.conf`: no credentials, since
compose passes them in the environment. The url names the compose
network's service. Agent Skill Template:
`.claude/skills/infra-establish/templates/flyway.conf`.

`infrastructure/flyway/migrations/`: empty, with a `.gitkeep`, until
work needs schema. The naming, when it does: `V<n>__<description>.sql`.
**No grant statements in migrations, ever:** the default privileges
handle it.

## 6. Bring the services up

```sh
podman compose config      # sanity: interpolation resolves, file renders
podman compose up -d       # first start: db created, bootstrap SQL runs
podman compose ps          # expect: <project>-postgres Up (healthy)
```

**A trap a CBC Run met:** the image runs `bootstrap.sql` against a
*temporary* server, and then restarts. The health check can report
healthy during that temporary server, and a query in that window
fails with `the database system is shutting down`. Wait a second and
retry. `pg_isready`, plus one real query, is the true "up".

## 7. Verify both ways

The Catalog Check:

```sh
podman exec -i <project>-postgres \
  psql -U postgres -d <project_db> < infrastructure/postgres/verify-database-model.sql
```

The Behavioral Check (the Infrastructure Service Constraint
attempted, and refused, live):

```sh
podman exec -it <project>-postgres \
  psql -U <project>_runtime -d <project_db> -c 'CREATE TABLE t(i int);'
# expected: ERROR: permission denied for schema <project_schema>
```

The other refusal worth watching live: a role with no grant cannot
connect. Try it with a throwaway role, dropped after:

```sh
podman exec <project>-postgres psql -U postgres -d <project_db> -c "CREATE ROLE probe LOGIN;"
podman exec <project>-postgres psql -U probe -d <project_db> -c 'select 1'
# expected: FATAL:  permission denied for database "<project_db>"
podman exec <project>-postgres psql -U postgres -d <project_db> -c "DROP ROLE probe;"
```

**Flyway as `migrator`:** it connects, sees the schema, and shows an
empty history, which is correct on a fresh Runtime Ground.

```sh
podman compose run --rm flyway info
```

## 8. Know the reset path

`bootstrap.sql` runs only against an empty volume. After any change
to it (**destructive: it drops all data. Get explicit confirmation
first**):

```sh
podman compose down --volumes
podman compose up -d
```

…then run step 7 again, both checks.

## 9. The connection facts

**Decide, and write in the manuals, which identity people inspect
with.** Day-to-day inspection in an IDE or `psql` would otherwise use
`runtime`: the identity the application writes with. So whoever
inspects holds a password that can change every table. Say which the
project means, in the manuals and against CBC Framing. Either:

- the System Definition's Trust Assumptions cover people reading
  with it, trusted not to write; or
- a read-only identity is owed for looking, made at the CBC
  Bootstrap beside the two.

Left unsaid, the writing identity is handed out as the looking one.
Then the Invariant Slices cannot tell whether that reader can write,
so they must defend against one who does.

The connection facts the system's code needs:

1. the host: `localhost:${POSTGRES_PORT:-5432}` from outside, and
   `postgres:5432` from container to container;
2. the database: `<project_db>`;
3. the schema: `<project_schema>`;
4. **the application connects as `<project>_runtime`, and nothing
   else;**
5. `migrator` is the migration tool's identity alone;
6. the Database Setup Identity is used by hand for admin, never in
   config.

**Reading from outside without a host `psql`.** The State Witness
Reading, persisted state read from the host as `runtime` through the
published port, needs a client. A host without one uses a client
container on the host network. With a host `psql`, the same URL works
directly:

```sh
podman run --rm --network host docker.io/library/postgres:17 \
  psql "postgresql://<project>_runtime:<password>@localhost:${POSTGRES_PORT:-5432}/<project_db>" -c 'select 1'
# expected: 1
```

These facts land in the project's living Infrastructure Contract:
one section per Infrastructure Service, grown at each later
Infrastructure Service Re-entry, the refusals written as contract
terms. Note there that the Runtime Ground's files were filled from
this Agent Skill's Agent Skill Templates: the trail a later reader
needs to find the Master Copies.
