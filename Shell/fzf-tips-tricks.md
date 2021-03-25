# FZF: Tips and Tricks
**_Posted on 23 Mar, 2021_** 

[fzf](https://github.com/junegunn/fzf) is a recent addition to my CLI utilities, below are some common use-cases.

## Ignoring unnecessary directories

Following [bash script](https://github.com/Bhupesh-V/.Varshney/blob/master/scripts/xfi) helps ignoring some directory paths while searching files via fzf.

```bash
#!/usr/bin/env bash

EXCLUDE_DIRS=(
    "! -path /*.git/*"
    "! -path /*go/*"
    "! -path /*.bundle/*"
    "! -path /*.cache/*"
    "! -path /*.local/*"
    "! -path /*.themes/*"
    "! -path /*.config/*"
    "! -path /*.codeintel/*"
    "! -path /*python2.7/*"
    "! -path /*python3.6/*"
    "! -path /*__pycache__/*"
)

find $HOME -type f ${EXCLUDE_DIRS[@]} | fzf --height 40% --reverse
```

> Note that for some reason you won't able to ignore `bin` directory paths (like in python venv's etc).

## Searching hidden files.

```bash
locate "$PWD*" | fzf --height 40% --reverse
# or
find . -type f -not -path '*/\.git/*' | fzf --height 40% --reverse
```

## Changing Directories.

```bash
# faster but limited
cd "$(locate "$PWD*" | fzf --height 40% --reverse)"
# bit slower but better
cd "$(find ~ -maxdepth 5 -not -path '*/\.git/*' -type d | fzf --height 40% --reverse)"
```

Save this in your `.bashrc`:
```bash
fcd() {
    cd "$(find ~ -maxdepth 5 -not -path '*/\.git/*' -type d | fzf --height 40% --reverse)"
}
```

## Switching Git branches

fzf can be used as a nice prompt for showing branches:

```bash
#!/usr/bin/env sh

header="Select a branch to switch to"

choice=$(git for-each-ref --format='%(refname:short)' refs/heads/* | fzf \
  --prompt="Switch branch: " \
  --height 40% --reverse
)

git switch $choice
```
