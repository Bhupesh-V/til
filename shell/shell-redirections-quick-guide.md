# Shell Redirections ↔ Quick Guide

File descriptors:

- **`stdin`**  : 0
- **`stdout`** : 1
- **`stderr`** : 2


## Redirecting `stdin`

This trick can be used to take multi-line input in scripts.

```bash
#!/usr/bin/env bash

echo -e "Enter Commit Message (Ctrl+d when done):"
msg=$(</dev/stdin)
echo $msg
```

## Redirecting `stderr`

1. Use **`2>`**. Compatible with both `bash` and `sh`

## Redirecting both `stderr` & `stdout`

1. With `bash`, use `some_command &> /dev/null`
2. With `sh`,
   ```bash
   some_command > where-to-redirect 2>&1
   # or
   some_command 2>&1 > stdout_and_err
   ```
3. If you want to capture standard output/error separately,
   ```bash
   $ some_command 1>output.txt 2>error.txt
   ```
