# Using local Go package path


A bunch of times you might find yourself working with private Go packages that need to be tested locally.
Go let's us do that with `replace` in `go.mod` file

```
module mymodule

go 1.17

# make sure replace is just after require
require github.com/org/repo v1.1.2
replace github.com/org/repo => /Users/PC/Documents/repo

require (
        ...
        ...
)
```

After this, just run `go get -u .` and restart your IDE for changes to make effect

