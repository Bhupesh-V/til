# My vim cheatsheet
<!-- 14 June, 2020 -->
I have started transitioning slowly to lightweight editors, because of my low system configuration.
And what can be better than `vim`. I will keep a log of things I learn in the process.

For starters I use **neovim** (v0.2.2).
(PS: I will write this TIL through vim only :)

All my Plugins & Colorschemes are listed in my [dotfiles](https://github.com/Bhupesh-V/.Varshney#initvim-or-vimrc)

## Super Basic Stuff

> Some must know stuff filtered from the vast array of vim things.

### Editing

- **`i`** insert text before the cursor position
- **`a`** append text after the cursor position (my advice, always use this instead of `i`)
- **`A`** append text at end of line
- **`o`** open a new line after current line
- **`O`** open a new line before current line
- **`x`** delete character under cursor
- **`D`** delete until the end of line
- **`r`** replace the character under cursor
- **`R`** replace stuff until we want

## Basic Stuff

### Undo/Redo/Repeat

- <kbd>u</kbd> : Undo latest changes in vim.
- <kbd>Ctrl</kbd> + <kbd>r</kbd> : to redo
- <kbd>.</kbd> : repeat last change in vim.

### Cut/Copy/Paste

> I felt like a rookie when I used to search this, anyways here is how you do it:

1. Enable visual mode by pressing `v`.
2. Use arrow keys to select text.
3. Use <kbd>d</kbd> to Cut. OR
4. Use <kbd>y</kbd> to yank (copy) text (only inside vim)
   > `:"+y` : for yanking(copying) text to system's clipboard.
5. Use <kbd>p</kbd> to paste after the cursor position or <kbd>P</kbd> to paste before the cursor.
   > `:"+p` : to paste from system's clipboard 
   
### Search & Replace

1. Move your cursor to the desired word
2. Use `*` to select all its occurences. 
3. Hit <kbd>Esc</kbd> and use `:%s//<replace-word>` to replace all the selcted words.
   > `:nohlsearch` : for clearing search highlighting.

## Intermediate Stuff
<!--
7. <kbd>Ctrl</kbd> + <kbd>ws</kbd>: Split Windows horizontally.
9. <kbd>Ctrl</kbd> + <kbd>wv</kbd>: Split Windows vertically.
10. <kbd>Ctrl</kbd> + <kbd>ww</kbd>: Switch between Windows.
11. <kbd>Ctrl</kbd> + <kbd>wq</kbd>: Quit Window.-->
1. `:earlier N` : Time travel in past N seconds.
2. `:later N` : Time tavel in future N seconds.
3. `:echo $MYVIMRC`: to view location of your default `.vimrc` file.
4. Use `==` in Visual Mode to fix line indent.
5. `:Ex `: press Tab to cycle through directories inside current dir.

---
I will only add stuff here when I start using it or use it for the first time.

