sequence = input("Введите непустую последовательность символов: ")

desired_chars = set("ABCDEFXYZ")

letters_set = set(char for char in sequence if char in desired_chars)

print("Множество букв от 'A' до 'F' и от 'X' до 'Z':", letters_set)
