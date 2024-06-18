import math


def func5(x):
    return math.exp(2.5 * x) * math.cos(math.pi * x) - math.sin(3 * math.pi * x)

x = float(input("Введите x: "))
y = func5(x)
print(f"y = {y}")