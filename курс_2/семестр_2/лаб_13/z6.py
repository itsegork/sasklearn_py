def variant_5():
  numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
  start, end = map(int, input("Введите начальный и конечный индексы (через пробел): ").split())
  sum_squares = sum([number*2 for number in numbers[start:end+1]])
  print("Сумма квадратов:", sum_squares)