x = [int(input()) for _ in range(14)]

print("Номера элементов, удовлетворяющих условию 0 < X(i) < 1:")
for i, x_i in enumerate(x):
    if 0 < x_i < 1:
        print(i + 1)