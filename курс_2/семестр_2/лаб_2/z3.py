import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
t = float(input("Введите значение t: "))
x = b * math.atan(t) - a
print(f"a = {a}")
print(f"b = {b}")
print(f"t = {t}")
print(f"x = {x}")
print(f"Целая часть x: {int(x)}")