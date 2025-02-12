<!-- omit from toc -->
# Postgres Tips & Tricks - Megalist of Secret SQL Queries

- [List all table indexes](#list-all-table-indexes)
- [List all column types across the schema](#list-all-column-types-across-the-schema)
- [List history of sequential \& index scans across all tables](#list-history-of-sequential--index-scans-across-all-tables)
- [Show index usage across all tables](#show-index-usage-across-all-tables)
- [Show table size](#show-table-size)

## List all table indexes

```sql
select 
    c.relnamespace::regnamespace as schema_name,
    c.relname as table_name,
    i.indexrelid::regclass as index_name,
    i.indisprimary as is_pk,
    i.indisunique as is_unique
from pg_index i
join pg_class c on c.oid = i.indrelid
where c.relname = 'TABLE_NAME'

```

## List all column types across the schema

```sql
SELECT n.nspname AS schema_name,
       t.typname AS type_name,
       t.typtype AS type_type,
       t.typcategory AS type_category
FROM pg_type t
JOIN pg_namespace n ON t.typnamespace = n.oid
WHERE n.nspname NOT IN ('pg_catalog', 'information_schema')
  AND t.typtype IN ('e', 'c'); -- 'e' for ENUM, 'c' for composite types
```

## List history of sequential & index scans across all tables

```sql
SELECT
  relname AS table_name,
  seq_scan,
  last_seq_scan,
  idx_scan,
  last_idx_scan,
  seq_scan + idx_scan AS total_accesses
FROM
  pg_stat_all_tables
WHERE
  schemaname = 'public'
  and seq_scan + idx_scan is not null
ORDER BY
  total_accesses DESC;
```

## Show index usage across all tables

```sql
SELECT
  relname AS table_name,
  indexrelname AS index_name,
  idx_scan AS index_scans
FROM
  pg_stat_user_indexes
  JOIN pg_index ON pg_stat_user_indexes.indexrelid = pg_index.indexrelid
ORDER BY
  idx_scan DESC;
```

## Show table size

```sql
SELECT pg_size_pretty(pg_relation_size('table'));
```
