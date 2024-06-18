import math


def func9(x):
    return math.log(1 + x) / (1 - x)

x = float(input("Введите x: "))
y = func9(x)
print(f"y = {y}")