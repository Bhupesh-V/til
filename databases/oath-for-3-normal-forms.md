# The 3NF Oath ✋🏼

> **Every non-key must provide a fact about the key, the whole key, and nothing but the key, so help me Codd.**

## 1NF: "Provide a fact about the key"

- Explanation: Every column must contain atomic values, meaning no lists or complex data structures. 1 cell = 1 piece of data.
- Actual Meaning: Non-key attributes must depend on the primary key, ensuring each column represents a single piece of data about the key.

## 2NF: "The whole key"

- Explanation: A table is in 2NF if it is in 1NF and every non-key column depends on the entire composite primary key (if applicable). No partial dependency on a subset of the composite key is allowed.
- Actual Meaning: Non-key attributes must depend on all parts of a composite primary key, not just a subset.

## 3NF: "Nothing but the key"

- Explanation: A table is in 3NF if it is in 2NF and there are no transitive dependencies. Non-key attributes should depend only and directly on the primary key, not indirectly through another non-key column.
- Actual Meaning: Data in the table should not rely on any other non-key attribute, ensuring direct dependency on the primary key.

### Resources

- https://en.wikipedia.org/wiki/Third_normal_form#%22Nothing_but_the_key%22
- https://www.reddit.com/r/explainlikeimfive/comments/13llrau/comment/jkqrp0p