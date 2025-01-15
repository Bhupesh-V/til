# Convert bulleted/unordered lists to numbered lists

1. Visually select the lines.
2. Enter command mode & run
   ```vim
   :'<,'>s/*/\=line('.') - line("'<") + 1 . '.'
   ```
   Replace * with - if you are using markdown
