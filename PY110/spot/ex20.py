# Write a function that takes a string as an argument and groups the
# number of times each character appears in the string as a dictionary
# sorted by the highest number of occurrences.

# The characters should be sorted alphabetically, and you should ignore
# spaces, special characters, and count uppercase letters as lowercase ones.

# Examples:

def get_char_count(string):
    temp_dict = {}
    result_dict = {}
    for char in string:
        if char.isalnum():
            temp_dict[char.casefold()] = temp_dict.get(char, 0) + 1
    for num in sorted(list(temp_dict.values()), reverse = True):
         result_dict[num] = sorted([k for k, v in temp_dict.items() 
                                      if v == num])
    return result_dict


print(get_char_count("Mississippi")) # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
print(get_char_count("Hello. Hello? HELLO!!") )# should return {6: ['l'], 3: ['e', 'h', 'o']}
print(get_char_count("aaa...bb...c!")) # should return {3: ['a'], 2: ['b'], 1: ['c']}
print(get_char_count("aaabbbccc")) # should return {3: ['a', 'b', 'c']}
print(get_char_count("abc123")) # should return {1: ['1', '2', '3', 'a', 'b', 'c']}