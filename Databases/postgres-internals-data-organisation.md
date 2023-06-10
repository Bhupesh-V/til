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

  Sample output:

  | oid  | spcname    | spcowner | spcacl | spcoptions |
  | ---- | ---------- | -------- | ------ | ---------- |
  | 1663 | pg_default | 10       |        |            |
  | 1664 | pg_global  | 10       |        |            |

## Files, Forks & Pages

- All information associated with a relation is stored in several different files called forks, each containing data of a particular type.
- Its filename consists of a numeric ID (oid), which can be extended by a suffix that corresponds to the fork’s type.
- This file can grow over time, and when its size reaches 1 GB, another file of this fork is created (such files are sometimes called segments).
- A single relation (table) can be represented on disk by several files.
- All files are logically split into **pages** (or blocks) which is the minimum amount of data that can be read or written (8KB)

### Types of Forks

TODO

## TOAST

- **The Oversized Attributes Storage Technique** (TOAST) is used to store large values when their size overheads the maximum page size.

- If the main table contains potentially long attributes, a separate TOAST table is created for it right away, one for all the attributes. For example, if a table has a column of the numeric or `text` type, a TOAST table will be created even if this column will never store any long values.

  ```sql
  SELECT
    attname,
    atttypid::regtype,
    attstorage,
    CASE attstorage
      WHEN 'p' THEN 'plain'
      WHEN 'e' THEN 'external'
      WHEN 'm' THEN 'main'
      WHEN 'x' THEN 'extended'
    END AS storage
  FROM
    pg_attribute
  WHERE
    attrelid = 'tablename'::regclass
    AND attnum > 0;
  ```

  Here's a glimpse of the output of the above query.

  | attname | atttypid                 | attstorage | storage  |
  | ------- | ------------------------ | ---------- | -------- |
  | a       | uuid                     | p          | plain    |
  | b       | text                     | x          | extended |
  | c       | jsonb                    | x          | extended |
  | d       | timestamp with time zone | p          | plain    |
  | e       | text[]                   | x          | extended |

  - **plain** means that TOAST is not used (applied to “short” data-types such as the integer type).
  - **extended** allows both compressing attributes and storing them in a separate TOAST table.
  - **external** implies that long attributes are stored in the TOAST table in an uncompressed state.
  - **main** requires long attributes to be compressed first; they will be moved to the TOAST table only if compression version did not help.

- TOAST tables reside in a separate schema called `pg_toast`, but they are usually hidden. To find the TOAST table for a particular table, you can use the following query.

  ```sql
  SELECT
    reltoastrelid::regclass
  FROM
    pg_class
  WHERE
    oid = 'tablename'::regclass;
  ```

  Sample output:

  | reltoastrelid           |
  | ----------------------- |
  | pg_toast.pg_toast_16415 |

## Processes & Memory

- First process to start is the **postmaster** process, which is responsible for managing the cluster. If any process dies, the postmaster will restart it.
- To enable process interaction, postmaster allocates shared memory, which is avail- able to all the processes.
- postmaster process also listens for incoming connections. Once a new client appears, postmaster spawns a separate backend process. This involves authentication, then taking in SQL queries as text, parsing them, and executing them.
