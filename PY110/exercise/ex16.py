# Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, and that they have the same number of elements.

# ExampleCopy Code

def interleave(lst1, lst2):
    combined_lst = []
    for i in range(len(lst1)):
        combined_lst.append(lst1[i])
        combined_lst.append(lst2[i])
    return combined_lst




list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True