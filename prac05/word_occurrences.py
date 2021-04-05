
user_text = str(input("Text: "))

text_words = {}
words = user_text.split()
for word in words:
    amount = text_words.get(word, 0)
    text_words[word] = amount + 1

words = list(text_words.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, text_words[word]))