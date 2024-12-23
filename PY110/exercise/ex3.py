# Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.



def is_real_palindrome(string):
    real_string = ''
    for char in string:
        if char.isalnum():
            real_string += char.casefold()
    return real_string[::-1] == real_string





print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

print(is_real_palindrome('Madam') == True)           # True

print(is_real_palindrome("Madam, I'm Adam") == True) # True