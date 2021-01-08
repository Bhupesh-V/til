# Add version info in Go projects
<!-- 08 Jan, 2021 -->
Go offers a nice way to specify version information at compile time using the `-ldflags` flag in go build command.

## How to use it effectively ?

Just declare a `-v` flag in your application using the `flag` package

```go
// yourapp.go
import (
    "os"
    "flag"
)

var AppVersion string = "dev"

func main() {

    Version := flag.Bool("v", false, "Prints Current AreYouOk Version")
    if *Version {
      fmt.Println(AppVersion)
      os.Exit(0)
    }
}
```

Now compile this & provide the value for `AppVersion` variable at compile time

```bash
go build -ldflags="-X 'main.AppVersion=v1.0.0'"
```

Test if it works by running `./yourapp -v`

