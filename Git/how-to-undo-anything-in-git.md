# How to undo anything in Git
**_Posted on 03 Apr, 2021_** 

> Posting this as a reference for my future self, so I don't have to search every time.

**Update**: Wrote a [tool to undo you last command in Git](https://github.com/Bhupesh-V/ugit)

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
git commit --amend will update and replace the most recent commit with a new commit that combines any staged changes with the contents of the previous commit. With nothing currently staged, this just rewrites the previous commit message.

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

1. Use `git reflog` to get the SHA before you delete the branch
   ```bash
   git reflog
   ```
2. Now if the change isn't pushed to remote, run
   ```bash
   git checkout -b branch_name <SHA1>
   ```
   Otherwise recreate branch
   ```bash
   git branch branchName <SHA1>
   ```

## Stop a file from being tracked

When you committed the file previously but now I realise it shouldn't have been
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
