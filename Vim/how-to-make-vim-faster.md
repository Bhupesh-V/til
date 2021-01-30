# How to make Vim faster ⚡️
<!-- 30 Jan, 2021 -->

Apart from not loading shit ton of plugins, there are some other tricks that can be used to make the Vim more faster:

1. `set noswapfile`
   If you are a single user on your system, you probably don't need swap files.

2. `set lazyredraw`
   When this option is set, the screen will not be redrawn while executing macros, registers and other commands that have not been typed.

3. `set shada=NONE` (NeoVim) or `set viminfo=NONE` (Vanilla Vim)
   The shada or viminfo file is used to store a lot of things like command line history, marks, input-line history, search history.
   Disabling this for real dev work won't be a wise choice but it can be a life-saver if you are using Vim over SSH.

