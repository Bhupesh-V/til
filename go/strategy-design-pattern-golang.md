# Strategy Design Pattern in Go


```go
// modified version of https://play.golang.org/p/VH-IvOgH1qw

package main

import (
	"fmt"
)

type Greeter interface {
	Hello()
}

type Greet struct {
	GreetType Greeter
}

func (gg *Greet) Hello() {
	gg.GreetType.Hello()
}

// different greeters
type ShortGreet struct{}

func (sg ShortGreet) Hello() {
	fmt.Println("hi")
}

type LongGreet struct{}

func (lg LongGreet) Hello() {
	fmt.Println("Oh well, hello there!")
}

func main() {
	var g = &Greet{}
	g.GreetType = ShortGreet{}
	g.Hello()

	g.GreetType = LongGreet{}
	g.Hello()
}

```

[**Play with it online**](https://go.dev/play/p/DAjsBRhtkEr)
