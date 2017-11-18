# from x import y
from ending_death import ending
from goodie_points import goodie_points

# STAGE 1
def mountain_start():
  print("You find yourself at the bottom of a mountain.")

# STAGE 2
def first_stage():
    pass

# STAGE 3
def long_path():
    pass
def rest_first_stage():
    ending()

# STAGE 4
def long_path_right():
    pass
def long_path_left():
    pass
def direct_climbing():
    pass

# STAGE 5
def dead_end():
    ending()
def plateau():
    pass
def stuck():
    pass

# STAGE 6 or 7
# climb_down can be called either after stuck() or after wait()
def climb_down():
    ending()

# STAGE 6
def cave_left():
    pass
def cave_middle():
    pass
def cave_right():
    pass
def wait():
    pass

# STAGE 7
def dragon():
    pass
def phoenix():
    pass
def wait_more():
    pass

# STAGE 7/8, depending on path
def top():
    ending()

mountain_start()
