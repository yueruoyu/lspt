# A merge sort is a recursive sorting algorithm that works by breaking down a list's elements into nested sub-lists, then combining those nested sub-lists back together in sorted order. It is best explained with an example. Given the list [9, 5, 7, 1, 8, 2, 0, 6], let's walk through the process of sorting it with merge sort. We'll start off by breaking the list down into nested sub-lists:

# Copy Code
# [9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
# [[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
# [[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
# # repeat until each sub-list contains only 1 value
# [[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]
# In the first step, we partition the list into a list of two sub-lists, so that each sub-list contains approximately half of the entries. In the next step, we partition each sub-list in the same way. This process repeats until each of the innermost lists contains exactly one element.

# We now work our way back to a flat list by merging each pair of nested sub-lists in the proper ascending order:

# Copy Code
# [[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] -->
# [[[2, 9], [6, 7]], [[5, 8], [0, 1]]] -->
# [[2, 6, 7, 9], [0, 1, 5, 8]] -->
# [0, 1, 2, 5, 6, 7, 8, 9]
# For example, on the 2nd line, we merge [2, 9] with [6, 7], which becomes `[2, 6, 7, 9].

# Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order. The function should sort the list using the merge sort algorithm as described above. You may assume that every element of the list will have the same data type: either all numbers or all strings.

# Feel free to use the merge function you wrote in the previous exercise.

# ExamplesCopy Code
# # All of these examples should print True

def merge(list1, list2):
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2


# def merge_sort(lst):
#     processed = [[ele] for ele in lst]
#     result = []
#     while len(processed) != 1:
#         while len(processed) > 1:
#             result.append(merge(processed[0], processed[1]))
#             processed.pop(0)
#             processed.pop(0)
#         if len(processed) == 1:
#             result.append(processed[0])
#         processed = result.copy()
#         result = []
#         print(processed)
#     return processed[0]

def merge_sort(lst):

    if len(lst) == 1:
        return lst

    sublst1 = lst[:len(lst)//2]
    sublst2 = lst[len(lst)//2:]

    return merge(merge_sort(sublst1), merge_sort(sublst2))

print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)