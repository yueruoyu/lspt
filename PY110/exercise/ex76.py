# A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

# Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

# NOTE: The largest possible featured number is 9876543201.

# ExamplesCopy Code

def unique_check(number):
    for char in '0123456789':
        if str(number).count(char) >= 2:
            return False
    return True



def next_featured(num):
    if num >= 9876543201:
        return ("There is no possible number that "
                "fulfills those requirements.")
    potential_feature_number = num + 1
    while (potential_feature_number % 2 == 0 or 
            potential_feature_number % 7 != 0 or 
            not unique_check(potential_feature_number)):
        potential_feature_number += 1
    return potential_feature_number





print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True