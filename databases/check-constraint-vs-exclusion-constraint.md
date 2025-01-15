# CHECK constraint v/s EXCLUSION constraint
**_Posted on 22 Jul, 2022_**

## `CHECK` constraint

CHECK checks whether a record being entered matches the boolean criteria or not. If the record violates that condition, it is not entered into the table.

```sql
CREATE TABLE PEOPLE(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     CHECK(AGE > 16),
   ADDRESS        CHAR(150),
);
```

## `EXCLUSION` constraint

EXCLUSION lets you enforce a constraint on multiple rows (for a given column). It let's you validate what data is valid for a row based on other rows that exist within the table.

> Exclusion constraints tell the database (conceptually) "When you're given a new or updated row, compare it against each existing row. Here's a list of comparisons to use. If all the comparisons between the new data and an existing row return true, reject the new data.

This constraint use btree indexes to do comparisons at a large scale. In PostgreSQL you have to create the [`btree_gist`](https://www.postgresql.org/docs/current/btree-gist.html) extension to use the EXCLUSION constraint.

```sql
CREATE EXTENSION btree_gist
```

Let's see how to use this constraint

```sql
CREATE TABLE PEOPLE(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(150),
   EXCLUDE USING gist (ADDRESS with =)
);
```

Note that if you specify "=", the semantics are equal to `UNIQUE` constraint. The magic lies in using multi-column constraints. For e.g.

```sql
EXCLUDE USING gist (a with =, b with &&)
```
Here _Row1_ will conflict with _Row2_, IFF:
1. `Row1.a == Row2_.a`, and
2. `Row1.b && Row2.b`

You can utilize other [PostgreSQL geometric operators](https://www.postgresql.org/docs/current/functions-geometry.html) here to build more complex constraints.

### Resources

- [Protect Your Data with PostgreSQL Constraints](https://nathanmlong.com/2016/01/protect-your-data-with-postgresql-constraints/)
- [Not Just UNIQUE: Exclusion Constraints](https://www.slideshare.net/pgconf/not-just-unique-exclusion-constraints)
