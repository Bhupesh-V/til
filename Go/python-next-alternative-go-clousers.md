# Creating Python's `next()` alternative using Go Closures
<!-- 4 June 2020 -->
If you don't know what next() in python means, the below code illustrates it.

```python

MCU_Movies = iter(["Iron Man", "Thor", "Captain America: The first Avenger"])
x = next(MCU_Movies)
print(x, end="\n")
x = next(MCU_Movies)
print(x, end="\n")
x = next(MCU_Movies)
print(x)

```

So if you had guess this would print

```bash
Iron Man
Thor
Captain America: The first Avenger
```

> The `next()` function is used to get the next item in an iterator.

Go doesn't have a next method (nor the concept of iterators actually) so we will try to achieve something similar using [Closures](https://tour.golang.org/moretypes/25).


- A closure is implemented through a anonymous(_function with no name_) function, basically closure is an instance of function.
- In Go functions are first class citizens, meaning we can do all sort of things with them, assign them to a variable, pass as an argument to another function.

Below is a naive implementation of how this could look in Go. Ping me if you have a better way to do this ;)

```golang

package main

import "fmt"

/*
nextIterator returns another function, which we define anonymously in the body of nextIterator.
The returned function closes over the variable index to form a closure.
*/
func nextIterator(array []int) func() int {
    index := -1

    return func() int{
        index++
        return array[index]
    }
}
func main() {

	// an integer array
    var prices = []int{7, 1, 5}

    // create an instance of the anonymous function. i.e, a closue
    next := nextIterator(prices)

    // call the closure
    fmt.Println(next())
    fmt.Println(next())
    fmt.Println(next())

}
```

See this demo on [Go Playground](https://play.golang.org/p/8nH6t0HfnGu).