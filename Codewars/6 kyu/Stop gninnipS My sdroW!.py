def spin_words(sentence):
    sentence_split = sentence.split()
    result = []
    for word in sentence_split:
        if len(word) > 4:
            spinned_word = ''
            for char in word[::-1]:
                spinned_word+=char
            result.append(spinned_word)
        else:
            result.append(word)
    return ' '.join(result)

print(spin_words("Welcome"))


"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""
