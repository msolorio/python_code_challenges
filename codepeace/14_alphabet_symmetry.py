"""
Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) = [4, 3, 1]
"""
import string

# Get number of positioned characters in word
def positioned_chars(word):
    lowercase_word = word.lower()
    
    count = 0
    for index, char in enumerate(lowercase_word):
        # if letter position in word == alpha position
        if index == string.ascii_lowercase.index(char):
            count += 1
    
    return count


def get_positioned_chars_for_words(list_of_words):
    return [ positioned_chars(word) for word in list_of_words ]
