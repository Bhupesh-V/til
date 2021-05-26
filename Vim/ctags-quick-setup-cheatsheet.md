# ctags in Vim - Quick Cheatsheet
<!-- **_Posted on 26 May, 2021_** -->

> Consider using modern stuff like LSP over ctags

## Setup

1. Install [universal-ctags](https://github.com/universal-ctags/ctags). Support languages like C/C++, Markdown, HTML, Java, Go, Javascript, Python, Shell scripts
   ```bash
   # Linux
   sudo snap install universal-ctags
   # Mac
   brew install --HEAD universal-ctags/universal-ctags/universal-ctags
   ```
2. Run the command `ctags -R *` inside project folder
3. Optionally Install fzf.vim which offers fuzzy searching over tags available using `:Tags` command

## Usage

- `Ctrl + ]`: Jump to tag underneath cursor
- `Ctrl + t`: Jump back up in tag stack
- `Ctrl + W Ctrl + ]` - Open the definition in a horizontal split
