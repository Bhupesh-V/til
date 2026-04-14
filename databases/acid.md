# ACID

## Atomicity

- If operations, when grouped together in "atomic" transactions fail to be comitted due to a fault, then the transaction is aborted.
- _Abortability_ could have been a better term

## Consistency

- Defines the the database is in a "good state" which is highly subjective because you can violate data rules
- Not a property of a database.
- The application may rely on database's atomicity & isolation properties to achieve consistency (?)

## Isolation

- Concurrently running transactions are isolated from each other.

## Durability

- Promise that once a transaction has comitted successfully, any data it has written will not be forgotten, even if there's a hardware failure.
- Single node = write to disk
- Distributed = replicate


Reference: DDIA