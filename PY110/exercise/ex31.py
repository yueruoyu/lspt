# Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

# ExamplesCopy Code


def is_balanced(string):
    evaluation = 0
    for letter in string:
        if letter == '(':
            evaluation += 1
        elif letter == ')':
            evaluation -= 1
        if evaluation < 0:
            return False
    if evaluation != 0:
        return False
    return True





print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
# Note that balanced pairs must start with a (, not a ).

