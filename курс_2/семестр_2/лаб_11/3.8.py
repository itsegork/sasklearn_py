numbers = [float(input()) for _ in range(12)]

negative_numbers = []
positive_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)
    else:
        positive_numbers.append(number)

numbers = negative_numbers + positive_numbers

print(numbers)