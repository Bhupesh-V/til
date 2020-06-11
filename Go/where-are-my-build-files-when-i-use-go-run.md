# Where are my build files when I use `go run`
<!-- 9 June 2020 -->
By default, 'go run' runs the compiled binary directly.
The binaries are stored in a `temp` work folder, to see where they are stored use the `-work` flag.


## Demo

```bash
go run --work fizzbuzz.go
```

Sample Output

```
WORK=/tmp/go-build645222420
[1 2 Fizz]
```

When you run this go will not delete the temporary build when exiting.
The default directory may vary with your system & `GOPATH`.