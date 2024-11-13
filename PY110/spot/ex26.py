# Create a function that takes two integer arrays of equal length, compares the value of each member in one array to the corresponding member in the other, 
# squares the absolute value difference between those two values, and returns the average of those squared absolute value differences between each member pair.

# Examples
# [1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2] --> 16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1] --> 1 because (1 + 1) / 2

def solution(lst1, lst2):
    return sum((a-b)**2 for a, b in zip(lst1, lst2))/len(lst1)


print(solution([1, 2, 3], [4, 5, 6]) == 9)
print(solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5)
print(solution([-1, 0], [0, -1]) == 1)