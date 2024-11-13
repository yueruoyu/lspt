# Given a list of strings, return a new list where the strings are sorted based on the 
# highest number of adjacent consonants a string contains. If two strings contain the 
# same highest number of adjacent consonants, they should retain their original order 
# in relation to each other. Consonants are considered adjacent if they are next to 
# each other in the same word or if there is a space between two consonants in adjacent words.

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def sort_by_most_adjacent_consonants(string_lst):
    return_lst = string_lst.copy()
    return_lst.sort(key = most_consonants, reverse = True)
    return return_lst


# def most_consonants(string):
#     highest_counter = 0
#     string = string.replace(' ', '')
#     for i in range(len(string) - 1):
#         if string[i] not in CONSONANTS:
#             continue
#         j = i + 1
#         while string[j].casefold() in CONSONANTS:
#             j += 1
#             if j == len(string):
#                 break
#         if (j - i) >= 2 and (j - i) > highest_counter:
#             highest_counter = j - i + 1
#     return highest_counter

def most_consonants(string):
    highest_counter = 0
    string = string.replace(' ', '')
    consonant_lst = []
    for letter in string:
        if letter in CONSONANTS:
            consonant_lst.append(letter)
            if len(consonant_lst) >= 2 and len(consonant_lst) > highest_counter:
                highest_counter = len(consonant_lst)
        else:
            if len(consonant_lst) >= 2 and len(consonant_lst) > highest_counter:
                highest_counter = len(consonant_lst)
            consonant_lst.clear()
    return highest_counter

        

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_most_adjacent_consonants(my_list))
my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_most_adjacent_consonants(my_list))
my_list = ['day', 'week', 'month', 'year']
print(sort_by_most_adjacent_consonants(my_list))

        