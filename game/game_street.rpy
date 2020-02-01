################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_street
################################################################################
screen game_map_street_1():

    modal True

    if abs(global_xoffset) >= (3840-1280):
        timer 0.01 action Return('street')

    add 'bg_street_bg' xpos 0 ypos 0 xoffset global_xoffset
    add 'bg_street_lights' xpos 0 ypos 0 xoffset global_xoffset*1.15

    # use game_buttonControll(3840-1280)

    # use game_map_street_chaLH

    timer 0.01 action Show('f_1_110', t=9.1)

    timer 1+1.8 action Show('m_s', t=1, transition=Dissolve(0.5))

    timer start_time_street+1.6 action Show('m_walk_slow', t=2.5)

    timer start_time_street+1.8 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+1.9 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.0 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.1 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.2 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.3 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.4 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.6 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.7 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.8 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.9 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.0 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.1 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.2 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.3 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.4 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.6 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.7 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.8 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.9 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.0 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.1 action SetVariable('global_xoffset', global_xoffset-20)

    timer start_time_street+4.1 action Show('m_s', t=999)

    timer start_time_street+7 action Return()

screen game_map_street_2():

    if abs(global_xoffset) >= (3840-1280):
        timer 0.01 action Return('street')

    add 'bg_street_bg' xpos 0 ypos 0 xoffset global_xoffset
    add 'bg_street_lights' xpos 0 ypos 0 xoffset global_xoffset*1.15

    use game_buttonControll(3840-1280)

    if interact >= 5:
        timer 0.01 action Return('E1')

    text _(str(interact)) xpos 200 ypos 50 color '#000'

