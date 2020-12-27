# Line Editors in Linux, Tips and Tricks

I will log various ways through which tools like `sed`, `cut` and `tr` can be used.

## `sed` 😥

- Print specific lines from a file using line numbers.
  ```bash
  # print lines 12 to 22
  sed -n '12,22p' file.txt
  ```

- Omit first line of output.
  ```bash
  sed -n '1!p'
  ```

- Omit last line of file.
  ```bash
  sed '$d' file.txt
  ```

- Print everything after a _pattern_ (inclusive).
  ```bash
  sed -n '/pattern/,$ p' file.txt
  ```

- Print everything before a _pattern_ (inclusive).
  ```bash
  sed -n '1,/pattern/ p' file.txt
  ```

## `tr` ➡️

- Translate (or convert) all () to [] in a text file.
  ```bash
  tr '()' '[]'
  ```

- Translate all occurrences of multiple spaces with a single space.
  ```bash
  tr -s ' '
  ```

## `cut` ✂️

- Print every 4th word (or field) from a space separated STDIN.
  ```bash
  cut -d' ' -f4
  ```
  I don't know about you but this is pretty cool.


## `awk`

- Don't print first line of file
  ```bash
  awk NR\>1 file.txt
  ```

