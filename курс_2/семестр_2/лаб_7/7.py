import random
numbers = [random.randint(-10, 10) for _ in range(10)]
for number in numbers:
    if number < 0:
        continue
    elif number == 0:
        break
    else:
        print(number ** 0.5)