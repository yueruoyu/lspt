# Given two words, determine the number of letters you need to remove from them to make them anagrams.


def anagram_difference(str1, str2):
    while True:
        check = (set(str1) & set(str2))
        if len(check) == 0:
            break
        delete_item = check.pop()
        str1 = str1.replace(str(delete_item), '', 1)
        str2 = str2.replace(str(delete_item), '', 1)
    return len(str1) + len(str2)
    


print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('abc', 'aabbbbc'))