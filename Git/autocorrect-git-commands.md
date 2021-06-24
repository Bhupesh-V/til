# Auto-correct Git commands

> [**help.autocorrect**](https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpautoCorrect) docs

Git offers correcting misspelled git commands within a timed interval

```bash
# run the correct command after 0.7 seconds
git config --global help.autocorrect 7
```

Or in your global `.gitconfig`

```gitconfig
[help]
        # default 0
        # negative value to run correct command immediately
	autocorrect = 7
```

Now test it by running `git sttus`

```
$ git sttus
WARNING: You called a Git command named 'sttus', which does not exist.
Continuing in 0.7 seconds, assuming that you meant 'status'.
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Git/autocorrect-git-commands.md

no changes added to commit (use "git add" and/or "git commit -a")

```
