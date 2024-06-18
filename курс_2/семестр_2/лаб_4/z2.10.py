import math


def func10(x):
    return (math.cos(2 * math.pi * x) * math.sin(2 * math.pi * x)) / (1 / (math.log(x + 1)) + x*2 + x*3)

x = float(input("Введите x: "))
y = func10(x)
print(f"y = {y}")