"""
Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.
"""


# FOR EACH CHARACTER IN STRING
# CHECK HOW MANY INSTANCES OF THAT CHAR IN STRING
# IF MORE THAN ONE RETURN FALSE
# def has_unique_chars(string):
#     for char in string:
#         instances = len(['' for l in string if l == char])
        
#         if instances > 1: return False
    
#     return True



# FOR EACH CHAR SEARCH FOR CHAR LATER IN STRING
# IF FIND RETURNS ANYTHING OTHER THAN -1 THE CHAR IS NOT UNIQUE
def has_unique_chars(str):
    for idx, char in enumerate(str):
        if str.find(char, idx + 1) != -1: return False

    return True

# CODEWARS
# def has_unique_chars(str):
#     return len(str) == len(set(str))