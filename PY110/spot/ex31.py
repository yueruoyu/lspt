# Find the highest scoring word in a string.
# Each letter scores points based on its position in the alphabet: a = 1, b = 2, c = 3, ... z = 26.
# Return the highest scoring word. If two words score the same, return the word that appears earliest in the string.
def high(sentence):
    high_word =''
    high_score = 0
    for word in sentence.split():
        score = 0
        for char in word:
            score += ord(char) - ord('a') + 1
        if score > high_score:
            high_word = word
            high_score = score
    return high_word



print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak') == 'semynak')
print(high('aaa b') == 'aaa')
