import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))
y = (1 / (x * 2)) * math.sin((x * 2) + b - x + a)
print(f"a = {a}")
print(f"b = {b}")
print(f"x = {x}")
print(f"y = {y}")
print(f"Целая часть y: {int(y)}")