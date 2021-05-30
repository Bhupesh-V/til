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

