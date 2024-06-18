filename = input("Введите имя файла: ")

# Разделяем имя файла по точке (.) и берем последний элемент
extension = filename.split(".")[-1]

print("Расширение файла:", extension)

