def variant_1():
  text = input("Введите строку: ")
  words = text.split()
  result = []
  for word in words:
    result.append('-'.join(word.upper()))
  print("Результат:", ' '.join(result))