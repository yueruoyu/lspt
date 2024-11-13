# Given an integer n, find the maximal number you can obtain by deleting
# exactly one digit of the given number.

def delete_digit(num):
    return max([int(str(num)[:i] + str(num)[i+1:]) 
                for i in range(len(str(num)))])

print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)