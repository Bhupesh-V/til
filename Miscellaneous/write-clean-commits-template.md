# Writing Cleaner Commits - Template
<!--20 Nov 2019 -->
Writing cleaner commits is hard, so I use this template which makes me a pro 😅

```text
# If applied, this commit will...
# [Add/Fix/Remove/Update/Refactor/Document] [issue #id] [summary]


# Why is it necessary? (Bug fix, feature, improvements?)
-
# How does the change address the issue? 
-
# What side effects does this change have?
-

```

##### OR

```text
# If applied, this commit will...
# [Add/Fix/Remove/Update/Refactor/Document]

# Reference any issue number here
- This fixes #454
# Why is it necessary? (Bug fix, feature, improvements?)
-
# How does the change address the issue? 
-
```

## How ?
You have to configure Git to use the above template file (for example, `.gitmessage` in your home directory), then create the template file by running.

```bash
git config --global commit.template ~/.gitmessage
subl ~/.gitmessage
```

This will invoke sublime with the template (use `code` if you use VSCode) Now copy paste the above template, hit save and your are done.

Now when commiting changes instead of using `git commit -m ""`, Use `git commit` this will invoke the commit template which you already set.


### Resources

- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Git commit practices your future self will thank you for](https://victoria.dev/blog/git-commit-practices-your-future-self-will-thank-you-for/)