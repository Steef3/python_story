# from x import y
from ending_death import ending

# STAGE 1
def forest_start():
  print("You are standing in the middle of a forest.")
  # GOOD PRACTICE: indent each of the possibilities to make it more user-friendly
  print("""You look around and you see four paths.
  One towards the South.
  One towards the North.
  One towards the East.
  One towards the West.
  You stomp onto the ground, because you cannot decide which path you should take and notice that the ground moved.""")
  print("...")
  print("Do you go to either compass direction or stomp some more?")

  choice = input("Choose wisely: ")

  choice = choice.casefold()

  if "south" in choice:
      print("You decided to go towards the South.")
      south()

  elif "north" in choice:
      print("You decided to go towards the North.")
      north()

  elif "east" in choice:
      print("You decided to go towards the East.")
      east()

  elif "west" in choice:
      print("You decided to go towards the West.")
      west()

  elif "stomp" in choice or "ground" in choice:
      print("You decided to stomp more.")
      below()

  else:
      print("You typed in something the game does not understand and that made it explode.")
      # WARNING: make sure to change, when goodie-points are actually implemented
      ending()

# STAGE 2
def south():
    print("South Test.")
def north():
    print("North Test.")
def east():
    print("East Test.")
def west():
    print("West Test.")
def below():
    print("That was a risky idea!!! That one last stomp was too much for the ground and you fall deep down into a cave.")
    # GOODIE POINTS
    print("Destroying ground (especially if it's not yours) is very bad! - 5 goodie-points.")

    print("After recovering from the fall, you see three chests that are all shiny and do not have any locks.")

    # TO DO: figure out how to implement indentation for each decision that is needed
    # GOODIE POINTS
    print("""Each chest has something written on it:
    1. 'Choose a job you love, and you will never have to work a day in your life.' - Confucius
    2. 'Love all, trust a few, do wrong to none.' - William Shakespeare
    3. 'Happiness is not something ready made. It comes from your own actions.' - Dalai Lama""")
    print("Which chest do you open?")

    choice = input("You can only choose one: ")

    choice = choice.casefold()

    # TO DO: improve checking for possible words
    if "1" in choice or "confucius" in choice:
        print("Confucius Test.")
    elif "2" in choice or "william" in choice or "shakespeare" in choice:
        print("Shakespeare Test.")
    elif "3" in choice or "dalai" in choice or "lama" in choice:
        earth_core()

# STAGE 3
def north_west():
    print("North West Test.")
def south_west():
    print("South West Test.")
def north_pole():
    print("North Pole Test.")
def earth_core():
    print("Earth Core Test.")

forest_start()
