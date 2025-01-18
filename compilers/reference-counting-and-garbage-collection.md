# Reference Counting v/s Garbage Collection


## Reference Counting (or ARC - Automatic Garbage Collection)

- In this form of GC objects are deallocated once there are no more references to them
- Each object, contains a reference counter, which is incremented every time you set a variable to that object (i.e. a new reference to the object is created), and is decremented every time you set a reference to the object to nil/null, or a reference goes out of scope (i.e. it is deleted when the stack unwinds).
- Once the reference count goes to 0, the object get deleted

### Cons
- Cyclic references `A->B->A`, and no reference count ever goes to zero.
- A little overhead of updating reference counts[^1]

### Examples

- [Cpython](https://devguide.python.org/internals/garbage-collector/index.html)
- [Memory Management in Python](https://realpython.com/python-memory-management/#garbage-collection)
- [Python Memory Management and Weak References](https://uwpce-pythoncert.github.io/SystemDevelopment/weak_references.html#python-memory-management-and-weak-references)

  ```
  Python 3.8.10 (default, Jun 22 2022, 20:18:18)
  [GCC 9.4.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import sys
  >>> a = "bhupesh"
  >>> sys.getrefcount(a)
  2
  >>>
  ```


## Garbage Collection (or Tracing GC)

- Involves keeping a list of all root objects (global, local, function variables) & tracing which objects are unreachable
- Once the GC has gone through all the objects referenced by the root objects, it goes through every allocated object, if it is marked as reachable it stays in memory, if not, it is deallocated, this is known as the **mark-and-sweep algorithm**

### Cons
- GC Pauses.
- Requires large memory space.

### Examples

- [Go](https://go.dev/doc/gc-guide)
  - [In Go, when will a variable become unreachable?](https://stackoverflow.com/questions/37588639/in-go-when-will-a-variable-become-unreachable)
  - [How Go GC detects if a memory object contains a pointer](https://www.sobyte.net/post/2022-03/how-gc-detect-pointer-in-mem-obj/)

[^1]: This point seems to be debatable on the [internet](https://kevinlawler.com/refcount).
