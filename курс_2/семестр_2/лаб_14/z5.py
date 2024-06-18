n = int(input("Введите количество сотрудников: "))
vacation_schedule = {}
for i in range(n):
  surname, day, month = input(f"Введите данные о сотруднике {i+1}: ").split()
  vacation_schedule[surname] = (day, month)

month_query = input("Введите название месяца: ")

surnames = []
for surname, (day, month) in vacation_schedule.items():
  if month == month_query:
    surnames.append(surname)

if surnames:
  print("Сотрудники в отпуске:", " ".join(surnames))
else:
  print("")