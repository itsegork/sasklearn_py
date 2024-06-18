import math


def func1(t):
    if 0.5 <= t <= 1:
        return math.cos(2 * math.pi * t)
    else:
        return math.log(7) / 7

t = float(input("Введите t: "))
y = func1(t)
print(f"y = {y}")