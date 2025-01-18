# Postgres Tips & Tricks


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

List all indexes for a table

```sql
select * from pg_indexes where tablename = 'TABLE_NAME'
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
