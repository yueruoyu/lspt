# Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

# ExamplesCopy Code
# # All of these examples should print True

def word_sizes(string):
    word_list = string.split()
    count_dict = {}
    for word in word_list:
        real_word = ''
        for char in word:
            if char.isalpha():
                real_word += char
        count_dict[len(real_word)] = count_dict.get(len(real_word), 0) + 1
    return count_dict


string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})