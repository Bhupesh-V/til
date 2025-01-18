# FZF: Tips and Tricks
 

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

If you prefer the `locate` command instead, make sure to update your `/etc/updatedb.conf` file with following `PRUNENAMES`
```
PRUNE_BIND_MOUNTS="yes"
PRUNENAMES=".git .cache .bundle .local .config node_modules __pycache__ python3.6 go"
PRUNEPATHS="/tmp /var/spool /media /var/lib/os-prober /var/lib/ceph /home/.ecryptfs /var/lib/schroot"
PRUNEFS="NFS nfs nfs4 rpc_pipefs afs binfmt_misc proc smbfs autofs iso9660 ncpfs coda devpts ftpfs devfs devtmpfs fuse.mfs shfs sysfs cifs lustre tmpfs usbfs udf fuse.glusterfs fuse.sshfs curlftpfs ceph fuse.ceph fuse.rozofs ecryptfs fusesmb"
```

or include any other directories you don't want like `.DS_Store` etc.
Then run `sudo updatedb` to update the mlocate database. After that you can just pipe the output to fzf.

```bash
# look for any path in you $HOME directory
locate -ei "$HOME" | fzf --height 40% --reverse
```

In vim you can create a [custom command](https://github.com/junegunn/fzf/blob/master/README-VIM.md#fzfrun), make sure you have [fzf.vim](https://github.com/junegunn/fzf.vim) installed.

```vim
command! -nargs=1 -bang Locate call fzf#run(fzf#wrap({'source': 'locate -ei $HOME'}, <bang>0))
```

## Changing Directories.

If you followed the previous tip then using this is a no brainer

```bash
# faster but limited
cd "$(locate "$HOME" | fzf --height 40% --reverse)"
# bit slower but better
cd "$(find ~ -maxdepth 5 -not -path '*/\.git/*' -type d | fzf --height 40% --reverse)"
```

Save this in your `.bashrc`:
```bash
fcd() {
    cd "$(find ~ -maxdepth 5 -not -path '*/\.git/*' -type d | fzf --height 40% --reverse)"
}
```

## Opening files from terminal using your file-manager 🗃️

```bash
# xdg-open for X11
# open for Mac
browse "$(locate -ei "$HOME" | fzf --height 40% --reverse)"
```

A better version using `xargs`

```bash
alias bro="locate -ei "$HOME" | fzf --height 40% --reverse | xargs browse 2>/dev/null"
```

## Switching Git branches

fzf can be used as a nice prompt for showing git branches:

```bash
#!/usr/bin/env sh

choice=$(git for-each-ref --format='%(refname:short)' refs/heads/* | fzf \
  --prompt="Switch branch: " \
  --header="Select a branch to switch to" \
  --height 40% --reverse
)

git switch $choice
```

## Interactively stage files in Git

```bash
#!/usr/bin/env bash

readarray -t choices < <(git ls-files --other --modified --exclude-standard | fzf \
  --prompt="Stage Files: " \
  --height 40% --reverse --multi \
  --header="Choose files to stage (TAB to select multiple files)"
)

git add "${choices[@]}"

```

## Deleting unused branches interactively
```bash
#!/usr/bin/env sh

header="Select branches to delete"

choices=$(git for-each-ref --format='%(refname:short)' refs/heads/* | fzf \
  --prompt="Delete Branches: " --pointer='🡆'\
  --header="Press TAB to select choices" \
  --multi --height 30% --reverse
)

git branch -d $choices
```

## Diff(ing) files across branches

Useful in cases when your working with multiple people and want to compare files that are changed while building a feature. 

```bash
#!/usr/bin/env bash

# FZF Wrapper over git to interactively diff files across branches

readarray -t git_files < <(git ls-files | fzf \
  --prompt="Choose File(s): " \
  --height 40% --reverse --multi \
  --header="Choose files to diff (TAB to select multiple files)"
)

target_branch=$(git for-each-ref --format='%(refname:short)' refs/heads/* | fzf \
  --prompt="Select target branch: " \
  --header="Select branch to compare the files against" \
  --height 40% --reverse
)

# get current branch
current_branch=$(git branch | grep \\* | cut -d ' ' -f2)

printf "%s\n" "Viewing diff for following files against $(tput bold)$target_branch$(tput sgr0)"
printf "$(tput bold)$(tput setaf 208)%s$(tput sgr0)\n" "${git_files[@]}"
echo

git diff "$current_branch".."$target_branch" -- "${git_files[@]}"

```

## Replacing [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli) with `fzf`

I like the idea of using emojis in commit messages but I am not ready to install node/npm and 10 other dependencies for a CLI.

We can use fzf to create a nice gitmoji like prompt. Here is a simple bash script that does the job.
First download the [`gimojis.csv`](https://gist.github.com/Bhupesh-V/43bc0f2d8b84ea6c2ce767de56260b34) file and change the path to the csv file in the script.

```bash
#!/usr/bin/env bash

gitmoji_path="$HOME/.config/gitmojis.csv"

emoji=$(cat $gitmoji_path | fzf --prompt="Choose gitmoji: " --height 40% --reverse | awk '{print $1}')
printf "Emoji: %s\n" "$emoji"

read -erp "Enter Commit Title: " title
echo -e "Enter Commit Message (Ctrl+d when done):"
msg=$(</dev/stdin)
echo
read -erp "Issue / PR ref #: " issue_ref
if [[ "$issue_ref" ]]; then
    git commit -m "$emoji $title (#$issue_ref)" -m "$msg"
else
    git commit -m "$emoji $title" -m "$msg"
fi
```

ofc credits goes to [gitmoji](https://gitmoji.dev/) 💚️

## Preview files & directories 📂️

For files you may want to check the filetype, size & permissions.

First create a bash function like this

```bash
fino () { 
    declare filepath=${1:-$(</dev/stdin)};
    if [[ -f "$filepath" ]]; then
        echo -e "$(basename "$filepath")";
        info=$(file "$filepath" | awk -F ":" '{print $2}');
        echo -e "$info";
        ls -alh "$filepath" | awk '{print $1 "\nSize: " $5 "\nLast Modify: " $6 " " $7 " " $8}';
    fi
}
export -f fino
```

Now just use the `--preview` option in fzf.

```bash
locate -ei "$HOME" | fzf --preview "fino {}" --height 40% --reverse
```

Previewing directories may include listing its contents

```bash
# Notice the [[ -d ... ]] means only run when the path is a directory
locate -ei "$HOME" | fzf --preview "[[ -d {} ]] && tree -C {} | head -200" --height 40% --reverse
```

## Beautifying `fzf`?

fzf offers very minimal but satisfying enough features to tweak around

1. Changing pointers (default '>'). Below are some valid pointer styles
   ```bash
   fzf --prompt='Open File: ' --pointer='ᐅ'
   fzf --prompt='Open File: ' --pointer='🡆'
   fzf --prompt='Open File: ' --pointer='🠲'
   fzf --prompt='Open File: ' --pointer='⮞'
   fzf --prompt='Open File: ' --pointer='🢂'
   fzf --prompt='Open File: ' --pointer='➡'
   ```

2. Colors 💅️ (WIP)

   A full list of color rules can be found [here](https://www.mankier.com/1/fzf#Options-Display) or on `man fzf`.
   Below are some nice colorscheme combinations you might like
   ```bash
   # Inspired from ayu colorscheme Vim
   --color 'fg:#E6E1CF,fg+:#ddeeff,bg:#0F1419,pointer:#FF8400,header:#70B650,query:#FCD363'
   # Inspired from afterglow theme Vim
   --color 'fg:#E6E1CF,fg+:#ddeeff,bg:#1A1A1A,bg+:#393939,pointer:#FF8400,header:#717879'
   # Inspired from sonokai theme Vim
   --color 'fg:#E6E1CF,fg+:#ddeeff,bg:#2C2E34,bg+:#3C3E48,pointer:#EB4B48,header:#7F8490'
   # Inspired from Monokai Pro
   --color 'fg:#E6E1CF,fg+:#ddeeff,bg:#2B292E,bg+:#3D3B40,prompt:#A9DC76,pointer:#FF6188,header:#AB9DF2,query:#FFD866'
   ```

