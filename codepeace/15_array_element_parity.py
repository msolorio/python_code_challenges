"""
In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.

Examples:

[1, -1, 2, -2, 3] => 3

3 has no matching negative appearance

[-3, 1, 2, 3, -1, -4, -2] => -4

-4 has no matching positive appearance

[1, -1, 2, -2, 3, 3] => 3

(the only-positive or only-negative integer may appear more than once)

Good luck!
"""

# FINDS FIRST ITEM THAT DOES NOT HAVE AN OPPOSITE
def find_orphan(nums_list):
    return next((x for x in nums_list if (x * -1) not in nums_list), None)

# FOUND ON CODEWARS
# GETS ARRAY OF UNIQUE VALUES AND SUMS THEM
# def solve(arr): return sum(set(arr))