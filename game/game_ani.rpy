################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Ani
################################################################################
screen f_1_110(t):

    zorder 105

    add 'f_1_110' ypos 650 align(0.5, 1.0) xoffset global_xoffset at b

    timer t action Hide('f_1_110')

screen m_walk_slow(t):

    zorder 105

    add 'm_walk_slow' xpos 130 ypos 650 align(0.5, 1.0)

    timer t action Hide('m_walk_slow')

screen m_s(t):

    zorder 105

    add 'm_s' xpos 130 ypos 650 align(0.5, 1.0) at a

    timer t action Hide('m_s')