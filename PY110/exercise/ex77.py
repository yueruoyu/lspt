# Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.

# ExamplesCopy Code

def sum_square_difference(num):
    sum1 = 0
    sum2 = 0

    for i in range(1, num + 1):
        sum1 += i
        sum2 += i**2
    return sum1**2 -sum2



print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True