
label start:

    "start"

    # $ global_xoffset = 0

    # call screen game_map_street_1

    jump s1

label s1:

    $ global_xoffset = -400
    call screen game_map_street_2

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'E1':
        jump e1
    
    jump s2

label s2:
    $ global_xoffset = 0

    call screen game_map_cn_1

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'E1':
        jump e1

    jump s3

label s3:
    $ global_xoffset = 0

    call screen game_map_shop_1

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'E1':
        jump e1

    jump s4

label s4:
    $ global_xoffset = 0
 
    call screen game_map_home_1

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'E1':
        jump e1

    '[_return]'

    return

label e1:

    'e1'

    return

label be1:

    'be1'

    return