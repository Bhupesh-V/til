# My vim cheatsheet
<!-- 14 June, 2020 -->
I have started transitioning slowly to lightweight editors, because my low system specifications.
And what better than `vim`, so I will start logging interesting things I learn here.

For starters I use **neovim**.
(PS: I will write this TIL through vim only :)

### How to install plugins
1. Open up the `~/.config/nvim/init.vim` file add the plugin.
```
call plug#begin()
Plug 'roxma/nvim-completion-manager'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
call plug#end()% 
```

2. Open nvim, use `:PlugInstall` to install the new plugins.

### Some nvim specifc shortcuts

- <kbd>E</kbd> - to go back the directory after opening a file.
- </kbd>NERDTree</kbd> - to start the Tree like menu.
- When in NERDTree use </kbd>m</kbd> for creating a file.

### Vim Commands

1. <kbd>i</kbd> : to come in Insert/Editing Mode.
2. <kbd>Esc</kbd> : for command mode. 


---
I will only add stuff here when I start using it daily.

