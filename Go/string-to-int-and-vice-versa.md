# Convert `string` to `int` and vice-versa in Go
<!-- 31 May 2020 -->
There are basically 2-3 methods to convert integer to string and back to integer but the most easiest way is to use the `Itoa` and `Atoi` methods in the `strconv` package.


## Demo

```golang
package main

import (
    "fmt"
    "strconv"
)

func main() {
	// String to Int
	nice, _ := strconv.Atoi("69")
	fmt.Printf("%T", nice)

	//Integer to String
	high := strconv.Itoa(420)
	fmt.Printf("\n%T", high)
}
```

`Atoi` returns a second value (`err` ignored in this example for easier understanding)

The above code should output:
```
int
string
```
See [online](https://play.golang.org/p/moTZJ5LYEz9) demo
