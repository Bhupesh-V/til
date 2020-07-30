# Alternative to 'ls' commnand
<!-- 22 July 2020 -->
the bash builtin `echo` can be used to list contents of a directory.

```bash
echo *
```

List all files that start with letter 'i'.

```bash
echo i*
```

## How

The character * serves as a "wild card" for filename expansion in globbing. By itself, it matches every filename in a given directory.

## Resource
- [globbing](https://www.tldp.org/LDP/abs/html/globbingref.html)