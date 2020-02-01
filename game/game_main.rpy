################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Main
################################################################################
screen game_main():
    pass

screen game_buttonControll(xoffset_max):

    text _(str(xoffset_max*-1)) xpos 200 ypos 100 color '#000'
    text _(str(global_xoffset)) xpos 200 ypos 200 color '#000'

    
    imagebutton:
        xalign 1.0 yalign 0.3
        auto 'right_arr_%s'
        # if abs(global_xoffset-10) > abs(xoffset_max):
        #     action NullAction()
        # elif abs(global_xoffset-10) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
        #     action SetVariable('global_xoffset', xoffset_max*-1)
        # else:
        action SetVariable('global_xoffset', global_xoffset-10)

    imagebutton:
        xalign 1.0 yalign 0.7
        auto 'right_arr_%s'
        # if abs(global_xoffset-150) > abs(xoffset_max):
        #     action NullAction()
        # elif abs(global_xoffset-150) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
        #     action SetVariable('global_xoffset', xoffset_max*-1)
        # else:
        action SetVariable('global_xoffset', global_xoffset-150)

screen game_map_street_1():

    modal True

    if abs(global_xoffset) >= (3840-1280):
        timer 0.01 action Return('street')

    add 'bg_street' xpos 0 ypos 0 xoffset global_xoffset

    use game_buttonControll(3840-1280)

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

# screen game_map_street_chaLH():

#     if

screen game_map_templ():

    add 'bg_templ' xpos 0 ypos 0 xoffset global_xoffset
    
    use game_buttonControll()