input_string = input("Введите строку, содержащую английский текст: ")
words = input_string.split()
count = 0
for word in words:
    if word[0].lower() == "b":
        count += 1
print("Количество слов, начинающихся с буквы b:", count)