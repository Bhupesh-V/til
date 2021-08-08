# Parsing changelogs using regex with Go
**_Posted on 08 Aug, 2021_**

Consider a sample `CHANGELOG.md` file like this

```
# Changelog

All notable changes to this project will be documented in this file.

## [0.4] - Nov 11, 2019

### Added

- `getSubmissionDate()`, `getExitCode` new methods.
- Official Documentation.

### Changed

- Class Run `init` - Now you can pass _source code_, _input_ and _output_ to program as strings (limited to file paths in prior versions).


## [0.3] - Nov 9, 2019

### Added

- Removed redundant imports
- Added Module/Class docstrings for documentation
- Formatted Code


## [0.2] - Oct 31, 2019

### Changed

- Fix import requests problem.


## [0.1] - Oct 30, 2019
- Initial Release
```


The following golang code can be used to extract the changelog for a requested version


```golang
// Parse a changelog.md file and display changelog for a requested version

package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
	"strings"
)

func Parse(match string, rem string) string {
	// remove the enclosing pattern of previous release
	temp := strings.TrimSuffix(match, rem)
	return strings.Trim(temp, "\r\n")
}

func main() {
	enclosingPattern := `## [`
	var submatchall []string
	// prefixing verion number 0.6 with v won't work
	ver := "0.3"
	// Every new version looks like this: ## [1.4.0] - Jan 12, 2069
	// (?s) + <enclosing pattern> + <version-number> + .* + </enclosingPattern>

	// (?s) : Make the dot match all characters including line break characters
	// .* : . (dot) indicates any character whereas * specifies 0 or more instances of previous token
	// var re = regexp.MustCompile(`(?s)## \[0.6.*?## \[`)
	var re = regexp.MustCompile(`(?s)` + `## \[` + ver + `.*?` + `## \[`)

	data, err := ioutil.ReadFile("CHANGELOG.md")
	if err != nil {
		fmt.Println("File reading error", err)
	}
	fileContent := string(data)
	submatchall = re.FindAllString(fileContent, 1)
	if len(submatchall) == 1 {
		fmt.Println(Parse(submatchall[0], enclosingPattern))
	} else {
		fmt.Println("No changelog or invalid version", ver)
		os.Exit(1)
	}
}
```

Here is a sample output

```
$ go run changelog-parser.go
## [0.3] - Nov 9, 2019

### Added

- Removed redundant imports
- Added Module/Class docstrings for documentation
- Formatted Code

```
