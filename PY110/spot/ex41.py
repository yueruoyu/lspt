# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the input string.

def duplicate_count(string):
    string = string.casefold()
    count_dict ={}
    for char in string:
        if char not in count_dict:
            count_dict[char] = string.count(char)
    count = 0
    for v in list(count_dict.values()):
        if v >= 2:
            count += 1
    return count

print(duplicate_count("") == 0)
print(duplicate_count("abcde") == 0)
print(duplicate_count("abcdeaa") == 1)
print(duplicate_count("abcdeaB") == 2)
print(duplicate_count("Indivisibilities") == 2)