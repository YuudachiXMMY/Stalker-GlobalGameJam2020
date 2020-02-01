################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_home
################################################################################
screen game_map_home_1():

    if abs(global_xoffset) >= (4943-1280):
        timer 0.01 action Return('home')

    add 'bg_hm_bg' xpos 0 ypos 0 xoffset global_xoffset

    add 'bg_hm_ani' xpos 0 ypos 0 xoffset global_xoffset

    use game_buttonControll(4943-1280)