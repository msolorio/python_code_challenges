"""
In a certain kingdom, strange mathematics is taught at school. Its main difference from ordinary mathematics is that the numbers in it are not ordered in ascending order, but lexicographically, as in a dictionary (first by the first digit, then, if the first digit is equal, by the second, and so on). In addition, we do not consider an infinite set of natural numbers, but only the first n numbers.

So, for example, if n = 11, then the numbers in strange mathematics are ordered as follows:

1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9.

Help your students to learn this science: write a function that receives two integer numbers: n (total amount of numbers in strange mathematics) and k (number from sequence) and returns the location of a given number k in the order defined in strange mathematics.

For example, if n = 11 and k = 2, the function should return 4 as the answer.

Input: 1 <= n <= 100 000 , 1 <= k <= n.

Output: position of the number k in sequence of the first n natural numbers in lexicographic order. Numbering starts with 1.

Examples:
strange_math(11, 2) == 4
strange_math(15, 5) == 11
strange_math(15, 15) == 7
"""

# GET LIST OF NUMS
# CONVERT LIST OF NUMS TO LIST OF STRINGS
# SORT LIST OF STRINGS IN PLACE
# GET INDEX + 1 OF CHOSEN NUM
def get_num_position(total_nums, chosen_num):
    nums_list = list(range(1, total_nums + 1))
    strings_list = [str(num) for num in nums_list]
    strings_list.sort()

    try:
        return strings_list.index(str(chosen_num)) + 1
    except ValueError:
        return 'Chosen num is not in the list'

# FROM CODEWARS
# def get_num_position(total_nums, chosen_num):
#     return sorted(range(total_nums + 1), key=str).index(chosen_num)