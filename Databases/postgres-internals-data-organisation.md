# Postgres 14 Internals: Data Organisation

**_Posted on 5 June, 2023_**

- A single PostgreSQL instance can serve several databases at a time; together they are called a database cluster.
- The directory that contains all the files related to the cluster is usually called `PGDATA`.
- After a cluster is intialised 3 databases are available.
  1. `template0`: used for restoring data from a logical backup or creating a database with a different encoding; it must never be modified.
  2. `template1`: serves as a template for all the other databases that a user can create in the cluster.
  3. `postgres`: a regular database that you can use at your discretion.

  > You can find the list of dbs using `select * from pg_database`.

## System Catalog

- Metadata of all cluster objects (such as tables, indexes, data types, or functions) is stored in tables that belong to the system catalog.
- All system catalog tables begin with `pg_`, like in `pg_database`.

## Schemas

- Schemas are namespaces that store all objects of a database.
- Some predefined schemas include
  - `public`: default schema for user objects.
  - `pg_catalog`: used for system catalog tables.
  - `information_schema`: provides an alternative view for the system catalog as defined by the SQL standard.
  - `pg_toast`: for objects related to `TOAST`.
  - `pg_temp`: comprises temporary tables.
- If the schema is not specified explicitly when an object is accessed, Postgres selects the first suitable schema from the *search path*.

## Tablespaces

- Tablespaces define physical data layout.
- A tablespace is a directory in a file system.
- One and the same tablespace can be used by different databases, and each database can store data in several tablespaces.
- Each database has the so-called default tablespace.
- You can find all tablespaces using the following query.

  ```sql
  select * from pg_tablespace;
  ```

## Files & Forks

- All information associated with a relation is stored in several different files called forks, each containing data of a particular type.
- Its filename consists of a numeric ID (oid), which can be extended by a suffix that corresponds to the fork’s type.
- This file can grow over time, and when its size reaches 1 GB, another file of this fork is created (such files are sometimes called segments).
- A single relation (table) can be represented on disk by several files.

### Types of Forks

TODO