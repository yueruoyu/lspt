# Write a function that takes two strings as input, `full_text` and `search_text`,
# and returns the number of times `search_text` appears in `full_text`.

# Examples:

def solution(string, substring):
    return string.count(substring)

print(solution('abcdeb','b')) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb')) # should return 1