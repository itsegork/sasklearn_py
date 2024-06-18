n = int(input("Введите количество специальностей: "))
specialities = {}
for i in range(n):
  speciality, groups = input(f"Введите данные специальности {i+1}: ").split(" - ")
  specialities[groups] = speciality

group_query = input("Введите номер группы: ")

if group_query in specialities:
  print("Специальность:", specialities[group_query])
else:
  print("")