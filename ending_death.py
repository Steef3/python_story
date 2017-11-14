from sys import exit

print("Please input a number!")
goodie_points = input("> ")
goodie_points = int(goodie_points)

# defines how a game ends, in case the player dies
# system used on every map
def ending(x):
    if x < 100:
        hell()
    elif x >= 100 and x < 500:
        heaven()
    elif x >= 500:
        rebirth()
    # the following line will not be effective ever, since goodie_points are always an integer
    # python will result in an error, if the goodie_points are anything else than an integer
    else:
        print("You broke the game...")
        exit(0)

# not having enough goodie-points leads to being put into hell
def hell():
    print("You died. Since you have not earned enough goodie-points you are going to hell.")
    exit(0)

# having enough goodie-points leads to being allowed into heaven
def heaven():
    print("You died. Since you have earned enough goodie-points you are going to heaven!")
    exit(0)

# having more than 499 goodie-points leads to moving on towards a new map, even though the player died
def rebirth():
    print("You died. Since you have earned so many goodie-points God grants you another life on a random map!")
    # map xyz
    exit(0)

ending(goodie_points)
