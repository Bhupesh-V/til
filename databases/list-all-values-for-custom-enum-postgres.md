# List all values of a custom enum in Postgres



```sql
select enum_range(null::my_enum)
```

To list in separate rows

```sql
select unnest(enum_range(null, null::my_enum));
```
