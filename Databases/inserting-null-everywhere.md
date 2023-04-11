# Inserting NULL wherever possible on Postgres

**_Posted on 11 Apr, 2023_**

### UUID

To insert null UUIDs, activate the extension

```sql
create extension if not exists "uuid-ossp";
```

then use the function `uuid_nil()`.
