# My vim cheatsheet
<!-- 14 June, 2020 -->
I have started transitioning slowly to lightweight editors, because of my low system configuration.
And what can better than `vim`, so I will start logging interesting things I learn here.

For starters I use **neovim**.
(PS: I will write this TIL through vim only :)

### How to install plugins
1. Open up the `~/.config/nvim/init.vim` file add the plugin.

My init file
```
call plug#begin()
Plug 'roxma/nvim-completion-manager'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'gilgigilgil/anderson.vim'
call plug#end()

vnoremap <C-c> "+y
map <C-v> "+p
```

2. Open nvim, use `:PlugInstall` to install the new plugins.

### Some nvim specifc shortcuts

- <kbd>E</kbd> - to go back the directory after opening a file.
- </kbd>:NERDTree</kbd> - to start the Tree like menu.
- When in NERDTree use </kbd>m</kbd> for creating a file.

### Vim Commands

1. `:i` : to come in Insert/Editing Mode.
2. <kbd>Esc</kbd> : for command mode. 
3. `:V` : to enable visual mode, use <kbd>shift</kbd> and arrow keys to select text.
4. `:"+y` : for yanking(copying) text from vim to system's clipboard (tested on Ubuntu 18, might not work on other systems. Search according to your system).
5. `:nohlsearch` : for clearing search highlighting.
6. `:set nu` : to enable Line numbers(left margin).
7. `:"+p` : to paste from system's clipboard (I have added key bindings for copy/paste in my nvim config file).
8. `:u` : Undo latest changes in vim.
9. <kbd>Ctrl + ws</kbd> : Split Windows horizontally.
10. <kbd>Ctrl + wv</kbd> : Split Windows vertically.
11. <kbd>Ctrl + ww</kbd> : Switch between Windows.
12. <kbd>Ctrl + wq</kbd> : Quit Window.
13. `:earlier N` : Time travel in past N seconds.
14. `:later N` : Time tavel in future N seconds.
---
I will only add stuff here when I start using it or use it for the first time.

