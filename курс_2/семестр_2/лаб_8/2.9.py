string = input("Введите строку с точко-запятой: ")
index_of_semicolon = string.find(";")

if index_of_semicolon != -1:
    count_chars_before_semicolon = index_of_semicolon
    print(f"Количество символов до точки с запятой: {count_chars_before_semicolon}")
else:
    print("В строке нет точки с запятой")