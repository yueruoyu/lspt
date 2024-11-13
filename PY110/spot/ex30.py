# Write a function to determine if two words are anagrams of each other.



def is_anagram(str1, str2):
    return sorted(str1.casefold()) == sorted(str2.casefold())


print(is_anagram('Creative', 'Reactive') == True)
print(is_anagram("foefet", "toffee") == True)
print(is_anagram("Buckethead", "DeathCubeK") == True)
print(is_anagram("Twoo", "WooT") == True)
print(is_anagram("dumble", "bumble") == False)