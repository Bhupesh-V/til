# Collected notes on Database Sharding 🗃
<!-- 16 Feb, 2021 -->

Sharding means breaking up data into two or more smaller chunks.
Shards may deployed at separate "physical" locations.

Different ways of partitioning:

- Horizontal Partitioning: Schema remains same but the data rows are segregated.
- Vertical Partitioning: Schema is changed, each row in a shard is different from another shard.

Can be done either at application level(logically decide which shard to store data) or natively at database level

## Pros

- Horizontal Scaling (scaling out): add more machines so as to distribute load.
  > In contrast to Vertical Scaling (scaling up) which can be done by improving server resources like CPU etc.
- Faster query results, since monolithic db will have millions of rows to search from. Indexing size is reduced
- Better uptime, resistant from outages. Only a part of application will be affected


## Cons

- Increased Complexity in implementing a sharded db
- Uneven segregation can lead to problems
- Cannot go back to unsharded state
- Not much good support at database level.

## Techniques

Different approaches exist to create a sharded architecture:

1. Key base Sharding
   - A hash function is applied on user data (like primary keys, IP address etc).
   - The hash value generated (shard id) can be used to determine on which shard data must be stored.
   - Problem lies in the fact that if you start adding more servers each one will need a corresponding hash value and many of your existing entries will need to be remapped to the new correct hash value and then migrated to the appropriate server. Thus increasing chances of downtime. Although [consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing) can be used to fix this.
2. Range based Sharding
   - Data is divided in terms of ranges, each shard stores different part of the division
3. Directory based Sharding
   - A special table (map) is used to determine which shard holds what data.
   - Most flexible of all the tree approaches, custom rules can be enforced easily.

### Resources

- [Shared Nothing Architecture](https://en.wikipedia.org/wiki/Shared-nothing_architecture)
- [Performance & Scalability](https://www.infoq.com/performance-scalability/)

