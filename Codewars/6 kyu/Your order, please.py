"""Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers."""


def order(sentence):
    dict = {}
    list = []
    list_result = []
    sentence_split = sentence.split()
    for word in sentence_split:
        list.append(word)
    for word in list:
        for char in word:
            if char.isdigit():
                num = int(char)
                dict[num] = word
    list.clear()
#    for item in dict:
#        dict[item] = dict[item].replace(str(item),"")
    for key in sorted(dict.keys()):
        list.append(dict[key])
    return " ".join(list)

print(order("is2 Thi1s T4est 3a"))
