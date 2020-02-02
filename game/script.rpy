
label start:

    "start"

    $ global_xoffset = 0

    call screen game_map_street_1
    call screen game_map_street_2

    $ global_xoffset = 0

    call screen game_map_cn_1

    $ global_xoffset = 0

    call screen game_map_shop_1

    $ global_xoffset = 0
 
    call screen game_map_home_1

    $ tmp = _return

    if tmp == 'E1':
        jump e1

    '[_return]'

    return

label e1:

    'e1'

    return