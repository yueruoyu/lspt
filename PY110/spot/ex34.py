# Create a function that turns a string into a Wave. You will be passed a string
# and you must return that string in an array where an uppercase letter is a person standing up.


# def wave(string):
#     word_list =[]
#     time = len(string.replace(' ', ''))
#     for i in range(time):
#         word =''
#         count = 0
#         for char in string: 
#             if not char.isalpha():
#                 word = word + char
#             else:
#                 if count == i:
#                     word = word + char.upper()
#                     count += 1
#                 else:
#                     word = word + char.lower()
#                     count += 1
#         word_list.append(word)
#     return word_list

def wave(string):
    return [string[:i].lower() + string[i].upper() + string[i+1:].lower() 
            for i in range(len(string)) if string[i].isalpha()]


print(wave("hello"))
 # ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
print(wave("") == [])
print(wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])
print(wave(" gap ") == [" Gap ", " gAp ", " gaP "])