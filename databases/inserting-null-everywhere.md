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
insert into my_table (my_jsonb_column) values (to_jsonb(null));
update my_table set my_jsonb_column = to_jsonb(null) where id = 1;
```

> Fair warning: JSONB `null` is different from SQL `null`.
