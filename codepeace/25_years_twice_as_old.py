"""
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son is currently (or in how many years he will be twice as old as his son is currently).
"""

def get_years(fathers_age, sons_age):
    return abs(fathers_age - (2 * sons_age))
