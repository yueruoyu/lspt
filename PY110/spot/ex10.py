# Write a function that, given a string of text, returns a list of the top-3 most
# occurring words, in descending order of the number of occurrences.

# Assumptions:
# - A word is a string of letters (A to Z) optionally containing one or more apostrophes (').
# - Matches should be case-insensitive.
# - Ties may be broken arbitrarily.
# - If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty list if a text contains no words.

# Examples:

def is_word(string):
    return any([char.isalpha() for char in string])


def top_3_words(sentence):
    top_dict ={}
    word_lst = [word.casefold() for word in sentence.split()]
    for word in word_lst:
        if is_word(word):
            top_dict[word] = word_lst.count(word)

    top_list = list(top_dict.keys())
    top_list.sort(key=top_dict.get, reverse=True)
    return top_list[:3]


from collections import Counter
import re

def top_3_words(text):
    # Use a regex to find all words (case-insensitive) allowing letters and apostrophes
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())
    
    # Filter out words that consist only of apostrophes
    words = [word for word in words if re.search(r"[a-zA-Z]", word)]
    
    # Count occurrences of each word
    word_counts = Counter(words)
    
    # Get the top 3 most common words
    top_words = [word for word, count in word_counts.most_common(3)]
    
    return top_words


print(top_3_words(" , e .. ")) # ["e"]
print(top_3_words(" ... ")) # []
print(top_3_words(" ' ")) # []
print(top_3_words(" ''' ")) # []
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")) # should return ["a", "of", "on"]