numbers = [float(input()) for _ in range(12)]
min_element = min(numbers)

min_index = numbers.index(min_element)

numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print(numbers)