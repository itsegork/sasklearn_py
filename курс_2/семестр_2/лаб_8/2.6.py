string = input("Введите строку: ")
new_string = string.replace("_", "")
length_of_new_string = len(new_string)

print(f"Сформированный текст: {new_string}")
print(f"Длина сформированного текста: {length_of_new_string}")