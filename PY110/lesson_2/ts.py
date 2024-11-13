lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
def check_even(dictionary):
    result = [p for ele in dictionary.values()
                for p in ele
                if p % 2 == 1]
    return result == []

print([dicts for dicts in lst if check_even(dicts)]) 