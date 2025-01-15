# EXPLAIN queries in PostgreSQL
**_Posted on 20 Dec, 2021_**

PostgreSQL devises multiple "query plans" for executing a query in the most optimized & best possible way. You can use `EXPLAIN` command to see what query plan a planner creates

## `EXPLAIN`

```sql
=> EXPLAIN SELECT * FROM users;
                        QUERY PLAN
----------------------------------------------------------
 Seq Scan on users  (cost=0.00..11.62 rows=362 width=332)
(1 row)
```

## `EXPLAIN ANALYZE`

Actually executes the command, returning the execution plan and real statistics.

> ⚠️ Use `EXPLAIN`, if you want to see the execution plan without running it, or use a transaction and do an immediate rollback.

```sql
=> EXPLAIN ANALYZE SELECT * FROM users;
                                              QUERY PLAN
------------------------------------------------------------------------------------------------------
 Seq Scan on users  (cost=0.00..11.62 rows=362 width=332) (actual time=0.018..0.376 rows=365 loops=1)
 Planning Time: 0.056 ms
 Execution Time: 0.648 ms
(3 rows)
```

## Glossary

1. Sequential Scan

   > A sequential scan (or seq scan) reads the rows from the table, in order.
2. Planning Time

   > Time it took to generate the query plan from the parsed query and optimize it. It does not include parsing or rewriting.
3. Execution Time
   
   > The time shown by `EXPLAIN ANALYZE` includes executor start-up and shut-down time, as well as the time to run any triggers that are fired. Doesn't include parsing, rewriting, or planning time. 
4. Plan Rows

   > The number of rows, per-loop, that the planner expects to be returned by the operation.
5. Plan Width

   > The estimated average size of each row returned by the operation, in bytes.
6. Startup Cost

   > The estimated cost of returning the first row.
7. Total Cost

   > The estimated cost of returning all rows, by the operation and its descendents.


### Resources
- https://www.postgresql.org/docs/current/sql-explain.html
- https://www.postgresql.org/docs/9.4/using-explain.html
- https://planetscale.com/blog/how-read-mysql-explains
- [Tool to EXPLAIN for MySQL](https://explainmysql.com/)
