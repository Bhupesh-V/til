# Anatomy of `go.mod` file
**_Posted on 20 Aug, 2021_**

Consider a hypothetical `go.mod` file

```go
module hello

go 1.13

require (
    golang.org/x/demo v0.3.0 // indirect
    rsc.io/quote v1.5.2
    golang.org/x/text version v0.0.0-20170915032832-14c0d48ead0c
)
```

The golang.org/x/text version `v0.0.0-20170915032832-14c0d48ead0c` is an example of a pseudo-version, which is the go command’s version syntax for a specific untagged commit.
The format looks like this,

`vX.Y.Z-yyyymmddhhmmss-abcdefxyz`

*Most recent tagged version* + *Commit time UTC* + *Commit prefix (12 chars)*

The _indirect_ comment indicates a dependency is not used directly by this module, only indirectly by other module dependencies (transitive dependency).
