A = float(input("Введите размер стипендии в рублях: "))
B = float(input("Введите расходы на проживание в месяц в рублях: "))
monthly_expenses = B
total_expenses = 0

for i in range(10):
    total_expenses += monthly_expenses
    monthly_expenses *= 1.03

total_money_needed = total_expenses - 10 * A
print(f"Общая сумма денег, которую нужно попросить у родителей: {total_money_needed:.2f} руб.")