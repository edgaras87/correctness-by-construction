# The Database Role Split on PostgreSQL — database authority as a property the grants enforce

How database authority is split into roles on PostgreSQL. It is
generic throughout. A using project's concrete names, passwords and
wiring live in that project's own manuals, never here. On any
conflict with the setup walkthrough,
`.claude/skills/infra-establish/references/postgres-setup-walkthrough.md`,
**this model wins.**

## The principle

Making a database available to a system is not one grant but two
decisions:

- *who may change what the database is:* structure, DDL;
- *who may change what it holds:* data, DML.

The rule:

> **The running application must not control database structure.**

The schema exists only through versioned migrations. The application
works on data inside a structure it cannot alter. The split is
enforced by the **database's own grant system,** never by convention,
code review, or trust. An application identity that *cannot* issue
DDL makes drift in structure impossible, not merely forbidden.

## The roles

Three identities, two of them the model's own:

- **`migrator`:** the structure authority.
  - It owns the application schema and every object in it.
  - It is the **only identity migrations run as.** Flyway, or its
    equivalent, connects as `migrator`, and nothing else does.
  - It runs DDL within that schema, and only there. It does not own
    the database, cannot drop it, and creates no schemas beyond its
    own. It is not a superuser.
- **`runtime`:** the data authority; **what the running application
  connects as.** DML only: read and write rows, use sequences. No
  create, no alter, no drop, no ownership. If the application
  attempts DDL, the database refuses.
- *the Database Setup Identity:* the server's existing admin role,
  `postgres` in a stock container, never created by this model.
  - It runs the setup **once:** it creates the database, and owns it,
    the two roles, the application schema, and the grants.
  - It is not part of the running system, and never appears in
    application or migration config.

**Database ownership stays above the split,** with the Database
Setup Identity by default. A dedicated database-owner role is real on
shared or managed clusters. It is an extension by need, not the base
model.

## The application schema

Own it; don't use `public`. The mechanism is **ownership scoped to
the schema:** `migrator` owns a **schema named for the project,** and
everything hangs off that ownership. The default `public` schema is
the wrong place. It is a shared legacy surface whose ownership is not
the migrator's to have. The application's `search_path` names the
project's schema. And `public` is stripped of PUBLIC privileges, so
"unused" is enforced, not assumed.

## The grant boundaries (run once by the Database Setup Identity)

```sql
CREATE ROLE migrator LOGIN;
CREATE ROLE runtime  LOGIN;
CREATE DATABASE app;                    -- owned by the Database Setup Identity

-- access is explicit: nobody by default, the working identities by grant
REVOKE CONNECT ON DATABASE app FROM PUBLIC;
GRANT  CONNECT ON DATABASE app TO migrator;
GRANT  CONNECT ON DATABASE app TO runtime;

-- connected to app, as the Database Setup Identity
CREATE SCHEMA app AUTHORIZATION migrator;
GRANT USAGE ON SCHEMA app TO runtime;
REVOKE ALL ON SCHEMA public FROM PUBLIC;   -- public is no application surface

-- future objects migrator creates arrive consumable by runtime automatically
ALTER DEFAULT PRIVILEGES FOR ROLE migrator IN SCHEMA app
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO runtime;
ALTER DEFAULT PRIVILEGES FOR ROLE migrator IN SCHEMA app
  GRANT USAGE, SELECT ON SEQUENCES TO runtime;
```

The load-bearing lines are the **default privileges** pair. Every
table and sequence a future migration creates arrives already granted
to `runtime`. So the split needs no grant discipline per migration,
and cannot wear away one migration at a time. The connect revoke
works the same way for the connect right: access at every level
exists by grant, never by default.

`runtime` deliberately receives no `TRUNCATE`, no `REFERENCES`, no
`CREATE` anywhere. `migrator` deliberately owns one schema, not the
database and not the server.

## Naming across a cluster

Roles are **cluster-wide.** On any cluster serving more than one
project, role names carry the project as a prefix
(`<project>_migrator`, `<project>_runtime`), with an underscore.
Hyphens are not legal in unquoted SQL identifiers, and quoted names
cost at every use. The schema lives inside the project's database, so
it may carry the bare project name.

## Why this split and not less

- **One identity, the app as owner:** the common default, and a
  direct violation of the principle. Any ORM auto-DDL, any stray
  migration call, any injected statement can restructure the
  database. Refused.
- **Convention only ("the app just doesn't run DDL"):** rules nothing
  enforces decay. The grant system makes the rule a property.
- **More roles** (a dedicated database owner, readers, identities per
  service, row-level security): real needs at a larger scope.
  Extensions by need, not the base model.

## What a using project supplies

1. concrete role names, under the naming rule above, and their
   credentials (secrets handling is the project's);
2. the schema name, and the application's `search_path`;
3. which migration tool connects as `migrator`;
4. where `bootstrap.sql` lives, and how it is applied;
5. how the model is verified on the Runtime Ground: Catalog Checks,
   plus a Behavioral Check that DDL is refused;
6. where each of these is written: in the project's manuals and the
   Runtime Ground's files, referring to this model, never restating
   it.
