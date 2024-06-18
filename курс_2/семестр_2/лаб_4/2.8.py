import math


def func8(t):
    return math.cos(2 * math.pi * t) * math.sin(2 * math.pi * t) / (1 + math.cos(2 * math.pi * t) * math.sin(2 * math.pi * t))

t = float(input("Введите t: "))
y = func8(t)
print(f"y = {y}")