# Write a function that takes a list of words as input and returns a list of
# integers. Each integer represents the count of letters in the word that occupy
# their positions in the alphabet.

# Examples:

def solve(lst):
    count_list = []
    for word in lst:
        count = 0
        for i in range(len(word)):
            if ord(word[i].casefold()) - ord('a') == i:
                count += 1
        count_list.append(count)
    return count_list

print(solve(["abode","ABc","xyzD"])) # should return [4, 3, 1]
print(solve(["abide","ABc","xyz"])) # should return [4, 3, 0]