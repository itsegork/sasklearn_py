# Ввод данных
A = float(input("Введите размер ежемесячной стипендии A: "))
B = float(input("Введите расходы на проживание B: "))

# Вычисление суммы денег, необходимых на весь учебный год
total_money = A  # Изначально у нас есть только стипендия
months = 0  # Счетчик месяцев

while months < 10:  # Продолжаем считать до конца учебного года (10 месяцев)
    total_money += B
    B *= 1.03  # Увеличиваем расходы на 3% каждый месяц
    months += 1

print("Сумма денег, необходимых на весь учебный год:", total_money)
