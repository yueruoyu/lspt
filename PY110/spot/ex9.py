# Write a function that generates text following a pattern where:
# 1) the first and last characters of each word remain in their original place
# 2) characters between the first and last characters are sorted alphabetically
# 3) punctuation should remain at the same place as it started

# Examples:


def scramble_words(sentence):
    return ' '.join([transform(word) for word in sentence.split()])

def transform(word):
    alpha_list =[]
    for char in word:
        if char.isalpha():
            alpha_list.append(char)
    sorted_list = list(reversed([alpha_list[0]] + 
        sorted(alpha_list[1:-1]) + [alpha_list[-1]]))
    return_lst = []
    for char in word:
        if not char.isalpha():
            return_lst.append(char)
        else:
            return_lst.append(sorted_list.pop())
    return ''.join(return_lst)


print(scramble_words('professionals')) # should return 'paefilnoorsss'
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.")) # "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")