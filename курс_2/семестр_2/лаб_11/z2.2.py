b = [float(input()) for _ in range(20)]

positive_sum = 0
for x in b:
    if x > 0:
        positive_sum += x

print("Сумма положительных элементов:", positive_sum)