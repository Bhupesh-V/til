# Distributed Hash Tables (DHT)


## DHT Structure
Components include:

1. A keybase which is a set of 160 bit string
2. A `partition()` is applied over this keybase to distribute ownership among participating nodes in the DHT. Following hash functions are used
   1. Consistent Hashing, or
   2. Rendezvous Hashing
3. Each node in the network is a skip graph

## DHT Read/Write Flow

1. Generate hash (e.g SHA-1) for a given file, which gives us a 160 bit key, k
2. Send message `put(k, data)` to any node in DHT
3. The message is passed from node -> node until it finally reaches to the node responsible for key `k`
4. This node stores the data and the associated key, k
5. Now any client can request to read this data by generating the hash again which will again produce key, k
6. Send message `get(k)` to any node to read data.


# Q/A

- Generate similarity score b/w 2 hashes
- Where exactly keybase partitioning takes place? Or Who decides to partition the available keys?
