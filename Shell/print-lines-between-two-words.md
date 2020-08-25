# Print lines between 2 words
<!-- 24 Aug 2020 -->

You may arrive in a situation where you may want to "extract" out text between two words.
For example to view the latest changelog (where `x.x.x` is the latest version) in a [CHANGELOG.md](https://github.com/Bhupesh-V/dotman/blob/master/CHANGELOG.md) file.

### Using `sed`

```bash
sed -n -e '/x.x.x/,/0.1.0/ p' CHANGELOG.md | sed -e '1d;$d'
```

`sed -e '1d;$d'` removes the first & last line.

### Using `awk`

```bash
awk '/x.x.x/,/0.1.0/' CHANGELOG.md | awk 'NR>2 {print last} {last=$0}'
```

`awk 'NR>2 {print last} {last=$0}'` removes the first & last line.

> NOTE: `NR` means which Line number is being processed

#### Resources

- [How to show lines after each grep match until other specific match?](https://unix.stackexchange.com/questions/21076/how-to-show-lines-after-each-grep-match-until-other-specific-match)
- [What is the easiest way to remove 1st and last line from file with awk?](https://stackoverflow.com/questions/15856733/what-is-the-easiest-way-to-remove-1st-and-last-line-from-file-with-awk)