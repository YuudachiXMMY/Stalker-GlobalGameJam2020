################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_Shop
################################################################################
screen game_map_shop_1():

    if abs(global_xoffset) >= (3691-1280):
        timer 0.01 action Return('shop')

    add 'bg_st_shop' xpos 0 ypos 0 xoffset global_xoffset*0.7

    add 'bg_st_ani' xpos 0 ypos 0 xoffset global_xoffset*0.7

    add 'bg_st_front' xpos 0 ypos 0 xoffset global_xoffset

    add 'bg_st_label' xpos 0 ypos 0 xoffset global_xoffset*1.15

    use game_buttonControll(3691-1280)