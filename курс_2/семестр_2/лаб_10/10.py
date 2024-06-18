sequence = input("Введите непустую последовательность символов: ")

desired_chars = set("0123456789+-*/")

digits_arithmetic_set = set(char for char in sequence if char in desired_chars)

print("Множество цифр и знаков арифметических операций:", digits_arithmetic_set)
