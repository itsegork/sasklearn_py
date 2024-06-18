n = int(input("Введите количество студентов: "))
students = {}
for i in range(n):
  surname, speciality, group = input(f"Введите данные студента {i+1}: ").split()
  students[surname] = (speciality, group)

speciality_query = input("Введите название специальности: ")

surnames = []
for surname, (speciality, group) in students.items():
  if speciality == speciality_query:
    surnames.append(surname)

if surnames:
  print("Фамилии студентов:", ", ".join(surnames))
else:
  print("Проверьте запрос")