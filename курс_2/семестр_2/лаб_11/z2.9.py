temperatures = [float(input()) for _ in range(15)]

below_zero_count = 0
for temperature in temperatures:
    if temperature < 0:
        below_zero_count += 1

print("Количество дней с температурой ниже 0° С:", below_zero_count)