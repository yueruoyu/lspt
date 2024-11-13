# Write a function that takes a string of integers as input and returns the
# number of substrings that result in an odd number when converted to an integer.

# Examples:

def solve(string):
    count = 0
    for i in range(len(string)):
        if int(string[i]) % 2 == 1:
            count += i + 1
    return count

print(solve("1341")) # should return 7
print(solve("1357")) # should return 10