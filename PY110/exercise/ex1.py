# Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

# Example 1Copy Code
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.
# Example 2Copy Code
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.


num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")
num3 = input("Enter the 3rd number: ")
num4 = input("Enter the 4th number: ")
num5 = input("Enter the 5th number: ")
num6 = input("Enter the last number: ")

if num6 in [num1, num2, num3, num4, num5]:
    print(f"{num6} is in {num1},{num2},{num3},{num4},{num5}.")
else:
    print(f"{num6} isn't in {num1},{num2},{num3},{num4},{num5}.")

print