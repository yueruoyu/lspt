# Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits 
# in the given string of digits.

def greatest_product(s):
    return max([int(s[i]) * int(s[i+1]) * int(s[i+2]) * int(s[i+3]) * int(s[i+4]) 
            for i in range(len(s) - 4)])

print(greatest_product("123834539327238239583") == 3240)
print(greatest_product("395831238345393272382") == 3240)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("02494037820244202221011110532909999") == 0)