# Sum column values in Vim

1. Visually select your column
2. Enter into command mode & enter
   ```vim
   :'<,'>!awk '{print; sum+=$1}; END {print "Total: "sum}'
   ```
