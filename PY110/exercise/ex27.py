# Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

# You may assume that the argument will always be a positive integer.

# ExamplesCopy Code


def sequence(num):
    return list(range(1, num + 1))
    # result_lst = []
    # for idx in range(num):
    #     result_lst.append(idx + 1)
    # return result_lst


print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True