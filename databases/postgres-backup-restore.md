<!-- omit from toc -->
# Taking & Restoring Postgres Backups

- [Pre-requisites](#pre-requisites)
- [Playground Setup](#playground-setup)
- [Taking Backup](#taking-backup)
  - [Example](#example)
- [Restoring from Backup](#restoring-from-backup)
  - [Example](#example-1)
- [Verifying Backup Restores](#verifying-backup-restores)
  - [Check all Indexes across `public` schema](#check-all-indexes-across-public-schema)
  - [Check all ENUM types across `public` schema](#check-all-enum-types-across-public-schema)
  - [Check total count of rows for critical tables](#check-total-count-of-rows-for-critical-tables)
- [Tips](#tips)


## Pre-requisites

- We primarily need `pg_dump` & `pg_restore`.
  - On Mac: `brew install postgresql@16`

> Note: It's important that the Postgres CLI tools version should match the Postgres database version.

## Playground Setup

For the sake of this TIL, we are migrating a postgres db to another postgres db. Use the following `docker-compose.yml` as a setup

```
services:
  db_version_1:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=db_1
      - POSTGRES_USER=db
      - POSTGRES_PASSWORD=123
    ports:
      - '5442:5432'
    volumes:
      - db_version_1:/var/lib/postgresql/data
    networks:
      - backend
    command: ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]

  db_version_2:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=db_2
      - POSTGRES_USER=db
      - POSTGRES_PASSWORD=123
    ports:
      - '5492:5432'
    volumes:
      - db_version_2:/var/lib/postgresql/data
    networks:
      - backend
    command: ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]


volumes:
  db:
    driver: local
  db_version_2:
    driver: local

networks:
  public_network:
    driver: bridge
```

Up the databases, using

```
docker-compose up -d db_version_1
docker-compose up -d db_version_2
```

Tip: Wipe the databases

```
docker-compose stop db_version_2

# Remove the container
docker-compose rm db_version_2

# Remove the associated volume
docker volume rm bookstore-ai-backend_db_version_2
```

## Taking Backup

```
PGPASSWORD='source_db_password' pg_dump -h HOST -p PORT -U USER -d DB_NAME -Fc -f source.dump
```

### Example

```
PGPASSWORD='123' pg_dump -h localhost -p 5442 -U db -d db_1 -Fc -f source.dump
```

Mime Type

```
file source.dump
source.dump: PostgreSQL custom database dump - v1.15-0
```


## Restoring from Backup

```
PGPASSWORD='target_db_password' pg_restore -h HOST -p PORT -U USER -d DB_NAME --exit-on-error --single-transaction source.dump
```

### Example

Assuming the new db is running at port `5492` with a name `db_2`

```
PGPASSWORD='123' pg_restore -h localhost -p 5492 -U db -d db_2 --exit-on-error --single-transaction source.dump
```

## Verifying Backup Restores

To perform a High level verification of the backups restored (other than the functional tests).

### Check all Indexes across `public` schema

```
select
  n.nspname as schema_name,
  t.relname as table_name,
  i.relname as index_name,
  ix.indisprimary as is_pk,
  ix.indisunique as is_unique
from
  pg_index ix
  join pg_class i on i.oid = ix.indexrelid
  join pg_class t on t.oid = ix.indrelid
  join pg_namespace n on n.oid = t.relnamespace
where
  t.relkind = 'r' -- regular tables
  and n.nspname = 'public'
order by
  t.relname,
  i.relname;
```

### Check all ENUM types across `public` schema

```sql
SELECT
  n.nspname AS schema,
  t.typname AS enum_type,
  e.enumlabel AS enum_value,
  e.enumsortorder
FROM
  pg_type t
  JOIN pg_enum e ON t.oid = e.enumtypid
  JOIN pg_namespace n ON n.oid = t.typnamespace
WHERE
  n.nspname = 'public'
ORDER BY
  enum_type,
  enumsortorder;
```

### Check total count of rows for critical tables

```sql
SELECT
  (SELECT COUNT(*) FROM users) AS user_count,
  (SELECT COUNT(*) FROM gorp_migrations) AS migrations_count;
  ...
```

## Tips

1. While restoring a db, if the goal is wipe the target db before a restoration, use the `--clean` flag in `pg_restore` command.
2. If the target db doesn't exist, create it using `--create` flag in `pg_restore`.
