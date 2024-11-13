# Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

# ExamplesCopy Code

def century(year):
    century = (year - 1) // 100 + 1
    check_century = '0' + (str(century))
    match check_century[-1]:
        case "1":
            if check_century[-2] != '1':
                return str(century) + 'st'
            else:
                return str(century) + 'th'
        case "2":
            if check_century[-2] != '1':
                return str(century) + 'nd'
            else:
                return str(century) + 'th'
        case "3":
            if check_century[-2] != '1':
                return str(century) + 'rd'
            else:
                return str(century) + 'th'
        case _:
            return str(century) + 'th'


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True