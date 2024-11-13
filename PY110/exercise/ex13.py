# Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

# ExampleCopy Code

# def union(lst1, lst2):
#     return set(lst1) | set(lst2)

def union(lst1, lst2):
    lst1.extend(lst2)

print(union([1, 3, 5], [3, 6, 9])) # True
