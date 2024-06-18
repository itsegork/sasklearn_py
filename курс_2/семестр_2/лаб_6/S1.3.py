x = 10
daily_distance = x
total_distance = x

for i in range(1, 7):
    daily_distance *= 1.1
    total_distance += daily_distance

print(f"Суммарный путь за неделю: {total_distance} км")