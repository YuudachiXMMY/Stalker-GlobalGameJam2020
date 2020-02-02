################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Ani
################################################################################
screen f_1_110(t, s):

    zorder 105

    if renpy.get_screen(s):

        add 'f_w' ypos 690 align(0.5, 1.0) xoffset global_xoffset at b

        timer t action Hide('f_1_110')
    
    else:
        timer 0.01 action Hide('m_s')

screen m_walk_slow(t, s):

    zorder 105

    if renpy.get_screen(s):
        add 'm_walk_slow' xpos 130 ypos 690 align(0.5, 1.0)

        timer t action Hide('m_walk_slow')

    else:
        timer 0.01 action Hide('m_s')

screen m_s(t, s):

    zorder 105

    if renpy.get_screen(s):

        add 'm_s' xpos 130 ypos 690 align(0.5, 1.0):
            if t < 99:
                at a

        timer t action Hide('m_s')

    else:
        timer 0.01 action Hide('m_s')

################################################################################
## 共存
################################################################################
screen chaMoveCon(cha):

    zorder 105

    if renpy.get_screen([   'game_map_street_2',
                            'game_map_cn_1',
                            'game_map_shop_1',
                            'game_map_home_1']):

        add cha xpos 130 ypos 690 align(0.5, 1.0)

screen f_con():

    zorder 105

    if renpy.get_screen([   'game_map_street_2',
                            'game_map_home_1']):

        if tmp_xpos != f_xpos:
            add 'f_w' xpos tmp_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset at f_w_con
            timer 4 action [SetVariable('f_xpos', tmp_xpos),
                            Hide('f_con'), Show('f_con')]
        elif abs((130+abs(global_xoffset))) >= f_xpos-350 and abs((130+abs(global_xoffset))) <= f_xpos+350:
            timer 0.01 action Return('BE1')
        elif abs((130+abs(global_xoffset))) >= f_xpos-750 and abs((130+abs(global_xoffset))) <= f_xpos+750:
            add 'f_ht' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
        else:
            add 'f_b' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset

    elif renpy.get_screen([ 'game_map_cn_1',
                            'game_map_shop_1']):

        if tmp_xpos != f_xpos:
            add 'f_w' xpos tmp_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset at f_w_con
            timer 4 action [SetVariable('f_xpos', tmp_xpos),
                            Hide('f_con'), Show('f_con')]
        elif abs((130+abs(global_xoffset))) >= f_xpos-650 and abs((130+abs(global_xoffset))) <= f_xpos+650:
            timer 0.01 action Return('BE1')
        elif abs((130+abs(global_xoffset))) >= f_xpos-850 and abs((130+abs(global_xoffset))) <= f_xpos+850:
            add 'f_ht' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
        else:
            add 'f_b' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
