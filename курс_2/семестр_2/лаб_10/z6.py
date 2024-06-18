text = input("Введите последовательность символов: ")

unique_chars = set()


for char in text:
    if '5' <= char <= '9' or char in "+-*/%=":
        unique_chars.add(char)

print("Множество уникальных символов:", unique_chars)
