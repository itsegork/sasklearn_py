def variant_9():
  text = input("Введите строку: ")
  letters = ''.join(text.lower().split())
  result = ':'.join(sorted(letters))
  print("Результат:", result)

variant_9()