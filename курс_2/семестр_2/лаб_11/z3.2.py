numbers = [int(input()) for _ in range(10)]

min_element = min(numbers)

min_index = numbers.index(min_element)

numbers[-1], numbers[min_index] = numbers[min_index], numbers[-1]

print(numbers)