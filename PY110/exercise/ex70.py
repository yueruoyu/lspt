# Our recursive fibonacci function from the previous exercise isn't very efficient. It starts slowing down with an nth argument value somewhere around 35-60, depending on your system. One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

# Memoization is an approach that involves saving a computed answer for future reuse, instead of computing it from scratch every time it is needed. In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2) because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).

# For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

# An image representing the computation of the 7th Fibonacci number is shown below. It is the same image that was shown in the previous exercise, except this one highlights the values that have previously been computed.

# Fibonacci Memoization

# Hint: One approach to memoization is to use a lookup table, such as an object, for storing and accessing previously computed values.

fibo_dict = {}
def fibo(num):
    if num in [1, 2]:
        return 1
    elif num in fibo_dict:
        return fibo_dict[num]
    else:
        fibo_dict[num] = fibo(num -1) + fibo(num -2)
    return fibo_dict[num]