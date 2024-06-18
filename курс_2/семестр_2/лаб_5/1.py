distance = 10  # дневная норма в первый день (в км)
days = 8  # количество дней

total_distance = 0
day = 1
while day <= days:
    total_distance += distance
    distance *= 1.1  # увеличение дневной нормы на 10%
    day += 1

print("Суммарный путь за 1 неделю:", total_distance, "км")
