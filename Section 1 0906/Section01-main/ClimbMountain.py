# File: ClimbMountain.py

"""
This program teaches Karel to climb a stair-step
mountain and plant a flag at the top.
"""

"""
Potential Questions of Karel:
turn_left()         turn_right()
turn_around()
front_is_clear() 	front_is_blocked()
left_is_clear() 	left_is_blocked()
right_is_clear() 	right_is_blocked()
beepers_present() 	no_beepers_present()
beepers_in_bag() 	no_beepers_in_bag()
facing_north() 	not_facing_north()
facing_south() 	not_facing_south()
facing_east() 	not_facing_east()
facing_west() 	not_facing_west()
"""
"""inflection_point()step_down()"""

import karel

def climb_mountain():
    """Climbs a stair-step mountain of any size."""
    move_to_wall()
    step_up()
    inflection_point()

def step_up():
    """Climbs one step directly ahead of Karel."""
    while front_is_blocked():
            turn_left()
            move()
            turn_right()
            move()


def move_to_wall():
    """Moves Karel forward until it is blocked."""
    while front_is_clear():
        move()


def turn_right():
     turn_left()
     turn_left()
     turn_left()


def inflection_point():
     if front_is_clear() and left_is_clear():
          put_beeper()
          move()
          turn_right()





def turn_around():
     turn_left()
     turn_left()