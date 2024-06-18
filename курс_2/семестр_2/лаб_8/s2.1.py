def count_words_in_string(s):

    words = s[:-1].split()
    return len(words)


s = "Дана строка, заканчивающаяся точкой."
word_count = count_words_in_string(s)
print("Количество слов в строке:", word_count)