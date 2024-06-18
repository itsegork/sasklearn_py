n = 40
total_sum = 0

for i in range(1, n+1):
    odd_number = 2*i - 1
    total_sum += odd_number**2

print(f"Сумма квадратов первых {n} нечетных чисел натурального ряда равна: {total_sum}")