# FZF: Tips and Tricks
**_Posted on 23 Mar, 2021_** 

[fzf](https://github.com/junegunn/fzf) is a recent addition to my CLI utilities, below are some common use-cases.

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

Save this in your `.bashrc` like this:
```bash
fcd() {
    cd "$(find ~ -maxdepth 5 -not -path '*/\.git/*' -type d | fzf --height 40% --reverse)"
}
```

## Switching Git branches

fzf can be used as a nice prompt to quickly switch branches

```bash
#!/usr/bin/env sh

header="Select a branch to switch to"

choice=$(git for-each-ref --format='%(refname:short)' refs/heads/* | fzf \
  --header="$header [$flags]" \
  --prompt="Switch branch: " \
  --height 40% --reverse
)

git switch $choice
```
