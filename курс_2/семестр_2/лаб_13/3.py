def variant_2():
  text = input("Введите строку: ")
  char_counts = {}
  for char in text:
    char_counts[char.lower()] = char_counts.get(char.lower(), 0) + 1
  max_count = max(char_counts.values())
  print("Максимальное количество повторений:", max_count)

variant_2()