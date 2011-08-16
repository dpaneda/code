set expandtab
set tabstop=4
set sw=4
set softtabstop=4
set autoindent
set shiftround
set background=dark

"Color scheme af in colors dir
"colorscheme af
syntax on

"Increases compatability for
"vims where ftplugin might
"be turned off.
filetype plugin on

set tw=80
set formatoptions-=t

" show tab chars with ...>
" set list listchars=tab:»·,trail:·

" show line numbers
set number

set history=100

" show a full list when hitting tab
" looking for files.
set wildmode=list:longest,full
set showmode
set showcmd

filetype on

autocmd FileType c,cpp,slang set cindent

autocmd FileType perl set smartindent

autocmd FileType css set smartindent

autocmd FileType xsd,xml filetype indent on

autocmd FileType html,css set noexpandtab tabstop=2

autocmd FileType make set noexpandtab shiftwidth=8

"Auto Complete <c-x><c-o>
autocmd FileType php set omnifunc=phpcomplete#CompletePHP
autocmd FileType c set omnifunc=ccomplete#Complete

" Delete trailing white space and ^M chars open/save
" autocmd FileType php autocmd BufWritePre <buffer> :call setline(1,map(getline(1,"$"),'substitute(v:val,"\[ \t\r]\\+$","","")'))
" autocmd FileType php autocmd BufEnter <buffer> :call setline(1,map(getline(1,"$"),'substitute(v:val,"\[ \t\r]\\+$","","")'))

set incsearch
" Ignore case on searches
set ignorecase
" only case is ignored on all lowercase searches
set smartcase

" Keep context on top and bottom of cursor
set scrolloff=5

set backspace=eol,start,indent
"inoremap <Tab> <C-T>
"inoremap <S-Tab> <C-D>

"come back to the same location after editing
set viminfo='10,\"100,:20,%,n~/.viminfo
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif 

:setl makeprg=php
:set errorformat=%m\ in\ %f\ on\ line\ %l

set tags=./tags,./../tags,./../../tags,./../../../tags,./../../../../tags,./../../../../../tags,./../../../../../../tags,./../../../../../../../tags,./../../../../../../../../tags,./TAGS,./../TAGS,./../../TAGS,./../../../TAGS,./../../../../TAGS,./../../../../../TAGS,./../../../../../../TAGS,./../../../../../../../TAGS,./../../../../../../../../TAGS

map <F2> :NERDTreeToggle<CR>
set pastetoggle=<f12>
