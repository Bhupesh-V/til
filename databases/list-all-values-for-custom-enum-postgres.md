# List all values of a custom enum in Postgres

**_Posted on 23 May, 2023_**

```sql
select enum_range(null::my_enum)
```

To list in separate rows

```sql
select unnest(enum_range(null, null::my_enum));
```
