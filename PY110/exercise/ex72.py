# Write a function that takes a string and returns a dictionary containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

# You may assume that the string will always contain at least one character.

# ExamplesCopy Code

def letter_percentages(string):
    qty_lower = 0
    qty_upper = 0
    qty_neither = 0
    for char in string:
        if ord(char) in range(ord('a'), ord('z') + 1):
            qty_lower += 1
        elif ord(char) in range(ord('A'), ord('Z') + 1):
            qty_upper += 1
        else:
            qty_neither += 1
    return {
    'lowercase': f"{qty_lower / len(string) * 100:.02f}",
    'uppercase': f"{qty_upper / len(string) * 100:.02f}",
    'neither': f"{qty_neither / len(string) * 100:.02f}",
    }



expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)