# Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

# Note: You can use the following constant to represent the degree symbol:

# Copy Code
DEGREE = "\u00B0"
# ExamplesCopy Code
# # All of these examples should print True


def dms(angle):
    degree_value = int(angle)
    minutes_value = int((angle - degree_value) * 60)
    second_value = int(((angle - degree_value) * 60 - minutes_value) * 60)
    return f"{degree_value}\u00B0{minutes_value:02d}'{second_value:02d}\""

print(dms(30))
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773))
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

