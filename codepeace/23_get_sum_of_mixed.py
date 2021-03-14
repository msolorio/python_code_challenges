"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
"""

def get_sum_of_mixed(nums_list):
    true_nums = [int(item) for item in nums_list]

    return sum(true_nums)

# From Codewars
# def get_sum_of_mixed(nums_list):
#     return sum(map(int, nums_list))
