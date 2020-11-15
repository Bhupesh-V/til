# Get last commit date of file
<!-- 15 nov 2020 -->
this can be done using the `git log` command

```bash
git log --follow -p -- filename
```

this by default renders the diffed version history of the file over time. We can use
`awk` to look for pattern _Date_ in this.

```bash
git log --follow -p -- README.md | awk '/Date/ { print $4,$3,$6 }'
```

this will grab the date of each commit which modified this file!

```bash
14 Nov 2020
11 Nov 2020
11 Nov 2020
7 Nov 2020
...
```

Here is simple script that will list last commit date of each file inside a git repo.

```bash
#!/usr/bin/env bash

# Utility to list last commit date of each file in a git repo

[[ ! -d ".git" ]] && echo -e "Not a git repo" && exit 1

for file in $(du --exclude='.git' -a . | awk '{ print $2 }'); do
	if [[ -f "${file:2}" ]]; then
		last_modify_date=$(git log --follow -p -- "${file:2}" | awk '/Date/ { print $4,$3,$6 }' | head -1)
		if [[ "$last_modify_date" ]]; then
			printf "%s : %s\n" "$last_modify_date" "${file:2}"
		fi
	fi
done

```

