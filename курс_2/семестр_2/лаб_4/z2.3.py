def func3(x):
    return (1.2 * x*2 + 1.2 * x + 1.2) / (1 + x*2 + x*4)

x = float(input("Введите x: "))
y = func3(x)
print(f"y = {y}")