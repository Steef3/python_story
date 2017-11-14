# from x import y

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

  # TO DO: change all the strings to be independent of lower or capital letters
  if "south" in choice or "South" in choice:
      print("You decided to go towards the South.")

  elif "north" in choice or "North" in choice:
      print("You decided to go towards the North.")

  elif "east" in choice or "East" in choice:
      print("You decided to go towards the East.")

  elif "west" in choice or "West" in choice:
      print("You decided to go towards the West.")

  elif "stomp" in choice:
      print("You decided to stomp more.")
      print("That was a risky idea!!! That one last stomp was too much for the ground and you fall deep down into a cave.")
      print("Destroying ground (especially if it's not yours) is very bad! - 5 goodie-points.")

      # TO DO: implement goodie_points here
      print("After recovering from the fall, you see three chests that are all shiny and do not have any locks.")

      # TO DO: figure out how to implement indentation for each decision that is needed
      print("""Each chest has something written on it:
      'Inspirational quote 1'
      'Inspirational quote 2'
      'Inspirational quote 3'""")
      print("Which chest do you open?")

  else:
      print("You typed in something the game does not understand and that made it explode.")
      # TO DO: implement ending()

forest_start()
