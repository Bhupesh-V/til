# Splitting strings in Go



Splitting strings in Go is done by using the `Split()` method.
You need to import the `strings` standard library to use this.

## Demo

```go
package main 

import (
	"fmt"
	"strings"
)

func main(){
	var date string = "1999-03-12"
	date_array = strings.Split(date, "-")

	fmt.Println(date_array)
}
```

The `split()` return a Go Array, running this program should print the following:
```
[1999 03 12]
```
