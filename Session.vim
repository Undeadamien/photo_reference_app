let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/code/python/prepare_session
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +13 ~/code/python/test.py
badd +12 ~/AppData/Local/nvim/lua/undeadamien/autocmd.lua
badd +2 ~/AppData/Local/nvim/lua/undeadamien/init.lua
badd +9 ~/AppData/Local/nvim/lua/undeadamien/packer.lua
badd +2 ~/AppData/Local/nvim/lua/undeadamien/remap.lua
badd +1 ~/AppData/Local/nvim/lua/undeadamien/set.lua
badd +2 ~/AppData/Local/nvim/init.lua
badd +2 ~/AppData/Local/nvim/plugin/colors.lua
badd +1 ~/AppData/Local/nvim/plugin/lsp.lua
badd +4 ~/AppData/Local/nvim/plugin/packer_compiled.lua
badd +6 ~/AppData/Local/nvim/plugin/treesitter.lua
badd +10 ~/AppData/Local/nvim/plugin/telescope.lua
badd +1 ~/code/rust/hello_world/main.rs
badd +1 ~/code/python/Session.vim
badd +9 ~/code/python/prepare_session/prepare_session.pyw
badd +1 ~/code/python/prepare_session/session.nvim
badd +1 ~/code/python/prepare_session/Session.vim
badd +0 ~/Documents/GitHub/photo_reference_app/main.pyw
badd +1 ~/Documents/GitHub/photo_reference_app/module/reference_window.py
badd +11 ~/Documents/GitHub/photo_reference_app/module/setup_window.py
argglobal
%argdel
edit ~/Documents/GitHub/photo_reference_app/main.pyw
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 120 + 120) / 240)
exe '2resize ' . ((&lines * 26 + 28) / 56)
exe 'vert 2resize ' . ((&columns * 119 + 120) / 240)
exe '3resize ' . ((&lines * 27 + 28) / 56)
exe 'vert 3resize ' . ((&columns * 119 + 120) / 240)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 19 - ((18 * winheight(0) + 27) / 54)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 19
normal! 0
lcd ~/Documents/GitHub/photo_reference_app
wincmd w
argglobal
if bufexists(fnamemodify("~/Documents/GitHub/photo_reference_app/module/setup_window.py", ":p")) | buffer ~/Documents/GitHub/photo_reference_app/module/setup_window.py | else | edit ~/Documents/GitHub/photo_reference_app/module/setup_window.py | endif
if &buftype ==# 'terminal'
  silent file ~/Documents/GitHub/photo_reference_app/module/setup_window.py
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 13) / 26)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/Documents/GitHub/photo_reference_app/module
wincmd w
argglobal
if bufexists(fnamemodify("~/Documents/GitHub/photo_reference_app/module/reference_window.py", ":p")) | buffer ~/Documents/GitHub/photo_reference_app/module/reference_window.py | else | edit ~/Documents/GitHub/photo_reference_app/module/reference_window.py | endif
if &buftype ==# 'terminal'
  silent file ~/Documents/GitHub/photo_reference_app/module/reference_window.py
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 13) / 27)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/Documents/GitHub/photo_reference_app
wincmd w
exe 'vert 1resize ' . ((&columns * 120 + 120) / 240)
exe '2resize ' . ((&lines * 26 + 28) / 56)
exe 'vert 2resize ' . ((&columns * 119 + 120) / 240)
exe '3resize ' . ((&lines * 27 + 28) / 56)
exe 'vert 3resize ' . ((&columns * 119 + 120) / 240)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
