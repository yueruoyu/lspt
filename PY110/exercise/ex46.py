# Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.

# ExampleCopy Code

def multiply_items(lst1, lst2):
    return [item[0] * item[1] for item in list(zip(lst1, lst2))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True