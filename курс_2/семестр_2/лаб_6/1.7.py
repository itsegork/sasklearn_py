total_sum = 0

for number in range(7, 38):
    if number % 2 != 0:
        total_sum += number**3

print(f"Сумма кубов нечетных чисел от 7 до 37 составляет: {total_sum}")