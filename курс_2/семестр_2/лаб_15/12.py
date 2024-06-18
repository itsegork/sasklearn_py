def process_list(numbers, a, b, c):

  sum_other_numbers = 0
  for number in numbers:
    if a < number < b and number % c == 0:
      print(number)
    else:
      sum_other_numbers += number

  print("Сумма остальных элементов:", sum_other_numbers)

numbers = [1, 5, 8, 12, 15, 20, 25, 30]
a = 5
b = 20
c = 3

process_list(numbers, a, b, c)