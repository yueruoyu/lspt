# In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

# Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

# You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

# ExamplesCopy Code

INTEGER_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def integer_to_string(num):
    string = ''
    if num == 0:
        return '0'
    while num != 0:
        string = INTEGER_LIST[num % 10] + string
        num = num // 10
    return string





print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
