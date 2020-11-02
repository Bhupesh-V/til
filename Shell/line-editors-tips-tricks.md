# Line Editing in Linux, Tips and Tricks

I will log various ways through which tools like `sed`, `cut` and `tr` can be used.

## `sed` 😥

- Print specific lines from a file using line numbers
  ```bash
  # print lines 12 to 22
  sed -n '12,22p' file.txt
  ```

## `tr` ➡️

- Translate (or convert) all () to [] in a textfile.
  ```bash
  tr '()' '[]'
  ```

- Translate all occurences of multiple spaces with a single space.
  ```bash
  tr -s ' '
  ```

## `cut` ✂️

- Print every 4th word (or field) from a space separated STDIN.
  ```bash
  cut -d' ' -f4
  ```
  I don't know about you but this is pretty cool.
