# Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

# You may assume that only ASCII characters will be included in the argument.

# ExamplesCopy Code
# All of these examples should print True

CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def double_consonants(string):
    result_string = ''
    for letter in string:
        if letter.casefold() in CONSONANTS:
            result_string += letter * 2
        else:
            result_string += letter
    return result_string



print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
