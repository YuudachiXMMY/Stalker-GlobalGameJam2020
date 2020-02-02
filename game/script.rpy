
label start:

    "start"

    # $ global_xoffset = 0

    # call screen game_map_street_1 with Dissolve(2.0)

    jump s1

label s1:

    $ f_xpos = 1720
    $ tmp_xpos = 1720

    $ global_xoffset = -400

    call screen game_map_street_2

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2
    if tmp == 'E1':
        jump e1
    
    jump s2

label s2:

    $ f_xpos = 1560
    $ tmp_xpos = 1560

    $ global_xoffset = 0

    call screen game_map_cn_1 with Dissolve(3.0)

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2
    if tmp == 'E1':
        jump e1

    jump s3

label s3:

    $ f_xpos = 800
    $ tmp_xpos = 800

    $ global_xoffset = 0

    call screen game_map_shop_1 with Dissolve(3.0)

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2
    if tmp == 'E1':
        jump e1

    jump s4

label s4:
    $ global_xoffset = 0
 
    call screen game_map_home_1 with Dissolve(3.0)

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2
    if tmp == 'E1':
        jump e1

    '[_return]'

    return


######################################
# ending

label e1:

    scene image '/cg/cg_none_1.jpg' with Dissolve(0.5)
    pause 0.5
    scene image '/cg/cg_none_2.jpg' with Dissolve(0.3)
    pause 0.2
    scene image '/cg/cg_none_3.jpg' with Dissolve(0.5)
    pause 0.7
    scene image '/cg/cg_none_4.jpg' with Dissolve(0.5)
    pause

    return

label be1:

    scene image '/cg/cg_caught_1.jpg' with Dissolve(2.0)
    pause 1.5
    scene image '/cg/cg_caught_2.jpg' with Dissolve(2.0)
    pause

    return

label be2:

    scene image '/cg/cg_die1.jpg' with Dissolve(2.0)
    pause

    return