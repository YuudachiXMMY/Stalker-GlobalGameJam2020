################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Main
################################################################################
screen game_buttonControll(xoffset_max):

    text _(str(xoffset_max*-1)) xpos 200 ypos 100 color '#000'
    text _(str(global_xoffset)) xpos 200 ypos 200 color '#000'

    imagebutton:
        xalign 1.0 yalign 0.2
        auto 'right_arr_%s'
        # if abs(global_xoffset-10) > abs(xoffset_max):
        #     action NullAction()
        # elif abs(global_xoffset-10) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
        #     action SetVariable('global_xoffset', xoffset_max*-1)
        # else:
        action SetVariable('global_xoffset', global_xoffset-10)

    imagebutton:
        xalign 1.0 yalign 0.5
        auto 'right_arr_%s'
        # if abs(global_xoffset-150) > abs(xoffset_max):
        #     action NullAction()
        # elif abs(global_xoffset-150) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
        #     action SetVariable('global_xoffset', xoffset_max*-1)
        # else:
        action SetVariable('global_xoffset', global_xoffset-75)

    imagebutton:
        xalign 1.0 yalign 0.8
        auto 'left_arr_%s'
        action SetVariable('interact', interact+1)