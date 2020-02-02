################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_cn
################################################################################
screen game_map_cn_1():

    if abs(global_xoffset) >= (4500):
        timer 0.01 action Return('cn')

    add 'bg_cn_sky' xpos -80 ypos 0 xoffset global_xoffset*0.7 alpha 0.6
    add 'bg_cn_mt' xpos -80 ypos 0 xoffset global_xoffset*0.7 alpha 0.6

    add 'bg_cn_mid' xpos -80 ypos 0 xoffset global_xoffset*0.78 alpha 0.6

    add 'bg_cn_tree' xpos -80 ypos 0 xoffset global_xoffset*0.85

    add 'bg_cn_building' xpos -80 ypos 0 xoffset global_xoffset

    add 'bg_cn_ani' xpos -80 ypos 0 xoffset global_xoffset

    use game_buttonControll(4500)