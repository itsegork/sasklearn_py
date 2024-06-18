first_row = input("Введите первую строку: ")

numbers = first_row.split()

matrix = [
    [int(number) for number in numbers]
]

num_repetitions = int(input("Сколько раз повторить матрицу: "))
for _ in range(num_repetitions - 1):
    matrix.append([number for number in reversed(numbers)])

    matrix.append([int(number) for number in numbers])

for row in matrix:
    for number in row:
        print(number, end=" ")
    print()