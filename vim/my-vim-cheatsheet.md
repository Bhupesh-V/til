# My Vim Cheatsheet
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

> Update: I started using vim "actively" from Nov 12, 2020 and it has now been 1 month complete in Vim & I don't think I am moving to another text editor in future.

For starters I use **neovim** (v0.4.4).

All my Plugins & Colorschemes are listed in my [**dotfiles**](https://github.com/Bhupesh-V/.Varshney#initvim-or-vimrc)

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
4. Use **`==`** in Visual Mode to fix line indent.
5. When in command mode (:), use <kbd>Ctrl</kbd> + <kbd>f</kbd> to browse through your command history, live edit any command and hit enter to run it (the quick fix window).
6. Use **`:resize 60`** to resize windows horizontally or **`:vertical resize 60`** for vertical resizing. Also signed values can be used like +5, -2.
7. Use **`:right`**, **`:left`** or **`:center`** to align text. Assuming width of document is `textwidth` (default is 80). You can also specify arguments for e.g `:center 100` will move the start of line to _100th_ column.
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
14. If you have spell-checking (`:set spell`) enabled use `zg` to exclude certain words from being reported as misspelled. This adds the words to your own list of words called a _spellfile_. On NeoVim this fill is created automatically, although you can do it manually.
    ```bash
    mkdir -p ~/.vim/spell/
    ```
    then in `vimrc`
    ```vim
    set spellfile=~/.vim/spell/en.utf-8.add
    ```
15. Use `q:` to open command line history or `Ctrl + f` when already in command mode
16. Use `q/` to open search history, this will list all the things you searched using search mode `/`. Press `i` to change anything and \<CR\> to execute again.
17. To quickly jump to function definition or variable assignments under cursor use `gd`(local declaration) or `gD`(global declaration)
18. To reselect the last visual selection use `gv`.
19. When in visual mode use `gU` to make text uppercase & `gu` to lowercase.

### Code Folding

It helps you view only a selected range of text. (Read `:h usr_28.txt` for a quick overview)

Quick settings to put in vimrc/init.vimrc

```vim
set foldmethod=indent
set foldcolumn=2
```

> You can also setup foldmethod [based on file type](https://github.com/Bhupesh-V/.Varshney/blob/fa65398dedcb12831d20c6ac4762471bc9eea66c/init.vim#L173-L178
)

- **za**: Toggle code folding.
- **zR**: Open all folds.
- **zM**: Close all folds.
- **zo**: Open current fold.
- **zc**: Close current fold.


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

- **f** : find next
- **F** : find backward
- **t** : find next char & place cursor before
- **T** : find next char & place cursor before backward
- **;** : go to the next occurrence of f/t
- **,** : go to previous occurrence of f/t


### Completions

Use <kbd>Ctrl</kbd> + <kbd>x</kbd> +

1. <kbd>f</kbd>	= File name completion
2. <kbd>l</kbd>	= Whole line completion (context aware, handy if you are copy pasting a previously typed line)
3. <kbd>i</kbd>	= Keywords in current & included file ("include" means when you import or #include)
4. <kbd>s</kbd>	= Spelling suggestions
5. <kbd>k</kbd>	= Keywords from dictionary. For this to work add `set dictionary+=/usr/share/dict/words` to your vimrc

> use `:help ins-completion` to see more such completions


### Registers

Take registers as "special vim storage locations". There are exactly 21 + 26 registers which store different kind of stuff

> In command mode use `:di` or `:reg` to display contents of all these registers. Do `h registers` to read manual

**10 flavors of registers**

| Register Name        | Register           | Description|
|:-------------:|:-------------:|:----------------|
| The unnamed register | `""` | Last yank/delete or change |
| 10 numbered registers |  `"0` to `"9` | **0** store the most recent yank<br> **1** stores the most recent delete<br>With successive deletes/changes vim shifts the contents of register 1 to 2, 2 to 3 & so on.|
| The small delete register |  `"-` | Text from commands that delete less than one line|
| 26 named registers |  `"a` to `"z` or `"A` to `"Z` | Add whatever you want, lowercase for clearing previous content. Uppercase for appending|
| 3 read only registers |  `":`, `".` & `"%` | **:** contains the most recent executed command line, use @:<br> **%** contains name of current file<br> **.** contains the last inserted text|
| Alternate buffer register |  `"#` | The name of the alternate file for the current window|
| The Expression register |  `"=` | Evaluate expression press \<C-R\> then = |
| The black hole register |  `"_` | What goes in black hole, stays in black hole |
| The Selection registers |  `"*` & `"+` | Store & retrieve selected text from GUIs (read `quotestar` & `quoteplus`)|
| Last search pattern register |  `"/` |The most recent search-pattern|

### File Browsing

Vim has a default file browser called netrw, below are some handy tips that will help:

1. **R** : rename a file/directory.
2. **qf** : Show file info.
3. **x** : open file in associated program, use it open media files like images.
4. **Ctrl + l** : refresh netrw, Opens a new buffer. Use `:e .` instead.
5. **d** : Make a new directory.
6. **gh** : toggle display of hidden files.
7. **D** : Delete a file/directory (Doesn't work on non-empty directories).

### `Ex` mode

It let's you run commands repetitively without using `:`.

Use `Q` to enter into Ex mode, `vi` or `visual` to go back.

The Ex mode in Vim is quite underrated in 2020 since we have a `:term` but learning about it can be quite helpful sometimes.


---
I will only add stuff here when I start using it or use it for the first time.

