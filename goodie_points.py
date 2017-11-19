# TO DO: do not use a global variable for security reasons
goodie_points_count = 0

def goodie_points(change):

    global goodie_points_count

    # TO FIGURE OUT: why is this line not needed?
    # goodie_points_count = int(goodie_points_count)

    if change < 0:
        print("Goodie-points: {}".format(change))
    elif change == 0:
        print("Goodie-points: 0")
    elif change >= 0:
        print(f"Goodie-points: +{change}")
    # the following should never actually run
    else:
        print("The game broke, please restart!")
        exit(0)

    goodie_points_count = goodie_points_count + change

    with open('goodie_points.py', 'r') as goodie_file:
        data = goodie_file.readlines()
        # TO DO: figure out an alternative way of doing this, because it is very static this way
        data[1] = 'goodie_points_count = ' + str(goodie_points_count) + '\n'

    with open('goodie_points.py', 'w') as goodie_file:
        goodie_file.writelines(data)
    print(f"Current count: {goodie_points_count}!")

# Goodie-point syntax and info
'''
goodie_points(x)
'''
