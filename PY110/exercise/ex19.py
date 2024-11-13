# Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

# ExamplesCopy Code

def digit_list(num):
    return [int(ele) for ele in list(str(num))]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
