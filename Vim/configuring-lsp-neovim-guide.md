# Configuring LSP on NeoVim
<!-- **_Posted on 26 May, 2021_** -->

1. Instal [vim-lsc](https://github.com/natebosch/vim-lsc) client
   ```vim
   Plug 'natebosch/vim-lsc'
   ```

2. Install language server pack for python
   ```bash
   pip3 install python-lsp-server[all]
   ```

3. Install `vim-go` plug-in
   ```vim
   Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
   " run :GoInstallBinaries if setting up first time
   " this will also install the languager server for go (gopls) automatically
   ```
   [Read Docs](https://github.com/golang/tools/blob/master/gopls/README.md#installation)


## Setup `vimrc`

```vim
set shortmess-=F
let g:lsc_server_commands = {
            \ 'python': 'pylsp',
            \  "go": {
            \    "command": "gopls serve",
            \    "log_level": -1,
            \    "suppress_stderr": v:true,
            \  },
            \}

" Use all the defaults (recommended):
let g:lsc_auto_map = v:true

" Apply the defaults with a few overrides:
let g:lsc_auto_map = {'defaults': v:true, 'FindReferences': '<leader>r'}

" Setting a value to a blank string leaves that command unmapped:
let g:lsc_auto_map = {'defaults': v:true, 'FindImplementations': ''}

" ... or set only the commands you want mapped without defaults.
" Complete default mappings are:
let g:lsc_auto_map = {
            \ 'GoToDefinition': '<C-]>',
            \ 'GoToDefinitionSplit': ['<C-W>]', '<C-W><C-]>'],
            \ 'FindReferences': 'gr',
            \ 'NextReference': '<C-n>',
            \ 'PreviousReference': '<C-p>',
            \ 'FindImplementations': 'gI',
            \ 'FindCodeActions': 'ga',
            \ 'Rename': 'gR',
            \ 'ShowHover': v:true,
            \ 'DocumentSymbol': 'go',
            \ 'WorkspaceSymbol': 'gS',
            \ 'SignatureHelp': 'gm',
            \ 'Completion': 'omnifunc',
            \}
" }}}
```
