# Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.

# ExamplesCopy Code

def staggered_case(original):
    result = ''
    for idx in range(0, len(original)):
        if ord(original[idx].casefold()) in range(ord('a'), ord('z') + 1):
            if idx % 2 == 0:
                result += original[idx].upper()
            else:
                result += original[idx].lower()
        else:
            result += original[idx]
    return result




string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True