string = input("Введите строку: ")
index_of_semicolon = string.find(";")

if index_of_semicolon != -1:
    count_chars_after_semicolon = len(string) - index_of_semicolon - 1
    print(f"Количество символов после точки с запятой: {count_chars_after_semicolon}")
else:
    print("В строке нет точки с запятой")