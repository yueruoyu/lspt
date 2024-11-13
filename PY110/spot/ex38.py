# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols and return the final state of the string.

def clean_string(string):
    clean_string = ''
    for char in string:
        if char == '#':
            clean_string = clean_string[:len(clean_string)-1]
        else:
            clean_string = clean_string + char
    return clean_string

print(clean_string('abc#d##c') == "ac")
print(clean_string('abc####d##c#') == "")