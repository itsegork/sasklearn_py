def add_numbers_to_list(numbers_string, list1):

  numbers = numbers_string.split(';')
  for number in numbers:
    list1.append(int(number))
  return list1

numbers_string = input("Введите строку с числами (через точку с запятой): ")
list1 = list(map(int, input("Введите элементы списка через пробел: ").split()))

print(add_numbers_to_list(numbers_string, list1))