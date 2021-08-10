# Print value of `$PATH` in readable format
**_Posted on 10 Aug, 2021_**

```bash
# might only work in bash
echo "${PATH//:/$'\n'}"
```

Substitute all occurrences of ":" in `$PATH` with a newline "\n"


#### Resources
- [search & replace - bash-hackers](https://wiki.bash-hackers.org/syntax/pe#search_and_replace)
- [bash cyberciti](https://bash.cyberciti.biz/guide/$PATH)
