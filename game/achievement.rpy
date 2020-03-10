################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## Achievement
################################################################################

define achievement.steam_position = "bottom right"

label achieve:
    $ achievement.Sync()

    $ achievement.register('TruckDead_0_0', steam='ACHIEVEMENT_TruckDead_0_0')
    if not achievement.has('TruckDead_0_0') and persistent.dead_times > 0:
        $ achievement.grant('TruckDead_0_0')

    $ achievement.register('TruckDead_0_1', steam='ACHIEVEMENT_TruckDead_0_1')
    if not achievement.has('TruckDead_0_1') and persistent.dead_times >= 5:
        $ achievement.grant('TruckDead_0_1')
    
    'achieve'
    
    jump startr