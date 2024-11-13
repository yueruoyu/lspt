# Write a function `generate_hashtag(s)` that generates a hashtag from the given string `s`.

# Rules:
# - The hashtag must start with a '#' symbol.
# - All words in the hashtag must start with a capital letter.
# - If the resulting hashtag is longer than 140 characters, the function should return `False`.
# - If the input string or the resulting hashtag is an empty string, the function should return `False`.

# Examples:


def generate_hashtag(string):
    if string == '' or len(string) >= 140 or not string.strip()[0].isalpha():
        return False
    capital_tag = True
    result ='#'
    for char in string:
        if char == ' ':
            capital_tag = True
        elif char.isalpha() and capital_tag == True:
            result = result + char.upper()
            capital_tag = False
        elif char.isalpha() and capital_tag == False:
            result = result + char.lower()
    return result


print(generate_hashtag(""))                       # should return `False`
print(generate_hashtag(" " * 200))                # should return `False`
print(generate_hashtag("Do We have A Hashtag"))   # should return "#DoWeHaveAHashtag"
print(generate_hashtag("Nice To Meet You"))       # should return "#NiceToMeetYou"
print(generate_hashtag("this is a test"))         # should return "#ThisIsATest"
print(generate_hashtag("this is a very long string" + " " * 140 + "end"))  # should return "#ThisIsAVeryLongStringEnd"
print(generate_hashtag("a" * 139))                # should return "#A" + "a" * 138
print(generate_hashtag("a" * 140))                # should return `False`