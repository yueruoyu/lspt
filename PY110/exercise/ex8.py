# Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

# ExamplesCopy Code


INTEGER_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def string_to_integer(string):
    sum = 0
    for idx in range(-1, -len(string) - 1, -1):
        sum += INTEGER_LIST.index(string[idx]) * (10 ** (-idx - 1))
    return sum



print(string_to_integer("4321"))  # True
print(string_to_integer("570"))    # True