aa= int(input("Введите: "))
a = [float(input()) for _ in range(20)]

negative_count = 0
for x in a:
    if x < 0:
        negative_count += 1

print("Количество отрицательных элементов:", negative_count)