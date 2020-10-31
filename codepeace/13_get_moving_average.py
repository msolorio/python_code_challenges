"""
Task
Given a list values of integers and an integer n representing size of the window, calculate and return the moving average.

When integer n is equal to zero or the size of values list is less than window's size, return None

Example:

Values: [1, 2, 3, 4, 5]
Window size: 3

Moving average is calculated as:


 1, 2, 3, 4, 5
 |     |
 ^^^^^^^
 (1+2+3)/3 = 2


  1, 2, 3, 4, 5
     |     |
     ^^^^^^^
     (2+3+4)/3 = 3


  1, 2, 3, 4, 5
        |     |
        ^^^^^^^
        (3+4+5)/3 = 4

Here, the moving average would be [2, 3, 4]
"""

# get average of nums between i and i + size_of_window
def get_average(index, list, size_of_window):
    subset = list[index:index + size_of_window]

    return sum(subset) / len(subset)


def get_moving_average(list_of_nums, size_of_window):
    if size_of_window == 0 or size_of_window > len(list_of_nums):
        return None

    averages = []

    for index in range(0, len(list_of_nums) - size_of_window + 1):
        average = get_average(index, list_of_nums, size_of_window)
        averages.append(average)
    
    return averages
