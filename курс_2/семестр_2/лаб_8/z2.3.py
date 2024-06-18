string = input("Введите строку: ")
count_r = 0
count_t = 0

for char in string:
    if char == "r":
        count_r += 1
    elif char == "t":
        count_t += 1

print(f"Количество символов 'r': {count_r}")
print(f"Количество символов 't': {count_t}")