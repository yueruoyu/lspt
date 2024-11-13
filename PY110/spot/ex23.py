# Write a function `longest(s)` that finds and returns the longest substring of
# `s` where the characters are in alphabetical order.

# Example:


def longest(string):
    storage =''
    count = 0
    for char in string:
        if storage == '' or ord(char) >= ord(storage[-1]):
            storage = storage + char
            if count < len(storage):
                count = len(storage)
                result = storage
        else:
            storage = char
    return result




print(longest('asd'))                  # should return 'as'
print(longest('nab'))                 # should return 'ab'
print(longest('abcdeapbcdef'))         # should return 'abcde'
print(longest('asdfaaaabbbbcttavvfffffdf')) # should return 'aaaabbbbctt'
print(longest('asdfbyfgiklag'))        # should return 'fgikl'
print(longest('z'))                    # should return 'z'
print(longest('zyba'))s                 # should return 'z'