# Find default git branch name
<!-- 25 July 2020 -->
```bash
git remote show origin | awk '/HEAD/ {print $3}'
```
