import numpy as np

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Запрашиваем элементы матрицы
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Введите элемент [{i}, {j}]: ")))
    matrix.append(row)

# Выводим исходную матрицу
print("Исходная матрица:")
for row in matrix:
    print(row)

# Выполняем различные операции с матрицей в зависимости от варианта задания
variant = int(input("Введите номер варианта задания (1-10): "))
result = None

if variant == 1:
    # Сумма элементов каждого столбца
    result = [sum(row[i] for row in matrix) for i in range(cols)]
    print("Сумма элементов каждого столбца:")
    print(result)

elif variant == 2:
    # Сумма элементов каждой строки
    result = [sum(row) for row in matrix]
    print("Сумма элементов каждой строки:")
    print(result)

elif variant == 3:
    # Сумма положительных элементов под главной диагональю и на ней
    result = 0
    for i in range(rows):
        for j in range(i + 1):
            result += matrix[i][j]
    print("Сумма положительных элементов под главной диагональю и на ней:")
    print(result)

elif variant == 4:
    # Сумма отрицательных элементов над главной диагональю
    result = 0
    for i in range(rows):
        for j in range(i):
            result += matrix[i][j]
    print("Сумма отрицательных элементов над главной диагональю:")
    print(result)

elif variant == 5:
    # Сумма положительных элементов над дополнительной диагональю
    result = 0
    for i in range(rows):
        for j in range(cols - i - 1):
            result += matrix[i][j]
    print("Сумма положительных элементов над дополнительной диагональю:")
    print(result)

elif variant == 6:
    # Сумма отрицательных элементов под дополнительной диагональю
    result = 0
    for i in range(rows):
        for j in range(cols - i):
            result += matrix[i][j]
    print("Сумма отрицательных элементов под дополнительной диагональю:")
    print(result)

elif variant == 7:
    # Число элементов, кратных k
    k = int(input("Введите k: "))
    result = 0
    for row in matrix:
        for element in row:
            if element % k == 0:
                result += 1
    print("Число элементов, кратных {}:".format(k))
    print(result)

elif variant == 8:
    # Упорядочивание элементов каждой строки по возрастанию
    for row in matrix:
        row.sort()
    print("Упорядоченная матрица:")
    for row in matrix:
        print(row)

elif variant == 9:
    # Замена отрицательных элементов на нули
    for row in matrix:
        for i in range(len(row)):
            if row[i] < 0:
                row[i] = 0
    print("Матрица с замененными отрицательными элементами на нули:")
    for row in matrix:
        print(row)

elif variant == 10:
    # Минимальный элемент и его индексы
    min_element = matrix[0][0]
    min_row = 0
    min_col = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_row = i
                min_col = j
    print("Минимальный элемент:")
    print(min_element)
    print("Индексы минимального элемента:")
    print(min_row, min_col)

elif variant == 8:
    # Упорядочивание элементов каждой строки по возрастанию
    result = np.sort(matrix, axis=1)
    print("Упорядоченная матрица:")
    print(result)

elif variant == 9:
    # Замена отрицательных элементов на нули
    matrix[matrix < 0] = 0
    print("Матрица с замененными отрицательными элементами на нули:")
    print(matrix)

elif variant == 10:
    # Минимальный элемент и его индексы
    min_element = np.min(matrix)
    min_row, min_col = np.where(matrix == min_element)
    print("Минимальный элемент:")
    print(min_element)
    print("Индексы минимального элемента:")
    print(min_row[0], min_col[0])

else:
    print("Неверный вариант задания.")