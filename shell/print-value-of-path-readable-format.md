# Print value of `$PATH` in readable format
**_Posted on 10 Aug, 2021_**

```bash
# for bash
echo "${PATH//:/$'\n'}"
# for zsh omit the $ char
echo "${PATH//:/'\n'}"
```

Substitute all occurrences of ":" in `$PATH` with a newline "\n"

- The `$'...'` way of quoting a string allows us to use special characters such as tab (`\t`) safely.


#### Resources
- [search & replace - bash-hackers](https://wiki.bash-hackers.org/syntax/pe#search_and_replace)
- [bash cyberciti](https://bash.cyberciti.biz/guide/$PATH)
