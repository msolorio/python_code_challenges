"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def get_unique_letters(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('Both arguments must be strings')

    str_list = list(str1 + str2)
    sorted_list = sorted(str_list, key=str.lower)
    # remove duplicate characters
    res = []
    for char in sorted_list:
        if char not in res:
            res.append(char)
    
    return ''.join(res)
