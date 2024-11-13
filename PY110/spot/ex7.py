# Write a function that takes a list of words and constructs a new word by
# concatenating the nth letter from each word, where n is the position of the
# word in the list.
# Example:

def nth_char(lst):
    string =''
    for i, word in enumerate(lst):
        string += word[i]
    return string



print(nth_char(['yoda', 'best', 'has'])) # should return 'yes'