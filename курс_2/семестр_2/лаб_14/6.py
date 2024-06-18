n = int(input("Введите количество стран: "))
countries = {}
for i in range(n):
  country, cities = input(f"Введите данные о стране {i+1}: ").split(" - ")
  countries[cities.split(", ")] = country

city_query = input("Введите название города: ")

for cities in countries.keys():
  if city_query in cities:
    print("Страна:", countries[cities])
    break
else:
  print("")