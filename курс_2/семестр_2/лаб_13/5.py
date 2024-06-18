def variant_4():
  numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
  start, end = map(int, input("Введите начальный и конечный индексы (через пробел): ").split())
  product = 1
  for i in range(start, end+1):
    product *= numbers[i]
  print("Произведение:", product)

variant_4()