k = 3
total_sum = 0

for number in range(1000, 10000):
    if number % k == 0:
        total_sum += number

print(f"Сумма всех 4-значных чисел, кратных {k}, составляет: {total_sum}")