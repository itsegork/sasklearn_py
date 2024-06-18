m = float(input("Введите массу первого пакета: "))
n = float(input("Введите массу второго пакета: "))

if m > n:
    mass_heavier = m
else:
    mass_heavier = n

print(f"Масса более тяжелого пакета: {mass_heavier}")