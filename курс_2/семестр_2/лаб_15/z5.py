def сумма_и_произведение(список):
  if len(список) == 0:
    print("Сумма: 0, Произведение: 0")
  else:
    сумма = sum(список)
    произведение = 1
    for i in список:
      произведение *= i
    print("Сумма:", сумма, "Произведение:", произведение)

список_чисел = list(map(float, input("Введите список чисел через пробел: ").split()))
сумма_и_произведение(список_чисел)