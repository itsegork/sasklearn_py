text = input("Введите строку: ")

# Удаляем пробелы
text = text.replace(" ", "")

# Проверяем, является ли строка палиндромом
is_palindrome = text == text[::-1]

if is_palindrome:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
