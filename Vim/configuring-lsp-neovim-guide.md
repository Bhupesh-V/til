# Configuring LSP on NeoVim
**_Posted on 26 May, 2021_** 

Make sure you have NeoVim version >=0.5.5 installed

## Necessary stuff

```vim
" For language server configurations
Plug 'neovim/nvim-lspconfig'
```

For autocompletion choose either of these choices both seems to be equally good

```vim
Plug 'nvim-lua/completion-nvim'
```
Or

```vim
Plug 'hrsh7th/nvim-compe'
```

For the sake of this guide I have chosen `nvim-compe`

## Installing language servers

You would have to manually install the language servers you need.

1. Install language server pack for **python** (make sure you are running latest pip and Python 3.6+)
   ```bash
   pip install 'python-language-server[all]'
   ```

2. Language server pack for go is maintained by the go team itself. Use `go get` to [install **gopls**](https://github.com/golang/tools/blob/master/gopls/README.md#installation)
   ```bash
   GO111MODULE=on go get golang.org/x/tools/gopls@latest
   ```

   Or, You can also use the [`vim-go`](https://github.com/fatih/vim-go) plug-in
   ```vim
   Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
   " run :GoInstallBinaries if setting up first time
   " this will also install the languager server for go (gopls) automatically
   ```

3. For bash, install [bash-language-server](https://github.com/bash-lsp/bash-language-server)
   ```bash
   # if you have npm installed
   npm i -g bash-language-server
   # snap
   sudo snap install bash-language-server
   ```

- To install other language servers visit [**langserver.org**](https://langserver.org/) and choose accordingly.
- After that check the [necessary config](https://github.com/neovim/nvim-lspconfig/blob/master/CONFIG.md) for neovim setup

## Configure keybindings

The following boilerplate config can be used as it is

```vim
" make completion menu more rich
set completeopt=menuone,noselect

" Use <Tab> and <S-Tab> to navigate through popup menu
inoremap <expr> <Tab>   pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

nnoremap <silent> gd <cmd>lua vim.lsp.buf.definition()<CR>
nnoremap <silent> gD <cmd>lua vim.lsp.buf.declaration()<CR>
nnoremap <silent> gr <cmd>lua vim.lsp.buf.references()<CR>
nnoremap <silent> gi <cmd>lua vim.lsp.buf.implementation()<CR>
nnoremap <silent> gh <cmd>lua vim.lsp.buf.hover()<CR>
nnoremap <silent> <C-k> <cmd>lua vim.lsp.buf.signature_help()<CR>
nnoremap <silent> <C-n> <cmd>lua vim.lsp.diagnostic.goto_prev()<CR>
nnoremap <silent> <C-p> <cmd>lua vim.lsp.diagnostic.goto_next()<CR>

autocmd BufWritePre *go,*.py lua vim.lsp.buf.formatting_sync(nil, 100)
```

## Setup `nvim-lspconfig`

```vim
" Initialise server packs
lua <<EOF
require'lspconfig'.gopls.setup{}
require'lspconfig'.pyls.setup{}
require'lspconfig'.bashls.setup{}
EOF
```

## Setup `nvim-compe`

```vim
let g:compe = {}
let g:compe.enabled = v:true
let g:compe.autocomplete = v:true
let g:compe.debug = v:false
let g:compe.min_length = 1
let g:compe.preselect = 'enable'
let g:compe.throttle_time = 80
let g:compe.source_timeout = 200
let g:compe.resolve_timeout = 800
let g:compe.incomplete_delay = 400
let g:compe.max_abbr_width = 100
let g:compe.max_kind_width = 100
let g:compe.max_menu_width = 100
let g:compe.documentation = v:true

let g:compe.source = {}
let g:compe.source.path = v:true
let g:compe.source.buffer = v:true
let g:compe.source.calc = v:true
let g:compe.source.nvim_lsp = v:true
let g:compe.source.nvim_lua = v:true
let g:compe.source.vsnip = v:true
let g:compe.source.ultisnips = v:true
let g:compe.source.luasnip = v:true
let g:compe.source.emoji = v:true

```

> Notice: If you are embedding lua code in your vimscript config, use the following heredoc

```
lua <<EOF
-- [[ this is lua comment ]]
   lua code
   ...
EOF
```

## Spicy Stuff

Below are some plugins which spice up the neovim lsp experience

### [lspsaga.nvim](https://github.com/glepnir/lspsaga.nvim)

> Richer UI for LSP

```vim
" lsp provider to find the cursor word definition and reference
nnoremap <silent> gh <cmd>lua require'lspsaga.provider'.lsp_finder()<CR>
" preview definition
nnoremap <silent> gd <cmd>lua require'lspsaga.provider'.preview_definition()<CR>
" show hover doc
nnoremap <silent> K <cmd>lua require('lspsaga.hover').render_hover_doc()<CR>
" scroll down hover doc or scroll in definition preview
nnoremap <silent> <C-f> <cmd>lua require('lspsaga.action').smart_scroll_with_saga(1)<CR>
" scroll up hover doc
nnoremap <silent> <C-b> <cmd>lua require('lspsaga.action').smart_scroll_with_saga(-1)<CR>
" code action
nnoremap <silent><leader>ca <cmd>lua require('lspsaga.codeaction').code_action()<CR>
vnoremap <silent><leader>ca :<C-U>lua require('lspsaga.codeaction').range_code_action()<CR>
```

### [lsp_signature](https://github.com/ray-x/lsp_signature.nvim)

> Show function signature help as you type

```vim
lua <<EOF
require'lspconfig'.gopls.setup {
    on_attach = function(client)
    require 'lsp_signature'.on_attach(client)
end,
}
EOF
```

## Resources
- [nvim-lspconfig github](https://github.com/neovim/nvim-lspconfig)
- [nvim-compe github](https://github.com/hrsh7th/nvim-compe)
- [Native LSP in NeoVim - Chris@Machine](https://www.chrisatmachine.com/Neovim/27-native-lsp/)
