def get_day_name(day_number):

  days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
  return days[(day_number + 3) % 7]

day_number = int(input("Введите день месяца (1 - 30): "))

print(get_day_name(day_number))