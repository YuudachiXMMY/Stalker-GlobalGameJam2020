################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## Game_Shop
################################################################################
screen game_map_shop_1():

    zorder 100

    if abs(global_xoffset) >= (3691-1280):
        timer 0.01 action [ Hide('f_con'),
                            Return('shop')]

    add 'bg_st_shop' xpos 0 ypos 0 xoffset global_xoffset*0.7

    add 'bg_st_ani' xpos 0 ypos 0 xoffset global_xoffset*0.7

    add 'bg_st_label' xpos 0 ypos 0 xoffset global_xoffset*1.15

    if abs(global_xoffset) == 0:
        add 'm_s' xpos 130 ypos 690 align(0.5, 1.0)
    if abs(global_xoffset) == 0 and not renpy.get_screen('f_con'):
        add 'f_b' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset

    timer 0.01 action Show('bg_st_front')

    # f 主控
    timer 4.5 action [  SetVariable('tmp_xpos', 1100),
                        Show('f_con')]
    timer 9 action [  SetVariable('tmp_xpos', 1600),
                        Show('f_con')]
    timer 15 action [  SetVariable('tmp_xpos', 2100),
                        Show('f_con')]
    timer 22 action [  SetVariable('tmp_xpos', 2900),
                        Show('f_con')]
    timer 30 action [  SetVariable('tmp_xpos', 3500),
                        Show('f_con')]

    use game_buttonControll(3691-1280)

screen bg_st_front():

    zorder 111

    if renpy.get_screen(['game_map_shop_1']):

        add 'bg_st_front' xpos 0 ypos 0 xoffset global_xoffset

    else:
        timer 0.01 action Hide('bg_st_front')