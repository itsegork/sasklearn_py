sequence = input("Введите непустую последовательность символов: ")
unique_digits = set()
for char in sequence:
    if char.isdigit():
        unique_digits.add(char)  # Добавляем цифру в множество

print("unique_digits:", unique_digits)
