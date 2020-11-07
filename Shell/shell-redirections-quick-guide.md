# Shell Redirections ↔ Quick Guide

File descriptors:

- **`stdin`**  : 0
- **`stdout`** : 1
- **`stderr`** : 2


## Redirecting `stderr`

1. Use **`2>`**. Compatible with both `bash` and `sh`

## Redirecting both `stderr` & `stdout`

1. With `bash`, use **`&>`**
2. With `sh`, use **`> where-to-redirect 2>&1`**