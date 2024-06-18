initial_amoebas = 1  # начальное количество амеб
hours = 24  # общее количество часов
amoebas = initial_amoebas
time = 3  # начальное время (через каждые 3 часа амеба делится)

print("Количество амеб через каждые 3 часа:")
while time <= hours:
    amoebas *= 2
    print(f"Через {time} часов: {amoebas} амеб")
    time += 3
