def variant_10():
  text = input("Введите строку: ")
  char_counts = {}
  for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1
  max_count = max(char_counts.values())
  print("Максимальное количество повторений:", max_count)

variant_10()