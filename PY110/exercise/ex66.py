# Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

# ExampleCopy Code


num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven':'7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
}

def word_to_digit(sentence):
    word_lst = sentence.split()
    converted_lst = []
    for word in word_lst:
        if word in num_dict:
            converted_lst.append(num_dict[word])
        else:
            converted_lst.append(word)
    return ' '.join(converted_lst)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True