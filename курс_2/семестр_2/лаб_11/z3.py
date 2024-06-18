numbers = [int(input()) for _ in range(20)]

max_element = max(numbers)

max_index = numbers.index(max_element)

numbers[0], numbers[max_index] = numbers[max_index], numbers[0]

print(numbers)