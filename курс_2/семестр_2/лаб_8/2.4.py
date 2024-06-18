string = input("Введите строку: ")
count_star = 0
count_semicolon = 0

for char in string:
    if char == "*":
        count_star += 1
    elif char == ";":
        count_semicolon += 1

print(f"Количество символов '*': {count_star}")
print(f"Количество символов ';': {count_semicolon}")