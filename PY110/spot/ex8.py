# Write a function that takes a non-empty string `s` as input and finds the
# minimum substring `t` and the maximum number `k`, such that the entire string
# `s` is equal to `t` repeated `k` times.

# Examples:

def f(s):
    for i in range(len(s)):
        if s[:i + 1] * (len(s) // len(s[: i + 1])) == s:
            return [s[: i + 1], len(s) // len(s[: i + 1])]

print(f("ababab")) # should return ["ab", 3]