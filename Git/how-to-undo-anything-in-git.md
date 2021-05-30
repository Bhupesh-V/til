# How to undo anything in Git
**_Posted on 03 Apr, 2021_** 

> Posting this as a reference for my future self, so I don't have to search every time.

**Update**: Wrote [**ugit** to undo you last git command](https://github.com/Bhupesh-V/ugit)

If the reader has a better way to undo something, please edit the page and send a PR. More than happy to correct myself.


## Undo `git commit`
```bash
# undo last commit (unstage everything)
$ git reset HEAD~

# undo last commit (don't unstage everything)
$ git reset --soft HEAD^
```

## Undo most recent commit message
```bash
$ git commit --amend
# or
$ git commit --amend -m "Fixes bug #42"
```
`git commit --amend` will update and replace the most recent commit with a new commit that combines any staged changes with the contents of the previous commit. With nothing currently staged, this just rewrites the previous commit message.

## Undo `git merge`

**Not yet pushed to remote**
```bash
$ git reset --hard <commit-before-merge>

# assuming the merge was your most recent commit
$ git reset HEAD~
```

**When you have already PUSHed the merge to remote**
```bash
git revert -m 1 <merge-commit-hash>
```
git revert will make sure that a new commit is created to revert the effects of that unwanted merge. The `-m 1` option tells Git that we want to keep the parent side of the merge (which is the branch we had merged into).
Finally, also make sure to provide the correct commit hash: when using git revert, we have to specify the actual merge commit's hash.

Now, when you have fixed changes in your branch you would have to revert the revert before merging again. Read [How to revert a faulty merge](https://github.com/git/git/blob/master/Documentation/howto/revert-a-faulty-merge.txt)

```bash
$ git checkout feature
...
# commits to fix the bug.
$ git checkout master
...
$ git revert e443799
...
$ git merge feature
...
# Fix any merge conflicts introduced by the bug fix
$ git commit # commit the merge
...
$ git push
```

## Undo `git push`
```bash
$ git revert HEAD~
```

## Undo `git add`
```bash
$ git restore --staged index.html
```

## Undo most recent `git checkout`
```bash
$ git checkout -
```

## Undo `git pull`
1. Get SHA1 of state before pull using `git reflog`
2. Reset state using
   ```bash
   # WARNING: Uncommited changes will be lost
   git reset --hard <SHA1>
   ```

Optionally you can go back in time using `git reset --hard master@{"5 minutes ago"}`

## Undo accidental `git branch -D` delete

1. Use `git reflog` to get the commit SHA before you deleted the branch
   ```bash
   git reflog
   ```
2. Now if the change isn't pushed to remote, run
   ```bash
   git checkout -b branch_name <SHA1>
   ```
   Otherwise recreate the branch
   ```bash
   git branch <branchName> <SHA1>
   ```

## Stop a file from being tracked

When you committed the file previously but now realise it shouldn't have been
```bash
git rm --cached application.log
```

## Most recent `git reset` 
1. Get last good state using `git reflog`
2. Use `git reset` to reset :)
   ```bash
   git reset <COMMIT_HASH>
   ```

## Most recent `git stash pop/drop/clear` 

1. Find the lost stash,
   ```bash
   git fsck --no-progress --unreachable | grep commit | cut -d ' ' -f3 | xargs git log --oneline --merges --no-walk
   ```
2. Update the stash refs:
   ```bash
   git update-ref refs/stash "$LOST_STASH_COMMIT" --create-reflog -m "my recovered stash"
   ```

## Most recent `git stash apply`

> Make sure that diff coloring is set to _auto_ in your `.gitconfig` otherwise the command will fail with unrecognised input.

```bash
git stash show -p | git apply --reverse
```

<!-- ## Undo create `git tag` (rename a tag) -->
<!-- https://stackoverflow.com/questions/1028649/how-do-you-rename-a-git-tag -->
<!-- https://github.com/tj/git-extras/blob/master/Commands.md#git-rename-tag -->

<!-- ## Undo `git rebase` -->
<!-- https://krishansubudhi.github.io/git/2020/01/20/git-rebase-undo.html -->
<!-- https://medium.com/@shreyaWhiz/how-to-undo-a-mistaken-git-rebase-life-saver-2977ff0a0602 -->

## Undo accidental git tag delete 

> Only works for annotated tags, tags created using `git tag -a`
<!-- https://dzone.com/articles/git-tip-restore-deleted-tag -->

1. Use `git fsck` to check for dangling/unreachable commits.
   ```bash
   git fsck --unreachable | grep tag
   ```
2. Verify that its the correct tag:
   ```bash
   git cat-file -p "COMMIT_HASH"
   ```
3. Update tag refs:
   ```bash
   git update-ref refs/tags/"TAG_NAME" --create-reflog "COMMIT_HASH"
   ```
4. Tag is now restored, run `git tag -l` to verify

## Undo/Restore a file to a previous version

1. Get the commit you want to restore the file to
   ```bash
   git log --oneline <FILE>
   ```

2. Use `git restore` to restore the file :)
   ```bash
   git restore --source=<COMMIT> <FILE>
   ```

## Undo accidental file delete

**When you have not commited the changes yet**
```bash
git checkout HEAD <file-path>
```

**When commited the file delete**
1. Choose commit that deleted the file
   ```bash
   git log --diff-filter=D --oneline
   ```
2. Checkout the file
   ```bash
   git checkout <COMMIT>~1 -- <FILE>
   ```

## Undo a git merge 😟️
> Undoing a git merge is a risky business. Please proceed with caution

**When the merge has conflicts, and you want to give up**
```bash
git merge --abort
```

**When the merge is unpushed**
```bash
git reset --merge ORIG_HEAD
```
Reference `ORIG_HEAD` points to the original commit before the merge. So we are just reseting that

**When you pushed the merge commit**

1. Switch to your main/default branch
   ```bash
   git checkout main
   ```
2. Get the merge commit from git log
   ```bash
   git log --oneline
   ```
3. Revert that merge commit
   ```bash
   git revert -m 1 <COMMIT>
   ```

Also must read: [How to revert a faulty merge](https://github.com/git/git/blob/master/Documentation/howto/revert-a-faulty-merge.txt)

### Resources

- [undo-git-pull-how-to-bring-repos-to-old-state](https://stackoverflow.com/questions/1223354/undo-git-pull-how-to-bring-repos-to-old-state) 
- [git revert docs](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt--mparent-number)

