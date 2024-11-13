# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

# ExamplesCopy Code

def repeater(string):
    double_string = ''
    for letter in string:
        double_string += letter * 2
    return double_string


print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True