"""



"""

word_to_count = {}

text = input("Text: ")

words = text.split()

for word in words:
    count_word = word_to_count.get(word,0)
    word_to_count[word] = count_word + 1

#  Creates list from dictionary and sorts
words = list(word_to_count.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
