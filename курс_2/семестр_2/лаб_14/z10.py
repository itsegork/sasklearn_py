n = int(input("Введите количество одноклассников: "))
birthdays = {}
for i in range(n):
  name, day, month = input(f"Введите данные о однокласснике {i+1}: ").split()
  birthdays[name] = (day, month)

month_query = input("Введите название месяца: ")

results = []
for name, (day, month) in birthdays.items():
  if month == month_query:
    results.append(f"{name} ({day})")

if results:
  print("Имена одноклассников и дни рождения:", " ".join(results))
else:
  print("")