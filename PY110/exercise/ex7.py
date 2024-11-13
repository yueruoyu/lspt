# Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

# ExamplesCopy Code


def swap(string):
      word_lst = string.split()
      for idx in range(len(word_lst)):
            if len(word_lst[idx]) >= 2:
                  word_lst[idx] = (word_lst[idx][-1] + 
                        word_lst[idx][1:-1] + 
                        word_lst[idx][0])
      return ' '.join(word_lst)





print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
