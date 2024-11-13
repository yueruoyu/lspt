# As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

# You may not use Python's datetime module.

# ExamplesCopy Code

def after_midnight(string):
    hour = int(string[0:2])
    minute = int(string[3:5])
    return (hour % 24) * 60 + minute

def before_midnight(string):
    hour = int(string[0:2])
    minute = int(string[3:5])
    return ((24 - hour) % 24) * 60 - minute

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
