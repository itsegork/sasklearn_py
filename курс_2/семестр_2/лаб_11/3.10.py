numbers = [int(input()) for _ in range(12)]

zeros = []
ones = []
for number in numbers:
    if number == 0:
        zeros.append(number)
    else:
        ones.append(number)

numbers = zeros + ones

print(numbers)