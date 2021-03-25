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

If you prefer the `locate` command instead, make sure to update your `/etc/updatedb.conf` file with following `PRUNENAMES`
```
PRUNE_BIND_MOUNTS="yes"
PRUNENAMES=".git .cache .bundle .local .config node_modules __pycache__"
PRUNEPATHS="/tmp /var/spool /media /var/lib/os-prober /var/lib/ceph /home/.ecryptfs /var/lib/schroot"
PRUNEFS="NFS nfs nfs4 rpc_pipefs afs binfmt_misc proc smbfs autofs iso9660 ncpfs coda devpts ftpfs devfs devtmpfs fuse.mfs shfs sysfs cifs lustre tmpfs usbfs udf fuse.glusterfs fuse.sshfs curlftpfs ceph fuse.ceph fuse.rozofs ecryptfs fusesmb"
```

or include any other directories you don't want like `.DS_Store` etc.
Then run `sudo updatedb` to update the mlocate database. After that you can just pipe the output to fzf.

```bash
# look for any path in you $HOME directory
locate -ei "$HOME" | fzf --height 40% --reverse
```

## Changing Directories.

If you followed the previous tip then using this is a no brainer

```bash
# faster but limited
browse "$(locate "$PWD*" | fzf --height 40% --reverse)"
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

header="Select a branch to switch to"

choice=$(git for-each-ref --format='%(refname:short)' refs/heads/* | fzf \
  --prompt="Switch branch: " \
  --height 40% --reverse
)

git switch $choice
```
