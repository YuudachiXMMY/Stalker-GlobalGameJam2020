################################################################################
## Game_screen Images 初始化
################################################################################

init offset = -10

################################################################################
## Backgrounds
################################################################################
image bg_templ:
    'gui/templet - bg.png'

# Street
image bg_street_bg:
    'bg/street/street.jpg'

image bg_street_lights:
    'bg/street/lights.jpg'

# CN
image bg_cn_building:
    'bg/cn/building.png'

image bg_cn_mt:
    'bg/cn/mt.png'

image bg_cn_mid:
    'bg/cn/mid.png'

image bg_cn_tree:
    'bg/cn/tree.png'

image bg_cn_ani1:
    'bg/cn/ani1.png'

image bg_cn_ani2:
    'bg/cn/ani2.png'

image bg_cn_ani3:
    'bg/cn/ani3.png'

image bg_cn_ani:
    'bg_cn_ani1'
    pause 0.5
    'bg_cn_ani2'
    pause 0.5
    'bg_cn_ani3'
    pause 0.5
    repeat

# ST
image bg_st_shop:
    'bg/shop/shop.png'

image bg_st_label:
    'bg/shop/label.png'

image bg_st_front:
    'bg/shop/front.png'

image bg_st_ani1:
    'bg/shop/ani1.png'

image bg_st_ani2:
    'bg/shop/ani2.png'

image bg_st_ani3:
    'bg/shop/ani3.png'

image bg_st_ani:
    'bg_st_ani1'
    pause 0.5
    'bg_st_ani2'
    pause 0.5
    'bg_st_ani3'
    pause 0.5
    repeat

# home
image bg_hm_bg:
    'bg/home/bg.png'

image bg_hm_ani1:
    'bg/home/ani1.png'

image bg_hm_ani2:
    'bg/home/ani2.png'

image bg_hm_ani3:
    'bg/home/ani3.png'

image bg_hm_ani:
    'bg_hm_ani1'
    pause 0.5
    'bg_hm_ani2'
    pause 0.5
    'bg_hm_ani3'
    pause 0.5
    repeat

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

image m_walk_slow_sing:
    'cha/m/s.png'
    pause 0.2
    'cha/m/w1.png'
    pause 0.2
    'cha/m/w2.png'
    pause 0.2
    'cha/m/w1.png'
    pause 0.2
    'cha/m/s.png'

image m_walk_fast_sing:
    'cha/m/s.png'
    pause 0.05
    'cha/m/w1.png'
    pause 0.05
    'cha/m/w2.png'
    pause 0.05
    'cha/m/w1.png'
    pause 0.05
    'cha/m/s.png'