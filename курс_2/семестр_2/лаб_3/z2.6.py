a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

count_positive = 0
if a > 0:
    count_positive += 1
if b > 0:
    count_positive += 1
if c > 0:
    count_positive += 1

print(f"count_positive = {count_positive}")