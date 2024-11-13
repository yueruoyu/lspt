# It is quite common to find yourself in a situation where you need to perform a search on some data to find something you're looking for. Imagine that you need to search through an old-fashioned phone book. Back in the day, phone books were printed every year by phone companies. The phone books contained an alphabetical list (by last name) of every customer, together with their phone number. A straightforward way to search the phone book would be to go through the phone book one name at a time, checking whether the current name is the one you're trying to find.

# This may be a simple and easy way to search, but it's not very efficient. In the worst case scenario, it could mean having to search through every single name in the book, and some phone books could be over 1000 pages. A linear search such as this can take quite a long time.

# A binary search is a much more efficient alternative. This algorithm lets you cut the search area in half on each iteration by discarding the half that you know your search term doesn't exist in. The binary search algorithm is able to do this by relying on the data being sorted. Going back to the phone book example, let's say that we're searching the following phone_book data for the search item 'Smith':

# Copy Code
# # Phone book data
# phone_book = [
#     'Embry',
#     'Hanson',
#     'Hawkins',
#     'John',
#     'Lee',
#     'Seeli',
#     'Smith',
#     'Zimmer',
# ]
# With a linear search, we would have to sequentially go through each of the names until we found the search item, 'Smith'. In a binary search, however, the following sequence happens:

# Retrieve the middle value from the data (assume truncation to integer) --> 'John'.
# If the middle value is equal to 'Smith', stop the search.
# If the middle value is less than 'Smith':
# Discard the lower half, including the middle value --> `['Embry', 'Hanson', 'Hawkins', 'John'].
# Repeat the process from the top, using the upper half as the starting data --> ['Lee', 'Seeli', 'Smith', 'Zimmer'].
# If the middle value is greater than 'Smith', do the same as the previous step, but with opposite halves.
# Using the process described above, the search successfully ends on the third iteration when the middle value is 'Smith'. For an 8-element list like this, we need, at most, 3 iterations. For an 8000-element list, we need, at most, just 13 iterations. For 8,000,000 elements, we need just 23 iterations. This is incredibly efficient.

# Implement a binary_search function that takes a list and a search item as arguments, and returns the index of the search item if found, or -1 otherwise. You may assume that the list argument will always be sorted.

# ExamplesCopy Code
# # All of these examples should print True


# def binary_search(lst, target):
#     try:
#         if lst == []:
#             return "Hello"
#         if lst[len(lst) // 2] == target:
#             return len(lst) // 2
#         elif lst[len(lst) // 2] > target:
#             print(lst[:len(lst)//2])
#             return binary_search(lst[:len(lst)//2], target)
#         else:
#             print(lst[len(lst)//2 + 1:])
#             return (len(lst) // 2 + 1 + binary_search(lst[len(lst)//2 + 1:], target))
#     except TypeError:
#         return -1

def binary_search(lst, term):
    if len(lst) > 1:
        check = len(lst) // 2
        test = lst[check]
        if test == term:
            return check
        if test < term:
            if binary_search(lst[check:], term) == -1:
                return -1
            else:
                return check + binary_search(lst[check:], term)
        if test > term:
            if binary_search(lst[:check], term) == -1:
                return -1
            else:
                return binary_search(lst[:check], term)
    if lst[0] == term:
        return 0
    return -1

businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77))
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)