import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))
y = math.cos(x * b) * a + (x * b) * 3
print(f"a = {a}")
print(f"b = {b}")
print(f"x = {x}")
print(f"y = {y}")
print(f"Целая часть y: {int(y)}")