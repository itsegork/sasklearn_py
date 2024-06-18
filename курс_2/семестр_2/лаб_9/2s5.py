text = input("Введите строку: ")

result = ""
for char in text:
    if char not in result and char != " ":
        result += char

print("Результат:", result)
