# Write a function that takes a list of integers as input and counts the number of
# pairs in the list. A pair is defined as two equal integers separated by some
# other integer(s).

# Examples:
def pairs(lst):
    count = 0
    for i in range(len(lst)-2):
        for j in range(i+2, len(lst)):
            if lst[i] == lst[j]:
                count += 1
    return count

print(pairs([1, 2, 5, 6, 5, 2]))
# --> 2
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]))
# --> 4