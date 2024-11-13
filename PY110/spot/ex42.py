# Mothers arranged a dance party for the children in school. At that party,
# there are only mothers and their children. All are having great fun on the
# dance floor when suddenly all the lights went out. It's a dark night and no
# one can see each other. But you were flying nearby and you can see in the
# dark and have ability to teleport people anywhere you want.
# Legend:
# - Uppercase letters stands for mothers, lowercase stand for their children,
# i.e. "A" mother's children are "aaaa".
# - Function input: String contains only letters, uppercase letters are unique.

def find_children(string):
    children_list =[]
    mother_list =[]
    for char in string:
        if char.isupper():
            mother_list.append(char)
        else:
            children_list.append(char)
    children_list.sort()
    for char in mother_list:
        children_list.insert(children_list.index(char.lower()), char)
    return ''.join(children_list)


print(find_children("abBA") == "AaBb")
print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
print(find_children("CbcBcbaA") == "AaBbbCcc")
print(find_children("xXfuUuuF") == "FfUuuuXx")
print(find_children("") == "")
