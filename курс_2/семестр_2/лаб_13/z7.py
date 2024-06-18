def variant_6():
  text = input("Введите строку: ")
  words = text.split()
  min_length = len(words[0])
  for word in words:
    if len(word) < min_length:
      min_length = len(word)
  print("Длина самого короткого слова:", min_length)