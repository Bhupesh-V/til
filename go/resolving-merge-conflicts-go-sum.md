# Resolving merge conflicts in go.sum


1. Accept all the changes from any one branch (preferably the one you want to merge)
2. Re-download all dependencies via `go get -u .`
3. Run `go mod tidy`

## TODO

Since this can be a common thing among teams, best way to automate this would be to setup a `post-merge` git hook.
