# Create a program that reads any sentenceand says if it is a palindrome, disregarding
# the spaces.

sentence = str(input("Enter here your sentence: ")).replace(" ", "").lower()

sentence_length = len(sentence)

inverse_sentence = sentence[::-1]

# for letter in range(sentence_length - 1, -1, -1):
#     inverse_sentence += sentence[letter]

print("The inverse of the sentence {} is {}".format(sentence, inverse_sentence))
print(
    "This sentence is a palindrome."
    if sentence == inverse_sentence
    else "This sentence is not a palindrome."
)
