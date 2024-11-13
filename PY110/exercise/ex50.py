# Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

# ExamplesCopy Code


def staggered_case(original):
    result = ''
    flag = 0
    for idx in range(0, len(original)):
        if ord(original[idx].casefold()) in range(ord('a'), ord('z') + 1):
            if flag == 0:
                result += original[idx].upper()
                flag = 1
            else:
                result += original[idx].lower()
                flag = 0
        else:
            result += original[idx]
    return result




string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True