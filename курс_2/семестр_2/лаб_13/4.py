def variant_3():
  numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
  start, end = map(int, input("Введите начальный и конечный индексы (через пробел): ").split())
  sum_numbers = sum(numbers[start:end+1])
  print("Сумма:", sum_numbers)

variant_3()