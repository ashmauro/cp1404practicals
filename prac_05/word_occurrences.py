"""
CP1404/CP5632 Practical
word occurrences
"""
# Text: this is a collection of words of nice words this is a fun thing it is
text = input("Text: ")
words = text.split()

word_count_dict = {}

for word in words:  # for loop to create a dictionary of all words and their count
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

#  Creates list from dictionary keys and sorts
words = list(word_count_dict.keys())
words.sort()

max_length = max(len(word) for word in words)  # max length of word for dynamic formatting
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count_dict[word]))
