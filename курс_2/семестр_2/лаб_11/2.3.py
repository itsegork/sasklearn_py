sequence = [int(input()) for _ in range(16)]

even_list = []
for i in range(0, len(sequence), 2):
    even_list.append(sequence[i])

print("Список значений под четными номерами:", even_list)