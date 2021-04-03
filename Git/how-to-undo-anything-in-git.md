# How to undo anything in Git
**_Posted on 03 Apr, 2021_** 

> Posting this as a reference for my future self, so I don't have to search every time.

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
```bash
$ git reset --hard <commit-before-merge>

# when you don't have the hash of the commit before the merge at hand
$ git reset --hard HEAD~1

# when you have already PUSHed the merge to remote
$ git revert -m 1 <merge-commit-hash>
```
git revert will make sure that a new commit is created to revert the effects of that unwanted merge. The `-m 1` option tells Git that we want to keep the parent side of the merge (which is the branch we had merged into).
Finally, also make sure to provide the correct commit hash: when using git revert, we have to specify the actual merge commit's hash.


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

## Stop a file from being tracked
When you committed the file previously but now I realise it shouldn't have been
```bash
git rm --cached application.log
```

<!-- ## Most recent `git reset` -->
<!-- ## Most recent `git stash pop` -->
