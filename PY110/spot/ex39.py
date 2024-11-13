# Sort the given strings in alphabetical order, case insensitive.


def sortme(lst):
    return sorted(lst, key=str.casefold)

print(sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"])
print(sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"])