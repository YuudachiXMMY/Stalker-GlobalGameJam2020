################################################################################
## Game_screen Images 初始化
################################################################################

init offset = -10

################################################################################
## Backgrounds
################################################################################
image bg_templ:
    'gui/templet - bg.png'

image bg_street:
    'bg/street.jpg'

################################################################################
## Gui
################################################################################
image right_arr_idle:
    'gui/game_screen/rightarr.png'

image left_arr_idle:
    'gui/game_screen/leftarr.png'

################################################################################
## Temp Scene 1
################################################################################
image f_1_110:
    'cha/tmp_f/1-1.0.png'
    pause 0.4
    'cha/tmp_f/1-1.1.png'
    pause 0.4
    'cha/tmp_f/1-1.2.png'
    pause 0.4
    'cha/tmp_f/1-1.2.obj.png'

image m_walk:
    'cha/tmp_m/1-walk1.png'
    pause 0.2
    'cha/tmp_m/1-walk2.png'
    pause 0.2
    'cha/tmp_m/1-walk3.png'
    pause 0.2
    repeat

image m_1_110:
    'cha/tmp_m/1-stable-1.0.png'

################################################################################
## Scene 1
################################################################################
image m_s:
    'cha/m/s.png'

image m_walk_slow:
    'cha/m/s.png'
    pause 0.2
    'cha/m/w1.png'
    pause 0.2
    'cha/m/w2.png'
    pause 0.2
    'cha/m/w1.png'
    pause 0.2
    'cha/m/s.png'
    pause 0.2
    'cha/m/w-1.png'
    pause 0.2
    'cha/m/w-2.png'
    pause 0.2
    'cha/m/w-1.png'
    pause 0.2
    repeat

image m_walk_fast:
    'cha/m/s.png'
    pause 0.05
    'cha/m/w1.png'
    pause 0.05
    'cha/m/w2.png'
    pause 0.05
    'cha/m/w1.png'
    pause 0.05
    'cha/m/s.png'
    pause 0.05
    'cha/m/w-1.png'
    pause 0.05
    'cha/m/w-2.png'
    pause 0.05
    'cha/m/w-1.png'
    pause 0.05
    repeat