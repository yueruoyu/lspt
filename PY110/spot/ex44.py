# Given two arrays a and b write a function comp(a, b) that checks whether
# the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in `b` are the elements in `a` squared,
# regardless of the order.

def comp(lst1, lst2):
    if (not lst1) or len(lst1) != len(lst2):
        return False
    squared_lst1 = [num**2 for num in lst1]
    for num in squared_lst1:
        try:
            lst2.remove(num)
        except ValueError:
            return False
    return lst2 == []


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)
print(comp(None, [1, 2, 3]) == False)
print(comp([1, 2], []) == False)
print(comp([1, 2], [1, 4, 4]) == False)