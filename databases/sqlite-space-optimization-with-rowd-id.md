# SQLite db optimization with ROWID
**_Posted on 04 Jul, 2022_**

SQLite lets you improve your database performance by using a phrase "WITHOUT ROWID" in create table command

> A WITHOUT ROWID table is a table that uses a Clustered Index as the primary key.

```sql
CREATE TABLE IF NOT EXISTS plays(
  word TEXT PRIMARY KEY,
  chapter INTEGER
) WITHOUT ROWID;
```

## When to use

- when your schema has composite multi-column primary keys
- when your primary key is not likely an INTEGER

## Resources

- [Clustered Indexes and the WITHOUT ROWID Optimization](https://www.sqlite.org/withoutrowid.html) - Must Read
