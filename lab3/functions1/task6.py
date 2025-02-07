def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

print(reverse_words("We are ready"))