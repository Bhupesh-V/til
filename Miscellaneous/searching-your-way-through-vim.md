# Searching your way through vim
<!-- Dec 9, 2020 -->

1. Matching a word "exactly"

`/.*\<hello world\>\&.*\<goodbye world\>/`

2. Searching between 2 words (inclusive)

`\&` allows to match two regular expression parts at the same position. To have both strings match in the same line, you need to allow for an arbitrary number of characters before the matches.
Example : `/.*red\&.*blue/`
Say you want to find how many f-strings are used in your python program the search query for that would be `f"\&.*"`

3. Search between 2 words on different lines.
   `try\_.\{-}except`
   This will highlight everything between try/except block inclusive.

Read `:help pattern.txt` for everything related to searching.
