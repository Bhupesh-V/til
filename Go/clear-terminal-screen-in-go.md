# Clearing terminal screen in Go
<!-- 5 June 2020 -->
There are two ways I like (without any external dependency)

### Using `os/exec` package

I have added some boilerplate code to make sure you see whats happening. I think this is probably the best way to do this.

```golang
package main
 
import (
    "os"
    "fmt"
    "os/exec"
    "time"
)
 
func main() {
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")

	fmt.Println("Clearing Screen in 2s...")

	// sleep for 2 seconds
	duration, _ := time.ParseDuration("2s")
	time.Sleep(duration)
    
    c := exec.Command("clear")
    c.Stdout = os.Stdout
    c.Run()
}
```

### Using ANSI Escape Sequences

Not a good way but may come in handy for some situations.

```golang

package main
 
import (
    "fmt"
    "time"
)
 
func main() {
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")
	fmt.Println("this is a line")

	fmt.Println("Clearing Screen in 1s...")
	dur, _ := time.ParseDuration("1s")
	time.Sleep(dur)

    fmt.Print("\033[2J")
}
```

> The sequence `\033[2J` is read as _Esc[2J_ where *"2j"* clears the screen and moves the cursor to the home position (line 0, column 0).