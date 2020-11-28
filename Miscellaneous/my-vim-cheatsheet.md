# My Vim cheatsheet
<!-- 14 June, 2020 -->

<pre>                         
 _______ _______ _______ 
|\     /|\     /|\     /|
| +---+ | +---+ | +---+ |
| |   | | |   | | |   | |
| |v  | | |i  | | |m  | |
| +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|
                         
</pre>

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
- **`dd`** Delete current line.
- **`cc`** delete current line and switch to insert mode.
- **`C`** delete everything from the cursor position to the EOL.

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
2. Use `*` to select all its occurrences. 
3. Hit <kbd>Esc</kbd> and use **`:%s//<replace-word>/`** to replace all the selected words.
   > `:nohlsearch` : for clearing search highlighting.
   Also read (:h usr_12.txt), section 12.2 for a nice overview on search.

   When in search mode instead of hitting Enter use `Ctrl + g` and `Ctrl + t` to traverse matches while still being in search mode.

## Intermediate Stuff

1. **`:earlier N`** : Time travel in past N seconds.
2. **`:later N`** : Time travel in future N seconds.
3. **`:echo $MYVIMRC`** : to view location of your default `.vimrc` file.
4. Use `==` in Visual Mode to fix line indent.
5. When in command mode (:), use <kbd>Ctrl</kbd> + <kbd>f</kbd> to browse through your command history, live edit any command and hit enter to run it (the quick fix window).
6. Use **`:resize 60`** to resize windows horizontally or **`:vertical resize 60`** for vertical resizing. Also signed values can be used like +5, -2.
7. Use **`:right`**, **`:left`** or **`:center`** to align text. Assuming width of document is `textwidth` (default is 80). You can also specify arguments for e.g `:center 100` will move the start of line to 100th column.
8. To list all your active/inactive buffers, use **`:buffers`** in command mode. You can switch to a buffer by providing the buffer name, `:buffer <TAB>` to see all buffers.
9. Use `:verb map <key>` to check which key is mapped to what operation. Useful when debugging your mappings and differentiating them from that of a plugin.
   > Read help for checking key notations `:h key-notation`
10. Use vim's `wildignore` setting to exclude searching for files and directories according to your project. For e.g for python projects this could look like
    ```vim
    set wildignore+=*/.git/*,*/site-packages/*,*/lib/*,*/bin/*,*.pyc
    ```
    This should exclude searching through your virtual environments [Read manual `:h 'wildignore'`].
    Another handy trick is to exclude media files from appearing in search by excluding them as well.
    ```vim
    set wildignore+=*.jpg,*.bmp,*.gif,*.png,*.jpeg,*.avi,*.mp4,*.mkv,*.pdf,*.odt
    ```
11. `:syntax` will output all highlight groups for syntax highlighting of the current open file. It can come handy when you are writing your own colorscheme.
12. Scrolling 2 or more windows together. When in multiple windows (or splits), you can use `scrollbind`.
    Pick one window then `:set scb`, pick another window `:set scb` for disabling use `:set noscb`
13. To search for pattern in vim help text use `:helpgrep` or `:helpg`


### Navigation

- **w** jump through beginning of words in a line
- **e** jump to end of words in a line
- **b** to move backward
- **H** jump to top of text under screen (not to be confused with top of file).
- **M** jump to middle
- **L** jump to bottom
- **gg** go to top of file
- **GG** go to end of file
- **0** go to beginning of line
- **$** go to end of current line
- **^** go to first character in a line
- **g_** go to last character of the line
- **zb** put current line at bottom of screen
- **zt** put current line at top of screen
- **Ctrl+f** scroll down 1 page
- **Ctrl+b** scroll up 1 page

**Character Wise**

f - find next
F - find backward
t - find next char & place cursor before
T - find next char & place cursor before backward
; - go to the next occurrence of f/t
, - go to previous occurrence of f/t


### Completions

Use <kbd>Ctrl</kbd> + <kbd>x</kbd> +

1. <kbd>f</kbd>	= File name completion
2. <kbd>l</kbd>	= Whole line completion (context aware, handy if you are copy pasting a previously typed line)
3. <kbd>i</kbd>	= Keywords in current & included file ("include" means when you import or #include)
4. <kbd>s</kbd>	= Spelling suggestions
5. <kbd>k</kbd>	= Keywords from dictionary. For this to work add `set dictionary+=/usr/share/dict/words` to your vimrc

> use `:help ins-completion` to see more such completions


### Registers

Take registers as "special vim storage locations". There are exactly 21 registers which store different kind of stuff, from these 4 registers are read-only.
In command mode use `:di` or `:reg` to display contents of all these registers. Do `h registers` to read the docs

---
I will only add stuff here when I start using it or use it for the first time.

