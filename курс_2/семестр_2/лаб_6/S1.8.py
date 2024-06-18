n = 30
total_sum = 0

for i in range(1, n+1):
    even_number = 2*i
    total_sum += even_number**2

print(f"Сумма квадратов первых {n} четных чисел натурального ряда равна: {total_sum}")