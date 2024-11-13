# Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

# ExampleCopy Code


def multiply_list(lst1, lst2):
    lst3 = zip(lst1, lst2)
    result_lst = []
    for ele in lst3:
        a, b = ele
        result_lst.append(a * b)
    return result_lst


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True