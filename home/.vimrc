set expandtab
set tabstop=2
set sw=2
set softtabstop=2
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
autocmd FileType php set noexpandtab omnifunc=phpcomplete#CompletePHP
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

:set errorformat=%m\ in\ %f\ on\ line\ %l

set tags=./tags,./../tags,./../../tags,./../../../tags,./../../../../tags,./../../../../../tags,./../../../../../../tags,./../../../../../../../tags,./../../../../../../../../tags,./TAGS,./../TAGS,./../../TAGS,./../../../TAGS,./../../../../TAGS,./../../../../../TAGS,./../../../../../../TAGS,./../../../../../../../TAGS,./../../../../../../../../TAGS

map <F2> :NERDTreeToggle<CR>
map <F3> :TlistToggle<CR>
set pastetoggle=<f12>
nnoremap <F11> :set nonumber!<CR>

highlight Pmenu ctermbg=238 gui=bold
colorscheme desert

set foldmethod=syntax   "fold based on indent
set foldnestmax=10      "deepest fold is 10 levels
set nofoldenable        "dont fold by default
set foldlevel=4         "this is just what i use
