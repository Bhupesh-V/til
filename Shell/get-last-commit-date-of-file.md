# Get last commit date of file
<!-- 15 nov 2020 -->
this can be done using the `git log` command

```bash
git log --follow -p -- filename
```

This by default renders the diffed version history of the file over time. This can be 
suppressed by `-q` flag after that we can use `awk` to look for pattern _Date_.

```bash
git log --follow -q -- README.md | awk '/Date/ { print $4,$3,$6 }'
```

This will grab the date of each commit which modified this file!

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
        commit_date=$(git log --follow -q -- "${file:2}" | awk '/Date/ { print $4,$3,$6 }' | head -1)
        [[ "$commit_date" ]] && printf "%12s : %s\n" "$commit_date" "${file:2}"
    fi
done
```

A better version of the script is available in my [dotfiles](https://github.com/Bhupesh-V/.Varshney/blob/master/scripts/last-modify.sh)
