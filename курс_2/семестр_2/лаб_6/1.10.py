lower_limit = 6
upper_limit = 36
total_sum = 0

for i in range(lower_limit, upper_limit+1):
    if i % 2 == 0:
        total_sum += i**3

print(f"Сумма кубов четных чисел от {lower_limit} до {upper_limit} равна: {total_sum}")