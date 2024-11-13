# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

# ExampleCopy Code

def count_occurrences(lst):
    count_dict = {}
    for ele in lst:
        count_dict[ele] = count_dict.get(ele, 0) + 1
    for k, v in count_dict.items():
        print(f"{k} => {v}")






vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
# Expected OutputCopy Code
# # your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2