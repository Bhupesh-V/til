# FZF: Tips and Tricks
**_Posted on 23 Mar, 2021_** 

fzf is a recent addition to my CLI utilities, below are some use-cases that might help perform common operations

1. Searching hidden files.
   ```bash
   locate "$PWD*" | fzf --height 40% --reverse
   # or
   find . -type f -not -path '*/\.git/*' | fzf --height 40% --reverse
   ```

2. Changing Directories.
   ```bash
   cd "$(locate "$PWD*" | fzf --height 40% --reverse)"
   ```
