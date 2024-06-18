# Считываем две строки от пользователя
first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")

# Проверяем условие
if first_string[-1] == second_string[0]:
    print("ВЕРНО")
else:
    print("НЕВЕРНО")
