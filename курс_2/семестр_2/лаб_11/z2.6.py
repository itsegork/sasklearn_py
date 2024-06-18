z = [float(input()) for _ in range(20)]

min_positive = None
for x in z:
    if x > 0 and (min_positive is None or x < min_positive):
        min_positive = x

print("Наименьший положительный элемент:", min_positive)