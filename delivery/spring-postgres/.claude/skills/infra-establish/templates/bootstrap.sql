-- Agent Skill Template — the Master Copy is in correctness-by-construction.
-- Copy into a CBC Run at the same path and fill; the filled
-- file is the CBC Run's own (.claude/rules/delivered-copies.md, rule 8, An Agent Skill Template is…).

-- infrastructure/postgres/init/bootstrap.sql
--
-- Purpose:
--   Make the Database Role Split real for this project: the two working
--   identities, the application schema, and the privilege boundaries.
--   Reference: .claude/skills/infra-establish/references/postgres-role-split.md.
--   This file makes it real, and never derives it again.
--
-- Run as:
--   the Database Setup Identity (postgres). It runs automatically, ONCE, at the
--   container's first start against an empty volume (docker-entrypoint-initdb.d;
--   files there run in lexical order, irrelevant while this is the only one).
--   Re-run = full reset: podman compose down --volumes, then up.
--
-- Database context:
--   <project_db>: the container's entrypoint creates POSTGRES_DB (compose.yaml)
--   at first start, then runs this script CONNECTED TO IT: schema and grant
--   statements below land in this database. CREATE ROLE is the exception:
--   roles are cluster-wide, in no database.
--
-- Local development note:
--   Role passwords are explicit local-dev placeholders, coupled to .env
--   (FLYWAY_MIGRATOR_PASSWORD must equal the migrator password here).
--
-- Boundary:
--   Identities, schema, and privilege boundaries only. No tables, no
--   application objects: those arrive solely through the migration tool.

-- the two identities of the Database Role Split. Prefixed names are the
-- shared-cluster case, since roles are cluster-wide
-- (.claude/skills/infra-establish/references/postgres-role-split.md, Naming across a cluster).
-- One dedicated cluster in one container, the usual case in CBC Runs,
-- takes the Database Role Split's bare names, migrator and runtime. Then:
--   - infrastructure/postgres/verify-database-model.sql's role filter becomes an explicit IN list;
--   - the other templates' <project>_ role references drop the prefix too.
CREATE ROLE <project>_migrator LOGIN PASSWORD '<project>_migrator_localdev';
CREATE ROLE <project>_runtime  LOGIN PASSWORD '<project>_runtime_localdev';

-- PUBLIC (the grant target: every role, present and future) loses the default
-- right to connect; access to this database exists only by the named grants
-- below. The Database Setup Identity needs no grant: superusers bypass checks.
REVOKE CONNECT ON DATABASE <project_db> FROM PUBLIC;
GRANT  CONNECT ON DATABASE <project_db> TO <project>_migrator;
GRANT  CONNECT ON DATABASE <project_db> TO <project>_runtime;

-- the application schema: owned by migrator, consumable by runtime
CREATE SCHEMA <project_schema> AUTHORIZATION <project>_migrator;
GRANT USAGE ON SCHEMA <project_schema> TO <project>_runtime;

-- the DEFAULT SCHEMA named "public" (unrelated to the PUBLIC grant target
-- above) stops being usable by anyone: no second schema beside the
-- governed one. (PG15+ already revokes CREATE; this makes the whole stance explicit.)
REVOKE ALL ON SCHEMA public FROM PUBLIC;

-- the load-bearing lines
-- (.claude/skills/infra-establish/references/postgres-role-split.md, The grant boundaries…)
ALTER DEFAULT PRIVILEGES FOR ROLE <project>_migrator IN SCHEMA <project_schema>
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO <project>_runtime;
ALTER DEFAULT PRIVILEGES FOR ROLE <project>_migrator IN SCHEMA <project_schema>
  GRANT USAGE, SELECT ON SEQUENCES TO <project>_runtime;

-- search_path: where unqualified names resolve. It is pinned so migrations
-- and application statements land in the governed schema, never in public.
-- It is a default for convenience. The authority boundary is the grants above.
ALTER ROLE <project>_migrator SET search_path = <project_schema>;
ALTER ROLE <project>_runtime  SET search_path = <project_schema>;
