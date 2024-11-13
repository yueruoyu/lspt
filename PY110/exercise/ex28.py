# Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

# ExampleCopy Code
def swap_name(name):
    full_name = name.split()
    first_name = full_name.pop(0)
    last_name = full_name.pop(-1)
    middle_name = ' '.join(full_name)
    if middle_name:
        return f"{last_name}, {first_name} {middle_name}"
    else:
        return f"{last_name}, {first_name}"


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson") 
# You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").