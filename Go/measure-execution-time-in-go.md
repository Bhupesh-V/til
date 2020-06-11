# Measure Exection time in Go
<!-- 2 June 2020 -->
To know who how long your go code executes you can use the `time.Now()` and `time.Since()` methods in the `time` package.

## Demo

```golang

package main

import (
	"fmt"
	"time"
)

func main(){

	start := time.Now()
	dur, _ := time.ParseDuration("15ms")

	// A Go Anonymous function (self-executing)
	func (){
		for i := 0; i < 100; i++ {
			time.Sleep(dur)
			fmt.Println("Bhupesh is programming in Go")
		}
	}()

	elapsed := time.Since(start)

	fmt.Printf("Execution Time : %s", elapsed)
}

```

Since() returns the time elapsed since t (`start` in our demo). It is shorthand for `time.Now().Sub(t)`.

Here is the output of the above code
You can also play with the [online](https://play.golang.org/p/YgiaYf_Wetq) demo


```
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Bhupesh is programming in Go
Execution Time : 750ms
```
