# View a python function's history over-time with Git & FZF


I am kinda hooked up on modifying my git terminal workflow and integrate FZF wherever I can, this is such an example script to see changes in a python function overtime in your git history. And yes, its interesting (& stupid) 

```bash
#!/usr/bin/env bash

# FZF Wrapper over git to interactively search code changes inside functions

readarray -t choices < <(git ls-files | fzf \
  --prompt="Choose File: " \
  --height 40% --reverse \
)

printf "%s\n" "$(grep -o -P '(?<=def ).*?(?=\()' $choices)" | fzf \
--ansi --preview "echo {} | xargs -I{} git log --color -L :{}:$choices" \
--prompt="Choose function/method: " \
--bind 'j:down,k:up,ctrl-j:preview-down,ctrl-k:preview-up,ctrl-space:toggle-preview' --preview-window right:60% \

```

The actual trick is finding all python functions and methods names in a given file using `grep`

```bash
$ grep -o -P '(?<=def ).*?(?=\()' rich/columns.py
__init__
add_renderable
__rich_console__
iter_renderables
```

Next we plug the function name with filename in this `git` command

```bash
git log -L :funciton_name:relative_file_path
```

Read more about [git log searching](https://git-scm.com/book/en/v2/Git-Tools-Searching)

Below is a screencast demoing the same for [rich](https://github.com/willmcgugan/rich) package

[![git-search-demo-gif](https://user-images.githubusercontent.com/34342551/146226062-b87d98c6-f5e0-465b-8c8d-98ccf6bce629.gif)](https://user-images.githubusercontent.com/34342551/146226062-b87d98c6-f5e0-465b-8c8d-98ccf6bce629.gif)

If you are still interested, [here is the script](https://github.com/Bhupesh-V/.Varshney/blob/master/scripts/git/git-search) to hack around.

> I wish this was scalable to all the programming languages but currently I don't have any clue on how to do this
If you want to contribute help me by adding `grep` patterns to do the same search for you favourite programming language. Thanks

