# Write a function that takes a lowercase string as input and returns the
# length of the longest substring that consists entirely of vowels (a, e, i, o, u).

# Examples:


def solve(string):
    vowels_list = []
    count = 0
    for char in string:
        if char in 'aeiou':
            vowels_list.append(char)
            if len(vowels_list) > count:
                count = len(vowels_list)
        else:
            if len(vowels_list) > count:
                count = len(vowels_list)
            vowels_list = []
    return count


print(solve("roadwarriors")) # should return 2
print(solve("suoideaaeiou")) # should return 3