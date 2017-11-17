from sys import exit
from goodie_points import goodie_points_count

# defines how a game ends, in case the player dies
# system used on every map

goodie_points = goodie_points_count

# usage: ending(goodie_points)
def ending():

    global goodie_points
    # TO DO: figure out a better way of displaying goodie-points
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
        exit(0)

# not having enough goodie-points leads to being put into hell
def hell():
    print("Since you have not earned enough goodie-points you are going to hell.")
    exit(0)

# having enough goodie-points leads to being allowed into heaven
def heaven():
    print("Since you have earned enough goodie-points you are going to heaven!")
    exit(0)

# having more than 499 goodie-points leads to moving on towards a new map, even though the player died
def rebirth():
    print("Since you have earned so many goodie-points God grants you another life on a random map!")
    # TO DO: ranom new map xyz
    exit(0)
