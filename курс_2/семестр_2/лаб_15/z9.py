def get_day_name(day_number, language):

  days_ru = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
  days_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if language == "русский":
    return days_ru[day_number - 1]
  elif language == "английский":
    return days_en[day_number - 1]
  else:
    return "Неверный язык"

day_number = int(input("Введите номер дня недели: "))
language = input("Введите язык (русский/английский): ")

print(get_day_name(day_number, language))