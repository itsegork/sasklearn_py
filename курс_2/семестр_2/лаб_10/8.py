sequence = input("Введите непустую последовательность символов: ")

desired_chars = set("EFGHIJKLMNOP.,?!:;")

result_set = set(char for char in sequence if char in desired_chars)

print("Множество символов от 'E' до 'N' и знаков препинания:", result_set)
