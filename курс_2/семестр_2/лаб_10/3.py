text = input("Введите последовательность символов: ")

unique_chars = set()

for char in text:
    if 'A' <= char <= 'Z' or '0' <= char <= '5':
        unique_chars.add(char)
print("Множество уникальных символов:", unique_chars)
