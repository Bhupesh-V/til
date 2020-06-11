# Reading & Setting Environment variables in Go
<!-- 9 June 2020 -->
Use `os.Getenv()` and `os.Setenv()` for reading and setting environment variables.

## Demo

```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	os.Setenv("NAME", "gopher")

	fmt.Printf("My Desktop Environment : %s.\n", os.Getenv("XDG_CURRENT_DESKTOP"))
}
```