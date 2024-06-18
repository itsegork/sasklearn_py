n = 40
sum_of_squares = 0
count = 1
odd_number = 1

while count <= n:
    sum_of_squares += odd_number ** 2
    count += 1
    odd_number += 2

print("Сумма квадратов первых", n, "нечетных чисел натурального ряда равна:", sum_of_squares)
