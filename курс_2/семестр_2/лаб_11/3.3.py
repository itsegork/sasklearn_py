numbers = [float(input()) for _ in range(15)]

max_element = max(numbers)

max_index = numbers.index(max_element)

numbers[-1], numbers[max_index] = numbers[max_index], numbers[-1]

print(numbers)