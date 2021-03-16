"""
Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.

ORIGINAL
def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
    if (spl(i).length > longest): longest = spl[i].length
    return longest
"""

# SOLUTION
# def find_longest(str):
#     spl = str.split(" ")
#     longest = 0
#     i = 0

#     while (i < len(spl)):
#         if (len(spl[i]) > longest): longest = len(spl[i])
#         i += 1

#     return longest

# I DID IT MYYYYYY WAY 🎶
# GIVEN A STRING OF WORDS OUTPUT THE LENGTH OF THE LONGEST WORD
def get_longest_word(sentence):
    words = sentence.split(' ')
    lengths = [len(word) for word in words]

    return max(lengths)
