from math import prod 

def compute_sum(nums):
    return sum(num for num in nums)

def compute_product(nums):
    return prod(num for num in nums)

valid_nums = False
while True:
    try:
        if not valid_nums:
            nums = [int(num) for num in input("Please enter a list of space separated integers greater than 0: ").split()]
            if not nums:
                print("Must enter at least one integer.")
                continue
        else:
            sum_or_product = input('Enter "s" to compute the sum, or "p" to compute the product. ')
    except ValueError:
        print("Error: non-integer input. Please enter a valid integer.")
    else:
        negative_ints = [num for num in nums
                        if num <= 0]
        if negative_ints:
            print(f"Error: non-positive integer input(s): {", ".join(str(num) for num in negative_ints)}")
        else:
            valid_nums = True
            sum_or_product = input('Enter "s" to compute the sum, or "p" to compute the product. ')
            match sum_or_product:
                case 's':
                    print(f'The sum of the integers {", ".join(str(num) for num in nums)} is {compute_sum(nums)}')
                    break
                case 'p':
                    print(f'The product of the integers {", ".join(str(num) for num in nums)} is {compute_product(nums)}')
                    break
                case _:
                    print("Error: input must either be for sum or product, 's' or 'p'")