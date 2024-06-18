n = 30
sum_of_squares = 0
count = 1
even_number = 2

while count <= n:
    sum_of_squares += even_number ** 2
    count += 1
    even_number += 2

print("Сумма квадратов первых", n, "четных чисел натурального ряда равна:", sum_of_squares)
