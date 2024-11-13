# The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

# You may not use Python's datetime module.

# ExamplesCopy Code

# Disregard Daylight Savings and Standard Time and other complications.


def time_of_day(num):
    raw_hour, minute = divmod(num, 60)
    if raw_hour < 24:
        hour = raw_hour - (raw_hour // 24) * 24
    else:
        hour, _ = divmod(raw_hour, 24)
    return f"{hour:02d}:{minute:02d}"



print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True