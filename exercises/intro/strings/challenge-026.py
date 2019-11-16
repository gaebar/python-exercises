# Challenge 026
word = input("Enter a word: ")
first_word = word[0]
length = len(word)
rest = word[1:length]
if first_word != "a" and first_word != "e" and first_word != "i" and first_word != "o" and first_word != "u":
    new_word = rest + first_word + "ay"
else:
    new_word = word + "way"
print(new_word.lower())
