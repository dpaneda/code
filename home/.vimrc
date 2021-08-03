set expandtab
set tabstop=4
set sw=4
set softtabstop=4
set autoindent
set shiftround
set background=dark
set modeline

"Color scheme af in colors dir
"colorscheme af
syntax on
"set termguicolors

"Increases compatability for
"vims where ftplugin might
"be turned off.
filetype plugin on

set tw=120
set formatoptions-=t

" show tab chars with ...>
" set list listchars=tab:»·,trail:·

" turn hybrid line numbers on
set number relativenumber

set history=100

" show a full list when hitting tab
" looking for files.
set wildmode=list:longest,full
set showmode
set showcmd

filetype on

autocmd FileType c,cpp,slang set cindent

"Auto Complete <c-x><c-o>
autocmd FileType php set noexpandtab omnifunc=phpcomplete#CompletePHP
autocmd FileType python set expandtab
autocmd FileType c set omnifunc=ccomplete#Complete

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
"set viminfo='10,\"100,:20,%,n~/.viminfo
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif 

:set errorformat=%m\ in\ %f\ on\ line\ %l

set tags=./tags,./../tags,./../../tags,./../../../tags,./../../../../tags,./../../../../../tags,./../../../../../../tags,./../../../../../../../tags,./../../../../../../../../tags,./TAGS,./../TAGS,./../../TAGS,./../../../TAGS,./../../../../TAGS,./../../../../../TAGS,./../../../../../../TAGS,./../../../../../../../TAGS,./../../../../../../../../TAGS

map <F2> :NERDTreeToggle<CR>
map <F3> :TlistToggle<CR>
set pastetoggle=<f12>
nnoremap <F11> :set number! relativenumber!<CR>

highlight Pmenu ctermbg=238 gui=bold
colorscheme gruvbox
let g:gruvbox_contrast_dark = 'hard'

set foldmethod=syntax   "fold based on indent
set foldnestmax=10      "deepest fold is 10 levels
set nofoldenable        "dont fold by default
set foldlevel=4         "this is just what i use

"Changing Leader Key
let mapleader = ","

" Set title to window
set title

"Vimux config
let g:VimuxOrientation = "h"
let g:VimuxHeight = 50

"set spell
"setlocal spell spelllang=es
let g:airline_powerline_fonts = 1

" vim hardcodes background color erase even if the terminfo file does
" not contain bce (not to mention that libvte based terminals
" incorrectly contain bce in their terminfo files). This causes
" incorrect background rendering when using a color theme with a
" background color.
"let &t_ut=''

function! Hashbang(portable, permission, RemExt)
let shells = {
        \    'awk': "awk",
        \     'sh': "bash",
        \     'hs': "runhaskell",
        \     'jl': "julia",
        \    'lua': "lua",
        \    'mak': "make",
        \     'js': "node",
        \      'm': "octave",
        \     'pl': "perl",
        \    'php': "php",
        \     'py': "python",
        \      'r': "Rscript",
        \     'rb': "ruby",
        \  'scala': "scala",
        \    'tcl': "tclsh",
        \     'tk': "wish"
        \    }

let extension = expand("%:e")

if has_key(shells,extension)
	let fileshell = shells[extension]

	if a:portable
		let line =  "#! /usr/bin/env " . fileshell
	else
		let line = "#! " . system("which " . fileshell)
	endif

	0put = line

	if a:permission
		:autocmd BufWritePost * :autocmd VimLeave * :!chmod u+x %
	endif


	if a:RemExt
		:autocmd BufWritePost * :autocmd VimLeave * :!mv % "%:p:r"
	endif

endif

endfunction

:autocmd BufNewFile *.* :call Hashbang(1,1,0)
