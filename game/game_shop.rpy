################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_Shop
################################################################################
screen game_map_shop_1():

    zorder 100

    if abs(global_xoffset) >= (3691-1280):
        timer 0.01 action Return('shop')

    add 'bg_st_shop' xpos 0 ypos 0 xoffset global_xoffset*0.7

    add 'bg_st_ani' xpos 0 ypos 0 xoffset global_xoffset*0.7

    add 'bg_st_label' xpos 0 ypos 0 xoffset global_xoffset*1.15

    timer 0.01 action Show('bg_st_front')

    use game_buttonControll(3691-1280)

screen bg_st_front():

    zorder 111

    if renpy.get_screen(['game_map_shop_1']):

        add 'bg_st_front' xpos 0 ypos 0 xoffset global_xoffset

    else:
        timer 0.01 action Hide('bg_st_front')