numbers = [int(input()) for _ in range(10)]

positive_numbers = []
negative_numbers = []
for number in numbers:
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

numbers = positive_numbers + negative_numbers

print(numbers)