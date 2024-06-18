a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if a >= 0:
    a = a*2
else:
    a = a*4
if b >= 0:
    b = b*2
else:
    b = b*4
if c >= 0:
    c = c*2
else:
    c = c*4

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
