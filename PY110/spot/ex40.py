# Given a List [] of n integers, find the minimum number to be inserted
# in the list, so that the sum of all elements of the list should
# equal the closest prime number.

def minimum_number(lst):
    sum_value = sum(lst)
    while True:
        for i in range(2, sum_value):
            if sum_value % i == 0:
                prime_flag = False
                break
            prime_flag = True
        if prime_flag == False:
            sum_value = sum_value + 1
        else:
            break
    return sum_value - sum(lst)






print(minimum_number([3,1,2]) == 1)
print(minimum_number([5,2]) == 0)
print(minimum_number([1,1,1]) == 0)
print(minimum_number([2,12,8,4,6]) == 5)
print(minimum_number([50,39,49,6,17,28]) == 2)