def variant_8():
  text = input("Введите строку: ")
  words = text.split()
  max_length = len(words[0])
  for word in words:
    if len(word) > max_length:
      max_length = len(word)
  print("Длина самого длинного слова:", max_length)

variant_8()