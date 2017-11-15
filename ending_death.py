from sys import exit

# defines how a game ends, in case the player dies
# system used on every map

# usage: ending(goodie_points)
def ending():

    # this print is for testing only
    # TO DO: make sure that it will be changed to the actual number of goodie_points that the player has
    print("Please input a number!")
    goodie_points = input("> ")
    goodie_points = int(goodie_points)

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
