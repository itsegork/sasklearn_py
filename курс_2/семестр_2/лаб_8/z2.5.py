string = input("Введите строку: ")
index_of_colon = string.find(":")

if index_of_colon != -1:
    count_chars_before_colon = index_of_colon
    print(f"Количество символов перед двоеточием: {count_chars_before_colon}")
else:
    print("В строке нет двоеточия")