################################################################################
## 初始化
################################################################################

init offset = -10

default curr_mouse_position = (0, 0)
default curr_player_position = (0, 0)
default globalXoffset = 0
default localXoffset = 0

################################################################################
## Main
################################################################################

screen getMousePosition():

    zorder 109
    
    imagebutton:
        xpos 151
        idle "gui/null_mouseControll.png"
        action [SetVariable('curr_mouse_position', renpy.get_mouse_pos()),
                SetVariable('localXoffset', globalXoffset)]
                # Show("freeMove_main")]
                
screen screenControl():

    zorder 110
                
    fixed:
        if renpy.get_mouse_pos()[0] < 151:
            timer 0.5 action SetVariable('globalXoffset', globalXoffset+50)
        elif renpy.get_mouse_pos()[0] > 1769:
            timer 0.5 action SetVariable('globalXoffset', globalXoffset-50)

        # imagebutton:
        #     yalign 0.5 xalign 0.0
        #     idle "gui/mapScreen/leftarr.png"
        #     action SetVariable('globalXoffset', globalXoffset+50)
        # imagebutton:
        #     yalign 0.5 xalign 1.0
        #     idle "gui/mapScreen/rightarr.png"
        #     action SetVariable('globalXoffset', globalXoffset-50)

screen chaControl_show():

    zorder 100

    add 'cha/01/00.png':
        zoom 0.7 xanchor 0.5 yanchor 1.0
        xoffset globalXoffset
        ypos 1090
        if curr_mouse_position == curr_player_position:
            xpos curr_player_position[0]-localXoffset
        else:
            xpos curr_mouse_position[0]-localXoffset
            
    timer 0.01 action SetVariable('curr_player_position', curr_mouse_position)

    # if curr_mouse_position == curr_player_position:
    #     add 'cha/01/00.png' zoom 0.7 xanchor 0.5 yanchor 1.0 pos(curr_player_position[0]-localXoffset, 1090) xoffset globalXoffset
    # else:
    #     timer 0.01 action SetVariable('curr_player_position', curr_mouse_position)
    #     add 'cha/01/00.png' zoom 0.7 xanchor 0.5 yanchor 1.0 pos(curr_mouse_position[0]-localXoffset, 1090) xoffset globalXoffset

screen freeMove_main():
    
    tag freeMove_main
    
    zorder 100

    add 'images/map/Map1.png' pos(0, 0) xoffset globalXoffset

    use chaControl_show

    # use screenControl
    # timer 0.01 action Show('chaControl_show')
    
    timer 0.01 action Show('getMousePosition')

    timer 0.01 action Show('screenControl')


    text _('mos pos'+str(curr_mouse_position)) xpos 500
    text _('cur pos'+str(curr_player_position)) xpos 500 ypos 200
    
    text _('global xof'+str(globalXoffset)) xpos 900
    text _('cur xof'+str(localXoffset)) xpos 900 ypos 200

    fixed:
        pass