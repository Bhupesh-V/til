# grep cheatsheet
**_Posted on 15 Dec, 2021_**

Will be logging here various uses-cases of `grep`


1. Print anything between 2 patterns
   ```bash
   # print all function names inside a python files
   grep -o -P '(?<=def ).*?(?=\()' demo.py
   ```

2. Ignore more than one pattern from search
   ```bash
   # ignore json and py files from output
   # -v means invert-match
   # -E activates extended regexp patterns (egrep). Allows use of symbols like +, |, ?
   ls | grep -Ev '(.json|.py)'
   # this is same as
   ls | grep -v -e .json -e .py
   ```
