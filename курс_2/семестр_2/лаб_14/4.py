n = int(input("Введите количество записей в словаре: "))
dictionary = {}
for i in range(n):
  word, definition = input(f"Введите запись {i+1}: ").split(" - ")
  dictionary[word] = definition

word_query = input("Введите слово: ")

if word_query in dictionary:
  print("Описание:", dictionary[word_query])
else:
  print("Нет в словаре")