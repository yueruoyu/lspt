# Write a function that splits the string into pairs of two characters.
# If the string contains an odd number of characters, replace the missing second character of the final pair with an underscore ('_').

def solution(string):
    if len(string) == 0:
        return []
    if len(string) == 1:
        return [f"{string}_"]
    return [string[0:2]] + solution(string[2:])



print(solution('abc') == ['ab', 'c_'])
print(solution('abcdef') == ['ab', 'cd', 'ef'])
print(solution("abcdef") == ["ab", "cd", "ef"])
print(solution("abcdefg") == ["ab", "cd", "ef", "g_"])
print(solution("") == [])