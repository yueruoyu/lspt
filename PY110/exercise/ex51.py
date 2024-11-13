# Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.

# ExampleCopy Code


def unique_sequence(lst):
    result = []
    result.append(lst[0])
    for ele in lst:
        if result[-1] != ele:
            result.append(ele)
    return result




original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original))      # True