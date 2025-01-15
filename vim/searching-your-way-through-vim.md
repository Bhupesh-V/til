# Searching your way through vim
<!-- Dec 9, 2020 -->

## Matching a word "exactly"
`/\<hello world\>/`

`\<` and `\>` mark the start and end of a whole word resp.

## Searching between 2 words (inclusive)
`/red\&.*blue/`

This will highlight everything b/w "red" and "blue" on the same line.

`\&` also called as "Branch" matches the last pattern but **only if** all the preceding patterns match at the same position 

Example: Find **f-strings** `f"\&.*"`

## Search between 2 words on different lines.
`hello\_.*world`

This will highlight everything between hello world.

Example: Find **try/catch** block `hello\_.*world`

`"\_.*except"` matches all text from the current position to the last occurrence of "except" in the file.


> Read `:help pattern.txt` for everything related to pattern searching.
