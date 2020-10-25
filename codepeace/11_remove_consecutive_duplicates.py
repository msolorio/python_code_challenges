"""
Your task is to remove all consecutive duplicate words from string, leaving only first words entries. For example:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"
"""

def remove_consecutive_duplicates(s):
    words_list = s.split(' ')

    # iterate over list filtering out items that are repeats
    # of one before
    unique_words = []
    for index, word in enumerate(words_list):
        if index == 0 or word != words_list[index - 1]:
            unique_words.append(word)

    return ' '.join(unique_words)

