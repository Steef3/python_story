from sys import exit

# defines how a game ends, in case the player dies
# system used on every map

# usage: ending("number of goodie-points")
def ending():

    from goodie_points import goodie_points_count

    goodie_points = goodie_points_count

    print("You died and you have {} goodie-points!".format(goodie_points))
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
    # TO DO: random new map xyz
    reset_goodie_points()
    exit(0)

# this will reset the goodie-points counter to 0
def reset_goodie_points():
    with open('goodie_points.py', 'r') as goodie_file:
        data = goodie_file.readlines()
        # TO DO: figure out an alternative way of doing this, because it is very static this way
        data[1] = 'goodie_points_count = 0' + '\n'

    with open('goodie_points.py', 'w') as goodie_file:
        goodie_file.writelines(data)
