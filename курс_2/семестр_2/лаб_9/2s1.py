# Считываем слово от пользователя
word = input("Введите слово: ")

# Проверяем, достаточно ли букв в слове для вывода четвертой буквы
if len(word) >= 4:
    fourth_letter = word[3]
    print(f"Четвертая буква: {fourth_letter}")
else:
    print("НЕТ")
