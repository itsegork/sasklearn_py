text = input("Введите строку слов: ")

words = text.split()  # Разделяем строку на список слов
longest_word = ""      # Инициализируем переменную для самого длинного слова
max_length = 0         # Инициализируем переменную для максимальной длины

for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

print("Самое длинное слово:", longest_word)
