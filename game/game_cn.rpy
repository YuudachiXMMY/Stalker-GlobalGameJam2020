################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_cn
################################################################################
screen game_map_cn_1():

    zorder 100

    if abs(global_xoffset) >= (4500):
        timer 0.01 action [ Hide('f_con'),
                            Return('cn')]

    add 'bg_cn_sky' xpos -80 ypos 0 xoffset global_xoffset*0.7 alpha 0.6
    add 'bg_cn_mt' xpos -80 ypos 0 xoffset global_xoffset*0.7 alpha 0.6

    add 'bg_cn_mid' xpos -80 ypos 0 xoffset global_xoffset*0.78 alpha 0.6

    add 'bg_cn_tree' xpos -80 ypos 0 xoffset global_xoffset*0.85
    add 'cha/cat/tree.png' xpos 400 ypos 0 xoffset global_xoffset*0.85
    
    if abs(global_xoffset) >= 2310 and abs(global_xoffset) <= 2890:
        timer 0.01 action Show('bg_cn_cat')
    else:
        add 'cha/cat/c1.png' xpos 400 ypos 0 xoffset global_xoffset*0.85
    
    add 'bg_cn_building' xpos -80 ypos 0 xoffset global_xoffset

    add 'bg_cn_ani' xpos -80 ypos 0 xoffset global_xoffset

    if abs(global_xoffset) == 0:
        add 'm_s' xpos 130 ypos 690 align(0.5, 1.0)
    if abs(global_xoffset) == 0 and not renpy.get_screen('f_con'):
        add 'f_b' xpos 1560 ypos 690 align(0.5, 1.0) xoffset global_xoffset

    # f 主控
    timer 4.5 action [  SetVariable('tmp_xpos', 2410),
                        Show('f_con')]
    timer 12 action [  SetVariable('tmp_xpos', 2860),
                        Show('f_con')]
    timer 20 action [  SetVariable('tmp_xpos', 3720),
                        Show('f_con')]
    timer 28 action [  SetVariable('tmp_xpos', 4120),
                        Show('f_con')]
    timer 35 action [  SetVariable('tmp_xpos', 6100),
                        Show('f_con')]

    use game_buttonControll(4500)

screen bg_cn_cat():

    zorder 111

    if renpy.get_screen(['game_map_cn_1']):

        if not cn_cat_inter:
            add 'cat_inter' xpos 400 ypos 0 xoffset global_xoffset*0.85
        elif cn_cat_inter:
            add 'cat_inter_yes' xpos 400 ypos 0 xoffset global_xoffset*0.85

    else:
        timer 0.01 action Hide('bg_cn_cat')