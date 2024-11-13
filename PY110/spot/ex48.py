# Your task is to Reverse and Combine Words.
# Input: String containing different "words" separated by spaces
# 1. More than one word? Reverse each word and combine first with second, third with fourth and so on...
# (odd number of words => last one stays alone, but has to be reversed too)
# 2. Start it again until there's only one word without spaces
# 3. Return your result…

def reverse_and_combine_text(string):
    result = []
    word_list = string.split()
    if len(word_list) == 1:
        return string
    if len(word_list) == 2:
        return word_list[0][::-1] + word_list[1][::-1]
    for i in range(0, len(word_list)-1, 2):
        result.append(word_list[i][::-1] + word_list[i+1][::-1])
    if len(word_list) % 2 == 1:
        result.append(word_list[-1][::-1])
    return reverse_and_combine_text(' '.join(result))





print(reverse_and_combine_text("abc def") == "cbafed")
print(reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi")
print(reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed")
print(reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44")) 
# trzwqfdstrteettr45hh4325543544hjhjh21lllll")
print(reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt"))
# "gffds432243fdsfdseewttf")