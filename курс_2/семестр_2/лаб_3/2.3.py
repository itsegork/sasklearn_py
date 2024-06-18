x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

if x < y:
    x = (x + y) / 2
    y = 2 * x * y
else:
    y = (x + y) / 2
    x = 2 * x * y

print(f"x = {x}")
print(f"y = {y}")