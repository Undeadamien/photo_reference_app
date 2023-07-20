let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Documents/GitHub/photo_reference_app/module
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 ~/code/python/
badd +1 ~/code/python/test.py
badd +1 ~/code/cpp/maze_solver/Session.vim
badd +75 ~/code/cpp/maze_solver/maze_solver.cpp
badd +3 ~/code/cpp/maze_solver/maze.txt
badd +1 ~/code/cpp/maze_solver/maze_solver.exe
badd +1 ~/AppData/Local/nvim/lua/undeadamien/packer.lua
badd +1 ~/code/rust/hello_world/main.rs
badd +470 C:/Program\ Files/Microsoft\ Visual\ Studio/2022/Community/VC/Tools/MSVC/14.36.32532/include/vector
badd +1 term://~/code/cpp/maze_solver//6232:C:/WINDOWS/system32/cmd.exe
badd +1 ~/AppData/Local/nvim/plugin/colors.lua
badd +1 ~/AppData/Local/nvim/plugin/
badd +10 ~/AppData/Local/nvim/plugin/lsp.lua
badd +2 ~/AppData/Local/nvim/plugin/packer_compiled.lua
badd +4 ~/AppData/Local/nvim/plugin/telescope.lua
badd +1 ~/AppData/Local/nvim/plugin/treesitter.lua
badd +1 ~/AppData/Local/nvim/init.lua
badd +9 ~/AppData/Local/nvim/lua/undeadamien/autocmd.lua
badd +1 ~/AppData/Local/nvim/lua/undeadamien/init.lua
badd +24 ~/AppData/Local/nvim/lua/undeadamien/remap.lua
badd +1 ~/Documents/GitHub/photo_reference_app/main.pyw
badd +1 ~/AppData/Local/nvim-data/mason/packages/python-lsp-server/venv/Lib/site-packages/jedi/third_party/typeshed/stdlib/2and3/math.pyi
badd +1 ~/Documents/GitHub/mtg_analysis/
badd +1 ~/AppData/Local/nvim/quick_push.txt
badd +1 ~/code/cpp/hello_world/hello_world.cpp
badd +2 ~/code/cpp/war_card_game/war_card_game.cpp
badd +1 ~/AppData/Local/nvim
badd +1 ~/AppData/Local/nvim/lua/undeadamien/set.lua
badd +1 ~/Documents/GitHub/war_card_analysis/results.csv
badd +1 ~/Documents/GitHub/war_card_analysis/data_generator.cpp
badd +1 ~/Documents/GitHub/war_card_analysis/main.ipynb
badd +46 ~/Documents/GitHub/war_card_game/war_card_game.py
badd +1 ~/Documents/GitHub
badd +1 ~/Documents/GitHub/photo_reference_app/Session.vim
badd +134 ~/Documents/GitHub/photo_reference_app/main2refactored.pyw
badd +28 reference_window.py
badd +116 setup_window.py
badd +12 ~/Documents/GitHub/photo_reference_app/config.ini
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
exe 'vert 1resize ' . ((&columns * 106 + 106) / 213)
exe '2resize ' . ((&lines * 15 + 25) / 50)
exe 'vert 2resize ' . ((&columns * 106 + 106) / 213)
exe '3resize ' . ((&lines * 32 + 25) / 50)
exe 'vert 3resize ' . ((&columns * 106 + 106) / 213)
argglobal
balt ~/Documents/GitHub/photo_reference_app/Session.vim
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
let s:l = 1 - ((0 * winheight(0) + 24) / 48)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 010|
lcd ~/Documents/GitHub/photo_reference_app
wincmd w
argglobal
if bufexists(fnamemodify("~/Documents/GitHub/photo_reference_app/module/reference_window.py", ":p")) | buffer ~/Documents/GitHub/photo_reference_app/module/reference_window.py | else | edit ~/Documents/GitHub/photo_reference_app/module/reference_window.py | endif
if &buftype ==# 'terminal'
  silent file ~/Documents/GitHub/photo_reference_app/module/reference_window.py
endif
balt ~/Documents/GitHub/photo_reference_app/main.pyw
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
let s:l = 1 - ((0 * winheight(0) + 7) / 15)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/Documents/GitHub/photo_reference_app
wincmd w
argglobal
if bufexists(fnamemodify("~/Documents/GitHub/photo_reference_app/module/setup_window.py", ":p")) | buffer ~/Documents/GitHub/photo_reference_app/module/setup_window.py | else | edit ~/Documents/GitHub/photo_reference_app/module/setup_window.py | endif
if &buftype ==# 'terminal'
  silent file ~/Documents/GitHub/photo_reference_app/module/setup_window.py
endif
balt ~/Documents/GitHub/photo_reference_app/main.pyw
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
let s:l = 1 - ((0 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 020|
lcd ~/Documents/GitHub/photo_reference_app
wincmd w
exe 'vert 1resize ' . ((&columns * 106 + 106) / 213)
exe '2resize ' . ((&lines * 15 + 25) / 50)
exe 'vert 2resize ' . ((&columns * 106 + 106) / 213)
exe '3resize ' . ((&lines * 32 + 25) / 50)
exe 'vert 3resize ' . ((&columns * 106 + 106) / 213)
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
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
