def variant_7():
  text = input("Введите строку: ")
  words = text.split()
  result = []
  for word in words[::-1]:
    result.append('+'.join(word))
  print("Результат:", ' '.join(result))