import math


def func6(x):
    return math.exp(x) * math.sin(2.8 * x) / (1 + math.cos(6 * math.pi * x))

x = float(input("Введите x: "))
y = func6(x)
print(f"y = {y}")