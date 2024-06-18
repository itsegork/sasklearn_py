n = 15
numbers = []

for i in range(n):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

sum_numbers = sum(numbers)
prod_numbers = 1
for num in numbers:
    prod_numbers *= num

print(f"Сумма чисел: {sum_numbers}")
print(f"Произведение чисел: {prod_numbers}")