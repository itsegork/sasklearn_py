set1_str = input("Введите элементы первого множества через пробел: ")
set2_str = input("Введите элементы второго множества через пробел: ")


set1 = set(int(x) for x in set1_str.split())
set2 = set(int(x) for x in set2_str.split())

# 1) Все различные числа в множествах
all_numbers = set1 | set2  # Объединение множеств
print("Все различные числа:", all_numbers)

# 2) Общие числа в множествах
common_numbers = set1 & set2  # Пересечение множеств
common_numbers = sorted(common_numbers)  # Сортировка по возрастанию
print("Общие числа в порядке возрастания:", common_numbers)
