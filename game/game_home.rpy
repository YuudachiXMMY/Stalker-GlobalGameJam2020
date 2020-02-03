################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## Game_home
################################################################################
screen game_map_home_1():

    zorder 100

    if abs(global_xoffset) >= (4943-1280):
        timer 0.01 action Return('home')

    add 'bg_hm_bg' xpos 0 ypos 0 xoffset global_xoffset

    add 'bg_hm_ani' xpos 0 ypos 0 xoffset global_xoffset

    #trashes
    timer 0.01 action Show('hm_trash_1')
    timer 0.01 action Show('hm_trash_2')
    timer 0.01 action Show('hm_trash_3')


    if abs(global_xoffset) == 0:
        add 'm_s' xpos 130 ypos 690 align(0.5, 1.0)
    if abs(global_xoffset) == 0 and not renpy.get_screen('f_con'):
        add 'f_b' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset

    # f 主控
    timer 4.5 action [  SetVariable('tmp_xpos', 1600),
                        Show('f_con')]
    timer 9 action [  SetVariable('tmp_xpos', 2100),
                        Show('f_con')]
    timer 15 action [  SetVariable('tmp_xpos', 2900),
                        Show('f_con')]
    timer 22 action [  SetVariable('tmp_xpos', 3800),
                        Show('f_con')]
    timer 27 action [  SetVariable('tmp_xpos', 4400),
                        Show('f_con')]
    timer 35 action [  SetVariable('tmp_xpos', 5300),
                        Show('f_con')]

    use game_buttonControll(4943-1280)

screen hm_trash_1():

    zorder 102

    if renpy.get_screen('game_map_home_1'):
        if not trash_1_solv:
            add 'trash2' xpos 0 ypos 0 xoffset global_xoffset
        elif trash_1_solv:
            add 'trash1' xpos 0 ypos 0 xoffset global_xoffset

    else:
        timer 0.01 action Hide('hm_trash')

screen hm_trash_2():

    zorder 102

    if renpy.get_screen('game_map_home_1'):
        if not trash_2_solv:
            add 'trash2' xpos -1000 ypos 0 xoffset global_xoffset
        elif trash_2_solv:
            add 'trash1' xpos -1000 ypos 0 xoffset global_xoffset

    else:
        timer 0.01 action Hide('hm_trash')

screen hm_trash_3():

    zorder 102

    if renpy.get_screen('game_map_home_1'):
        if not trash_3_solv:
            add 'trash2' xpos -3000 ypos 0 xoffset global_xoffset
        elif trash_3_solv:
            add 'trash1' xpos -3000 ypos 0 xoffset global_xoffset

    else:
        timer 0.01 action Hide('hm_trash')