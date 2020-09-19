with open('bag_of_words.txt') as word_file:
    words = list(set(word_file.read().split('\n')))
