n = 25
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

sum = 0
product = 1

index = 0
while index < n:
    sum += numbers[index]
    product *= numbers[index]
    index += 1

print("Сумма чисел:", sum)
print("Произведение чисел:", product)

