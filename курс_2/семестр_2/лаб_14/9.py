list1 = input("Введите элементы первого списка, разделенные пробелами: ").split()
list2 = input("Введите элементы второго списка, разделенные пробелами: ").split()

if len(list1) != len(list2):
  print("Списки должны быть одинаковой длины")
else:
  dictionary = dict(zip(list1, list2))
  print(dictionary)