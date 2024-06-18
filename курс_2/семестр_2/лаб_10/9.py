sequence = input("Введите непустую последовательность символов: ")

desired_chars = set("+-*/%<>=!")

arithmetic_relation_set = set(char for char in sequence if char in desired_chars)

print("Множество знаков арифметических операций и операций отношения:", arithmetic_relation_set)
