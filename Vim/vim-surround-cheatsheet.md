# vim surround: quick cheatsheet
<!-- 27 Dec, 2020 -->

## Adding `ys` (_you surround_)

> `ys` takes a valid vim motion or text object as first argument

- `ysiw"`  : surround inner word with "
- `yss]`   : surround current line with ]
- `ys2aw*` : add * around 2 words 

**The `vS` mapping**

- `vS"`    : visually surround selected text with "

**Spicy Stuff**

- `yswt` : prompt & surround with a html tag
> If a t or < is specified, Vim prompts for an HTML/XML tag to insert (also supports adding attributes)

- `yswf` : prompt & surround with a function call
> If a f is specified, Vim prompts for an function name to insert (use F to add space around ())

## Changing `cs` (_change surround_)

> Takes 2 arguments a _target_ to replace & a _replacement_ character

- `cs])`    : change surrounding [] with ()
- `cst<h3>` : change surrounding html tag with h3

## Deleting `ds` (_delete surround_)

- `ds"` : delete surrounding "
- `dst` : delete surrounding tag (HTML)

Do `:helpg surround` for more docs.

Thanks tpope!
