# TO DO: do not use a global variable for security reasons
goodie_points_count = 0

# TO DO: display the number of gained goodie-points automatically, instead of printing them every time separately

def goodie_points(change):

    global goodie_points_count

    # TO FIGURE OUT: why is this line not needed?
    # goodie_points_count = int(goodie_points_count)

    # TO DO: add + for positive goodie-points/make distinction between - and +
    if change < 0:
        print("Goodie-points: {}".format(change))
    elif change == 0:
        print("Goodie-points: 0")
    elif change >= 0:
        print(f"Goodie-points: +{change}")
    # the following should never actually run
    else:
        print("The game broke, please restart!")

    goodie_points_count = goodie_points_count + change

    with open('goodie_points.py', 'r') as goodie_file:
        data = goodie_file.readlines()
        # TO DO: figure out an alternative way of doing this, because it is very static this way
        data[1] = 'goodie_points_count = ' + str(goodie_points_count) + '\n'

    with open('goodie_points.py', 'w') as goodie_file:
        goodie_file.writelines(data)
    print(f"Current count: {goodie_points_count}!")

# Goodie-point syntax
'''
print("Goodie-points: +/-x")
goodie_points(x)
'''
