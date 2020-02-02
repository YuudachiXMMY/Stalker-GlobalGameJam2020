################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Main
################################################################################
screen game_buttonControll(xoffset_max):

    zorder 300

    if not renpy.get_screen('game_map_street_1'):

        text _(str(global_xoffset)) xpos 50 ypos 20 color '#000'
        text _(str(f_xpos)) xpos 50 ypos 45 color '#000'
        text _(str(tmp_xpos)) xpos 50 ypos 70 color '#000'
        text _(str(street_achieve)) xpos 100 ypos 0 color '#000'
        text _(str(interact)) xpos 50 ypos 0 color '#000'

        imagebutton:
            keysym 'z'
            xalign 0.95 yalign 0.2
            auto 'sarr_%s'
            # if abs(global_xoffset-10) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-10) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            if tmp_xpos != f_xpos:
                action [SetVariable('global_xoffset', global_xoffset-20),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_slow_sing')]
            else:
                action [SetVariable('global_xoffset', global_xoffset-20),
                        Hide('chaMoveCon'), Hide('f_con'),
                        Show('chaMoveCon', cha='m_walk_slow_sing'),
                        Show('f_con')]

        imagebutton:
            keysym 'x'
            xalign 0.95 yalign 0.5
            auto 'farr_%s'
            # if abs(global_xoffset-150) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-150) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            if tmp_xpos != f_xpos:
                action [SetVariable('global_xoffset', global_xoffset-90),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_fast_sing')]
            else:
                action [SetVariable('global_xoffset', global_xoffset-90),
                    Hide('chaMoveCon'), Hide('f_con'),
                    Show('chaMoveCon', cha='m_walk_fast_sing'),
                    Show('f_con')]

        imagebutton:
            keysym 'K_SPACE'
            xalign 0.95 yalign 0.8
            auto 'inter_%s'
            if renpy.get_screen('game_map_street_2') and abs(global_xoffset)==400:
                action SetVariable('interact', interact+1)
            elif renpy.get_screen('game_map_street_2') and street_achieve == 0 and abs(global_xoffset) >= 1120 and abs(global_xoffset) <= 1390:
                action SetVariable('street_achieve', street_achieve+1)
            else:
                action NullAction()