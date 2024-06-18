m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

if m != n:
    if m > n:
        m = n = m
    else:
        m = n = n
else:
    m = n = 0

print(f"m = {m}")
print(f"n = {n}")