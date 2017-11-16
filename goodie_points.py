# TO DO: do not use a global variable for security reasons
goodie_points_count = 0

def goodie_points(change):

    global goodie_points_count

    # TO FIGURE OUT: why is this line not needed?
    # goodie_points_count = int(goodie_points_count)

    goodie_points_count = goodie_points_count + change

    with open('goodie_points.py', 'r') as goodie_file:
        data = goodie_file.readlines()
        # TO DO: figure out an alternative way of doing this, because it is very static this way
        data[1] = 'goodie_points_count = ' + str(goodie_points_count) + '\n'

    with open('goodie_points.py', 'w') as goodie_file:
        goodie_file.writelines(data)
    print(f"Current count: {goodie_points_count}!")

# TO DO: reset goodie_points_count for each map
'''
def startgame():
    goodie_points_count = 0
'''

# Goodie-point syntax
'''
print("Goodie-points: +/- x")
goodie_points(x)
'''
