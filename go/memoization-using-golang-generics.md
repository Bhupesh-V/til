# Memoization using Golang Generics
**_Posted on 22 Jun, 2022_**

Memoization helps save computation of things that have already been computed by saving them for future use. In this example we use golang generics to implement a `Memoized()` function that can handle use-case.

```go
// Required Go 1.18 or greater

package main

import "fmt"

type FibonacciDef func(int) int

func Memoize[K comparable, T any](fn func(K) T) func(K) T {
	// Type K needs to be comparable (and hashable) since we used it as a map Key
	// Type T is any type that can act as a map value

	cache := make(map[K]T)
	return func(n K) T {
		if val, ok := cache[n]; ok {
			return val
		}
		// add to cache if not found
		cache[n] = fn(n)
		return cache[n]
	}
}

func main() {
	var memoizedFib FibonacciDef
	var simpleFib FibonacciDef
	memoizedFib = Memoize(func(num int) int {
		if num < 2 {
			return num
		}
		return memoizedFib(num-1) + memoizedFib(num-2)
	})
	simpleFib = func(num int) int {
		if num < 2 {
			return num
		}
		return simpleFib(num-1) + simpleFib(num-2)
	}
	fmt.Println(memoizedFib(50))
	// takes more than 1 minute to compute
	fmt.Println(simpleFib(50))
}
```

