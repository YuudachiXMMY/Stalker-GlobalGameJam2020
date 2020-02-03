################################################################################
## init
################################################################################

init offset = -1

################################################################################
## init
################################################################################

default global_xoffset = 0
default tmp_xoffset = global_xoffset

define start_time_street = 7.5

default interact = 0

default f_xpos = 1720
default tmp_xpos = 1720

default persistent.street_achieve = 0
default cn_achieve = 0
default shop_achieve = 0
default home_achieve = 0

default m_hide = False
default persistent.cn_cat_inter = False
default persistent.f_ht_times = 0

default trash_1_solv = False
default trash_2_solv = False
default trash_3_solv = False
default persistent.trash_counts = 0

default persistent.dead_times = 0
default persistent.caught_times = 0
# define cn_hide_lst = ((abs(global_xoffset)>=20 and abs(global_xoffset)<40) or 
#                     (abs(global_xoffset)>=100 and abs(global_xoffset)<120) or 
#                     (abs(global_xoffset)>=380 and abs(global_xoffset)<400) or
#                     (abs(global_xoffset)>=560 and abs(global_xoffset)<600) )