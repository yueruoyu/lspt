# Given a dictionary, return its keys sorted by the values associated with each key.

# ExampleCopy Code
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']

def order_by_value(dictionary):
    return sorted(list(dictionary.keys()), key=dictionary.get)

print(order_by_value(my_dict) == keys)  # True