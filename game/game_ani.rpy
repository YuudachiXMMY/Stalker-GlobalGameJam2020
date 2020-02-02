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

        add 'f_1_110' ypos 650 align(0.5, 1.0) xoffset global_xoffset at b

        timer t action Hide('f_1_110')
    
    else:
        timer 0.01 action Hide('m_s')

screen m_walk_slow(t, s):

    zorder 105

    if renpy.get_screen(s):
        add 'm_walk_slow' xpos 130 ypos 650 align(0.5, 1.0)

        timer t action Hide('m_walk_slow')

    else:
        timer 0.01 action Hide('m_s')

screen m_s(t, s):

    zorder 105

    if renpy.get_screen(s):

        add 'm_s' xpos 130 ypos 650 align(0.5, 1.0):
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

    add cha xpos 130 ypos 650 align(0.5, 1.0)

screen f_con(cha):

    zorder 105

    pass