# In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

# Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.

# ExamplesCopy Code
INTEGER_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def string_to_integer(string):
    sum = 0
    for idx in range(-1, -len(string) - 1, -1):
        sum += INTEGER_LIST.index(string[idx]) * (10 ** (-idx - 1))
    return sum


def string_to_signed_integer(string):
    if '-' in string:
        return - string_to_integer(string.replace('-', ''))
    else:
        return string_to_integer(string.replace('+', ''))




print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True