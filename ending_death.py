from sys import exit
import random

# defines how a game ends, in case the player dies
# system used on every map

# usage: ending("number of goodie-points")
def ending(kind):

    from goodie_points import goodie_points_count

    goodie_points = goodie_points_count

    # two kinds of endings implemented so far

    if kind == "completed":
        print("You have completed this map and you have {} goodie-points! How much you have earned will determine your fate now!".format(goodie_points))
    elif kind == "death":
        print("You died. You start counting your goodie-points and find yourself having earned {} goodie-points!".format(goodie_points))
    else:
        print("The game broke...")
        reset_goodie_points()
        exit(0)

    # three different types of endings regarding goodie-points so far
    if goodie_points < 100:
        hell()
    elif goodie_points >= 100 and goodie_points < 500:
        heaven()
    elif goodie_points >= 500:
        rebirth()
    # python will result in an error, if the goodie_points are anything else than an integer
    # the following else should never actually run
    else:
        print("You broke the game...")
        reset_goodie_points()
        exit(0)

# not having enough goodie-points leads to being put into hell
def hell():
    print("Since you have not earned enough goodie-points you are going to hell.")
    reset_goodie_points()
    exit(0)

# having enough goodie-points leads to being allowed into heaven
def heaven():
    print("Since you have earned enough goodie-points you are going to heaven!")
    reset_goodie_points()
    exit(0)

# having more than 499 goodie-points leads to moving on towards a new map, even though the player died
def rebirth():
    print("Since you have earned so many goodie-points God grants you another life on a random map!")
    reset_goodie_points()
    # TO DO: import maps and pick a random map
    # TO DO: fix random and run functions within the correct files and not in edning_death.py
    '''
    from map_1_forest import forest_start
    from map_2_underwater import underwater_start
    from map_3_clouds import clouds_start
    from map_4_mountain import mountain_start
    maps = [forest_start, underwater_start, clouds_start, mountain_start]

    map_index = random.randrange(0,3)
    print ("---------- Map index = ", map_index)
    maps[map_index]()
    '''
    # TO DO: remove exit()
    exit(0)
# this will reset the goodie-points counter to 0
def reset_goodie_points():
    with open('goodie_points.py', 'r') as goodie_file:
        data = goodie_file.readlines()
        # TO DO: figure out an alternative way of doing this, because it is very static this way
        data[1] = 'goodie_points_count = 0' + '\n'

    with open('goodie_points.py', 'w') as goodie_file:
        goodie_file.writelines(data)
    print("Points will be reset to 0.")
