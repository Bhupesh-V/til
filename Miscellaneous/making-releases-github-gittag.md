# Releases on GitHub
<!-- 2 Jul 2019 -->
Git tagging is generally used to release software on github.
Here are some basic git commands for tagging.

- To tag specific points of your repo. Run this when you commit something.
  ```shell
  git tag -a v1.4 -m "my version 1.4"
  ```

- To lists all the tags of your repo.
  ```bash
  git tag
  ```

- To tag specific commits.
  ```bash
  git tag -a v1.4 9fceb02
  ```

- To push tags on GitHub.
  ```bash
  git push origin v1.4
  ```