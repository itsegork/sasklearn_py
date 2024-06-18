k = 3
start = 1000  # начальное 4-значное число
end = 10000  # конечное 4-значное число
total_sum = 0
number = start

while number <= end:
    if number % k == 0:
        total_sum += number
    number += 1

print("Сумма всех 4-значных чисел, кратных", k, ":", total_sum)
