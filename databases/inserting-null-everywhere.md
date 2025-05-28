# Inserting NULL wherever possible on Postgres

## UUID

To insert null UUIDs, activate the extension

```sql
create extension if not exists "uuid-ossp";
```

then use the function `uuid_nil()`.

## JSONB

To insert null JSONB, use the `to_jsonb` function:

```sql
UPDATE
  table_name
SET
  my_jsonb_column = to_jsonb(null)
WHERE
  id = 1;

-- or

UPDATE
  table_name
SET
  my_jsonb_column = 'null'::jsonb
WHERE
  id = '1';
```

Fair warning: JSONB `null` is different from SQL `null`.

```sql
SELECT
  pg_typeof(NULL) AS sql_null_type,
  pg_typeof('null'::jsonb) AS jsonb_null_type;

-- "sql_null_type"	"jsonb_null_type"
-- "unknown"	"jsonb"
```
