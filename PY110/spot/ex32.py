# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.


def alphabet_position(string):
    return_str = ''
    for char in string:
        if char.isalpha():
            return_str = return_str + ' ' + str(ord(char.casefold()) - ord('a') + 1)
    return_str = return_str.strip()
    return return_str




print(alphabet_position("The sunset sets at twelve o' clock."))
# == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("-.-'") == "")