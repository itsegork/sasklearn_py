text = input("Введите последовательность символов: ")


unique_chars = set()


for char in text:
    if char in "+-*/%=()[]{}<>,.?!;:'\"":
        unique_chars.add(char)
print("Множество уникальных символов:", unique_chars)
