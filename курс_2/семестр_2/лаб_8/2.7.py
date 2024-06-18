string = input("Введите строку с двоеточием:")
old_string_length = len(string)
new_string = string.replace(":", "")
new_string_length = len(new_string)

count_removed_chars = old_string_length - new_string_length
print(f"Количество удалённых символов: {count_removed_chars}")