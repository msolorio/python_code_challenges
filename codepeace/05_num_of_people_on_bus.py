"""
There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.

example
[[5, 0], [3, 5]] => 3 
"""
from functools import reduce
###############################################################
## USING REDUCE

# def num_of_people_on_bus(bus_stop_data):
#     return reduce(lambda a,b: a + b[0] - b[1], bus_stop_data, 0)

###############################################################
## ANOTHER WAY
def num_of_people_on_bus(bus_stop_data):
    total = 0

    for stop in bus_stop_data:
        total = total + stop[0] - stop[1]

    return total
