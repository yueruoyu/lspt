# Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

# ExamplesCopy Code
# # All of these examples should print True

def multiplicative_average(lst):
    product = 1
    for num in lst:
        product *= num
    return f"{product / len(lst):.3f}"


print(multiplicative_average([3, 5]))
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")