"""
Remember the pyramid of balls in billiards? To build a classic pyramid (5 levels) you need 15 balls. With 3 balls you can build a 2-level pyramid, etc.

For more examples,

pyramid(1) == 1

pyramid(3) == 2

pyramid(6) == 3

pyramid(10) == 4

pyramid(15) == 5
Write a function that takes number of balls (≥ 1) and calculates how many levels you can build a pyramid.
"""

def get_pyramid_levels(num_of_balls):
    levels = 1

    while num_of_balls >= levels:
        num_of_balls -= levels
        levels += 1

    return levels - 1
