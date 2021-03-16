# Generate Feed for files inside a Git repository - Recent N files
**_Posted on 16 Mar, 2021_**

Github is nice enough to provide us with RSS feeds for latest commits in a repo but it lacks the basic thing of telling me what commit introduced a new file.
The following command will show each new path that was Added to the git history along with the commit date.

```bash
git log --no-color --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty='%ad'
```

If you just want the file names, leave the `--pretty` option empty

```bash
git log --no-color --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty=''
```

You should see something like this

```
 A   scripts/oib
 A   scripts/surf
 A   snippets/python.snippets
 A   snippets/markdown.snippets
 A   .Xmodmap
 A   codesnippets/go.md
 A   scripts/areyouok.go
 A   scripts/convert-to-gif.sh
 A   scripts/backup_as_gist.py
 ...
```

To generate recent N results use the `-n` flag

```bash
git log --no-color -n 5 --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty=''
```

If you want to follow renames as well,

```bash
git log --no-color --date=format:'%d %b, %Y' --diff-filter=AR --name-status --pretty=''
```

The magic here is done by the [`--diff-filter=A`](https://www.git-scm.com/docs/git-log#Documentation/git-log.txt---diff-filterACDMRTUXB82308203) option that only shows files that were **A**dded. I remember using this to find [birthday of README files](https://bhupesh-v.github.io/git-cake-when-is-my-readme-birthday/).

> NOTE: We are assuming that the file creation date to be the _date of commit that introduced the file_ and since its a Feed for a git repo, this should makes sense (I was born when I was committed 😁️)

Now you can easily generate a valid RSS/Atom XML file which is pretty easy to do. For reference I generate a [**json** file](https://github.com/Bhupesh-V/til/blob/master/recent_tils.json) instead to show (& automate) recent [TILs](https://github.com/Bhupesh-V/til) on my [GitHub Profile](https://github.com/Bhupesh-V)

