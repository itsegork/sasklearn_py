start = 7
end = 37
sum_of_cubes = 0

while start <= end:
    if start % 2 != 0: # Проверяем, что число нечетное
        sum_of_cubes += start ** 3
    start += 1

print("Сумма кубов нечетных чисел от 7 до 37 равна:", sum_of_cubes)
