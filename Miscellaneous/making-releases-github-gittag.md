# Releases on GitHub
<!-- 2 Jul 2019 -->
Git tagging is generally used to release software on github.
Here are some basic git commands to use git tagging.

```bash
git tag -a v1.4 -m "my version 1.4"
```
- It is used to tag specific points of your repo.
Run this when you commit something.

```bash
git tag
```
- It lists all the tags of your repo.

```bash
git tag -a v1.4 9fceb02
```
- To tag specific commits.

```bash
git push origin v1.4
```
- To push tags on GitHub.
