a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

count_two_digit = 0
if 10 <= a <= 99:
    count_two_digit += 1
if 10 <= b <= 99:
    count_two_digit += 1
if 10 <= c <= 99:
    count_two_digit += 1

print(f"count_two_digit = {count_two_digit}")