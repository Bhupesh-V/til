# Reference Counting v/s Garbage Collection
**_Posted on 30 Jul, 2022_**

## Reference Counting (or ARC - Automatic Garbage Collection)

- In this form of GC objects are deallocated once there are no more references to them
- Each object, contains a reference counter, which is incremented every time you set a variable to that object (i.e. a new reference to the object is created), and is decremented every time you set a reference to the object to nil/null, or a reference goes out of scope (i.e. it is deleted when the stack unwinds).
- Once the reference count goes to 0, the object get deleted

### Cons
- Cyclic references `A->B->A`, and no reference count ever goes to zero.
- A little overhead of updating reference counts[^1]

### Examples
- [Cpython](https://devguide.python.org/internals/garbage-collector/index.html)


## Garbage Collection (or Tracing GC)

A very barebones Tracing GC:

- Involves keeping a list of all root objects (global, local, function variables) & tracing which objects are unreachable
- Once the GC has gone through all the objects referenced by the root objects, it goes through every allocated object, if it is marked as reachable it stays in memory, if not, it is deallocated, this is known as the **mark-and-sweep algorithm**

### Cons
- Pauses.
- Requires large memory space.

### Examples
- Java
- [Go](https://go.dev/doc/gc-guide)

[^1]: This point seems to be debatable on the [internet](https://kevinlawler.com/refcount).
